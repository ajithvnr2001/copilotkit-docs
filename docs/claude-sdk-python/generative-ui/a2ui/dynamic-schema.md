---
url: https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui/dynamic-schema/
title: Dynamic Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:20.823673+00:00
---

# Dynamic Schema A2UI

> Source: https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui/dynamic-schema/

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

[A2UI](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/hashbrown)

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

Dynamic Schema A2UI

Generative UIDeclarativeA2UI

# Dynamic Schema A2UI

LLM-generated A2UI. A secondary LLM creates both the schema and data from any prompt.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

a2ui_dynamic.py

page.tsx

catalog.ts

definitions.ts

renderers.tsx

route.ts
    
    
    """Claude Agent SDK backend for the Declarative Generative UI (A2UI Dynamic) demo.The agent exposes a single `generate_a2ui(context: str)` tool. When called,it invokes a secondary Claude call bound to the `render_a2ui` tool schema(forced via `tool_choice`) and returns an `a2ui_operations` container whichthe runtime's A2UI middleware detects and forwards to the frontend renderer.The dedicated runtime route (`api/copilotkit-declarative-gen-ui/route.ts`)sets `injectA2UITool: false` so the runtime does not double-bind a secondA2UI tool on top of this one — the registered client catalog is stillserialised into `copilotkit.context` so the secondary LLM knows what'savailable.Mirrors the langgraph-python and ag2 references."""from __future__ import annotationsimport asyncioimport jsonimport osimport tracebackfrom collections.abc import AsyncIteratorfrom textwrap import dedentfrom typing import Anyimport anthropicfrom ag_ui.core import (    EventType,    RunAgentInput,    RunFinishedEvent,    RunStartedEvent,    TextMessageContentEvent,    TextMessageEndEvent,    TextMessageStartEvent,    ToolCallArgsEvent,    ToolCallEndEvent,    ToolCallResultEvent,    ToolCallStartEvent,)from ag_ui.encoder import EventEncoderfrom tools import (    RENDER_A2UI_TOOL_SCHEMA,    build_a2ui_operations_from_tool_call,)from agents._anthropic_message_safety import sanitize_unresolved_tool_usesfrom agents.claude_agent_sdk_adapter import normalize_claude_modelSYSTEM_PROMPT = dedent("""    You are a demo assistant for Declarative Generative UI (A2UI — Dynamic    Schema). Whenever a response would benefit from a rich visual — a    dashboard, status report, KPI summary, card layout, info grid, a    pie/donut chart of part-of-whole breakdowns, a bar chart comparing    values across categories, or anything more structured than plain text —    call `generate_a2ui` to draw it. The registered catalog includes    `Card`, `StatusBadge`, `Metric`, `InfoRow`, `PrimaryButton`, `PieChart`,    and `BarChart` (in addition to the basic A2UI primitives). Prefer    `PieChart` for part-of-whole breakdowns and `BarChart` for comparisons    across categories. `generate_a2ui` takes a single `context` argument    summarising the conversation. Keep chat replies to one short sentence;    let the UI do the talking.""").strip()GENERATE_A2UI_TOOL = {    "name": "generate_a2ui",    "description": (        "Generate dynamic A2UI components based on the conversation. "        "A secondary LLM designs the UI schema and data using the registered catalog."    ),    "input_schema": {        "type": "object",        "properties": {            "context": {                "type": "string",                "description": "Conversation context summary the secondary LLM should design UI from.",            },        },        "required": ["context"],    },}def _generate_a2ui(    context: str, conversation_messages: list[dict[str, Any]] | None = None) -> dict[str, Any]:    """Invoke a secondary LLM bound to render_a2ui and return an operations container."""    client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))    render_tool_schema = {        "name": RENDER_A2UI_TOOL_SCHEMA["name"],        "description": RENDER_A2UI_TOOL_SCHEMA["description"],        "input_schema": RENDER_A2UI_TOOL_SCHEMA["parameters"],    }    llm_messages = (        sanitize_unresolved_tool_uses(conversation_messages)        if conversation_messages        else [            {                "role": "user",                "content": "Generate a dynamic A2UI dashboard based on the conversation.",            }        ]    )    response = client.messages.create(        model=normalize_claude_model(os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8")),        max_tokens=4096,        system=context or "Generate a useful dashboard UI.",        messages=llm_messages,        tools=[render_tool_schema],        tool_choice={"type": "tool", "name": "render_a2ui"},    )    for block in response.content:        if getattr(block, "type", None) == "tool_use" and block.name == "render_a2ui":            return build_a2ui_operations_from_tool_call(dict(block.input))    return {"error": "LLM did not call render_a2ui"}async def run_a2ui_dynamic_agent(input_data: RunAgentInput) -> AsyncIterator[str]:    """Stream a Claude conversation that may call `generate_a2ui`."""    encoder = EventEncoder()    client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))    messages: list[dict[str, Any]] = []    for msg in input_data.messages or []:        role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)        if role not in ("user", "assistant"):            continue        raw = getattr(msg, "content", None)        content = ""        if isinstance(raw, str):            content = raw        elif isinstance(raw, list):            parts = []            for part in raw:                if hasattr(part, "text"):                    parts.append(part.text)                elif isinstance(part, dict) and "text" in part:                    parts.append(part["text"])            content = "".join(parts)        if content:            messages.append({"role": role, "content": content})    thread_id = input_data.thread_id or "default"    run_id = input_data.run_id or "run-1"    yield encoder.encode(        RunStartedEvent(type=EventType.RUN_STARTED, thread_id=thread_id, run_id=run_id)    )    # Maximum tool iterations per run. `generate_a2ui` normally renders in a    # single turn, but a misbehaving model could keep re-calling the tool and    # never yield an empty `tool_calls` turn — which would wedge the run and    # RUN_FINISHED would never fire (done-signal-missing timeout). Cap the loop    # so the run always terminates. Mirrors the claude-sdk-typescript sibling's    # MAX_TOOL_ITERATIONS bound.    MAX_TOOL_ITERATIONS = 10    for _iter in range(MAX_TOOL_ITERATIONS):        msg_id = f"msg-{run_id}-{len(messages)}"        yield encoder.encode(            TextMessageStartEvent(                type=EventType.TEXT_MESSAGE_START,                message_id=msg_id,                role="assistant",            )        )        response_text = ""        tool_calls: list[dict[str, Any]] = []        try:            async with client.messages.stream(                model=normalize_claude_model(                    os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8")                ),                max_tokens=2048,                system=SYSTEM_PROMPT,                messages=messages,                tools=[GENERATE_A2UI_TOOL],            ) as stream:                current_tool_id: str | None = None                current_tool_name: str | None = None                current_tool_args = ""                async for event in stream:                    etype = type(event).__name__                    if etype == "RawContentBlockStartEvent":                        block = event.content_block  # type: ignore[attr-defined]                        if block.type == "tool_use":                            current_tool_id = block.id                            current_tool_name = block.name                            current_tool_args = ""                            yield encoder.encode(                                ToolCallStartEvent(                                    type=EventType.TOOL_CALL_START,                                    tool_call_id=current_tool_id,                                    tool_call_name=current_tool_name,                                    parent_message_id=msg_id,                                )                            )                    elif etype == "RawContentBlockDeltaEvent":                        delta = event.delta  # type: ignore[attr-defined]                        if delta.type == "text_delta":                            response_text += delta.text                            yield encoder.encode(                                TextMessageContentEvent(                                    type=EventType.TEXT_MESSAGE_CONTENT,                                    message_id=msg_id,                                    delta=delta.text,                                )                            )                        elif delta.type == "input_json_delta":                            current_tool_args += delta.partial_json                            yield encoder.encode(                                ToolCallArgsEvent(                                    type=EventType.TOOL_CALL_ARGS,                                    tool_call_id=current_tool_id or "",                                    delta=delta.partial_json,                                )                            )                    elif etype in (                        "RawContentBlockStopEvent",                        "ParsedContentBlockStopEvent",                    ):                        if current_tool_id and current_tool_name:                            yield encoder.encode(                                ToolCallEndEvent(                                    type=EventType.TOOL_CALL_END,                                    tool_call_id=current_tool_id,                                )                            )                            try:                                parsed = (                                    json.loads(current_tool_args)                                    if current_tool_args                                    else {}                                )                            except json.JSONDecodeError:                                parsed = {}                            tool_calls.append(                                {                                    "id": current_tool_id,                                    "name": current_tool_name,                                    "input": parsed,                                }                            )                            current_tool_id = None                            current_tool_name = None                            current_tool_args = ""        except Exception:            err_text = f"Agent error: {traceback.format_exc()}"            yield encoder.encode(                TextMessageContentEvent(                    type=EventType.TEXT_MESSAGE_CONTENT,                    message_id=msg_id,                    delta=err_text,                )            )        yield encoder.encode(            TextMessageEndEvent(                type=EventType.TEXT_MESSAGE_END,                message_id=msg_id,            )        )        if not tool_calls:            break        # Build assistant turn with tool_use blocks.        assistant_content: list[dict[str, Any]] = []        if response_text:            assistant_content.append({"type": "text", "text": response_text})        for tc in tool_calls:            assistant_content.append(                {                    "type": "tool_use",                    "id": tc["id"],                    "name": tc["name"],                    "input": tc["input"],                }            )        messages.append({"role": "assistant", "content": assistant_content})        # Execute generate_a2ui and emit tool_result.        tool_results: list[dict[str, Any]] = []        for tc in tool_calls:            if tc["name"] == "generate_a2ui":                ctx = tc["input"].get("context", "")                try:                    # Offload to a worker thread: _generate_a2ui runs a                    # synchronous anthropic.Anthropic() LLM round-trip, which                    # would otherwise block the uvicorn event loop and wedge the                    # :8000 /health endpoint under load.                    result_obj = await asyncio.to_thread(                        _generate_a2ui, ctx, conversation_messages=messages                    )                    result_text = json.dumps(result_obj)                except Exception as exc:  # noqa: BLE001 - surface as tool result                    result_text = json.dumps(                        {                            "error": "generate_a2ui failed",                            "detail": exc.__class__.__name__,                        }                    )            else:                result_text = json.dumps({"error": f"unknown tool {tc['name']}"})            yield encoder.encode(                ToolCallResultEvent(                    type=EventType.TOOL_CALL_RESULT,                    tool_call_id=tc["id"],                    message_id=f"{msg_id}-tool-result-{tc['id']}",                    content=result_text,                )            )            tool_results.append(                {                    "type": "tool_result",                    "tool_use_id": tc["id"],                    "content": result_text,                }            )        messages.append({"role": "user", "content": tool_results})    yield encoder.encode(        RunFinishedEvent(            type=EventType.RUN_FINISHED, thread_id=thread_id, run_id=run_id        )    )

In the dynamic-schema approach, a secondary LLM generates the entire UI (schema, data, and layout) based on the conversation context. It's the most flexible A2UI flavor; the agent can render any UI for any request without pre-defined schemas.

## How it works#

  1. The agent calls the A2UI tool to draw a surface, made available when `injectA2UITool: true`.
  2. The runtime serializes your client-side catalog (component names + Zod prop schemas) into the agent's `copilotkit.context` so the LLM knows which components it may emit.
  3. The tool call streams through LangGraph as `TOOL_CALL_ARGS` events.
  4. The A2UI middleware intercepts the stream and renders cards progressively as data items arrive.



## The 3-file split#

The canonical Bring-Your-Own-Catalog (BYOC) layout keeps three files side-by-side under `frontend/src/app/a2ui/`:

File| What lives there  
---|---  
`definitions.ts`| Zod props schema + human-readable descriptions for each custom component. Platform-agnostic, so the runtime can serialise it to the LLM.  
`renderers.tsx`| React implementations keyed by the same names. TypeScript enforces that every definition has a renderer.  
`catalog.ts`| `createCatalog(definitions, renderers, { includeBasicCatalog: true })`: merges your custom components with CopilotKit's built-in primitives.  
  
### Declare your custom component definitions#

Each entry pairs a Zod prop schema with a description. The description is crucial; the LLM reads it to decide which component to emit. The example below ships a small dashboard catalog (Card / StatusBadge / Metric / InfoRow / PrimaryButton):

definitions.ts
    
    
    import { z } from "zod";import type { CatalogDefinitions } from "@copilotkit/a2ui-renderer";export const myDefinitions = {  Card: {    description:      "A titled card container with an optional subtitle and a single child slot. Use it to group related content (metrics, rows, buttons).",    props: z.object({      title: z.string(),      subtitle: z.string().optional(),      child: z.string().optional(),    }),  },  StatusBadge: {    description:      "A small coloured pill communicating the state of something (healthy/degraded/down, online/offline, open/closed). Choose `variant` to match the intent.",    props: z.object({      text: z.string(),      variant: z.enum(["success", "warning", "error", "info"]).optional(),    }),  },  Metric: {    description:      "A key/value KPI display with an optional trend indicator. Ideal for dashboards (e.g. 'Revenue • $12.4k • up').",    props: z.object({      label: z.string(),      value: z.string(),      trend: z.enum(["up", "down", "neutral"]).optional(),    }),  },  InfoRow: {    description:      "A compact two-column 'label: value' row. Good for stacks of facts inside a Card (owner, region, last updated, etc.).",    props: z.object({      label: z.string(),      value: z.string(),    }),  },  DataTable: {    description:      "A data table with column headers and rows. Ideal for rankings and per-person/per-item breakdowns (rep performance vs quota, deal lists). Each row's keys MUST appear in `columns[].key`; unknown row keys render as blank cells and indicate model/schema drift.",    props: z.object({      columns: z.array(z.object({ key: z.string(), label: z.string() })),      // Cells may be strings or numbers — the renderer stringifies at      // render time, but accepting both lets the LLM emit raw numerics      // (e.g. attainment 124) instead of being forced to stringify.      rows: z.array(z.record(z.union([z.string(), z.number()]))),    }),  },  PrimaryButton: {    description:      "A styled primary call-to-action button. Attach an optional `action` that will be dispatched back to the agent when the user clicks it.",    props: z.object({      label: z.string(),      action: z.any().optional(),    }),  },  PieChart: {    description:      "A pie/donut chart with a brand-coloured legend. Provide `title`, `description`, and `data` as an array of `{ label, value }` objects. Great for part-of-whole breakdowns (sales by region, traffic sources, portfolio allocation).",    props: z.object({      title: z.string(),      description: z.string(),      data: z.array(        z.object({          label: z.string(),          value: z.number(),        }),      ),    }),  },  BarChart: {    description:      "A vertical bar chart built on Recharts. Provide `title`, `description`, and `data` as an array of `{ label, value }` objects. Great for comparing series across categories (quarterly revenue, headcount by team, signups per month).",    props: z.object({      title: z.string(),      description: z.string(),      data: z.array(        z.object({          label: z.string(),          value: z.number(),        }),      ),    }),  },} satisfies CatalogDefinitions;

### Implement the React renderers#

Every key in `myDefinitions` must have a matching renderer. Props are statically typed against the Zod schema, so refactors stay safe:

renderers.tsx
    
    
    export const myRenderers: CatalogRenderers<MyDefinitions> = {  Card: ({ props, children }) => (    <Card      className="w-full min-w-0 overflow-hidden"      data-testid="declarative-card"    >      <CardHeader>        <CardTitle>{props.title}</CardTitle>        {props.subtitle && <CardDescription>{props.subtitle}</CardDescription>}      </CardHeader>      {props.child && (        <CardContent className="flex flex-col gap-4">          {children(props.child)}        </CardContent>      )}    </Card>  ),  StatusBadge: ({ props }) => (    <Badge      variant={props.variant ?? "info"}      data-testid="declarative-status-badge"    >      {props.text}    </Badge>  ),  Metric: ({ props }) => {    const trend = props.trend ?? "neutral";    const arrow = trend === "up" ? "↑" : trend === "down" ? "↓" : "";    const trendClass =      trend === "up"        ? "text-emerald-600"        : trend === "down"          ? "text-rose-600"          : "text-[var(--foreground)]";    return (      // `flex-1 min-w-[120px]` lets a row of Metrics distribute evenly      // inside the basic catalog's gap-less Row — 3 metrics in a 600px      // card column get ~200px each instead of squishing to content width.      <div        data-testid="declarative-metric"        className="flex flex-1 min-w-[120px] flex-col gap-1"      >        <div className="text-xs font-medium uppercase tracking-wider text-[var(--muted-foreground)]">          {props.label}        </div>        <div          className={`flex items-baseline gap-1.5 text-2xl font-semibold tabular-nums ${trendClass}`}        >          <span>{props.value}</span>          {arrow && <span className="text-base">{arrow}</span>}        </div>      </div>    );  },  InfoRow: ({ props }) => (    // Divider via `border-b last:border-b-0` so the final row doesn't dangle    // a trailing line, regardless of whether the agent wraps these in a    // Column or drops them directly into a Card's child slot.    <div      data-testid="declarative-info-row"      className="flex items-baseline justify-between gap-4 py-2 border-b border-[var(--border)] last:border-b-0 last:pb-0 first:pt-0"    >      <span className="text-sm text-[var(--muted-foreground)]">        {props.label}      </span>      <span className="text-sm font-medium text-[var(--foreground)] text-right tabular-nums">        {props.value}      </span>    </div>  ),  DataTable: ({ props }) => {    const cols = Array.isArray(props.columns) ? props.columns : [];    const rows = Array.isArray(props.rows) ? props.rows : [];    return (      <div        data-testid="declarative-data-table"        className="w-full overflow-x-auto"      >        <table className="w-full border-collapse text-sm">          <thead>            <tr>              {cols.map((col) => (                <th                  key={col.key}                  className="border-b-2 border-[var(--border)] px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-[var(--muted-foreground)]"                >                  {col.label}                </th>              ))}            </tr>          </thead>          <tbody>            {rows.map((row, i) => {              // Stable row key: prefer the first column's value (primary-key-ish),              // suffix with index in case values repeat, fall back to a JSON              // stringify of the row when columns is empty. Stable keys prevent              // React from re-mounting every row when the agent re-emits a              // slightly different table.              const pk = cols.length > 0 ? row[cols[0].key] : undefined;              const rowKey =                pk !== undefined ? `${pk}-${i}` : JSON.stringify(row);              return (                <tr                  key={rowKey}                  className="border-b border-[var(--border)] last:border-b-0"                >                  {cols.map((col) => (                    <td                      key={col.key}                      className="px-3 py-2 tabular-nums text-[var(--foreground)]"                    >                      {String(row[col.key] ?? "")}                    </td>                  ))}                </tr>              );            })}          </tbody>        </table>      </div>    );  },  PrimaryButton: ({ props, dispatch }) => (    <Button      onClick={() => {        if (props.action && dispatch) dispatch(props.action);      }}    >      {props.label}    </Button>  ),  PieChart: ({ props }) => {    const data = props.data ?? [];    const safeData = Array.isArray(data) ? data : [];    const total = safeData.reduce((sum, d) => sum + (Number(d.value) || 0), 0);    return (      // `flex-1 min-w-0` so multiple charts in a basic-catalog Row      // distribute the available width evenly instead of each insisting      // on its content size and overflowing.      <Card        className="w-full flex-1 min-w-0 overflow-hidden"        data-testid="declarative-pie-chart"      >        <CardHeader>          <CardTitle>{props.title}</CardTitle>          <CardDescription>{props.description}</CardDescription>        </CardHeader>        <CardContent className="flex flex-col gap-4">          {safeData.length === 0 ? (            <div className="py-8 text-center text-sm text-[var(--muted-foreground)]">              No data available            </div>          ) : (            <>              <DonutChart data={safeData} />              <div className="flex flex-col gap-2 pt-2">                {safeData.map((item, index) => {                  const val = Number(item.value) || 0;                  const pct =                    total > 0 ? ((val / total) * 100).toFixed(0) : "0";                  return (                    <div                      key={index}                      className="flex items-center gap-3 text-sm"                    >                      <span                        className="inline-block h-2.5 w-2.5 shrink-0 rounded-sm"                        style={{                          backgroundColor:                            CHART_COLORS[index % CHART_COLORS.length],                        }}                      />                      <span className="flex-1 truncate text-[var(--foreground)]">                        {item.label}                      </span>                      <span className="tabular-nums text-[var(--muted-foreground)]">                        {val.toLocaleString()}                      </span>                      <span className="w-10 text-right tabular-nums text-[var(--muted-foreground)]">                        {pct}%                      </span>                    </div>                  );                })}              </div>            </>          )}        </CardContent>      </Card>    );  },  BarChart: ({ props }) => {    const { isNew } = useSeenIndices();    const data = props.data ?? [];    const safeData = Array.isArray(data) ? data : [];    return (      <Card        className="w-full flex-1 min-w-0 overflow-hidden"        data-testid="declarative-bar-chart"      >        {/* Scoped keyframe — no globals.css needed */}        <style>{`          @keyframes barSlideIn {            from { transform: translateY(40px); opacity: 0; }            20% { opacity: 1; }            to { transform: translateY(0); opacity: 1; }          }        `}</style>        <CardHeader>          <CardTitle>{props.title}</CardTitle>          <CardDescription>{props.description}</CardDescription>        </CardHeader>        <CardContent>          {safeData.length === 0 ? (            <div className="py-8 text-center text-sm text-[var(--muted-foreground)]">              No data available            </div>          ) : (            <ResponsiveContainer width="100%" height={260}>              <RechartsBarChart                data={safeData}                margin={{ top: 12, right: 12, bottom: 4, left: -8 }}              >                <CartesianGrid                  strokeDasharray="3 3"                  stroke="var(--border)"                  vertical={false}                />                <XAxis                  dataKey="label"                  tick={{ fontSize: 12, fill: "var(--muted-foreground)" }}                  stroke="var(--border)"                  tickLine={false}                  axisLine={false}                />                <YAxis                  tick={{ fontSize: 12, fill: "var(--muted-foreground)" }}                  stroke="var(--border)"                  tickLine={false}                  axisLine={false}                />                <Tooltip                  contentStyle={CHART_TOOLTIP_STYLE}                  cursor={{ fill: "var(--muted)", opacity: 0.5 }}                />                <Bar                  isAnimationActive={false}                  dataKey="value"                  radius={[6, 6, 0, 0]}                  maxBarSize={48}                  // eslint-disable-next-line @typescript-eslint/no-explicit-any                  shape={                    ((barProps: any) => (                      <AnimatedBar                        {...barProps}                        isNew={isNew(barProps.index as number)}                      />                      // eslint-disable-next-line @typescript-eslint/no-explicit-any                    )) as any                  }                >                  {safeData.map((_, index) => (                    <Cell                      key={index}                      fill={CHART_COLORS[index % CHART_COLORS.length]}                    />                  ))}                </Bar>              </RechartsBarChart>            </ResponsiveContainer>          )}        </CardContent>      </Card>    );  },};

### Wire definitions × renderers into a catalog#

`createCatalog` is what you hand to the provider. Flip `includeBasicCatalog: true` to merge CopilotKit's built-ins (Column, Row, Text, Image, Card, Button, List, Tabs, …), so the LLM can compose custom + basic components interchangeably:

catalog.ts
    
    
    import { createCatalog } from "@copilotkit/a2ui-renderer";import { myDefinitions } from "./definitions";import { myRenderers } from "./renderers";export const myCatalog = createCatalog(myDefinitions, myRenderers, {  catalogId: "declarative-gen-ui-catalog",  includeBasicCatalog: true,});

### Pass the catalog to the provider#

A single prop (`a2ui={{ catalog }}`) is all the frontend needs; the provider registers the catalog and wires up the built-in A2UI activity-message renderer:

page.tsx
    
    
    import React from "react";import { CopilotKit } from "@copilotkit/react-core/v2";import { myCatalog } from "./a2ui/catalog";import { Chat } from "./chat";export default function DeclarativeGenUIDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit-declarative-gen-ui"      agent="declarative-gen-ui"      a2ui={{ catalog: myCatalog }}    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>

That is all the default path needs. The catalog auto-enables A2UI and injects the `generate_a2ui` tool, so the runtime needs no `a2ui` block. (No catalog? Turn it on from the runtime instead with `a2ui: { injectA2UITool: true }`.)

## I opted out of auto-inject, now what?#

By not passing a catalog, not setting `injectA2UITool`, or by passing a catalog and setting `injectA2UITool: false`, you have opted out entirely. That means you hook up two pieces yourself: the `generate_a2ui` tool which lets your agent generate A2UI surfaces, and the `A2UIMiddleware` which lets those surfaces render.

### The `A2UIMiddleware`#

The `A2UIMiddleware` is what turns the agent's `a2ui_operations` into rendered surfaces. Without it, the agent's output never becomes UI; it falls through as a plain tool result. It can also inject the `generate_a2ui` tool for you (`injectA2UITool: true`), letting you skip the next step. Attach it to the AG-UI agent:
    
    
    import { A2UIMiddleware } from "@ag-ui/a2ui-middleware";
    
    agent.use(new A2UIMiddleware({ injectA2UITool: false }));

### The A2UI agent tool#

The `generate_a2ui` tool runs a secondary LLM (a subagent) that designs the surface, which is why you hand it a model. Build it with the AG-UI factory and add it to your agent's tools:

agent.py
    
    
    from ag_ui_langgraph import get_a2ui_tools
    from langchain_openai import ChatOpenAI
    
    generate_a2ui = get_a2ui_tools({
        "model": ChatOpenAI(model="gpt-4o"),
        "default_catalog_id": "copilotkit://app-dashboard-catalog",
    })
    
    tools = [my_other_tool, generate_a2ui]

## Progressive streaming#

The secondary LLM's `render_a2ui` tool call streams through LangGraph as `TOOL_CALL_ARGS` events. The A2UI middleware:

  1. Waits for the full `components` array before emitting anything; the schema must be complete before rendering starts.
  2. Extracts `surfaceId` \+ `root` from the partial JSON.
  3. Emits `createSurface` \+ `updateComponents` once the schema is complete.
  4. Extracts complete `items` objects progressively and emits an `updateDataModel` for each, so cards appear one by one as data streams in.



A built-in progress indicator shows while the schema is still generating and hides automatically once data items start arriving.

## When should I use dynamic schemas?#

  * You don't know the UI shape ahead of time; the agent decides what to show based on the user's request.
  * You want to prototype A2UI without committing to a schema file yet.
  * You're building a conversational dashboard where the layout varies per turn.



If the surface is well-known (e.g. a product card, a flight result), prefer a **[fixed schema](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui/dynamic-schema/fixed-schema)** ; it's faster, cheaper, and the UI is deterministic.

### On this page

How it worksThe 3-file splitDeclare your custom component definitionsImplement the React renderersWire definitions × renderers into a catalogPass the catalog to the providerI opted out of auto-inject, now what?The A2UIMiddlewareThe A2UI agent toolProgressive streamingWhen should I use dynamic schemas?
