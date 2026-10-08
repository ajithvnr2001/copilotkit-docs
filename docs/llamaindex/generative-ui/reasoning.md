---
url: https://docs.copilotkit.ai/llamaindex/generative-ui/reasoning/
title: Reasoning
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:14:52.437258+00:00
---

# Reasoning

> Source: https://docs.copilotkit.ai/llamaindex/generative-ui/reasoning/

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

# Reasoning

Surface the agent's thinking chain in the chat — default or fully custom.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

reasoning_agent.py

page.tsx

reasoning-block.tsx

route.ts
    
    
    """Reasoning agent for LlamaIndex.Shared by `reasoning-custom` (custom amber ReasoningBlock slot) and`reasoning-default` (CopilotKit's built-in reasoning slot). The systemprompt asks the model to think step-by-step before answering, so the LLMproduces a reasoning channel that the chat UI can render.Why a reasoning model + the OpenAI Responses API------------------------------------------------Mirrors the langgraph-python parity gold standard(`init_chat_model("openai:<reasoning-model>", use_responses_api=True,reasoning={"effort": "medium", "summary": "detailed"})`). The OpenAIResponses API streams `response.reasoning_summary_text.delta` items only fornative reasoning models (gpt-5, o3, o4-mini, …); a non-reasoning model likegpt-4.1 on the chat-completions wire emits NO reasoning channel against realOpenAI, so the reasoning slot would only ever light up under aimock. Routingthrough `OpenAIResponses` with a reasoning model makes the chain of thoughtstream against a REAL provider; aimock renders the fixture's abstract`reasoning` field into the same Responses-API shape for deterministic tests.(LlamaIndex pins the default to `gpt-5` rather than langgraph's `gpt-5.4`because LlamaIndex 0.5.6 rejects model names absent from its context-sizetable at workflow construction — see REASONING_MODEL below.)Uses `get_reasoning_ag_ui_workflow_router` (a thin in-package extension of thestock `get_ag_ui_workflow_router`) so the model's reasoning summary deltassurface as AG-UI `REASONING_MESSAGE_*` events. The stock router reads onlyassistant text and silently drops the reasoning channel; see`_reasoning_router.py` for the three framework gaps it closes (and for how`_extract_reasoning_delta` reads the Responses-API summary delta off`resp.raw`, which LlamaIndex's own stream processing does not surface). Thefrontend `CopilotChatReasoningMessage` slot then composes with the flow."""from __future__ import annotationsimport osfrom llama_index.llms.openai import OpenAIResponsesfrom agents._reasoning_router import get_reasoning_ag_ui_workflow_routerSYSTEM_PROMPT = (    "You are a helpful assistant. For each user question, first think "    "step-by-step about the approach, then give a concise answer. Keep "    "responses brief -- 1 to 3 sentences max.")# Reasoning-capable model routed through the OpenAI Responses API.## Default is `gpt-5` (a native reasoning model), NOT the langgraph gold# standard's `gpt-5.4`. LlamaIndex 0.5.6's `OpenAIResponses.metadata` resolves# the context window through `openai_modelname_to_contextsize()`, which raises# `ValueError: Unknown model` for names outside its hard-coded table —# `AGUIChatWorkflow.__init__` reads `llm.metadata.is_function_calling_model`,# so an unrecognized name (like `gpt-5.4`) crashes workflow construction at# startup. `gpt-5` is in both that table AND the O1_MODELS reasoning list, so# it streams reasoning natively against real OpenAI. Deployments can override# via OPENAI_REASONING_MODEL (with any name LlamaIndex 0.5.6 recognizes).REASONING_MODEL = os.environ.get("OPENAI_REASONING_MODEL", "gpt-5")# `summary: detailed` requests the streamed reasoning summary; `effort:# medium` mirrors the gold config. We pass these through BOTH# `reasoning_options` (idiomatic; honored for O1_MODELS like gpt-5) AND# `additional_kwargs` (unconditionally merged into the /v1/responses body by# `OpenAIResponses._get_model_kwargs`), so the `reasoning` param still reaches# the wire if a deployment overrides to a reasoning model outside the# O1_MODELS allowlist._REASONING_PARAMS = {"effort": "medium", "summary": "detailed"}_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]reasoning_router = get_reasoning_ag_ui_workflow_router(    llm=OpenAIResponses(        model=REASONING_MODEL,        reasoning_options=_REASONING_PARAMS,        additional_kwargs={"reasoning": _REASONING_PARAMS},        **_openai_kwargs,    ),    frontend_tools=[],    backend_tools=[],    system_prompt=SYSTEM_PROMPT,    initial_state={},)

