---
url: https://docs.copilotkit.ai/strands-typescript/custom-look-and-feel/reasoning-messages/
title: Reasoning Messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:29:33.071170+00:00
---

# Reasoning Messages

> Source: https://docs.copilotkit.ai/strands-typescript/custom-look-and-feel/reasoning-messages/

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

[CSS Customization](https://docs.copilotkit.ai/strands-typescript/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/strands-typescript/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/strands-typescript/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/strands-typescript/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/strands-typescript/custom-look-and-feel/reasoning-messages)

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

Reasoning Messages

BasicsChatCustom Look and Feel

# Reasoning Messages

Customize how reasoning (thinking) tokens from models like o1, o3, and o4-mini are displayed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

reasoning-agent.ts

page.tsx

suggestions.ts

route.ts
    
    
    /** * Reasoning agents: emit AG-UI REASONING_MESSAGE_* events. * * Mirrors the Python siblings `agents/reasoning_agent.py` and * `agents/reasoning_chain_agent.py`. * * Why a reasoning model plus the Responses API: the OpenAI Responses API * streams `response.reasoning_summary_text.delta` items only for native * reasoning models (gpt-5, o3, o4-mini and friends). The Strands bridge * translates those into AG-UI REASONING_MESSAGE_* events with * `role: "reasoning"`, which the frontend renders through the * `reasoningMessage` slot. gpt-4o emits no reasoning items, so the showcase's * default chat-completions model would never light the slot up. * * `buildReasoningAgent` is tool-free and serves reasoning-default and * reasoning-custom. `buildReasoningChainAgent` adds the four mock tools the * tool-rendering-reasoning-chain demo paints per-tool renderers for; each pill * drives a chained pair of calls, so the agent has to own every tool in the * chain to reach the closing narration. */import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import { StrandsAgent } from "@ag-ui/aws-strands";import { createModel } from "./model-factory";export const REASONING_MODEL = process.env.OPENAI_REASONING_MODEL ?? "gpt-5.4";/** Responses-API model that streams reasoning summaries on every turn. */function reasoningModel() {  return createModel({    openaiApi: "responses",    reasoning: true,    openaiModelId: REASONING_MODEL,  });}const REASONING_SYSTEM_PROMPT =  "You are a helpful assistant. For each user question, first think " +  "step-by-step about the approach, then give a concise answer.";/** Tool-free agent backing reasoning-default and reasoning-custom. */export async function buildReasoningAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await reasoningModel(),      systemPrompt: REASONING_SYSTEM_PROMPT,      tools: [],    }),    name: "reasoning",    description:      "Strands agent that streams reasoning summaries alongside its answer",  });}const getWeather = tool({  name: "get_weather",  description: "Get the current weather for a given location.",  inputSchema: z.object({    location: z.string().describe("City or airport to report on."),  }),  callback: ({ location }) => ({    city: location,    temperature: 68,    humidity: 55,    wind_speed: 10,    conditions: "Sunny",  }),});const searchFlights = tool({  name: "search_flights",  description:    "Search mock flights from an origin airport to a destination airport.",  inputSchema: z.object({    origin: z.string().describe("Origin airport code."),    destination: z.string().describe("Destination airport code."),  }),  callback: ({ origin, destination }) => ({    origin,    destination,    flights: [      {        airline: "United",        flight: "UA231",        depart: "08:15",        arrive: "16:45",        price_usd: 348,      },      {        airline: "Delta",        flight: "DL412",        depart: "11:20",        arrive: "19:55",        price_usd: 312,      },      {        airline: "JetBlue",        flight: "B6722",        depart: "17:05",        arrive: "01:30",        price_usd: 289,      },    ],  }),});const getStockPrice = tool({  name: "get_stock_price",  description: "Get a mock current price for a stock ticker.",  inputSchema: z.object({    ticker: z.string().describe("Ticker symbol to quote."),    price_usd: z.number().optional().describe("Optional scripted price."),    change_pct: z      .number()      .optional()      .describe("Optional scripted percentage change."),  }),  // The optional arguments let the model (or an aimock fixture) script a  // deterministic quote: when supplied they are echoed back verbatim.  callback: ({ ticker, price_usd, change_pct }) => ({    ticker: ticker.toUpperCase(),    price_usd:      price_usd !== undefined        ? Math.round(price_usd * 100) / 100        : Math.round((100 + Math.random() * 400) * 100) / 100,    change_pct:      change_pct !== undefined        ? Math.round(change_pct * 100) / 100        : Math.round((Math.random() < 0.5 ? -1 : 1) * Math.random() * 300) /          100,  }),});const rollDice = tool({  name: "roll_dice",  description: "Roll a single die with the given number of sides.",  inputSchema: z.object({    sides: z.number().default(6).describe("Number of faces on the die."),  }),  callback: ({ sides }) => ({    sides,    result: 1 + Math.floor(Math.random() * Math.max(2, sides)),  }),});const REASONING_CHAIN_SYSTEM_PROMPT = `You are a helpful travel & lifestyle concierge with mock tools for weather, flights, stock prices, and dice rolls -- they all return fake data, so call them liberally.Your habit is to CHAIN tools when one answer naturally invites another. For a single user question, call at least TWO tools in succession when the topic allows, then compose your final reply. Default chains:  - 'What's the weather in <city>?' -> call get_weather(<city>), then call search_flights(origin='SFO', destination=<city>) so the user also sees how to get there.  - 'How is <ticker> doing?' -> call get_stock_price(<ticker>), then call get_stock_price on a comparable ticker (e.g. 'MSFT' or 'GOOGL') so the user can compare.  - 'Roll a 20-sided die' -> call roll_dice(sides=20), then call roll_dice again with a different number of sides so the user sees a contrast.  - 'Find flights from <a> to <b>' -> call search_flights(a, b), then call get_weather(<b>) for the destination.Only skip chaining when the user has clearly asked for a single, atomic answer and more tool calls would feel intrusive. Never fabricate data that a tool could provide.`;/** Agent backing tool-rendering-reasoning-chain. */export async function buildReasoningChainAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await reasoningModel(),      systemPrompt: REASONING_CHAIN_SYSTEM_PROMPT,      tools: [getWeather, searchFlights, getStockPrice, rollDice],    }),    name: "reasoning_chain",    description:      "Strands agent that chains mock tools while streaming reasoning summaries",  });}

Some models (like OpenAI's o1, o3, and o4-mini) emit **reasoning tokens** : internal "thinking" traces that show the model's chain-of-thought before it produces a final answer. CopilotKit surfaces these tokens automatically with a collapsible **Reasoning Message** card.

## Default Behavior#

When reasoning events arrive from the agent, CopilotKit renders them inside a built-in card that:

  * Shows a **"Thinking…"** label with a pulsating indicator while the model is reasoning.
  * Expands automatically so you can follow the model's thought process in real-time.
  * Collapses and switches to **"Thought for X seconds"** once reasoning finishes.
  * Renders the reasoning content as **Markdown**.
  * Includes a chevron toggle so users can re-expand and review the reasoning at any time.



No extra configuration is needed; if your model emits reasoning tokens, the card appears automatically.

The only requirement is connecting your agent to CopilotKit; no extra props or configuration needed:

page.tsx
    
    
    const AGENT_ID = "reasoning-default";export default function ReasoningDefaultDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningDefaultSuggestions();  return <CopilotChat agentId={AGENT_ID} className="h-full rounded-2xl" />;}

## Customizing the Reasoning Message#

The reasoning message is composed of three sub-components that can each be replaced independently via **slot props** :

Sub-component| Slot prop| Description  
---|---|---  
`Header`| `header`| The clickable bar with the brain icon, label, and chevron  
`Content`| `contentView`| The reasoning text area (Markdown)  
`Toggle`| `toggle`| The expand/collapse animation wrapper  
  
You pass custom sub-components through the `messageView` prop on `CopilotChat`, `CopilotPopup`, or `CopilotSidebar`:
    
    
    <CopilotChat
      messageView={{
        reasoningMessage: {
          header: CustomHeader,
          contentView: CustomContent,
        },
      }}
    />

### Custom Header#

Replace the header to change the icon, label text, or styling. The header receives these props:

Prop| Type| Description  
---|---|---  
`isOpen`| `boolean`| Whether the content panel is currently expanded  
`label`| `string`| `"Thinking…"` while streaming, `"Thought for X seconds"` after  
`hasContent`| `boolean`| Whether any reasoning text has been received  
`isStreaming`| `boolean`| Whether reasoning is actively streaming  
`onClick`| `() => void`| Toggle handler (only present when `hasContent` is `true`)  
      
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function CustomHeader({
      isOpen,
      label,
      hasContent,
      isStreaming,
      ...props
    }: React.ButtonHTMLAttributes<HTMLButtonElement> & {
      isOpen?: boolean;
      label?: string;
      hasContent?: boolean;
      isStreaming?: boolean;
    }) {
      return (
        <button
          className="flex w-full items-center gap-2 px-3 py-2 text-sm font-medium"
          {...props}
        >
          {isStreaming ? "🧠" : "💡"}
          <span>{label}</span>
          {hasContent && (
            <span className="ml-auto text-xs">{isOpen ? "Hide" : "Show"}</span>
          )}
        </button>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: { header: CustomHeader },
      }}
    />

### Custom Content#

Replace the content area to change how reasoning text is displayed:

Prop| Type| Description  
---|---|---  
`isStreaming`| `boolean`| Whether reasoning tokens are still arriving  
`hasContent`| `boolean`| Whether any reasoning text has been received  
`children`| `string`| The raw reasoning text  
      
    
    function CustomContent({
      isStreaming,
      hasContent,
      children,
      ...props
    }: React.HTMLAttributes<HTMLDivElement> & {
      isStreaming?: boolean;
      hasContent?: boolean;
    }) {
      if (!hasContent && !isStreaming) return null;
    
      return (
        <div className="px-4 pb-3 text-sm text-gray-500 font-mono" {...props}>
          {children}
          {isStreaming && <span className="animate-pulse ml-1">▊</span>}
        </div>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: { contentView: CustomContent },
      }}
    />

## Fully Custom Reasoning Message#

For complete control over the entire reasoning card, pass a **component** instead of slot props. Your component receives the same top-level props as the built-in one:

Prop| Type| Description  
---|---|---  
`message`| `ReasoningMessage`| The reasoning message object (`.content` holds the text)  
`messages`| `Message[]`| All messages in the conversation  
`isRunning`| `boolean`| Whether the agent is currently running  
  
DemoCode

reasoning-agent.ts

page.tsx

reasoning-block.tsx

route.ts
    
    
    /** * Reasoning agents: emit AG-UI REASONING_MESSAGE_* events. * * Mirrors the Python siblings `agents/reasoning_agent.py` and * `agents/reasoning_chain_agent.py`. * * Why a reasoning model plus the Responses API: the OpenAI Responses API * streams `response.reasoning_summary_text.delta` items only for native * reasoning models (gpt-5, o3, o4-mini and friends). The Strands bridge * translates those into AG-UI REASONING_MESSAGE_* events with * `role: "reasoning"`, which the frontend renders through the * `reasoningMessage` slot. gpt-4o emits no reasoning items, so the showcase's * default chat-completions model would never light the slot up. * * `buildReasoningAgent` is tool-free and serves reasoning-default and * reasoning-custom. `buildReasoningChainAgent` adds the four mock tools the * tool-rendering-reasoning-chain demo paints per-tool renderers for; each pill * drives a chained pair of calls, so the agent has to own every tool in the * chain to reach the closing narration. */import { Agent, tool } from "@strands-agents/sdk";import { z } from "zod";import { StrandsAgent } from "@ag-ui/aws-strands";import { createModel } from "./model-factory";export const REASONING_MODEL = process.env.OPENAI_REASONING_MODEL ?? "gpt-5.4";/** Responses-API model that streams reasoning summaries on every turn. */function reasoningModel() {  return createModel({    openaiApi: "responses",    reasoning: true,    openaiModelId: REASONING_MODEL,  });}const REASONING_SYSTEM_PROMPT =  "You are a helpful assistant. For each user question, first think " +  "step-by-step about the approach, then give a concise answer.";/** Tool-free agent backing reasoning-default and reasoning-custom. */export async function buildReasoningAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await reasoningModel(),      systemPrompt: REASONING_SYSTEM_PROMPT,      tools: [],    }),    name: "reasoning",    description:      "Strands agent that streams reasoning summaries alongside its answer",  });}const getWeather = tool({  name: "get_weather",  description: "Get the current weather for a given location.",  inputSchema: z.object({    location: z.string().describe("City or airport to report on."),  }),  callback: ({ location }) => ({    city: location,    temperature: 68,    humidity: 55,    wind_speed: 10,    conditions: "Sunny",  }),});const searchFlights = tool({  name: "search_flights",  description:    "Search mock flights from an origin airport to a destination airport.",  inputSchema: z.object({    origin: z.string().describe("Origin airport code."),    destination: z.string().describe("Destination airport code."),  }),  callback: ({ origin, destination }) => ({    origin,    destination,    flights: [      {        airline: "United",        flight: "UA231",        depart: "08:15",        arrive: "16:45",        price_usd: 348,      },      {        airline: "Delta",        flight: "DL412",        depart: "11:20",        arrive: "19:55",        price_usd: 312,      },      {        airline: "JetBlue",        flight: "B6722",        depart: "17:05",        arrive: "01:30",        price_usd: 289,      },    ],  }),});const getStockPrice = tool({  name: "get_stock_price",  description: "Get a mock current price for a stock ticker.",  inputSchema: z.object({    ticker: z.string().describe("Ticker symbol to quote."),    price_usd: z.number().optional().describe("Optional scripted price."),    change_pct: z      .number()      .optional()      .describe("Optional scripted percentage change."),  }),  // The optional arguments let the model (or an aimock fixture) script a  // deterministic quote: when supplied they are echoed back verbatim.  callback: ({ ticker, price_usd, change_pct }) => ({    ticker: ticker.toUpperCase(),    price_usd:      price_usd !== undefined        ? Math.round(price_usd * 100) / 100        : Math.round((100 + Math.random() * 400) * 100) / 100,    change_pct:      change_pct !== undefined        ? Math.round(change_pct * 100) / 100        : Math.round((Math.random() < 0.5 ? -1 : 1) * Math.random() * 300) /          100,  }),});const rollDice = tool({  name: "roll_dice",  description: "Roll a single die with the given number of sides.",  inputSchema: z.object({    sides: z.number().default(6).describe("Number of faces on the die."),  }),  callback: ({ sides }) => ({    sides,    result: 1 + Math.floor(Math.random() * Math.max(2, sides)),  }),});const REASONING_CHAIN_SYSTEM_PROMPT = `You are a helpful travel & lifestyle concierge with mock tools for weather, flights, stock prices, and dice rolls -- they all return fake data, so call them liberally.Your habit is to CHAIN tools when one answer naturally invites another. For a single user question, call at least TWO tools in succession when the topic allows, then compose your final reply. Default chains:  - 'What's the weather in <city>?' -> call get_weather(<city>), then call search_flights(origin='SFO', destination=<city>) so the user also sees how to get there.  - 'How is <ticker> doing?' -> call get_stock_price(<ticker>), then call get_stock_price on a comparable ticker (e.g. 'MSFT' or 'GOOGL') so the user can compare.  - 'Roll a 20-sided die' -> call roll_dice(sides=20), then call roll_dice again with a different number of sides so the user sees a contrast.  - 'Find flights from <a> to <b>' -> call search_flights(a, b), then call get_weather(<b>) for the destination.Only skip chaining when the user has clearly asked for a single, atomic answer and more tool calls would feel intrusive. Never fabricate data that a tool could provide.`;/** Agent backing tool-rendering-reasoning-chain. */export async function buildReasoningChainAgent(): Promise<StrandsAgent> {  return new StrandsAgent({    agent: new Agent({      model: await reasoningModel(),      systemPrompt: REASONING_CHAIN_SYSTEM_PROMPT,      tools: [getWeather, searchFlights, getStockPrice, rollDice],    }),    name: "reasoning_chain",    description:      "Strands agent that chains mock tools while streaming reasoning summaries",  });}

The `ReasoningBlock` used above renders the reasoning as an amber-tagged inline banner, intentionally louder than the default card so the thinking chain is the focal UI of the demo. Swap in your own component to match your product's tone:

page.tsx
    
    
    const AGENT_ID = "reasoning-custom";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}

## Render-Prop Children#

The built-in `CopilotChatReasoningMessage` also supports a **render-prop** pattern for cases where you want to rearrange the built-in sub-components without reimplementing them:
    
    
    import {
      CopilotChatReasoningMessage,
    } from "@copilotkit/react-core/v2";
    import { CopilotChat } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";
    
    function MyReasoningLayout(props: React.ComponentProps<typeof CopilotChatReasoningMessage>) {
      return (
        <CopilotChatReasoningMessage {...props}>
          {({ header, toggle }) => (
            <div className="rounded-lg border bg-yellow-50 my-2">
              {header}
              {toggle}
            </div>
          )}
        </CopilotChatReasoningMessage>
      );
    }
    
    <CopilotChat
      messageView={{
        reasoningMessage: MyReasoningLayout,
      }}
    />

The render-prop callback receives:

Property| Description  
---|---  
`header`| Pre-rendered header element  
`contentView`| Pre-rendered content element  
`toggle`| Pre-rendered expand/collapse wrapper (contains `contentView`)  
`message`| The reasoning message object  
`messages`| All messages  
`isRunning`| Whether the agent is running  
  
### On this page

Default BehaviorCustomizing the Reasoning MessageCustom HeaderCustom ContentFully Custom Reasoning MessageRender-Prop Children
