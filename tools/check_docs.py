#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
# Copyright (c) 2026 kairyo and contributors
"""Read-only structural checks; not a security or content certification."""

import hashlib
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
EXPECTED = (
    "README.md", "AGENTS.md", "CONTRIBUTING.md", "CHANGELOG.md",
    "LICENSE-NOTICE.md", "THIRD-PARTY-NOTICES.md", "REVIEW.md", "VERSION",
    "docs/01-principles.md", "docs/02-exploration.md",
    "docs/03-figma-handoff.md", "docs/04-design-systems.md",
    "docs/05-apple.md", "docs/06-android.md", "docs/07-inclusive-design.md",
    "docs/08-implementation-acceptance.md", "docs/09-reference-library.md",
    "docs/10-adoption-maintenance.md", "references/sources.md",
    "templates/design-brief.md", "templates/adoption-record.md",
    "templates/verification-record.md", "examples/anonymous-cases.md",
    "examples/form-submit-recovery.md", "examples/stepped-form-branch-return.md",
    "examples/figma-variable-theme.md", "templates/landing-page-brief.md",
    "skills/README.md", "skills/review-cases.md",
    "skills/design-direction-review/SKILL.md",
    "skills/design-direction-review/agents/openai.yaml",
    "skills/adaptive-ui-review/SKILL.md",
    "skills/adaptive-ui-review/agents/openai.yaml",
    "skills/adaptive-ui-review/references/platform-sources.md",
    "README.en.md", "PROJECT_MANAGEMENT.md",
    ".github/ISSUE_TEMPLATE/documentation-change.md",
    ".github/ISSUE_TEMPLATE/validation-report.md",
    ".github/pull_request_template.md",
    "reviews/2026-11-03-github-management.md",
    "reviews/2026-11-05-figma-landing.md",
    "reviews/2026-11-06-form-validation.md",
    "reviews/2026-11-04-repository-review.md",
    "reviews/text-cases/README.md", "reviews/text-cases/inputs.json",
    "reviews/text-cases/rubric.json", "reviews/text-cases/2026-11-04-run.md",
    "tools/check_docs.py",
    "LICENSE", "tools/LICENSE",
    "skills/design-direction-review/LICENSE",
    "skills/adaptive-ui-review/LICENSE",
)
LICENSE_SHA256 = {
    "LICENSE": "9e5f1b3c610b9c2da5c313bf81d577a7d1acec686bdb0384edefa6df0f90cd94",
    "skills/design-direction-review/LICENSE": "9e5f1b3c610b9c2da5c313bf81d577a7d1acec686bdb0384edefa6df0f90cd94",
    "skills/adaptive-ui-review/LICENSE": "9e5f1b3c610b9c2da5c313bf81d577a7d1acec686bdb0384edefa6df0f90cd94",
    "tools/LICENSE": "b8bd3684691b6a6d9a73328b7fa4bf492a354dbabd1b3cea219c3e3f7f2b65ab",
}
# Exact licensing and attribution URLs, separate from the design-source registry.
LICENSE_REFERENCE_URLS = {
    "https://creativecommons.org/licenses/by/4.0/",
    "https://github.com/kairyo/design-standards",
}
SKILL_NAMES = {"design-direction-review", "adaptive-ui-review"}
CASE_GUIDANCE_FILES = {
    name for name in EXPECTED if name.startswith(("docs/", "templates/", "examples/"))
} | {
    "references/sources.md", "skills/design-direction-review/SKILL.md",
    "skills/adaptive-ui-review/SKILL.md",
    "skills/adaptive-ui-review/references/platform-sources.md",
}
ALLOWED_SOURCE_HOSTS = {
    "developer.apple.com", "developer.android.com", "help.figma.com",
    "www.w3.org", "www.designtokens.org", "github.com", "learn.chatgpt.com",
    "styledictionary.com", "react-aria.adobe.com",
}
ALLOWED_GITHUB_PATHS = {
    "/material-components/material-components-android",
    "/ant-design/ant-design/blob/46f0421cb8db963e35a41b822ceb9232d5c8ef57/docs/spec/research-form.zh-CN.md",
    "/dequelabs/axe-core/blob/6b52b841461bd23345970b91ec75fdaff6bad31a/README.md",
    "/elayadesign/ai-design-skills/blob/456d9e0d3e2d84c748bb143c6ca3d90c45e16213/skills/figma-designer/SKILL.md",
    "/elayadesign/ai-design-skills/blob/456d9e0d3e2d84c748bb143c6ca3d90c45e16213/skills/landing-page-design/SKILL.md",
    "/elayadesign/ai-design-skills/blob/456d9e0d3e2d84c748bb143c6ca3d90c45e16213/LICENSE",
}
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
REPOSITORY_GITHUB_PATH = re.compile(
    r"/kairyo/design-standards/(?:issues(?:/\d+)?|pulls|pull/\d+|milestones|milestone/\d+)"
)
URL = re.compile(r"https?://[^\s<>)\]，；。]+")
PRIVATE_PATH = re.compile(r"/(?:Users|home)/[^\s/]+/|(?:file|vscode)://")
SECRET = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}")


