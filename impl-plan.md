# Implementation Plan: Automatic README Update

## Status

Proposed plan based on the approved [architecture.md](architecture.md) and [design-review.md](design-review.md). No production implementation is authorized until this plan is reviewed and approved.

| Task ID | Task Description | Priority | Dependencies | Blocked/Unblocked Status | Acceptance Criteria |
| --- | --- | --- | --- | --- | --- |
| T1 | Establish the minimal Python project and pytest layout required by the workflow. | P1 | None | Unblocked | `pytest` discovers and runs the repository test suite; the workflow can use a documented, reproducible Python setup; no unrelated application features are added. |
| T2 | Add `src/features.py` with the user-editable `features()` function returning a list of exact feature labels. | P1 | T1 | Blocked by T1 | Importing and calling `features()` returns a list; labels are not translated or rewritten; a test verifies the provider contract. |
| T3 | Implement a README updater that renders provider labels inside the exact sync-marker region and preserves all other content. | P1 | T2 | Blocked by T2 | Valid input changes only text strictly between one correctly ordered marker pair; malformed/missing/duplicate markers or invalid provider output fail without writing; exact labels and outside-region preservation are covered by unit tests. |
| T4 | Add or update `README.md` with the required exact markers and an initial managed feature section. | P1 | T2 | Blocked by T2 | README contains one start/end marker pair in the correct order; the initial managed region reflects the feature list; explanatory content outside the region is not subject to updater changes. |
| T5 | Add focused tests for feature retrieval, README output, preservation, invalid input, and no-op updates. | P1 | T3, T4 | Blocked by T3 and T4 | `pytest` covers happy path, exact label output, content preservation, malformed markers, invalid provider output, and unchanged output; all tests pass locally. |
| T6 | Implement the GitHub Actions workflow for pushes to `main` changing `src/**`, enforcing tests before any update, and serializing runs. | P1 | T1, T5 | Blocked by T1 and T5 | Workflow triggers only on pushes to `main` with changed paths under `src/**`; tests use the pushed revision; test failure prevents every README/PR write; concurrent runs use one concurrency group; the test job has read-only repository permissions. |
| T7 | Add post-test automation-branch and PR lifecycle operations: update the existing documentation-sync PR or create it if absent, targeting `main`. | P1 | T6 | Blocked by T6 | A stable automation branch based on current `main` identifies the documentation-sync PR; the write job runs only after tests pass and uses minimum required permissions; an existing matching open PR is updated, otherwise one is created; no duplicate PR is opened and no automatic merge occurs. |
| T8 | Run end-to-end verification of workflow logic, updater behavior, branch/PR handling, and final README output; record actual results. | P1 | T5, T7 | Blocked by T5 and T7 | Unit and available integration checks pass; test-failure gating, trigger scope, PR create/update paths, and final README preservation are verified; results and any environment limitations are recorded without inventing evidence. |

## Dependency Order

```text
T1 -> T2 -> T3 -> T5 -> T6 -> T7 -> T8
       \-> T4 ----/                 ^
                                    |
                         T5 --------+
```

T3 and T4 may proceed independently after T2. T5 requires both. T6 depends on a working test suite so the required test gate can be exercised before workflow integration.

## Planning Approval Checklist

- [x] All major architecture components are covered.
- [x] Tasks are ordered by dependency.
- [x] Dependencies and blocked tasks are identified.
- [x] Every task has acceptance criteria.
- [ ] Human approval received; implementation may begin only after approval.