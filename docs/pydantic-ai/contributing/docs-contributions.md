---
url: https://docs.copilotkit.ai/pydantic-ai/contributing/docs-contributions/
title: Documentation Contributions
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:23:28.667685+00:00
---

# Documentation Contributions

> Source: https://docs.copilotkit.ai/pydantic-ai/contributing/docs-contributions/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/pydantic-ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/pydantic-ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/pydantic-ai/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Code Contributions](https://docs.copilotkit.ai/pydantic-ai/contributing/code-contributions)[Documentation Contributions](https://docs.copilotkit.ai/pydantic-ai/contributing/docs-contributions)

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/pydantic-ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Documentation Contributions

OtherContributing

# Documentation Contributions

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

We move quickly and our docs sometimes lag the code, so contributions to the documentation site are very welcome.

The documentation site lives in `showcase/shell-docs` inside the [CopilotKit](https://github.com/CopilotKit/CopilotKit) monorepo. It is a [Fumadocs](https://fumadocs.dev/) site; the legacy Nextra `docs/` tree is being phased out and is no longer the right place to author new content.

## Prerequisites#

  * [Node.js](https://nodejs.org/en/) 20.x or later
  * [pnpm](https://pnpm.io/) v10.x installed globally (`npm i -g pnpm@^10`)
  * [Nx](https://nx.dev/) — used to drive all tasks in the monorepo. You don't need to install it globally; the repo's `pnpm install` provides everything.



## How To Contribute#

### Fork and clone the repository#

First, fork the [CopilotKit GitHub repository](https://github.com/CopilotKit/CopilotKit), then clone your fork:
    
    
    git clone https://github.com/<your-username>/CopilotKit
    cd CopilotKit
    pnpm install

`pnpm install` at the repo root installs every package in the workspace and wires up the lefthook pre-commit hook (lint, format, test) — running it once is required before your first commit.

### Run the documentation site locally#

The shell-docs site is an Nx project (`@copilotkit/showcase-shell-docs`). Run it through Nx from the repo root:
    
    
    nx run shell-docs:dev

The site is served at <http://localhost:3003>. If you prefer to run it from the package directory, `cd showcase/shell-docs && pnpm dev` works too — both go through the same script.

Always prefer running tasks via Nx (`nx run`, `nx run-many`, `nx affected`) rather than the underlying tooling directly. This is the convention across the monorepo and ensures task dependencies are respected.

### Make your changes#

Documentation pages live under:
    
    
    showcase/shell-docs/src/content/docs/

A few conventions to keep in mind:

  * The site is built with **Fumadocs**. Content is authored in MDX. Frontmatter (`title`, `description`, `icon`, etc.) drives the sidebar and metadata.
  * For code samples, prefer the **`<Snippet>` region pattern** over hand-inlining code blocks. `<Snippet>` pulls real source from the showcase integrations under `showcase/integrations/<framework>/...` using region markers (e.g. `// region:my-region` … `// endregion:my-region`). This keeps every code sample tied to runnable demo code and lets us catch drift automatically. When in doubt, look at how an adjacent page references the same integration and follow that pattern.
  * Reference pages for hooks, components, and runtime APIs use a `<PropertyReference>` component to render the prop / parameter table. Match the style of an existing reference page in the same directory.



Please review your changes for grammar, spelling, and formatting, and confirm that links, code blocks, and images render correctly in the local dev server before opening a PR.

### Review changes and submit a pull request#

Before pushing, the lefthook pre-commit hook will run lint, format, and tests on the affected projects via Nx. If anything fails, fix the issue and commit again — don't bypass the hook.

When you're happy with the result, push and open a PR against the [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit/pulls) repo. Thank you for your contribution!

## Need help?#

If you need help with anything, please don't hesitate to reach out on [Discord](https://discord.gg/6dffbvGU3D). There's a dedicated [#contributing](https://discord.com/channels/1122926057641742418/1183863183149117561) channel.

### On this page

PrerequisitesHow To ContributeNeed help?
