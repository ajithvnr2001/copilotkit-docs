---
url: https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui/fixed-schema/
title: Fixed Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:20.734369+00:00
---

# Fixed Schema A2UI

> Source: https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui/fixed-schema/

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

Fixed Schema A2UI

Generative UIDeclarativeA2UI

# Fixed Schema A2UI

Pre-defined A2UI schema with dynamic data. The fastest approach, with no LLM schema generation needed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

a2ui_fixed.py

flight_schema.json

page.tsx

catalog.ts

route.ts
    
    
    """Claude Agent SDK backend for the A2UI Fixed Schema demo.The component tree (schema) is authored ahead of time as JSON and shippedwith the backend. The agent only streams *data* into the data model atruntime via the `display_flight` tool, which emits an `a2ui_operations`container the runtime A2UI middleware detects in tool results and forwardsto the frontend renderer.Mirrors the langgraph-python and ag2 references. The dedicated runtimeroute at `api/copilotkit-a2ui-fixed-schema/route.ts` runs with`injectA2UITool: false` because the backend owns the rendering tool."""from __future__ import annotationsimport jsonimport osimport tracebackfrom collections.abc import AsyncIteratorfrom pathlib import Pathfrom textwrap import dedentfrom typing import Anyimport anthropicfrom ag_ui.core import (    EventType,    RunAgentInput,    RunFinishedEvent,    RunStartedEvent,    TextMessageContentEvent,    TextMessageEndEvent,    TextMessageStartEvent,    ToolCallArgsEvent,    ToolCallEndEvent,    ToolCallResultEvent,    ToolCallStartEvent,)from ag_ui.encoder import EventEncoderfrom agents.claude_agent_sdk_adapter import normalize_claude_modelCATALOG_ID = "copilotkit://flight-fixed-catalog"SURFACE_ID = "flight-fixed-schema"_SCHEMAS_DIR = Path(__file__).parent / "a2ui_schemas"def _load_schema(filename: str) -> list[dict]:    with open(_SCHEMAS_DIR / filename, "r", encoding="utf-8") as fh:        return json.load(fh)FLIGHT_SCHEMA = _load_schema("flight_schema.json")SYSTEM_PROMPT = dedent("""    You help users find flights. When asked about a flight, call    `display_flight` with origin (3-letter code), destination (3-letter    code), airline, and price (e.g. '$289'). Keep any chat reply to one    short sentence.""").strip()DISPLAY_FLIGHT_TOOL = {    "name": "display_flight",    "description": (        "Show a flight card for the given trip. Emits an a2ui_operations "        "container the runtime A2UI middleware detects and forwards to the "        "frontend renderer."    ),    "input_schema": {        "type": "object",        "properties": {            "origin": {                "type": "string",                "description": "Origin airport code, e.g. 'SFO'",            },            "destination": {                "type": "string",                "description": "Destination airport code, e.g. 'JFK'",            },            "airline": {"type": "string", "description": "Airline name, e.g. 'United'"},            "price": {"type": "string", "description": "Price string, e.g. '$289'"},        },        "required": ["origin", "destination", "airline", "price"],    },}def _display_flight_operations(    origin: str, destination: str, airline: str, price: str) -> dict[str, Any]:    # A2UI v0.9 message shape — each operation is wrapped in a versioned    # container keyed by the operation name (createSurface, updateComponents,    # updateDataModel). The runtime A2UI middleware + react-core renderer    # (packages/react-core/src/v2/a2ui/A2UIMessageRenderer.tsx) read these    # keys directly; the legacy snake_case `{type: "create_surface", ...}`    # shape is silently dropped, leaving the flight card unrendered.    # Mirrors `copilotkit.a2ui.render(...)` used by langgraph-python's    # display_flight tool (sdk-python/copilotkit/a2ui.py).    return {        "a2ui_operations": [            {                "version": "v0.9",                "createSurface": {                    "surfaceId": SURFACE_ID,                    "catalogId": CATALOG_ID,                },            },            {                "version": "v0.9",                "updateComponents": {                    "surfaceId": SURFACE_ID,                    "components": FLIGHT_SCHEMA,                },            },            {                "version": "v0.9",                "updateDataModel": {                    "surfaceId": SURFACE_ID,                    "path": "/",                    "value": {                        "origin": origin,                        "destination": destination,                        "airline": airline,                        "price": price,                    },                },            },        ]    }async def run_a2ui_fixed_agent(input_data: RunAgentInput) -> AsyncIterator[str]:    """Stream a Claude conversation that may call `display_flight`."""    encoder = EventEncoder()    client = anthropic.AsyncAnthropic(api_key=os.getenv("ANTHROPIC_API_KEY", ""))    messages: list[dict[str, Any]] = []    for msg in input_data.messages or []:        role = msg.role.value if hasattr(msg.role, "value") else str(msg.role)        if role not in ("user", "assistant"):            continue        raw = getattr(msg, "content", None)        content = ""        if isinstance(raw, str):            content = raw        elif isinstance(raw, list):            parts = []            for part in raw:                if hasattr(part, "text"):                    parts.append(part.text)                elif isinstance(part, dict) and "text" in part:                    parts.append(part["text"])            content = "".join(parts)        if content:            messages.append({"role": role, "content": content})    thread_id = input_data.thread_id or "default"    run_id = input_data.run_id or "run-1"    yield encoder.encode(        RunStartedEvent(type=EventType.RUN_STARTED, thread_id=thread_id, run_id=run_id)    )    while True:        msg_id = f"msg-{run_id}-{len(messages)}"        yield encoder.encode(            TextMessageStartEvent(                type=EventType.TEXT_MESSAGE_START,                message_id=msg_id,                role="assistant",            )        )        response_text = ""        tool_calls: list[dict[str, Any]] = []        try:            async with client.messages.stream(                model=normalize_claude_model(                    os.getenv("ANTHROPIC_MODEL", "claude-opus-4-8")                ),                max_tokens=2048,                system=SYSTEM_PROMPT,                messages=messages,                tools=[DISPLAY_FLIGHT_TOOL],            ) as stream:                current_tool_id: str | None = None                current_tool_name: str | None = None                current_tool_args = ""                async for event in stream:                    etype = type(event).__name__                    if etype == "RawContentBlockStartEvent":                        block = event.content_block  # type: ignore[attr-defined]                        if block.type == "tool_use":                            current_tool_id = block.id                            current_tool_name = block.name                            current_tool_args = ""                            yield encoder.encode(                                ToolCallStartEvent(                                    type=EventType.TOOL_CALL_START,                                    tool_call_id=current_tool_id,                                    tool_call_name=current_tool_name,                                    parent_message_id=msg_id,                                )                            )                    elif etype == "RawContentBlockDeltaEvent":                        delta = event.delta  # type: ignore[attr-defined]                        if delta.type == "text_delta":                            response_text += delta.text                            yield encoder.encode(                                TextMessageContentEvent(                                    type=EventType.TEXT_MESSAGE_CONTENT,                                    message_id=msg_id,                                    delta=delta.text,                                )                            )                        elif delta.type == "input_json_delta":                            current_tool_args += delta.partial_json                            yield encoder.encode(                                ToolCallArgsEvent(                                    type=EventType.TOOL_CALL_ARGS,                                    tool_call_id=current_tool_id or "",                                    delta=delta.partial_json,                                )                            )                    elif etype in (                        "RawContentBlockStopEvent",                        "ParsedContentBlockStopEvent",                    ):                        if current_tool_id and current_tool_name:                            yield encoder.encode(                                ToolCallEndEvent(                                    type=EventType.TOOL_CALL_END,                                    tool_call_id=current_tool_id,                                )                            )                            try:                                parsed = (                                    json.loads(current_tool_args)                                    if current_tool_args                                    else {}                                )                            except json.JSONDecodeError:                                parsed = {}                            tool_calls.append(                                {                                    "id": current_tool_id,                                    "name": current_tool_name,                                    "input": parsed,                                }                            )                            current_tool_id = None                            current_tool_name = None                            current_tool_args = ""        except Exception:            err_text = f"Agent error: {traceback.format_exc()}"            yield encoder.encode(                TextMessageContentEvent(                    type=EventType.TEXT_MESSAGE_CONTENT,                    message_id=msg_id,                    delta=err_text,                )            )        yield encoder.encode(            TextMessageEndEvent(                type=EventType.TEXT_MESSAGE_END,                message_id=msg_id,            )        )        if not tool_calls:            break        assistant_content: list[dict[str, Any]] = []        if response_text:            assistant_content.append({"type": "text", "text": response_text})        for tc in tool_calls:            assistant_content.append(                {                    "type": "tool_use",                    "id": tc["id"],                    "name": tc["name"],                    "input": tc["input"],                }            )        messages.append({"role": "assistant", "content": assistant_content})        tool_results: list[dict[str, Any]] = []        for tc in tool_calls:            if tc["name"] == "display_flight":                args = tc["input"]                result_obj = _display_flight_operations(                    origin=args.get("origin", ""),                    destination=args.get("destination", ""),                    airline=args.get("airline", ""),                    price=args.get("price", ""),                )                result_text = json.dumps(result_obj)            else:                result_text = json.dumps({"error": f"unknown tool {tc['name']}"})            yield encoder.encode(                ToolCallResultEvent(                    type=EventType.TOOL_CALL_RESULT,                    tool_call_id=tc["id"],                    message_id=f"{msg_id}-tool-result-{tc['id']}",                    content=result_text,                )            )            tool_results.append(                {                    "type": "tool_result",                    "tool_use_id": tc["id"],                    "content": result_text,                }            )        messages.append({"role": "user", "content": tool_results})    yield encoder.encode(        RunFinishedEvent(            type=EventType.RUN_FINISHED, thread_id=thread_id, run_id=run_id        )    )

