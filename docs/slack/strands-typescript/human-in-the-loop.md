---
url: https://docs.copilotkit.ai/slack/strands-typescript/human-in-the-loop/
title: HITL Overview
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:39:49.207736+00:00
---

# HITL Overview

> Source: https://docs.copilotkit.ai/slack/strands-typescript/human-in-the-loop/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

ChannelSlackAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Getting Started

[Overview](https://docs.copilotkit.ai/slack/strands-typescript)[Configure the Channel in Intelligence](https://docs.copilotkit.ai/slack/strands-typescript/intelligence)[Connect and run your agent](https://docs.copilotkit.ai/slack/strands-typescript/connect)

Build

[Tools and context](https://docs.copilotkit.ai/slack/strands-typescript/tools)[Identity and Memory](https://docs.copilotkit.ai/slack/strands-typescript/identity-and-memory)[Rich messages and components](https://docs.copilotkit.ai/slack/strands-typescript/rich-messages)[Interactive messages and approvals](https://docs.copilotkit.ai/slack/strands-typescript/interactive)[Commands and reactions](https://docs.copilotkit.ai/slack/strands-typescript/commands-and-reactions)[Files and multimodal input](https://docs.copilotkit.ai/slack/strands-typescript/files-and-multimodality)[Threads and state](https://docs.copilotkit.ai/slack/strands-typescript/threads-and-state)

Production

[Persistence and scaling](https://docs.copilotkit.ai/slack/strands-typescript/persistence-and-scaling)[History and transcripts](https://docs.copilotkit.ai/slack/strands-typescript/history-and-transcripts)[Deploy and operate](https://docs.copilotkit.ai/slack/strands-typescript/deploy-and-operate)[API reference](https://docs.copilotkit.ai/reference/channels)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[AWS Strands (TypeScript)](https://docs.copilotkit.ai/slack/strands-typescript)

# HITL Overview

Allow your agent and users to collaborate on complex tasks.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.ts

page.tsx

time-picker-card.tsx

route.ts
    
    
    /** * Agent factories for the Strands TypeScript showcase backend. * * `buildShowcaseAgent` is the single shared agent that serves the vast * majority of demos (the frontend differentiates each demo via * useFrontendTool / useRenderTool / useHumanInTheLoop / useAgentContext). * It mirrors the Python sibling's `build_showcase_agent` minus A2UI. * * The tool-free specialized agents (voice, byoc-hashbrown, byoc-json-render) * are mounted on dedicated sub-paths by `server.ts`. */import { readFileSync } from "node:fs";import { dirname, join } from "node:path";import { fileURLToPath } from "node:url";import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import type { RunAgentInput } from "@ag-ui/core";import { StrandsAgent } from "@ag-ui/aws-strands";import type { StrandsAgentConfig } from "@ag-ui/aws-strands";import {  A2UI_OPERATIONS_KEY,  createSurface,  updateComponents,  updateDataModel,} from "@ag-ui/a2ui-toolkit";import { createModel } from "./model-factory";import { SHOWCASE_TOOLS } from "./tools";import {  withStateContext,  salesStateFromArgs,  notesStateFromArgs,  stepsStateFromArgs,  documentStateFromArgs,  makeSubagentStateFromResult,} from "./state";import {  SYSTEM_PROMPT,  VOICE_SYSTEM_PROMPT,  BYOC_HASHBROWN_SYSTEM_PROMPT,  BYOC_JSON_RENDER_SYSTEM_PROMPT,} from "./prompts";export class ShowcaseStrandsAgent extends StrandsAgent {  override async *run(inputData: RunAgentInput) {    // The adapter exposes context during model calls and restores history afterward.    yield* super.run(withStateContext(inputData));  }}export async function buildShowcaseAgent(): Promise<StrandsAgent> {  const config: StrandsAgentConfig = {    toolBehaviors: {      // The tool keeps the sales pipeline in appState; this snapshot, built      // from the args, only carries it to the UI.      manage_sales_todos: {        skipMessagesSnapshot: true,        stateFromArgs: salesStateFromArgs,      },      // Shared State (Read + Write) — notes panel.      set_notes: { stateFromArgs: notesStateFromArgs },      // gen-ui-agent — live progress card driven by set_steps transitions.      set_steps: { stateFromArgs: stepsStateFromArgs },      // shared-state-streaming — stream the document string into state.      write_document: { stateFromArgs: documentStateFromArgs },      // Sub-agents — append a delegation entry carrying the actual output.      research_agent: {        stateFromResult: makeSubagentStateFromResult("research_agent"),      },      writing_agent: {        stateFromResult: makeSubagentStateFromResult("writing_agent"),      },      critique_agent: {        stateFromResult: makeSubagentStateFromResult("critique_agent"),      },    },  };  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: SYSTEM_PROMPT,    tools: SHOWCASE_TOOLS,  });  return new ShowcaseStrandsAgent({    agent: strandsAgent,    name: "strands_agent",    description:      "A polished CopilotKit demo assistant: chat, tools, shared state, HITL, sub-agents.",    config,  });}/** Tool-free agent for the voice demo (transcription + basic chat). */export async function buildVoiceAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: VOICE_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "voice_agent",    description: "Simple assistant for the voice demo — no tools.",  });}/** Tool-free hashbrown UI-kit envelope generator (declarative-hashbrown). */export async function buildByocHashbrownAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: BYOC_HASHBROWN_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "byoc_hashbrown",    description:      "Hashbrown UI-kit envelope generator for the declarative-hashbrown demo.",  });}/** Tool-free json-render flat-spec generator (declarative-json-render). */export async function buildByocJsonRenderAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    model: await createModel(),    systemPrompt: BYOC_JSON_RENDER_SYSTEM_PROMPT,    tools: [],  });  return new StrandsAgent({    agent: strandsAgent,    name: "byoc_json_render",    description:      "json-render flat-spec generator for the declarative-json-render demo.",  });}// ---------------------------------------------------------------------------// A2UI Fixed Schema (declarative-generative-ui) — dedicated backend tool.// ---------------------------------------------------------------------------//// Unlike the dynamic A2UI demo (which relies on the adapter auto-injecting a// `generate_a2ui` tool to *generate* a surface), the fixed-schema demo wires a// single plain backend tool — `display_flight` — that returns the// `a2ui_operations` envelope (createSurface -> updateComponents ->// updateDataModel). The component tree is fixed and authored ahead of time// (./a2ui_schemas/flight_schema.json); only the *data* changes per call. The// runtime A2UIMiddleware detects the envelope in the tool result and paints.// No sub-agent, no generation, no `generate_a2ui` injection.//// The schema's component names + data paths must match the showcase frontend// catalog at src/app/demos/a2ui-fixed-schema/a2ui/{definitions,renderers,// catalog}.ts — catalog id `copilotkit://flight-fixed-catalog`. This mirrors// the canonical langgraph-python demo (src/agents/a2ui_fixed.py).const _A2UI_DIR = dirname(fileURLToPath(import.meta.url));const A2UI_FIXED_CATALOG_ID = "copilotkit://flight-fixed-catalog";const A2UI_FIXED_SURFACE_ID = "flight-fixed-schema";// Fixed, pre-authored component layout. Loaded from JSON so it can be authored// and reviewed independently of the agent code.const FLIGHT_SCHEMA: Array<Record<string, unknown>> = JSON.parse(  readFileSync(join(_A2UI_DIR, "a2ui_schemas", "flight_schema.json"), "utf-8"),);const A2UI_FIXED_SYSTEM_PROMPT =  "You help users find flights. When asked about a flight, call " +  "`display_flight` exactly ONCE with origin, destination, airline, and " +  'price. Use short airport codes (e.g. "SFO", "JFK") for ' +  'origin/destination and a price string like "$289". The tool\'s return ' +  "value is an A2UI surface descriptor — the flight card is already rendered " +  "to the user; do NOT call `display_flight` again for the same trip and do " +  "NOT repeat the flight details in text. After the tool returns, reply with " +  "one short confirmation sentence and stop.";/** * Dedicated agent for the A2UI fixed-schema demo. Returns the envelope as a * plain OBJECT (not a JSON string): the Strands TS SDK wraps an object * tool-return in a `json` content block the adapter reads and re-stringifies * into the TOOL_CALL_RESULT the client A2UIMiddleware scans for * `a2ui_operations`. (A bare string return lands in no content block and the * result comes through empty — unlike the Python SDK, which wraps strings.) */export async function buildA2uiFixedSchemaAgent(): Promise<StrandsAgent> {  const displayFlight = tool({    name: "display_flight",    description:      "Show a flight card for the given trip. Use short airport codes " +      '(e.g. "SFO", "JFK") for origin/destination and a price string like ' +      '"$289". After this tool returns, the flight card is already rendered ' +      "to the user via the A2UI surface — do NOT call it again for the same " +      "flight; reply with one short confirmation sentence and stop.",    inputSchema: z.object({      origin: z.string().describe('Origin airport code, e.g. "SFO".'),      destination: z.string().describe('Destination airport code, e.g. "JFK".'),      airline: z.string().describe('Airline name, e.g. "United".'),      price: z.string().describe('Price string, e.g. "$289".'),    }),    callback: ({ origin, destination, airline, price }) => ({      [A2UI_OPERATIONS_KEY]: [        createSurface(A2UI_FIXED_SURFACE_ID, A2UI_FIXED_CATALOG_ID),        updateComponents(A2UI_FIXED_SURFACE_ID, FLIGHT_SCHEMA),        updateDataModel(A2UI_FIXED_SURFACE_ID, {          origin,          destination,          airline,          price,        }),      ],    }),  });  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_FIXED_SYSTEM_PROMPT,    tools: [displayFlight],  });  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_fixed_schema",    description:      "A2UI surface from a fixed, pre-authored schema (direct backend tool)",  });}// ---------------------------------------------------------------------------// A2UI Dynamic Schema (declarative-gen-ui) — adapter auto-injects generate_a2ui.// ---------------------------------------------------------------------------//// Unlike the fixed-schema demo (which wires a `display_flight` tool returning a// pre-authored envelope), the dynamic demo lets the agent *generate* the// surface layout on the fly. The Next.js route// (app/api/copilotkit-declarative-gen-ui/route.ts) sets// `a2ui: { injectA2UITool: true, defaultCatalogId: "declarative-gen-ui-catalog" }`;// the runtime forwards the flag, the Strands adapter auto-injects a// `generate_a2ui` tool and drives a secondary render planner. The// `config.a2ui` block below supplies the catalog id stamped into generated// surfaces and the composition guide that teaches the planner the page's// catalog. Mirrors the ag-ui dynamic-schema reference example.//// The compositionGuide MUST describe the catalog the page registers at// src/app/demos/declarative-gen-ui/a2ui/{definitions,renderers,catalog}.ts// (catalog id `declarative-gen-ui-catalog`): Card / StatusBadge / Metric /// InfoRow / PrimaryButton / PieChart / BarChart / DataTable, composed inside// the basic catalog's Row / Column / Text (`includeBasicCatalog: true`).//// Grounding dataset + composition rules are kept in spirit with the frontend// `sales-context.ts` (SALES_DATASET + COMPOSITION_RULES) the page registers via// `useAgentContext`. The frontend context steers the PRIMARY agent; this// compositionGuide is the channel the adapter feeds to the secondary// `render_a2ui` planner (it gets `guidelines`, not the frontend App Context),// so the planner is self-contained.const A2UI_DYNAMIC_CATALOG_ID = "declarative-gen-ui-catalog";const A2UI_DYNAMIC_SALES_DATASET = `Vantage Threads (fictional B2B apparel company) — Q2 sales data. Ground every visual in these numbers; invent only plausible details consistent with them.- Quarterly revenue: $4.2M (up 12% QoQ). New customers: 186 (up 8%). Win rate: 31% (down 2pts). Avg deal size: $22.6k (up 5%).- Revenue by region: North America $1.9M, EMEA $1.3M, APAC $720k, LATAM $280k.- Monthly revenue: Jan $1.21M, Feb $1.34M, Mar $1.65M, Apr $1.38M, May $1.42M, Jun $1.40M.- Reps (vs quota): Dana Whitfield 124%, Marcus Lee 108%, Priya Sharma 97%, Tom Okafor 88%, Elena Vasquez 71%.- At-risk: total $615k ARR across 3 accounts — Northwind Retail ($340k renewal, no contact 6 weeks; severity high), Cascadia Outfitters ($180k, champion left; severity medium), Atlas Goods ($95k, stalled legal review; severity medium).- Biggest account: Meridian Apparel Group — owner Dana Whitfield, region North America, ARR $612k, renewal Sep 30, last contact 3 days ago, health green, 4 open opportunities worth $210k.- Meridian revenue by product line: Outerwear $260k, Footwear $180k, Accessories $112k, Custom $60k.`;const A2UI_DYNAMIC_COMPOSITION_RULES = `Use ONLY these exact component names (the registered catalog — any other name fails to render): Card, Column, Row, Text, Metric, PieChart, BarChart, DataTable, StatusBadge, InfoRow, PrimaryButton. The single-value KPI tile component is named exactly "Metric" (NOT "MetricTile" or "MetricCard").Pick A2UI components by the shape of the question — never ask which chart the user wants:1. Overall snapshot / "sales dashboard" → a Column (gap 16) whose first child is a Row (gap 16) of 4 Metric components (each with trend + trendValue), followed by a Row with a PieChart (revenue by region) next to a BarChart (monthly revenue, all six months Jan-Jun). Do NOT wrap the dashboard in a surrounding Card — the charts carry their own card chrome. Do NOT use StatusBadge, DataTable, or InfoRow here.2. Rep / team performance → a Column (gap 16) with a Card containing a DataTable (columns: rep, attainment, pipeline) next to or above a BarChart of quota attainment % per rep — no StatusBadge or InfoRow.3. Risk / health checks → a Column (gap 16): first a Row (gap 16) of 3 Metric components (ARR at risk $615k trend down, accounts at risk 3, biggest exposure Northwind $340k), then a Row (gap 16) with one compact Card per at-risk account (title = account name, subtitle = ARR at stake) containing a StatusBadge (error for high severity, warning otherwise) above a one-line Text with the reason and the recommended next action — no DataTable or InfoRow.4. Single account/entity details → a Row (gap 16) with a Card of InfoRow facts (owner, region, ARR, renewal date, last contact) next to a PieChart of that account's revenue by product line — no DataTable or StatusBadge.5. Part-of-whole follow-ups → PieChart; trends or comparisons over time/categories → BarChart.Compose generously — a dashboard should feel like a real analytics product, not a single widget.`;const A2UI_DYNAMIC_COMPOSITION_GUIDE = `${A2UI_DYNAMIC_SALES_DATASET}\n\n${A2UI_DYNAMIC_COMPOSITION_RULES}`;// Mirrors the langgraph-python demo's a2ui_dynamic.py SYSTEM_PROMPT.const A2UI_DYNAMIC_SYSTEM_PROMPT =  "You are the embedded sales analyst for Vantage Threads, the fictional " +  "B2B apparel company described in your App Context. Answer every " +  "business question by calling `generate_a2ui` to draw a rich visual " +  "surface, and keep the chat reply to one short sentence.\n\n" +  "Ground every number in the sales dataset from App Context — never " +  "invent figures that contradict it. Follow the dashboard composition " +  "rules from App Context when choosing components: pick the component " +  "by the shape of the question (snapshot → composed KPI dashboard with " +  "charts; team performance → table; risk → status badges; single " +  "account → info rows; part-of-whole → pie; trend/comparison → bar). " +  "Never ask the user which chart they want. `generate_a2ui` takes no " +  "arguments and handles the rendering automatically. Compose " +  "generously — a dashboard should feel like a real analytics product, " +  "not a single widget.";/** * Dedicated agent for the A2UI dynamic-schema demo. Wires NO `generate_a2ui` * tool — the runtime's `injectA2UITool: true` makes the adapter auto-inject it * and drive a secondary render planner to GENERATE the surface. */export async function buildA2uiDynamicAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_DYNAMIC_SYSTEM_PROMPT,  });  const config: StrandsAgentConfig = {    a2ui: {      defaultCatalogId: A2UI_DYNAMIC_CATALOG_ID,      guidelines: { compositionGuide: A2UI_DYNAMIC_COMPOSITION_GUIDE },    },  };  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_dynamic_schema",    description:      "Dynamic A2UI surfaces generated on the fly (auto-injected tool)",    config,  });}// ---------------------------------------------------------------------------// A2UI Error Recovery (a2ui-recovery) — adapter auto-injects + runs recovery.// ---------------------------------------------------------------------------//// Same auto-injected dynamic-schema setup as buildA2uiDynamicAgent, but the// aimock fixtures force the inner render_a2ui to emit free-form/sloppy args// (heal pill) or a structurally-invalid surface on every attempt (exhaust// pill). The Strands adapter runs the toolkit validate->retry recovery loop on// its auto-inject path (default 3 attempts) and returns the// a2ui_recovery_exhausted hard-fail envelope when the cap is hit — so this// agent wires NO tool, unlike the langgraph/ADK siblings (which own the tool// explicitly via getA2UITools + injectA2UITool:false). Mirrors the ag-ui dojo// aws-strands recovery example./** * Dedicated agent for the A2UI error-recovery demo. Wires NO `generate_a2ui` * tool — the runtime's `injectA2UITool: true` makes the adapter auto-inject it, * drive the secondary render planner, and run the recovery loop. */export async function buildA2uiRecoveryAgent(): Promise<StrandsAgent> {  const strandsAgent = new Agent({    // Chat Completions API: the Responses adapter buffers tool-call argument    // deltas, which would defeat A2UI's progressive surface streaming.    model: await createModel({ openaiApi: "chat" }),    systemPrompt: A2UI_DYNAMIC_SYSTEM_PROMPT,  });  const config: StrandsAgentConfig = {    a2ui: {      defaultCatalogId: A2UI_DYNAMIC_CATALOG_ID,      guidelines: { compositionGuide: A2UI_DYNAMIC_COMPOSITION_GUIDE },    },  };  return new StrandsAgent({    agent: strandsAgent,    name: "a2ui_recovery",    description:      "Dynamic A2UI with automatic error recovery (auto-injected tool)",    config,  });}

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/slack/strands-typescript/inspector).

## What is this?#

Human-in-the-loop (HITL) lets an agent pause mid-run to collect input, confirmation, or a choice from the user, then resume with that answer folded back into its reasoning. It's what turns an autonomous workflow into a collaborative one: the agent keeps its context, the user keeps the steering wheel.

## When should I use this?#

Use HITL when you need:

  * **Quality control** — a human gate at high-stakes decision points
  * **Edge cases** — graceful fallbacks when the agent's confidence is low
  * **Expert input** — lean on the user for domain knowledge the model lacks
  * **Reliability** — a more robust loop for real-world, production traffic



## Two patterns for HITL in CopilotKit#

### Pause a tool with Strands' native interrupt

AWS Strands ships a first-class [interrupt primitive](https://strandsagents.com/docs/user-guide/concepts/interrupts/). A tool's callback receives a context whose `interrupt({ name, reason })` call halts the agent loop and hands `reason` to the client as the interrupt payload. The AG-UI adapter finishes the run with `RUN_FINISHED` carrying `outcome.type === "interrupt"`.

src/agent/interrupt-agent.ts
    
    
    export const scheduleMeeting = tool({
      name: "schedule_meeting",
      description:
        "Ask the user to pick a meeting time, then confirm what was scheduled.",
      inputSchema: z.object({
        topic: z.string().describe("Short description of the meeting purpose."),
        attendee: z.string().optional().describe("Who the meeting is with."),
      }),
      callback: ({ topic, attendee }, context) => {
        // Typed optional by the SDK, so this is checked rather than asserted: with
        // no context there is nothing to pause on, and pretending otherwise would
        // schedule a meeting the user never saw.
        if (!context) {
          throw new Error("schedule_meeting needs a tool context to pause on");
        }
    
        // `attendee` is optional and the reason has to be JSON, which has no
        // `undefined`, so it is omitted rather than sent as undefined.
        const answer = context.interrupt<ResumeEnvelope>({
          name: "schedule_meeting",
          reason: attendee === undefined ? { topic } : { topic, attendee },
        });
    
        // Three cancel shapes reach here: each bridge's own sentinel for a
        // cancelled resume entry, and the picker's Cancel button, which resolves
        // with a `cancelled` flag inside the payload.
        const { choice, cancelled } = readResume(answer);
        if (cancelled) {
          return `User cancelled. Meeting NOT scheduled: ${topic}`;
        }
    
        const label = choice.chosen_label || choice.chosen_time;
        return label
          ? `Meeting scheduled for ${label}: ${topic}`
          : `User did not pick a time. Meeting NOT scheduled: ${topic}`;
      },
    });

How the answer reaches the tool depends on the adapter version. The pinned `@ag-ui/aws-strands` 0.2.3 hands the client's payload through untouched and signals a cancel as `{ status: "cancelled" }`; the Python adapter wraps an answer as `{ response: ... }` and cancels with `{ cancelled: true }`. Read both shapes, or a picked slot comes back to the model as though the user never picked one.

### Keep the pausing tool off a client-executed name

`useHumanInTheLoop` registers its tool on the FRONTEND, so a name used there cannot also be a pausing backend tool. This showcase mounts a dedicated interrupt agent and points the interrupt demos' agent names at it, leaving `schedule_meeting` on the shared agent free for the frontend-tool flow.

### Resume in the same process, or across a restart

Pause and resume on the same running process need no extra wiring. For a resume that survives a restart, give the agent a Strands `SessionManager` through `StrandsAgentConfig.sessionManagerProvider`; the adapter persists its interrupt checkpoint into that session.

CopilotKit ships two complementary ways to pause an agent turn and ask the human something. They look similar from the outside (the chat pauses, a custom component appears, the user answers, the run resumes) but they're wired differently on the backend, and each has its own niche.

Pattern| Who decides to pause?| Backend surface  
---|---|---  
`useHumanInTheLoop`| The **LLM** , by calling a registered client-side tool| A frontend-only tool description (Zod schema + `render`)  
`useInterrupt`| The **graph** , by calling `interrupt(...)` during a node| A server-side `interrupt()` call in your LangGraph agent  
  
**Pick`useHumanInTheLoop`** when the pause is an _agent-initiated_ decision — the model chose to ask the user — and you want the picker UI inlined into the normal tool-call flow.

**Pick`useInterrupt`** when the pause is a _graph-enforced_ checkpoint — the code path deterministically requires a human answer — and you want `langgraph.interrupt()` as the server-side contract.

## Pattern 1 — `useHumanInTheLoop` (tool-based)#

The agent registers a HITL tool on the client with `useHumanInTheLoop`. When the LLM calls that tool, CopilotKit routes the call through your `render` function, which shows a custom component and calls `respond` with the user's answer. The agent sees the answer as the tool result and continues from there.

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];export default function HitlInChatDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="hitl-in-chat">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useConfigureSuggestions({    suggestions: [      {        title: "Book a call with sales",        message:          "Please book an intro call with the sales team to discuss pricing.",      },      {        title: "Schedule a 1:1 with Alice",        message: "Schedule a 1:1 with Alice next week to review Q2 goals.",      },    ],    available: "always",  });  useHumanInTheLoop({    agentId: "hitl-in-chat",    name: "book_call",    description:      "Use this tool for ANY request to schedule, book, set up, arrange, or organize a call, meeting, 1:1, intro, sync, or chat — including phrasings like 'schedule a 1:1 with Alice', 'book a call', or 'set up a meeting'. It presents the user an in-chat time picker with candidate slots and returns their chosen time. ALWAYS prefer this tool over `schedule_meeting` or any other scheduling tool when the user wants to pick a meeting time in this conversation.",    parameters: z.object({      topic: z        .string()        .describe("What the call is about (e.g. 'Intro with sales')"),      attendee: z        .string()        .describe("Who the call is with (e.g. 'Alice from Sales')"),    }),    render: ({ args, status, respond }: any) => (      <TimePickerCard        topic={args?.topic ?? "a call"}        attendee={args?.attendee}        slots={DEFAULT_SLOTS}        status={status}        onSubmit={(result) => respond?.(result)}      />    ),  });

The picker UI is fed a static list of candidate slots — this is just data the demo page owns, so you can swap in real availability, a calendar API, or anything else:

page.tsx
    
    
    import React from "react";import {  CopilotKit,  CopilotChat,  useHumanInTheLoop,  useConfigureSuggestions,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { TimeSlot } from "./time-picker-card";import { TimePickerCard } from "./time-picker-card";const DEFAULT_SLOTS: TimeSlot[] = [  { label: "Tomorrow 10:00 AM", iso: "2026-04-19T10:00:00-07:00" },  { label: "Tomorrow 2:00 PM", iso: "2026-04-19T14:00:00-07:00" },  { label: "Monday 9:00 AM", iso: "2026-04-21T09:00:00-07:00" },  { label: "Monday 3:30 PM", iso: "2026-04-21T15:30:00-07:00" },];

## Pattern 2 — `useInterrupt` (graph-paused)#

With LangGraph's `interrupt()` the pause is enforced by the graph itself: a node calls `interrupt({...})`, the run suspends, the client receives the payload, renders a UI, and resumes the run with the user's answer. CopilotKit's `useInterrupt` hook is the render contract.

See the [`useInterrupt` deep dive](https://docs.copilotkit.ai/slack/strands-typescript/human-in-the-loop/useInterrupt) for the full walkthrough, including the backend tool and render-prop wiring.

DemoCode

interrupt-agent.ts

page.tsx

time-picker-card.tsx

route.ts
    
    
    /** * Dedicated Strands agent for the two interrupt demos. * * Mirrors the Python sibling's `agents/interrupt_agent.py`. * * `schedule_meeting` pauses itself through Strands' native interrupt system: * `context.interrupt(...)` halts the agent loop and the AG-UI bridge finishes * the run with `RUN_FINISHED` carrying `outcome.type === "interrupt"`. The * frontend renders the time picker from the interrupt payload, and resuming on * the same `threadId` returns the user's choice to that same `interrupt()` * call, so the tool body continues where it left off. * * How the resume payload arrives depends on the bridge, so the tool normalises * both shapes (see `readResume`): the pinned `@ag-ui/aws-strands` 0.2.3 passes * the client's payload through and cancels with `{ status: "cancelled" }`, * while the Python bridge wraps a resolved answer as `{ response: ... }` and * cancels with `{ cancelled: true }`. * * This is a dedicated agent rather than a tool on the shared showcase agent * because the shared agent already owns a `schedule_meeting` that answers * straight away. One tool name cannot both answer immediately for the other * demos and pause for these two, so the pausing version gets its own mount. * * Pause and resume happen in the same process here, so no `SessionManager` is * needed. Durable resume across a restart requires one. * * Docs: https://strandsagents.com/docs/user-guide/concepts/interrupts/ */import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import { StrandsAgent } from "@ag-ui/aws-strands";import { createModel } from "./model-factory";/** What the picker sends back. */interface MeetingChoice {  chosen_time?: string;  chosen_label?: string;  cancelled?: boolean;  status?: string;}/** * What the bridge hands a resumed tool. Two shapes are in circulation: * * - `@ag-ui/aws-strands` 0.2.3 (the pinned release) passes the client's payload *   through untouched, and signals a cancel as `{ status: "cancelled" }`. * - `ag_ui_strands` (Python) wraps it as `{ response: payload }`, and signals a *   cancel as `{ cancelled: true }`. * * Reading only one of them silently mis-reports the other: a resolved pick * arrives with no recognised answer and the tool tells the model the user never * picked a time. */interface ResumeEnvelope {  /** `null` when the client answered with no payload at all. */  response?: MeetingChoice | null;  cancelled?: boolean;  status?: string;}/** Normalise both envelope shapes to `{ choice, cancelled }`. */export function readResume(  answer: ResumeEnvelope | MeetingChoice | null | undefined,): {  choice: MeetingChoice;  cancelled: boolean;} {  const envelope: ResumeEnvelope =    answer && typeof answer === "object" ? answer : {};  const inner =    "response" in envelope      ? envelope.response      : (answer as MeetingChoice | null | undefined);  const choice: MeetingChoice = inner && typeof inner === "object" ? inner : {};  const cancelled = Boolean(    envelope.cancelled ||    envelope.status === "cancelled" ||    choice.cancelled ||    choice.status === "cancelled",  );  return { choice, cancelled };}export const scheduleMeeting = tool({  name: "schedule_meeting",  description:    "Ask the user to pick a meeting time, then confirm what was scheduled.",  inputSchema: z.object({    topic: z.string().describe("Short description of the meeting purpose."),    attendee: z.string().optional().describe("Who the meeting is with."),  }),  callback: ({ topic, attendee }, context) => {    // Typed optional by the SDK, so this is checked rather than asserted: with    // no context there is nothing to pause on, and pretending otherwise would    // schedule a meeting the user never saw.    if (!context) {      throw new Error("schedule_meeting needs a tool context to pause on");    }    // `attendee` is optional and the reason has to be JSON, which has no    // `undefined`, so it is omitted rather than sent as undefined.    const answer = context.interrupt<ResumeEnvelope>({      name: "schedule_meeting",      reason: attendee === undefined ? { topic } : { topic, attendee },    });    // Three cancel shapes reach here: each bridge's own sentinel for a    // cancelled resume entry, and the picker's Cancel button, which resolves    // with a `cancelled` flag inside the payload.    const { choice, cancelled } = readResume(answer);    if (cancelled) {      return `User cancelled. Meeting NOT scheduled: ${topic}`;    }    const label = choice.chosen_label || choice.chosen_time;    return label      ? `Meeting scheduled for ${label}: ${topic}`      : `User did not pick a time. Meeting NOT scheduled: ${topic}`;  },});const SYSTEM_PROMPT = `You are a scheduling assistant.Whenever the user asks you to book a call or schedule a meeting, you MUST callthe \`schedule_meeting\` tool. Pass a short \`topic\` describing the purpose and,if known, an \`attendee\` describing who the meeting is with.The tool pauses execution and shows the user a time picker. Once it resumes withtheir choice, briefly confirm whether the meeting was scheduled and at whattime, or note that the user cancelled. Do not ask for approval yourself: alwayscall the tool and let the picker handle the decision. Keep responses short andfriendly.Never claim a meeting is scheduled unless the tool result says so.`;/** Build the agent backing gen-ui-interrupt and interrupt-headless. */export async function buildInterruptAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await createModel(),      systemPrompt: SYSTEM_PROMPT,      tools: [scheduleMeeting],    }),    name: "interrupt",    description:      "Strands agent whose scheduling tool pauses natively for the user to pick a time",  });}

## Going headless#

Both patterns above ship with a `render` prop — CopilotKit handles the "when to show the picker" logic for you. If you want to drive interrupt resolution from a custom UI that lives anywhere in the tree (not necessarily inside a chat), see the [headless interrupts guide](https://docs.copilotkit.ai/slack/strands-typescript/human-in-the-loop/headless) — it shows how to compose `useAgent`, `agent.subscribe`, and `copilotkit.runAgent` to build your own `useInterrupt` equivalent.

### On this page

What is this?When should I use this?Two patterns for HITL in CopilotKitPattern 1 — useHumanInTheLoop (tool-based)Pattern 2 — useInterrupt (graph-paused)Going headless
