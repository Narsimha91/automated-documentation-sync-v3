# Requirements: Automatic README Update

## Source

- Confluence user story: **Automatic README Update**
- Human clarifications approved on 2026-09-30

## User Story

As a developer, I want the project's README documentation to be automatically updated when important source-code changes are made, so that the documentation stays up to date without requiring manual updates.

## Functional Requirements

- **FR1: Scoped trigger.** The automated workflow runs only for pushes to `main` that change files inside `src/**`. Changes to unrelated paths, including documentation or configuration files, do not trigger it.
- **FR2: Test before update.** The workflow runs `pytest` before updating the README. If any test fails, the workflow stops and reports the failure; no README update or PR update is performed.
- **FR3: Feature provider.** `src/features.py` defines a function named `features()` that returns a list of feature labels. Users can edit the list to add features.
- **FR4: Exact feature labels.** The README update uses each feature label exactly as returned by `features()`, without translating, renaming, or otherwise changing its text.
- **FR5: Bounded README update.** The updater replaces only the content strictly between the exact markers `<!-- docs-sync:start -->` and `<!-- docs-sync:end -->` in `README.md`.
- **FR6: Preserve surrounding content.** All README content outside the sync markers remains unchanged.
- **FR7: Pull request lifecycle.** After tests pass and the README is updated, the automation finds and updates the existing documentation-sync PR when one exists; otherwise, it creates the initial PR. The PR targets `main`; changes are not merged automatically.

## Acceptance Criteria

- **AC1: Scoped trigger:** A push to `main` that changes a file under `src/**` triggers the workflow. A push to another branch or a push that changes only unrelated paths does not.
- **AC2: Pre-execution testing:** `pytest` runs before README generation. On test failure, the workflow exits unsuccessfully and does not update the README or PR.
- **AC3: Feature-driven update:** The workflow obtains feature labels by executing `src/features.py` through its `features()` function and writes the returned labels exactly inside the README sync region.
- **AC4: Content preservation:** README content before the start marker and after the end marker is unchanged by the updater.
- **AC5: Pull request review:** Successful automation updates the existing documentation-sync PR targeting `main`, or creates it if none exists, for team review; it does not merge the PR.

## Non-Functional Requirements

The Confluence story and approved clarifications do not specify additional measurable non-functional requirements. Reliability and safety expectations directly implied by the acceptance criteria are:

- The updater must fail clearly if the required README markers or feature provider cannot be found, rather than silently replacing unrelated README content.
- A failed test run must prevent subsequent README and PR-update steps.

## Clarifications and Scope

- Feature labels are authored in the list returned by `features()` and rendered verbatim. No mapping such as `add` to `addition` is performed.
- The marker syntax is the exact HTML comment pair shown above.
- The workflow creates a PR on the first successful run when none exists, then updates that PR on later runs rather than creating duplicates.
- The workflow trigger is restricted to pushes on `main` that change files under `src/**`.
- PR merge remains a human review and approval action.
- The story does not define PR identification rules or feature-list formatting beyond preserving each exact label, nor handling of duplicate/empty labels. PR identification and formatting details remain for architecture/design review rather than being assumed here.