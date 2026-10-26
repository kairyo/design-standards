#!/usr/bin/env python3
"""Read-only structural checks; not a security or content certification."""

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
    "tools/check_docs.py",
)
ALLOWED_SOURCE_HOSTS = {
    "developer.apple.com", "developer.android.com", "help.figma.com",
    "www.w3.org", "www.designtokens.org", "github.com",
}
LINK = re.compile(r"(?<!!)\[[^\]\n]*\]\(([^)\n]+)\)")
URL = re.compile(r"https?://[^\s<>)\]，；。]+")
PRIVATE_PATH = re.compile(r"/(?:Users|home)/[^\s/]+/|(?:file|vscode)://")
SECRET = re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|gh[pousr]_[A-Za-z0-9]{30,}")


def main():
    errors = []
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
    documents = sorted(
        ROOT / name for name in actual_files if name.endswith(".md")
    )
    link_count = 0
    source_ids = set()
    for path in documents:
        relative = path.relative_to(ROOT)
        content = path.read_text(encoding="utf-8")
        if not content.endswith("\n"):
            errors.append(f"missing final newline: {relative}")
        if PRIVATE_PATH.search(content) or SECRET.search(content):
            errors.append(f"potential private material: {relative}")
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
        for url in URL.findall(content):
            parsed = urlsplit(url)
            if parsed.hostname not in ALLOWED_SOURCE_HOSTS:
                errors.append(f"unregistered external host in {relative}: {parsed.hostname}")
            if parsed.hostname == "github.com" and parsed.path.rstrip("/") != "/material-components/material-components-android":
                errors.append(f"unregistered GitHub reference in {relative}")
            if parsed.query or parsed.username or parsed.password:
                errors.append(f"review URL parameters/identity in {relative}")
        if relative.as_posix() == "references/sources.md":
            matches = re.findall(r"^## (S\d{2})$", content, re.M)
            source_ids = set(matches)
            if len(matches) != len(source_ids):
                errors.append("duplicate source IDs")
    if source_ids != {f"S{i:02d}" for i in range(1, 16)}:
        errors.append("source registry must contain S01 through S15")
    if errors:
        print("FAIL\n" + "\n".join(errors))
        return 1
    print(f"PASS: {len(EXPECTED)} required files; {len(documents)} Markdown files; "
          f"{link_count} internal links; {len(source_ids)} source entries")
    print("Scope: structural checks only. Manual fact, privacy, license, and history review still required.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
