---
url: https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/
title: Prebuilt Components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:55.154154+00:00
---

# Prebuilt Components

> Source: https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/

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

[LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript)

# Prebuilt Components

Drop-in chat components with a full customization ladder, from pure CSS to fully headless.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

graph.ts

page.tsx

route.ts
    
    
    /** * LangGraph TypeScript agent — CopilotKit showcase integration * * Defines a graph with a chat node and all showcase tools, * wired to CopilotKit via the sdk-js LangGraph adapter so frontend actions * and shared state flow seamlessly. */import { z } from "zod";import type { RunnableConfig } from "@langchain/core/runnables";import { tool } from "@langchain/core/tools";import { ToolNode } from "@langchain/langgraph/prebuilt";import type { AIMessage } from "@langchain/core/messages";import { SystemMessage } from "@langchain/core/messages";import {  MemorySaver,  START,  StateGraph,  Annotation,} from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import { getA2UITools } from "@ag-ui/langgraph";import { makeChatOpenAI } from "./openai-headers";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";import {  getWeatherImpl,  queryDataImpl,  manageSalesTodosImpl,  getSalesTodosImpl,  scheduleMeetingImpl,  searchFlightsImpl,} from "../../shared-tools";// ---------------------------------------------------------------------------// 1. Agent state — extends CopilotKit state with a proverbs list// ---------------------------------------------------------------------------const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,  proverbs: Annotation<string[]>,});export type AgentState = typeof AgentStateAnnotation.State;// ---------------------------------------------------------------------------// 2. Tools — shared implementations wrapped for LangChain// ---------------------------------------------------------------------------const getWeather = tool(  async ({ location }) => JSON.stringify(getWeatherImpl(location)),  {    name: "get_weather",    description: "Get current weather for a location",    schema: z.object({      location: z.string().describe("City name"),    }),  },);const queryData = tool(  async ({ query }) => JSON.stringify(queryDataImpl(query)),  {    name: "query_data",    description: "Query financial database for chart data",    schema: z.object({      query: z.string().describe("Natural language query"),    }),  },);const manageSalesTodos = tool(  async ({ todos }) => JSON.stringify(manageSalesTodosImpl(todos)),  {    name: "manage_sales_todos",    description: "Create or update the sales todo list",    schema: z.object({      todos: z        .array(          z.object({            id: z.string().optional(),            title: z.string(),            stage: z.string().optional(),            value: z.number().optional(),            dueDate: z.string().optional(),            assignee: z.string().optional(),            completed: z.boolean().optional(),          }),        )        .describe("Array of sales todo items"),    }),  },);const getSalesTodos = tool(  async ({ currentTodos }) => JSON.stringify(getSalesTodosImpl(currentTodos)),  {    name: "get_sales_todos",    description: "Get the current sales todo list",    schema: z.object({      currentTodos: z        .array(          z.object({            id: z.string().optional(),            title: z.string().optional(),            stage: z.string().optional(),            value: z.number().optional(),            dueDate: z.string().optional(),            assignee: z.string().optional(),            completed: z.boolean().optional(),          }),        )        .optional()        .nullable()        .describe("Current todos if any"),    }),  },);const scheduleMeeting = tool(  async ({ reason, durationMinutes }) =>    JSON.stringify(scheduleMeetingImpl(reason, durationMinutes)),  {    name: "schedule_meeting",    description: "Schedule a meeting (requires user approval via HITL)",    schema: z.object({      reason: z.string().describe("Reason for the meeting"),      durationMinutes: z.number().optional().describe("Duration in minutes"),    }),  },);const searchFlights = tool(  async ({ flights }) => JSON.stringify(searchFlightsImpl(flights)),  {    name: "search_flights",    description: "Search for available flights",    schema: z.object({      flights: z        .array(          z.object({            airline: z.string(),            airlineLogo: z.string().optional(),            flightNumber: z.string(),            origin: z.string(),            destination: z.string(),            date: z.string(),            departureTime: z.string(),            arrivalTime: z.string(),            duration: z.string(),            status: z.string(),            statusColor: z.string().optional(),            price: z.string(),            currency: z.string().optional(),          }),        )        .describe("Array of flight results"),    }),  },);// Dynamic A2UI via the canonical ag-ui factory (same as beautiful_chat /// a2ui_dynamic). A secondary LLM designs the surface; the factory forces the// host catalog and emits the a2ui_operations envelope. Replaces the prior// hand-rolled generate_a2ui tool.const generateA2ui = getA2UITools({  model: new ChatOpenAI({ model: "gpt-5-mini" }),  defaultCatalogId: "copilotkit://app-dashboard-catalog",});const tools = [  getWeather,  queryData,  manageSalesTodos,  getSalesTodos,  scheduleMeeting,  searchFlights,  generateA2ui,];// ---------------------------------------------------------------------------// 3. Chat node — binds backend + frontend tools, invokes the model// ---------------------------------------------------------------------------async function chatNode(state: AgentState, config: RunnableConfig) {  const model = makeChatOpenAI(config, { model: "gpt-5-mini" });  const modelWithTools = model.bindTools!([    ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),    ...tools,  ]);  const systemMessage = new SystemMessage({    content: `You are a helpful assistant. The current proverbs are ${JSON.stringify(state.proverbs)}.`,  });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    config,  );  return { messages: response };}// ---------------------------------------------------------------------------// 4. Routing — send tool calls to tool_node unless they're CopilotKit actions// ---------------------------------------------------------------------------function shouldContinue({ messages, copilotkit }: AgentState) {  const lastMessage = messages[messages.length - 1] as AIMessage;  if (lastMessage.tool_calls?.length) {    const actions = copilotkit?.actions;    const toolCallName = lastMessage.tool_calls![0].name;    if (!actions || actions.every((action) => action.name !== toolCallName)) {      return "tool_node";    }  }  return "__end__";}// ---------------------------------------------------------------------------// 5. Compile the graph// ---------------------------------------------------------------------------const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNode)  .addNode("tool_node", new ToolNode(tools))  .addEdge(START, "chat_node")  .addEdge("tool_node", "chat_node")  .addConditionalEdges("chat_node", shouldContinue as any);const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

