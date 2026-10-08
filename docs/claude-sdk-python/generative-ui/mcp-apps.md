---
url: https://docs.copilotkit.ai/claude-sdk-python/generative-ui/mcp-apps/
title: MCP Apps
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:23.021086+00:00
---

# MCP Apps

> Source: https://docs.copilotkit.ai/claude-sdk-python/generative-ui/mcp-apps/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

[MCP Apps](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/open-generative-ui)

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

MCP Apps

Generative UIOpen-ended

# MCP Apps

Render interactive UI components from MCP servers directly in your chat interface.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

mcp_apps_agent.py

page.tsx

route.ts
    
    
    """Claude Agent SDK (Python) backend for the CopilotKit MCP Apps demo.This agent has no bespoke tools — the CopilotKit runtime is wired with``mcpApps: { servers: [...] }`` pointing at the public Excalidraw MCPserver (see ``src/app/api/copilotkit-mcp-apps/route.ts``). The runtimeauto-applies the MCP Apps middleware, which appends the remote MCPserver's tools to the AG-UI tool list forwarded to this agent on everyrequest and emits the activity events that CopilotKit's built-in``MCPAppsActivityRenderer`` renders in the chat as a sandboxed iframe.Implementation note:    The shared ``run_agent`` in ``src/agents/agent.py`` ships a fixed    sales-assistant tool registry (``TOOLS``) and ignores    ``input_data.tools``. For MCP Apps we want the OPPOSITE — no    bespoke tools, only the MCP-injected tools forwarded by the    runtime. So this module owns its own streaming loop that:    1. Builds the Anthropic ``tools`` list directly from       ``input_data.tools`` (the MCP middleware injects them there).    2. Streams Anthropic SSE through to AG-UI events.    3. Pass-through: when Claude emits ``tool_use``, we emit       ``TOOL_CALL_*`` events and stop. The MCP Apps middleware on the       runtime layer intercepts the call, fetches the UI resource,       emits the activity event, and re-invokes us with the tool       result. No server-side tool execution loop here.Reference:https://docs.copilotkit.ai/integrations/claude-agent-sdk-python/generative-ui/mcp-apps"""from __future__ import annotationsimport jsonimport osimport tracebackfrom collections.abc import AsyncIteratorfrom textwrap import dedentfrom typing import Anyimport anthropicfrom ag_ui.core import (    EventType,    RunAgentInput,    RunFinishedEvent,    RunStartedEvent,    TextMessageContentEvent,    TextMessageEndEvent,    TextMessageStartEvent,    ToolCallArgsEvent,    ToolCallEndEvent,    ToolCallStartEvent,)from ag_ui.encoder import EventEncoderfrom agents.claude_agent_sdk_adapter import normalize_claude_modelSYSTEM_PROMPT = dedent(    """    You draw simple diagrams in Excalidraw via the MCP tool.    SPEED MATTERS. Produce a correct-enough diagram fast; do not optimize    for polish. Target: one tool call, done in seconds.    When the user asks for a diagram:    1. Call `create_view` ONCE with 3-5 elements total: shapes + arrows +       an optional title text.    2. Use straightforward shapes (rectangle, ellipse, diamond) with plain       `label` fields (`{"text": "...", "fontSize": 18}`) on them.    3. Connect with arrows. Endpoints can be element centers or simple       coordinates — you don't need edge anchors / fixedPoint bindings.    4. Include ONE `cameraUpdate` at the END of the elements array that       frames the whole diagram. Use an approved 4:3 size (600x450 or       800x600). No opening camera needed.    5. Reply with ONE short sentence describing what you drew.    Every element needs a unique string `id` (e.g. `"b1"`, `"a1"`,    `"title"`). Standard sizes: rectangles 160x70, ellipses/diamonds    120x80, 40-80px gap between shapes.    Do NOT:    - Call `read_me`. You already know the basic shape API.    - Make multiple `create_view` calls.    - Iterate or refine. Ship on the first shot.    - Add decorative colors / fills / zone backgrounds unless the user      explicitly asks for them.    - Add labels on arrows unless crucial.    If the user asks for something specific (colors, more elements,    particular layout), follow their lead — but still in ONE call.    """).strip()def _build_anthropic_tools(input_tools: list[Any] | None) -> list[dict[str, Any]]:    """Map AG-UI ``input_data.tools`` into Anthropic ``tools`` schemas.    The MCP Apps middleware appends MCP server tools to ``input_data.tools``    on every request. We forward them to Anthropic verbatim so Claude    can pick the right MCP tool to call.    """    if not input_tools:        return []    out: list[dict[str, Any]] = []    for tool in input_tools:        name = getattr(tool, "name", None) or (            tool.get("name") if isinstance(tool, dict) else None        )        if not name:            continue        description = getattr(tool, "description", None) or (            tool.get("description") if isinstance(tool, dict) else ""        )        parameters = getattr(tool, "parameters", None)        if parameters is None and isinstance(tool, dict):            parameters = tool.get("parameters")        # ``parameters`` is a JSON schema (or a JSON-encoded string).        if isinstance(parameters, str):            try:                parameters = json.loads(parameters)            except json.JSONDecodeError:                parameters = {"type": "object", "properties": {}}        if not isinstance(parameters, dict):            parameters = {"type": "object", "properties": {}}        out.append(            {                "name": name,                "description": description or "",                "input_schema": parameters,            }        )    return outdef _convert_messages(input_data: RunAgentInput) -> list[dict[str, Any]]:    """Flatten AG-UI messages into Anthropic ``messages`` shape.    Preserve frontend/MCP tool continuations: after the runtime resolves a    tool call it re-invokes this agent with the original assistant tool_use    plus a tool result message. Anthropic needs those as structured    assistant/user blocks, not flattened text, or the model never sees the MCP    result and can repeat the same call.    """    messages: list[dict[str, Any]] = []    for msg in input_data.messages or []:        role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)        if role == "tool":            tool_call_id = getattr(msg, "tool_call_id", None) or (                getattr(msg, "toolCallId", None)            )            raw_content = getattr(msg, "content", None)            result_text = _text_from_content(raw_content)            if tool_call_id:                messages.append(                    {                        "role": "user",                        "content": [                            {                                "type": "tool_result",                                "tool_use_id": tool_call_id,                                "content": result_text,                            }                        ],                    }                )            continue        if role not in ("user", "assistant"):            continue        raw_content = getattr(msg, "content", None)        content = _text_from_content(raw_content)        if role == "assistant":            tool_calls = getattr(msg, "tool_calls", None) or getattr(                msg, "toolCalls", None            )            if tool_calls:                content_blocks: list[dict[str, Any]] = []                if content:                    content_blocks.append({"type": "text", "text": content})                for tool_call in tool_calls:                    tool_call_id = getattr(tool_call, "id", None) or (                        tool_call.get("id") if isinstance(tool_call, dict) else None                    )                    function = getattr(tool_call, "function", None) or (                        tool_call.get("function")                        if isinstance(tool_call, dict)                        else None                    )                    tool_name = "unknown"                    args_raw: Any = "{}"                    if function:                        tool_name = getattr(function, "name", None) or (                            function.get("name")                            if isinstance(function, dict)                            else "unknown"                        )                        args_raw = getattr(function, "arguments", None) or (                            function.get("arguments", "{}")                            if isinstance(function, dict)                            else "{}"                        )                    try:                        tool_args = (                            json.loads(args_raw)                            if isinstance(args_raw, str)                            else args_raw                        )                    except json.JSONDecodeError:                        tool_args = {}                    content_blocks.append(                        {                            "type": "tool_use",                            "id": tool_call_id or "unknown",                            "name": tool_name,                            "input": tool_args,                        }                    )                messages.append({"role": "assistant", "content": content_blocks})                continue        if content:            messages.append({"role": role, "content": content})    return messagesdef _text_from_content(raw_content: Any) -> str:    if isinstance(raw_content, str):        return raw_content    if isinstance(raw_content, list):        parts: list[str] = []        for part in raw_content:            if hasattr(part, "text"):                parts.append(part.text)            elif isinstance(part, dict) and "text" in part:                parts.append(part["text"])        parts_text = "".join(parts)        return parts_text if parts_text else json.dumps(raw_content)    return ""async def run_mcp_apps_agent(input_data: RunAgentInput) -> AsyncIterator[str]:    """Pass-through Claude streaming loop for the MCP Apps demo.    No bespoke tools. No server-side tool execution. Tools come in via    the AG-UI request (injected by the MCP Apps middleware), and tool    calls go back out as AG-UI events for the runtime middleware to    intercept.    """    encoder = EventEncoder()    client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))    thread_id = input_data.thread_id or "default"    run_id = input_data.run_id or "run-1"    msg_id = f"msg-{run_id}"    yield encoder.encode(        RunStartedEvent(type=EventType.RUN_STARTED, thread_id=thread_id, run_id=run_id)    )    tools = _build_anthropic_tools(input_data.tools)    messages = _convert_messages(input_data)    yield encoder.encode(        TextMessageStartEvent(            type=EventType.TEXT_MESSAGE_START,            message_id=msg_id,            role="assistant",        )    )    try:        stream_kwargs: dict[str, Any] = {            "model": normalize_claude_model(                os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8")            ),            "max_tokens": 4096,            "system": SYSTEM_PROMPT,            "messages": messages,        }        if tools:            stream_kwargs["tools"] = tools        async with client.messages.stream(**stream_kwargs) as stream:            current_tool_id: str | None = None            current_tool_name: str | None = None            async for event in stream:                etype = type(event).__name__                if etype == "RawContentBlockStartEvent":                    block = event.content_block  # type: ignore[attr-defined]                    if block.type == "tool_use":                        current_tool_id = block.id                        current_tool_name = block.name                        yield encoder.encode(                            ToolCallStartEvent(                                type=EventType.TOOL_CALL_START,                                tool_call_id=current_tool_id,                                tool_call_name=current_tool_name,                                parent_message_id=msg_id,                            )                        )                elif etype == "RawContentBlockDeltaEvent":                    delta = event.delta  # type: ignore[attr-defined]                    if delta.type == "text_delta":                        yield encoder.encode(                            TextMessageContentEvent(                                type=EventType.TEXT_MESSAGE_CONTENT,                                message_id=msg_id,                                delta=delta.text,                            )                        )                    elif delta.type == "input_json_delta" and current_tool_id:                        yield encoder.encode(                            ToolCallArgsEvent(                                type=EventType.TOOL_CALL_ARGS,                                tool_call_id=current_tool_id,                                delta=delta.partial_json,                            )                        )                elif etype in (                    "RawContentBlockStopEvent",                    "ParsedContentBlockStopEvent",                ):                    if current_tool_id:                        yield encoder.encode(                            ToolCallEndEvent(                                type=EventType.TOOL_CALL_END,                                tool_call_id=current_tool_id,                            )                        )                        current_tool_id = None                        current_tool_name = None    except Exception:        # Surface error as visible chat text so probes catch it instead        # of silently breaking the SSE stream. Mirrors the pattern in        # ``agents.agent.run_agent``.        err_text = f"Agent error: {traceback.format_exc()}"        yield encoder.encode(            TextMessageContentEvent(                type=EventType.TEXT_MESSAGE_CONTENT,                message_id=msg_id,                delta=err_text,            )        )    yield encoder.encode(        TextMessageEndEvent(type=EventType.TEXT_MESSAGE_END, message_id=msg_id)    )    yield encoder.encode(        RunFinishedEvent(            type=EventType.RUN_FINISHED, thread_id=thread_id, run_id=run_id        )    )

