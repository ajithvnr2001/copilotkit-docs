---
url: https://docs.copilotkit.ai/google-adk/agentic-chat-ui/
title: Chat Components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:15.922692+00:00
---

# Chat Components

> Source: https://docs.copilotkit.ai/google-adk/agentic-chat-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

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

[Google ADK](https://docs.copilotkit.ai/google-adk)

# Chat Components

Customizable, drop-in components for building AI-powered chat interfaces

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

shared_chat.py

page.tsx

route.ts
    
    
    """Shared LlmAgent factories used across multiple demos.`build_simple_chat_agent` produces a plain Gemini chat agent with no backendtools — appropriate for any demo whose only customisation is on the frontend(prebuilt-sidebar, prebuilt-popup, chat-slots, chat-customization-css,headless-simple, headless-complete, voice, frontend-tools, agentic-chat).`build_thinking_chat_agent` uses Gemini 3.1 Flash-Lite with the thinking_configexposed so reasoning is streamed back as `thought` parts; the v2 React corerenders these via CopilotChatReasoningMessage.`get_model` returns a `Gemini` instance configured with the aimock proxyendpoint when `GOOGLE_GEMINI_BASE_URL` is set, or the default model stringotherwise. All agent modules should call `get_model()` instead ofhard-coding `"gemini-3.1-flash-lite"` so Railway deployments route throughaimock.`stop_on_terminal_text` is the canonical after_model_callback shared by everyregistered LlmAgent. Gemini 3.1 Flash-Lite does not naturally end its agenticloop after a successful tool call — it keeps re-issuing the same tool. Thecallback inspects each non-partial model response and, when it containstext with no pending function_call, sets `_invocation_context.end_invocation= True` so ADK terminates the loop. Without this guard every backend orfrontend tool in this package fires infinitely."""from __future__ import annotationsimport loggingimport osfrom typing import Optional, Unionfrom google.adk.agents import LlmAgentfrom google.adk.agents.callback_context import CallbackContextfrom google.adk.models.google_llm import Geminifrom google.adk.models.llm_response import LlmResponsefrom google.genai import typesfrom ag_ui_adk import AGUIToolsetfrom agents._header_forwarding import install_httpx_hooklogger = logging.getLogger(__name__)DEFAULT_MODEL = "gemini-3.1-flash-lite"def stop_on_terminal_text(    callback_context: CallbackContext, llm_response: LlmResponse) -> Optional[LlmResponse]:    """Terminate the ADK agentic loop on a final text-only model turn.    Lifted from the (orphaned) `simple_after_model_modifier` in    `agents/main.py`, with the SalesPipelineAgent name-gate removed so it    applies to every registered agent. Guards:    1. Skip partial streaming events — never end on a mid-stream chunk       (belt-and-suspenders with `ADK_DISABLE_PROGRESSIVE_SSE_STREAMING=1`       in `entrypoint.sh`).    2. Only terminate when the final non-partial response contains TEXT       and NO pending function_call — mixed text+function_call responses       (a known Gemini Flash quirk) must NOT terminate.    3. `_invocation_context` is an ADK private attribute; if it disappears       in a future ADK release, log-and-degrade rather than crash the       callback (which would stall the request).    Without this guard, Gemini calls the same tool indefinitely after a    successful tool result because no native termination condition fires.    """    content = llm_response.content    if not content or not content.parts:        if llm_response.error_message:            logger.warning(                "stop_on_terminal_text: Gemini returned error_message for agent=%s: %s",                callback_context.agent_name,                llm_response.error_message,            )        return None    if getattr(llm_response, "partial", False):        return None    # Under thinking mode (`include_thoughts=True`), Gemini emits a turn    # as TWO separate non-partial chunks:    #   1. text-only chunk: thought + reply text, `finish_reason=None`    #   2. function_call-only chunk: `finish_reason=FUNCTION_CALL`    # The callback fires on both. Without the finish_reason guard below,    # chunk 1's text-without-function-call shape causes premature    # termination — the function call in chunk 2 still streams but the    # agentic loop is already marked `end_invocation=True`, so the    # post-tool-result re-invocation that would chain to the next tool    # never happens (tool-rendering-reasoning-chain AAPL→MSFT regression).    # Only terminate when Gemini signals the turn is genuinely done with    # `finish_reason=STOP` (no further chunks coming). FUNCTION_CALL and    # None mean "more chunks are inbound" — defer.    finish_reason = getattr(llm_response, "finish_reason", None)    finish_reason_name = (        getattr(finish_reason, "name", None) if finish_reason is not None else None    )    if finish_reason_name != "STOP" and finish_reason != "STOP":        return None    has_text = any(getattr(part, "text", None) for part in content.parts)    has_function_call = any(        getattr(part, "function_call", None) for part in content.parts    )    if content.role != "model" or not has_text or has_function_call:        return None    invocation_context = getattr(callback_context, "_invocation_context", None)    if invocation_context is None:        logger.debug(            "stop_on_terminal_text: callback_context has no "            "_invocation_context attribute; skipping end_invocation."        )        return None    try:        invocation_context.end_invocation = True    except AttributeError:        logger.debug(            "stop_on_terminal_text: _invocation_context lacks "            "end_invocation; ADK private-API shape may have drifted."        )    return Nonedef get_model(model: str = DEFAULT_MODEL) -> Union[str, Gemini]:    """Return a model suitable for LlmAgent's `model=` parameter.    When `GOOGLE_GEMINI_BASE_URL` is set (Railway aimock proxy), returns a    `Gemini` instance with its `base_url` pointed at the proxy. Otherwise    returns the plain model string so the ADK resolves the default endpoint.    """    base_url = os.environ.get("GOOGLE_GEMINI_BASE_URL")    if base_url:        gemini = Gemini(model=model, base_url=base_url)        # Walk Gemini's ``._client`` chain and attach the request hook so        # inbound x-* headers (e.g. ``x-aimock-context``) ride along on        # outbound calls to the aimock proxy.        install_httpx_hook(gemini)        return gemini    return modeldef get_a2ui_model(model: str = DEFAULT_MODEL) -> Gemini:    """Return a concrete ``Gemini`` BaseLlm for the A2UI sub-agent.    The middleware's ``get_a2ui_tool({"model": ...})`` invokes the model    directly (forced ``render_a2ui`` call), so it needs a model *object*, not    the bare string ``get_model`` may return for ``LlmAgent.model=``. This    mirrors ``get_model``'s aimock-proxy wiring (base_url + x-header hook) so    the sub-agent's Gemini calls route through the same proxy as the primary    agent and match the same aimock fixtures. (The auto-inject path got this    object for free from the agent's ``canonical_model``; backend-owned wiring    must resolve it explicitly.)    """    resolved = get_model(model)    if isinstance(resolved, Gemini):        return resolved    # No proxy: build a plain Gemini against the default endpoint.    return Gemini(model=model)def build_simple_chat_agent(    *,    name: str,    instruction: str,    model: str = DEFAULT_MODEL,) -> LlmAgent:    return LlmAgent(        name=name,        model=get_model(model),        instruction=instruction,        tools=[AGUIToolset()],        after_model_callback=stop_on_terminal_text,    )def build_thinking_chat_agent(    *,    name: str,    instruction: str,    model: str = DEFAULT_MODEL,) -> LlmAgent:    """LlmAgent with Gemini thinking enabled.    `include_thoughts=True` makes Gemini emit `thought=True` parts alongside    final answer parts; ADK forwards these through ag-ui as reasoning chunks    so v2's CopilotChatReasoningMessage / useRenderReasoning can show them.    `thinking_budget=-1` lets the model decide how much to think.    """    return LlmAgent(        name=name,        model=get_model(model),        instruction=instruction,        tools=[AGUIToolset()],        generate_content_config=types.GenerateContentConfig(            thinking_config=types.ThinkingConfig(                include_thoughts=True,                thinking_budget=-1,            ),        ),        after_model_callback=stop_on_terminal_text,    )

## Pre-built components for agentic chat#

CopilotKit's chat components give you a fully functional, customizable AI chat interface out of the box. They handle streaming, generative UI, and deep customization so you can focus on your agent's behavior, not UI plumbing.

## What it looks like in code#

The live `agentic-chat` cell above is built from a single, small page. Wrap your UI in `<CopilotKit>` once (it wires the runtime, session, and agent registry) and drop `<CopilotChat>` wherever the chat should go:

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">      <Chat />    </CopilotKit>

Inside the chat, the `useConfigureSuggestions` hook lets you show contextual starter prompts. The example below uses it to seed a simple "Write a sonnet" suggestion:

suggestions.ts
    
    
    export function useAgenticChatSuggestions() {  useConfigureSuggestions({    suggestions: [      { title: "Write a sonnet", message: "Write a short sonnet about AI." },      {        title: "Tell me a joke",        message: "Tell me a one-line joke.",      },      {        title: "Is 17 prime?",        message: "Walk me through whether 17 is prime.",      },    ],    available: "always",  });}
