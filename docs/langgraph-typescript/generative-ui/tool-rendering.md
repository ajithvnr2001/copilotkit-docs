---
url: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/tool-rendering/
title: Tool Call Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:24.604688+00:00
---

# Tool Call Rendering

> Source: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/tool-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Tool Call Rendering

Generative UIControlled

# Tool Call Rendering

Render your agent's tool calls with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

tool-rendering.ts

page.tsx

weather-card.tsx

flight-list-card.tsx

route.ts
    
    
    /** * Tool Rendering agent -- TypeScript port of tool_rendering_agent.py. * * Backs the tool-rendering demos: *   - tool-rendering-default-catchall  (no frontend renderers) *   - tool-rendering-custom-catchall   (wildcard renderer on frontend) *   - tool-rendering                   (per-tool + catch-all on frontend) * * All cells share this backend -- they differ only in how the frontend * renders the same tool calls. */import { makeChatOpenAI } from "./openai-headers";import { z } from "zod";import type { RunnableConfig } from "@langchain/core/runnables";import { tool } from "@langchain/core/tools";import { ToolNode } from "@langchain/langgraph/prebuilt";import { AIMessage, SystemMessage } from "@langchain/core/messages";import {  Annotation,  MemorySaver,  START,  StateGraph,} from "@langchain/langgraph";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";// ---------------------------------------------------------------------------// 1. Agent state -- extends CopilotKit state annotation// ---------------------------------------------------------------------------const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,});export type AgentState = typeof AgentStateAnnotation.State;// ---------------------------------------------------------------------------// 2. System prompt -- matches LGP exactly// ---------------------------------------------------------------------------const SYSTEM_PROMPT =  "You are a travel & lifestyle concierge. Use the mock tools for " +  "weather, flights, stock prices, or d20 rolls when the user asks; " +  "otherwise reply in plain text. For flights, default origin to 'SFO' " +  "if the user only names a destination. Call multiple tools in one " +  "turn if asked. After tools return, summarize in one short sentence. " +  "Never fabricate data a tool could provide.";// ---------------------------------------------------------------------------// 3. Tools -- aligned with LGP tool definitions// ---------------------------------------------------------------------------const getWeather = tool(  async ({ location }) => ({    city: location,    temperature: 68,    humidity: 55,    wind_speed: 10,    conditions: "Sunny",  }),  {    name: "get_weather",    description: "Get the current weather for a given location.",    schema: z.object({      location: z.string().describe("City name"),    }),  },);const searchFlights = tool(  async ({ origin, destination }) => ({    origin,    destination,    flights: [      {        airline: "United",        flight: "UA231",        depart: "08:15",        arrive: "16:45",        price_usd: 348,      },      {        airline: "Delta",        flight: "DL412",        depart: "11:20",        arrive: "19:55",        price_usd: 312,      },      {        airline: "JetBlue",        flight: "B6722",        depart: "17:05",        arrive: "01:30",        price_usd: 289,      },    ],  }),  {    name: "search_flights",    description:      "Search mock flights from an origin airport to a destination airport.",    schema: z.object({      origin: z.string().describe("Origin airport code"),      destination: z.string().describe("Destination airport code"),    }),  },);const getStockPrice = tool(  async ({ ticker, price_usd, change_pct }) => {    const randInt = (lo: number, hi: number) =>      Math.floor(Math.random() * (hi - lo + 1)) + lo;    const sign = Math.random() < 0.5 ? -1 : 1;    return {      ticker: ticker.toUpperCase(),      price_usd:        price_usd != null          ? Math.round(price_usd * 100) / 100          : Math.round((100 + randInt(0, 400) + randInt(0, 99) / 100) * 100) /            100,      change_pct:        change_pct != null          ? Math.round(change_pct * 100) / 100          : Math.round(sign * (randInt(0, 300) / 100) * 100) / 100,    };  },  {    name: "get_stock_price",    description:      "Get a mock current price for a stock ticker.\n\n" +      "The optional `price_usd` and `change_pct` arguments let the LLM (or " +      "aimock fixture) script a deterministic ticker quote for testing -- " +      "when supplied, the tool echoes them back verbatim. When omitted (or " +      "null), the tool returns mock random values. Mirrors the " +      "deterministic-`value` pattern on `roll_d20`.",    schema: z.object({      ticker: z.string().describe("Stock ticker symbol"),      price_usd: z        .number()        .optional()        .describe(          "Deterministic price override for testing (echoed back verbatim)",        ),      change_pct: z        .number()        .optional()        .describe(          "Deterministic change-pct override for testing (echoed back verbatim)",        ),    }),  },);const rollD20 = tool(  async ({ value }) => {    const rolled =      typeof value === "number" && value >= 1 && value <= 20        ? value        : Math.floor(Math.random() * 20) + 1;    return { sides: 20, value: rolled, result: rolled };  },  {    name: "roll_d20",    description: "Roll a 20-sided die.",    schema: z.object({      value: z        .number()        .int()        .optional()        .describe(          "Deterministic override for the roll result (used by test fixtures)",        ),    }),  },);const tools = [getWeather, searchFlights, getStockPrice, rollD20];// ---------------------------------------------------------------------------// 4. Chat node -- binds backend + frontend tools, invokes the model// ---------------------------------------------------------------------------async function chatNode(state: AgentState, config: RunnableConfig) {  const model = makeChatOpenAI(config, { model: "gpt-5.4" });  const modelWithTools = model.bindTools!([    ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),    ...tools,  ]);  const systemMessage = new SystemMessage({ content: SYSTEM_PROMPT });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    config,  );  // Normalize tool calls that streamed in as `additional_kwargs.tool_calls`  // but failed to promote to the parsed top-level `tool_calls`.  //  // When the model returns BOTH assistant content AND a tool call in one  // message (as the tool-rendering fixtures do — "Looking up the weather…"  // + get_weather), langchain-js's streamed-chunk reassembly can leave the  // fully-formed tool call only under `additional_kwargs.tool_calls` while  // the top-level `tool_calls` stays empty (the intermediate chunks surface  // as `invalid_tool_calls` with "Malformed args" during accumulation), and  // the merged result is a bare "generic" message rather than an AIMessage.  // `shouldContinue`, `ToolNode`, and the AG-UI TOOL_CALL_* event emitter all  // key off a proper AIMessage with top-level `tool_calls`, so the unparsed  // result silently drops the tool call: the graph ends at chat_node (or  // ToolNode rejects the non-AIMessage), the tool never runs, and the  // frontend renders no card. LGP-python's `create_agent` parses the same  // fixture response correctly, so this restores TS↔Python parity.  return { messages: normalizeAssistantMessage(response) };}/** * Ensure the chat model's response is a well-formed `AIMessage` whose tool * calls live in the top-level `tool_calls` array. When langchain-js's * streamed reassembly leaves tool calls only under * `additional_kwargs.tool_calls` (and/or produces a non-AIMessage), rebuild * a clean `AIMessage` that preserves the content and promotes those tool * calls. A no-op passthrough when the response already parses correctly. */function normalizeAssistantMessage(response: AIMessage): AIMessage {  const alreadyHasToolCalls =    Array.isArray(response.tool_calls) && response.tool_calls.length > 0;  const isAIMessage = response instanceof AIMessage;  if (alreadyHasToolCalls && isAIMessage) return response;  const rawToolCalls = (    response.additional_kwargs as { tool_calls?: unknown } | undefined  )?.tool_calls;  const parsed: NonNullable<AIMessage["tool_calls"]> = [];  if (Array.isArray(rawToolCalls)) {    for (const raw of rawToolCalls) {      const fn = (raw as { function?: { name?: string; arguments?: string } })        ?.function;      const id = (raw as { id?: string })?.id;      const name = fn?.name;      if (!name) continue;      let args: Record<string, unknown> = {};      if (typeof fn?.arguments === "string" && fn.arguments.length > 0) {        try {          args = JSON.parse(fn.arguments);        } catch {          // Leave args empty when the accumulated JSON is unparseable          // rather than dropping the whole tool call.          args = {};        }      }      parsed.push({ id, name, args, type: "tool_call" });    }  }  // Nothing to reconcile and it's already an AIMessage — leave it untouched.  if (parsed.length === 0 && isAIMessage) return response;  return new AIMessage({    id: response.id,    content: response.content ?? "",    tool_calls: parsed.length > 0 ? parsed : response.tool_calls,    additional_kwargs: response.additional_kwargs,    response_metadata: response.response_metadata,  });}// ---------------------------------------------------------------------------// 5. Routing -- send tool calls to tool_node unless they're CopilotKit//    frontend actions.// ---------------------------------------------------------------------------function shouldContinue({ messages, copilotkit }: AgentState) {  const lastMessage = messages[messages.length - 1] as AIMessage;  if (lastMessage.tool_calls?.length) {    const actions = copilotkit?.actions;    const toolCallName = lastMessage.tool_calls![0].name;    if (!actions || actions.every((action) => action.name !== toolCallName)) {      return "tool_node";    }  }  return "__end__";}// ---------------------------------------------------------------------------// 6. Compile the graph// ---------------------------------------------------------------------------const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNode)  .addNode("tool_node", new ToolNode(tools))  .addEdge(START, "chat_node")  .addEdge("tool_node", "chat_node")  .addConditionalEdges("chat_node", shouldContinue as any);const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

