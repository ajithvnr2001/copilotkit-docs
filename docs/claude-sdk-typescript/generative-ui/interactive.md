---
url: https://docs.copilotkit.ai/claude-sdk-typescript/generative-ui/interactive/
title: Interactive components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:54:50.939099+00:00
---

# Interactive components

> Source: https://docs.copilotkit.ai/claude-sdk-typescript/generative-ui/interactive/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-typescript)[Quickstart](https://docs.copilotkit.ai/claude-sdk-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-typescript/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-typescript/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Claude Agent SDK (TypeScript)](https://docs.copilotkit.ai/claude-sdk-typescript)[Build Generative UI](https://docs.copilotkit.ai/claude-sdk-typescript/generative-ui)

# Interactive components

Create approval flows where the agent pauses and waits for human input.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not supported on Claude Agent SDK (TypeScript)

Claude Agent SDK (TypeScript) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## What is this?#

Interactive generative UI creates flows where the agent pauses execution and waits for user input before continuing. This enables approval workflows, confirmation dialogs, and any scenario where human judgment is needed mid-execution.

## When should I use this?#

Use interactive generative UI when you need:

  * Approval/rejection flows (e.g. "Run this command?")
  * User decisions that the agent should know about
  * Confirmation dialogs with structured responses
  * Any flow where the agent pauses for human judgment



## How it works in code#

### Model approvals as async frontend tools

Claude Agent SDK human-in-the-loop demos use CopilotKit's promise-based frontend tool flow. The agent calls an approval tool, the UI resolves the tool result after the user decides, and the same Claude run continues with that result. Register the approval UI from the page component.

page.tsx - useHumanInTheLoop
    
    
    useHumanInTheLoop({
      agentId: "hitl-in-chat",
      name: "book_call",
      description:
        "Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent.",
      parameters: z.object({
        topic: z
          .string()
          .describe("What the call is about (e.g. 'Intro with sales')"),
        attendee: z
          .string()
          .describe("Who the call is with (e.g. 'Alice from Sales')"),
      }),
      render: ({ args, status, respond }: any) => (
        <TimePickerCard
          topic={args?.topic ?? "a call"}
          attendee={args?.attendee}
          slots={DEFAULT_SLOTS}
          status={status}
          onSubmit={(result) => respond?.(result)}
        />
      ),
    });

This framework implements the same interactive pause shape with a Promise-based frontend tool. The agent calls `schedule_meeting`, the client renders the picker, and the tool result resolves only after the user chooses a slot or cancels.

Not supported on Claude Agent SDK (TypeScript)

Claude Agent SDK (TypeScript) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

Not supported on Claude Agent SDK (TypeScript)

Claude Agent SDK (TypeScript) doesn't support Human in the Loop: Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.
