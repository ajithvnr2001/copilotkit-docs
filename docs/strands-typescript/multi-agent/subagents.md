---
url: https://docs.copilotkit.ai/strands-typescript/multi-agent/subagents/
title: Sub-Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:30:00.029366+00:00
---

# Sub-Agents

> Source: https://docs.copilotkit.ai/strands-typescript/multi-agent/subagents/

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

Agent capabilities

# Sub-Agents

Decompose work across multiple specialized agents with a visible delegation log.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.ts

tools.ts

state.ts

page.tsx

delegation-log.tsx

route.ts
    
    
    /** * Agent factories for the Strands TypeScript showcase backend. * * `buildShowcaseAgent` is the single shared agent that serves the vast * majority of demos (the frontend differentiates each demo via * useFrontendTool / useRenderTool / useHumanInTheLoop / useAgentContext). * It mirrors the Python sibling's `build_showcase_agent` minus A2UI. * * The tool-free specialized agents (voice, byoc-hashbrown, byoc-json-render) * are mounted on dedicated sub-paths by `server.ts`. */import { readFileSync } from "node:fs";import { dirname, join } from "node:path";import { fileURLToPath } from "node:url";import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import type { RunAgentInput } from "@ag-ui/core";import { StrandsAgent } from "@ag-ui/aws-strands";import type { StrandsAgentConfig } from "@ag-ui/aws-strands";import {  A2UI_OPERATIONS_KEY,  createSurface,  updateComponents,  updateDataModel,} from "@ag-ui/a2ui-toolkit";import { createModel } from "./model-factory";import { SHOWCASE_TOOLS } from "./tools";import {  withStateContext,  salesStateFromArgs,  notesStateFromArgs,  stepsStateFromArgs,  documentStateFromArgs,  makeSubagentStateFromResult,} from "./state";import {  SYSTEM_PROMPT,  VOICE_SYSTEM_PROMPT,  BYOC_HASHBROWN_SYSTEM_PROMPT,  BYOC_JSON_RENDER_SYSTEM_PROMPT,} from "./prompts";export class ShowcaseStrandsAgent extends StrandsAgent {  override async *run(inputData: RunAgentInput) {    // The adapter exposes context during model calls and restores history afterward.    yield* super.run(withStateContext(inputData));  }}export async function buildShowcaseAgent(): Promise<StrandsAgent> {  const config: StrandsAgentConfig = {    toolBehaviors: {      // The tool keeps the sales pipeline in appState; this snapshot, built      // from the args, only carries it to the UI.      manage_sales_todos: {        skipMessagesSnapshot: true,        stateFromArgs: salesStateFromArgs,      },      // Shared State (Read + Write) — notes panel.      set_notes: { stateFromArgs: notesStateFromArgs },      // gen-ui-agent — live progress card driven by set_steps transitions.      set_steps: { stateFromArgs: stepsStateFromArgs },      // shared-state-streaming — stream the document string into state.      write_document: { stateFromArgs: documentStateFromArgs },      // Sub-agents — append a delegation entry carrying the actual output.      research_agent: {        stateFromResult: makeSubagentStateFromResult("research_agent"),      },      writing_agent: {        stateFromResult: makeSubagentStateFromResult("writing_agent"),      },      critique_agent: {        stateFromResult: makeSubagentStateFromResult("critique_agent"),      },    },  };  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: SYSTEM_PROMPT,    tools: SHOWCASE_TOOLS,  });  return new ShowcaseStrandsAgent({    agent: strandsAgent,    name: "strands_agent",    description:      "A polished CopilotKit demo assistant: chat, tools, shared state, HITL, sub-agents.",    config,  });}/** Tool-free agent for the voice demo (transcription + basic chat). */export async function buildVoiceAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: VOICE_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "voice_agent",    description: "Simple assistant for the voice demo — no tools.",  });}/** Tool-free hashbrown UI-kit envelope generator (declarative-hashbrown). */export async function buildByocHashbrownAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: BYOC_HASHBROWN_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "byoc_hashbrown",    description:      "Hashbrown UI-kit envelope generator for the declarative-hashbrown demo.",  });}/** Tool-free json-render flat-spec generator (declarative-json-render). */export async function buildByocJsonRenderAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: BYOC_JSON_RENDER_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "byoc_json_render",    description:      "json-render flat-spec generator for the declarative-json-render demo.",  });}// ---------------------------------------------------------------------------// A2UI Fixed Schema (declarative-generative-ui) — dedicated backend tool.// ---------------------------------------------------------------------------//// Unlike the dynamic A2UI demo (which relies on the adapter auto-injecting a// `generate_a2ui` tool to *generate* a surface), the fixed-schema demo wires a// single plain backend tool — `display_flight` — that returns the// `a2ui_operations` envelope (createSurface -> updateComponents ->// updateDataModel). The component tree is fixed and authored ahead of time// (./a2ui_schemas/flight_schema.json); only the *data* changes per call. The// runtime A2UIMiddleware detects the envelope in the tool result and paints.// No sub-agent, no generation, no `generate_a2ui` injection.//// The schema's component names + data paths must match the showcase frontend// catalog at src/app/demos/a2ui-fixed-schema/a2ui/{definitions,renderers,// catalog}.ts — catalog id `copilotkit://flight-fixed-catalog`. This mirrors// the canonical langgraph-python demo (src/agents/a2ui_fixed.py).const _A2UI_DIR = dirname(fileURLToPath(import.meta.url));const A2UI_FIXED_CATALOG_ID = "copilotkit://flight-fixed-catalog";const A2UI_FIXED_SURFACE_ID = "flight-fixed-schema";// Fixed, pre-authored component layout. Loaded from JSON so it can be authored// and reviewed independently of the agent code.const FLIGHT_SCHEMA: Array<Record<string, unknown>> = JSON.parse(  readFileSync(join(_A2UI_DIR, "a2ui_schemas", "flight_schema.json"), "utf-8"),);const A2UI_FIXED_SYSTEM_PROMPT =  "You help users find flights. When asked about a flight, call " +  "`display_flight` exactly ONCE with origin, destination, airline, and " +  'price. Use short airport codes (e.g. "SFO", "JFK") for ' +  'origin/destination and a price string like "$289". The tool\'s return ' +  "value is an A2UI surface descriptor — the flight card is already rendered " +  "to the user; do NOT call `display_flight` again for the same trip and do " +  "NOT repeat the flight details in text. After the tool returns, reply with " +  "one short confirmation sentence and stop.";/** * Dedicated agent for the A2UI fixed-schema demo. Returns the envelope as a * plain OBJECT (not a JSON string): the Strands TS SDK wraps an object * tool-return in a `json` content block the adapter reads and re-stringifies * into the TOOL_CALL_RESULT the client A2UIMiddleware scans for * `a2ui_operations`. (A bare string return lands in no content block and the * result comes through empty — unlike the Python SDK, which wraps strings.) */export async function buildA2uiFixedSchemaAgent(): Promise<StrandsAgent> {  const displayFlight = tool({    name: "display_flight",    description:      "Show a flight card for the given trip. Use short airport codes " +      '(e.g. "SFO", "JFK") for origin/destination and a price string like ' +      '"$289". After this tool returns, the flight card is already rendered ' +      "to the user via the A2UI surface — do NOT call it again for the same " +      "flight; reply with one short confirmation sentence and stop.",    inputSchema: z.object({      origin: z.string().describe('Origin airport code, e.g. "SFO".'),      destination: z.string().describe('Destination airport code, e.g. "JFK".'),      airline: z.string().describe('Airline name, e.g. "United".'),      price: z.string().describe('Price string, e.g. "$289".'),    }),    callback: ({ origin, destination, airline, price }) => ({      [A2UI_OPERATIONS_KEY]: [        createSurface(A2UI_FIXED_SURFACE_ID, A2UI_FIXED_CATALOG_ID),        updateComponents(A2UI_FIXED_SURFACE_ID, FLIGHT_SCHEMA),        updateDataModel(A2UI_FIXED_SURFACE_ID, {          origin,          destination,          airline,          price,        }),      ],    }),  });  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_FIXED_SYSTEM_PROMPT,    tools: [displayFlight],  });  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_fixed_schema",    description:      "A2UI surface from a fixed, pre-authored schema (direct backend tool)",  });}// ---------------------------------------------------------------------------// A2UI Dynamic Schema (declarative-gen-ui) — adapter auto-injects generate_a2ui.// ---------------------------------------------------------------------------//// Unlike the fixed-schema demo (which wires a `display_flight` tool returning a// pre-authored envelope), the dynamic demo lets the agent *generate* the// surface layout on the fly. The Next.js route// (app/api/copilotkit-declarative-gen-ui/route.ts) sets// `a2ui: { injectA2UITool: true, defaultCatalogId: "declarative-gen-ui-catalog" }`;// the runtime forwards the flag, the Strands adapter auto-injects a// `generate_a2ui` tool and drives a secondary render planner. The// `config.a2ui` block below supplies the catalog id stamped into generated// surfaces and the composition guide that teaches the planner the page's// catalog. Mirrors the ag-ui dynamic-schema reference example.//// The compositionGuide MUST describe the catalog the page registers at// src/app/demos/declarative-gen-ui/a2ui/{definitions,renderers,catalog}.ts// (catalog id `declarative-gen-ui-catalog`): Card / StatusBadge / Metric /// InfoRow / PrimaryButton / PieChart / BarChart / DataTable, composed inside// the basic catalog's Row / Column / Text (`includeBasicCatalog: true`).//// Grounding dataset + composition rules are kept in spirit with the frontend// `sales-context.ts` (SALES_DATASET + COMPOSITION_RULES) the page registers via// `useAgentContext`. The frontend context steers the PRIMARY agent; this// compositionGuide is the channel the adapter feeds to the secondary// `render_a2ui` planner (it gets `guidelines`, not the frontend App Context),// so the planner is self-contained.const A2UI_DYNAMIC_CATALOG_ID = "declarative-gen-ui-catalog";const A2UI_DYNAMIC_SALES_DATASET = `Vantage Threads (fictional B2B apparel company) — Q2 sales data. Ground every visual in these numbers; invent only plausible details consistent with them.- Quarterly revenue: $4.2M (up 12% QoQ). New customers: 186 (up 8%). Win rate: 31% (down 2pts). Avg deal size: $22.6k (up 5%).- Revenue by region: North America $1.9M, EMEA $1.3M, APAC $720k, LATAM $280k.- Monthly revenue: Jan $1.21M, Feb $1.34M, Mar $1.65M, Apr $1.38M, May $1.42M, Jun $1.40M.- Reps (vs quota): Dana Whitfield 124%, Marcus Lee 108%, Priya Sharma 97%, Tom Okafor 88%, Elena Vasquez 71%.- At-risk: total $615k ARR across 3 accounts — Northwind Retail ($340k renewal, no contact 6 weeks; severity high), Cascadia Outfitters ($180k, champion left; severity medium), Atlas Goods ($95k, stalled legal review; severity medium).- Biggest account: Meridian Apparel Group — owner Dana Whitfield, region North America, ARR $612k, renewal Sep 30, last contact 3 days ago, health green, 4 open opportunities worth $210k.- Meridian revenue by product line: Outerwear $260k, Footwear $180k, Accessories $112k, Custom $60k.`;const A2UI_DYNAMIC_COMPOSITION_RULES = `Use ONLY these exact component names (the registered catalog — any other name fails to render): Card, Column, Row, Text, Metric, PieChart, BarChart, DataTable, StatusBadge, InfoRow, PrimaryButton. The single-value KPI tile component is named exactly "Metric" (NOT "MetricTile" or "MetricCard").Pick A2UI components by the shape of the question — never ask which chart the user wants:1. Overall snapshot / "sales dashboard" → a Column (gap 16) whose first child is a Row (gap 16) of 4 Metric components (each with trend + trendValue), followed by a Row with a PieChart (revenue by region) next to a BarChart (monthly revenue, all six months Jan-Jun). Do NOT wrap the dashboard in a surrounding Card — the charts carry their own card chrome. Do NOT use StatusBadge, DataTable, or InfoRow here.2. Rep / team performance → a Column (gap 16) with a Card containing a DataTable (columns: rep, attainment, pipeline) next to or above a BarChart of quota attainment % per rep — no StatusBadge or InfoRow.3. Risk / health checks → a Column (gap 16): first a Row (gap 16) of 3 Metric components (ARR at risk $615k trend down, accounts at risk 3, biggest exposure Northwind $340k), then a Row (gap 16) with one compact Card per at-risk account (title = account name, subtitle = ARR at stake) containing a StatusBadge (error for high severity, warning otherwise) above a one-line Text with the reason and the recommended next action — no DataTable or InfoRow.4. Single account/entity details → a Row (gap 16) with a Card of InfoRow facts (owner, region, ARR, renewal date, last contact) next to a PieChart of that account's revenue by product line — no DataTable or StatusBadge.5. Part-of-whole follow-ups → PieChart; trends or comparisons over time/categories → BarChart.Compose generously — a dashboard should feel like a real analytics product, not a single widget.`;const A2UI_DYNAMIC_COMPOSITION_GUIDE = `${A2UI_DYNAMIC_SALES_DATASET}\n\n${A2UI_DYNAMIC_COMPOSITION_RULES}`;// Mirrors the langgraph-python demo's a2ui_dynamic.py SYSTEM_PROMPT.const A2UI_DYNAMIC_SYSTEM_PROMPT =  "You are the embedded sales analyst for Vantage Threads, the fictional " +  "B2B apparel company described in your App Context. Answer every " +  "business question by calling `generate_a2ui` to draw a rich visual " +  "surface, and keep the chat reply to one short sentence.\n\n" +  "Ground every number in the sales dataset from App Context — never " +  "invent figures that contradict it. Follow the dashboard composition " +  "rules from App Context when choosing components: pick the component " +  "by the shape of the question (snapshot → composed KPI dashboard with " +  "charts; team performance → table; risk → status badges; single " +  "account → info rows; part-of-whole → pie; trend/comparison → bar). " +  "Never ask the user which chart they want. `generate_a2ui` takes no " +  "arguments and handles the rendering automatically. Compose " +  "generously — a dashboard should feel like a real analytics product, " +  "not a single widget.";/** * Dedicated agent for the A2UI dynamic-schema demo. Wires NO `generate_a2ui` * tool — the runtime's `injectA2UITool: true` makes the adapter auto-inject it * and drive a secondary render planner to GENERATE the surface. */export async function buildA2uiDynamicAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_DYNAMIC_SYSTEM_PROMPT,  });  const config: StrandsAgentConfig = {    a2ui: {      defaultCatalogId: A2UI_DYNAMIC_CATALOG_ID,      guidelines: { compositionGuide: A2UI_DYNAMIC_COMPOSITION_GUIDE },    },  };  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_dynamic_schema",    description:      "Dynamic A2UI surfaces generated on the fly (auto-injected tool)",    config,  });}// ---------------------------------------------------------------------------// A2UI Error Recovery (a2ui-recovery) — adapter auto-injects + runs recovery.// ---------------------------------------------------------------------------//// Same auto-injected dynamic-schema setup as buildA2uiDynamicAgent, but the// aimock fixtures force the inner render_a2ui to emit free-form/sloppy args// (heal pill) or a structurally-invalid surface on every attempt (exhaust// pill). The Strands adapter runs the toolkit validate->retry recovery loop on// its auto-inject path (default 3 attempts) and returns the// a2ui_recovery_exhausted hard-fail envelope when the cap is hit — so this// agent wires NO tool, unlike the langgraph/ADK siblings (which own the tool// explicitly via getA2UITools + injectA2UITool:false). Mirrors the ag-ui dojo// aws-strands recovery example./** * Dedicated agent for the A2UI error-recovery demo. Wires NO `generate_a2ui` * tool — the runtime's `injectA2UITool: true` makes the adapter auto-inject it, * drive the secondary render planner, and run the recovery loop. */export async function buildA2uiRecoveryAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_DYNAMIC_SYSTEM_PROMPT,  });  const config: StrandsAgentConfig = {    a2ui: {      defaultCatalogId: A2UI_DYNAMIC_CATALOG_ID,      guidelines: { compositionGuide: A2UI_DYNAMIC_COMPOSITION_GUIDE },    },  };  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_recovery",    description:      "Dynamic A2UI with automatic error recovery (auto-injected tool)",    config,  });}

## What is this?#

Sub-agents are the canonical multi-agent pattern: a top-level **supervisor** LLM orchestrates one or more specialized **sub-agents** by exposing each of them as a tool. The supervisor decides what to delegate, the sub-agents do their narrow job, and their results flow back up to the supervisor's next step.

This is fundamentally the same shape as tool-calling, but each "tool" is itself a full-blown agent with its own system prompt and (often) its own tools, memory, and model.

## When should I use this?#

Reach for sub-agents when a task has distinct specialized sub-tasks that each benefit from their own focus:

  * **Research → Write → Critique** pipelines, where each stage needs a different system prompt and temperature.
  * **Router + specialists** , where one agent classifies the request and dispatches to the right expert.
  * **Divide-and-conquer** — any problem that fits cleanly into parallel or sequential sub-problems.



The example below uses the Research → Write → Critique shape as the canonical example.

## Setting up sub-agents#

Each sub-agent is an isolated agent call with its own model, system prompt, and optional tools. They don't share memory or tools with the supervisor; the supervisor only ever sees what the sub-agent returns.

tools.ts
    
    
    const SUBAGENT_SYSTEM_PROMPTS: Record<string, string> = {  research_agent:    "You are a research sub-agent. Given a topic, produce a concise bulleted list of 3-5 key facts. No preamble, no closing.",  writing_agent:    "You are a writing sub-agent. Given a brief and optional source facts, produce a polished 1-paragraph draft. Be clear and concrete. No preamble.",  critique_agent:    "You are an editorial critique sub-agent. Given a draft, give 2-3 crisp, actionable critiques. No preamble.",};const SUBAGENT_EMPTY_RESULT = "(sub-agent returned no content)";let _openaiClient: OpenAI | null = null;export function openaiClient(): OpenAI {  if (!_openaiClient) {    const apiKey = process.env.OPENAI_API_KEY;    if (!apiKey) {      throw new Error("OPENAI_API_KEY must be set for sub-agent delegation.");    }    _openaiClient = new OpenAI({      apiKey,      ...(process.env.OPENAI_BASE_URL        ? { baseURL: process.env.OPENAI_BASE_URL }        : {}),      // Match the shared agent so sub-agent calls hit the right aimock fixtures.      defaultHeaders: { "x-aimock-context": AIMOCK_CONTEXT },      // Per-request inbound x-* forwarding (incl. X-AIMock-Strict / x-test-id /      // x-diag-*), mirroring model-factory.ts. The sub-agent client is built      // ONCE (memoized), but forwardingFetch reads an AsyncLocalStorage      // snapshot per outbound call (seeded by the Express cvdiag/forwarding      // middleware around agent.run()), so per-request headers flow correctly.      // It never clobbers the static x-aimock-context above, and is      // byte-identical to a plain fetch when no x-* are in scope (demo traffic      // unaffected).      fetch: forwardingFetch,    });  }  return _openaiClient;}/** * Run a single-shot completion as a sub-agent. Returns the failure marker * (caught in `state.ts`) on transport/API errors rather than throwing, so a * delegation failure surfaces as a "failed" log row instead of a 500. */async function runSubagent(name: string, task: string): Promise<string> {  const systemPrompt = SUBAGENT_SYSTEM_PROMPTS[name];  try {    const response = await openaiClient().chat.completions.create({      model: process.env.SUBAGENT_MODEL_ID ?? "gpt-4o-mini",      messages: [        { role: "system", content: systemPrompt },        { role: "user", content: task },      ],    });    const content = response.choices[0]?.message?.content ?? "";    const text = content.trim();    return text || SUBAGENT_EMPTY_RESULT;  } catch (err) {    const cls = err instanceof Error ? err.constructor.name : "Error";    return `${SUBAGENT_FAILURE_MARKER}${cls}`;  }}

Keep sub-agent system prompts narrow and focused. The point of this pattern is that each one does one thing well. If a sub-agent needs to know the whole user context to do its job, that's a signal the boundary is wrong.

## Exposing sub-agents as tools#

The supervisor delegates by calling tools. Each delegation tool is a thin wrapper around a specialized agent call that:

  1. Runs the sub-agent on the supplied `task` string.
  2. Records the delegation into a `delegations` slot in shared agent state (so the UI can render a live log).
  3. Returns the sub-agent's final message as the tool result, which the supervisor sees on its next turn.



tools.ts
    
    
    export const researchAgent = tool({  name: "research_agent",  description:    "Delegate a research task to the research sub-agent. Use for gathering facts, background, definitions, statistics. Returns a bulleted list of key facts.",  inputSchema: z.object({    task: z.string().describe("The research brief to hand off."),  }),  callback: ({ task }) => runSubagent("research_agent", task),});export const writingAgent = tool({  name: "writing_agent",  description:    "Delegate a drafting task to the writing sub-agent. Use for producing a polished paragraph, draft, or summary. Pass relevant facts inside `task`.",  inputSchema: z.object({    task: z.string().describe("The writing brief to hand off."),  }),  callback: ({ task }) => runSubagent("writing_agent", task),});export const critiqueAgent = tool({  name: "critique_agent",  description:    "Delegate a critique task to the critique sub-agent. Use for reviewing a draft and suggesting concrete improvements.",  inputSchema: z.object({    task: z.string().describe("The draft to critique."),  }),  callback: ({ task }) => runSubagent("critique_agent", task),});

This is where CopilotKit's shared-state channel earns its keep: the supervisor's tool calls mutate `delegations` as they happen, and the frontend renders every new entry live.

Give every delegation a stable `id` and merge new entries by that `id`. The client sends its copy of shared state back as run input on every run, so a slot that blindly appends whatever it receives — a LangGraph `Annotated[list, operator.add]` reducer, for example — concatenates the entries the client just echoed onto the ones the agent already has, and the log doubles when a thread is continued.

## Rendering a live delegation log#

On the frontend, the delegation log is a reactive render of the `delegations` slot.

Subscribe with `useAgent({ updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged] })`, read `agent.state.delegations`, and render one card per entry.

delegation-log.tsx
    
    
    /** * Live delegation log — renders the `delegations` slot of agent state. * * Each entry corresponds to one invocation of a sub-agent. The list * grows in real time as the supervisor fans work out to its children. * The parent header shows how many sub-agents have been called and * whether the supervisor is still running. */// Fixed list of the three sub-agent roles the supervisor can call.// Rendered as always-visible indicator chips at the top of the log// (regardless of whether the supervisor has delegated yet) so the user// — and the e2e suite — can see at a glance which sub-agents exist and// which are currently active.const INDICATOR_ROLES: ReadonlyArray<{  role: "researcher" | "writer" | "critic";  subAgent: SubAgentName;}> = [  { role: "researcher", subAgent: "research_agent" },  { role: "writer", subAgent: "writing_agent" },  { role: "critic", subAgent: "critique_agent" },];export function DelegationLog({ delegations, isRunning }: DelegationLogProps) {  const calledRoles = new Set<SubAgentName>(    delegations.map((d) => d.sub_agent),  );  return (    <div      data-testid="delegation-log"      className="w-full h-full flex flex-col bg-white rounded-2xl shadow-sm border border-[#DBDBE5] overflow-hidden"    >      <div className="flex items-center justify-between px-6 py-3 border-b border-[#E9E9EF] bg-[#FAFAFC]">        <div className="flex items-center gap-3">          <span className="text-lg font-semibold text-[#010507]">            Sub-agent delegations          </span>          {isRunning && (            <span              data-testid="supervisor-running"              className="inline-flex items-center gap-1.5 px-2 py-0.5 rounded-full border border-[#BEC2FF] bg-[#BEC2FF1A] text-[#010507] text-[10px] font-semibold uppercase tracking-[0.12em]"            >              <span className="w-1.5 h-1.5 rounded-full bg-[#010507] animate-pulse" />              Supervisor running            </span>          )}        </div>        <span          data-testid="delegation-count"          className="text-xs font-mono text-[#838389]"        >          {delegations.length} calls        </span>      </div>      <div        data-testid="subagent-indicators"        className="flex items-center gap-2 border-b border-[#E9E9EF] bg-white px-6 py-2"      >        {INDICATOR_ROLES.map(({ role, subAgent }) => {          const style = SUB_AGENT_STYLE[subAgent];          const fired = calledRoles.has(subAgent);          return (            <span              key={role}              data-testid={`subagent-indicator-${role}`}              data-role={role}              data-fired={fired ? "true" : "false"}              className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color} ${                fired ? "" : "opacity-60"              }`}            >              <span aria-hidden>{style.emoji}</span>              <span>{style.label}</span>            </span>          );        })}      </div>      <div className="flex-1 overflow-y-auto p-4 space-y-3">        {delegations.length === 0 ? (          <p className="text-[#838389] italic text-sm">            Ask the supervisor to complete a task. Every sub-agent it calls will            appear here.          </p>        ) : (          delegations.map((d, idx) => {            const style = SUB_AGENT_STYLE[d.sub_agent];            return (              <div                key={d.id}                data-testid="delegation-entry"                className="border border-[#E9E9EF] rounded-xl p-3 bg-[#FAFAFC]"              >                <div className="flex items-center justify-between mb-2">                  <div className="flex items-center gap-2">                    <span className="text-xs font-mono text-[#AFAFB7]">                      #{idx + 1}                    </span>                    <span                      className={`inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-[10px] font-semibold uppercase tracking-[0.1em] border ${style.color}`}                    >                      <span>{style.emoji}</span>                      <span>{style.label}</span>                    </span>                  </div>                  <span className="text-[10px] uppercase tracking-[0.12em] font-semibold text-[#189370]">                    {d.status}                  </span>                </div>                <div className="text-xs text-[#57575B] mb-2">                  <span className="font-semibold text-[#010507]">Task: </span>                  {d.task}                </div>                <div className="text-sm text-[#010507] whitespace-pre-wrap bg-white rounded-lg p-2.5 border border-[#E9E9EF]">                  {d.result}                </div>              </div>            );          })        )}      </div>    </div>  );}

The result: as the supervisor fans work out to its sub-agents, the log grows in real time, giving the user visibility into a process that would otherwise be a long opaque spinner.

## Related#

  * **[Shared State](https://docs.copilotkit.ai/strands-typescript/shared-state)** — the channel that makes the delegation log live.
  * **[State streaming](https://docs.copilotkit.ai/strands-typescript/shared-state/streaming)** — stream _individual_ sub-agent outputs token-by-token inside each log entry.


