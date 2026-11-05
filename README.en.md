# Design Standards

[中文](README.md) · [Project management](PROJECT_MANAGEMENT.md) · [Issues](https://github.com/kairyo/design-standards/issues) · [Pull requests](https://github.com/kairyo/design-standards/pulls)

GitHub collaboration content and entry points are bilingual in Chinese and English. The ten chapters, design record templates, examples, skills, and historical evidence remain in Chinese for now. Keep both README versions aligned; translation does not expand claims or authorization.

Cross-project, cross-platform design methods and acceptance guidance. The aim is to ground design decisions, trace implementation, and verify quality, without making every product look the same.

**Version: v0.1 / `0.1.0-draft.3`. Status: REVIEW_CANDIDATE. The first repository-wide independent content review is complete; real-world effectiveness validation and formal release remain pending. See the [review record](reviews/2026-11-04-repository-review.md) for its version and scope.**

This repository supports design planning, handoff, and acceptance for Web/HTML, native Apple clients, and Android. Differences in frameworks, operating systems, fonts, and rendering mean that one set of values or one tool workflow cannot be assumed to fit every project. This is not an official platform standard or a skill package that improves visual quality merely by being installed.

## Where to start

| Task | Entry point |
| --- | --- |
| Define design goals, hierarchy, and brand | [01 Principles](docs/01-principles.md), [02 Exploration](docs/02-exploration.md) |
| Organize Figma and prepare implementation inputs | [03 Figma and handoff](docs/03-figma-handoff.md) |
| Establish a reusable visual language | [04 Design systems](docs/04-design-systems.md) |
| Handle system and window differences | [05 Apple](docs/05-apple.md), [06 Android](docs/06-android.md) |
| Address localization, themes, and accessibility | [07 Inclusive design](docs/07-inclusive-design.md) |
| Move from design to real-product acceptance | [08 Implementation and acceptance](docs/08-implementation-acceptance.md) |
| Assess source reliability and applicability | [09 Sources and experience](docs/09-reference-library.md), [Source registry](references/sources.md) |
| Adopt, make exceptions, update, or exit | [10 Adoption and maintenance](docs/10-adoption-maintenance.md) |
| Review design direction or adaptive interfaces with skills | [Skills and reuse boundaries](skills/README.md), [Boundary cases](skills/review-cases.md) |

Materials for discussion: [Design brief](templates/design-brief.md), [Adoption record](templates/adoption-record.md), [Verification record](templates/verification-record.md), [Synthetic anonymous cases](examples/anonymous-cases.md), [Complete form submission and correction example](examples/form-submit-recovery.md), and [Stepped-form return example](examples/stepped-form-branch-return.md). The complete example connects chapters 02, 04, 07, and 08; the stepped example adds checks for drafts, active data, and focus when moving back and forth. All product checks remain unexecuted; these examples do not establish that the repository contains a runnable form.

The `skills/` directory contains two self-contained, original review skills. They remain candidates and have not been globally installed, automatically registered, or enabled in existing projects. Existing third-party design plugins are indexed only; they are not distributed here.

Focused additions: [Figma variable-binding and theme-switching example](examples/figma-variable-theme.md) and [Optional landing-page brief appendix](templates/landing-page-brief.md). The former connects samples, consumers, modes, and restoration across chapters 03, 04, and 08; the latter extends chapter 02 with visitor entry context, the primary action, and evidence for claims. Both contain original methods and synthetic content, without actual Figma execution or landing-page effectiveness validation.

## Four distinct claim categories

- `OFFICIAL_REQUIREMENT`: an official normative requirement with a clear source and applicability conditions. Not every official recommendation belongs here.
- `TEAM_RECOMMENDATION`: a method proposed by this repository, including selective adoption of official design advice. It is not an official endorsement.
- `PROJECT_CHOICE`: brand, languages, scope, values, technology, and process decided by an individual project.
- `UNVERIFIED`: a claim without an adequately read source or corresponding verification evidence. It cannot support acceptance sign-off.

Record source reading, recommended adoption, project approval, and implementation acceptance separately. The default category in the chapters is `TEAM_RECOMMENDATION`; other categories are explicitly marked where applicable.

## Boundaries

This repository changes no existing project's designs, rules, or permissions. A project must explicitly select chapters, pin a full commit SHA, and resolve conflicts before adopting them. An update here must not automatically overwrite frozen designs.

This repository does not standardize models, accounts, permissions, memory, personal settings, engineering pipelines, or database rules, and grants no additional publication authority. Work continues to follow the current project's management and safety requirements.

Only original methods, public source links, and short applicability notes belong here. The repository contains no private project identifiers, real user data, design files, fonts, icon packs, third-party document mirrors, or SDK exports.

## Maintenance and status

- [GitHub project management and bilingual conventions](PROJECT_MANAGEMENT.md)
- [Project tracking issue](https://github.com/kairyo/design-standards/issues/1), [Milestones](https://github.com/kairyo/design-standards/milestones)
- [Collaboration maintenance verification record](reviews/2026-11-03-github-management.md)
- [Variable example and landing-page appendix verification record](reviews/2026-11-05-figma-landing.md)
- [Repository-wide independent content review](reviews/2026-11-04-repository-review.md), [Minimal text-case suite](reviews/text-cases/README.md)
- [Contributing and publication checks](CONTRIBUTING.md)
- [Agent maintenance instructions for this repository](AGENTS.md)
- [Changelog](CHANGELOG.md)
- [Review record and outstanding work](REVIEW.md)
- [License scope and attribution](LICENSE-NOTICE.md), [Third-party notices](THIRD-PARTY-NOTICES.md)

This version's original documentation, templates, examples, and skill text use [CC BY 4.0](LICENSE); original checking code uses [MIT](tools/LICENSE). See the license notice for file scope, attribution, and third-party exceptions. Contributors provide material they are entitled to submit under the corresponding license. License grants and quality acceptance are recorded separately; this review candidate makes no claim of adoption by any production project.
