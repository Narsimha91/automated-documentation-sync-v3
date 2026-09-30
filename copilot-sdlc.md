# GitHub Copilot SDLC Demo

## Project: Automated Documentation Sync

Build this project from an **empty GitHub repository** using GitHub Copilot.

The project requirement is maintained in **Confluence** and must be retrieved using the **Confluence MCP server**.

The purpose of this demo is to demonstrate an AI-assisted SDLC:

```text
Confluence
    ↓
Confluence MCP
    ↓
Requirements
    ↓
Architecture
    ↓
Design Review
    ↓
Implementation Plan
    ↓
Implementation
    ↓
Testing
    ↓
Code Review
    ↓
Pull Request
```

Copilot acts as the development assistant and peer reviewer.

The human developer approves important decisions and changes.

---

# 1. Start From an Empty Repository

Assume the repository initially contains:

```text
copilot-sdlc.md
```

Do not assume that application source code already exists.

Before implementing anything:

* inspect the repository
* connect to/use the configured Confluence MCP server
* retrieve the project requirement from Confluence
* use the retrieved requirement as the source for the rest of the SDLC

Do not invent requirements if the Confluence requirement cannot be retrieved.

---

# 2. Stage 1 — Requirements

## Source

Retrieve the **Automatic README Update** User Story from **Confluence using MCP**.

Ask Copilot to:

1. Read and understand the User Story.
2. Identify functional and non-functional requirements.
3. Identify acceptance criteria.
4. Ask clarification questions if anything is unclear.
5. Wait for the human's answers.
6. Create `requirements.md` after human approval.

The requirements must be based only on the **README Update** User Story and agreed clarifications.

# 3. Stage 2 — Architecture

Design the high-level system architecture based on the approved `requirements.md`.

1. Propose the system architecture.
2. Identify the key components and their responsibilities.
3. Recommend suitable technologies.
4. Describe the data flow.
5. Create a simple architecture/component diagram.
7. After human review and approval, document the proposed architecture in `architecture.md`.


# 4. Stage 3 — Design Review

Review the proposed `architecture.md` before writing production code.

1. Review the architecture as a senior reviewer.
2. Identify risks, gaps, and unclear design decisions.
3. Check that the architecture meets the approved requirements.
4. Document review findings and agreed decisions in `design-review.md`.
5. Update `architecture.md` if approved changes are required.


## Design Review Approval Criteria

Before implementation, verify that:

* [ ] All major risks and gaps are addressed.
* [ ] Architecture is consistent with `requirements.md`.
* [ ] Design decisions are clearly documented.
* [ ] Open questions are resolved or documented.
* [ ] No critical issues remain before implementation.

After human review and approval, document design reviews in `design-review.md` and any approved changes to `architecture.md`.


# 5. Stage 4 — Implementation Planning

Create an implementation plan based on the approved `architecture.md` and `design-review.md`.

1. Break the architecture into implementation tasks.
2. Prioritize the tasks.
3. Order tasks based on their dependencies.
4. Identify tasks that are blocked by other tasks.
5. Document the plan in `impl-plan.md`.

## Implementation Plan Output

`impl-plan.md` must contain:

* **Task ID**
* **Task Description**
* **Priority**
* **Dependencies**
* **Blocked/Unblocked Status**
* **Acceptance Criteria**

## Planning Approval Criteria

Before implementation, verify that:

* [ ] All major architecture components are covered.
* [ ] Tasks are in dependency order.
* [ ] Dependencies and blocked tasks are clearly identified.
* [ ] Each task has clear acceptance criteria.
* [ ] The plan is ready for implementation.

After human review and approval, document implementation plan in `impl-plan.md`.


# 6. Stage 5 — Implementation

Implement the approved tasks from `impl-plan.md`.

1. Implement tasks in the defined dependency order.
2. Follow the approved `requirements.md` and `architecture.md`.
3. Apply only changes approved by the human in the loop.
4. Add or update simple tests for the implemented changes.
5. Run the simple relevant tests after each task.
6. Report the implementation and test results.

## Implementation Approval Criteria

Before moving to the next stage, verify that:

* [ ] All approved implementation tasks are completed.
* [ ] Implementation follows the approved architecture.
* [ ] Tests are added or updated.
* [ ] Relevant tests pass.
* [ ] No unapproved changes were introduced.
* [ ] The implementation is ready for code review.

