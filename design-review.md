# Design Review: Automatic README Update

## Review Scope

Reviewed [architecture.md](architecture.md) against the approved [requirements.md](requirements.md) before production implementation.

## Review Summary

The proposed architecture covers the approved functional requirements. The human resolved the source-branch ambiguity by restricting workflow triggers to pushes on `main` that change `src/**`. The same pushed `main` revision is the source for tests and feature extraction, while the generated README update is proposed through a stable automation branch and PR targeting `main`.

## Review Findings

| ID | Severity | Finding | Recommendation | Status |
| --- | --- | --- | --- | --- |
| DR-1 | Resolved | The original requirements did not specify eligible source branches, risking documentation generated from unmerged feature-branch code. | Restrict the workflow to pushes on `main` with a `src/**` path filter; use that pushed revision for tests and feature extraction. | Resolved by human decision; recorded in requirements and architecture. |
| DR-2 | Medium | Creating or updating a PR requires repository permissions and compatible repository Actions settings. A token with insufficient permissions could make the workflow fail after tests pass. | Use the built-in `GITHUB_TOKEN`, grant only contents and pull-request write permissions, and document that repository settings must permit Actions to create PRs. Keep merge permission unavailable. | Address during implementation and report clearly if repository policy blocks PR operations. |
| DR-3 | Medium | Concurrent pushes could race while updating one stable automation branch and its PR. | Serialize workflow runs with a concurrency group for this documentation-sync workflow; prefer the latest queued source revision and ensure the generated branch is based on current `main`. | Address during implementation. |
| DR-4 | Low | A malformed README or invalid feature provider could otherwise cause partial or misleading output. | Validate the feature provider and exactly one correctly ordered marker pair before writing; write only after the full updated document is constructed. Add focused tests for invalid inputs and preservation. | Address during implementation. |
| DR-5 | Low | The story says to report failed tests but does not prescribe notification channels. | Use the GitHub Actions failed job/check as the failure report; do not introduce external notification services without approval. | Resolved within current scope. |

## Requirements Alignment

- Main-only and `src/**`-only trigger scope is specified and approved.
- `pytest` is the first operation that can affect generation or PR state; failures stop downstream steps.
- Feature labels come from `features()` and are rendered verbatim.
- README changes are limited to the exact sync region; malformed markers fail without writing.
- The stable automation branch supports creating the first PR and updating it on later runs. The PR targets `main`, and merging remains manual.

## Decisions and Actions

- Use pushes to `main` with paths under `src/**` as the only workflow trigger.
- Run tests and feature extraction against the same pushed `main` revision.
- Use a stable automation branch and one serialized workflow run at a time to maintain the documentation-sync PR.
- Request only the GitHub token permissions needed for content writes and pull-request operations; do not enable automatic merge.
- Treat repository-level permission restrictions as an actionable workflow failure, not as a reason to bypass review.
- Implement README changes atomically after validating provider output and markers.

## Open Questions

No critical design questions remain before implementation planning. Repository-specific Actions policy and feature-list edge-case policy (such as duplicate or empty strings) should be checked during implementation; they must not weaken marker safety, exact label rendering, or the test gate.

## Final Review Status

**Approved for implementation planning.** The main-branch trigger decision was supplied by the human reviewer on 2026-09-30. Medium and low findings have concrete implementation actions; no critical design issues remain.

## Superseded Review Draft Notice

The review draft below is retained as historical material only and is not the controlling review. Its claims about non-default branch triggers, metadata-derived README content, and human approval on 2026-09-29 conflict with the current approved [requirements.md](requirements.md), [architecture.md](architecture.md), and the review above. Implement only the current main-only, `features()`-based design.

# Superseded Design Review Draft (Historical, Not Approved)

## Review Summary

The revised architecture covers the `src/**` trigger, test-before-update ordering, README preservation, and human review through a pull request. It now records the tested revision and sorted changed source paths, so README output changes deterministically for each distinct in-scope push. A pull request from a non-default source branch is based on the tested revision and carries that source change with its README update; a push already on the default branch produces a documentation-only PR.

The user approved proceeding with the review recommendations. The significant source-to-README and branch-targeting gaps are addressed in the revised architecture. No production code has been written in this stage.

## Risks and Gaps

| ID | Severity | Finding and disposition |
| --- | --- | --- |
| DR-1 | High - Resolved | README output now includes the full tested revision SHA and sorted paths changed under `src/`. This creates a deterministic, auditable update even when project-level metadata is unchanged, without inferring behavior or using AI. |
| DR-2 | High - Resolved | The PR branch is based on the tested revision. Feature-branch PRs contain the source change and its README update together; pushes already on the default branch produce a README-only PR. |
| DR-3 | Medium - Resolved | Project name is required; absent or dynamic description/version fields are omitted; missing name or source-change metadata fails without writing. |
| DR-4 | Low - Implementation follow-up | The implementation must select and pin the pull-request action to a reviewed immutable revision, then test branch updates, no-diff runs, and repeated runs. This is an implementation task, not an unresolved architecture decision. |

## Recommended Changes

- Applied: include the tested revision SHA and sorted, escaped changed paths in the managed README section; do not generate semantic claims from source code.
- Applied: base feature-branch PRs on the tested revision so source and generated README content are reviewed together; create a documentation-only PR when the triggering source revision is already on the default branch.
- Applied: require project name, omit absent/dynamic description and version, and fail without writing when required data or valid markers are unavailable.
- Implementation follow-up: select and pin the PR action to an immutable reviewed revision; test no-diff and repeated-run behavior and ensure failures do not write README content.

## Agreed Design Decisions

- Any added, modified, deleted, or renamed path under `src/` is in scope for triggering the workflow, regardless of file type; changes only outside `src/` are excluded.
- Run `pytest` before attempting a README update. A test failure must stop the update and be reported.
- Generate README content deterministically from project metadata, preserve user-authored README content, and make the automated change reviewable through GitHub before merge.
- Do not automatically merge the generated change.
- The generated source-change record consists of the full tested revision SHA and sorted changed `src/` paths; commit messages and inferred behavior are excluded.
- A feature-branch PR must include the tested source revision with the README update; a default-branch push produces a README-only PR.
- Project name is required; absent or dynamic description and version values are omitted. Invalid markers or missing required inputs fail without modifying the README.
- The human developer approved applying the design-review recommendations on 2026-09-29.

## Open Questions

No architecture-level questions block Stage 4 planning. During implementation, the exact immutable action revision and Python patch version must be selected and recorded. Tests must verify source-path collection, revision provenance, README preservation, error behavior, and PR branch alignment.

## Final Recommendation

**APPROVED** — The revised architecture addresses the blocking source-to-README and branch-targeting findings and is ready for Stage 4 implementation planning. Pin the PR action and verify the listed workflow behaviors during implementation. No production code was changed during this review.