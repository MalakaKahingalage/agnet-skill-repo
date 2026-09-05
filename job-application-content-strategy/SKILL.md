---
name: job-application-content-strategy
description: Analyze job ads and build stronger application content strategy for resumes, CVs, and cover letters. Use when a user wants to tailor an application for a specific role, decide which achievements to emphasize, choose the right framing for a target employer, or turn a broad career history into a sharper role-matched narrative.
---

# Job Application Content Strategy

## Overview

Use this skill when the main problem is not document formatting, but content strategy: what to emphasize, what to cut, how to frame experience for a target role, and how to turn a user's existing evidence into a stronger shortlist-worthy application.

This skill is for:
- resume and CV tailoring
- cover letter strategy
- role-fit analysis
- evidence selection
- headline and summary positioning
- translating technical work into business-relevant value

Do not use this skill for PDF layout or export. Pair it with `$resume-pdf-packager` when the user also wants polished PDFs.

## Core Workflow

1. Read the target role carefully.
   Extract:
   - title and seniority
   - functional shape of the role
   - required capabilities
   - preferred capabilities
   - implied success measures
   - stakeholder environment
   - operating model clues such as consulting, product, operations, transformation, leadership, or specialist IC

2. Build the role thesis.
   Summarize in 2-4 lines what the employer is really buying.
   This should be sharper than the job ad itself.

3. Map the user's evidence to that thesis.
   Prefer:
   - measurable outcomes
   - scale
   - leadership scope
   - complexity handled
   - relevance to the target environment
   - proof of judgment, not just activity

4. Decide what narrative to lead with.
   Common patterns:
   - transformation leader
   - technical programme leader
   - product or workflow owner
   - specialist builder with production credibility
   - operations uplift leader
   - consulting-style translator between business and engineering

5. Rewrite the top of the application first.
   Prioritize:
   - headline
   - summary/profile
   - top proof points
   - first role bullets

   If page 1 is weak, the rest of the document usually does not matter.

6. Tailor the cover letter separately.
   The cover letter should not repeat the resume line by line.
   Its job is to explain:
   - why this role
   - why this candidate
   - why this fit makes sense now

## Decision Rules

### What to emphasize

Lead with evidence that answers the target role's real buying criteria:
- direct capability match
- adjacent capability with clear transfer value
- leadership scale
- measurable operational or business improvement
- stakeholder complexity
- delivery in production or live environments

### What to cut or compress

Cut or shrink:
- weakly relevant tool lists near the top
- generic responsibility language
- duplicated bullets
- “worked on” phrasing without outcomes
- content that reads like an internal status report instead of market-facing proof

### How to handle domain gaps

If the user lacks direct domain match:
- do not hide the gap
- reposition around transferable operating problems
- show why the core capability still maps

Example:
If the role is outside networking but the user has built AI-enabled operational workflows in networking, focus on workflow transformation, service uplift, adoption, governance, and measurable efficiency rather than the narrow domain label.

## Writing Rules

- Prefer outcome-led language over task-led language.
- Put the strongest numbers high and early.
- Use specific verbs: architected, operationalised, reduced, secured, shifted, improved, scaled, governed.
- Avoid inflated or unverifiable claims.
- Avoid generic AI hype language.
- Favor production credibility over conceptual enthusiasm.
- Translate technical achievements into team, service, risk, cost, or business outcomes.

## Resume Strategy

When tailoring a resume:

1. Start with a role-aligned headline.
2. Rewrite the profile around the target role's buying criteria.
3. Add 2-4 top proof points if the role benefits from immediate scanning.
4. Reorder bullets inside the most relevant role so the strongest evidence comes first.
5. Make leadership scale visible when it matters.
6. Make value visible in numbers whenever defensible.

Use the checklist in `references/resume-strategy-checklist.md`.

## Cover Letter Strategy

A strong cover letter should do three things:
- establish fit quickly
- explain the relevance of the user's background to the role
- show judgment about why the role matters and how the user would add value

Structure:
1. Opening fit statement
2. Why the background maps
3. 2-3 strongest reasons to shortlist
4. Close tied to the employer or role context

Use the checklist in `references/cover-letter-strategy-checklist.md`.

## Common Reframing Patterns

- From “network specialist” to “enterprise operations transformation leader”
- From “tooling owner” to “workflow and service improvement owner”
- From “technical SME” to “trusted delivery lead in complex environments”
- From “automation engineer” to “production AI and automation capability builder”
- From “manager in all but title” to “leader with operating proof”

## Validation

Before finalizing the content, check:
- Does the top third of the resume clearly match the role?
- Are the best metrics visible early?
- Is the narrative coherent, or does it read like multiple competing profiles?
- Does the cover letter add value beyond repeating the resume?
- Would a hiring manager understand within 30-60 seconds why this candidate fits?

## Resources

- Resume tailoring checklist: `references/resume-strategy-checklist.md`
- Cover letter checklist: `references/cover-letter-strategy-checklist.md`
- Role analysis prompts: `references/role-analysis-patterns.md`