## What is this?#

Some models (OpenAI's `o1`, `o3`, and `o4-mini`, Anthropic's thinking variants) emit **reasoning tokens** , internal chain-of-thought traces that explain how the model is working toward its answer. CopilotKit surfaces these as first-class messages: when a `REASONING_MESSAGE_*` event arrives from the agent, the chat renders it inline so the user can follow the agent's thinking.

Reasoning isn't a custom-renderer plumb-in; it's a dedicated message type on the chat view. You can either accept the built-in rendering or override the `reasoningMessage` slot with your own component.

## When should I use this?#

Expose reasoning in the UI when you want to:

  * Give users real-time insight into the agent's thought process
  * Show progress on long or multi-step problems
  * Debug prompt behavior during development
  * Brand the reasoning card to match the rest of your product



## Default reasoning rendering (zero-config)#

Out of the box, reasoning events render inside CopilotKit's built-in `CopilotChatReasoningMessage` card:

  * A **"Thinking…"** label with a pulsing indicator while the model reasons.
  * Auto-expanded content so users can follow the chain of thought live.
  * Collapses to **"Thought for X seconds"** once reasoning finishes, with a chevron to re-expand.
  * Reasoning text rendered as Markdown.



No configuration is needed; if your model emits reasoning tokens, the card appears automatically:

page.tsx
    
    
    // Functional agent-registration key (matches the /api/copilotkit route's// specializedAgents map and the backend /reasoning router). The manifest// demo id is `reasoning-default`; the agent key stays// `reasoning-default-render` to mirror built-in-agent / claude-sdk-python.const AGENT_ID = "reasoning-default-render";export default function ReasoningDefaultDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningDefaultSuggestions();  return <CopilotChat agentId={AGENT_ID} className="h-full rounded-2xl" />;}

Here's what the built-in card looks like while the model thinks through a multi-step problem:

DemoCode

reasoning_agent.py

page.tsx

route.ts
    
    
    """Reasoning agent for LlamaIndex.Shared by `reasoning-custom` (custom amber ReasoningBlock slot) and`reasoning-default` (CopilotKit's built-in reasoning slot). The systemprompt asks the model to think step-by-step before answering, so the LLMproduces a reasoning channel that the chat UI can render.Why a reasoning model + the OpenAI Responses API------------------------------------------------Mirrors the langgraph-python parity gold standard(`init_chat_model("openai:<reasoning-model>", use_responses_api=True,reasoning={"effort": "medium", "summary": "detailed"})`). The OpenAIResponses API streams `response.reasoning_summary_text.delta` items only fornative reasoning models (gpt-5, o3, o4-mini, …); a non-reasoning model likegpt-4.1 on the chat-completions wire emits NO reasoning channel against realOpenAI, so the reasoning slot would only ever light up under aimock. Routingthrough `OpenAIResponses` with a reasoning model makes the chain of thoughtstream against a REAL provider; aimock renders the fixture's abstract`reasoning` field into the same Responses-API shape for deterministic tests.(LlamaIndex pins the default to `gpt-5` rather than langgraph's `gpt-5.4`because LlamaIndex 0.5.6 rejects model names absent from its context-sizetable at workflow construction — see REASONING_MODEL below.)Uses `get_reasoning_ag_ui_workflow_router` (a thin in-package extension of thestock `get_ag_ui_workflow_router`) so the model's reasoning summary deltassurface as AG-UI `REASONING_MESSAGE_*` events. The stock router reads onlyassistant text and silently drops the reasoning channel; see`_reasoning_router.py` for the three framework gaps it closes (and for how`_extract_reasoning_delta` reads the Responses-API summary delta off`resp.raw`, which LlamaIndex's own stream processing does not surface). Thefrontend `CopilotChatReasoningMessage` slot then composes with the flow."""from __future__ import annotationsimport osfrom llama_index.llms.openai import OpenAIResponsesfrom agents._reasoning_router import get_reasoning_ag_ui_workflow_routerSYSTEM_PROMPT = (    "You are a helpful assistant. For each user question, first think "    "step-by-step about the approach, then give a concise answer. Keep "    "responses brief -- 1 to 3 sentences max.")# Reasoning-capable model routed through the OpenAI Responses API.## Default is `gpt-5` (a native reasoning model), NOT the langgraph gold# standard's `gpt-5.4`. LlamaIndex 0.5.6's `OpenAIResponses.metadata` resolves# the context window through `openai_modelname_to_contextsize()`, which raises# `ValueError: Unknown model` for names outside its hard-coded table —# `AGUIChatWorkflow.__init__` reads `llm.metadata.is_function_calling_model`,# so an unrecognized name (like `gpt-5.4`) crashes workflow construction at# startup. `gpt-5` is in both that table AND the O1_MODELS reasoning list, so# it streams reasoning natively against real OpenAI. Deployments can override# via OPENAI_REASONING_MODEL (with any name LlamaIndex 0.5.6 recognizes).REASONING_MODEL = os.environ.get("OPENAI_REASONING_MODEL", "gpt-5")# `summary: detailed` requests the streamed reasoning summary; `effort:# medium` mirrors the gold config. We pass these through BOTH# `reasoning_options` (idiomatic; honored for O1_MODELS like gpt-5) AND# `additional_kwargs` (unconditionally merged into the /v1/responses body by# `OpenAIResponses._get_model_kwargs`), so the `reasoning` param still reaches# the wire if a deployment overrides to a reasoning model outside the# O1_MODELS allowlist._REASONING_PARAMS = {"effort": "medium", "summary": "detailed"}_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]reasoning_router = get_reasoning_ag_ui_workflow_router(    llm=OpenAIResponses(        model=REASONING_MODEL,        reasoning_options=_REASONING_PARAMS,        additional_kwargs={"reasoning": _REASONING_PARAMS},        **_openai_kwargs,    ),    frontend_tools=[],    backend_tools=[],    system_prompt=SYSTEM_PROMPT,    initial_state={},)