def check_external_urls(name, content, errors):
    for url in URL.findall(content):
        parsed = urlsplit(url)
        if url in LICENSE_REFERENCE_URLS:
            continue
        # Repository tracking links are separate from external source references.
        if (parsed.scheme == "https" and parsed.netloc.lower() == "github.com"
                and REPOSITORY_GITHUB_PATH.fullmatch(parsed.path.rstrip("/"))):
            if parsed.query or parsed.username or parsed.password:
                errors.append(f"review URL parameters/identity in {name}")
            continue
        if parsed.hostname not in ALLOWED_SOURCE_HOSTS:
            errors.append(f"unregistered external host in {name}: {parsed.hostname}")
        if parsed.hostname == "github.com" and parsed.path.rstrip("/") not in ALLOWED_GITHUB_PATHS:
            errors.append(f"unregistered GitHub reference in {name}")
        if parsed.query or parsed.username or parsed.password:
            errors.append(f"review URL parameters/identity in {name}")


def unique_json_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON object key")
        result[key] = value
    return result


def check_text_cases(text_contents, errors):
    """Check fixture correspondence only; never execute or grade responses."""
    fixtures = {}
    for name in ("inputs", "rubric"):
        path = f"reviews/text-cases/{name}.json"
        try:
            fixture = json.loads(text_contents.get(path, ""), object_pairs_hook=unique_json_object)
        except ValueError:
            errors.append(f"invalid case JSON: {path}")
            continue
        if (not isinstance(fixture, dict) or type(fixture.get("schema_version")) is not int
                or fixture["schema_version"] != 1):
            errors.append(f"invalid case schema: {path}")
            continue
        # Inspect decoded strings too: JSON escapes must not hide public URLs or paths.
        pending, strings = [fixture], []
        while pending:
            value = pending.pop()
            if isinstance(value, dict):
                pending.extend(value.keys())
                pending.extend(value.values())
            elif isinstance(value, list):
                pending.extend(value)
            elif isinstance(value, str):
                strings.append(value)
        decoded = "\n".join(strings)
        if PRIVATE_PATH.search(decoded) or SECRET.search(decoded):
            errors.append(f"potential private material: {path}")
        check_external_urls(path, decoded, errors)
        fixtures[name] = fixture
        cases = fixture.get("cases")
        if not isinstance(cases, list) or not cases:
            errors.append(f"missing case list: {path}")
            continue
        ids = []
        for case in cases:
            if not isinstance(case, dict) or not re.fullmatch(r"T[1-9]\d*", str(case.get("id", ""))):
                errors.append(f"invalid case ID: {path}")
                continue
            ids.append(case["id"])
            values = [case.get("prompt")] if name == "inputs" else case.get("required")
            if not isinstance(values, list) or not values or not all(
                    isinstance(value, str) and value.strip() for value in values):
                errors.append(f"missing case content: {path}: {case['id']}")
        if len(ids) != len(set(ids)):
            errors.append(f"duplicate case IDs: {path}")
        fixture["checked_ids"] = ids
    if set(fixtures) != {"inputs", "rubric"}:
        return
    inputs, rubric = fixtures["inputs"], fixtures["rubric"]
    if inputs.get("checked_ids") != rubric.get("checked_ids"):
        errors.append("case inputs and rubric IDs/order differ")
    if not isinstance(inputs.get("instruction"), str) or not inputs["instruction"].strip():
        errors.append("missing shared case instruction")
    files = inputs.get("specification_files")
    if not isinstance(files, list) or not files or not all(
            isinstance(name, str) and name in text_contents and name in CASE_GUIDANCE_FILES
            for name in files):
        errors.append("invalid case specification file list")
    elif len(files) != len(set(files)):
        errors.append("duplicate case specification files")
    ratings = rubric.get("ratings")
    if not isinstance(ratings, dict) or set(ratings) != {"PASS", "PARTIAL", "FAIL", "NOT_RUN"} or not all(
            isinstance(value, str) and value.strip() for value in ratings.values()):
        errors.append("invalid case rating definitions")
    failures = rubric.get("failure_conditions")
    if not isinstance(failures, list) or not failures or not all(
            isinstance(value, str) and value.strip() for value in failures):
        errors.append("missing case failure conditions")


