---
url: https://docs.copilotkit.ai/llamaindex/custom-look-and-feel/reasoning-messages/
title: Reasoning Messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:14:38.301805+00:00
---

# Reasoning Messages

> Source: https://docs.copilotkit.ai/llamaindex/custom-look-and-feel/reasoning-messages/

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

On this page

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)Custom Look and Feel

# Reasoning Messages

Customize how reasoning (thinking) tokens from models like o1, o3, and o4-mini are displayed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

reasoning_agent.py

page.tsx

route.ts
    
    
    """Reasoning agent for LlamaIndex.Shared by `reasoning-custom` (custom amber ReasoningBlock slot) and`reasoning-default` (CopilotKit's built-in reasoning slot). The systemprompt asks the model to think step-by-step before answering, so the LLMproduces a reasoning channel that the chat UI can render.Why a reasoning model + the OpenAI Responses API------------------------------------------------Mirrors the langgraph-python parity gold standard(`init_chat_model("openai:<reasoning-model>", use_responses_api=True,reasoning={"effort": "medium", "summary": "detailed"})`). The OpenAIResponses API streams `response.reasoning_summary_text.delta` items only fornative reasoning models (gpt-5, o3, o4-mini, …); a non-reasoning model likegpt-4.1 on the chat-completions wire emits NO reasoning channel against realOpenAI, so the reasoning slot would only ever light up under aimock. Routingthrough `OpenAIResponses` with a reasoning model makes the chain of thoughtstream against a REAL provider; aimock renders the fixture's abstract`reasoning` field into the same Responses-API shape for deterministic tests.(LlamaIndex pins the default to `gpt-5` rather than langgraph's `gpt-5.4`because LlamaIndex 0.5.6 rejects model names absent from its context-sizetable at workflow construction — see REASONING_MODEL below.)Uses `get_reasoning_ag_ui_workflow_router` (a thin in-package extension of thestock `get_ag_ui_workflow_router`) so the model's reasoning summary deltassurface as AG-UI `REASONING_MESSAGE_*` events. The stock router reads onlyassistant text and silently drops the reasoning channel; see`_reasoning_router.py` for the three framework gaps it closes (and for how`_extract_reasoning_delta` reads the Responses-API summary delta off`resp.raw`, which LlamaIndex's own stream processing does not surface). Thefrontend `CopilotChatReasoningMessage` slot then composes with the flow."""from __future__ import annotationsimport osfrom llama_index.llms.openai import OpenAIResponsesfrom agents._reasoning_router import get_reasoning_ag_ui_workflow_routerSYSTEM_PROMPT = (    "You are a helpful assistant. For each user question, first think "    "step-by-step about the approach, then give a concise answer. Keep "    "responses brief -- 1 to 3 sentences max.")# Reasoning-capable model routed through the OpenAI Responses API.## Default is `gpt-5` (a native reasoning model), NOT the langgraph gold# standard's `gpt-5.4`. LlamaIndex 0.5.6's `OpenAIResponses.metadata` resolves# the context window through `openai_modelname_to_contextsize()`, which raises# `ValueError: Unknown model` for names outside its hard-coded table —# `AGUIChatWorkflow.__init__` reads `llm.metadata.is_function_calling_model`,# so an unrecognized name (like `gpt-5.4`) crashes workflow construction at# startup. `gpt-5` is in both that table AND the O1_MODELS reasoning list, so# it streams reasoning natively against real OpenAI. Deployments can override# via OPENAI_REASONING_MODEL (with any name LlamaIndex 0.5.6 recognizes).REASONING_MODEL = os.environ.get("OPENAI_REASONING_MODEL", "gpt-5")# `summary: detailed` requests the streamed reasoning summary; `effort:# medium` mirrors the gold config. We pass these through BOTH# `reasoning_options` (idiomatic; honored for O1_MODELS like gpt-5) AND# `additional_kwargs` (unconditionally merged into the /v1/responses body by# `OpenAIResponses._get_model_kwargs`), so the `reasoning` param still reaches# the wire if a deployment overrides to a reasoning model outside the# O1_MODELS allowlist._REASONING_PARAMS = {"effort": "medium", "summary": "detailed"}_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]reasoning_router = get_reasoning_ag_ui_workflow_router(    llm=OpenAIResponses(        model=REASONING_MODEL,        reasoning_options=_REASONING_PARAMS,        additional_kwargs={"reasoning": _REASONING_PARAMS},        **_openai_kwargs,    ),    frontend_tools=[],    backend_tools=[],    system_prompt=SYSTEM_PROMPT,    initial_state={},)

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
    
    
    // Functional agent-registration key (matches the /api/copilotkit route's// specializedAgents map and the backend /reasoning router). The manifest// demo id is `reasoning-default`; the agent key stays// `reasoning-default-render` to mirror built-in-agent / claude-sdk-python.const AGENT_ID = "reasoning-default-render";export default function ReasoningDefaultDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningDefaultSuggestions();  return <CopilotChat agentId={AGENT_ID} className="h-full rounded-2xl" />;}

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

