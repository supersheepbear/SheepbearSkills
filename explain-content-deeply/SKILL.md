---
name: explain-content-deeply
description: Create complete, standalone, beginner-friendly textbook-style explanations from provided content, source materials, excerpts, notes, transcripts, documents, or topics, and write the finished teaching output into a lesson-specific subfolder under a user-chosen folder. Use when the user asks to teach, explain, rewrite as a lesson, deeply analyze learning material, cover every point without assuming prior knowledge, create chapter-by-chapter instruction, add Feynman-style checks, save explanations as files, or complete a multi-part teaching project.
---

# Explain Content Deeply

## Core Goal

Turn the user's provided material or topic into a complete teaching explanation that can independently replace the original source. The reader should understand every important detail without seeing the source text.

Use a textbook style: explanation-heavy, visually light, precise, patient, and friendly to beginners. Write so a motivated middle-school student can follow it. Do not intentionally use advanced or academic-sounding words when simpler words work. When a difficult term is necessary, define it immediately in plain language before using it heavily.

## Start-of-Task Mode Check

Before teaching new content, ask the user these mode questions in English and wait for their choices. Ask once, then complete the whole lesson directly. Do not require the user to say `start` or `continue` during the normal workflow. If the user has already specified one or more answers, ask only for the missing choices. If the user omits the output folder, use `d:\teaching`.

```text
Before I begin, please choose the teaching mode:

Output folder:
Please provide a parent folder path. I will create a new lesson-specific subfolder inside it and write all lesson files there.
If you do not provide one, I will use d:\teaching as the parent folder.

Answer format:
1. Explain everything in one file.
2. Split the lesson into multiple chapter files. By choosing this, you explicitly request automatic subagent use for chapter writing whenever the subagent tool is available and higher-priority tool rules permit it.
3. Let me choose based on the length and density of the material. If I choose multiple chapters, treat this as your explicit request to use automatic subagents whenever the subagent tool is available and higher-priority tool rules permit it.

Answer language:
1. Full English.
2. Full Chinese, with key terms translated into English for learning.
3. Another language you specify.

Complexity:
1. Simple mode: covers every point, but uses concise wording and stays relatively short.
2. Default mode.
3. Complex mode: very detailed, with more steps, examples, reasoning, and supporting details. It does not mean using harder vocabulary.
```

Default choices when the user delegates the choice:
- Output folder: use `d:\teaching` as the parent folder, then create a lesson-specific subfolder inside it.
- Answer format: choose `3`; for short material use one file, for long or dense material use multiple chapter files.
- Answer language: choose `2` if the user wrote the request in Chinese, otherwise match the user's language.
- Complexity: choose `2`.

## File Output Rules

Always write the teaching output to files in a new lesson-specific subfolder under the selected parent folder. Do not paste the full lesson into chat unless the user explicitly asks for that.

Treat the selected output folder as a parent folder, not the lesson workspace itself. Create the parent folder if it does not exist. Then create a lesson-specific subfolder inside it and use that subfolder as the lesson workspace. Name the subfolder from the topic when possible, and add a timestamp or numeric suffix if needed to avoid conflicts.

Use Markdown files by default:
- One-file mode: write `_lesson-manifest.md` and one complete lesson file, for example `lesson.md`.
- Multi-chapter mode: write `_lesson-manifest.md`, `00-writing-guide.md`, `00-table-of-contents.md`, then chapter files such as `01-introduction.md`, `02-core-concepts.md`, and so on.
- If a filename already exists inside the lesson workspace, do not overwrite it without confirmation. Create a unique filename when needed, then tell the user the exact path.

After the mode choices are known, complete the entire selected output in one run:
- In one-file mode, write the full lesson file.
- In multi-chapter mode, write the manifest, writing guide, table of contents, all chapter files, and the final reviewed versions without waiting for `start` or `continue`. Automatically use subagents for chapter drafts whenever current tool rules allow it.

After writing files, reply briefly with:
- The parent output folder path.
- The lesson workspace subfolder path.
- The files created.
- Whether the lesson is complete.

## Progress Manifest

Maintain `_lesson-manifest.md` for every lesson run. Use it as the source of truth for progress, review, and recovery if a run is interrupted.

Include:
- Source topic or source file summary.
- Selected parent output folder and actual lesson workspace subfolder.
- Answer format, answer language, and complexity.
- Table of contents.
- File map with planned and completed files.
- Chapter status: `planned`, `in_progress`, `drafted`, `reviewed`, or `complete`.
- Notes about unfinished work, missing source context, review issues, revision requests, and whether each issue was fixed.

Update the manifest whenever a file is created, a chapter is assigned, a chapter is completed, or review changes the status. At the end of a successful run, mark the lesson complete.

## Writing Guide

For multi-chapter lessons, write `00-writing-guide.md` before chapter files. Use it to keep all chapters consistent, especially when using subagents.

Include:
- Audience level: motivated middle-school student.
- Language choice and key-term translation rule.
- Complexity choice, with the reminder that complex mode means more careful explanation, not harder words.
- Tone rules: plain words, natural sentence length, no fancy vocabulary for its own sake.
- Logic rules: no unexplained jumps, show detailed reasoning, use transitions.
- Checklist format and required chapter structure.
- A small glossary of important terms and preferred translations if the selected language is Chinese.
- Boundaries for each chapter so chapters do not duplicate each other too much.

## Explanation Workflow

When producing the lesson:

1. Preserve the original structure as much as possible, but reorganize when a teaching sequence would improve understanding.
2. Cover all concepts, claims, definitions, procedures, examples, assumptions, relationships, and implications. Do not skip steps.
3. Explain with beginner-friendly language. Define necessary background before using it.
4. Keep the logic clear and continuous:
   - Make each idea connect naturally to the previous idea and the next idea.
   - Avoid sudden jumps, unexplained topic changes, or missing middle steps.
   - When explaining causes, formulas, arguments, workflows, or conclusions, show the detailed reasoning path instead of only giving the result.
   - Use transition sentences when moving from one concept to another.
