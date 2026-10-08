---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/headless/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:37.301185+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/headless/

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

[MS Agent Harness (.NET)](https://docs.copilotkit.ai/ms-agent-harness-dotnet)

# Headless UI

Build fully custom chat interfaces with complete rendering control via hooks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

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

Region `use-agent-simple` not found in `ms-agent-harness-dotnet::headless-simple`. Tag the relevant source lines with `// @region[use-agent-simple]` / `// @endregion[use-agent-simple]`.

The message list is a plain `.map()` over `agent.messages`: user messages render as right-aligned bubbles, assistant messages render any streamed text plus inline tool calls via `renderToolCall({ toolCall })`:

Missing snippet

Region `message-list-simple` not found in `ms-agent-harness-dotnet::headless-simple`. Tag the relevant source lines with `// @region[message-list-simple]` / `// @endregion[message-list-simple]`.

That's it: no `<CopilotChat />`, no `<CopilotChatMessageView>`, no slots. The downside: you only get text + tool calls. Reasoning messages, activity messages (A2UI, MCP Apps), and custom before/after slots won't show up unless you wire them in yourself, which is exactly what the next section covers.

## Complete (`headless-complete`)#

This is the heart of the page. The `headless-complete` cell rebuilds the **full** generative-UI weave (text, tool calls via `useRenderTool` / `useDefaultRenderTool` / `useComponent` / `useFrontendTool`, reasoning cards, A2UI + MCP Apps activity messages, and custom before/after message slots) from the low-level hooks directly, without importing `<CopilotChatMessageView>` or `<CopilotChatAssistantMessage>`.

### The `useRenderedMessages` hook#

The cell's central piece is a hand-rolled `useRenderedMessages(messages, isRunning)` that returns the same flat list of messages, each augmented with a `renderedContent: ReactNode` field. This hook is a **manual recreation of what`<CopilotChatMessageView>` does**; compare it line-for-line against the `renderMessageBlock` helper inside the canonical primitive: [`packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx:542-612`](https://github.com/CopilotKit/CopilotKit/blob/main/packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx#L542-L612).

use-rendered-messages.tsx
    
    
    import React, { useMemo } from "react";import type {  Message,  AssistantMessage,  UserMessage,  ReasoningMessage,  ActivityMessage,  ToolMessage,} from "@ag-ui/core";import {  CopilotChatReasoningMessage,  useRenderToolCall,  useRenderActivityMessage,  useRenderCustomMessages,} from "@copilotkit/react-core/v2";/** * Manual per-message composition for the TRULY headless chat cell. * * This hook mirrors — line-for-line in spirit — the role-dispatch that happens * inside `renderMessageBlock` in the canonical primitive: * *   packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx:542-612 * * The point of this cell is to demonstrate that the FULL generative-UI weave * (assistant text + tool-call renders + reasoning + activity + custom before / * after slots) can be re-composed from the low-level hooks directly, without * importing `<CopilotChatMessageView>` or `<CopilotChatAssistantMessage>`. * Only the reasoning-message LEAF component is imported — it's a pure * presentational primitive, not a dispatcher. * * Return shape: the original messages, each augmented with a `renderedContent` * field that the parent list drops directly into a `<UserBubble>` or * `<AssistantBubble>` chrome wrapper. * * Text rendering: we intentionally use plain text (a `<div>` with * `whitespace-pre-wrap`) rather than a markdown pipeline. Rationale: the cell's * goal is to show what "truly headless" looks like — every piece of composition * lives in user code — so pulling in a markdown library here would re-hide * a chunk of formatting decisions behind an opaque black box. Apps that want * markdown can drop Streamdown / react-markdown in at this exact line. */export type RenderedMessage = Message & { renderedContent: React.ReactNode };export function useRenderedMessages(  messages: Message[],  isRunning: boolean,): RenderedMessage[] {  const renderToolCall = useRenderToolCall();  const { renderActivityMessage } = useRenderActivityMessage();  const renderCustomMessage = useRenderCustomMessages();  return useMemo(() => {    return messages.map((message): RenderedMessage => {      const renderedContent = renderMessageContent({        message,        messages,        isRunning,        renderToolCall,        renderActivityMessage,        renderCustomMessage,      });      return { ...message, renderedContent } as RenderedMessage;    });    // `renderToolCall`, `renderActivityMessage`, and `renderCustomMessage` are    // callbacks produced by their respective hooks; their identity turns over    // whenever the underlying registries / agent / config change, which is    // exactly when we want to recompute.  }, [    messages,    isRunning,    renderToolCall,    renderActivityMessage,    renderCustomMessage,  ]);}

Three low-level hooks feed it:

  * `useRenderToolCall()` — returns the renderer for any registered tool call (per-tool via `useRenderTool` / `useComponent`, plus the wildcard from `useDefaultRenderTool`).
  * `useRenderActivityMessage()` — renders A2UI + MCP Apps activity messages for the current agent scope.
  * `useRenderCustomMessages()` — invokes `renderCustomMessage` hooks registered against the active `CopilotChatConfigurationProvider`, emitting `"before"` and `"after"` slots around every message.



### Per-role dispatch#

Inside `renderMessageContent` the role-switch mirrors `CopilotChatMessageView`'s `renderMessageBlock` exactly: assistant bodies get text + tool calls, user bodies get their text content, reasoning messages go through the `<CopilotChatReasoningMessage>` leaf component, and activity messages route through `renderActivityMessage`:

use-rendered-messages.tsx
    
    
      if (message.role === "assistant") {    body = renderAssistantBody({      message: message as AssistantMessage,      messages,      renderToolCall,    });  } else if (message.role === "user") {    body = renderUserBody(message as UserMessage);  } else if (message.role === "reasoning") {    body = (      <CopilotChatReasoningMessage        message={message as ReasoningMessage}        messages={messages}        isRunning={isRunning}      />    );  } else if (message.role === "activity") {    body = renderActivityMessage(message as ActivityMessage);  }

### Tool-call composition#

For each `toolCall` on an assistant message, we look up the sibling `tool`-role message (keyed by `toolCallId`) and hand both to `renderToolCall`. This mirrors `CopilotChatToolCallsView` exactly:

use-rendered-messages.tsx
    
    
    function renderAssistantBody(args: {  message: AssistantMessage;  messages: Message[];  renderToolCall: ReturnType<typeof useRenderToolCall>;}): React.ReactNode {  const { message, messages, renderToolCall } = args;  const text = message.content ?? "";  const hasText = text.trim().length > 0;  const toolCalls = message.toolCalls ?? [];  return (    <>      {hasText && <div className="whitespace-pre-wrap break-words">{text}</div>}      {toolCalls.map((toolCall) => {        // Tool result lives on a sibling `tool`-role message keyed by toolCallId.        // Mirrors CopilotChatToolCallsView (react-core/v2/components/chat/CopilotChatToolCallsView.tsx).        const toolMessage = messages.find(          (m) => m.role === "tool" && m.toolCallId === toolCall.id,        ) as ToolMessage | undefined;        return (          <React.Fragment key={toolCall.id}>            {renderToolCall({ toolCall, toolMessage })}          </React.Fragment>        );      })}    </>  );}

### Bubble chrome#

The `UserBubble` and `AssistantBubble` components are **pure chrome** : they receive the pre-rendered node from `useRenderedMessages` and drop it into a styled container. No chat primitives are imported here:

message-list.tsx
    
    
    function UserBubble({ children }: { children: React.ReactNode }) {  return (    <div className="flex justify-end">      <div className="max-w-[75%] rounded-2xl rounded-br-sm bg-[#010507] text-white px-4 py-2 text-sm whitespace-pre-wrap break-words">        {children}      </div>    </div>  );}function AssistantBubble({ children }: { children: React.ReactNode }) {  if (isEmpty(children)) return null;  return (    <div className="flex justify-start">      <div className="max-w-[85%] flex flex-col gap-2">        <div className="rounded-2xl rounded-bl-sm bg-[#F0F0F4] text-[#010507] px-4 py-2 text-sm">          {children}        </div>      </div>    </div>  );}
