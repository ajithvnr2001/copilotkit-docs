---
url: https://docs.copilotkit.ai/google-adk/generative-ui/tool-rendering/
title: Tool Call Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:08.664080+00:00
---

# Tool Call Rendering

> Source: https://docs.copilotkit.ai/google-adk/generative-ui/tool-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/google-adk/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/google-adk/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/google-adk/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

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

tool_rendering_agent.py

tool_rendering_common.py

page.tsx

route.ts
    
    
    """Agent backing the `tool-rendering` demo.Custom per-tool renderers (WeatherCard, FlightListCard, StockCard,D20Card) plus a wildcard catch-all on the frontend. Backend tools areidentical across the basic tool-rendering variants — seetool_rendering_common.py."""from __future__ import annotationsfrom google.adk.agents import LlmAgentfrom agents.shared_chat import get_model, stop_on_terminal_textfrom agents.tool_rendering_common import (    TOOL_RENDERING_INSTRUCTION,    get_stock_price,    get_weather,    roll_d20,    search_flights,)tool_rendering_agent = LlmAgent(    name="ToolRenderingAgent",    model=get_model(),    instruction=TOOL_RENDERING_INSTRUCTION,    tools=[get_weather, search_flights, get_stock_price, roll_d20],    after_model_callback=stop_on_terminal_text,)

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

tool_rendering_default_catchall_agent.py

tool_rendering_common.py

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

tool_rendering_custom_catchall_agent.py

tool_rendering_common.py

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

tool_rendering_common.py
    
    
    from __future__ import annotationsfrom random import choice, randintfrom google.adk.tools import ToolContextdef get_weather(tool_context: ToolContext, location: str) -> dict:    """Get the current weather for a given location."""    return {        "city": location,        "temperature": 68,        "humidity": 55,        "wind_speed": 10,        "conditions": "Sunny",    }

### On this page

What is this?When should I use this?Default tool rendering (zero-config)Custom catch-allPer-tool renderersTool inputs and results are separateThe backend tool definition
