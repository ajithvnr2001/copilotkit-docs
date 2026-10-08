---
url: https://docs.copilotkit.ai/deepagents/headless/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:00:15.530039+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/deepagents/headless/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

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

[Deep Agents](https://docs.copilotkit.ai/deepagents)

# Headless UI

Build fully custom chat interfaces with complete rendering control via hooks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Not available for Deep Agents yet

This feature (`headless-complete`) hasn't been tagged in any Deep Agents cell yet. Try [CopilotKit's Built-in Agent](https://docs.copilotkit.ai/built-in-agent/headless), [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/headless), [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/headless).

## Full rendering control via hooks#

CopilotKit's headless hooks give you complete control over the chat experience: you compose messages, streaming, and tool-call surfaces yourself with zero UI opinions. Bring your own design system and render everything your way.

There are two live cells on this page. Start with **Minimal** for the smallest possible custom chat on `useAgent` \+ `useCopilotKit`, then jump to **Complete** to see the full generative-UI composition (tool calls, reasoning, activity messages, custom before/after slots) rebuilt by hand from the low-level hooks.

## When should I use this?#

Use headless UI when you want to:

  * Build a completely custom chat interface with your own design system
  * Integrate agent chat into existing UI patterns
  * Have full control over message rendering and interaction
  * Drop generative UI primitives (`useRenderToolCall`, `useRenderActivityMessage`, `useRenderCustomMessages`) into a layout that isn't a chat at all



## Minimal (`headless-simple`)#

The bare minimum: three hooks do the heavy lifting.

  * `useAgent({ agentId })` exposes the current conversation (`messages`, `isRunning`) and the run-state object.
  * `useCopilotKit()` returns the runtime handle you call `runAgent({ agent })` on (the same entry point `<CopilotChat />` uses internally).
  * `useComponent(...)` (sugar over `useFrontendTool`) lets you register a React component the agent can render by invoking a named tool call. `useRenderToolCall()` then returns a function that paints any tool call inline.



Missing snippet

No demo found for `deepagents::headless-simple`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

The message list is a plain `.map()` over `agent.messages`: user messages render as right-aligned bubbles, assistant messages render any streamed text plus inline tool calls via `renderToolCall({ toolCall })`:

Missing snippet

No demo found for `deepagents::headless-simple`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

That's it: no `<CopilotChat />`, no `<CopilotChatMessageView>`, no slots. The downside: you only get text + tool calls. Reasoning messages, activity messages (A2UI, MCP Apps), and custom before/after slots won't show up unless you wire them in yourself, which is exactly what the next section covers.

## Complete (`headless-complete`)#

This is the heart of the page. The `headless-complete` cell rebuilds the **full** generative-UI weave (text, tool calls via `useRenderTool` / `useDefaultRenderTool` / `useComponent` / `useFrontendTool`, reasoning cards, A2UI + MCP Apps activity messages, and custom before/after message slots) from the low-level hooks directly, without importing `<CopilotChatMessageView>` or `<CopilotChatAssistantMessage>`.

### The `useRenderedMessages` hook#

The cell's central piece is a hand-rolled `useRenderedMessages(messages, isRunning)` that returns the same flat list of messages, each augmented with a `renderedContent: ReactNode` field. This hook is a **manual recreation of what`<CopilotChatMessageView>` does**; compare it line-for-line against the `renderMessageBlock` helper inside the canonical primitive: [`packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx:542-612`](https://github.com/CopilotKit/CopilotKit/blob/main/packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx#L542-L612).

Missing snippet

No demo found for `deepagents::headless-complete`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

Three low-level hooks feed it:

  * `useRenderToolCall()` — returns the renderer for any registered tool call (per-tool via `useRenderTool` / `useComponent`, plus the wildcard from `useDefaultRenderTool`).
  * `useRenderActivityMessage()` — renders A2UI + MCP Apps activity messages for the current agent scope.
  * `useRenderCustomMessages()` — invokes `renderCustomMessage` hooks registered against the active `CopilotChatConfigurationProvider`, emitting `"before"` and `"after"` slots around every message.



### Per-role dispatch#

Inside `renderMessageContent` the role-switch mirrors `CopilotChatMessageView`'s `renderMessageBlock` exactly: assistant bodies get text + tool calls, user bodies get their text content, reasoning messages go through the `<CopilotChatReasoningMessage>` leaf component, and activity messages route through `renderActivityMessage`:

Missing snippet

No demo found for `deepagents::headless-complete`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

### Tool-call composition#

For each `toolCall` on an assistant message, we look up the sibling `tool`-role message (keyed by `toolCallId`) and hand both to `renderToolCall`. This mirrors `CopilotChatToolCallsView` exactly:

Missing snippet

No demo found for `deepagents::headless-complete`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.

### Bubble chrome#

The `UserBubble` and `AssistantBubble` components are **pure chrome** : they receive the pre-rendered node from `useRenderedMessages` and drop it into a styled container. No chat primitives are imported here:

Missing snippet

No demo found for `deepagents::headless-complete`. Known demos are bundled from manifest `demos[i]`; check the cell id and framework slug.