[Want users to resume conversations across sessions?Persistent threads ship with CopilotKit Intelligence. Try it for free.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_prebuilt_components&utm_frontend=react&utm_backend=langgraph-typescript)

## Pre-built components for agentic chat#

CopilotKit ships three prebuilt chat surfaces that connect directly to your agent: [**CopilotChat**](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/chat), [**CopilotSidebar**](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/sidebar), and [**CopilotPopup**](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/popup). Each is a wrapper around the same primitives with a different layout. Pick the one that fits your app; they all handle streaming, generative UI, and deep customization.

If your chat surface needs saved conversations, history, or thread switching, drop in the [**Threads Drawer**](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/copilot-threads-drawer) next to any of them — or build your own switcher with [Headless Threads](https://docs.copilotkit.ai/langgraph-typescript/headless-threads).

## The customization ladder#

One of CopilotKit's design principles is that **you should never have to throw the prebuilt UI away** to get the look you want. Start at the top of this ladder and step down only when you need more control.

[Level 1 · EasiestDrop in as-isRender `<CopilotChat>`, `<CopilotSidebar>`, or `<CopilotPopup>` and ship. Streaming, tool calls, generative UI, and suggestions, all wired up.](https://docs.copilotkit.ai/prebuilt-components/chat)[Level 2 · Re-skinCustomize with CSSOverride theme tokens (`--copilot-kit-primary-color`, etc.) or target `.copilotKit...` classes. Keep every feature, change every color.](https://docs.copilotkit.ai/custom-look-and-feel/css)[Level 3 · RecomposeCustomize via slots (subcomponents)Swap the welcome screen, message bubble, composer, disclaimer, header, or toggle button with your own React component. Recursive; drill down as deep as you want.](https://docs.copilotkit.ai/custom-look-and-feel/slots)[Level 4 · Full controlGo fully headlessCompose your own chat from the low-level hooks (`useAgent`, `useCopilotKit`, `useRenderToolCall`). Any layout, any design system, or even non-chat surfaces.](https://docs.copilotkit.ai/custom-look-and-feel/headless-ui)

Everything below Level 1 is incremental: you can freely mix CSS variables, a custom welcome slot, and headless tool-call renderers in the same app. Nothing forces you to throw work away as your needs grow.

## Drop-in chat in a few lines#

Wrap your app in `<CopilotKit>` and drop `<CopilotChat>` where the chat should live. The provider wires the runtime, the session, and the agent registry. Everything else is optional configuration:

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="agentic_chat">      <Chat />    </CopilotKit>

## Starter suggestions#

`useConfigureSuggestions` lets you seed the chat with contextual prompts the moment a user arrives. The example below uses a single "Write a sonnet" suggestion:

suggestions.ts
    
    
    export function useAgenticChatSuggestions() {  useConfigureSuggestions({    suggestions: [      { title: "Write a sonnet", message: "Write a short sonnet about AI." },      {        title: "Tell me a joke",        message: "Tell me a one-line joke.",      },      {        title: "Is 17 prime?",        message: "Walk me through whether 17 is prime.",      },    ],    available: "always",  });}

## Pick a surface#

Each surface is a drop-in component with the same underlying primitives, differing only in layout.

  * [`<CopilotChat>`](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/chat): inline chat pane you can place anywhere and size to fit.
  * [`<CopilotSidebar>`](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/sidebar): collapsible sidebar docked to the edge of your app.
  * [`<CopilotPopup>`](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/popup): floating bubble that overlays your page content.



Add a conversation-history sidebar next to any of these with [Threads Drawer](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/copilot-threads-drawer) — a drop-in thread switcher with no active-thread wiring.

Need to open/close the chat from your own button, or capture thumbs-up/down feedback? See [Open, close, and feedback](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/chat-controls).
