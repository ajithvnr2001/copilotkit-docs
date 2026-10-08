---
url: https://docs.copilotkit.ai/llamaindex/generative-ui/interactive/
title: Interactive components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:14:49.485071+00:00
---

# Interactive components

> Source: https://docs.copilotkit.ai/llamaindex/generative-ui/interactive/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)[Build Generative UI](https://docs.copilotkit.ai/llamaindex/generative-ui)

# Interactive components

Create approval flows where the agent pauses and waits for human input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not supported on LlamaIndex

LlamaIndex doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## What is this?#

Interactive generative UI creates flows where the agent pauses execution and waits for user input before continuing. This enables approval workflows, confirmation dialogs, and any scenario where human judgment is needed mid-execution.

## When should I use this?#

Use interactive generative UI when you need:

  * Approval/rejection flows (e.g. "Run this command?")
  * User decisions that the agent should know about
  * Confirmation dialogs with structured responses
  * Any flow where the agent pauses for human judgment



## How it works in code#

This framework implements the same interactive pause shape with a Promise-based frontend tool. The agent calls `schedule_meeting`, the client renders the picker, and the tool result resolves only after the user chooses a slot or cancels.

Not supported on LlamaIndex

LlamaIndex doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

Not supported on LlamaIndex

LlamaIndex doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.