## Custom reasoning rendering#

For full control over the reasoning card, pass a component to the `reasoningMessage` slot on `messageView`. Your component receives the `ReasoningMessage` object (`.content` holds the streaming text), the full `messages` list, and `isRunning`, enough to decide whether this block is still streaming and whether it's the active trailing message:

page.tsxreasoning-block.tsx
    
    
    // Functional agent-registration key (matches the /api/copilotkit route's// specializedAgents map and the backend /reasoning router). The manifest// demo id is `reasoning-custom`; the agent key stays `agentic-chat-reasoning`// to mirror built-in-agent / claude-sdk-python.const AGENT_ID = "agentic-chat-reasoning";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}
    
    
    "use client";// Custom `reasoningMessage` slot renderer.//// Receives the `ReasoningMessage` plus (optionally) the full message list and// the running state from the slot system. Renders the content inline with a// visibly tagged amber banner so the user can always see the agent's thinking// chain — this is the focal UI of the demo.import React from "react";import type { ReasoningMessage, Message } from "@ag-ui/core";export function ReasoningBlock({  message,  messages,  isRunning,}: {  message: ReasoningMessage;  messages?: Message[];  isRunning?: boolean;}) {  const isLatest = messages?.[messages.length - 1]?.id === message.id;  const isStreaming = !!(isRunning && isLatest);  const hasContent = !!(message.content && message.content.length > 0);  return (    <div      data-testid="reasoning-block"      className="my-2 rounded-xl border border-[#DBDBE5] bg-[#BEC2FF1A] px-3.5 py-2.5 text-sm"    >      <div className="flex items-center gap-2 font-medium text-[#010507]">        <span className="inline-block rounded-full border border-[#BEC2FF] bg-white px-2 py-0.5 text-[10px] uppercase tracking-[0.14em] text-[#57575B]">          Reasoning        </span>        <span className="text-[#57575B]">          {isStreaming ? "Thinking…" : hasContent ? "Agent reasoning" : "…"}        </span>      </div>      {hasContent && (        <div className="mt-1.5 whitespace-pre-wrap italic text-[#57575B]">          {message.content}        </div>      )}    </div>  );}

The `ReasoningBlock` (imported above) renders the reasoning as an amber-tagged inline banner, intentionally louder than the default card so the thinking chain is the focal UI of the demo. Swap in your own component to match your product's tone.

The `messageView.reasoningMessage` slot accepts either a full component (as shown) or a sub-slot object like `{ header, contentView, toggle }` if you just want to tweak parts of the default card. See the reference docs for sub-slot props.