Waif for human review and approval on implementation changes.



# 7. Stage 6 — Code Review

Perform a structured review of the implementation before creating the PR.

Review the code against `requirements.md`, `architecture.md`, and `impl-plan.md`.

## Code Review Checklist

| Review Area           | Review Question                                                             |
| --------------------- | --------------------------------------------------------------------------- |
| **Correctness**       | Does each component behave as specified in `requirements.md`?               |
| **Security**          | Are secrets excluded from output? Is user input validated?                  |
| **Error Handling**    | Are API failures, missing files, and empty repositories handled gracefully? |
| **Test Coverage**     | Do tests cover happy paths and important edge cases?                        |
| **Code Clarity**      | Are function names clear and is the logic easy to follow?                   |
| **DRY Principle**     | Is there duplicated logic that can be refactored?                           |
| **Dependency Safety** | Are dependencies reasonable and free from known vulnerabilities?            |

## Review Output

Document the complete review in:

```text
code-review.md
```

The report must contain:

* **Review Summary**
* **Review Findings**
* **Severity**
* **Recommendations**
* **Actions Taken**
* **Final Review Status**

## Review Approval Criteria

Before creating the PR:

* [ ] All critical findings are resolved.
* [ ] Important findings are resolved or accepted by the human reviewer.
* [ ] Tests pass after approved changes.
* [ ] No security issues remain.
* [ ] Implementation matches the approved requirements and architecture.
* [ ] Code is ready for PR.

After human approval, commit `code-review.md` and any approved review changes before proceeding to PR creation.





# 8. Stage 7 — Verify

Generate and run a comprehensive verification suite for the completed implementation.

Verify both:

* **Code** — unit and integration tests.
* **Final output document** — content and quality checks.

## Verification

1. Generate or update tests based on `requirements.md`.
2. Run all unit tests.
3. Run integration tests.
4. Verify the final generated document.
5. Check that the document:

   * contains the expected content
   * is complete
   * is correctly formatted
   * does not contain unintended changes
6. Report all verification results.

## Verification Report

Create the verification report as:

```text
verification-report.md
```

The `verification-report.md` file must include:

* **Test Summary**
* **Unit Test Results**
* **Integration Test Results**
* **Document Quality Results**
* **Issues Found**
* **Final Verification Status**

## Verification Approval Criteria

* [ ] All unit tests pass.
* [ ] All integration tests pass.
* [ ] Final document content is correct.
* [ ] Document formatting is correct.
* [ ] No unintended changes are present.
* [ ] All critical issues are resolved.

After human approval, commit `verification-report.md`.



# 9. Stage 8 — PR Using Agentic SDLC

Use Agent Mode to create the Pull Request and complete the SDLC cycle.

Before creating the PR:

1. Review `requirements.md`, `architecture.md`, `design-review.md`, `impl-plan.md`, `code-review.md`, and `verification-report.md`.
2. Review the complete Git diff.
3. Confirm all required tests and verification checks have passed.
4. Create or update `CHANGELOG.md`.
5. Generate the PR description.
6. Create the Pull Request.
7. Do not merge the PR automatically.

## Changelog

Create or update:

```text
CHANGELOG.md
```

The changelog must briefly describe the changes included in the PR.

## Required PR Description

The PR description must contain:

### Summary

Provide a 2–3 sentence overview of what was built and why.

### Changes Made

Provide a bulleted list of **all files added or modified** and explain the reason for each change.

### Test Evidence

Include the actual test run output or a link to the CI results.

Do not invent test results.

### Known Limitations

Include anything marked **Not Found**, unresolved, or explicitly out of scope.

### Reviewer Checklist

Include:

```markdown id="4kjza4"
- [ ] Requirements are satisfied
- [ ] Architecture is approved
- [ ] Design review is complete
- [ ] Implementation plan is complete
- [ ] Code review is complete
- [ ] Unit and integration tests pass
- [ ] Verification report is approved
- [ ] CHANGELOG.md is updated
- [ ] No unintended changes are included
- [ ] Known limitations have been reviewed
```

## PR Approval Criteria

* [ ] All required PR sections are present.
* [ ] `CHANGELOG.md` is included and accurate.
* [ ] Test evidence is accurate.
* [ ] All required review documents are committed.
* [ ] PR is ready for human review.
* [ ] No automatic merge is performed.