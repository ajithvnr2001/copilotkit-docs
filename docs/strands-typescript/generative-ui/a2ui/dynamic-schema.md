---
url: https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui/dynamic-schema/
title: Dynamic Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:29:40.263138+00:00
---

# Dynamic Schema A2UI

> Source: https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui/dynamic-schema/

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

Dynamic Schema A2UI

Generative UIDeclarativeA2UI

# Dynamic Schema A2UI

LLM-generated A2UI. A secondary LLM creates both the schema and data from any prompt.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.ts

page.tsx

catalog.ts

route.ts
    
    
    /** * Agent factories for the Strands TypeScript showcase backend. * * `buildShowcaseAgent` is the single shared agent that serves the vast * majority of demos (the frontend differentiates each demo via * useFrontendTool / useRenderTool / useHumanInTheLoop / useAgentContext). * It mirrors the Python sibling's `build_showcase_agent` minus A2UI. * * The tool-free specialized agents (voice, byoc-hashbrown, byoc-json-render) * are mounted on dedicated sub-paths by `server.ts`. */import { readFileSync } from "node:fs";import { dirname, join } from "node:path";import { fileURLToPath } from "node:url";import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import type { RunAgentInput } from "@ag-ui/core";import { StrandsAgent } from "@ag-ui/aws-strands";import type { StrandsAgentConfig } from "@ag-ui/aws-strands";import {  A2UI_OPERATIONS_KEY,  createSurface,  updateComponents,  updateDataModel,} from "@ag-ui/a2ui-toolkit";import { createModel } from "./model-factory";import { SHOWCASE_TOOLS } from "./tools";import {  withStateContext,  salesStateFromArgs,  notesStateFromArgs,  stepsStateFromArgs,  documentStateFromArgs,  makeSubagentStateFromResult,} from "./state";import {  SYSTEM_PROMPT,  VOICE_SYSTEM_PROMPT,  BYOC_HASHBROWN_SYSTEM_PROMPT,  BYOC_JSON_RENDER_SYSTEM_PROMPT,} from "./prompts";export class ShowcaseStrandsAgent extends StrandsAgent {  override async *run(inputData: RunAgentInput) {    // The adapter exposes context during model calls and restores history afterward.    yield* super.run(withStateContext(inputData));  }}export async function buildShowcaseAgent(): Promise<StrandsAgent> {  const config: StrandsAgentConfig = {    toolBehaviors: {      // The tool keeps the sales pipeline in appState; this snapshot, built      // from the args, only carries it to the UI.      manage_sales_todos: {        skipMessagesSnapshot: true,        stateFromArgs: salesStateFromArgs,      },      // Shared State (Read + Write) — notes panel.      set_notes: { stateFromArgs: notesStateFromArgs },      // gen-ui-agent — live progress card driven by set_steps transitions.      set_steps: { stateFromArgs: stepsStateFromArgs },      // shared-state-streaming — stream the document string into state.      write_document: { stateFromArgs: documentStateFromArgs },      // Sub-agents — append a delegation entry carrying the actual output.      research_agent: {        stateFromResult: makeSubagentStateFromResult("research_agent"),      },      writing_agent: {        stateFromResult: makeSubagentStateFromResult("writing_agent"),      },      critique_agent: {        stateFromResult: makeSubagentStateFromResult("critique_agent"),      },    },  };  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: SYSTEM_PROMPT,    tools: SHOWCASE_TOOLS,  });  return new ShowcaseStrandsAgent({    agent: strandsAgent,    name: "strands_agent",    description:      "A polished CopilotKit demo assistant: chat, tools, shared state, HITL, sub-agents.",    config,  });}/** Tool-free agent for the voice demo (transcription + basic chat). */export async function buildVoiceAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: VOICE_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "voice_agent",    description: "Simple assistant for the voice demo — no tools.",  });}/** Tool-free hashbrown UI-kit envelope generator (declarative-hashbrown). */export async function buildByocHashbrownAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: BYOC_HASHBROWN_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "byoc_hashbrown",    description:      "Hashbrown UI-kit envelope generator for the declarative-hashbrown demo.",  });}/** Tool-free json-render flat-spec generator (declarative-json-render). */export async function buildByocJsonRenderAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: BYOC_JSON_RENDER_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "byoc_json_render",    description:      "json-render flat-spec generator for the declarative-json-render demo.",  });}// ---------------------------------------------------------------------------// A2UI Fixed Schema (declarative-generative-ui) — dedicated backend tool.// ---------------------------------------------------------------------------//// Unlike the dynamic A2UI demo (which relies on the adapter auto-injecting a// `generate_a2ui` tool to *generate* a surface), the fixed-schema demo wires a// single plain backend tool — `display_flight` — that returns the// `a2ui_operations` envelope (createSurface -> updateComponents ->// updateDataModel). The component tree is fixed and authored ahead of time// (./a2ui_schemas/flight_schema.json); only the *data* changes per call. The// runtime A2UIMiddleware detects the envelope in the tool result and paints.// No sub-agent, no generation, no `generate_a2ui` injection.//// The schema's component names + data paths must match the showcase frontend// catalog at src/app/demos/a2ui-fixed-schema/a2ui/{definitions,renderers,// catalog}.ts — catalog id `copilotkit://flight-fixed-catalog`. This mirrors// the canonical langgraph-python demo (src/agents/a2ui_fixed.py).const _A2UI_DIR = dirname(fileURLToPath(import.meta.url));const A2UI_FIXED_CATALOG_ID = "copilotkit://flight-fixed-catalog";const A2UI_FIXED_SURFACE_ID = "flight-fixed-schema";// Fixed, pre-authored component layout. Loaded from JSON so it can be authored// and reviewed independently of the agent code.const FLIGHT_SCHEMA: Array<Record<string, unknown>> = JSON.parse(  readFileSync(join(_A2UI_DIR, "a2ui_schemas", "flight_schema.json"), "utf-8"),);const A2UI_FIXED_SYSTEM_PROMPT =  "You help users find flights. When asked about a flight, call " +  "`display_flight` exactly ONCE with origin, destination, airline, and " +  'price. Use short airport codes (e.g. "SFO", "JFK") for ' +  'origin/destination and a price string like "$289". The tool\'s return ' +  "value is an A2UI surface descriptor — the flight card is already rendered " +  "to the user; do NOT call `display_flight` again for the same trip and do " +  "NOT repeat the flight details in text. After the tool returns, reply with " +  "one short confirmation sentence and stop.";/** * Dedicated agent for the A2UI fixed-schema demo. Returns the envelope as a * plain OBJECT (not a JSON string): the Strands TS SDK wraps an object * tool-return in a `json` content block the adapter reads and re-stringifies * into the TOOL_CALL_RESULT the client A2UIMiddleware scans for * `a2ui_operations`. (A bare string return lands in no content block and the * result comes through empty — unlike the Python SDK, which wraps strings.) */export async function buildA2uiFixedSchemaAgent(): Promise<StrandsAgent> {  const displayFlight = tool({    name: "display_flight",    description:      "Show a flight card for the given trip. Use short airport codes " +      '(e.g. "SFO", "JFK") for origin/destination and a price string like ' +      '"$289". After this tool returns, the flight card is already rendered ' +      "to the user via the A2UI surface — do NOT call it again for the same " +      "flight; reply with one short confirmation sentence and stop.",    inputSchema: z.object({      origin: z.string().describe('Origin airport code, e.g. "SFO".'),      destination: z.string().describe('Destination airport code, e.g. "JFK".'),      airline: z.string().describe('Airline name, e.g. "United".'),      price: z.string().describe('Price string, e.g. "$289".'),    }),    callback: ({ origin, destination, airline, price }) => ({      [A2UI_OPERATIONS_KEY]: [        createSurface(A2UI_FIXED_SURFACE_ID, A2UI_FIXED_CATALOG_ID),        updateComponents(A2UI_FIXED_SURFACE_ID, FLIGHT_SCHEMA),        updateDataModel(A2UI_FIXED_SURFACE_ID, {          origin,          destination,          airline,          price,        }),      ],    }),  });  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_FIXED_SYSTEM_PROMPT,    tools: [displayFlight],  });  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_fixed_schema",    description:      "A2UI surface from a fixed, pre-authored schema (direct backend tool)",  });}// ---------------------------------------------------------------------------// A2UI Dynamic Schema (declarative-gen-ui) — adapter auto-injects generate_a2ui.// ---------------------------------------------------------------------------//// Unlike the fixed-schema demo (which wires a `display_flight` tool returning a// pre-authored envelope), the dynamic demo lets the agent *generate* the// surface layout on the fly. The Next.js route// (app/api/copilotkit-declarative-gen-ui/route.ts) sets// `a2ui: { injectA2UITool: true, defaultCatalogId: "declarative-gen-ui-catalog" }`;// the runtime forwards the flag, the Strands adapter auto-injects a// `generate_a2ui` tool and drives a secondary render planner. The// `config.a2ui` block below supplies the catalog id stamped into generated// surfaces and the composition guide that teaches the planner the page's// catalog. Mirrors the ag-ui dynamic-schema reference example.//// The compositionGuide MUST describe the catalog the page registers at// src/app/demos/declarative-gen-ui/a2ui/{definitions,renderers,catalog}.ts// (catalog id `declarative-gen-ui-catalog`): Card / StatusBadge / Metric /// InfoRow / PrimaryButton / PieChart / BarChart / DataTable, composed inside// the basic catalog's Row / Column / Text (`includeBasicCatalog: true`).//// Grounding dataset + composition rules are kept in spirit with the frontend// `sales-context.ts` (SALES_DATASET + COMPOSITION_RULES) the page registers via// `useAgentContext`. The frontend context steers the PRIMARY agent; this// compositionGuide is the channel the adapter feeds to the secondary// `render_a2ui` planner (it gets `guidelines`, not the frontend App Context),// so the planner is self-contained.const A2UI_DYNAMIC_CATALOG_ID = "declarative-gen-ui-catalog";const A2UI_DYNAMIC_SALES_DATASET = `Vantage Threads (fictional B2B apparel company) — Q2 sales data. Ground every visual in these numbers; invent only plausible details consistent with them.- Quarterly revenue: $4.2M (up 12% QoQ). New customers: 186 (up 8%). Win rate: 31% (down 2pts). Avg deal size: $22.6k (up 5%).- Revenue by region: North America $1.9M, EMEA $1.3M, APAC $720k, LATAM $280k.- Monthly revenue: Jan $1.21M, Feb $1.34M, Mar $1.65M, Apr $1.38M, May $1.42M, Jun $1.40M.- Reps (vs quota): Dana Whitfield 124%, Marcus Lee 108%, Priya Sharma 97%, Tom Okafor 88%, Elena Vasquez 71%.- At-risk: total $615k ARR across 3 accounts — Northwind Retail ($340k renewal, no contact 6 weeks; severity high), Cascadia Outfitters ($180k, champion left; severity medium), Atlas Goods ($95k, stalled legal review; severity medium).- Biggest account: Meridian Apparel Group — owner Dana Whitfield, region North America, ARR $612k, renewal Sep 30, last contact 3 days ago, health green, 4 open opportunities worth $210k.- Meridian revenue by product line: Outerwear $260k, Footwear $180k, Accessories $112k, Custom $60k.`;const A2UI_DYNAMIC_COMPOSITION_RULES = `Use ONLY these exact component names (the registered catalog — any other name fails to render): Card, Column, Row, Text, Metric, PieChart, BarChart, DataTable, StatusBadge, InfoRow, PrimaryButton. The single-value KPI tile component is named exactly "Metric" (NOT "MetricTile" or "MetricCard").Pick A2UI components by the shape of the question — never ask which chart the user wants:1. Overall snapshot / "sales dashboard" → a Column (gap 16) whose first child is a Row (gap 16) of 4 Metric components (each with trend + trendValue), followed by a Row with a PieChart (revenue by region) next to a BarChart (monthly revenue, all six months Jan-Jun). Do NOT wrap the dashboard in a surrounding Card — the charts carry their own card chrome. Do NOT use StatusBadge, DataTable, or InfoRow here.2. Rep / team performance → a Column (gap 16) with a Card containing a DataTable (columns: rep, attainment, pipeline) next to or above a BarChart of quota attainment % per rep — no StatusBadge or InfoRow.3. Risk / health checks → a Column (gap 16): first a Row (gap 16) of 3 Metric components (ARR at risk $615k trend down, accounts at risk 3, biggest exposure Northwind $340k), then a Row (gap 16) with one compact Card per at-risk account (title = account name, subtitle = ARR at stake) containing a StatusBadge (error for high severity, warning otherwise) above a one-line Text with the reason and the recommended next action — no DataTable or InfoRow.4. Single account/entity details → a Row (gap 16) with a Card of InfoRow facts (owner, region, ARR, renewal date, last contact) next to a PieChart of that account's revenue by product line — no DataTable or StatusBadge.5. Part-of-whole follow-ups → PieChart; trends or comparisons over time/categories → BarChart.Compose generously — a dashboard should feel like a real analytics product, not a single widget.`;const A2UI_DYNAMIC_COMPOSITION_GUIDE = `${A2UI_DYNAMIC_SALES_DATASET}\n\n${A2UI_DYNAMIC_COMPOSITION_RULES}`;// Mirrors the langgraph-python demo's a2ui_dynamic.py SYSTEM_PROMPT.const A2UI_DYNAMIC_SYSTEM_PROMPT =  "You are the embedded sales analyst for Vantage Threads, the fictional " +  "B2B apparel company described in your App Context. Answer every " +  "business question by calling `generate_a2ui` to draw a rich visual " +  "surface, and keep the chat reply to one short sentence.\n\n" +  "Ground every number in the sales dataset from App Context — never " +  "invent figures that contradict it. Follow the dashboard composition " +  "rules from App Context when choosing components: pick the component " +  "by the shape of the question (snapshot → composed KPI dashboard with " +  "charts; team performance → table; risk → status badges; single " +  "account → info rows; part-of-whole → pie; trend/comparison → bar). " +  "Never ask the user which chart they want. `generate_a2ui` takes no " +  "arguments and handles the rendering automatically. Compose " +  "generously — a dashboard should feel like a real analytics product, " +  "not a single widget.";/** * Dedicated agent for the A2UI dynamic-schema demo. Wires NO `generate_a2ui` * tool — the runtime's `injectA2UITool: true` makes the adapter auto-inject it * and drive a secondary render planner to GENERATE the surface. */export async function buildA2uiDynamicAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_DYNAMIC_SYSTEM_PROMPT,  });  const config: StrandsAgentConfig = {    a2ui: {      defaultCatalogId: A2UI_DYNAMIC_CATALOG_ID,      guidelines: { compositionGuide: A2UI_DYNAMIC_COMPOSITION_GUIDE },    },  };  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_dynamic_schema",    description:      "Dynamic A2UI surfaces generated on the fly (auto-injected tool)",    config,  });}// ---------------------------------------------------------------------------// A2UI Error Recovery (a2ui-recovery) — adapter auto-injects + runs recovery.// ---------------------------------------------------------------------------//// Same auto-injected dynamic-schema setup as buildA2uiDynamicAgent, but the// aimock fixtures force the inner render_a2ui to emit free-form/sloppy args// (heal pill) or a structurally-invalid surface on every attempt (exhaust// pill). The Strands adapter runs the toolkit validate->retry recovery loop on// its auto-inject path (default 3 attempts) and returns the// a2ui_recovery_exhausted hard-fail envelope when the cap is hit — so this// agent wires NO tool, unlike the langgraph/ADK siblings (which own the tool// explicitly via getA2UITools + injectA2UITool:false). Mirrors the ag-ui dojo// aws-strands recovery example./** * Dedicated agent for the A2UI error-recovery demo. Wires NO `generate_a2ui` * tool — the runtime's `injectA2UITool: true` makes the adapter auto-inject it, * drive the secondary render planner, and run the recovery loop. */export async function buildA2uiRecoveryAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_DYNAMIC_SYSTEM_PROMPT,  });  const config: StrandsAgentConfig = {    a2ui: {      defaultCatalogId: A2UI_DYNAMIC_CATALOG_ID,      guidelines: { compositionGuide: A2UI_DYNAMIC_COMPOSITION_GUIDE },    },  };  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_recovery",    description:      "Dynamic A2UI with automatic error recovery (auto-injected tool)",    config,  });}

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
    
    
    import { z } from "zod";import type { CatalogDefinitions } from "@copilotkit/a2ui-renderer";export const myDefinitions = {  // Override the basic catalog's Row/Column so `gap` is honoured — the  // built-in versions ignore it, which makes composed dashboards cramped.  Row: {    description:      "Horizontal layout container. Children share the width evenly. Use `gap` (px) to space dashboard tiles.",    props: z.object({      gap: z.number().optional(),      // Enum mirrors the keys the renderer actually maps to CSS. Anything      // outside this set silently falls back at render time, so we reject      // it at schema-parse time to surface LLM typos early.      align: z        .enum(["start", "center", "end", "stretch", "baseline"])        .optional(),      justify: z.enum(["start", "center", "end", "spaceBetween"]).optional(),      children: z.array(z.string()),    }),  },  Column: {    description:      "Vertical layout container. Use `gap` (px) to space stacked sections.",    props: z.object({      gap: z.number().optional(),      align: z        .enum(["start", "center", "end", "stretch", "baseline"])        .optional(),      children: z.array(z.string()),    }),  },  // Override the basic catalog's Text so it aligns flush with sibling  // components (the built-in version carries an 8px outer margin).  Text: {    description: "A plain text line. Use for short explanations inside cards.",    props: z.object({      text: z.string(),    }),  },  Card: {    description:      "A titled card container with an optional subtitle and a single child slot. Use it to group related content (metrics, rows, buttons).",    props: z.object({      title: z.string(),      subtitle: z.string().optional(),      child: z.string().optional(),    }),  },  StatusBadge: {    description:      "A small coloured pill communicating the state of something (healthy/degraded/at-risk, on-track/behind). Choose `variant` to match the intent.",    props: z.object({      text: z.string(),      variant: z.enum(["success", "warning", "error", "info"]).optional(),    }),  },  Metric: {    description:      "A key/value KPI tile with an optional trend indicator and trend delta. Ideal for dashboard KPI rows (e.g. 'Revenue • $4.2M • up 12%').",    props: z.object({      label: z.string(),      value: z.string(),      trend: z.enum(["up", "down", "neutral"]).optional(),      trendValue: z.string().optional(),    }),  },  InfoRow: {    description:      "A compact two-column 'label: value' row. Good for stacks of facts inside a Card (owner, region, ARR, renewal date, etc.).",    props: z.object({      label: z.string(),      value: z.string(),    }),  },  DataTable: {    description:      "A data table with column headers and rows. Ideal for rankings and per-person/per-item breakdowns (rep performance vs quota, deal lists). Each row's keys MUST appear in `columns[].key`; unknown row keys render as blank cells and indicate model/schema drift.",    // NOTE on B12 (row-keys ⊆ columns[].key): we'd normally enforce this    // with `z.object(...).refine(...)`, but the host catalog package's    // `CatalogComponentDefinition` type requires `props: ZodObject<…>`    // (it inspects `.shape` at runtime), and `.refine` returns a    // `ZodEffects` that breaks both the `satisfies CatalogDefinitions`    // type assertion and the runtime `.shape` access. Until the host    // type is broadened, we encode the constraint in the description    // above so the LLM sees the rule, and leave hard enforcement to    // the rendering pipeline (which already shows the empty cell —    // detection is the gap, not behaviour).    props: z.object({      columns: z.array(z.object({ key: z.string(), label: z.string() })),      // Cells may be strings or numbers — the renderer stringifies at      // render time, but accepting both lets the LLM emit raw numerics      // (e.g. attainment 124) instead of being forced to stringify.      rows: z.array(z.record(z.union([z.string(), z.number()]))),    }),  },  PrimaryButton: {    description:      "A styled primary call-to-action button. Attach an optional `action` that will be dispatched back to the agent when the user clicks it.",    props: z.object({      label: z.string(),      // The renderer hands `action` opaquely to the A2UI `dispatch` helper,      // which forwards it back to the agent. We don't constrain the shape      // (different demos use different action payloads), but `z.unknown()`      // is strictly better than `z.any()` here because it forces any      // consumer that touches the value to narrow it explicitly.      action: z.unknown().optional(),    }),  },  PieChart: {    description:      "A pie/donut chart with a brand-coloured legend. Provide `title`, `description`, and `data` as an array of `{ label, value }` objects. Great for part-of-whole breakdowns (revenue by region, pipeline by stage).",    props: z.object({      title: z.string(),      description: z.string(),      data: z.array(        z.object({          label: z.string(),          value: z.number(),        }),      ),    }),  },  BarChart: {    description:      "A vertical bar chart built on Recharts. Provide `title`, `description`, and `data` as an array of `{ label, value }` objects. Great for comparing series across categories or time (monthly revenue, signups per month).",    props: z.object({      title: z.string(),      description: z.string(),      data: z.array(        z.object({          label: z.string(),          value: z.number(),        }),      ),    }),  },} satisfies CatalogDefinitions;

### Implement the React renderers#

Every key in `myDefinitions` must have a matching renderer. Props are statically typed against the Zod schema, so refactors stay safe:

renderers.tsx
    
    
    export const myRenderers: CatalogRenderers<MyDefinitions> = {  Row: ({ props, children }) => {    const justifyMap: Record<string, string> = {      start: "flex-start",      center: "center",      end: "flex-end",      spaceBetween: "space-between",    };    const items = Array.isArray(props.children) ? props.children : [];    return (      <div        style={{          display: "flex",          flexDirection: "row",          gap: `${props.gap ?? 16}px`,          alignItems: props.align ?? "stretch",          justifyContent: justifyMap[props.justify ?? "start"] ?? "flex-start",          flexWrap: "wrap",          width: "100%",        }}      >        {items.map((id, i) => (          <div key={`${id}-${i}`} style={{ flex: "1 1 0", minWidth: 0 }}>            {children(id)}          </div>        ))}      </div>    );  },  Column: ({ props, children }) => {    const items = Array.isArray(props.children) ? props.children : [];    return (      <div        style={{          display: "flex",          flexDirection: "column",          gap: `${props.gap ?? 12}px`,          width: "100%",        }}      >        {items.map((id, i) => (          <React.Fragment key={`${id}-${i}`}>{children(id)}</React.Fragment>        ))}      </div>    );  },  Text: ({ props }) => (    <span style={{ fontSize: "0.85rem", color: c.cardFg, lineHeight: 1.5 }}>      {props.text}    </span>  ),  Card: ({ props, children }) => (    // `data-testid="declarative-card"` stays shared so existing e2e selectors    // still find every card; `data-card-id={props.title}` disambiguates    // sibling cards (e.g. the at-risk pill's 3 severity cards) so test    // assertions can target a specific card by title.    <CardShell      title={props.title}      subtitle={props.subtitle}      testid="declarative-card"      cardId={props.title}    >      {props.child && children(props.child)}    </CardShell>  ),  StatusBadge: ({ props }) => {    const variant = props.variant ?? "info";    const Icon = {      error: TriangleAlert,      warning: CircleAlert,      success: CircleCheck,      info: Info,    }[variant];    return (      // `alignSelf: flex-start` keeps the pill content-sized — flex parents      // (our Column override) default to stretch, which inflates it into a      // full-width banner.      <Badge        variant={variant}        style={{ alignSelf: "flex-start" }}        data-testid="declarative-status-badge"      >        <Icon size={12} strokeWidth={2.5} style={{ marginRight: 4 }} />        {props.text}      </Badge>    );  },  Metric: ({ props }) => {    const trendColors: Record<string, string> = {      up: "#059669",      down: "#dc2626",      neutral: c.muted,    };    const trendIcons: Record<string, string> = {      up: "↑",      down: "↓",      neutral: "→",    };    return (      <div        data-testid="declarative-metric"        style={{          display: "flex",          flexDirection: "column",          gap: "4px",          minWidth: "120px",        }}      >        <span          style={{            fontSize: "0.75rem",            color: c.muted,            fontWeight: 500,            textTransform: "uppercase",            letterSpacing: "0.05em",          }}        >          {props.label}        </span>        <div style={{ display: "flex", alignItems: "baseline", gap: "8px" }}>          <span            style={{              fontSize: "1.5rem",              fontWeight: 700,              color: c.cardFg,              letterSpacing: "-0.02em",            }}          >            {props.value}          </span>          {props.trend && (            <span              style={{                fontSize: "0.8rem",                fontWeight: 500,                color: trendColors[props.trend] ?? c.muted,              }}            >              {trendIcons[props.trend]}              {props.trendValue ? ` ${props.trendValue}` : ""}            </span>          )}        </div>      </div>    );  },  InfoRow: ({ props }) => (    // Divider via `border-b last:border-b-0` so the final row doesn't dangle    // a trailing line, regardless of whether the agent wraps these in a    // Column or drops them directly into a Card's child slot.    <div      data-testid="declarative-info-row"      className="flex items-baseline justify-between gap-4 py-2 border-b border-[var(--border)] last:border-b-0 last:pb-0 first:pt-0"    >      <span className="text-sm text-[var(--muted-foreground)]">        {props.label}      </span>      <span className="text-sm font-medium text-[var(--foreground)] text-right tabular-nums">        {props.value}      </span>    </div>  ),  DataTable: ({ props }) => {    const cols = Array.isArray(props.columns) ? props.columns : [];    const rows = Array.isArray(props.rows) ? props.rows : [];    return (      <div        data-testid="declarative-data-table"        className="w-full overflow-x-auto"      >        <table className="w-full border-collapse text-sm">          <thead>            <tr>              {cols.map((col) => (                <th                  key={col.key}                  className="border-b-2 border-[var(--border)] px-3 py-2 text-left text-xs font-semibold uppercase tracking-wider text-[var(--muted-foreground)]"                >                  {col.label}                </th>              ))}            </tr>          </thead>          <tbody>            {rows.map((row, i) => {              // Stable row key: prefer the first column's value (primary-key-ish),              // suffix with index in case values repeat, fall back to a JSON              // stringify of the row when columns is empty. Stable keys prevent              // React from re-mounting every row when the agent re-emits a              // slightly different table.              const pk = cols.length > 0 ? row[cols[0].key] : undefined;              const rowKey =                pk !== undefined ? `${pk}-${i}` : JSON.stringify(row);              return (                <tr                  key={rowKey}                  className="border-b border-[var(--border)] last:border-b-0"                >                  {cols.map((col) => (                    <td                      key={col.key}                      className="px-3 py-2 tabular-nums text-[var(--foreground)]"                    >                      {String(row[col.key] ?? "")}                    </td>                  ))}                </tr>              );            })}          </tbody>        </table>      </div>    );  },  PrimaryButton: ({ props, dispatch }) => (    <Button      onClick={() => {        if (props.action && dispatch) dispatch(props.action);      }}    >      {props.label}    </Button>  ),  PieChart: ({ props }) => {    // Coerce values to numbers — the LLM sometimes emits them as strings.    // Use a strict finite check so null/undefined/NaN/non-numeric strings are    // surfaced via console.warn rather than silently collapsed to 0 (which    // masks schema/data drift). Recharts requires a numeric value to render,    // so we fall back to 0 only after logging.    const data = (Array.isArray(props.data) ? props.data : []).map((d) => {      const raw = (d as { value?: unknown }).value;      const n = typeof raw === "number" ? raw : parseFloat(raw as string);      let value: number;      if (Number.isFinite(n)) {        value = n;      } else {        console.warn("Invalid chart value", {          component: "PieChart",          key: "value",          raw,        });        value = 0;      }      return { ...d, value };    });    return (      <CardShell        title={props.title}        subtitle={props.description}        testid="declarative-pie-chart"      >        {data.length === 0 ? (          <div className="py-8 text-center text-sm text-[var(--muted-foreground)]">            No data available          </div>        ) : (          <div style={{ width: "100%", height: 200 }}>            <ResponsiveContainer>              <RechartsPieChart>                <Pie                  data={data}                  dataKey="value"                  nameKey="label"                  cx="50%"                  cy="50%"                  innerRadius={40}                  outerRadius={80}                  paddingAngle={2}                >                  {data.map((_, i) => (                    <Cell                      key={i}                      fill={CHART_COLORS[i % CHART_COLORS.length]}                    />                  ))}                </Pie>                <Tooltip />              </RechartsPieChart>            </ResponsiveContainer>          </div>        )}      </CardShell>    );  },  BarChart: ({ props }) => {    // Coerce values to numbers — the LLM sometimes emits them as strings,    // which recharts treats as categorical (unordered Y-axis ticks). Use a    // strict finite check so null/undefined/NaN/non-numeric strings are    // surfaced via console.warn rather than silently collapsed to 0 (which    // masks schema/data drift). Recharts requires a numeric value to render,    // so we fall back to 0 only after logging.    const data = (Array.isArray(props.data) ? props.data : []).map((d) => {      const raw = (d as { value?: unknown }).value;      const n = typeof raw === "number" ? raw : parseFloat(raw as string);      let value: number;      if (Number.isFinite(n)) {        value = n;      } else {        console.warn("Invalid chart value", {          component: "BarChart",          key: "value",          raw,        });        value = 0;      }      return { ...d, value };    });    return (      <CardShell        title={props.title}        subtitle={props.description}        testid="declarative-bar-chart"      >        {data.length === 0 ? (          <div className="py-8 text-center text-sm text-[var(--muted-foreground)]">            No data available          </div>        ) : (          <div style={{ width: "100%", height: 200 }}>            <ResponsiveContainer>              <RechartsBarChart data={data}>                <CartesianGrid strokeDasharray="3 3" stroke={c.divider} />                <XAxis dataKey="label" tick={{ fontSize: 11, fill: c.muted }} />                <YAxis tick={{ fontSize: 11, fill: c.muted }} />                <Tooltip />                <Bar dataKey="value" fill="#3b82f6" radius={[4, 4, 0, 0]} />              </RechartsBarChart>            </ResponsiveContainer>          </div>        )}      </CardShell>    );  },};

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



If the surface is well-known (e.g. a product card, a flight result), prefer a **[fixed schema](https://docs.copilotkit.ai/strands-typescript/generative-ui/a2ui/dynamic-schema/fixed-schema)** ; it's faster, cheaper, and the UI is deterministic.

### On this page

How it worksThe 3-file splitDeclare your custom component definitionsImplement the React renderersWire definitions × renderers into a catalogPass the catalog to the providerI opted out of auto-inject, now what?The A2UIMiddlewareThe A2UI agent toolProgressive streamingWhen should I use dynamic schemas?
