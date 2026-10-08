---
url: https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/popup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:59.188944+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/popup/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Prebuilt Components

[CopilotChat](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/chat)[CopilotSidebar](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/sidebar)[CopilotPopup](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/popup)[Open, close, and feedback](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/chat-controls)

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/langgraph-typescript/multimodal-attachments)[Voice](https://docs.copilotkit.ai/langgraph-typescript/voice)[Reasoning](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/reasoning)

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

CopilotPopup

BasicsChatPrebuilt Components

# CopilotPopup

Floating chat bubble that toggles open an overlay chat window.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

graph.ts

page.tsx

route.ts
    
    
    /** * LangGraph TypeScript agent — CopilotKit showcase integration * * Defines a graph with a chat node and all showcase tools, * wired to CopilotKit via the sdk-js LangGraph adapter so frontend actions * and shared state flow seamlessly. */import { z } from "zod";import type { RunnableConfig } from "@langchain/core/runnables";import { tool } from "@langchain/core/tools";import { ToolNode } from "@langchain/langgraph/prebuilt";import type { AIMessage } from "@langchain/core/messages";import { SystemMessage } from "@langchain/core/messages";import {  MemorySaver,  START,  StateGraph,  Annotation,} from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import { getA2UITools } from "@ag-ui/langgraph";import { makeChatOpenAI } from "./openai-headers";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";import {  getWeatherImpl,  queryDataImpl,  manageSalesTodosImpl,  getSalesTodosImpl,  scheduleMeetingImpl,  searchFlightsImpl,} from "../../shared-tools";// ---------------------------------------------------------------------------// 1. Agent state — extends CopilotKit state with a proverbs list// ---------------------------------------------------------------------------const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,  proverbs: Annotation<string[]>,});export type AgentState = typeof AgentStateAnnotation.State;// ---------------------------------------------------------------------------// 2. Tools — shared implementations wrapped for LangChain// ---------------------------------------------------------------------------const getWeather = tool(  async ({ location }) => JSON.stringify(getWeatherImpl(location)),  {    name: "get_weather",    description: "Get current weather for a location",    schema: z.object({      location: z.string().describe("City name"),    }),  },);const queryData = tool(  async ({ query }) => JSON.stringify(queryDataImpl(query)),  {    name: "query_data",    description: "Query financial database for chart data",    schema: z.object({      query: z.string().describe("Natural language query"),    }),  },);const manageSalesTodos = tool(  async ({ todos }) => JSON.stringify(manageSalesTodosImpl(todos)),  {    name: "manage_sales_todos",    description: "Create or update the sales todo list",    schema: z.object({      todos: z        .array(          z.object({            id: z.string().optional(),            title: z.string(),            stage: z.string().optional(),            value: z.number().optional(),            dueDate: z.string().optional(),            assignee: z.string().optional(),            completed: z.boolean().optional(),          }),        )        .describe("Array of sales todo items"),    }),  },);const getSalesTodos = tool(  async ({ currentTodos }) => JSON.stringify(getSalesTodosImpl(currentTodos)),  {    name: "get_sales_todos",    description: "Get the current sales todo list",    schema: z.object({      currentTodos: z        .array(          z.object({            id: z.string().optional(),            title: z.string().optional(),            stage: z.string().optional(),            value: z.number().optional(),            dueDate: z.string().optional(),            assignee: z.string().optional(),            completed: z.boolean().optional(),          }),        )        .optional()        .nullable()        .describe("Current todos if any"),    }),  },);const scheduleMeeting = tool(  async ({ reason, durationMinutes }) =>    JSON.stringify(scheduleMeetingImpl(reason, durationMinutes)),  {    name: "schedule_meeting",    description: "Schedule a meeting (requires user approval via HITL)",    schema: z.object({      reason: z.string().describe("Reason for the meeting"),      durationMinutes: z.number().optional().describe("Duration in minutes"),    }),  },);const searchFlights = tool(  async ({ flights }) => JSON.stringify(searchFlightsImpl(flights)),  {    name: "search_flights",    description: "Search for available flights",    schema: z.object({      flights: z        .array(          z.object({            airline: z.string(),            airlineLogo: z.string().optional(),            flightNumber: z.string(),            origin: z.string(),            destination: z.string(),            date: z.string(),            departureTime: z.string(),            arrivalTime: z.string(),            duration: z.string(),            status: z.string(),            statusColor: z.string().optional(),            price: z.string(),            currency: z.string().optional(),          }),        )        .describe("Array of flight results"),    }),  },);// Dynamic A2UI via the canonical ag-ui factory (same as beautiful_chat /// a2ui_dynamic). A secondary LLM designs the surface; the factory forces the// host catalog and emits the a2ui_operations envelope. Replaces the prior// hand-rolled generate_a2ui tool.const generateA2ui = getA2UITools({  model: new ChatOpenAI({ model: "gpt-5-mini" }),  defaultCatalogId: "copilotkit://app-dashboard-catalog",});const tools = [  getWeather,  queryData,  manageSalesTodos,  getSalesTodos,  scheduleMeeting,  searchFlights,  generateA2ui,];// ---------------------------------------------------------------------------// 3. Chat node — binds backend + frontend tools, invokes the model// ---------------------------------------------------------------------------async function chatNode(state: AgentState, config: RunnableConfig) {  const model = makeChatOpenAI(config, { model: "gpt-5-mini" });  const modelWithTools = model.bindTools!([    ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),    ...tools,  ]);  const systemMessage = new SystemMessage({    content: `You are a helpful assistant. The current proverbs are ${JSON.stringify(state.proverbs)}.`,  });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    config,  );  return { messages: response };}// ---------------------------------------------------------------------------// 4. Routing — send tool calls to tool_node unless they're CopilotKit actions// ---------------------------------------------------------------------------function shouldContinue({ messages, copilotkit }: AgentState) {  const lastMessage = messages[messages.length - 1] as AIMessage;  if (lastMessage.tool_calls?.length) {    const actions = copilotkit?.actions;    const toolCallName = lastMessage.tool_calls![0].name;    if (!actions || actions.every((action) => action.name !== toolCallName)) {      return "tool_node";    }  }  return "__end__";}// ---------------------------------------------------------------------------// 5. Compile the graph// ---------------------------------------------------------------------------const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNode)  .addNode("tool_node", new ToolNode(tools))  .addEdge(START, "chat_node")  .addEdge("tool_node", "chat_node")  .addConditionalEdges("chat_node", shouldContinue as any);const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

## What is this?#

`<CopilotPopup>` is a prebuilt floating launcher that opens an overlay chat window on top of your page content. It's the lightest-weight way to add a copilot to an existing app. Drop it in once and a bubble appears in the corner ready to chat.

## When should I use this?#

Use the popup when you want:

  * A minimal-footprint copilot that overlays existing content on demand
  * A launcher you can place on top of any page without reflowing the layout
  * A quick assistant bubble that users open for short, task-focused chats



If you need chat to live alongside your content rather than on top of it, use [CopilotSidebar](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/sidebar). For a fully embedded chat pane, use [`<CopilotChat>`](https://docs.copilotkit.ai/langgraph-typescript/prebuilt-components/chat) directly.

## Basic setup#

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotPopup>` as a sibling of your main content. The example below opens the popup by default and customizes the input placeholder via `labels`:
    
    
    import { CopilotKit, CopilotPopup } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotPopup`. That one is the [deprecated v1 popup](https://docs.copilotkit.ai/langgraph-typescript/migrate/v2). This page documents the v2 popup, which you import from `@copilotkit/react-core/v2`.

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="prebuilt-popup">      <MainContent />      <CopilotPopup        agentId="prebuilt-popup"        defaultOpen={true}        labels={{          chatInputPlaceholder: "Ask the popup anything...",        }}      />      <Suggestions />    </CopilotKit>

## Configuring the popup#

`<CopilotPopup>` accepts the same props as `<CopilotChat>` plus a few of its own. Commonly used options:

Prop| Description  
---|---  
`defaultOpen`| Whether the popup starts open on first render.  
`agentId`| Agent slug the popup should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy for the header, placeholder, and disclaimer.  
`header`| Slot for the popup header bar — see the [slot system](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/slots).  
`toggleButton`| Slot for the floating launcher button.  
  
## Styling#

`CopilotPopup` participates in the slot system, so every piece of its UI is customizable, from Tailwind classes on the message view to a full component swap for the header or toggle button. See [custom look and feel](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/slots) for the full slot reference.

### On this page

What is this?When should I use this?Basic setupConfiguring the popupStyling
