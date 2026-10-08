---
url: https://docs.copilotkit.ai/llamaindex/generative-ui/a2ui/fixed-schema/
title: Fixed Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:14:47.331969+00:00
---

# Fixed Schema A2UI

> Source: https://docs.copilotkit.ai/llamaindex/generative-ui/a2ui/fixed-schema/

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

[A2UI](https://docs.copilotkit.ai/llamaindex/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/llamaindex/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/llamaindex/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/llamaindex/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/llamaindex/generative-ui/hashbrown)

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

booked_schema.json

page.tsx

catalog.ts

definitions.ts

renderers.tsx

route.ts
    
    
    """LlamaIndex agent for the A2UI Fixed Schema demo.Mirrors `langgraph-python/src/agents/a2ui_fixed.py`: the component tree (theflight card schema) is authored ahead of time as JSON; the agent only streams*data* into the data model at runtime via a `display_flight` tool. The frontendregisters a matching catalog (see`src/app/demos/a2ui-fixed-schema/a2ui/catalog.ts`) that pins the schema'scomponent names (Card / Title / Airport / …) to real React components.INTEGRATION-LEVEL STREAMED render_a2ui FIX------------------------------------------The A2UI middleware (`@ag-ui/a2ui-middleware`) mounts the surface from aSTREAMED render-tool CALL, NOT from a tool result:  - On `TOOL_CALL_START`: it tracks the call ONLY when `toolCallName` is in its    watched set (populated when `injectA2UITool: true`, watching `render_a2ui`).  - On `TOOL_CALL_ARGS` deltas: it accumulates the args, parses `components` out    of the streamed args, and emits the `a2ui-surface` activity    (`createSurface` / `updateComponents` / `updateDataModel`) once `components`    (and then `data`) are present.A `TOOL_CALL_RESULT` does NOT mount the surface. The upstream llama-index AG-UIadapter only appends backend tool results to chat history and re-emits via`MESSAGES_SNAPSHOT`, which the middleware ignores — so the surface was nevermounted (`reason=surface-missing`). This is the same root cause fixed for thesibling `declarative-gen-ui` (A2UI — Dynamic Schema) demo.We close the gap at the integration level by mirroring how google-adk drivesthe middleware — emitting a streamed `render_a2ui` tool-CALL:  1. `display_flight` (the backend tool) returns the fixed-schema `render_a2ui`     args (`surfaceId` / `catalogId` / `components` / `data`) as JSON. The     `components` array is the pre-authored flight schema; `data` is the runtime     trip the LLM supplied. Nothing is stubbed.  2. The workflow override (`_A2UIRenderToolCallWorkflow`) parses that backend     tool result and writes a discrete streamed `render_a2ui` tool-CALL to the     AG-UI stream: `TOOL_CALL_START` (toolCallName=`render_a2ui`), one or more     `TOOL_CALL_ARGS` deltas carrying the args JSON (whose `components` array and     `data` object the middleware parses), and `TOOL_CALL_END`. The upstream     `MESSAGES_SNAPSHOT` behaviour is preserved (super() body still runs).The streamed `TOOL_CALL_START` / `TOOL_CALL_ARGS` / `TOOL_CALL_END` events arealready in the upstream `AG_UI_EVENTS` allow-list the router streams against, sothey pass through the SSE shim unmodified.Pairs with the dedicated runtime route`src/app/api/copilotkit-a2ui-fixed-schema/route.ts` which sets`a2ui.injectA2UITool: true` so the middleware WATCHES the `render_a2ui`tool-call name (the watched-names set is only populated when the tool isinjected).Both changes live entirely in this integration; no shared/`@ag-ui` package istouched."""import jsonimport osimport uuidfrom pathlib import Pathfrom typing import Annotated, Awaitable, Callable, List, Optional, Unionfrom ag_ui.core import RunAgentInputfrom fastapi import APIRouterfrom fastapi.responses import StreamingResponsefrom llama_index.core.llms import ChatMessagefrom llama_index.core.workflow import Context, Workflow, stepfrom llama_index.core.workflow.events import StopEventfrom llama_index.llms.openai import OpenAIfrom llama_index.protocols.ag_ui.agent import (    AGUIChatWorkflow,    LoopEvent,    ToolCallResultEvent,)from llama_index.protocols.ag_ui.events import (    RunErrorWorkflowEvent,    RunFinishedWorkflowEvent,    RunStartedWorkflowEvent,    ToolCallArgsWorkflowEvent,    ToolCallEndWorkflowEvent,    ToolCallStartWorkflowEvent,)from llama_index.protocols.ag_ui.router import AG_UI_EVENTSfrom llama_index.protocols.ag_ui.utils import timestamp, workflow_event_to_sseCATALOG_ID = "copilotkit://flight-fixed-catalog"SURFACE_ID = "flight-fixed-schema"# The render-tool name `@ag-ui/a2ui-middleware` watches (when# `injectA2UITool: true`) and mounts the surface from. We synthesise a STREAMED# tool-CALL by this name on the outbound stream.RENDER_A2UI_TOOL_NAME = "render_a2ui"# Allow-list the router streams against. The streamed `render_a2ui` tool-CALL# events (TOOL_CALL_START / TOOL_CALL_ARGS / TOOL_CALL_END) are already part of# the upstream `AG_UI_EVENTS` tuple, so no extension is required._A2UI_AG_UI_EVENTS = AG_UI_EVENTS_SCHEMAS_DIR = Path(__file__).parent / "a2ui_schemas"# Schemas are JSON so they can be authored and reviewed independently of the# Python code. `_load_schema` is just a thin `json.load` wrapper.def _load_schema(path: Path) -> list[dict]:    with path.open("r", encoding="utf-8") as fh:        return json.load(fh)FLIGHT_SCHEMA = _load_schema(_SCHEMAS_DIR / "flight_schema.json")def _emit_render_a2ui_tool_call(ctx: Context, args: dict) -> None:    """Write a STREAMED ``render_a2ui`` tool-CALL to the AG-UI stream.    Emits ``TOOL_CALL_START`` (toolCallName=``render_a2ui``), the args JSON as    one or more ``TOOL_CALL_ARGS`` deltas (the middleware parses ``components``    and ``data`` out of the accumulated args), then ``TOOL_CALL_END``. This is    the exact event sequence ``@ag-ui/a2ui-middleware`` watches to mount the    surface.    """    tool_call_id = f"render_a2ui-{uuid.uuid4().hex}"    payload = json.dumps(args)    ctx.write_event_to_stream(        ToolCallStartWorkflowEvent(            tool_call_id=tool_call_id,            tool_call_name=RENDER_A2UI_TOOL_NAME,        )    )    # Chunk the args so the middleware exercises its streaming-args accumulator    # (it parses `components` / `data` from the concatenated deltas).    chunk_size = 256    for start in range(0, len(payload), chunk_size):        ctx.write_event_to_stream(            ToolCallArgsWorkflowEvent(                tool_call_id=tool_call_id,                delta=payload[start : start + chunk_size],            )        )    ctx.write_event_to_stream(ToolCallEndWorkflowEvent(tool_call_id=tool_call_id))class _A2UIRenderToolCallWorkflow(AGUIChatWorkflow):    """Upstream workflow that RE-EMITS each backend `display_flight` result as a    STREAMED ``render_a2ui`` tool-CALL so ``@ag-ui/a2ui-middleware`` mounts the    surface.    Only ``aggregate_tool_calls`` is overridden. The override re-applies    ``@step`` (a plain override drops the method from llama-index's step    registry) and reproduces the upstream body byte-for-byte — preserving the    ``MESSAGES_SNAPSHOT`` history update and the loop/stop control flow — with a    single addition: it parses each backend tool result (the fixed-schema    ``render_a2ui`` args carrying ``components``) and streams a discrete    ``render_a2ui`` tool-CALL. This mirrors how google-adk drives the middleware    without altering any other adapter behaviour.    """    @step    async def aggregate_tool_calls(        self, ctx: Context, ev: ToolCallResultEvent    ) -> Optional[Union[StopEvent, LoopEvent]]:        num_tool_calls = await ctx.store.get("num_tool_calls")        tool_call_results: Optional[List[ToolCallResultEvent]] = ctx.collect_events(            ev, [ToolCallResultEvent] * num_tool_calls        )        if tool_call_results is None:            # Not all sibling tool results have arrived yet.            return None        frontend_tool_calls = [            r for r in tool_call_results if r.tool_name in self.frontend_tools        ]        backend_tool_calls = [            r for r in tool_call_results if r.tool_name in self.backend_tools        ]        # ADDITION: for every backend `display_flight` result, RE-EMIT the        # fixed-schema component args as a STREAMED `render_a2ui` tool-CALL. The        # middleware mounts the surface from this streamed call (it does NOT        # inspect tool results or MESSAGES_SNAPSHOT). Frontend-tool results are        # resolved on the client and must NOT be re-emitted here.        for result in backend_tool_calls:            try:                render_args = json.loads(result.tool_output.content)            except (TypeError, ValueError):                render_args = None            if isinstance(render_args, dict) and render_args.get("components"):                _emit_render_a2ui_tool_call(ctx, render_args)        # --- upstream aggregate_tool_calls body (unchanged) ---        new_tool_messages = [            ChatMessage(                role="tool",                content=r.tool_output.content,                additional_kwargs={"tool_call_id": r.tool_call_id},            )            for r in backend_tool_calls        ]        chat_history = await ctx.store.get("chat_history")        if new_tool_messages:            chat_history.extend(new_tool_messages)            self._snapshot_messages(ctx, [*chat_history])            await ctx.store.set("chat_history", chat_history)        if len(frontend_tool_calls) > 0:            return StopEvent()        return LoopEvent(messages=chat_history)def _make_a2ui_router(    workflow_factory: Callable[[], Awaitable[Workflow]],) -> APIRouter:    """SSE router mirroring upstream ``AGUIWorkflowRouter``.    Upstream ``AGUIWorkflowRouter.run`` filters ``handler.stream_events()``    against a fixed ``AG_UI_EVENTS`` tuple; this shim is functionally identical    (it filters against ``_A2UI_AG_UI_EVENTS``, which equals ``AG_UI_EVENTS``).    The streamed ``render_a2ui`` tool-CALL events the workflow emits    (TOOL_CALL_START / TOOL_CALL_ARGS / TOOL_CALL_END) are already in that    allow-list, so they pass through unmodified.    """    router = APIRouter()    async def run(input: RunAgentInput):        workflow = await workflow_factory()        handler = workflow.run(input_data=input)        async def stream_response():            try:                yield workflow_event_to_sse(                    RunStartedWorkflowEvent(                        timestamp=timestamp(),                        thread_id=input.thread_id,                        run_id=input.run_id,                    )                )                async for stream_ev in handler.stream_events():                    if isinstance(stream_ev, _A2UI_AG_UI_EVENTS):                        yield workflow_event_to_sse(stream_ev)                _ = await handler                yield workflow_event_to_sse(                    RunFinishedWorkflowEvent(                        timestamp=timestamp(),                        thread_id=input.thread_id,                        run_id=input.run_id,                    )                )            except Exception as exc:  # noqa: BLE001 — mirror upstream error path                yield workflow_event_to_sse(                    RunErrorWorkflowEvent(                        timestamp=timestamp(),                        message=str(exc),                        code=str(type(exc)),                    )                )                await handler.cancel_run()                raise        return StreamingResponse(stream_response(), media_type="text/event-stream")    router.add_api_route("/run", run, methods=["POST"])    return routerasync def display_flight(    origin: Annotated[str, "Origin airport code (e.g. 'SFO')."],    destination: Annotated[str, "Destination airport code (e.g. 'JFK')."],    airline: Annotated[str, "Airline name."],    price: Annotated[str, "Price string (e.g. '$289')."],) -> str:    """Show a flight card for the given trip.    Returns the fixed-schema ``render_a2ui`` args (surfaceId, catalogId, the    pre-authored flight ``components``, and the runtime trip ``data``) as JSON.    The workflow override (`_A2UIRenderToolCallWorkflow.aggregate_tool_calls`)    parses this result and RE-EMITS it as a streamed ``render_a2ui`` tool-CALL    that the A2UI middleware watches and mounts the surface from. The frontend    catalog resolves the component names to the local React components.    """    args = {        "surfaceId": SURFACE_ID,        "catalogId": CATALOG_ID,        "components": FLIGHT_SCHEMA,        "data": {            "origin": origin,            "destination": destination,            "airline": airline,            "price": price,        },    }    return json.dumps(args)SYSTEM_PROMPT = (    "You help users find flights. When asked about a flight, call "    "display_flight with origin, destination, airline, and price. "    "Use short airport codes (e.g. 'SFO', 'JFK') and a price string like "    "'$289'. Keep any chat reply to one short sentence.")_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]def _a2ui_fixed_workflow_factory() -> Callable[[], Awaitable[Workflow]]:    async def factory() -> Workflow:        return _A2UIRenderToolCallWorkflow(            llm=OpenAI(model="gpt-5-mini", **_openai_kwargs),            frontend_tools=[],            backend_tools=[display_flight],            system_prompt=SYSTEM_PROMPT,            initial_state={},            timeout=120,        )    return factorya2ui_fixed_router = _make_a2ui_router(_a2ui_fixed_workflow_factory())

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
    
    
    import jsonimport osimport uuidfrom pathlib import Pathfrom typing import Annotated, Awaitable, Callable, List, Optional, Unionfrom ag_ui.core import RunAgentInputfrom fastapi import APIRouterfrom fastapi.responses import StreamingResponsefrom llama_index.core.llms import ChatMessagefrom llama_index.core.workflow import Context, Workflow, stepfrom llama_index.core.workflow.events import StopEventfrom llama_index.llms.openai import OpenAIfrom llama_index.protocols.ag_ui.agent import (    AGUIChatWorkflow,    LoopEvent,    ToolCallResultEvent,)from llama_index.protocols.ag_ui.events import (    RunErrorWorkflowEvent,    RunFinishedWorkflowEvent,    RunStartedWorkflowEvent,    ToolCallArgsWorkflowEvent,    ToolCallEndWorkflowEvent,    ToolCallStartWorkflowEvent,)from llama_index.protocols.ag_ui.router import AG_UI_EVENTSfrom llama_index.protocols.ag_ui.utils import timestamp, workflow_event_to_sseCATALOG_ID = "copilotkit://flight-fixed-catalog"SURFACE_ID = "flight-fixed-schema"# The render-tool name `@ag-ui/a2ui-middleware` watches (when# `injectA2UITool: true`) and mounts the surface from. We synthesise a STREAMED# tool-CALL by this name on the outbound stream.RENDER_A2UI_TOOL_NAME = "render_a2ui"# Allow-list the router streams against. The streamed `render_a2ui` tool-CALL# events (TOOL_CALL_START / TOOL_CALL_ARGS / TOOL_CALL_END) are already part of# the upstream `AG_UI_EVENTS` tuple, so no extension is required._A2UI_AG_UI_EVENTS = AG_UI_EVENTS_SCHEMAS_DIR = Path(__file__).parent / "a2ui_schemas"# Schemas are JSON so they can be authored and reviewed independently of the# Python code. `_load_schema` is just a thin `json.load` wrapper.def _load_schema(path: Path) -> list[dict]:    with path.open("r", encoding="utf-8") as fh:        return json.load(fh)FLIGHT_SCHEMA = _load_schema(_SCHEMAS_DIR / "flight_schema.json")

### Return render operations from the tool#

The agent tool returns an A2UI operations container. The A2UI middleware detects it in the tool result and forwards it to the frontend renderer. The LLM only supplies the four data fields (`origin`, `destination`, `airline`, `price`); the pre-authored schema defines the component tree:

a2ui_fixed.py
    
    
    import jsonimport osimport uuidfrom pathlib import Pathfrom typing import Annotated, Awaitable, Callable, List, Optional, Unionfrom ag_ui.core import RunAgentInputfrom fastapi import APIRouterfrom fastapi.responses import StreamingResponsefrom llama_index.core.llms import ChatMessagefrom llama_index.core.workflow import Context, Workflow, stepfrom llama_index.core.workflow.events import StopEventfrom llama_index.llms.openai import OpenAIfrom llama_index.protocols.ag_ui.agent import (    AGUIChatWorkflow,    LoopEvent,    ToolCallResultEvent,)from llama_index.protocols.ag_ui.events import (    RunErrorWorkflowEvent,    RunFinishedWorkflowEvent,    RunStartedWorkflowEvent,    ToolCallArgsWorkflowEvent,    ToolCallEndWorkflowEvent,    ToolCallStartWorkflowEvent,)from llama_index.protocols.ag_ui.router import AG_UI_EVENTSfrom llama_index.protocols.ag_ui.utils import timestamp, workflow_event_to_sseCATALOG_ID = "copilotkit://flight-fixed-catalog"SURFACE_ID = "flight-fixed-schema"# The render-tool name `@ag-ui/a2ui-middleware` watches (when# `injectA2UITool: true`) and mounts the surface from. We synthesise a STREAMED# tool-CALL by this name on the outbound stream.RENDER_A2UI_TOOL_NAME = "render_a2ui"# Allow-list the router streams against. The streamed `render_a2ui` tool-CALL# events (TOOL_CALL_START / TOOL_CALL_ARGS / TOOL_CALL_END) are already part of# the upstream `AG_UI_EVENTS` tuple, so no extension is required._A2UI_AG_UI_EVENTS = AG_UI_EVENTS_SCHEMAS_DIR = Path(__file__).parent / "a2ui_schemas"# Schemas are JSON so they can be authored and reviewed independently of the# Python code. `_load_schema` is just a thin `json.load` wrapper.def _load_schema(path: Path) -> list[dict]:    with path.open("r", encoding="utf-8") as fh:        return json.load(fh)FLIGHT_SCHEMA = _load_schema(_SCHEMAS_DIR / "flight_schema.json")def _emit_render_a2ui_tool_call(ctx: Context, args: dict) -> None:    """Write a STREAMED ``render_a2ui`` tool-CALL to the AG-UI stream.    Emits ``TOOL_CALL_START`` (toolCallName=``render_a2ui``), the args JSON as    one or more ``TOOL_CALL_ARGS`` deltas (the middleware parses ``components``    and ``data`` out of the accumulated args), then ``TOOL_CALL_END``. This is    the exact event sequence ``@ag-ui/a2ui-middleware`` watches to mount the    surface.    """    tool_call_id = f"render_a2ui-{uuid.uuid4().hex}"    payload = json.dumps(args)    ctx.write_event_to_stream(        ToolCallStartWorkflowEvent(            tool_call_id=tool_call_id,            tool_call_name=RENDER_A2UI_TOOL_NAME,        )    )    # Chunk the args so the middleware exercises its streaming-args accumulator    # (it parses `components` / `data` from the concatenated deltas).    chunk_size = 256    for start in range(0, len(payload), chunk_size):        ctx.write_event_to_stream(            ToolCallArgsWorkflowEvent(                tool_call_id=tool_call_id,                delta=payload[start : start + chunk_size],            )        )    ctx.write_event_to_stream(ToolCallEndWorkflowEvent(tool_call_id=tool_call_id))class _A2UIRenderToolCallWorkflow(AGUIChatWorkflow):    """Upstream workflow that RE-EMITS each backend `display_flight` result as a    STREAMED ``render_a2ui`` tool-CALL so ``@ag-ui/a2ui-middleware`` mounts the    surface.    Only ``aggregate_tool_calls`` is overridden. The override re-applies    ``@step`` (a plain override drops the method from llama-index's step    registry) and reproduces the upstream body byte-for-byte — preserving the    ``MESSAGES_SNAPSHOT`` history update and the loop/stop control flow — with a    single addition: it parses each backend tool result (the fixed-schema    ``render_a2ui`` args carrying ``components``) and streams a discrete    ``render_a2ui`` tool-CALL. This mirrors how google-adk drives the middleware    without altering any other adapter behaviour.    """    @step    async def aggregate_tool_calls(        self, ctx: Context, ev: ToolCallResultEvent    ) -> Optional[Union[StopEvent, LoopEvent]]:        num_tool_calls = await ctx.store.get("num_tool_calls")        tool_call_results: Optional[List[ToolCallResultEvent]] = ctx.collect_events(            ev, [ToolCallResultEvent] * num_tool_calls        )        if tool_call_results is None:            # Not all sibling tool results have arrived yet.            return None        frontend_tool_calls = [            r for r in tool_call_results if r.tool_name in self.frontend_tools        ]        backend_tool_calls = [            r for r in tool_call_results if r.tool_name in self.backend_tools        ]        # ADDITION: for every backend `display_flight` result, RE-EMIT the        # fixed-schema component args as a STREAMED `render_a2ui` tool-CALL. The        # middleware mounts the surface from this streamed call (it does NOT        # inspect tool results or MESSAGES_SNAPSHOT). Frontend-tool results are        # resolved on the client and must NOT be re-emitted here.        for result in backend_tool_calls:            try:                render_args = json.loads(result.tool_output.content)            except (TypeError, ValueError):                render_args = None            if isinstance(render_args, dict) and render_args.get("components"):                _emit_render_a2ui_tool_call(ctx, render_args)        # --- upstream aggregate_tool_calls body (unchanged) ---        new_tool_messages = [            ChatMessage(                role="tool",                content=r.tool_output.content,                additional_kwargs={"tool_call_id": r.tool_call_id},            )            for r in backend_tool_calls        ]        chat_history = await ctx.store.get("chat_history")        if new_tool_messages:            chat_history.extend(new_tool_messages)            self._snapshot_messages(ctx, [*chat_history])            await ctx.store.set("chat_history", chat_history)        if len(frontend_tool_calls) > 0:            return StopEvent()        return LoopEvent(messages=chat_history)def _make_a2ui_router(    workflow_factory: Callable[[], Awaitable[Workflow]],) -> APIRouter:    """SSE router mirroring upstream ``AGUIWorkflowRouter``.    Upstream ``AGUIWorkflowRouter.run`` filters ``handler.stream_events()``    against a fixed ``AG_UI_EVENTS`` tuple; this shim is functionally identical    (it filters against ``_A2UI_AG_UI_EVENTS``, which equals ``AG_UI_EVENTS``).    The streamed ``render_a2ui`` tool-CALL events the workflow emits    (TOOL_CALL_START / TOOL_CALL_ARGS / TOOL_CALL_END) are already in that    allow-list, so they pass through unmodified.    """    router = APIRouter()    async def run(input: RunAgentInput):        workflow = await workflow_factory()        handler = workflow.run(input_data=input)        async def stream_response():            try:                yield workflow_event_to_sse(                    RunStartedWorkflowEvent(                        timestamp=timestamp(),                        thread_id=input.thread_id,                        run_id=input.run_id,                    )                )                async for stream_ev in handler.stream_events():                    if isinstance(stream_ev, _A2UI_AG_UI_EVENTS):                        yield workflow_event_to_sse(stream_ev)                _ = await handler                yield workflow_event_to_sse(                    RunFinishedWorkflowEvent(                        timestamp=timestamp(),                        thread_id=input.thread_id,                        run_id=input.run_id,                    )                )            except Exception as exc:  # noqa: BLE001 — mirror upstream error path                yield workflow_event_to_sse(                    RunErrorWorkflowEvent(                        timestamp=timestamp(),                        message=str(exc),                        code=str(type(exc)),                    )                )                await handler.cancel_run()                raise        return StreamingResponse(stream_response(), media_type="text/event-stream")    router.add_api_route("/run", run, methods=["POST"])    return routerasync def display_flight(    origin: Annotated[str, "Origin airport code (e.g. 'SFO')."],    destination: Annotated[str, "Destination airport code (e.g. 'JFK')."],    airline: Annotated[str, "Airline name."],    price: Annotated[str, "Price string (e.g. '$289')."],) -> str:    """Show a flight card for the given trip.    Returns the fixed-schema ``render_a2ui`` args (surfaceId, catalogId, the    pre-authored flight ``components``, and the runtime trip ``data``) as JSON.    The workflow override (`_A2UIRenderToolCallWorkflow.aggregate_tool_calls`)    parses this result and RE-EMITS it as a streamed ``render_a2ui`` tool-CALL    that the A2UI middleware watches and mounts the surface from. The frontend    catalog resolves the component names to the local React components.    """    args = {        "surfaceId": SURFACE_ID,        "catalogId": CATALOG_ID,        "components": FLIGHT_SCHEMA,        "data": {            "origin": origin,            "destination": destination,            "airline": airline,            "price": price,        },    }    return json.dumps(args)

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



If the UI must adapt per prompt, reach for **[dynamic schemas](https://docs.copilotkit.ai/llamaindex/generative-ui/a2ui/fixed-schema/dynamic-schema)** instead.

### On this page

How it worksCompositional schemasThe 5-component custom catalogInstall the renderer packageDeclare the component definitionsImplement the React renderersWire the catalogLoad the schema JSON at startupReturn render operations from the toolWhy compositional beats monolithicRegistering the runtimeAction handlers (reference)When should I use fixed schemas?