reasoning_agent.py

page.tsx

reasoning-block.tsx

route.ts
    
    
    """Reasoning agent for LlamaIndex.Shared by `reasoning-custom` (custom amber ReasoningBlock slot) and`reasoning-default` (CopilotKit's built-in reasoning slot). The systemprompt asks the model to think step-by-step before answering, so the LLMproduces a reasoning channel that the chat UI can render.Why a reasoning model + the OpenAI Responses API------------------------------------------------Mirrors the langgraph-python parity gold standard(`init_chat_model("openai:<reasoning-model>", use_responses_api=True,reasoning={"effort": "medium", "summary": "detailed"})`). The OpenAIResponses API streams `response.reasoning_summary_text.delta` items only fornative reasoning models (gpt-5, o3, o4-mini, …); a non-reasoning model likegpt-4.1 on the chat-completions wire emits NO reasoning channel against realOpenAI, so the reasoning slot would only ever light up under aimock. Routingthrough `OpenAIResponses` with a reasoning model makes the chain of thoughtstream against a REAL provider; aimock renders the fixture's abstract`reasoning` field into the same Responses-API shape for deterministic tests.(LlamaIndex pins the default to `gpt-5` rather than langgraph's `gpt-5.4`because LlamaIndex 0.5.6 rejects model names absent from its context-sizetable at workflow construction — see REASONING_MODEL below.)Uses `get_reasoning_ag_ui_workflow_router` (a thin in-package extension of thestock `get_ag_ui_workflow_router`) so the model's reasoning summary deltassurface as AG-UI `REASONING_MESSAGE_*` events. The stock router reads onlyassistant text and silently drops the reasoning channel; see`_reasoning_router.py` for the three framework gaps it closes (and for how`_extract_reasoning_delta` reads the Responses-API summary delta off`resp.raw`, which LlamaIndex's own stream processing does not surface). Thefrontend `CopilotChatReasoningMessage` slot then composes with the flow."""from __future__ import annotationsimport osfrom llama_index.llms.openai import OpenAIResponsesfrom agents._reasoning_router import get_reasoning_ag_ui_workflow_routerSYSTEM_PROMPT = (    "You are a helpful assistant. For each user question, first think "    "step-by-step about the approach, then give a concise answer. Keep "    "responses brief -- 1 to 3 sentences max.")# Reasoning-capable model routed through the OpenAI Responses API.## Default is `gpt-5` (a native reasoning model), NOT the langgraph gold# standard's `gpt-5.4`. LlamaIndex 0.5.6's `OpenAIResponses.metadata` resolves# the context window through `openai_modelname_to_contextsize()`, which raises# `ValueError: Unknown model` for names outside its hard-coded table —# `AGUIChatWorkflow.__init__` reads `llm.metadata.is_function_calling_model`,# so an unrecognized name (like `gpt-5.4`) crashes workflow construction at# startup. `gpt-5` is in both that table AND the O1_MODELS reasoning list, so# it streams reasoning natively against real OpenAI. Deployments can override# via OPENAI_REASONING_MODEL (with any name LlamaIndex 0.5.6 recognizes).REASONING_MODEL = os.environ.get("OPENAI_REASONING_MODEL", "gpt-5")# `summary: detailed` requests the streamed reasoning summary; `effort:# medium` mirrors the gold config. We pass these through BOTH# `reasoning_options` (idiomatic; honored for O1_MODELS like gpt-5) AND# `additional_kwargs` (unconditionally merged into the /v1/responses body by# `OpenAIResponses._get_model_kwargs`), so the `reasoning` param still reaches# the wire if a deployment overrides to a reasoning model outside the# O1_MODELS allowlist._REASONING_PARAMS = {"effort": "medium", "summary": "detailed"}_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]reasoning_router = get_reasoning_ag_ui_workflow_router(    llm=OpenAIResponses(        model=REASONING_MODEL,        reasoning_options=_REASONING_PARAMS,        additional_kwargs={"reasoning": _REASONING_PARAMS},        **_openai_kwargs,    ),    frontend_tools=[],    backend_tools=[],    system_prompt=SYSTEM_PROMPT,    initial_state={},)

The `ReasoningBlock` used above renders the reasoning as an amber-tagged inline banner, intentionally louder than the default card so the thinking chain is the focal UI of the demo. Swap in your own component to match your product's tone:

page.tsx
    
    
    // Functional agent-registration key (matches the /api/copilotkit route's// specializedAgents map and the backend /reasoning router). The manifest// demo id is `reasoning-custom`; the agent key stays `agentic-chat-reasoning`// to mirror built-in-agent / claude-sdk-python.const AGENT_ID = "agentic-chat-reasoning";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}

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
