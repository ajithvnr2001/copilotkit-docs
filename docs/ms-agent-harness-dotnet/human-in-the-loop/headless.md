---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/headless/
title: Headless Interrupts
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:41.699630+00:00
---

# Headless Interrupts

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/headless/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[HITL Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/index)[Pausing the Agent for Input](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/useInterrupt)[Headless Interrupts](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/headless)[Governed Action Approval UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/governed-actions)

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityHuman-in-the-loop

# Headless Interrupts

Resolve agent interrupts from any UI, without a useInterrupt render slot.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not supported on MS Agent Harness (.NET)

MS Agent Harness (.NET) doesn't support Human in the Loop: Headless Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

## What is this?#

`useInterrupt`'s `render` callback is the 80% path: it keeps the UI glued to a `<CopilotChat>` transcript and handles "when to show the picker" logic for you. This page covers the escape hatch: a **render-less** interrupt resolver you assemble from the same primitives `useInterrupt` uses internally — a pattern that lives anywhere in your React tree, takes any shape you like (button grid, form, modal, keyboard shortcut), and resolves the interrupt without mounting a chat at all.

For promise-based integrations there is no native interrupt primitive, so the headless variant uses `useFrontendTool` with a Promise-based handler. The handler exposes its pending payload via React state — so a separate "app surface" can render the picker outside the chat — and resolves the Promise once the user interacts. Same UX, different mechanism.

## When should I use this?#

  * **Testing / Playwright fixtures** — a deterministic, chat-less button grid is easier to drive than a chat surface where the picker only appears after an LLM call.
  * **Non-chat UIs** — dashboards, side panels, inspector surfaces, or any place where you want the _agent's interrupt_ without the _chat transcript_.
  * **Custom flow control** — when you need to know exactly when the interrupt arrived (e.g. to gate other UI) and when it was resolved.
  * **Research / debugging** — when you want to observe the raw AG-UI custom events without the abstraction layer.



If you just want "a picker in chat", just use [`useInterrupt`](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/headless/useInterrupt).

## The primitives#

The render callback intentionally returns `null` — the picker UI lives in the app surface, not in the chat transcript. The handler's pending state drives whether the picker is shown:

Not supported on MS Agent Harness (.NET)

MS Agent Harness (.NET) doesn't support Human in the Loop: Headless Interrupts. See [the framework grid](https://docs.copilotkit.ai/) for which integrations support this feature.

A few things this pattern is careful about:

  * The handler stages its `resolve` callback in a ref keyed by tool-call id, so concurrent tool calls don't trample each other's resolvers.
  * `setPending` is called from inside the handler so the app surface re-renders the picker as soon as the agent calls the tool, and again with `null` after the user interacts so the picker disappears.
  * `render: () => null` keeps the chat transcript clean — the headless variant deliberately bypasses inline rendering.



## Going further#

  * [Tool-based HITL with `useHumanInTheLoop`](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/human-in-the-loop) — for LLM-initiated pauses where the model decides on the fly to ask the user, rather than the runtime forcing the pause itself.
  * [`useInterrupt`](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop/headless/useInterrupt) — the render-prop version of this page, with `enabled` gating and `handler` preprocessing.


