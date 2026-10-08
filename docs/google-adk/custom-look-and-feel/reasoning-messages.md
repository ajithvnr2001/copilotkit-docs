---
url: https://docs.copilotkit.ai/google-adk/custom-look-and-feel/reasoning-messages/
title: Reasoning Messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:54.585593+00:00
---

# Reasoning Messages

> Source: https://docs.copilotkit.ai/google-adk/custom-look-and-feel/reasoning-messages/

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

Reasoning Messages

BasicsChatCustom Look and Feel

# Reasoning Messages

Customize how reasoning (thinking) tokens from models like o1, o3, and o4-mini are displayed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

shared_chat.py

page.tsx

route.ts
    
    
    """Shared LlmAgent factories used across multiple demos.`build_simple_chat_agent` produces a plain Gemini chat agent with no backendtools — appropriate for any demo whose only customisation is on the frontend(prebuilt-sidebar, prebuilt-popup, chat-slots, chat-customization-css,headless-simple, headless-complete, voice, frontend-tools, agentic-chat).`build_thinking_chat_agent` uses Gemini 3.1 Flash-Lite with the thinking_configexposed so reasoning is streamed back as `thought` parts; the v2 React corerenders these via CopilotChatReasoningMessage.`get_model` returns a `Gemini` instance configured with the aimock proxyendpoint when `GOOGLE_GEMINI_BASE_URL` is set, or the default model stringotherwise. All agent modules should call `get_model()` instead ofhard-coding `"gemini-3.1-flash-lite"` so Railway deployments route throughaimock.`stop_on_terminal_text` is the canonical after_model_callback shared by everyregistered LlmAgent. Gemini 3.1 Flash-Lite does not naturally end its agenticloop after a successful tool call — it keeps re-issuing the same tool. Thecallback inspects each non-partial model response and, when it containstext with no pending function_call, sets `_invocation_context.end_invocation= True` so ADK terminates the loop. Without this guard every backend orfrontend tool in this package fires infinitely."""from __future__ import annotationsimport loggingimport osfrom typing import Optional, Unionfrom google.adk.agents import LlmAgentfrom google.adk.agents.callback_context import CallbackContextfrom google.adk.models.google_llm import Geminifrom google.adk.models.llm_response import LlmResponsefrom google.genai import typesfrom ag_ui_adk import AGUIToolsetfrom agents._header_forwarding import install_httpx_hooklogger = logging.getLogger(__name__)DEFAULT_MODEL = "gemini-3.1-flash-lite"def stop_on_terminal_text(    callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:    """Terminate the ADK agentic loop on a final text-only model turn.    Lifted from the (orphaned) `simple_after_model_modifier` in    `agents/main.py`, with the SalesPipelineAgent name-gate removed so it    applies to every registered agent. Guards:    1. Skip partial streaming events — never end on a mid-stream chunk       (belt-and-suspenders with `ADK_DISABLE_PROGRESSIVE_SSE_STREAMING=1`       in `entrypoint.sh`).    2. Only terminate when the final non-partial response contains TEXT       and NO pending function_call — mixed text+function_call responses       (a known Gemini Flash quirk) must NOT terminate.    3. `_invocation_context` is an ADK private attribute; if it disappears       in a future ADK release, log-and-degrade rather than crash the       callback (which would stall the request).    Without this guard, Gemini calls the same tool indefinitely after a    successful tool result because no native termination condition fires.    """    content = llm_response.content    if not content or not content.parts:        if llm_response.error_message:            logger.warning(                "stop_on_terminal_text: Gemini returned error_message for agent=%s: %s",                callback_context.agent_name,                llm_response.error_message,            )        return None    if getattr(llm_response, "partial", False):        return None    # Under thinking mode (`include_thoughts=True`), Gemini emits a turn    # as TWO separate non-partial chunks:    #   1. text-only chunk: thought + reply text, `finish_reason=None`    #   2. function_call-only chunk: `finish_reason=FUNCTION_CALL`    # The callback fires on both. Without the finish_reason guard below,    # chunk 1's text-without-function-call shape causes premature    # termination — the function call in chunk 2 still streams but the    # agentic loop is already marked `end_invocation=True`, so the    # post-tool-result re-invocation that would chain to the next tool    # never happens (tool-rendering-reasoning-chain AAPL→MSFT regression).    # Only terminate when Gemini signals the turn is genuinely done with    # `finish_reason=STOP` (no further chunks coming). FUNCTION_CALL and    # None mean "more chunks are inbound" — defer.    finish_reason = getattr(llm_response, "finish_reason", None)    finish_reason_name = (        getattr(finish_reason, "name", None) if finish_reason is not None else None    )    if finish_reason_name != "STOP" and finish_reason != "STOP":        return None    has_text = any(getattr(part, "text", None) for part in content.parts)    has_function_call = any(        getattr(part, "function_call", None) for part in content.parts    )    if content.role != "model" or not has_text or has_function_call:        return None    invocation_context = getattr(callback_context, "_invocation_context", None)    if invocation_context is None:        logger.debug(            "stop_on_terminal_text: callback_context has no "            "_invocation_context attribute; skipping end_invocation."        )        return None    try:        invocation_context.end_invocation = True    except AttributeError:        logger.debug(            "stop_on_terminal_text: _invocation_context lacks "            "end_invocation; ADK private-API shape may have drifted."        )    return Nonedef get_model(model: str = DEFAULT_MODEL) -> Union[str, Gemini]:    """Return a model suitable for LlmAgent's `model=` parameter.    When `GOOGLE_GEMINI_BASE_URL` is set (Railway aimock proxy), returns a    `Gemini` instance with its `base_url` pointed at the proxy. Otherwise    returns the plain model string so the ADK resolves the default endpoint.    """    base_url = os.environ.get("GOOGLE_GEMINI_BASE_URL")    if base_url:        gemini = Gemini(model=model, base_url=base_url)        # Walk Gemini's ``._client`` chain and attach the request hook so        # inbound x-* headers (e.g. ``x-aimock-context``) ride along on        # outbound calls to the aimock proxy.        install_httpx_hook(gemini)        return gemini    return modeldef get_a2ui_model(model: str = DEFAULT_MODEL) -> Gemini:    """Return a concrete ``Gemini`` BaseLlm for the A2UI sub-agent.    The middleware's ``get_a2ui_tool({"model": ...})`` invokes the model    directly (forced ``render_a2ui`` call), so it needs a model *object*, not    the bare string ``get_model`` may return for ``LlmAgent.model=``. This    mirrors ``get_model``'s aimock-proxy wiring (base_url + x-header hook) so    the sub-agent's Gemini calls route through the same proxy as the primary    agent and match the same aimock fixtures. (The auto-inject path got this    object for free from the agent's ``canonical_model``; backend-owned wiring    must resolve it explicitly.)    """    resolved = get_model(model)    if isinstance(resolved, Gemini):        return resolved    # No proxy: build a plain Gemini against the default endpoint.    return Gemini(model=model)def build_simple_chat_agent(    *,    name: str,    instruction: str,    model: str = DEFAULT_MODEL,) -> LlmAgent:    return LlmAgent(        name=name,        model=get_model(model),        instruction=instruction,        tools=[AGUIToolset()],        after_model_callback=stop_on_terminal_text,    )def build_thinking_chat_agent(    *,    name: str,    instruction: str,    model: str = DEFAULT_MODEL,) -> LlmAgent:    """LlmAgent with Gemini thinking enabled.    `include_thoughts=True` makes Gemini emit `thought=True` parts alongside    final answer parts; ADK forwards these through ag-ui as reasoning chunks    so v2's CopilotChatReasoningMessage / useRenderReasoning can show them.    `thinking_budget=-1` lets the model decide how much to think.    """    return LlmAgent(        name=name,        model=get_model(model),        instruction=instruction,        tools=[AGUIToolset()],        generate_content_config=types.GenerateContentConfig(            thinking_config=types.ThinkingConfig(                include_thoughts=True,                thinking_budget=-1,            ),        ),        after_model_callback=stop_on_terminal_text,    )

Some models (like OpenAI's o1, o3, and o4-mini) emit **reasoning tokens** : internal "thinking" traces that show the model's chain-of-thought before it produces a final answer. CopilotKit surfaces these tokens automatically with a collapsible **Reasoning Message** card.

## Default Behavior#

When reasoning events arrive from the agent, CopilotKit renders them inside a built-in card that:

  * Shows a **"Thinking…"** label with a pulsating indicator while the model is reasoning.
  * Expands automatically so you can follow the model's thought process in real-time.
  * Collapses and switches to **"Thought for X seconds"** once reasoning finishes.
  * Renders the reasoning content as **Markdown**.
  * Includes a chevron toggle so users can re-expand and review the reasoning at any time.



No extra configuration is needed; if your model emits reasoning tokens, the card appears automatically.

The only requirement is connecting your agent to CopilotKit; no extra props or configuration needed:

page.tsx
    
    
    const AGENT_ID = "reasoning-default";export default function ReasoningDefaultDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningDefaultSuggestions();  return <CopilotChat agentId={AGENT_ID} className="h-full rounded-2xl" />;}

## Customizing the Reasoning Message#

The reasoning message is composed of three sub-components that can each be replaced independently via **slot props** :

Sub-component| Slot prop| Description  
---|---|---  
`Header`| `header`| The clickable bar with the brain icon, label, and chevron  
`Content`| `contentView`| The reasoning text area (Markdown)  
`Toggle`| `toggle`| The expand/collapse animation wrapper  
  
You pass custom sub-components through the `messageView` prop on `CopilotChat`, `CopilotPopup`, or `CopilotSidebar`:
    
    
    <CopilotChat
      messageView={{
        reasoningMessage: {
          header: CustomHeader,
          contentView: CustomContent,
        },
      }}
    />

### Custom Header#

Replace the header to change the icon, label text, or styling. The header receives these props:

Prop| Type| Description  
---|---|---  
`isOpen`| `boolean`| Whether the content panel is currently expanded  
`label`| `string`| `"Thinking…"` while streaming, `"Thought for X seconds"` after  
`hasContent`| `boolean`| Whether any reasoning text has been received  
`isStreaming`| `boolean`| Whether reasoning is actively streaming  
`onClick`| `() => void`| Toggle handler (only present when `hasContent` is `true`)  
      
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function CustomHeader({
      isOpen,
      label,
      hasContent,
      isStreaming,
      ...props
    }: React.ButtonHTMLAttributes<HTMLButtonElement> & {
      isOpen?: boolean;
      label?: string;
      hasContent?: boolean;
      isStreaming?: boolean;
    }) {
      return (
        <button
          className="flex w-full items-center gap-2 px-3 py-2 text-sm font-medium"
          {...props}
        >
          {isStreaming ? "🧠" : "💡"}
          <span>{label}</span>
          {hasContent && (
            <span className="ml-auto text-xs">{isOpen ? "Hide" : "Show"}</span>
          )}
        </button>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: { header: CustomHeader },
      }}
    />

### Custom Content#

Replace the content area to change how reasoning text is displayed:

Prop| Type| Description  
---|---|---  
`isStreaming`| `boolean`| Whether reasoning tokens are still arriving  
`hasContent`| `boolean`| Whether any reasoning text has been received  
`children`| `string`| The raw reasoning text  
      
    
    function CustomContent({
      isStreaming,
      hasContent,
      children,
      ...props
    }: React.HTMLAttributes<HTMLDivElement> & {
      isStreaming?: boolean;
      hasContent?: boolean;
    }) {
      if (!hasContent && !isStreaming) return null;
    
      return (
        <div className="px-4 pb-3 text-sm text-gray-500 font-mono" {...props}>
          {children}
          {isStreaming && <span className="animate-pulse ml-1">▊</span>}
        </div>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: { contentView: CustomContent },
      }}
    />

## Fully Custom Reasoning Message#

For complete control over the entire reasoning card, pass a **component** instead of slot props. Your component receives the same top-level props as the built-in one:

Prop| Type| Description  
---|---|---  
`message`| `ReasoningMessage`| The reasoning message object (`.content` holds the text)  
`messages`| `Message[]`| All messages in the conversation  
`isRunning`| `boolean`| Whether the agent is currently running  
  
DemoCode

page.tsx

reasoning-block.tsx

shared_chat.py

route.ts
    
    
    "use client";// Reasoning — Custom//// Pairs with `reasoning-default` so users can compare default vs custom// reasoning rendering side by side. Both demos share the same backend// (the `_thinking_chat` ADK agent built via `build_thinking_chat_agent`// — see `src/agents/registry.py:144-145` where both `reasoning-default`// and `reasoning-custom` resolve to `AgentSpec(_thinking_chat)`) and// the same runtime URL (/api/copilotkit). This cell overrides the// `reasoningMessage` slot on the `messageView` slot with// `ReasoningBlock` — a tagged amber banner that emphasizes the agent's// thinking chain.//// Reasoning is a first-class message type in v2: see// packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx,// which discriminates messages by `message.role === "reasoning"` and// renders them via the `reasoningMessage` slot (default component:// `CopilotChatReasoningMessage`). The slot override below is the public,// stable way to customize that output.import type { CopilotChatReasoningMessage } from "@copilotkit/react-core/v2";import { CopilotKit, CopilotChat } from "@copilotkit/react-core/v2";import { ReasoningBlock } from "./reasoning-block";import { useReasoningCustomSuggestions } from "./suggestions";const AGENT_ID = "reasoning-custom";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}

The `ReasoningBlock` used above renders the reasoning as an amber-tagged inline banner, intentionally louder than the default card so the thinking chain is the focal UI of the demo. Swap in your own component to match your product's tone:

page.tsx
    
    
    const AGENT_ID = "reasoning-custom";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}

## Render-Prop Children#

The built-in `CopilotChatReasoningMessage` also supports a **render-prop** pattern for cases where you want to rearrange the built-in sub-components without reimplementing them:
    
    
    import {
      CopilotChatReasoningMessage,
    } from "@copilotkit/react-core/v2";
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function MyReasoningLayout(props: React.ComponentProps<typeof CopilotChatReasoningMessage>) {
      return (
        <CopilotChatReasoningMessage {...props}>
          {({ header, toggle }) => (
            <div className="rounded-lg border bg-yellow-50 my-2">
              {header}
              {toggle}
            </div>
          )}
        </CopilotChatReasoningMessage>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: MyReasoningLayout,
      }}
    />

The render-prop callback receives:

Property| Description  
---|---  
`header`| Pre-rendered header element  
`contentView`| Pre-rendered content element  
`toggle`| Pre-rendered expand/collapse wrapper (contains `contentView`)  
`message`| The reasoning message object  
`messages`| All messages  
`isRunning`| Whether the agent is running  
  
### On this page

Default BehaviorCustomizing the Reasoning MessageCustom HeaderCustom ContentFully Custom Reasoning MessageRender-Prop Children