5. Keep the tone clear enough for middle-school-level readers:
   - Use natural sentence length. Sentences may be longer when that makes the explanation smoother, but the wording should stay easy to follow.
   - Prefer common words over impressive words.
   - Explain unavoidable technical terms right away.
   - Use concrete examples before abstract summaries.
   - Never hide weak explanation behind fancy vocabulary.
6. Use multiple teaching methods where helpful:
   - Analogical transfer: connect new concepts to familiar situations.
   - Feynman technique: restate ideas in plain language and test whether they can be taught simply.
   - Elaboration: explain why each point matters and how it connects to nearby ideas.
   - Desirable difficulties: occasionally ask the learner to predict, compare, or explain before revealing the framework.
   - Concept mapping: describe relationships among ideas in words.
   - Spiral learning: revisit core ideas at increasing depth.
   - Retrieval practice: add self-check questions at meaningful points.
7. At key conceptual moments, explicitly separate the learning phases:
   - `Try first`: ask the learner to attempt abstraction, explanation, comparison, or prediction.
   - `Then learn`: provide the systematic framework and standard phrasing.
8. Use diagrams sparingly. Prefer clear prose, lists, definitions, and examples over heavy visual explanation.

## Chapter Format

For each chapter or section, include:

1. A clear title.
2. A short orientation explaining what this chapter will make understandable.
3. The full teaching explanation.
4. Beginner-friendly definitions of new terms, with English translations for key terms when the selected language is Chinese.
5. Examples or analogies where they genuinely improve understanding.
6. `Try first` moments before major abstractions or frameworks.
7. A final Feynman learning checklist with reference answers.

Use this exact checklist pattern, preserving the `details` format:

```markdown
### question xxxxx

<details>
<summary>answer</summary>
xxxxx
</details>
```

Write multiple checklist items per chapter. Questions should test whether the learner can explain, compare, apply, and simplify the chapter's ideas rather than merely recognize terms.

## Multi-Chapter Completion Workflow

When the user chooses multi-chapter mode, or when option `3` leads to a multi-chapter plan:

1. Create the lesson workspace subfolder under the selected parent folder.
2. Write `_lesson-manifest.md`, `00-writing-guide.md`, and `00-table-of-contents.md` to the lesson workspace.
3. Continue directly into chapter generation. Do not stop after the table of contents. Do not ask the user to say `start`.
4. Automatically spawn multiple subagents whenever the subagent tool is available and higher-priority tool rules permit it. Use one subagent per chapter or per clearly bounded chapter group. Treat the user's multi-chapter selection, or the user's option `3` delegation followed by a multi-chapter choice, as an explicit user request for this automatic subagent workflow. Do not ask for separate permission.
5. Give each subagent a disjoint file path and a precise chapter assignment. Tell subagents they are not alone in the workspace, they must not overwrite files outside their assigned chapter path, and they must follow `00-writing-guide.md` and this skill's chapter format.
6. Provide every subagent the shared teaching mode choices, the source material or relevant excerpt, the table of contents, the writing guide, the chapter boundary, and the required output path.
7. Update `_lesson-manifest.md` when chapters are assigned and when chapter files return.
8. If subagents are unavailable or current tool instructions do not permit them, write the chapters sequentially to the same files and briefly tell the user that sequential writing was used.
9. After all chapter drafts are written, the main agent must read every chapter file and perform an editorial review. Check for consistency, factual or reasoning mistakes, missing required checklist sections, duplicated coverage, broken order, unclear transitions, missing reasoning steps, weak explanations, and tone that is too advanced.
10. If a chapter has problems, write concrete revision notes in `_lesson-manifest.md`: chapter file, problem, why it matters, and what must change.
11. Send the revision notes back to the responsible subagent when possible and ask it to edit its assigned file directly. Tell the subagent not to touch other chapter files.
12. Review the revised chapter again. Repeat the review-and-revision loop until the chapter passes or until further subagent revision is unavailable.
13. If a subagent cannot revise, the main agent must fix the chapter directly, then review it again.
14. Mark each chapter `reviewed` only after it passes the main-agent review. Mark the whole lesson complete in `_lesson-manifest.md` only after all chapter files pass review.
15. Reply briefly with the lesson workspace path and created files.

## Interrupted-Run Recovery

The normal workflow should finish the whole lesson after the single mode choice. Only use recovery behavior if the run was interrupted, a tool failed, or the user explicitly asks to resume an incomplete lesson.

When recovery is needed:

1. Check `_lesson-manifest.md`, the parent output folder, the lesson workspace subfolder, and existing files to determine progress.
2. Continue from the next unfinished chapter or incomplete file.
3. Keep writing to files rather than pasting the full lesson into chat.
4. Update `_lesson-manifest.md`.
5. Reply with a short status and the paths updated.

## Quality Bar

Before finalizing each response or file, verify that it:

- Can be understood without the original material.
- Covers the source or topic completely for the chosen scope.
- Has clear logic, smooth context, and no unexplained jumps.
- Shows detailed reasoning for derivations, causes, procedures, and conclusions.
- Uses wording a middle-school student can follow.
- Avoids fancy words when simpler words work.
- Includes explicit teaching supports, not just summary.
- Includes the required Feynman checklist for any completed chapter.
- Was written to a lesson-specific subfolder under the selected parent output folder.
- Keeps `_lesson-manifest.md` current.
- Uses `00-writing-guide.md` for multi-chapter consistency.
- Clearly indicates whether the lesson is complete.
