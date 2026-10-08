---
url: https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui/fixed-schema/
title: Fixed Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:29:40.450546+00:00
---

# Fixed Schema A2UI

> Source: https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui/fixed-schema/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands-typescript)[Quickstart](https://docs.copilotkit.ai/strands-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/strands-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands-typescript/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/strands-typescript/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/strands-typescript/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands-typescript/webmcp)

Agent capabilities

AWS Strands (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/strands-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands-typescript/learning)

[User Memories](https://docs.copilotkit.ai/strands-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/strands-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands-typescript/community-frameworks)

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

agent.ts

page.tsx

catalog.ts

definitions.ts

renderers.tsx

route.ts
    
    
    /** * Agent factories for the Strands TypeScript showcase backend. * * `buildShowcaseAgent` is the single shared agent that serves the vast * majority of demos (the frontend differentiates each demo via * useFrontendTool / useRenderTool / useHumanInTheLoop / useAgentContext). * It mirrors the Python sibling's `build_showcase_agent` minus A2UI. * * The tool-free specialized agents (voice, byoc-hashbrown, byoc-json-render) * are mounted on dedicated sub-paths by `server.ts`. */import { readFileSync } from "node:fs";import { dirname, join } from "node:path";import { fileURLToPath } from "node:url";import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import type { RunAgentInput } from "@ag-ui/core";import { StrandsAgent } from "@ag-ui/aws-strands";import type { StrandsAgentConfig } from "@ag-ui/aws-strands";import {  A2UI_OPERATIONS_KEY,  createSurface,  updateComponents,  updateDataModel,} from "@ag-ui/a2ui-toolkit";import { createModel } from "./model-factory";import { SHOWCASE_TOOLS } from "./tools";import {  withStateContext,  salesStateFromArgs,  notesStateFromArgs,  stepsStateFromArgs,  documentStateFromArgs,  makeSubagentStateFromResult,} from "./state";import {  SYSTEM_PROMPT,  VOICE_SYSTEM_PROMPT,  BYOC_HASHBROWN_SYSTEM_PROMPT,  BYOC_JSON_RENDER_SYSTEM_PROMPT,} from "./prompts";export class ShowcaseStrandsAgent extends StrandsAgent {  override async *run(inputData: RunAgentInput) {    // The adapter exposes context during model calls and restores history afterward.    yield* super.run(withStateContext(inputData));  }}export async function buildShowcaseAgent(): Promise<StrandsAgent> {  const config: StrandsAgentConfig = {    toolBehaviors: {      // The tool keeps the sales pipeline in appState; this snapshot, built      // from the args, only carries it to the UI.      manage_sales_todos: {        skipMessagesSnapshot: true,        stateFromArgs: salesStateFromArgs,      },      // Shared State (Read + Write) — notes panel.      set_notes: { stateFromArgs: notesStateFromArgs },      // gen-ui-agent — live progress card driven by set_steps transitions.      set_steps: { stateFromArgs: stepsStateFromArgs },      // shared-state-streaming — stream the document string into state.      write_document: { stateFromArgs: documentStateFromArgs },      // Sub-agents — append a delegation entry carrying the actual output.      research_agent: {        stateFromResult: makeSubagentStateFromResult("research_agent"),      },      writing_agent: {        stateFromResult: makeSubagentStateFromResult("writing_agent"),      },      critique_agent: {        stateFromResult: makeSubagentStateFromResult("critique_agent"),      },    },  };  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: SYSTEM_PROMPT,    tools: SHOWCASE_TOOLS,  });  return new ShowcaseStrandsAgent({    agent: strandsAgent,    name: "strands_agent",    description:      "A polished CopilotKit demo assistant: chat, tools, shared state, HITL, sub-agents.",    config,  });}/** Tool-free agent for the voice demo (transcription + basic chat). */export async function buildVoiceAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: VOICE_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "voice_agent",    description: "Simple assistant for the voice demo — no tools.",  });}/** Tool-free hashbrown UI-kit envelope generator (declarative-hashbrown). */export async function buildByocHashbrownAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: BYOC_HASHBROWN_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "byoc_hashbrown",    description:      "Hashbrown UI-kit envelope generator for the declarative-hashbrown demo.",  });}/** Tool-free json-render flat-spec generator (declarative-json-render). */export async function buildByocJsonRenderAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: BYOC_JSON_RENDER_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "byoc_json_render",    description:      "json-render flat-spec generator for the declarative-json-render demo.",  });}// ---------------------------------------------------------------------------// A2UI Fixed Schema (declarative-generative-ui) — dedicated backend tool.// ---------------------------------------------------------------------------//// Unlike the dynamic A2UI demo (which relies on the adapter auto-injecting a// `generate_a2ui` tool to *generate* a surface), the fixed-schema demo wires a// single plain backend tool — `display_flight` — that returns the// `a2ui_operations` envelope (createSurface -> updateComponents ->// updateDataModel). The component tree is fixed and authored ahead of time// (./a2ui_schemas/flight_schema.json); only the *data* changes per call. The// runtime A2UIMiddleware detects the envelope in the tool result and paints.// No sub-agent, no generation, no `generate_a2ui` injection.//// The schema's component names + data paths must match the showcase frontend// catalog at src/app/demos/a2ui-fixed-schema/a2ui/{definitions,renderers,// catalog}.ts — catalog id `copilotkit://flight-fixed-catalog`. This mirrors// the canonical langgraph-python demo (src/agents/a2ui_fixed.py).const _A2UI_DIR = dirname(fileURLToPath(import.meta.url));const A2UI_FIXED_CATALOG_ID = "copilotkit://flight-fixed-catalog";const A2UI_FIXED_SURFACE_ID = "flight-fixed-schema";// Fixed, pre-authored component layout. Loaded from JSON so it can be authored// and reviewed independently of the agent code.const FLIGHT_SCHEMA: Array<Record<string, unknown>> = JSON.parse(  readFileSync(join(_A2UI_DIR, "a2ui_schemas", "flight_schema.json"), "utf-8"),);const A2UI_FIXED_SYSTEM_PROMPT =  "You help users find flights. When asked about a flight, call " +  "`display_flight` exactly ONCE with origin, destination, airline, and " +  'price. Use short airport codes (e.g. "SFO", "JFK") for ' +  'origin/destination and a price string like "$289". The tool\'s return ' +  "value is an A2UI surface descriptor — the flight card is already rendered " +  "to the user; do NOT call `display_flight` again for the same trip and do " +  "NOT repeat the flight details in text. After the tool returns, reply with " +  "one short confirmation sentence and stop.";/** * Dedicated agent for the A2UI fixed-schema demo. Returns the envelope as a * plain OBJECT (not a JSON string): the Strands TS SDK wraps an object * tool-return in a `json` content block the adapter reads and re-stringifies * into the TOOL_CALL_RESULT the client A2UIMiddleware scans for * `a2ui_operations`. (A bare string return lands in no content block and the * result comes through empty — unlike the Python SDK, which wraps strings.) */export async function buildA2uiFixedSchemaAgent(): Promise<StrandsAgent> {  const displayFlight = tool({    name: "display_flight",    description:      "Show a flight card for the given trip. Use short airport codes " +      '(e.g. "SFO", "JFK") for origin/destination and a price string like ' +      '"$289". After this tool returns, the flight card is already rendered ' +      "to the user via the A2UI surface — do NOT call it again for the same " +      "flight; reply with one short confirmation sentence and stop.",    inputSchema: z.object({      origin: z.string().describe('Origin airport code, e.g. "SFO".'),      destination: z.string().describe('Destination airport code, e.g. "JFK".'),      airline: z.string().describe('Airline name, e.g. "United".'),      price: z.string().describe('Price string, e.g. "$289".'),    }),    callback: ({ origin, destination, airline, price }) => ({      [A2UI_OPERATIONS_KEY]: [        createSurface(A2UI_FIXED_SURFACE_ID, A2UI_FIXED_CATALOG_ID),        updateComponents(A2UI_FIXED_SURFACE_ID, FLIGHT_SCHEMA),        updateDataModel(A2UI_FIXED_SURFACE_ID, {          origin,          destination,          airline,          price,        }),      ],    }),  });  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_FIXED_SYSTEM_PROMPT,    tools: [displayFlight],  });  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_fixed_schema",    description:      "A2UI surface from a fixed, pre-authored schema (direct backend tool)",  });}// ---------------------------------------------------------------------------// A2UI Dynamic Schema (declarative-gen-ui) — adapter auto-injects generate_a2ui.// ---------------------------------------------------------------------------//// Unlike the fixed-schema demo (which wires a `display_flight` tool returning a// pre-authored envelope), the dynamic demo lets the agent *generate* the// surface layout on the fly. The Next.js route// (app/api/copilotkit-declarative-gen-ui/route.ts) sets// `a2ui: { injectA2UITool: true, defaultCatalogId: "declarative-gen-ui-catalog" }`;// the runtime forwards the flag, the Strands adapter auto-injects a// `generate_a2ui` tool and drives a secondary render planner. The// `config.a2ui` block below supplies the catalog id stamped into generated// surfaces and the composition guide that teaches the planner the page's// catalog. Mirrors the ag-ui dynamic-schema reference example.//// The compositionGuide MUST describe the catalog the page registers at// src/app/demos/declarative-gen-ui/a2ui/{definitions,renderers,catalog}.ts// (catalog id `declarative-gen-ui-catalog`): Card / StatusBadge / Metric /// InfoRow / PrimaryButton / PieChart / BarChart / DataTable, composed inside// the basic catalog's Row / Column / Text (`includeBasicCatalog: true`).//// Grounding dataset + composition rules are kept in spirit with the frontend// `sales-context.ts` (SALES_DATASET + COMPOSITION_RULES) the page registers via// `useAgentContext`. The frontend context steers the PRIMARY agent; this// compositionGuide is the channel the adapter feeds to the secondary// `render_a2ui` planner (it gets `guidelines`, not the frontend App Context),// so the planner is self-contained.const A2UI_DYNAMIC_CATALOG_ID = "declarative-gen-ui-catalog";const A2UI_DYNAMIC_SALES_DATASET = `Vantage Threads (fictional B2B apparel company) — Q2 sales data. Ground every visual in these numbers; invent only plausible details consistent with them.- Quarterly revenue: $4.2M (up 12% QoQ). New customers: 186 (up 8%). Win rate: 31% (down 2pts). Avg deal size: $22.6k (up 5%).- Revenue by region: North America $1.9M, EMEA $1.3M, APAC $720k, LATAM $280k.- Monthly revenue: Jan $1.21M, Feb $1.34M, Mar $1.65M, Apr $1.38M, May $1.42M, Jun $1.40M.- Reps (vs quota): Dana Whitfield 124%, Marcus Lee 108%, Priya Sharma 97%, Tom Okafor 88%, Elena Vasquez 71%.- At-risk: total $615k ARR across 3 accounts — Northwind Retail ($340k renewal, no contact 6 weeks; severity high), Cascadia Outfitters ($180k, champion left; severity medium), Atlas Goods ($95k, stalled legal review; severity medium).- Biggest account: Meridian Apparel Group — owner Dana Whitfield, region North America, ARR $612k, renewal Sep 30, last contact 3 days ago, health green, 4 open opportunities worth $210k.- Meridian revenue by product line: Outerwear $260k, Footwear $180k, Accessories $112k, Custom $60k.`;const A2UI_DYNAMIC_COMPOSITION_RULES = `Use ONLY these exact component names (the registered catalog — any other name fails to render): Card, Column, Row, Text, Metric, PieChart, BarChart, DataTable, StatusBadge, InfoRow, PrimaryButton. The single-value KPI tile component is named exactly "Metric" (NOT "MetricTile" or "MetricCard").Pick A2UI components by the shape of the question — never ask which chart the user wants:1. Overall snapshot / "sales dashboard" → a Column (gap 16) whose first child is a Row (gap 16) of 4 Metric components (each with trend + trendValue), followed by a Row with a PieChart (revenue by region) next to a BarChart (monthly revenue, all six months Jan-Jun). Do NOT wrap the dashboard in a surrounding Card — the charts carry their own card chrome. Do NOT use StatusBadge, DataTable, or InfoRow here.2. Rep / team performance → a Column (gap 16) with a Card containing a DataTable (columns: rep, attainment, pipeline) next to or above a BarChart of quota attainment % per rep — no StatusBadge or InfoRow.3. Risk / health checks → a Column (gap 16): first a Row (gap 16) of 3 Metric components (ARR at risk $615k trend down, accounts at risk 3, biggest exposure Northwind $340k), then a Row (gap 16) with one compact Card per at-risk account (title = account name, subtitle = ARR at stake) containing a StatusBadge (error for high severity, warning otherwise) above a one-line Text with the reason and the recommended next action — no DataTable or InfoRow.4. Single account/entity details → a Row (gap 16) with a Card of InfoRow facts (owner, region, ARR, renewal date, last contact) next to a PieChart of that account's revenue by product line — no DataTable or StatusBadge.5. Part-of-whole follow-ups → PieChart; trends or comparisons over time/categories → BarChart.Compose generously — a dashboard should feel like a real analytics product, not a single widget.`;const A2UI_DYNAMIC_COMPOSITION_GUIDE = `${A2UI_DYNAMIC_SALES_DATASET}\n\n${A2UI_DYNAMIC_COMPOSITION_RULES}`;// Mirrors the langgraph-python demo's a2ui_dynamic.py SYSTEM_PROMPT.const A2UI_DYNAMIC_SYSTEM_PROMPT =  "You are the embedded sales analyst for Vantage Threads, the fictional " +  "B2B apparel company described in your App Context. Answer every " +  "business question by calling `generate_a2ui` to draw a rich visual " +  "surface, and keep the chat reply to one short sentence.\n\n" +  "Ground every number in the sales dataset from App Context — never " +  "invent figures that contradict it. Follow the dashboard composition " +  "rules from App Context when choosing components: pick the component " +  "by the shape of the question (snapshot → composed KPI dashboard with " +  "charts; team performance → table; risk → status badges; single " +  "account → info rows; part-of-whole → pie; trend/comparison → bar). " +  "Never ask the user which chart they want. `generate_a2ui` takes no " +  "arguments and handles the rendering automatically. Compose " +  "generously — a dashboard should feel like a real analytics product, " +  "not a single widget.";/** * Dedicated agent for the A2UI dynamic-schema demo. Wires NO `generate_a2ui` * tool — the runtime's `injectA2UITool: true` makes the adapter auto-inject it * and drive a secondary render planner to GENERATE the surface. */export async function buildA2uiDynamicAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_DYNAMIC_SYSTEM_PROMPT,  });  const config: StrandsAgentConfig = {    a2ui: {      defaultCatalogId: A2UI_DYNAMIC_CATALOG_ID,      guidelines: { compositionGuide: A2UI_DYNAMIC_COMPOSITION_GUIDE },    },  };  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_dynamic_schema",    description:      "Dynamic A2UI surfaces generated on the fly (auto-injected tool)",    config,  });}// ---------------------------------------------------------------------------// A2UI Error Recovery (a2ui-recovery) — adapter auto-injects + runs recovery.// ---------------------------------------------------------------------------//// Same auto-injected dynamic-schema setup as buildA2uiDynamicAgent, but the// aimock fixtures force the inner render_a2ui to emit free-form/sloppy args// (heal pill) or a structurally-invalid surface on every attempt (exhaust// pill). The Strands adapter runs the toolkit validate->retry recovery loop on// its auto-inject path (default 3 attempts) and returns the// a2ui_recovery_exhausted hard-fail envelope when the cap is hit — so this// agent wires NO tool, unlike the langgraph/ADK siblings (which own the tool// explicitly via getA2UITools + injectA2UITool:false). Mirrors the ag-ui dojo// aws-strands recovery example./** * Dedicated agent for the A2UI error-recovery demo. Wires NO `generate_a2ui` * tool — the runtime's `injectA2UITool: true` makes the adapter auto-inject it, * drive the secondary render planner, and run the recovery loop. */export async function buildA2uiRecoveryAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_DYNAMIC_SYSTEM_PROMPT,  });  const config: StrandsAgentConfig = {    a2ui: {      defaultCatalogId: A2UI_DYNAMIC_CATALOG_ID,      guidelines: { compositionGuide: A2UI_DYNAMIC_COMPOSITION_GUIDE },    },  };  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_recovery",    description:      "Dynamic A2UI with automatic error recovery (auto-injected tool)",    config,  });}

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

agent.ts
    
    
    const _A2UI_DIR = dirname(fileURLToPath(import.meta.url));const A2UI_FIXED_CATALOG_ID = "copilotkit://flight-fixed-catalog";const A2UI_FIXED_SURFACE_ID = "flight-fixed-schema";// Fixed, pre-authored component layout. Loaded from JSON so it can be authored// and reviewed independently of the agent code.const FLIGHT_SCHEMA: Array<Record<string, unknown>> = JSON.parse(  readFileSync(join(_A2UI_DIR, "a2ui_schemas", "flight_schema.json"), "utf-8"),);

### Return render operations from the tool#

The agent tool returns an A2UI operations container. The A2UI middleware detects it in the tool result and forwards it to the frontend renderer. The LLM only supplies the four data fields (`origin`, `destination`, `airline`, `price`); the pre-authored schema defines the component tree:

agent.ts
    
    
      const displayFlight = tool({    name: "display_flight",    description:      "Show a flight card for the given trip. Use short airport codes " +      '(e.g. "SFO", "JFK") for origin/destination and a price string like ' +      '"$289". After this tool returns, the flight card is already rendered ' +      "to the user via the A2UI surface — do NOT call it again for the same " +      "flight; reply with one short confirmation sentence and stop.",    inputSchema: z.object({      origin: z.string().describe('Origin airport code, e.g. "SFO".'),      destination: z.string().describe('Destination airport code, e.g. "JFK".'),      airline: z.string().describe('Airline name, e.g. "United".'),      price: z.string().describe('Price string, e.g. "$289".'),    }),    callback: ({ origin, destination, airline, price }) => ({      [A2UI_OPERATIONS_KEY]: [        createSurface(A2UI_FIXED_SURFACE_ID, A2UI_FIXED_CATALOG_ID),        updateComponents(A2UI_FIXED_SURFACE_ID, FLIGHT_SCHEMA),        updateDataModel(A2UI_FIXED_SURFACE_ID, {          origin,          destination,          airline,          price,        }),      ],    }),  });

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



If the UI must adapt per prompt, reach for **[dynamic schemas](https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui/fixed-schema/dynamic-schema)** instead.

### On this page

How it worksCompositional schemasThe 5-component custom catalogInstall the renderer packageDeclare the component definitionsImplement the React renderersWire the catalogLoad the schema JSON at startupReturn render operations from the toolWhy compositional beats monolithicRegistering the runtimeAction handlers (reference)When should I use fixed schemas?
