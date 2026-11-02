# Sideways pointers: why they exist, and what replaces them

<!-- A draft: why today's manuals point sideways at each other, what
     the new layering does with each kind, and what else changes with
     it. Read in the exchange and facts-in-sync manuals, 2026-11-02.
     The layering: temp/model-example/layers.md. -->

## 1. Why they exist today

Six kinds, read in the exchange and facts-in-sync manuals:

| Kind | Example | Why it is there |
|---|---|---|
| 1. A borrowed fact | The Delivery Take: "its commits follow `docs/conventions/commit-messages/`" | One manual relies on a fact another owns. Pointing is the only way to rely on another idea |
| 2. A fact split over two manuals | Stripping the *Decisions* footer from a shipped copy: facts-in-sync says the strip is the Exchange Convention's; exchange says why it goes is facts-in-sync's | One subject's parts landed in two manuals, each pointing at the other: a loop |
| 3. An example | facts-in-sync shows the pointer form with real exchange sections | Real paths used as illustrations; they break when those sections are renumbered |
| 4. A boundary | *What this does not cover* lists neighbouring manuals by path | The manual's form asks for it |
| 5. The channel | *Why it arrives this way* points at the Agent Model and agent-arrangement | The manual's form asks for it |
| 6. Rules about writing rules | Pointers to the conventions manual and to writing | Each manual stands on the one that sets its form |

Pointers up to an Idea Model point up, and are not the problem.

**The cause.** A manual holds several subjects and both seats, so at
its edges it touches other manuals' subjects. With no way to say "I
need X" without naming who gives X, the only way to rely on something
is to point at it.

## 2. In the new model

| Kind | Becomes |
|---|---|
| 1. A borrowed fact | The idea states a need in its own words: "commits in one stable form". The project text wires the need to the idea that meets it. The pointer moves from sideways, idea to idea, to up, project text to both ideas |
| 2. A fact split over two manuals | One home. The strip is a choice this repo made: one project text |
| 3. An example | Gone. An idea names no path; its examples are in plain words |
| 4. A boundary | Gone as a pointer. The idea's *Limits* says what it does not do; the idea map, read from the project texts, shows its neighbours |
| 5. The channel | One of *What each project decides*, answered in the project text |
| 6. Rules about writing rules | Each text names its template and the template's date: one pointer, to the template |

## 3. How the pointers differ

| | Today | New |
|---|---|---|
| Direction | Any: up, sideways, in loops | Up only: Work Approach to project text, project text to ideas, each text to its template |
| Form | Path, section number, title | Path and heading, with a "relies on" line |
| What it relies on | Unsaid: the sentence is read to know | Said, in the "relies on" line |
| How many | facts-in-sync: 37 paths, 18 ADRs | An idea: 0. A project text: the ideas it draws on. A Work Approach: 1 |
| ADR citations | Inside a manual's sentences | The idea holds its own why. ADRs stay as the project's history, cited from the project text |

## 4. What else changes

1. **The manual's nine sections** give way to three templates: idea,
   project text, Work Approach.
2. **The Foundation Line** becomes the project text's *Draws on*.
3. **The Change Walk is narrower.** A change flows only down, from the
   changed text to what draws on it.
4. **Renumbering costs nothing.** Pointers carry headings, not
   numbers.
5. **The seats go.** Each seat is a project text of its own.
6. **The paired Agent Skills and Agent Rules,** about 1,400 lines,
   become one idea each, with a small project text for each seat.
7. **Shipping, open.** A Work Approach points up at its project text,
   which a CBC Run cannot open. Either the kit's project text ships
   with it, or the pointer is stripped at shipping.
8. **The glossary, open.** Likely a list of names, each pointing at the
   idea that defines it.
9. **The writing rules still apply,** with far less to check: no
   section numbers, and fewer pointers.

Open 7 and 8 are settled before exchange moves: exchange is the idea
of shipping itself.
