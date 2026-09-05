---
name: subagent-driven-development
description: Execute implementation plans by dispatching fresh subagents per task with systematic two-stage review (spec compliance then code quality). Use for complex multi-task feature implementations, code refactoring, and multi-subagent workflows.
version: 1.0.0
license: MIT
metadata:
  tags: [delegation, subagent, implementation, workflow, parallel]
---

# Subagent-Driven Development

## Overview

Execute implementation plans by dispatching fresh subagents per task with systematic two-stage review.

**Core principle:** Fresh subagent per task + two-stage review (spec then quality) = high quality, fast iteration.

## When to Use

Use this skill when:
- You have an implementation plan (from writing-plans skill or user requirements)
- A task involves multiple distinct steps or modules
- You want to maintain high code quality with zero context pollution between tasks

## Workflow

### 1. Preparation & Todo Setup
1. Read and analyze the implementation plan.
2. Break down the plan into small, well-defined tasks (2-5 minutes of work each).
3. Initialize the tracking todo list.

### 2. Task Execution Loop (Per Task)

#### Step 1: Dispatch Implementer Subagent
Create a fresh subagent for the task with full context, requirements, file locations, and constraints.
- Provide full scene-setting context.
- Explicitly instruct the subagent to use Test-Driven Development (TDD) where applicable.

#### Step 2: Dispatch Spec Compliance Reviewer
Once implementation completes, dispatch a spec review subagent:
- Verify all requirements from the spec were implemented.
- Confirm file paths and signatures match the plan.
- Ensure no unauthorized scope creep was introduced.
- **Verdict required**: `PASS` or specific spec gaps.

If gaps exist, instruct the implementer to fix them and re-run spec review until `PASS`.

#### Step 3: Dispatch Code Quality Reviewer
Only after spec compliance passes:
- Audit style, error handling, variable names, test coverage, and edge cases.
- **Verdict required**: `APPROVED` or `REQUEST_CHANGES`.

If issues exist, fix them and re-review until `APPROVED`.

#### Step 4: Mark Task Complete & Proceed to Next Task

### 3. Final Integration Review & Verification
- Dispatch a final integration reviewer to test all components together.
- Run full test suites (`pytest`, `npm test`, etc.).
- Review `git diff --stat` and perform final commit.

## Core Rules

1. **Fresh Subagent per Task**: Never reuse an implementer subagent across unrelated tasks to prevent context pollution.
2. **Strict Order**: Spec compliance review MUST pass BEFORE starting code quality review.
3. **No Unfixed Issues**: Never proceed to the next task while either review stage has open issues.
4. **Appropriate Granularity**: Keep individual tasks small and focused (e.g. "Create User model", "Add password hashing", "Create login endpoint").