## What is this?#

Tools are how an LLM invokes predefined, typically-deterministic functions. Tool rendering lets you decide how each of those tool calls appears in the chat. Instead of showing raw JSON, you register a React component that draws a branded card for the call (arguments, live status, and the eventual result). This is the **Generative UI** variant CopilotKit calls **tool rendering**.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## When should I use this?#

Render tool calls when you want to:

  * Show users exactly what tools the agent is invoking and with what arguments
  * Display live progress indicators while a tool executes
  * Render rich, polished results once a tool completes
  * Give tool-heavy agents a transparent, on-brand chat experience



## Default tool rendering (zero-config)#

The simplest entry point: call `useDefaultRenderTool()` with no arguments. CopilotKit registers its built-in `DefaultToolCallRenderer` as the `*` wildcard: every tool call renders as a tidy status card (tool name, live **Running → Done** pill, collapsible arguments/result) without you writing any UI.

Without this hook the runtime has no `*` renderer and tool calls are invisible; the user only sees the assistant's final text summary.

page.tsx
    
    
      // Opt in to CopilotKit's built-in default tool-call card. Called with  // no config so the package-provided `DefaultToolCallRenderer` is used  // as the wildcard renderer — this is the "out-of-the-box" UI the cell  // is meant to showcase.  useDefaultRenderTool();

