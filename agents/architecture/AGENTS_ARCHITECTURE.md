# README.md — Architecture Documentation for Agents

This directory exists so that any artificial intelligence agent, or any person unfamiliar with the project, can quickly understand how the code is organized and how its parts are connected.

The main architecture documentation must be maintained in the `OUTLINE.md` file, which must be **always up to date**.

## Purpose of `OUTLINE.md`

`OUTLINE.md` must serve as a clear, practical guide that accurately reflects the current state of the project. Its role is to explain the architecture progressively: first the general system overview, and then the details of each part.

It must be written so that someone with no prior context can read it and understand:

- what the project does,
- how its modules are related,
- where each responsibility belongs,
- what external dependencies it uses,
- and what each important file does.

## Required content of `OUTLINE.md`

### 1. General overview at the beginning

At the beginning of the document, there must be a short summary of the project and its architecture.

That section must include:

- a brief explanation of what the project does,
- a simple diagram of how its parts are connected,
- and a quick overview of the system’s general flow.

The idea is that, in a very short time, the reader can understand how everything fits together.

### 2. Dependencies and external libraries

It must include a list of the project’s relevant dependencies and external libraries.

For each one, explain:

- its name,
- what it is used for,
- and what role it plays within the system.

Listing them is not enough. It must be clear why they exist and where they affect the architecture.

### 3. Project structure

After that, the general project structure must appear, reflecting the important folders and files.

Since the organization will follow this structure:

- `agents/`
  - `architecture/`
    - `OUTLINE.md`
    - `AGENTS_ARCHITECTURE.md`
  - `tasks/`
    - `AGENTS_TASKS.md`
- `back/`
- `front/`
- `main.py`

`OUTLINE.md` must explain the responsibility of each main folder and, when useful, also the most relevant subfolders and files.

The goal is not only to show names, but to explain what role each area of the project plays.

### 4. File-by-file explanation

For each relevant code file, `OUTLINE.md` must include:

#### High-level summary

First, a brief explanation in English of what the file does and what its main responsibility is.

#### More detailed explanation

Then, a more precise explanation describing, when applicable:

- important functions, classes, or components,
- internal flow,
- relationship with other files,
- relevant inputs and outputs,
- important architectural decisions,
- and any useful details for understanding the real behavior of the code.

The order must always be:

1. simple summary,
2. more detailed explanation.

## How it should be written

The documentation must be:

- clear,
- direct,
- easy to read,
- useful for someone with no context,
- and aligned with the real state of the project.

It must be written in English, except for file names, paths, libraries, classes, functions, or technical terms that make sense to keep in their original format.

## Main maintenance rule

`OUTLINE.md` must be updated **every time something important changes in the project**.

For example, when:

- a dependency is added or removed,
- an important folder is created, moved, or deleted,
- a relevant file is added,
- the responsibility of a module changes,
- the flow between parts of the system changes,
- or the architecture is refactored.

It must not be left for later. If the project changes, `OUTLINE.md` must also change within the same task.

## Priority: understanding over summarizing

The priority of this document is not to be short, but to be useful.

A slightly longer but clear explanation is preferable to an overly brief description that forces the reader to open many files to understand the basics.

## Real state of the project

The documentation must reflect how the system actually works, not how it should ideally work.

If there are incomplete parts, technical debt, unclear behaviors, or areas pending refactoring, that must also be stated explicitly.

## Purpose of this directory

This directory must work as the documentation entry point for understanding the project.

In particular:

- `agents/architecture/README.md` explains how the architecture documentation must be maintained.
- `agents/architecture/OUTLINE.md` contains the living and detailed documentation of the project’s real architecture.
- `agents/tasks/README.md` may be used to document work rules or task tracking, if applicable.

## Final instruction

If you modify the project, review and update `OUTLINE.md` before considering the work complete.

## Current Architecture Note

The project now has an implemented local persistence layer. The current database setup is documented in `OUTLINE.md` and initialized through `python main.py init-db`. Any future changes to database schema, storage location, backend flow, or dependencies must update `OUTLINE.md` in the same task.

`main.py` also opens the local developer terminal port by default. Any future changes to terminal actions, developer intelligence commands, or entry point behavior must also be reflected in `OUTLINE.md`.
