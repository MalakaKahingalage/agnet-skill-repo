---
name: resume-postbuild-validator
description: Validate a finished or recently tailored resume after drafting, rewriting, or PDF packaging. Use when a user wants a brutally honest post-build audit, ATS review, sharper rewrites, red-flag detection, or a ranked diagnosis of why a resume is not getting interviews.
---

# Resume Post-Build Validator

## Overview

Use this skill after the resume already exists and the main question is quality control: why it may be getting ignored, what is weakening it, and how to fix those issues without inventing experience.

This skill is for post-build resume validation, not first-pass drafting or PDF layout. Pair it with `$job-application-content-strategy` for role targeting and `$resume-pdf-packager` for final print-ready export.

## When To Use

Use this skill when the user asks for any of the following:
- a brutally honest resume review
- reasons they are not getting interviews
- ATS optimization for a target role
- red flags recruiters may notice
- stronger rewrites of existing bullets
- help positioning real experience more credibly
- a ranked breakdown of what is hurting the resume most

Typical inputs:
- markdown resume
- plain text resume
- resume extracted from PDF or DOCX
- one or more target job titles or job ads

## Workflow

1. Read the resume exactly as written.
   Preserve factual boundaries. Do not invent scope, metrics, tools, promotions, or outcomes.

2. Determine the targeting context.
   If the user supplied a specific job title or job ad, use it. If not, run a general market-facing audit first and note where role-specific advice would change the result.

3. Choose the audit mode.
   If the user requested one of the named passes, use that pass.
   If the user asked for a general validation, run all six passes in sequence using `references/audit-modes.md`, then consolidate the overlaps into one final diagnosis.

4. Produce findings before rewrites.
   Lead with the highest-damage issues. A review that jumps straight to rewritten bullets without explaining the problem is weaker and harder to trust.

5. Rewrite only where there is a clear gain.
   Sharpen wording, ordering, and specificity, but stay faithful to the source material. If a stronger version requires missing evidence, say what evidence is needed instead of fabricating it.

6. End with a practical fix plan.
   Give the user an ordered set of changes that can be applied immediately, starting with the items most likely to improve interview odds.

## Output Rules

- Be direct. Do not soften obvious weaknesses.
- Findings come first, ordered from most damaging to least damaging.
- For each issue, explain:
  - what is wrong
  - why it hurts interview chances
  - the exact fix
- When rewriting, show replacement wording rather than only abstract advice.
- Call out vague claims, generic phrases, missing proof, ATS gaps, trust issues, and weak positioning separately when they are distinct problems.
- Prefer recruiter-facing language over coaching language.
- If the resume has strong material but weak prioritization, say so explicitly and fix the ordering.

## Guardrails

- Do not exaggerate or fabricate achievements.
- Do not add keywords that the user cannot plausibly defend.
- Do not confuse formatting polish with content strength.
- If ATS guidance depends on the target role, say that clearly when the role is missing.
- If the resume is too thin to justify a stronger rewrite, say what evidence is missing.

## Recommended Response Shape

Use this structure unless the user asks for a different format:

1. `Top problems`
2. `Exact fixes`
3. `Rewritten sections or bullets`
4. `ATS or keyword gaps` when relevant
5. `Priority action plan`

For the `Hiring Problem Breakdown` mode, explicitly rank issues from most damaging to least damaging.

## Resources

- Audit pass definitions and exact mode prompts: `references/audit-modes.md`
