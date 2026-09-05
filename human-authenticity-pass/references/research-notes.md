# Research Notes — Human Authenticity Pass

## Research Objective

Design a reusable skill that can take AI-assisted professional documents and convert them into writing that reads as credible, human, specific, and interview-defensible.

## Core Conclusion

The right target is not "beat AI detectors."

The right target is a final pass based on:
- authenticity
- specificity
- truthfulness

## Main Findings

### 1. What Makes Text Feel AI-Written

Common patterns across sources and Gemini research:
- generic openings and closings
- abstract capability claims instead of examples
- overuse of buzzwords like `leverage`, `foster`, `navigate`, `dynamic`, `robust`, and `seamless`
- essay-style transitions like `furthermore`, `moreover`, and `additionally`
- uniform sentence length and repetitive bullet construction
- over-polished language that lacks friction, detail, and ownership
- inflated claims not grounded in role scope

### 2. What Makes Professional Writing Feel Human

- direct first-person ownership
- specific tools, systems, stakeholders, and constraints
- quantified results or grounded proxy metrics
- natural variation in sentence rhythm
- honest scope such as `I led`, `I coordinated`, or `In a team of 4, I owned...`
- role-tailored examples tied to the target job

### 3. Resume-Specific Guidance

High-trust resumes:
- focus on impact, not duties
- avoid progress bars, heavy graphics, and ATS-hostile layouts
- use quantified bullets where possible
- prefer active verbs over `responsible for`
- balance keyword alignment with readability

### 4. Cover-Letter Guidance

High-trust cover letters:
- avoid formulaic openings
- connect to the role or organisation specifically
- use 1-2 real examples
- sound like a professional speaking, not a chatbot summarising
- require human editing after AI drafting

### 5. Selection-Criteria Guidance

Strong criteria responses:
- prove merit with SAO or STAR evidence
- devote most words to the candidate's actions
- explicitly show what the candidate did, how, and what happened
- avoid theory, aspiration, and generic claims

### 6. Detection Research

AI detectors are unreliable for this use case.

Issues include:
- false positives
- bias against non-native English writers
- susceptibility to gaming
- poor fit for structured professional prose

Practical implication:
- do not build the skill around detector scores
- build it around human-review heuristics and evidence quality

### 7. Wikipedia AI-Writing Signals

Wikipedia's "Signs of AI writing" advice page is useful as a field guide, with an important caveat: style markers are signals, not proof. Its strongest transferable lesson for job documents is that AI-assisted text often smooths specific evidence into generic, inflated, broadly positive prose.

Useful patterns to audit:
- undue emphasis on significance, legacy, broader trends, or importance
- canned notability and credibility language that lists proof instead of demonstrating it
- superficial analysis that sounds plausible but lacks close evidence
- promotional wording and advertisement-like praise
- vague attribution such as `many believe`, `widely regarded`, or `known for`
- outline-like conclusions about future challenges and opportunities
- dense clusters of AI-coded vocabulary rather than one isolated word
- avoidance of simple syntax and plain verbs in favor of stiff synonyms
- negative parallelisms such as `not only X but also Y`, `not X but Y`, and `X rather than Y`
- overuse of three-part lists, title-case headings, inline-header bullets, boldface, em dashes, emoji, tables, and decorative separators
- markup or citation artifacts that suggest copied model output

Useful false-positive cautions:
- do not treat perfect grammar, formal language, isolated transitions, or a single em dash as proof of AI use
- avoid penalizing mixed registers, which can reflect profession, age, neurodivergence, culture, or ordinary personal style
- watch for confirmation bias; investigate the evidence problem rather than accusing the writer

Human-authenticity implication:
- ask whether the candidate can explain each claim, metric, citation, example, and word choice
- preserve plain human syntax when it sounds natural
- repair the deeper problem: missing specificity, weak attribution, inflated tone, unsupported evidence, or indefensible ownership

## Suggested Skill Behavior

1. audit draft for AI tells
2. identify unsupported claims
3. ask targeted evidence questions
4. rewrite using active, evidence-led language
5. run a final authenticity checklist

## Recommended Evaluation Lens: AST

### Authenticity

- does it sound natural aloud?
- does it avoid LLM cliches?
- does it use clear ownership?

### Specificity

- are tools, metrics, stakeholders, and constraints named?
- are outcomes concrete?

### Truthfulness

- can every claim be defended in an interview?
- is the scope proportionate and honest?

## Source Highlights

### MIT Career Advising & Professional Development

Using AI for cover letters:
- AI is best used as a brainstorming and editing partner
- obvious AI signs include formulaic structure, over-polished writing, and em-dash heavy style
- AI can oversell or hallucinate qualifications

<https://capd.mit.edu/resources/using-ai-for-cover-letters/>

### SEEK Australia

How to write a cover letter using AI:
- AI drafts must be personalised
- use specific achievements, storytelling, keywords, and read-aloud editing
- final human review is essential

<https://au.seek.com/career-advice/article/how-to-write-a-cover-letter-using-ai>

### Harvard Business School Alumni

Generative AI for job search:
- better inputs produce less generic outputs
- edit for accuracy and voice
- use GenAI as support, not replacement

<https://www.alumni.hbs.edu/careers/job-search/Pages/generative-ai.aspx>

### Turnitin

Understanding false positive rates:
- even vendor guidance says outputs should be treated as indicators, not conclusions
- sentence-level false positives exist

<https://www.turnitin.com/blog/understanding-the-false-positive-rate-for-sentences-of-our-ai-writing-detection-capability>

### Stanford HAI

AI detectors biased against non-native English writers:
- detectors are unreliable and easily gamed
- reported major false-positive issues for non-native English writers

<https://hai.stanford.edu/news/ai-detectors-biased-against-non-native-english-writers>

### Wikipedia

Signs of AI writing:
- use the page as a descriptive field guide, not a detector
- look for clusters of content, language, style, citation, and formatting signals
- focus the rewrite on evidence quality and defensible authorship rather than cosmetic signal removal

<https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing>

## Gemini Research Artifacts

Local research runs were saved under:
- `research/human-writing-skill/`
- `.gemini/antigravity-cli/brain/...` artifacts used during synthesis

## Bottom Line

A strong human-authenticity skill should function like a smart recruiter plus editor:
- skeptical of vague claims
- strict about evidence
- careful not to invent facts
- focused on making the writing sound like the real candidate