Here's what the built-in status card looks like for each tool call:

DemoCode

page.tsx

tool-rendering.ts

route.ts
    
    
    "use client";// Tool Rendering — DEFAULT CATCH-ALL variant (simplest).//// This cell is the simplest point in the three-way progression. The// backend exposes a handful of mock tools (get_weather, search_flights,// get_stock_price, roll_dice) and the frontend ONLY opts into// CopilotKit's built-in default tool-call card — no per-tool renderers,// no custom wildcard UI.//// `useDefaultRenderTool()` (called with no config) registers the built-// in `DefaultToolCallRenderer` under the `*` wildcard. That renderer// shows the tool name, a live status pill (Running → Done), and a// collapsible "Arguments / Result" section that fills in as the call// progresses. Without this hook the runtime has NO `*` renderer, so// `useRenderToolCall` falls through to `null` and tool calls are// invisible — the user only sees the assistant's final text summary.import React from "react";import {  CopilotKit,  CopilotChat,  useDefaultRenderTool,} from "@copilotkit/react-core/v2";import { useSuggestions } from "./suggestions";export default function ToolRenderingDefaultCatchallDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit"      agent="tool-rendering-default-catchall"    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  // Opt in to CopilotKit's built-in default tool-call card. Called with  // no config so the package-provided `DefaultToolCallRenderer` is used  // as the wildcard renderer — this is the "out-of-the-box" UI the cell  // is meant to showcase.  useDefaultRenderTool();  useSuggestions();  return (    <CopilotChat      agentId="tool-rendering-default-catchall"      className="h-full rounded-2xl"    />  );}

## Custom catch-all#

Once you want on-brand chrome, pass a `render` function to `useDefaultRenderTool`. It's a convenience wrapper around `useRenderTool({ name: "*", ... })`: one wildcard renderer handles every tool call, named or not:

page.tsx
    
    
      // `useDefaultRenderTool` is a convenience wrapper around  // `useRenderTool({ name: "*", ... })` — a single wildcard renderer  // that handles every tool call not claimed by a named renderer.  useDefaultRenderTool(    {      render: ({ name, parameters, status, result }) => (        <CustomCatchallRenderer          name={name}          parameters={parameters}          status={status as CatchallToolStatus}          result={result}        />      ),    },    [],  );

Here's the branded catch-all in action, where every tool call gets the same on-brand card:

DemoCode

page.tsx

custom-catchall-renderer.tsx

tool-rendering.ts

