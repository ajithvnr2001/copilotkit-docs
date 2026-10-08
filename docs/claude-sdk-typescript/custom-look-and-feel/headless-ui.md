---
url: https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/headless-ui/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:54:39.532769+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/headless-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-typescript)[Quickstart](https://docs.copilotkit.ai/claude-sdk-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/reasoning-messages)

[Multimodal Attachments](https://docs.copilotkit.ai/claude-sdk-typescript/multimodal-attachments)[Voice](https://docs.copilotkit.ai/claude-sdk-typescript/voice)[Reasoning](https://docs.copilotkit.ai/claude-sdk-typescript/generative-ui/reasoning)

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

Headless UI

BasicsChatCustom Look and Feel

# Headless UI

Build any UI — chat or not — on top of the CopilotKit primitives with zero UI opinions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

headless-complete-prompt.ts

page.tsx

chat.tsx

use-tool-renderers.tsx

route.ts
    
    
    /** * Headless Chat (Complete) demo — backend agent constants. * * Mirrors `agents/headless_complete.py` in the langgraph-python reference * and the equivalent claude-sdk-python set-up. The cell exercises every * CopilotKit rendering surface in a fully headless chat composed from * `useAgent` (no `<CopilotChat />`). To exercise those surfaces this * agent ships: * *   - two backend tools (`get_weather`, `get_stock_price`) — render via *     app-registered `useRenderTool` renderers on the frontend, *   - access to a frontend-registered `useComponent` tool *     (`highlight_note`) — the agent "calls" it (tool definition is *     forwarded by the AG-UI client) and the UI flows through the same *     `useRenderToolCall` path. * * The system prompt nudges the model toward the right surface per user * question and falls back to plain text otherwise. */import type Anthropic from "@anthropic-ai/sdk";export const HEADLESS_COMPLETE_SYSTEM_PROMPT =  "You are a helpful, concise assistant wired into a headless chat " +  "surface that demonstrates CopilotKit's full rendering stack. Pick " +  "the right surface for each user question and fall back to plain " +  "text when none of the tools fit.\n\n" +  "Routing rules:\n" +  "  - If the user asks about weather for a place, call `get_weather` " +  "with the location.\n" +  "  - If the user asks about a stock or ticker (AAPL, TSLA, MSFT, ...), " +  "call `get_stock_price` with the ticker.\n" +  "  - If the user asks for a revenue, sales, or trend chart, call " +  "`get_revenue_chart`.\n" +  "  - If the user asks you to highlight, flag, or mark a short note " +  "or phrase, call the frontend `highlight_note` tool with the text " +  "and a color (yellow, pink, green, or blue). Do NOT ask the user " +  "for the color — pick a sensible one if they didn't say.\n" +  "  - Otherwise, reply in plain text.\n\n" +  "After a tool returns, write one short sentence summarizing the " +  "result. Never fabricate data a tool could provide.";export const HEADLESS_GET_WEATHER_TOOL_SCHEMA: Anthropic.Tool = {  name: "get_weather",  description:    "Get the current weather for a given location. Returns a mock " +    "payload with city, temperature in Fahrenheit, humidity, wind " +    "speed, and conditions. Use this whenever the user asks about " +    "weather anywhere.",  input_schema: {    type: "object",    properties: {      location: {        type: "string",        description: "The city or region to get weather for.",      },    },    required: ["location"],  },};export const HEADLESS_GET_STOCK_PRICE_TOOL_SCHEMA: Anthropic.Tool = {  name: "get_stock_price",  description:    "Get a mock current price for a stock ticker. Returns a payload " +    "with the ticker symbol (uppercased), price in USD, and percentage " +    "change for the day. Use this whenever the user asks about a stock " +    "price.",  input_schema: {    type: "object",    properties: {      ticker: {        type: "string",        description: "Stock ticker symbol, e.g. 'AAPL'.",      },    },    required: ["ticker"],  },};export const HEADLESS_GET_REVENUE_CHART_TOOL_SCHEMA: Anthropic.Tool = {  name: "get_revenue_chart",  description:    "Return a mock six-month revenue trend chart. Use this when the " +    "user asks for revenue, sales, or trend charts.",  input_schema: {    type: "object",    properties: {},  },};export function getWeatherImpl(location: string): Record<string, unknown> {  return {    city: location,    temperature: 68,    humidity: 55,    wind_speed: 10,    conditions: "Sunny",  };}export function getStockPriceImpl(ticker: string): Record<string, unknown> {  return {    ticker: ticker.toUpperCase(),    price_usd: 189.42,    change_pct: 1.27,  };}export function getRevenueChartImpl(): Record<string, unknown> {  return {    title: "Revenue trend",    subtitle: "Last six months, USD thousands",    data: [      { label: "Jan", value: 42 },      { label: "Feb", value: 48 },      { label: "Mar", value: 53 },      { label: "Apr", value: 57 },      { label: "May", value: 63 },      { label: "Jun", value: 71 },    ],  };}

## What is this?#

A headless UI gives you **full control** over the chat experience. You bring your own components, layout, and styling while CopilotKit handles agent communication, message management, tool-call rendering, and streaming. No `<CopilotChat>`, no slot overrides, just your components composed on top of the low-level hooks.

## When should I use this?#

Use headless UI when:

  * The [slot system](https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/slots) isn't enough: you need a completely different layout.
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

chat.tsx
    
    
      const { agent } = useAgent({ agentId: "headless-simple" });  const { copilotkit } = useCopilotKit();  const [input, setInput] = useState("");  const send = (text: string) => {    const trimmed = text.trim();    if (!trimmed || agent.isRunning) return;    agent.addMessage({      id: createMessageId(),      role: "user",      content: trimmed,    });    setInput("");    void copilotkit.runAgent({ agent }).catch((err) => {      // The Headless Simple demo is the canonical "two hooks, your      // design system" example users copy-paste as a starting point.      // Silently swallowing errors here would model broken practice;      // log so a network failure / runtime error / transport disconnect      // surfaces in the console for the developer.      console.error(        "[claude-sdk-typescript:headless-simple] runAgent failed",        err,      );    });  };

The message list is a plain `.map()` over `agent.messages`: user messages render as right-aligned bubbles, assistant messages render streamed text plus inline tool calls via `renderToolCall({ toolCall })`:

chat.tsx
    
    
                    {visible.map((m) =>                  m.role === "user" ? (                    <UserBubble key={m.id} content={m.content} />                  ) : (                    <AssistantBubble key={m.id} content={m.content} />                  ),                )}

No `<CopilotChat />`, no slots. The trade-off: you only get text and tool calls. Reasoning messages, activity messages, and custom before/after slots won't show up unless you wire them in yourself, which is exactly what the complete example covers.

## Complete example#

The `headless-complete` cell rebuilds the **full** generative-UI composition from the low-level hooks directly, without importing `<CopilotChatMessageView>`: text, tool calls, reasoning cards, A2UI + MCP Apps activity messages, and custom before/after message slots.

### The `useRenderedMessages` hook#

The cell's central piece is a hand-rolled `useRenderedMessages(messages, isRunning)` that returns the same flat list of messages, each augmented with a `renderedContent: ReactNode` field. This hook is a **manual recreation of what`<CopilotChatMessageView>` does**:

message-list.tsx
    
    
      const renderToolCall = useRenderToolCall();  const { renderActivityMessage } = useRenderActivityMessage();  // Index tool results by their originating tool-call id so each tool-call  // card can hand the matching ToolMessage to `useRenderToolCall`.  // Without this the renderer can't see a result and the card stays in the  // "in-progress" state forever.  const toolMessagesByCallId = useMemo(() => {    const map = new Map<string, ToolResult>();    for (const m of messages) {      if (m.role === "tool" && "toolCallId" in m && m.toolCallId) {        map.set(m.toolCallId, m);      }    }    return map;  }, [messages]);

Three low-level hooks feed it:

  * `useRenderToolCall()` — returns the renderer for any registered tool call (per-tool via `useRenderTool` / `useComponent`, plus the wildcard from `useDefaultRenderTool`).
  * `useRenderActivityMessage()` — renders A2UI + MCP Apps activity messages for the current agent scope.
  * `useRenderCustomMessages()` — invokes `renderCustomMessage` hooks registered against the active `CopilotChatConfigurationProvider`, emitting `"before"` and `"after"` slots around every message.



### Per-role dispatch#

The role-switch mirrors `CopilotChatMessageView`'s `renderMessageBlock` exactly: assistant bodies get text and tool calls, user bodies get their text content, reasoning messages go through the `<CopilotChatReasoningMessage>` leaf, and activity messages route through `renderActivityMessage`:

message-list.tsx
    
    
          {messages.map((m) => {        if (m.role === "user") {          // Cast through the local input shape — UserBubble accepts a          // simplified version of the ag-ui content union.          return (            <UserBubble              key={m.id}              content={m.content as Parameters<typeof UserBubble>[0]["content"]}            />          );        }        if (m.role === "assistant") {          const toolCalls =            "toolCalls" in m && Array.isArray(m.toolCalls) ? m.toolCalls : [];          return (            <AssistantBubble              key={m.id}              content={typeof m.content === "string" ? m.content : undefined}            >              {toolCalls.map((tc) => {                const toolMessage = toolMessagesByCallId.get(tc.id);                const node = renderToolCall({                  toolCall: tc,                  toolMessage,                });                return node ? <div key={tc.id}>{node}</div> : null;              })}            </AssistantBubble>          );        }        if (m.role === "activity") {          const node = renderActivityMessage(m);          if (!node) return null;          return <ActivityWrapper key={m.id}>{node}</ActivityWrapper>;        }        return null;      })}

### Tool-call composition#

For each `toolCall` on an assistant message, we look up the sibling `tool`-role message (keyed by `toolCallId`) and hand both to `renderToolCall`:

message-list.tsx
    
    
                  {toolCalls.map((tc) => {                const toolMessage = toolMessagesByCallId.get(tc.id);                const node = renderToolCall({                  toolCall: tc,                  toolMessage,                });                return node ? <div key={tc.id}>{node}</div> : null;              })}

### Bubble chrome#

The `UserBubble` and `AssistantBubble` components are **pure chrome** : they receive the pre-rendered node from `useRenderedMessages` and drop it into a styled container. No chat primitives are imported here:

message-assistant.tsx
    
    
    export function AssistantBubble({  content,  children,}: {  content?: string;  children?: React.ReactNode;}) {  const hasText = typeof content === "string" && content.trim().length > 0;  const hasChildren = React.Children.count(children) > 0;  if (!hasText && !hasChildren) return null;  return (    <div      data-testid="headless-message-assistant"      data-message-role="assistant"      className="flex w-full items-start gap-3"    >      <Avatar className="h-8 w-8 shrink-0 border bg-muted text-muted-foreground">        <AvatarFallback className="bg-muted text-muted-foreground">          <Bot className="h-4 w-4" />        </AvatarFallback>      </Avatar>      <div className="flex max-w-[calc(100%-2.75rem)] flex-1 flex-col items-start gap-2">        {hasText && (          <div            className={cn(              "max-w-[90%] rounded-2xl rounded-tl-sm px-4 py-2.5 text-sm leading-relaxed shadow-sm",              "bg-muted text-foreground",            )}          >            <ReactMarkdown              remarkPlugins={[remarkGfm]}              components={{                p: ({ children }) => (                  <p className="my-1 first:mt-0 last:mb-0">{children}</p>                ),                ul: ({ children }) => (                  <ul className="my-1 list-disc pl-5">{children}</ul>                ),                ol: ({ children }) => (                  <ol className="my-1 list-decimal pl-5">{children}</ol>                ),                li: ({ children }) => <li className="my-0.5">{children}</li>,                code: ({ children, className }) => {                  const isBlock = (className ?? "").includes("language-");                  if (isBlock) {                    return <code className={className}>{children}</code>;                  }                  return (                    <code className="rounded bg-background px-1 py-0.5 font-mono text-[0.85em]">                      {children}                    </code>                  );                },                pre: ({ children }) => (                  <pre className="my-2 overflow-x-auto rounded-md bg-background p-3 font-mono text-xs">                    {children}                  </pre>                ),                a: ({ children, href }) => (                  <a                    href={href}                    target="_blank"                    rel="noreferrer noopener"                    className="text-primary underline underline-offset-2 hover:opacity-80"                  >                    {children}                  </a>                ),                strong: ({ children }) => (                  <strong className="font-semibold">{children}</strong>                ),                h1: ({ children }) => (                  <h1 className="my-2 text-base font-semibold">{children}</h1>                ),                h2: ({ children }) => (                  <h2 className="my-2 text-base font-semibold">{children}</h2>                ),                h3: ({ children }) => (                  <h3 className="my-2 text-sm font-semibold">{children}</h3>                ),                blockquote: ({ children }) => (                  <blockquote className="my-2 border-l-2 border-border pl-3 italic text-muted-foreground">                    {children}                  </blockquote>                ),              }}            >              {content as string}            </ReactMarkdown>          </div>        )}        {hasChildren && (          <div className="flex w-full max-w-full flex-col gap-2">            {children}          </div>        )}      </div>    </div>  );}export function UserBubble({  content,}: {  content: string | MultimodalPart[];}) {  const { text, attachments } = splitContent(content);  const hasText = text.trim().length > 0;  const hasAttachments = attachments.length > 0;  if (!hasText && !hasAttachments) return null;  return (    <div      data-testid="headless-message-user"      data-message-role="user"      className="flex w-full items-start gap-3 flex-row-reverse"    >      <Avatar className="h-8 w-8 shrink-0 border bg-primary text-primary-foreground">        <AvatarFallback className="bg-primary text-primary-foreground">          <User className="h-4 w-4" />        </AvatarFallback>      </Avatar>      <div className="flex max-w-[80%] flex-col items-end gap-2">        {hasAttachments && (          <div className="flex flex-wrap justify-end gap-2">            {attachments.map((a) => (              <AttachmentChip key={a.id} attachment={a} />            ))}          </div>        )}        {hasText && (          <div            className={cn(              "rounded-2xl rounded-tr-sm px-4 py-2.5 text-sm leading-relaxed shadow-sm",              "bg-primary text-primary-foreground",            )}          >            <p className="whitespace-pre-wrap break-words">{text}</p>          </div>        )}      </div>    </div>  );}function splitContent(content: string | MultimodalPart[]): {  text: string;  attachments: Attachment[];} {  if (typeof content === "string") {    return { text: content, attachments: [] };  }  let text = "";  const attachments: Attachment[] = [];  let i = 0;  for (const part of content) {    if (part.type === "text") {      text += part.text;      continue;    }    const meta = (part.metadata ?? {}) as {      filename?: string;      size?: number;    };    attachments.push({      id: `${part.type}-${i++}`,      type: part.type,      source: part.source,      filename: meta.filename,      size: meta.size,      status: "ready",    });  }  return { text, attachments };}

## Next steps#

  * [Slots](https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/slots) — less work than going fully headless, often enough.
  * [CSS customization](https://docs.copilotkit.ai/claude-sdk-typescript/custom-look-and-feel/css) — when you just need to re-skin the defaults.



### On this page

What is this?When should I use this?The core hooksMinimal exampleComplete exampleThe useRenderedMessages hookPer-role dispatchTool-call compositionBubble chromeNext steps
