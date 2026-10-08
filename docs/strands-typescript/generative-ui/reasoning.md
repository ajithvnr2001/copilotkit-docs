---
url: https://docs.copilotkit.ai/strands-typescript/generative-ui/reasoning/
title: Reasoning
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:29:43.433299+00:00
---

# Reasoning

> Source: https://docs.copilotkit.ai/strands-typescript/generative-ui/reasoning/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands-typescript)[Quickstart](https://docs.copilotkit.ai/strands-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/strands-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/strands-typescript/multimodal-attachments)[Voice](https://docs.copilotkit.ai/strands-typescript/voice)[Reasoning](https://docs.copilotkit.ai/strands-typescript/generative-ui/reasoning)

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

BasicsChat

# Reasoning

Surface the agent's thinking chain in the chat — default or fully custom.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

reasoning-agent.ts

page.tsx

reasoning-block.tsx

route.ts
    
    
    /** * Reasoning agents: emit AG-UI REASONING_MESSAGE_* events. * * Mirrors the Python siblings `agents/reasoning_agent.py` and * `agents/reasoning_chain_agent.py`. * * Why a reasoning model plus the Responses API: the OpenAI Responses API * streams `response.reasoning_summary_text.delta` items only for native * reasoning models (gpt-5, o3, o4-mini and friends). The Strands bridge * translates those into AG-UI REASONING_MESSAGE_* events with * `role: "reasoning"`, which the frontend renders through the * `reasoningMessage` slot. gpt-4o emits no reasoning items, so the showcase's * default chat-completions model would never light the slot up. * * `buildReasoningAgent` is tool-free and serves reasoning-default and * reasoning-custom. `buildReasoningChainAgent` adds the four mock tools the * tool-rendering-reasoning-chain demo paints per-tool renderers for; each pill * drives a chained pair of calls, so the agent has to own every tool in the * chain to reach the closing narration. */import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import { StrandsAgent } from "@ag-ui/aws-strands";import { createModel } from "./model-factory";export const REASONING_MODEL = process.env.OPENAI_REASONING_MODEL ?? "gpt-5.4";/** Responses-API model that streams reasoning summaries on every turn. */function reasoningModel() {  return createModel({    openaiApi: "responses",    reasoning: true,    openaiModelId: REASONING_MODEL,  });}const REASONING_SYSTEM_PROMPT =  "You are a helpful assistant. For each user question, first think " +  "step-by-step about the approach, then give a concise answer.";/** Tool-free agent backing reasoning-default and reasoning-custom. */export async function buildReasoningAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await reasoningModel(),      systemPrompt: REASONING_SYSTEM_PROMPT,      tools: [],    }),    name: "reasoning",    description:      "Strands agent that streams reasoning summaries alongside its answer",  });}const getWeather = tool({  name: "get_weather",  description: "Get the current weather for a given location.",  inputSchema: z.object({    location: z.string().describe("City or airport to report on."),  }),  callback: ({ location }) => ({    city: location,    temperature: 68,    humidity: 55,    wind_speed: 10,    conditions: "Sunny",  }),});const searchFlights = tool({  name: "search_flights",  description:    "Search mock flights from an origin airport to a destination airport.",  inputSchema: z.object({    origin: z.string().describe("Origin airport code."),    destination: z.string().describe("Destination airport code."),  }),  callback: ({ origin, destination }) => ({    origin,    destination,    flights: [      {        airline: "United",        flight: "UA231",        depart: "08:15",        arrive: "16:45",        price_usd: 348,      },      {        airline: "Delta",        flight: "DL412",        depart: "11:20",        arrive: "19:55",        price_usd: 312,      },      {        airline: "JetBlue",        flight: "B6722",        depart: "17:05",        arrive: "01:30",        price_usd: 289,      },    ],  }),});const getStockPrice = tool({  name: "get_stock_price",  description: "Get a mock current price for a stock ticker.",  inputSchema: z.object({    ticker: z.string().describe("Ticker symbol to quote."),    price_usd: z.number().optional().describe("Optional scripted price."),    change_pct: z      .number()      .optional()      .describe("Optional scripted percentage change."),  }),  // The optional arguments let the model (or an aimock fixture) script a  // deterministic quote: when supplied they are echoed back verbatim.  callback: ({ ticker, price_usd, change_pct }) => ({    ticker: ticker.toUpperCase(),    price_usd:      price_usd !== undefined        ? Math.round(price_usd * 100) / 100        : Math.round((100 + Math.random() * 400) * 100) / 100,    change_pct:      change_pct !== undefined        ? Math.round(change_pct * 100) / 100        : Math.round((Math.random() < 0.5 ? -1 : 1) * Math.random() * 300) /          100,  }),});const rollDice = tool({  name: "roll_dice",  description: "Roll a single die with the given number of sides.",  inputSchema: z.object({    sides: z.number().default(6).describe("Number of faces on the die."),  }),  callback: ({ sides }) => ({    sides,    result: 1 + Math.floor(Math.random() * Math.max(2, sides)),  }),});const REASONING_CHAIN_SYSTEM_PROMPT = `You are a helpful travel & lifestyle concierge with mock tools for weather, flights, stock prices, and dice rolls -- they all return fake data, so call them liberally.Your habit is to CHAIN tools when one answer naturally invites another. For a single user question, call at least TWO tools in succession when the topic allows, then compose your final reply. Default chains:  - 'What's the weather in <city>?' -> call get_weather(<city>), then call search_flights(origin='SFO', destination=<city>) so the user also sees how to get there.  - 'How is <ticker> doing?' -> call get_stock_price(<ticker>), then call get_stock_price on a comparable ticker (e.g. 'MSFT' or 'GOOGL') so the user can compare.  - 'Roll a 20-sided die' -> call roll_dice(sides=20), then call roll_dice again with a different number of sides so the user sees a contrast.  - 'Find flights from <a> to <b>' -> call search_flights(a, b), then call get_weather(<b>) for the destination.Only skip chaining when the user has clearly asked for a single, atomic answer and more tool calls would feel intrusive. Never fabricate data that a tool could provide.`;/** Agent backing tool-rendering-reasoning-chain. */export async function buildReasoningChainAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await reasoningModel(),      systemPrompt: REASONING_CHAIN_SYSTEM_PROMPT,      tools: [getWeather, searchFlights, getStockPrice, rollDice],    }),    name: "reasoning_chain",    description:      "Strands agent that chains mock tools while streaming reasoning summaries",  });}

## What is this?#

Some models (OpenAI's `o1`, `o3`, and `o4-mini`, Anthropic's thinking variants) emit **reasoning tokens** , internal chain-of-thought traces that explain how the model is working toward its answer. CopilotKit surfaces these as first-class messages: when a `REASONING_MESSAGE_*` event arrives from the agent, the chat renders it inline so the user can follow the agent's thinking.

Reasoning isn't a custom-renderer plumb-in; it's a dedicated message type on the chat view. You can either accept the built-in rendering or override the `reasoningMessage` slot with your own component.

## When should I use this?#

Expose reasoning in the UI when you want to:

  * Give users real-time insight into the agent's thought process
  * Show progress on long or multi-step problems
  * Debug prompt behavior during development
  * Brand the reasoning card to match the rest of your product



## Default reasoning rendering (zero-config)#

Out of the box, reasoning events render inside CopilotKit's built-in `CopilotChatReasoningMessage` card:

  * A **"Thinking…"** label with a pulsing indicator while the model reasons.
  * Auto-expanded content so users can follow the chain of thought live.
  * Collapses to **"Thought for X seconds"** once reasoning finishes, with a chevron to re-expand.
  * Reasoning text rendered as Markdown.



No configuration is needed; if your model emits reasoning tokens, the card appears automatically:

page.tsx
    
    
    const AGENT_ID = "reasoning-default";export default function ReasoningDefaultDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningDefaultSuggestions();  return <CopilotChat agentId={AGENT_ID} className="h-full rounded-2xl" />;}

Here's what the built-in card looks like while the model thinks through a multi-step problem:

DemoCode

reasoning-agent.ts

page.tsx

suggestions.ts

route.ts
    
    
    /** * Reasoning agents: emit AG-UI REASONING_MESSAGE_* events. * * Mirrors the Python siblings `agents/reasoning_agent.py` and * `agents/reasoning_chain_agent.py`. * * Why a reasoning model plus the Responses API: the OpenAI Responses API * streams `response.reasoning_summary_text.delta` items only for native * reasoning models (gpt-5, o3, o4-mini and friends). The Strands bridge * translates those into AG-UI REASONING_MESSAGE_* events with * `role: "reasoning"`, which the frontend renders through the * `reasoningMessage` slot. gpt-4o emits no reasoning items, so the showcase's * default chat-completions model would never light the slot up. * * `buildReasoningAgent` is tool-free and serves reasoning-default and * reasoning-custom. `buildReasoningChainAgent` adds the four mock tools the * tool-rendering-reasoning-chain demo paints per-tool renderers for; each pill * drives a chained pair of calls, so the agent has to own every tool in the * chain to reach the closing narration. */import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import { StrandsAgent } from "@ag-ui/aws-strands";import { createModel } from "./model-factory";export const REASONING_MODEL = process.env.OPENAI_REASONING_MODEL ?? "gpt-5.4";/** Responses-API model that streams reasoning summaries on every turn. */function reasoningModel() {  return createModel({    openaiApi: "responses",    reasoning: true,    openaiModelId: REASONING_MODEL,  });}const REASONING_SYSTEM_PROMPT =  "You are a helpful assistant. For each user question, first think " +  "step-by-step about the approach, then give a concise answer.";/** Tool-free agent backing reasoning-default and reasoning-custom. */export async function buildReasoningAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await reasoningModel(),      systemPrompt: REASONING_SYSTEM_PROMPT,      tools: [],    }),    name: "reasoning",    description:      "Strands agent that streams reasoning summaries alongside its answer",  });}const getWeather = tool({  name: "get_weather",  description: "Get the current weather for a given location.",  inputSchema: z.object({    location: z.string().describe("City or airport to report on."),  }),  callback: ({ location }) => ({    city: location,    temperature: 68,    humidity: 55,    wind_speed: 10,    conditions: "Sunny",  }),});const searchFlights = tool({  name: "search_flights",  description:    "Search mock flights from an origin airport to a destination airport.",  inputSchema: z.object({    origin: z.string().describe("Origin airport code."),    destination: z.string().describe("Destination airport code."),  }),  callback: ({ origin, destination }) => ({    origin,    destination,    flights: [      {        airline: "United",        flight: "UA231",        depart: "08:15",        arrive: "16:45",        price_usd: 348,      },      {        airline: "Delta",        flight: "DL412",        depart: "11:20",        arrive: "19:55",        price_usd: 312,      },      {        airline: "JetBlue",        flight: "B6722",        depart: "17:05",        arrive: "01:30",        price_usd: 289,      },    ],  }),});const getStockPrice = tool({  name: "get_stock_price",  description: "Get a mock current price for a stock ticker.",  inputSchema: z.object({    ticker: z.string().describe("Ticker symbol to quote."),    price_usd: z.number().optional().describe("Optional scripted price."),    change_pct: z      .number()      .optional()      .describe("Optional scripted percentage change."),  }),  // The optional arguments let the model (or an aimock fixture) script a  // deterministic quote: when supplied they are echoed back verbatim.  callback: ({ ticker, price_usd, change_pct }) => ({    ticker: ticker.toUpperCase(),    price_usd:      price_usd !== undefined        ? Math.round(price_usd * 100) / 100        : Math.round((100 + Math.random() * 400) * 100) / 100,    change_pct:      change_pct !== undefined        ? Math.round(change_pct * 100) / 100        : Math.round((Math.random() < 0.5 ? -1 : 1) * Math.random() * 300) /          100,  }),});const rollDice = tool({  name: "roll_dice",  description: "Roll a single die with the given number of sides.",  inputSchema: z.object({    sides: z.number().default(6).describe("Number of faces on the die."),  }),  callback: ({ sides }) => ({    sides,    result: 1 + Math.floor(Math.random() * Math.max(2, sides)),  }),});const REASONING_CHAIN_SYSTEM_PROMPT = `You are a helpful travel & lifestyle concierge with mock tools for weather, flights, stock prices, and dice rolls -- they all return fake data, so call them liberally.Your habit is to CHAIN tools when one answer naturally invites another. For a single user question, call at least TWO tools in succession when the topic allows, then compose your final reply. Default chains:  - 'What's the weather in <city>?' -> call get_weather(<city>), then call search_flights(origin='SFO', destination=<city>) so the user also sees how to get there.  - 'How is <ticker> doing?' -> call get_stock_price(<ticker>), then call get_stock_price on a comparable ticker (e.g. 'MSFT' or 'GOOGL') so the user can compare.  - 'Roll a 20-sided die' -> call roll_dice(sides=20), then call roll_dice again with a different number of sides so the user sees a contrast.  - 'Find flights from <a> to <b>' -> call search_flights(a, b), then call get_weather(<b>) for the destination.Only skip chaining when the user has clearly asked for a single, atomic answer and more tool calls would feel intrusive. Never fabricate data that a tool could provide.`;/** Agent backing tool-rendering-reasoning-chain. */export async function buildReasoningChainAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await reasoningModel(),      systemPrompt: REASONING_CHAIN_SYSTEM_PROMPT,      tools: [getWeather, searchFlights, getStockPrice, rollDice],    }),    name: "reasoning_chain",    description:      "Strands agent that chains mock tools while streaming reasoning summaries",  });}

## Custom reasoning rendering#

For full control over the reasoning card, pass a component to the `reasoningMessage` slot on `messageView`. Your component receives the `ReasoningMessage` object (`.content` holds the streaming text), the full `messages` list, and `isRunning`, enough to decide whether this block is still streaming and whether it's the active trailing message:

page.tsxreasoning-block.tsx
    
    
    const AGENT_ID = "reasoning-custom";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}
    
    
    "use client";// Custom `reasoningMessage` slot renderer.//// Receives the `ReasoningMessage` plus (optionally) the full message list and// the running state from the slot system. Renders the content inline with a// visibly tagged amber banner so the user can always see the agent's thinking// chain — this is the focal UI of the demo.import React from "react";import type { ReasoningMessage, Message } from "@ag-ui/core";export function ReasoningBlock({  message,  messages,  isRunning,}: {  message: ReasoningMessage;  messages?: Message[];  isRunning?: boolean;}) {  const isLatest = messages?.[messages.length - 1]?.id === message.id;  const isStreaming = !!(isRunning && isLatest);  const hasContent = !!(message.content && message.content.length > 0);  return (    <div      data-testid="reasoning-block"      className="my-2 rounded-xl border border-[#DBDBE5] bg-[#BEC2FF1A] px-3.5 py-2.5 text-sm"    >      <div className="flex items-center gap-2 font-medium text-[#010507]">        <span className="inline-block rounded-full border border-[#BEC2FF] bg-white px-2 py-0.5 text-[10px] uppercase tracking-[0.14em] text-[#57575B]">          Reasoning        </span>        <span className="text-[#57575B]">          {isStreaming ? "Thinking…" : hasContent ? "Agent reasoning" : "…"}        </span>      </div>      {hasContent && (        <div className="mt-1.5 whitespace-pre-wrap italic text-[#57575B]">          {message.content}        </div>      )}    </div>  );}

The `ReasoningBlock` (imported above) renders the reasoning as an amber-tagged inline banner, intentionally louder than the default card so the thinking chain is the focal UI of the demo. Swap in your own component to match your product's tone.

The `messageView.reasoningMessage` slot accepts either a full component (as shown) or a sub-slot object like `{ header, contentView, toggle }` if you just want to tweak parts of the default card. See the reference docs for sub-slot props.
