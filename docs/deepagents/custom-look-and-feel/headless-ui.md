---
url: https://docs.copilotkit.ai/deepagents/custom-look-and-feel/headless-ui/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:59:28.780717+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/deepagents/custom-look-and-feel/headless-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/reasoning-messages)

[Multimodal Attachments](https://docs.copilotkit.ai/deepagents/multimodal-attachments)[Voice](https://docs.copilotkit.ai/deepagents/voice)[Reasoning](https://docs.copilotkit.ai/deepagents/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Headless UI

BasicsChatCustom Look and Feel

# Headless UI

Build any UI — chat or not — on top of the CopilotKit primitives with zero UI opinions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Deep Agents yet

This feature (`headless-complete`) hasn't been tagged in any Deep Agents cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/custom-look-and-feel/headless-ui), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/custom-look-and-feel/headless-ui), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/headless-ui).

## What is this?#

A headless UI gives you **full control** over the chat experience. You bring your own components, layout, and styling while CopilotKit handles agent communication, message management, tool-call rendering, and streaming. No `<CopilotChat>`, no slot overrides, just your components composed on top of the low-level hooks.

## When should I use this?#

Use headless UI when:

  * The [slot system](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/slots) isn't enough: you need a completely different layout.
  * You're embedding chat into an existing UI with its own patterns.
  * You're building a **non-chat surface** that still talks to an agent (a dashboard, a canvas, an inspector) and want `useRenderToolCall` / `useRenderActivityMessage` on their own.
  * You want to render generative UI primitives outside of a chat entirely.



## The core hooks#

Three hooks power it, and they're the same ones `<CopilotChat>` uses internally.

  * `useAgent({ agentId })` — exposes the current conversation (`messages`, `isRunning`) and the run-state object.
  * `useCopilotKit()` — returns the runtime handle you call `runAgent({ agent })` on.
  * `useRenderToolCall()` — returns a function that paints any registered tool call inline.



## Minimal example#

Start with a hand-rolled message list and composer built from `useAgent` \+ `useCopilotKit`:

Missing snippet

No demo found for `deepagents::headless-simple`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

The message list is a plain `.map()` over `agent.messages`: user messages render as right-aligned bubbles, assistant messages render streamed text plus inline tool calls via `renderToolCall({ toolCall })`:

Missing snippet

No demo found for `deepagents::headless-simple`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

No `<CopilotChat />`, no slots. The trade-off: you only get text and tool calls. Reasoning messages, activity messages, and custom before/after slots won't show up unless you wire them in yourself, which is exactly what the complete example covers.

## Complete example#

The `headless-complete` cell rebuilds the **full** generative-UI composition from the low-level hooks directly, without importing `<CopilotChatMessageView>`: text, tool calls, reasoning cards, A2UI + MCP Apps activity messages, and custom before/after message slots.

### The `useRenderedMessages` hook#

The cell's central piece is a hand-rolled `useRenderedMessages(messages, isRunning)` that returns the same flat list of messages, each augmented with a `renderedContent: ReactNode` field. This hook is a **manual recreation of what`<CopilotChatMessageView>` does**:

Missing snippet

No demo found for `deepagents::headless-complete`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

Three low-level hooks feed it:

  * `useRenderToolCall()` — returns the renderer for any registered tool call (per-tool via `useRenderTool` / `useComponent`, plus the wildcard from `useDefaultRenderTool`).
  * `useRenderActivityMessage()` — renders A2UI + MCP Apps activity messages for the current agent scope.
  * `useRenderCustomMessages()` — invokes `renderCustomMessage` hooks registered against the active `CopilotChatConfigurationProvider`, emitting `"before"` and `"after"` slots around every message.



### Per-role dispatch#

The role-switch mirrors `CopilotChatMessageView`'s `renderMessageBlock` exactly: assistant bodies get text and tool calls, user bodies get their text content, reasoning messages go through the `<CopilotChatReasoningMessage>` leaf, and activity messages route through `renderActivityMessage`:

Missing snippet

No demo found for `deepagents::headless-complete`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

### Tool-call composition#

For each `toolCall` on an assistant message, we look up the sibling `tool`-role message (keyed by `toolCallId`) and hand both to `renderToolCall`:

Missing snippet

No demo found for `deepagents::headless-complete`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

### Bubble chrome#

The `UserBubble` and `AssistantBubble` components are **pure chrome** : they receive the pre-rendered node from `useRenderedMessages` and drop it into a styled container. No chat primitives are imported here:

Missing snippet

No demo found for `deepagents::headless-complete`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

## Next steps#

  * [Slots](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/slots) — less work than going fully headless, often enough.
  * [CSS customization](https://docs.copilotkit.ai/deepagents/custom-look-and-feel/css) — when you just need to re-skin the defaults.



### On this page

What is this?When should I use this?The core hooksMinimal exampleComplete exampleThe useRenderedMessages hookPer-role dispatchTool-call compositionBubble chromeNext steps