def main():
    errors = []
    text_contents = {}
    for name in EXPECTED:
        path = ROOT / name
        if not path.is_file() or not path.stat().st_size:
            errors.append(f"missing or empty: {name}")
    actual_files = {
        path.relative_to(ROOT).as_posix()
        for path in ROOT.rglob("*")
        if path.is_file() and ".git" not in path.relative_to(ROOT).parts
    }
    for name in sorted(actual_files - set(EXPECTED)):
        errors.append(f"unexpected file; review before publication: {name}")
    for name in EXPECTED:
        path = ROOT / name
        if not path.is_file():
            continue
        if path.is_symlink() or not path.resolve().is_relative_to(ROOT):
            errors.append(f"unexpected symlink or external target: {name}")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            errors.append(f"expected UTF-8 text: {name}")
            continue
        if PRIVATE_PATH.search(content) or SECRET.search(content):
            errors.append(f"potential private material: {name}")
        if (name in LICENSE_SHA256
                and hashlib.sha256(content.encode("utf-8")).hexdigest() != LICENSE_SHA256[name]):
            errors.append(f"license text differs from reviewed copy: {name}")
        text_contents[name] = content
    check_text_cases(text_contents, errors)
    documents = sorted(
        ROOT / name for name in text_contents if name.endswith(".md")
    )
    link_count = 0
    source_ids = set()
    for path in documents:
        relative = path.relative_to(ROOT)
        content = text_contents[relative.as_posix()]
        if not content.endswith("\n"):
            errors.append(f"missing final newline: {relative}")
        if len(re.findall(r"^```", content, re.M)) % 2:
            errors.append(f"unbalanced fenced code: {relative}")
        for raw in LINK.findall(content):
            target = raw.strip("<>")
            parsed = urlsplit(target)
            if parsed.scheme:
                continue
            link_count += 1
            destination = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if not destination.is_relative_to(ROOT) or not destination.is_file():
                errors.append(f"invalid local target in {relative}: {target}")
            elif parsed.fragment and re.fullmatch(r"s\d{2}", parsed.fragment):
                heading = f"## {parsed.fragment.upper()}"
                if heading not in destination.read_text(encoding="utf-8").splitlines():
                    errors.append(f"missing source anchor in {relative}: {target}")
            if (len(relative.parts) >= 3 and relative.parts[0] == "skills"
                    and relative.parts[1] in SKILL_NAMES):
                skill_root = ROOT / "skills" / relative.parts[1]
                if not destination.is_relative_to(skill_root):
                    errors.append(f"skill-local link escapes package in {relative}: {target}")
        check_external_urls(relative, content, errors)
        if relative.as_posix() == "references/sources.md":
            matches = re.findall(r"^## (S\d{2})$", content, re.M)
            source_ids = set(matches)
            if len(matches) != len(source_ids):
                errors.append("duplicate source IDs")
    if source_ids != {f"S{i:02d}" for i in range(1, 24)}:
        errors.append("source registry must contain S01 through S23")
    if errors:
        print("FAIL\n" + "\n".join(errors))
        return 1
    print(f"PASS: {len(EXPECTED)} required files; {len(documents)} Markdown files; "
          f"{link_count} internal links; {len(source_ids)} source entries")
    print("Scope: structural checks only. Manual fact, privacy, license, and history review still required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