route.ts
    
    
    "use client";// Tool Rendering — CUSTOM CATCH-ALL variant (middle of the progression).//// Same backend tools as `tool-rendering-default-catchall`, but this// cell opts out of CopilotKit's built-in default tool-call UI by// registering a SINGLE custom wildcard renderer via// `useDefaultRenderTool`. The same branded card now paints every tool// call — no per-tool renderers yet.import React from "react";import {  CopilotKit,  CopilotChat,  useDefaultRenderTool,} from "@copilotkit/react-core/v2";import {  CustomCatchallRenderer,  type CatchallToolStatus,} from "./custom-catchall-renderer";import { useSuggestions } from "./suggestions";export default function ToolRenderingCustomCatchallDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit"      agent="tool-rendering-custom-catchall"    >      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  // `useDefaultRenderTool` is a convenience wrapper around  // `useRenderTool({ name: "*", ... })` — a single wildcard renderer  // that handles every tool call not claimed by a named renderer.  useDefaultRenderTool(    {      render: ({ name, parameters, status, result }) => (        <CustomCatchallRenderer          name={name}          parameters={parameters}          status={status as CatchallToolStatus}          result={result}        />      ),    },    [],  );  useSuggestions();  return (    <CopilotChat      agentId="tool-rendering-custom-catchall"      className="h-full rounded-2xl"    />  );}

## Per-tool renderers#

The most expressive path is one renderer per tool name. The primary `tool-rendering` cell wires two: `get_weather` draws a branded `WeatherCard`, `search_flights` draws a `FlightListCard`. Each renderer receives the tool's parsed arguments, a live `status`, and (once the agent returns) the `result`:

### Tool inputs and results are separate#

In `useRenderTool`, `parameters` contains the **inputs** the agent sent to the tool. It does not change into the tool's return value when `status` becomes `"complete"`. The completed output arrives separately as `result`, a string. For a tool that returns JSON, parse that string before reading its fields.

For example, `get_weather` might receive `{ "location": "Paris" }` and return `{ "temperature": 22 }`. Read `parameters.location` for the requested city and the parsed `result.temperature` for the temperature. Adding `temperature` to the renderer's `parameters` schema does not copy it from the result.

If a card says **complete** but still shows placeholder details, check whether those details come from `parameters` instead of the parsed `result`. Completion reports that the tool returned; it does not fill the card's props for you.

The frontend pattern is the same for every backend. This shared, docs-only example includes every component, type, and helper that its renderers use:

components/weather-card.tsx
    
    
    export interface WeatherCardProps {
      loading: boolean;
      location: string;
      temperature?: number;
      humidity?: number;
      windSpeed?: number;
      conditions?: string;
    }
    
    export function WeatherCard({
      loading,
      location,
      temperature,
      humidity,
      windSpeed,
      conditions,
    }: WeatherCardProps) {
      return (
        <article className="rounded-xl border p-4">
          <h3 className="font-semibold">{location || "Weather"}</h3>
          {loading ? (
            <p>Fetching weather...</p>
          ) : (
            <dl>
              <div>
                <dt>Conditions</dt>
                <dd>{conditions ?? "--"}</dd>
              </div>
              <div>
                <dt>Temperature</dt>
                <dd>{temperature ?? "--"}&deg;F</dd>
              </div>
              <div>
                <dt>Humidity</dt>
                <dd>{humidity ?? "--"}%</dd>
              </div>
              <div>
                <dt>Wind</dt>
                <dd>{windSpeed ?? "--"} mph</dd>
              </div>
            </dl>
          )}
        </article>
      );
    }

components/flight-list-card.tsx
    
    
    export interface Flight {
      airline?: string;
      flight?: string;
      depart?: string;
      arrive?: string;
      price_usd?: number;
    }
    
    export interface FlightListCardProps {
      loading: boolean;
      origin: string;
      destination: string;
      flights: Flight[];
    }
    
    export function FlightListCard({
      loading,
      origin,
      destination,
      flights,
    }: FlightListCardProps) {
      return (
        <article className="rounded-xl border p-4">
          <h3 className="font-semibold">
            {origin || "?"} → {destination || "?"}
          </h3>
          {loading ? (
            <p>Searching...</p>
          ) : (
            <ul>
              {flights.map((flight, index) => (
                <li key={`${flight.flight ?? "flight"}-${index}`}>
                  {flight.airline ?? "--"} {flight.flight ?? ""}:{" "}
                  {flight.depart ?? "?"} → {flight.arrive ?? "?"}
                  {flight.price_usd !== undefined ? ` ($${flight.price_usd})` : ""}
                </li>
              ))}
            </ul>
          )}
        </article>
      );
    }

lib/parse-json-result.ts
    
    
    export function parseJsonResult<T>(result: unknown): T {
      if (!result) return {} as T;
    
      try {
        return (typeof result === "string" ? JSON.parse(result) : result) as T;
      } catch {
        return {} as T;
      }
    }

