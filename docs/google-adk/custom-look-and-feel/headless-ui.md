---
url: https://docs.copilotkit.ai/google-adk/custom-look-and-feel/headless-ui/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:48.266208+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/google-adk/custom-look-and-feel/headless-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/reasoning-messages)

[Multimodal Attachments](https://docs.copilotkit.ai/google-adk/multimodal-attachments)[Voice](https://docs.copilotkit.ai/google-adk/voice)[Reasoning](https://docs.copilotkit.ai/google-adk/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

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

shared_chat.py

page.tsx

chat.tsx

route.ts
    
    
    """Shared LlmAgent factories used across multiple demos.`build_simple_chat_agent` produces a plain Gemini chat agent with no backendtools — appropriate for any demo whose only customisation is on the frontend(prebuilt-sidebar, prebuilt-popup, chat-slots, chat-customization-css,headless-simple, headless-complete, voice, frontend-tools, agentic-chat).`build_thinking_chat_agent` uses Gemini 3.1 Flash-Lite with the thinking_configexposed so reasoning is streamed back as `thought` parts; the v2 React corerenders these via CopilotChatReasoningMessage.`get_model` returns a `Gemini` instance configured with the aimock proxyendpoint when `GOOGLE_GEMINI_BASE_URL` is set, or the default model stringotherwise. All agent modules should call `get_model()` instead ofhard-coding `"gemini-3.1-flash-lite"` so Railway deployments route throughaimock.`stop_on_terminal_text` is the canonical after_model_callback shared by everyregistered LlmAgent. Gemini 3.1 Flash-Lite does not naturally end its agenticloop after a successful tool call — it keeps re-issuing the same tool. Thecallback inspects each non-partial model response and, when it containstext with no pending function_call, sets `_invocation_context.end_invocation= True` so ADK terminates the loop. Without this guard every backend orfrontend tool in this package fires infinitely."""from __future__ import annotationsimport loggingimport osfrom typing import Optional, Unionfrom google.adk.agents import LlmAgentfrom google.adk.agents.callback_context import CallbackContextfrom google.adk.models.google_llm import Geminifrom google.adk.models.llm_response import LlmResponsefrom google.genai import typesfrom ag_ui_adk import AGUIToolsetfrom agents._header_forwarding import install_httpx_hooklogger = logging.getLogger(__name__)DEFAULT_MODEL = "gemini-3.1-flash-lite"def stop_on_terminal_text(    callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:    """Terminate the ADK agentic loop on a final text-only model turn.    Lifted from the (orphaned) `simple_after_model_modifier` in    `agents/main.py`, with the SalesPipelineAgent name-gate removed so it    applies to every registered agent. Guards:    1. Skip partial streaming events — never end on a mid-stream chunk       (belt-and-suspenders with `ADK_DISABLE_PROGRESSIVE_SSE_STREAMING=1`       in `entrypoint.sh`).    2. Only terminate when the final non-partial response contains TEXT       and NO pending function_call — mixed text+function_call responses       (a known Gemini Flash quirk) must NOT terminate.    3. `_invocation_context` is an ADK private attribute; if it disappears       in a future ADK release, log-and-degrade rather than crash the       callback (which would stall the request).    Without this guard, Gemini calls the same tool indefinitely after a    successful tool result because no native termination condition fires.    """    content = llm_response.content    if not content or not content.parts:        if llm_response.error_message:            logger.warning(                "stop_on_terminal_text: Gemini returned error_message for agent=%s: %s",                callback_context.agent_name,                llm_response.error_message,            )        return None    if getattr(llm_response, "partial", False):        return None    # Under thinking mode (`include_thoughts=True`), Gemini emits a turn    # as TWO separate non-partial chunks:    #   1. text-only chunk: thought + reply text, `finish_reason=None`    #   2. function_call-only chunk: `finish_reason=FUNCTION_CALL`    # The callback fires on both. Without the finish_reason guard below,    # chunk 1's text-without-function-call shape causes premature    # termination — the function call in chunk 2 still streams but the    # agentic loop is already marked `end_invocation=True`, so the    # post-tool-result re-invocation that would chain to the next tool    # never happens (tool-rendering-reasoning-chain AAPL→MSFT regression).    # Only terminate when Gemini signals the turn is genuinely done with    # `finish_reason=STOP` (no further chunks coming). FUNCTION_CALL and    # None mean "more chunks are inbound" — defer.    finish_reason = getattr(llm_response, "finish_reason", None)    finish_reason_name = (        getattr(finish_reason, "name", None) if finish_reason is not None else None    )    if finish_reason_name != "STOP" and finish_reason != "STOP":        return None    has_text = any(getattr(part, "text", None) for part in content.parts)    has_function_call = any(        getattr(part, "function_call", None) for part in content.parts    )    if content.role != "model" or not has_text or has_function_call:        return None    invocation_context = getattr(callback_context, "_invocation_context", None)    if invocation_context is None:        logger.debug(            "stop_on_terminal_text: callback_context has no "            "_invocation_context attribute; skipping end_invocation."        )        return None    try:        invocation_context.end_invocation = True    except AttributeError:        logger.debug(            "stop_on_terminal_text: _invocation_context lacks "            "end_invocation; ADK private-API shape may have drifted."        )    return Nonedef get_model(model: str = DEFAULT_MODEL) -> Union[str, Gemini]:    """Return a model suitable for LlmAgent's `model=` parameter.    When `GOOGLE_GEMINI_BASE_URL` is set (Railway aimock proxy), returns a    `Gemini` instance with its `base_url` pointed at the proxy. Otherwise    returns the plain model string so the ADK resolves the default endpoint.    """    base_url = os.environ.get("GOOGLE_GEMINI_BASE_URL")    if base_url:        gemini = Gemini(model=model, base_url=base_url)        # Walk Gemini's ``._client`` chain and attach the request hook so        # inbound x-* headers (e.g. ``x-aimock-context``) ride along on        # outbound calls to the aimock proxy.        install_httpx_hook(gemini)        return gemini    return modeldef get_a2ui_model(model: str = DEFAULT_MODEL) -> Gemini:    """Return a concrete ``Gemini`` BaseLlm for the A2UI sub-agent.    The middleware's ``get_a2ui_tool({"model": ...})`` invokes the model    directly (forced ``render_a2ui`` call), so it needs a model *object*, not    the bare string ``get_model`` may return for ``LlmAgent.model=``. This    mirrors ``get_model``'s aimock-proxy wiring (base_url + x-header hook) so    the sub-agent's Gemini calls route through the same proxy as the primary    agent and match the same aimock fixtures. (The auto-inject path got this    object for free from the agent's ``canonical_model``; backend-owned wiring    must resolve it explicitly.)    """    resolved = get_model(model)    if isinstance(resolved, Gemini):        return resolved    # No proxy: build a plain Gemini against the default endpoint.    return Gemini(model=model)def build_simple_chat_agent(    *,    name: str,    instruction: str,    model: str = DEFAULT_MODEL,) -> LlmAgent:    return LlmAgent(        name=name,        model=get_model(model),        instruction=instruction,        tools=[AGUIToolset()],        after_model_callback=stop_on_terminal_text,    )def build_thinking_chat_agent(    *,    name: str,    instruction: str,    model: str = DEFAULT_MODEL,) -> LlmAgent:    """LlmAgent with Gemini thinking enabled.    `include_thoughts=True` makes Gemini emit `thought=True` parts alongside    final answer parts; ADK forwards these through ag-ui as reasoning chunks    so v2's CopilotChatReasoningMessage / useRenderReasoning can show them.    `thinking_budget=-1` lets the model decide how much to think.    """    return LlmAgent(        name=name,        model=get_model(model),        instruction=instruction,        tools=[AGUIToolset()],        generate_content_config=types.GenerateContentConfig(            thinking_config=types.ThinkingConfig(                include_thoughts=True,                thinking_budget=-1,            ),        ),        after_model_callback=stop_on_terminal_text,    )

## What is this?#

A headless UI gives you **full control** over the chat experience. You bring your own components, layout, and styling while CopilotKit handles agent communication, message management, tool-call rendering, and streaming. No `<CopilotChat>`, no slot overrides, just your components composed on top of the low-level hooks.

## When should I use this?#

Use headless UI when:

  * The [slot system](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/slots) isn't enough: you need a completely different layout.
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
    
    
      const { agent } = useAgent({ agentId: "headless-simple" });  const { copilotkit } = useCopilotKit();  const [input, setInput] = useState("");  const send = (text: string) => {    const trimmed = text.trim();    if (!trimmed || agent.isRunning) return;    agent.addMessage({      id: crypto.randomUUID(),      role: "user",      content: trimmed,    });    setInput("");    void copilotkit.runAgent({ agent }).catch((err) => {      // The Headless Simple demo is the canonical "two hooks, your      // design system" example users copy-paste as a starting point.      // Silently swallowing errors here would model broken practice;      // log so a network failure / runtime error / transport disconnect      // surfaces in the console for the developer.      console.error("[google-adk:headless-simple] runAgent failed", err);    });  };

The message list is a plain `.map()` over `agent.messages`: user messages render as right-aligned bubbles, assistant messages render streamed text plus inline tool calls via `renderToolCall({ toolCall })`:

chat.tsx
    
    
                    {visible.map((m) =>                  m.role === "user" ? (                    <UserBubble key={m.id} content={m.content} />                  ) : (                    <AssistantBubble key={m.id} content={m.content} />                  ),                )}

No `<CopilotChat />`, no slots. The trade-off: you only get text and tool calls. Reasoning messages, activity messages, and custom before/after slots won't show up unless you wire them in yourself, which is exactly what the complete example covers.

## Complete example#

The `headless-complete` cell rebuilds the **full** generative-UI composition from the low-level hooks directly, without importing `<CopilotChatMessageView>`: text, tool calls, reasoning cards, A2UI + MCP Apps activity messages, and custom before/after message slots.

### The `useRenderedMessages` hook#

The cell's central piece is a hand-rolled `useRenderedMessages(messages, isRunning)` that returns the same flat list of messages, each augmented with a `renderedContent: ReactNode` field. This hook is a **manual recreation of what`<CopilotChatMessageView>` does**:

message-list.tsx
    
    
      const renderToolCall = useRenderToolCall();  const { renderActivityMessage } = useRenderActivityMessage();  // Index tool results by their originating tool-call id so each tool-call  // card can hand the matching ToolMessage to `useRenderToolCall`.  // Without this the renderer can't see a result and the card stays in the  // "in-progress" state forever.  const toolMessagesByCallId = useMemo(() => {    const map = new Map<string, ToolMessage>();    for (const m of messages) {      if (m.role === "tool" && "toolCallId" in m && m.toolCallId) {        map.set(m.toolCallId, m as ToolMessage);      }    }    return map;  }, [messages]);

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

  * [Slots](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/slots) — less work than going fully headless, often enough.
  * [CSS customization](https://docs.copilotkit.ai/google-adk/custom-look-and-feel/css) — when you just need to re-skin the defaults.



### On this page

What is this?When should I use this?The core hooksMinimal exampleComplete exampleThe useRenderedMessages hookPer-role dispatchTool-call compositionBubble chromeNext steps
