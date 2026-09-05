# Resume Audit Modes

Use these modes as named post-build validation passes. If the user asks for one mode, run that mode. If the user asks for a general post-build review, run all six, then merge overlapping findings into one ranked diagnosis.

## 1. Resume Audit Fix

Use when the user wants a blunt hiring-manager style critique of why the resume is being skipped.

Prompt basis:
`Act like a brutally honest hiring manager. Review my resume and tell me every reason I'm not getting interviews. Point out weak wording, vague achievements, ATS issues, generic phrases, and anything making recruiters skip me. Be direct and give exact fixes.`

Focus:
- weak wording
- vague or unsupported achievements
- generic filler language
- ATS problems
- reasons a recruiter would stop reading

Expected output:
- direct findings
- exact replacements for weak lines
- concise explanation of likely rejection triggers

## 2. Resume Rewrite Boost

Use when the user wants the resume rewritten for a target role without changing the underlying facts.

Prompt basis:
`Rewrite my resume for [job title] to maximize interview chances. Keep my real experience, but rewrite every bullet to sound sharper, more valuable, and results driven. Remove weak wording and make it read like a top candidate's resume.`

Focus:
- sharper bullets
- stronger verbs
- clearer value
- role relevance
- better top-candidate tone without dishonesty

Expected output:
- rewritten summary or profile
- rewritten bullets
- concise note on what changed and why

## 3. Resume Red Flags

Use when the user wants hidden trust or credibility issues surfaced.

Prompt basis:
`Review my resume like a recruiter scanning hundreds of applications. Find every hidden red flag, weak section, or trust issue that could stop me from getting interviews. Explain why it hurts me and how to fix it.`

Focus:
- credibility issues
- confusing chronology
- inflated wording
- suspiciously broad claims
- weak sections that imply low impact

Expected output:
- list of red flags
- why each one damages trust
- exact repair steps

## 4. ATS Resume Fix

Use when the user wants role-specific ATS optimization.

Prompt basis:
`Optimize my resume for ATS screening for [job title]. Find missing keywords, skills, and industry language recruiters expect. Rewrite sections naturally so my resume passes filters without sounding forced or keyword stuffed.`

Focus:
- missing keywords
- missing skills language
- underused industry terminology
- section rewrites that improve matching naturally

Expected output:
- missing keyword list
- natural rewrite suggestions
- note on where keyword stuffing would become a problem

## 5. Experience Positioning Fix

Use when the resume contains real evidence but presents it weakly.

Prompt basis:
`Based on my background, show me where I'm underselling myself. Rewrite my experience to sound more credible, valuable, and relevant for the roles I want without exaggerating or inventing achievements.`

Focus:
- undersold work
- buried impact
- weak framing
- relevance gaps caused by wording rather than experience

Expected output:
- places where the user is underselling themselves
- stronger rewrites grounded in the existing evidence
- notes on evidence still needed for stronger claims

## 6. Hiring Problem Breakdown

Use when the user wants a ranked diagnosis tied to interview outcomes.

Prompt basis:
`Based on my resume and the jobs I'm applying for, give me an honest breakdown of why I'm not getting hired. Rank the biggest problems from most damaging to least damaging and give me a clear step by step fix for each.`

Focus:
- root causes
- ranking by damage
- practical correction order
- likely interaction between content, targeting, and ATS issues

Expected output:
- ranked problem list
- step-by-step fix for each problem
- short action sequence the user can follow immediately

## Consolidation Rules

When multiple modes are used together:
- deduplicate overlapping findings
- keep the strongest explanation of each problem
- separate content issues from credibility issues and ATS issues
- end with one prioritized action plan instead of six disconnected mini-reviews

## Truthfulness Rules

- Never invent achievements, metrics, scope, or promotions.
- Only add role keywords when the user's background can plausibly support them.
- If a rewrite would be much stronger with missing evidence, say what evidence is needed.
