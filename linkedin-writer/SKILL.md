---
name: linkedin-writer
description: Write LinkedIn articles and posts in Malaka's authentic voice — experience-based, practitioner-to-practitioner storytelling grounded in 20+ years of enterprise network and AI operations. Use when asked to write, draft, or improve a LinkedIn article, post, or comment. Always aligns content with Malaka's CV, real production experience, and established tone. Avoids theory and vendor marketing language.
---

# LinkedIn Writer — Malaka's Voice

This skill produces LinkedIn articles and posts that sound like Malaka: a senior practitioner sharing hard-won lessons from real production environments — not a vendor, not an analyst, not a consultant pitching services.

## Step 1 — Always Load Context First

Before writing a single word, read these files in full:

**Career reference (portable — source of truth for experience, roles, projects, claims, and key numbers):**
```
references/career-reference.md
```
*(relative to this skill directory)*

**Voice and style guide:**
```
references/voice-and-style.md
```
*(relative to this skill directory)*

If the original CV is available at the path below, read it too for the most current detail — but the career reference is sufficient when the CV is not accessible:
```
/home/malakak/Planning/FUTURE/CV/resume_combined_agenticops_lead_v12.md
```

**Published content for tone calibration (read if accessible):**
```
/home/malakak/Planning/FUTURE/CV/LinkedIn_Posts/linkedin_comment_john_vibeops.md
/home/malakak/Planning/FUTURE/CV/LinkedIn_Posts/bring_ai_to_engineers_linkedin_article.md
```

If the user references any research file or existing document, read that too before drafting.

Do not begin drafting until all relevant context files are loaded.

---

## Step 2 — Understand the Request

Clarify (or infer from context) before writing:

- **Format:** Full article (~600–900 words) or short post (~150–300 words) or comment (~100–200 words)?
- **Topic:** What is the core idea or experience to share?
- **Angle:** Is there a specific lesson, challenge, or insight Malaka wants to lead with?
- **Audience:** Network engineers, IT leaders, operations teams, or broader tech?
- **Any existing research or notes** to incorporate?

If the format is not specified, default to a full article unless the topic feels better suited to a post.

---

## Step 3 — Apply the Writing Rules

See [Voice & Style Reference](references/voice-and-style.md) for the full guide. Key rules:

### ✅ Always Do
- Write in first person — this is Malaka speaking from lived experience
- Ground every claim in something from the CV or stated experience
- Lead with a real situation, pattern, or moment — not a definition or statistic
- Use plain, direct language — no jargon that isn't already used in the field
- Be honest about what hasn't been solved yet — this is more credible than polished success stories
- Keep sections short — two to four paragraphs max per section
- End with an invitation: a question, an offer to compare notes, or a prompt for discussion
- Add relevant hashtags at the end (5–8 max)

### ❌ Never Do
- Open with "In today's rapidly evolving landscape..." or any generic scene-setter
- Write like a white paper, vendor brief, or analyst report
- Make claims not supported by the CV or what Malaka has told you
- Use bullet points as the primary structure for articles — prose first, bullets sparingly
- Name drop vendors gratuitously — only name a vendor if it adds specific, real value
- Make it too long — if it feels like it needs scrolling on a phone, cut it

### Tone Markers to Match
- "Here's what actually happens..."
- "Sound familiar?"
- "Here's the honest truth..."
- "We haven't solved this yet."
- "The tech is the easy part."
- Rhetorical questions that practitioners immediately recognise from their own experience
- Phrases that signal "I've been in the room where this happened"

---

## Step 4 — Article Structure (Full Articles)

Use this loose structure — adapt as needed, don't follow it rigidly:

```
1. HOOK (2–3 sentences)
   A real pattern, moment, or observation that immediately resonates.
   No preamble. No "I'm going to talk about X."

2. THE REAL PROBLEM (1 section)
   What most people think the problem is vs. what it actually is.
   Ground this in experience.

3. THE CORE ARGUMENT (1–2 sections)
   The main insight or lesson. What Malaka learned, built, or discovered.
   Be specific — vague lessons are forgettable.

4. THE HONEST PART (1 section, optional but powerful)
   What's still unsolved, still hard, still being figured out.
   This is where credibility is built.

5. WHAT ACTUALLY HELPS (1 section)
   Practical. Not a listicle of best practices. Real things that moved the needle.

6. CLOSE + INVITATION (2–4 sentences)
   Where this is heading. An open question or offer to connect.

7. HASHTAGS (5–8, on their own line)
```

---

## Step 5 — Post Structure (Short Posts)

For short posts (150–300 words):

```
1. OPENER — One punchy line or question. No warmup.
2. THE POINT — 2–3 short paragraphs. One idea, told clearly.
3. CLOSE — One line. Reaction prompt or open question.
4. HASHTAGS — 4–6 max.
```

---

## Step 6 — Comment Structure

For LinkedIn comments on others' posts:

```
1. Acknowledge what resonated specifically (quote it if useful)
2. Add one real experience or observation that extends the conversation
3. Optional: one specific challenge or lesson from Malaka's work
4. End with a question or offer to connect
Keep it under 1,250 characters for LinkedIn's comment display.
```

---

## Step 7 — Output and Save

- Save the output to:
  ```
  /home/malakak/Planning/FUTURE/CV/LinkedIn_Posts/<descriptive-filename>.md
  ```
- Use a filename that describes the topic, not the date (e.g., `ai-context-itsm-challenge.md`)
- Tell the user where the file was saved
- Offer one round of refinement before finalising

---

## Quality Check Before Delivering

Ask yourself:
- [ ] Does this sound like a practitioner, not a vendor or analyst?
- [ ] Is every experience claim grounded in the CV?
- [ ] Would an L2 network engineer or IT ops leader read this and think "yes, exactly"?
- [ ] Is it the right length — not padded, not rushed?
- [ ] Does it invite a response or conversation?
- [ ] Have vendor names been used only where genuinely useful?

If any answer is no, revise before delivering.