## What is this?#

MCP Apps are MCP servers that expose tools with associated UI resources. When the agent calls one of these tools, CopilotKit automatically fetches the resource and renders the UI component in the chat; no additional frontend code required.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

Key benefits:

  * **Zero frontend code** — UI components are served by the MCP server
  * **Full interactivity** — components can use HTML, CSS, and JavaScript
  * **Secure sandboxing** — content runs in isolated iframes
  * **Thread persistence** — MCP Apps are stored in conversation history and restored on reconnect



## Wire the runtime to your MCP server(s)#

A single `mcpApps.servers` entry on the runtime is all it takes. The runtime auto-applies the MCP Apps middleware to every registered agent: each time an agent calls a tool backed by an MCP UI resource, the middleware fetches the resource and emits an `activity` event that the built-in `MCPAppsActivityRenderer` renders inline in the chat as a sandboxed iframe.

route.ts
    
    
    // The `mcpApps.servers` config is all you need server-side. The runtime// auto-applies the MCP Apps middleware to every registered agent: on each// MCP tool call it fetches the associated UI resource and emits an// `activity` event that the built-in `MCPAppsActivityRenderer` renders// inline in the chat.const runtime = new CopilotRuntime({  // @ts-ignore -- Published CopilotRuntime agents type wraps Record in MaybePromise<NonEmptyRecord<...>> which rejects plain Records; fixed in source, pending release  agents,  mcpApps: {    servers: [      {        type: "http",        url: process.env.MCP_SERVER_URL || "https://mcp.excalidraw.com",        // Always pin a stable `serverId`. Without it CopilotKit hashes the        // URL, and a URL change silently breaks restoration of persisted        // MCP Apps in prior conversation threads.        serverId: "excalidraw",      },    ],  },});

