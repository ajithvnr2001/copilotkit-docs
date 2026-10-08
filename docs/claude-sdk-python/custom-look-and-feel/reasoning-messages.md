---
url: https://docs.copilotkit.ai/claude-sdk-python/custom-look-and-feel/reasoning-messages/
title: Reasoning Messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:14.016343+00:00
---

# Reasoning Messages

> Source: https://docs.copilotkit.ai/claude-sdk-python/custom-look-and-feel/reasoning-messages/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/claude-sdk-python/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/claude-sdk-python/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/claude-sdk-python/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/claude-sdk-python/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/claude-sdk-python/custom-look-and-feel/reasoning-messages)

[Multimodal Attachments](https://docs.copilotkit.ai/claude-sdk-python/multimodal-attachments)[Voice](https://docs.copilotkit.ai/claude-sdk-python/voice)[Reasoning](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-python/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-python/community-frameworks)

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

reasoning_agent.py

page.tsx

route.ts
    
    
    """Reasoning agent — emits AG-UI REASONING_MESSAGE_* events.Shared by:  - reasoning-custom (custom amber ReasoningBlock slot on the frontend)  - reasoning-default (CopilotKit's built-in reasoning slot)Approach:The Anthropic Python SDK supports Claude's extended-thinking ("thinkingbudget") parameter on `messages.stream`, which streams `thinking_delta`content blocks separately from text. We map those onto AG-UI'sREASONING_MESSAGE_* events. Models without extended-thinking fall backto an inline ``<reasoning>...</reasoning>`` system-prompt convention thatthis agent parses out of the text stream."""from __future__ import annotationsimport osimport tracebackfrom collections.abc import AsyncIteratorfrom textwrap import dedentfrom typing import Anyimport anthropicfrom ag_ui.core import (    EventType,    RunAgentInput,    RunFinishedEvent,    RunStartedEvent,    TextMessageContentEvent,    TextMessageEndEvent,    TextMessageStartEvent,)from ag_ui.encoder import EventEncoderfrom agents.claude_agent_sdk_adapter import normalize_claude_model# System prompt for the native adaptive-thinking path (the default).# Extended thinking is always enabled below, so the model already emits its# step-by-step plan on the native `thinking` channel — which we forward as# REASONING_MESSAGE_*. We must NOT also instruct the model to wrap a plan in# `<reasoning>...</reasoning>` text tags: against real Claude that produces a# SECOND reasoning block (native thinking + tag-text), i.e. the double-bubble.# So the native prompt asks only for a clean final answer; the reasoning chain# comes entirely from the native channel.NATIVE_REASONING_SYSTEM_PROMPT = dedent("""    You are a helpful assistant. Think through each user question    step-by-step, then give a single concise final answer for the user.    Do not wrap your answer in any XML or markup tags.""").strip()# Fallback system prompt for a NO-native-thinking deployment. If extended# thinking is ever disabled, the inline `<reasoning>...</reasoning>` tag# convention (parsed by the dormant state machine below) is the only way to# surface a reasoning chain, so this prompt re-instates the tag instruction.REASONING_SYSTEM_PROMPT = dedent("""    You are a helpful assistant. For each user question, FIRST emit a    short step-by-step plan inside `<reasoning>...</reasoning>` tags    (one or two short sentences per step, plain text only — no    Markdown, no JSON), THEN follow with the final concise answer for    the user OUTSIDE the tags.    The reasoning block is shown to the user as a visible "thinking"    chain — keep it brief and readable.    Example:    <reasoning>    The user is asking about X. I should consider Y and Z.    Combining both gives W.    </reasoning>    Final answer: W.""").strip()async def run_reasoning_agent(    input_data: RunAgentInput,    *,    system_prompt: str | None = None,) -> AsyncIterator[str]:    """Stream a reasoning-enabled assistant response as AG-UI events.    Splits Claude's response into REASONING_MESSAGE_* (everything inside    `<reasoning>...</reasoning>` tags) and TEXT_MESSAGE_* (everything    outside). Tags themselves are stripped before forwarding.    """    encoder = EventEncoder()    client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))    messages: list[dict[str, Any]] = []    for msg in input_data.messages or []:        role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)        if role not in ("user", "assistant"):            continue        raw_content = getattr(msg, "content", None)        content = ""        if isinstance(raw_content, str):            content = raw_content        elif isinstance(raw_content, list):            parts: list[str] = []            for part in raw_content:                if hasattr(part, "text"):                    parts.append(part.text)                elif isinstance(part, dict) and "text" in part:                    parts.append(part["text"])            content = "".join(parts)        if content:            messages.append({"role": role, "content": content})    thread_id = input_data.thread_id or "default"    run_id = input_data.run_id or "run-1"    yield encoder.encode(        RunStartedEvent(type=EventType.RUN_STARTED, thread_id=thread_id, run_id=run_id)    )    # Native extended thinking is always enabled on the stream below, so the    # reasoning chain comes from the native `thinking` channel. Pick the system    # prompt to MATCH that: the native prompt does NOT instruct the model to    # emit `<reasoning>` tags (which would double up as a second reasoning    # block against real Claude). The tag-instructing prompt + the inline-tag    # parser stay as a dormant fallback for a no-native-thinking deployment.    # An explicit caller-supplied `system_prompt` always wins.    _native_thinking_enabled = True    default_system = (        NATIVE_REASONING_SYSTEM_PROMPT        if _native_thinking_enabled        else REASONING_SYSTEM_PROMPT    )    system = system_prompt or default_system    text_msg_id = f"msg-{run_id}-text"    reasoning_msg_id = f"msg-{run_id}-reasoning"    # State machine for parsing <reasoning>...</reasoning>    REASONING_OPEN = "<reasoning>"    REASONING_CLOSE = "</reasoning>"    in_reasoning = False    reasoning_started = False    # Idempotency guard for the inline-`<reasoning>`-tag REASONING_MESSAGE_END.    # Set once END is emitted for `reasoning_msg_id` so the in-stream close, the    # post-stream buffer flush, and the error/early-end cleanup never    # double-emit an END for the same inline reasoning block.    reasoning_ended = False    text_started = False    buffer = ""    # Native extended-thinking streaming state. When the model (or aimock    # replay) emits Anthropic `thinking`/`thinking_delta` blocks we forward    # them as REASONING_MESSAGE_* directly — independent of the inline    # `<reasoning>`-tag text parsing below, which stays as the no-thinking    # fallback. Mirrors claude-sdk-typescript's /reasoning handler.    #    # A single turn may contain MORE THAN ONE `thinking` content block. Each    # gets its OWN message id (incorporating `id(block)`) assigned on its    # content_block_start, and `native_reasoning_started` is reset to False at    # BOTH block start and block stop so every thinking block emits its own    # balanced START/CONTENT/END lifecycle rather than reopening an already    # ENDED message id. `native_reasoning_id is not None` is the "a native    # thinking block is currently open" sentinel. Mirrors the sibling    # tool_rendering_reasoning_chain_agent.py pattern.    native_reasoning_id: str | None = None    native_reasoning_started = False    # Import lazily so missing imports don't crash module import-time    # on older ag_ui versions.    from ag_ui.core import (        ReasoningMessageContentEvent,        ReasoningMessageEndEvent,        ReasoningMessageStartEvent,    )    # Adaptive thinking enabled so Claude streams native thinking blocks.    # Overridable via ANTHROPIC_REASONING_MODEL (falling back to    # ANTHROPIC_MODEL). Under aimock replay the thinking channel comes from    # the fixture's `reasoning` field regardless of the model name.    reasoning_model = os.getenv(        "ANTHROPIC_REASONING_MODEL",        os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8"),    )    reasoning_model = normalize_claude_model(reasoning_model)    try:        async with client.messages.stream(            model=reasoning_model,            max_tokens=3072,            system=system,            messages=messages,            thinking={"type": "adaptive"},        ) as stream:            async for event in stream:                etype = type(event).__name__                if etype == "RawContentBlockStartEvent":                    block = event.content_block  # type: ignore[attr-defined]                    if getattr(block, "type", None) == "thinking":                        # Fresh per-block id so two thinking blocks in one turn                        # each get their own balanced lifecycle. Reset                        # `started` so a new START is emitted for THIS block.                        native_reasoning_id = f"msg-{run_id}-think-{id(block)}"                        native_reasoning_started = False                    continue                if etype in (                    "RawContentBlockStopEvent",                    "ParsedContentBlockStopEvent",                ):                    if native_reasoning_id is not None:                        if native_reasoning_started:                            yield encoder.encode(                                ReasoningMessageEndEvent(                                    type=EventType.REASONING_MESSAGE_END,                                    message_id=native_reasoning_id,                                )                            )                        # Reset both so the next thinking block starts clean.                        native_reasoning_id = None                        native_reasoning_started = False                    continue                if etype != "RawContentBlockDeltaEvent":                    continue                delta = event.delta  # type: ignore[attr-defined]                if delta.type == "thinking_delta" and native_reasoning_id:                    thinking_text = getattr(delta, "thinking", "") or ""                    if thinking_text:                        if not native_reasoning_started:                            native_reasoning_started = True                            yield encoder.encode(                                ReasoningMessageStartEvent(                                    type=EventType.REASONING_MESSAGE_START,                                    message_id=native_reasoning_id,                                    role="reasoning",                                )                            )                        yield encoder.encode(                            ReasoningMessageContentEvent(                                type=EventType.REASONING_MESSAGE_CONTENT,                                message_id=native_reasoning_id,                                delta=thinking_text,                            )                        )                    continue                if delta.type != "text_delta":                    continue                buffer += delta.text                # Drain the buffer, emitting either reasoning or text                # whenever we have enough to safely classify.                while True:                    if in_reasoning:                        close_idx = buffer.find(REASONING_CLOSE)                        if close_idx == -1:                            # Hold last few chars in case the close tag is split.                            keep = max(0, len(buffer) - len(REASONING_CLOSE))                            chunk = buffer[:keep]                            buffer = buffer[keep:]                            if chunk:                                if not reasoning_started:                                    yield encoder.encode(                                        ReasoningMessageStartEvent(                                            type=EventType.REASONING_MESSAGE_START,                                            message_id=reasoning_msg_id,                                            role="reasoning",                                        )                                    )                                    reasoning_started = True                                yield encoder.encode(                                    ReasoningMessageContentEvent(                                        type=EventType.REASONING_MESSAGE_CONTENT,                                        message_id=reasoning_msg_id,                                        delta=chunk,                                    )                                )                            break                        # Found close tag — emit remaining reasoning, end it, switch mode.                        chunk = buffer[:close_idx]                        if chunk:                            if not reasoning_started:                                yield encoder.encode(                                    ReasoningMessageStartEvent(                                        type=EventType.REASONING_MESSAGE_START,                                        message_id=reasoning_msg_id,                                        role="reasoning",                                    )                                )                                reasoning_started = True                            yield encoder.encode(                                ReasoningMessageContentEvent(                                    type=EventType.REASONING_MESSAGE_CONTENT,                                    message_id=reasoning_msg_id,                                    delta=chunk,                                )                            )                        if reasoning_started and not reasoning_ended:                            yield encoder.encode(                                ReasoningMessageEndEvent(                                    type=EventType.REASONING_MESSAGE_END,                                    message_id=reasoning_msg_id,                                )                            )                            reasoning_ended = True                        buffer = buffer[close_idx + len(REASONING_CLOSE) :]                        in_reasoning = False                        continue                    else:                        open_idx = buffer.find(REASONING_OPEN)                        if open_idx == -1:                            # No open tag in buffer — emit as text but hold tail in case tag is split.                            keep = max(0, len(buffer) - len(REASONING_OPEN))                            chunk = buffer[:keep]                            buffer = buffer[keep:]                            if chunk:                                # Skip leading whitespace-only fragments before any reasoning                                # so the empty assistant message doesn't appear.                                if not text_started:                                    yield encoder.encode(                                        TextMessageStartEvent(                                            type=EventType.TEXT_MESSAGE_START,                                            message_id=text_msg_id,                                            role="assistant",                                        )                                    )                                    text_started = True                                yield encoder.encode(                                    TextMessageContentEvent(                                        type=EventType.TEXT_MESSAGE_CONTENT,                                        message_id=text_msg_id,                                        delta=chunk,                                    )                                )                            break                        # Found open tag — flush text up to it, switch to reasoning mode.                        chunk = buffer[:open_idx]                        if chunk:                            if not text_started:                                yield encoder.encode(                                    TextMessageStartEvent(                                        type=EventType.TEXT_MESSAGE_START,                                        message_id=text_msg_id,                                        role="assistant",                                    )                                )                                text_started = True                            yield encoder.encode(                                TextMessageContentEvent(                                    type=EventType.TEXT_MESSAGE_CONTENT,                                    message_id=text_msg_id,                                    delta=chunk,                                )                            )                        buffer = buffer[open_idx + len(REASONING_OPEN) :]                        in_reasoning = True                        continue        # Lifecycle guarantee: if a native thinking block streamed content        # but its content_block_stop never arrived (e.g. stream ended early),        # still close the reasoning message so the UI doesn't render an        # in-flight thinking bubble.        if native_reasoning_id is not None and native_reasoning_started:            yield encoder.encode(                ReasoningMessageEndEvent(                    type=EventType.REASONING_MESSAGE_END,                    message_id=native_reasoning_id,                )            )            native_reasoning_id = None            native_reasoning_started = False        # Flush any remaining buffered content as text.        if buffer:            if in_reasoning:                if not reasoning_started:                    yield encoder.encode(                        ReasoningMessageStartEvent(                            type=EventType.REASONING_MESSAGE_START,                            message_id=reasoning_msg_id,                            role="reasoning",                        )                    )                    reasoning_started = True                yield encoder.encode(                    ReasoningMessageContentEvent(                        type=EventType.REASONING_MESSAGE_CONTENT,                        message_id=reasoning_msg_id,                        delta=buffer,                    )                )                if not reasoning_ended:                    yield encoder.encode(                        ReasoningMessageEndEvent(                            type=EventType.REASONING_MESSAGE_END,                            message_id=reasoning_msg_id,                        )                    )                    reasoning_ended = True            else:                if not text_started:                    yield encoder.encode(                        TextMessageStartEvent(                            type=EventType.TEXT_MESSAGE_START,                            message_id=text_msg_id,                            role="assistant",                        )                    )                    text_started = True                yield encoder.encode(                    TextMessageContentEvent(                        type=EventType.TEXT_MESSAGE_CONTENT,                        message_id=text_msg_id,                        delta=buffer,                    )                )        # Lifecycle guarantee for the inline-`<reasoning>`-tag block: if the        # stream ended mid-inline-block (open `<reasoning>` with started content        # but no `</reasoning>`) and the buffer-flush above did not already emit        # the END (e.g. the buffer was empty because all content had already        # been streamed), close it now so the UI doesn't render a perpetual        # in-flight reasoning bubble. Mirrors the native-channel guard above.        if reasoning_started and not reasoning_ended:            yield encoder.encode(                ReasoningMessageEndEvent(                    type=EventType.REASONING_MESSAGE_END,                    message_id=reasoning_msg_id,                )            )            reasoning_ended = True    except Exception:        # Lifecycle guarantee on the error path: if the stream raised while a        # native thinking block was still open, close it before emitting the        # error text bubble so the UI doesn't render a perpetual in-flight        # thinking bubble. Mirrors the normal-completion guard above.        if native_reasoning_id is not None and native_reasoning_started:            yield encoder.encode(                ReasoningMessageEndEvent(                    type=EventType.REASONING_MESSAGE_END,                    message_id=native_reasoning_id,                )            )            native_reasoning_id = None            native_reasoning_started = False        # Same guarantee for the inline-`<reasoning>`-tag block: if the stream        # raised while inside an open inline reasoning block whose END had not        # yet been emitted, close it before the error text bubble so the UI        # doesn't strand a perpetual in-flight reasoning bubble. The        # `reasoning_ended` flag keeps this idempotent with the in-stream close        # and the normal-path cleanup.        if reasoning_started and not reasoning_ended:            yield encoder.encode(                ReasoningMessageEndEvent(                    type=EventType.REASONING_MESSAGE_END,                    message_id=reasoning_msg_id,                )            )            reasoning_ended = True        err_text = f"Agent error: {traceback.format_exc()}"        if not text_started:            yield encoder.encode(                TextMessageStartEvent(                    type=EventType.TEXT_MESSAGE_START,                    message_id=text_msg_id,                    role="assistant",                )            )            text_started = True        yield encoder.encode(            TextMessageContentEvent(                type=EventType.TEXT_MESSAGE_CONTENT,                message_id=text_msg_id,                delta=err_text,            )        )    if text_started:        yield encoder.encode(            TextMessageEndEvent(                type=EventType.TEXT_MESSAGE_END,                message_id=text_msg_id,            )        )    yield encoder.encode(        RunFinishedEvent(            type=EventType.RUN_FINISHED, thread_id=thread_id, run_id=run_id        )    )

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

reasoning_agent.py

page.tsx

reasoning-block.tsx

route.ts
    
    
    """Reasoning agent — emits AG-UI REASONING_MESSAGE_* events.Shared by:  - reasoning-custom (custom amber ReasoningBlock slot on the frontend)  - reasoning-default (CopilotKit's built-in reasoning slot)Approach:The Anthropic Python SDK supports Claude's extended-thinking ("thinkingbudget") parameter on `messages.stream`, which streams `thinking_delta`content blocks separately from text. We map those onto AG-UI'sREASONING_MESSAGE_* events. Models without extended-thinking fall backto an inline ``<reasoning>...</reasoning>`` system-prompt convention thatthis agent parses out of the text stream."""from __future__ import annotationsimport osimport tracebackfrom collections.abc import AsyncIteratorfrom textwrap import dedentfrom typing import Anyimport anthropicfrom ag_ui.core import (    EventType,    RunAgentInput,    RunFinishedEvent,    RunStartedEvent,    TextMessageContentEvent,    TextMessageEndEvent,    TextMessageStartEvent,)from ag_ui.encoder import EventEncoderfrom agents.claude_agent_sdk_adapter import normalize_claude_model# System prompt for the native adaptive-thinking path (the default).# Extended thinking is always enabled below, so the model already emits its# step-by-step plan on the native `thinking` channel — which we forward as# REASONING_MESSAGE_*. We must NOT also instruct the model to wrap a plan in# `<reasoning>...</reasoning>` text tags: against real Claude that produces a# SECOND reasoning block (native thinking + tag-text), i.e. the double-bubble.# So the native prompt asks only for a clean final answer; the reasoning chain# comes entirely from the native channel.NATIVE_REASONING_SYSTEM_PROMPT = dedent("""    You are a helpful assistant. Think through each user question    step-by-step, then give a single concise final answer for the user.    Do not wrap your answer in any XML or markup tags.""").strip()# Fallback system prompt for a NO-native-thinking deployment. If extended# thinking is ever disabled, the inline `<reasoning>...</reasoning>` tag# convention (parsed by the dormant state machine below) is the only way to# surface a reasoning chain, so this prompt re-instates the tag instruction.REASONING_SYSTEM_PROMPT = dedent("""    You are a helpful assistant. For each user question, FIRST emit a    short step-by-step plan inside `<reasoning>...</reasoning>` tags    (one or two short sentences per step, plain text only — no    Markdown, no JSON), THEN follow with the final concise answer for    the user OUTSIDE the tags.    The reasoning block is shown to the user as a visible "thinking"    chain — keep it brief and readable.    Example:    <reasoning>    The user is asking about X. I should consider Y and Z.    Combining both gives W.    </reasoning>    Final answer: W.""").strip()async def run_reasoning_agent(    input_data: RunAgentInput,    *,    system_prompt: str | None = None,) -> AsyncIterator[str]:    """Stream a reasoning-enabled assistant response as AG-UI events.    Splits Claude's response into REASONING_MESSAGE_* (everything inside    `<reasoning>...</reasoning>` tags) and TEXT_MESSAGE_* (everything    outside). Tags themselves are stripped before forwarding.    """    encoder = EventEncoder()    client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))    messages: list[dict[str, Any]] = []    for msg in input_data.messages or []:        role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)        if role not in ("user", "assistant"):            continue        raw_content = getattr(msg, "content", None)        content = ""        if isinstance(raw_content, str):            content = raw_content        elif isinstance(raw_content, list):            parts: list[str] = []            for part in raw_content:                if hasattr(part, "text"):                    parts.append(part.text)                elif isinstance(part, dict) and "text" in part:                    parts.append(part["text"])            content = "".join(parts)        if content:            messages.append({"role": role, "content": content})    thread_id = input_data.thread_id or "default"    run_id = input_data.run_id or "run-1"    yield encoder.encode(        RunStartedEvent(type=EventType.RUN_STARTED, thread_id=thread_id, run_id=run_id)    )    # Native extended thinking is always enabled on the stream below, so the    # reasoning chain comes from the native `thinking` channel. Pick the system    # prompt to MATCH that: the native prompt does NOT instruct the model to    # emit `<reasoning>` tags (which would double up as a second reasoning    # block against real Claude). The tag-instructing prompt + the inline-tag    # parser stay as a dormant fallback for a no-native-thinking deployment.    # An explicit caller-supplied `system_prompt` always wins.    _native_thinking_enabled = True    default_system = (        NATIVE_REASONING_SYSTEM_PROMPT        if _native_thinking_enabled        else REASONING_SYSTEM_PROMPT    )    system = system_prompt or default_system    text_msg_id = f"msg-{run_id}-text"    reasoning_msg_id = f"msg-{run_id}-reasoning"    # State machine for parsing <reasoning>...</reasoning>    REASONING_OPEN = "<reasoning>"    REASONING_CLOSE = "</reasoning>"    in_reasoning = False    reasoning_started = False    # Idempotency guard for the inline-`<reasoning>`-tag REASONING_MESSAGE_END.    # Set once END is emitted for `reasoning_msg_id` so the in-stream close, the    # post-stream buffer flush, and the error/early-end cleanup never    # double-emit an END for the same inline reasoning block.    reasoning_ended = False    text_started = False    buffer = ""    # Native extended-thinking streaming state. When the model (or aimock    # replay) emits Anthropic `thinking`/`thinking_delta` blocks we forward    # them as REASONING_MESSAGE_* directly — independent of the inline    # `<reasoning>`-tag text parsing below, which stays as the no-thinking    # fallback. Mirrors claude-sdk-typescript's /reasoning handler.    #    # A single turn may contain MORE THAN ONE `thinking` content block. Each    # gets its OWN message id (incorporating `id(block)`) assigned on its    # content_block_start, and `native_reasoning_started` is reset to False at    # BOTH block start and block stop so every thinking block emits its own    # balanced START/CONTENT/END lifecycle rather than reopening an already    # ENDED message id. `native_reasoning_id is not None` is the "a native    # thinking block is currently open" sentinel. Mirrors the sibling    # tool_rendering_reasoning_chain_agent.py pattern.    native_reasoning_id: str | None = None    native_reasoning_started = False    # Import lazily so missing imports don't crash module import-time    # on older ag_ui versions.    from ag_ui.core import (        ReasoningMessageContentEvent,        ReasoningMessageEndEvent,        ReasoningMessageStartEvent,    )    # Adaptive thinking enabled so Claude streams native thinking blocks.    # Overridable via ANTHROPIC_REASONING_MODEL (falling back to    # ANTHROPIC_MODEL). Under aimock replay the thinking channel comes from    # the fixture's `reasoning` field regardless of the model name.    reasoning_model = os.getenv(        "ANTHROPIC_REASONING_MODEL",        os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8"),    )    reasoning_model = normalize_claude_model(reasoning_model)    try:        async with client.messages.stream(            model=reasoning_model,            max_tokens=3072,            system=system,            messages=messages,            thinking={"type": "adaptive"},        ) as stream:            async for event in stream:                etype = type(event).__name__                if etype == "RawContentBlockStartEvent":                    block = event.content_block  # type: ignore[attr-defined]                    if getattr(block, "type", None) == "thinking":                        # Fresh per-block id so two thinking blocks in one turn                        # each get their own balanced lifecycle. Reset                        # `started` so a new START is emitted for THIS block.                        native_reasoning_id = f"msg-{run_id}-think-{id(block)}"                        native_reasoning_started = False                    continue                if etype in (                    "RawContentBlockStopEvent",                    "ParsedContentBlockStopEvent",                ):                    if native_reasoning_id is not None:                        if native_reasoning_started:                            yield encoder.encode(                                ReasoningMessageEndEvent(                                    type=EventType.REASONING_MESSAGE_END,                                    message_id=native_reasoning_id,                                )                            )                        # Reset both so the next thinking block starts clean.                        native_reasoning_id = None                        native_reasoning_started = False                    continue                if etype != "RawContentBlockDeltaEvent":                    continue                delta = event.delta  # type: ignore[attr-defined]                if delta.type == "thinking_delta" and native_reasoning_id:                    thinking_text = getattr(delta, "thinking", "") or ""                    if thinking_text:                        if not native_reasoning_started:                            native_reasoning_started = True                            yield encoder.encode(                                ReasoningMessageStartEvent(                                    type=EventType.REASONING_MESSAGE_START,                                    message_id=native_reasoning_id,                                    role="reasoning",                                )                            )                        yield encoder.encode(                            ReasoningMessageContentEvent(                                type=EventType.REASONING_MESSAGE_CONTENT,                                message_id=native_reasoning_id,                                delta=thinking_text,                            )                        )                    continue                if delta.type != "text_delta":                    continue                buffer += delta.text                # Drain the buffer, emitting either reasoning or text                # whenever we have enough to safely classify.                while True:                    if in_reasoning:                        close_idx = buffer.find(REASONING_CLOSE)                        if close_idx == -1:                            # Hold last few chars in case the close tag is split.                            keep = max(0, len(buffer) - len(REASONING_CLOSE))                            chunk = buffer[:keep]                            buffer = buffer[keep:]                            if chunk:                                if not reasoning_started:                                    yield encoder.encode(                                        ReasoningMessageStartEvent(                                            type=EventType.REASONING_MESSAGE_START,                                            message_id=reasoning_msg_id,                                            role="reasoning",                                        )                                    )                                    reasoning_started = True                                yield encoder.encode(                                    ReasoningMessageContentEvent(                                        type=EventType.REASONING_MESSAGE_CONTENT,                                        message_id=reasoning_msg_id,                                        delta=chunk,                                    )                                )                            break                        # Found close tag — emit remaining reasoning, end it, switch mode.                        chunk = buffer[:close_idx]                        if chunk:                            if not reasoning_started:                                yield encoder.encode(                                    ReasoningMessageStartEvent(                                        type=EventType.REASONING_MESSAGE_START,                                        message_id=reasoning_msg_id,                                        role="reasoning",                                    )                                )                                reasoning_started = True                            yield encoder.encode(                                ReasoningMessageContentEvent(                                    type=EventType.REASONING_MESSAGE_CONTENT,                                    message_id=reasoning_msg_id,                                    delta=chunk,                                )                            )                        if reasoning_started and not reasoning_ended:                            yield encoder.encode(                                ReasoningMessageEndEvent(                                    type=EventType.REASONING_MESSAGE_END,                                    message_id=reasoning_msg_id,                                )                            )                            reasoning_ended = True                        buffer = buffer[close_idx + len(REASONING_CLOSE) :]                        in_reasoning = False                        continue                    else:                        open_idx = buffer.find(REASONING_OPEN)                        if open_idx == -1:                            # No open tag in buffer — emit as text but hold tail in case tag is split.                            keep = max(0, len(buffer) - len(REASONING_OPEN))                            chunk = buffer[:keep]                            buffer = buffer[keep:]                            if chunk:                                # Skip leading whitespace-only fragments before any reasoning                                # so the empty assistant message doesn't appear.                                if not text_started:                                    yield encoder.encode(                                        TextMessageStartEvent(                                            type=EventType.TEXT_MESSAGE_START,                                            message_id=text_msg_id,                                            role="assistant",                                        )                                    )                                    text_started = True                                yield encoder.encode(                                    TextMessageContentEvent(                                        type=EventType.TEXT_MESSAGE_CONTENT,                                        message_id=text_msg_id,                                        delta=chunk,                                    )                                )                            break                        # Found open tag — flush text up to it, switch to reasoning mode.                        chunk = buffer[:open_idx]                        if chunk:                            if not text_started:                                yield encoder.encode(                                    TextMessageStartEvent(                                        type=EventType.TEXT_MESSAGE_START,                                        message_id=text_msg_id,                                        role="assistant",                                    )                                )                                text_started = True                            yield encoder.encode(                                TextMessageContentEvent(                                    type=EventType.TEXT_MESSAGE_CONTENT,                                    message_id=text_msg_id,                                    delta=chunk,                                )                            )                        buffer = buffer[open_idx + len(REASONING_OPEN) :]                        in_reasoning = True                        continue        # Lifecycle guarantee: if a native thinking block streamed content        # but its content_block_stop never arrived (e.g. stream ended early),        # still close the reasoning message so the UI doesn't render an        # in-flight thinking bubble.        if native_reasoning_id is not None and native_reasoning_started:            yield encoder.encode(                ReasoningMessageEndEvent(                    type=EventType.REASONING_MESSAGE_END,                    message_id=native_reasoning_id,                )            )            native_reasoning_id = None            native_reasoning_started = False        # Flush any remaining buffered content as text.        if buffer:            if in_reasoning:                if not reasoning_started:                    yield encoder.encode(                        ReasoningMessageStartEvent(                            type=EventType.REASONING_MESSAGE_START,                            message_id=reasoning_msg_id,                            role="reasoning",                        )                    )                    reasoning_started = True                yield encoder.encode(                    ReasoningMessageContentEvent(                        type=EventType.REASONING_MESSAGE_CONTENT,                        message_id=reasoning_msg_id,                        delta=buffer,                    )                )                if not reasoning_ended:                    yield encoder.encode(                        ReasoningMessageEndEvent(                            type=EventType.REASONING_MESSAGE_END,                            message_id=reasoning_msg_id,                        )                    )                    reasoning_ended = True            else:                if not text_started:                    yield encoder.encode(                        TextMessageStartEvent(                            type=EventType.TEXT_MESSAGE_START,                            message_id=text_msg_id,                            role="assistant",                        )                    )                    text_started = True                yield encoder.encode(                    TextMessageContentEvent(                        type=EventType.TEXT_MESSAGE_CONTENT,                        message_id=text_msg_id,                        delta=buffer,                    )                )        # Lifecycle guarantee for the inline-`<reasoning>`-tag block: if the        # stream ended mid-inline-block (open `<reasoning>` with started content        # but no `</reasoning>`) and the buffer-flush above did not already emit        # the END (e.g. the buffer was empty because all content had already        # been streamed), close it now so the UI doesn't render a perpetual        # in-flight reasoning bubble. Mirrors the native-channel guard above.        if reasoning_started and not reasoning_ended:            yield encoder.encode(                ReasoningMessageEndEvent(                    type=EventType.REASONING_MESSAGE_END,                    message_id=reasoning_msg_id,                )            )            reasoning_ended = True    except Exception:        # Lifecycle guarantee on the error path: if the stream raised while a        # native thinking block was still open, close it before emitting the        # error text bubble so the UI doesn't render a perpetual in-flight        # thinking bubble. Mirrors the normal-completion guard above.        if native_reasoning_id is not None and native_reasoning_started:            yield encoder.encode(                ReasoningMessageEndEvent(                    type=EventType.REASONING_MESSAGE_END,                    message_id=native_reasoning_id,                )            )            native_reasoning_id = None            native_reasoning_started = False        # Same guarantee for the inline-`<reasoning>`-tag block: if the stream        # raised while inside an open inline reasoning block whose END had not        # yet been emitted, close it before the error text bubble so the UI        # doesn't strand a perpetual in-flight reasoning bubble. The        # `reasoning_ended` flag keeps this idempotent with the in-stream close        # and the normal-path cleanup.        if reasoning_started and not reasoning_ended:            yield encoder.encode(                ReasoningMessageEndEvent(                    type=EventType.REASONING_MESSAGE_END,                    message_id=reasoning_msg_id,                )            )            reasoning_ended = True        err_text = f"Agent error: {traceback.format_exc()}"        if not text_started:            yield encoder.encode(                TextMessageStartEvent(                    type=EventType.TEXT_MESSAGE_START,                    message_id=text_msg_id,                    role="assistant",                )            )            text_started = True        yield encoder.encode(            TextMessageContentEvent(                type=EventType.TEXT_MESSAGE_CONTENT,                message_id=text_msg_id,                delta=err_text,            )        )    if text_started:        yield encoder.encode(            TextMessageEndEvent(                type=EventType.TEXT_MESSAGE_END,                message_id=text_msg_id,            )        )    yield encoder.encode(        RunFinishedEvent(            type=EventType.RUN_FINISHED, thread_id=thread_id, run_id=run_id        )    )

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