In the fixed-schema approach, you design the UI schema once (by hand, or using the [A2UI Composer](https://a2ui-composer.ag-ui.com/)) and keep it on the agent side. The agent tool only provides the _data_ ; the surface appears instantly when the tool returns because nothing has to be generated at runtime.

How the schema is _delivered_ to the runtime is the only thing that varies between integrations:

  * **Schema-loading** (including Strands TypeScript), the schema is saved as a `.json` file next to the agent and loaded once at startup.
  * **Schema-inline** (spring-ai, ms-agent-dotnet), the schema is declared inline as a typed literal in source. The host language doesn't ship a `load_schema` JSON loader, so the structure is compiled in directly.
  * **LLM-driven** (Mastra and Strands Python), the agent runs a secondary LLM call to produce the operations container per-request. The catalog is still fixed; the schema is generated on demand.



Ask about a flight and the agent renders a fully structured card from a pre-defined schema:

The flight card is an illustrative domain

Everything below uses flight booking so the wiring has something concrete to render — `display_flight`, `flight-fixed-catalog`, and the airport/airline components are this page's example, not part of the API.

What transfers is the **shape** : a fixed catalog, a tool that returns data against it, and an operations container with `createSurface` \+ `updateComponents` \+ `updateDataModel`. Keep your own application's domain and substitute your own components and tool — a page teaching the pattern is not a brief to build a flight booker.

## How it works#

  1. The schema is made available to the agent, either loaded from a JSON file at startup, declared inline, or generated per-request, depending on the integration.
  2. The agent's `display_flight` tool receives data from the primary LLM (origin / destination / airline / price).
  3. The tool returns an operations container with `createSurface` \+ `updateComponents` \+ `updateDataModel` operations.
  4. The A2UI middleware intercepts the tool result and the frontend renders the surface using the matching 5-component client catalog (Title, Airport, Arrow, AirlineBadge, PriceTag, plus the built-ins).



## Compositional schemas#

The example below ships a flight card assembled compositionally from small sub-components rather than one monolithic `FlightCard`:
    
    
    Card
     └─ Column
         ├─ Title        ("Flight Details")
         ├─ Row          (Airport → Arrow → Airport)
         ├─ Row          (AirlineBadge · PriceTag)
         └─ Button       (Book)

That tree lives backend-side, as a JSON file, an inline literal, or a per-request LLM output, depending on the integration. Components without data bindings (like `Title` or `Arrow`) carry their value inline; components bound to the LLM's data (like `Airport`) reference fields via JSON Pointer paths such as `{ "path": "/origin" }`. The A2UI binder resolves those paths _before_ the React renderer runs, so your renderer receives the resolved value and never sees the path — but the _definition_ still has to declare that prop as a literal-or-binding union, because that union is the only signal the binder has that the prop is bindable. See Declare the component definitions.

## The 5-component custom catalog#

The frontend catalog declares just the domain-specific primitives (Title, Airport, Arrow, AirlineBadge, PriceTag) and merges in CopilotKit's basic catalog (Card, Column, Row, Text, Button, …) via `includeBasicCatalog: true`.

### Install the renderer package#

The catalog, definitions and renderers below all import from `@copilotkit/a2ui-renderer`. It ships separately from `@copilotkit/react-core`, and the definitions use `zod` for prop schemas:
    
    
    npm install @copilotkit/a2ui-renderer zod

### Declare the component definitions#

Each component declares its props as a Zod schema. Any prop the schema binds to the data model — anything that can arrive as `{ "path": "/origin" }` rather than a literal — **must** be declared as a union of the literal type and the binding object. That is what the `DynString` helper below is for, and why `Airport`'s `code` uses it rather than a plain `z.string()`.

The binder decides whether to resolve a prop by _inspecting its Zod type_ : a union with a `{ path }` member is treated as dynamic and resolved against the data model, while a plain literal type is treated as static and passed through untouched. So declaring a bound prop as `z.string()` does not merely lose type precision — it tells the binder not to resolve it, and the raw `{ path: "/origin" }` object reaches your renderer.

Plain `z.string()` on a bound prop crashes the render

Because the unresolved object reaches the renderer, the first thing that renders it as text throws React's [error #31](https://react.dev/errors/31): `Objects are not valid as a React child (found: object with keys {path})`. Nothing in that message points at the schema, so it reads as a renderer bug rather than a missing union. If you hit it, check the prop's declared type first.

Props that are never bound (`Arrow`, or a `variant` enum) are fine as plain types. This applies only to props the schema binds.

Once the union is declared, the binder resolves the path before your renderer runs, so the renderer still receives a plain string — the union describes what the _schema_ may send, not what the renderer must handle. `@copilotkit/a2ui-renderer` re-exports A2UI's canonical `DynamicStringSchema` (plus `DynamicNumberSchema`, `DynamicBooleanSchema` and the matching types) if you would rather not hand-roll the union:
    
    
    import { DynamicStringSchema } from "@copilotkit/a2ui-renderer";

definitions.ts
    
    
    import { z } from "zod";import type { CatalogDefinitions } from "@copilotkit/a2ui-renderer";/** * Dynamic string: literal OR a data-model path binding. The GenericBinder * resolves path bindings to the actual value at render time. */const DynString = z.union([z.string(), z.object({ path: z.string() })]);export const definitions = {  /**   * Card override: gives the outer flight-card container a ShadCN look   * (rounded-xl, neutral-200 border, soft shadow). The basic catalog's   * Card uses inline styles; overriding here lets the demo's renderer   * adopt the demo's Tailwind aesthetic without touching the schema JSON.   */  Card: {    description: "A container card with a single child.",    props: z.object({      child: z.string(),    }),  },  Title: {    description: "A prominent heading for the flight card.",    props: z.object({      text: DynString,    }),  },  Airport: {    description: "A 3-letter airport code, displayed large.",    props: z.object({      code: DynString,    }),  },  Arrow: {    description: "A right-pointing arrow used between airports.",    props: z.object({}),  },  AirlineBadge: {    description: "A pill-styled airline name tag.",    props: z.object({      name: DynString,    }),  },  PriceTag: {    description: "A stylized price display (e.g. '$289').",    props: z.object({      amount: DynString,    }),  },  /**   * Button override: swaps in an ActionButton renderer that tracks   * its own `done` state so clicking "Book flight" visually updates to   * a "Booked ✓" confirmation. The basic catalog's Button is stateless,   * so without this override the click fires the action but the button   * looks unchanged. Mirrors the pattern in beautiful-chat   * (src/app/demos/beautiful-chat/declarative-generative-ui/renderers.tsx).   */  Button: {    description:      "An interactive button with an action event. Use 'child' with a Text component ID for the label. After click, the button shows a confirmation state.",    props: z.object({      child: z        .string()        .describe(          "The ID of the child component (e.g. a Text component for the label).",        ),      variant: z.enum(["primary", "secondary", "ghost"]).optional(),      // Union with { event } so GenericBinder resolves this as ACTION → callable () => void.      action: z        .union([          z.object({            event: z.object({              name: z.string(),              context: z.record(z.any()).optional(),            }),          }),          z.null(),        ])        .optional(),    }),  },} satisfies CatalogDefinitions;

### Implement the React renderers#

TypeScript enforces that the renderer map's keys and prop shapes match the definitions exactly, so refactors stay safe:

renderers.tsx
    
    
    export const renderers: CatalogRenderers<Definitions> = {  /**   * Card override: ShadCN-style outer container. The basic catalog's Card   * uses inline styles; overriding here keeps the demo's tailwind aesthetic.   * The flight schema renders Card > Column > [Title, Row, …]; the inner   * Column adds the vertical spacing.   */  Card: ({ props, children }) => (    <Card className="w-full max-w-md p-5" data-testid="a2ui-fixed-card">      {props.child ? children(props.child) : null}    </Card>  ),  Title: ({ props }) => (    <div className="flex items-center justify-between">      <div className="space-y-1">        <p className="text-[11px] font-medium uppercase tracking-[0.14em] text-neutral-500">          Itinerary        </p>        <h3 className="text-base font-semibold leading-none tracking-tight text-neutral-900">          {s(props.text)}        </h3>      </div>      <Badge variant="outline" className="font-mono">        1-stop · economy      </Badge>    </div>  ),  Airport: ({ props }) => (    <div className="flex flex-col items-center">      <span className="font-mono text-2xl font-semibold tracking-wider text-neutral-900">        {s(props.code)}      </span>    </div>  ),  Arrow: () => (    <div className="flex flex-1 items-center px-3">      <Separator className="flex-1 bg-neutral-200" />      <svg        width="16"        height="16"        viewBox="0 0 24 24"        fill="none"        stroke="currentColor"        strokeWidth="2"        strokeLinecap="round"        strokeLinejoin="round"        className="mx-1 text-neutral-400"        aria-hidden      >        <line x1="5" y1="12" x2="19" y2="12" />        <polyline points="12 5 19 12 12 19" />      </svg>      <Separator className="flex-1 bg-neutral-200" />    </div>  ),  AirlineBadge: ({ props }) => (    <Badge variant="secondary" className="uppercase tracking-[0.08em]">      {s(props.name)}    </Badge>  ),  PriceTag: ({ props }) => (    <div className="flex items-baseline gap-1">      <span className="text-[11px] font-medium uppercase tracking-[0.14em] text-neutral-500">        Total      </span>      <span className="font-mono text-base font-semibold text-neutral-900">        {s(props.amount)}      </span>    </div>  ),  /**   * Button override: this is a pure-presentation demo, so the button just   * renders its label. The schema declares an `action` for visual fidelity,   * but the click handler is inert until the Python SDK exposes   * `action_handlers=` on `a2ui.render` (see `src/agents/a2ui_fixed.py`).   */  Button: ({ props, children }) => (    <UIButton className="w-full">      {props.child ? children(props.child) : null}    </UIButton>  ),};

### Wire the catalog#

`createCatalog(..., { includeBasicCatalog: true })` merges the custom renderers with CopilotKit's built-ins so the schema can reference `Card`, `Column`, `Row`, `Button` alongside the domain primitives:

catalog.ts
    
    
    import { createCatalog } from "@copilotkit/a2ui-renderer";import { definitions } from "./definitions";import { renderers } from "./renderers";export const CATALOG_ID = "copilotkit://flight-fixed-catalog";export const catalog = createCatalog(definitions, renderers, {  catalogId: CATALOG_ID,  includeBasicCatalog: true,});

### Load the schema JSON at startup#

The integration parses the pre-authored JSON schema once at startup. The agent then reuses that component tree for every tool call:

a2ui_fixed.py
    
    
    _SCHEMAS_DIR = Path(__file__).parent / "a2ui_schemas"def _load_schema(filename: str) -> list[dict]:    with open(_SCHEMAS_DIR / filename, "r", encoding="utf-8") as fh:        return json.load(fh)FLIGHT_SCHEMA = _load_schema("flight_schema.json")

### Return render operations from the tool#

The agent tool returns an A2UI operations container. The A2UI middleware detects it in the tool result and forwards it to the frontend renderer. The LLM only supplies the four data fields (`origin`, `destination`, `airline`, `price`); the pre-authored schema defines the component tree:

a2ui_fixed.py
    
    
    _SCHEMAS_DIR = Path(__file__).parent / "a2ui_schemas"def _load_schema(filename: str) -> list[dict]:    with open(_SCHEMAS_DIR / filename, "r", encoding="utf-8") as fh:        return json.load(fh)FLIGHT_SCHEMA = _load_schema("flight_schema.json")SYSTEM_PROMPT = dedent("""    You help users find flights. When asked about a flight, call    `display_flight` with origin (3-letter code), destination (3-letter    code), airline, and price (e.g. '$289'). Keep any chat reply to one    short sentence.""").strip()DISPLAY_FLIGHT_TOOL = {    "name": "display_flight",    "description": (        "Show a flight card for the given trip. Emits an a2ui_operations "        "container the runtime A2UI middleware detects and forwards to the "        "frontend renderer."    ),    "input_schema": {        "type": "object",        "properties": {            "origin": {                "type": "string",                "description": "Origin airport code, e.g. 'SFO'",            },            "destination": {                "type": "string",                "description": "Destination airport code, e.g. 'JFK'",            },            "airline": {"type": "string", "description": "Airline name, e.g. 'United'"},            "price": {"type": "string", "description": "Price string, e.g. '$289'"},        },        "required": ["origin", "destination", "airline", "price"],    },}def _display_flight_operations(    origin: str, destination: str, airline: str, price: str) -> dict[str, Any]:    # A2UI v0.9 message shape — each operation is wrapped in a versioned    # container keyed by the operation name (createSurface, updateComponents,    # updateDataModel). The runtime A2UI middleware + react-core renderer    # (packages/react-core/src/v2/a2ui/A2UIMessageRenderer.tsx) read these    # keys directly; the legacy snake_case `{type: "create_surface", ...}`    # shape is silently dropped, leaving the flight card unrendered.    # Mirrors `copilotkit.a2ui.render(...)` used by langgraph-python's    # display_flight tool (sdk-python/copilotkit/a2ui.py).    return {        "a2ui_operations": [            {                "version": "v0.9",                "createSurface": {                    "surfaceId": SURFACE_ID,                    "catalogId": CATALOG_ID,                },            },            {                "version": "v0.9",                "updateComponents": {                    "surfaceId": SURFACE_ID,                    "components": FLIGHT_SCHEMA,                },            },            {                "version": "v0.9",                "updateDataModel": {                    "surfaceId": SURFACE_ID,                    "path": "/",                    "value": {                        "origin": origin,                        "destination": destination,                        "airline": airline,                        "price": price,                    },                },            },        ]    }

Nothing about A2UI depends on how the agent itself is built — the operations container is just the tool's return value, so the tool drops into whatever agent you already have.

## Why compositional beats monolithic#

A single big `FlightCard` component would be faster to write but would lock the design in place. Assembling the card from Card / Column / Row / Title / Airport / Arrow / AirlineBadge / PriceTag gives you:

  * **Reusable primitives** the same `Airport` renderer works in search results, booking confirmations, and future seat maps.
  * **Schema-level design iteration** re-arranging rows or swapping a badge requires only a JSON edit; the renderer code is untouched.
  * **A2UI Composer compatibility** hand-written and Composer-built schemas share the same primitive vocabulary.



## Registering the runtime#

Your agent owns the tool in the fixed-schema approach, so you do not want the runtime to inject its own. Enable A2UI but turn injection off.

Passing a catalog on the provider is enough to enable A2UI:

app/page.tsx
    
    
    <CopilotKit runtimeUrl="/api/copilotkit" a2ui={{ catalog: myCatalog }}>
      {children}
    </CopilotKit>

Because a catalog auto-injects the A2UI tool by default, set `injectA2UITool: false` on the runtime so your agent's own tool is the only one in play. The middleware still auto-detects the operations the tool returns and renders the surface, with no subagent involved:

app/api/copilotkit/route.ts
    
    
    const runtime = new CopilotRuntime({
      agents: { "a2ui-fixed-schema": agent },
      a2ui: { injectA2UITool: false, agents: ["a2ui-fixed-schema"] },
    });

## Action handlers (reference)#

The canonical reference pairs fixed schemas with `action_handlers={...}` to declare optimistic UI swaps (e.g. replacing the flight schema with `BOOKED_SCHEMA` when the user clicks "Book"). The Python SDK's `a2ui.render` does not yet accept `action_handlers`, so the cell omits them; the `booked_schema.json` sibling is retained so the swap can be wired up the moment the SDK exposes the handler kwarg.

When available, a button declares its action like this:
    
    
    {
      "Button": {
        "label": "Book",
        "action": {
          "name": "book_flight",
          "context": [
            { "key": "flightNumber", "value": { "path": "/flightNumber" } },
            { "key": "price", "value": { "path": "/price" } }
          ]
        }
      }
    }

And the Python tool matches it with a handler keyed by the action name (plus a `"*"` catch-all). Until the SDK lands, handle the click on the frontend instead — see [Advanced — Action Handlers](https://docs.copilotkit.ai/integrations/langgraph/generative-ui/a2ui/advanced#action-handlers) for the `createA2UIMessageRenderer` / `onAction` pattern.

## When should I use fixed schemas?#

  * The surface is well-known: flight cards, product tiles, order summaries, dashboards.
  * You want deterministic, designer-controlled UI. No LLM schema drift.
  * You want the fastest possible first paint; no secondary LLM call.



If the UI must adapt per prompt, reach for **[dynamic schemas](https://docs.copilotkit.ai/claude-sdk-python/generative-ui/a2ui/fixed-schema/dynamic-schema)** instead.

### On this page

How it worksCompositional schemasThe 5-component custom catalogInstall the renderer packageDeclare the component definitionsImplement the React renderersWire the catalogLoad the schema JSON at startupReturn render operations from the toolWhy compositional beats monolithicRegistering the runtimeAction handlers (reference)When should I use fixed schemas?