app/tool-renderers.tsx
    
    
    "use client";
    
    import { useRenderTool } from "@copilotkit/react-core/v2";
    import { z } from "zod";
    import { WeatherCard } from "../components/weather-card";
    import { FlightListCard, type Flight } from "../components/flight-list-card";
    import { parseJsonResult } from "../lib/parse-json-result";
    
    interface WeatherResult {
      city?: string;
      temperature?: number;
      humidity?: number;
      wind_speed?: number;
      conditions?: string;
    }
    
    interface FlightSearchResult {
      origin?: string;
      destination?: string;
      flights?: Flight[];
    }
    
    export function ToolRenderers() {
      useRenderTool(
        {
          name: "get_weather",
          parameters: z.object({ location: z.string() }),
          render: ({ parameters, result, status }) => {
            const parsed = parseJsonResult<WeatherResult>(result);
            return (
              <WeatherCard
                loading={status !== "complete"}
                location={parameters?.location ?? parsed.city ?? ""}
                temperature={parsed.temperature}
                humidity={parsed.humidity}
                windSpeed={parsed.wind_speed}
                conditions={parsed.conditions}
              />
            );
          },
        },
        [],
      );
    
      useRenderTool(
        {
          name: "search_flights",
          parameters: z.object({
            origin: z.string(),
            destination: z.string(),
          }),
          render: ({ parameters, result, status }) => {
            const parsed = parseJsonResult<FlightSearchResult>(result);
            return (
              <FlightListCard
                loading={status !== "complete"}
                origin={parameters?.origin ?? parsed.origin ?? ""}
                destination={parameters?.destination ?? parsed.destination ?? ""}
                flights={parsed.flights ?? []}
              />
            );
          },
        },
        [],
      );
    
      return null;
    }

Mount the renderers anywhere beneath the same `CopilotKit` provider as your chat. The renderer component returns no layout of its own; it registers the two named renderers for tool calls in the chat:

app/page.tsx
    
    
    "use client";
    
    import { CopilotChat, CopilotKit } from "@copilotkit/react-core/v2";
    import { ToolRenderers } from "./tool-renderers";
    
    export default function Page() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit" agent="tool-rendering">
          <ToolRenderers />
          <CopilotChat agentId="tool-rendering" />
        </CopilotKit>
      );
    }

The `name` you pass to `useRenderTool` must match the tool name the agent exposes; that's how the runtime routes the call to your component.

Per-tool renderers compose with a catch-all: named renderers claim the "interesting" tools and a wildcard handles everything else. In the primary cell, the same `CustomCatchallRenderer` from above catches `get_stock_price` and `roll_dice`:

page.tsx
    
    
      // Wildcard catch-all for anything that doesn't match a per-tool  // renderer above.  useDefaultRenderTool(    {      render: ({ name, parameters, status, result }) => (        <CustomCatchallRenderer          name={name}          parameters={parameters}          status={status as CatchallToolStatus}          result={result}        />      ),    },    [],  );

## The backend tool definition#

The frontend renderer only sees what the agent sends down. Here's the matching backend definition for `get_weather`: expose a tool named `get_weather`, return structured data, and let the frontend renderer with the same name paint the card.

tool-rendering.ts
    
    
    import { z } from "zod";import type { RunnableConfig } from "@langchain/core/runnables";import { tool } from "@langchain/core/tools";import { ToolNode } from "@langchain/langgraph/prebuilt";import { AIMessage, SystemMessage } from "@langchain/core/messages";import {  Annotation,  MemorySaver,  START,  StateGraph,} from "@langchain/langgraph";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";// ---------------------------------------------------------------------------// 1. Agent state -- extends CopilotKit state annotation// ---------------------------------------------------------------------------const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,});export type AgentState = typeof AgentStateAnnotation.State;// ---------------------------------------------------------------------------// 2. System prompt -- matches LGP exactly// ---------------------------------------------------------------------------const SYSTEM_PROMPT =  "You are a travel & lifestyle concierge. Use the mock tools for " +  "weather, flights, stock prices, or d20 rolls when the user asks; " +  "otherwise reply in plain text. For flights, default origin to 'SFO' " +  "if the user only names a destination. Call multiple tools in one " +  "turn if asked. After tools return, summarize in one short sentence. " +  "Never fabricate data a tool could provide.";// ---------------------------------------------------------------------------// 3. Tools -- aligned with LGP tool definitions// ---------------------------------------------------------------------------const getWeather = tool(  async ({ location }) => ({    city: location,    temperature: 68,    humidity: 55,    wind_speed: 10,    conditions: "Sunny",  }),  {    name: "get_weather",    description: "Get the current weather for a given location.",    schema: z.object({      location: z.string().describe("City name"),    }),  },);

### On this page

What is this?When should I use this?Default tool rendering (zero-config)Custom catch-allPer-tool renderersTool inputs and results are separateThe backend tool definition