Always pin a serverId

In production, always provide a stable `serverId`. Without it, CopilotKit hashes the server URL, and a URL change (for example between environments) silently breaks restoration of MCP Apps persisted in earlier conversation threads.

## No frontend renderer needed#

Unlike custom activity types, the MCP Apps renderer is already registered by `CopilotKit` out of the box. A plain `<CopilotChat />` is enough; no `renderActivityMessages` prop, no manual `useRenderActivityMessage` wiring.

page.tsx
    
    
      // No `renderActivityMessages`, no `useRenderActivityMessage` — the  // CopilotKitProvider auto-registers the built-in `MCPAppsActivityRenderer`  // for the "mcp-apps" activity type. A plain <CopilotChat /> is enough.  return (    <CopilotKit runtimeUrl="/api/copilotkit-mcp-apps" agent="mcp-apps">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );

## Transport types#

The middleware supports two transport types:

### HTTP#

Use this format to connect to an MCP server that accepts standard HTTP requests:
    
    
    {
      type: "http",
      url: "http://localhost:3101/mcp",
      serverId: "my-http-server"
    }

### SSE#

Use this format to connect to an MCP server that streams events over a persistent connection:
    
    
    {
      type: "sse",
      url: "https://mcp.example.com/sse",
      headers: {
        "Authorization": "Bearer token"
      },
      serverId: "my-sse-server"
    }

## Example MCP servers#

Try these open-source MCP Apps servers to get started:

  * [Excalidraw](https://mcp.excalidraw.com) — collaborative whiteboard rendered in-chat
  * [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps) — canonical reference implementations



### On this page

What is this?Wire the runtime to your MCP server(s)No frontend renderer neededTransport typesHTTPSSEExample MCP servers
