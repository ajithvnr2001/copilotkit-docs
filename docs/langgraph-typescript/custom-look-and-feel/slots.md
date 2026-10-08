---
url: https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/slots/
title: Slots (Subcomponents)
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:10:53.217982+00:00
---

# Slots (Subcomponents)

> Source: https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/slots/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/reasoning-messages)

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

Slots (Subcomponents)

BasicsChatCustom Look and Feel

# Slots (Subcomponents)

Customize any part of the chat UI by overriding individual sub-components via slots.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

graph.ts

page.tsx

slot-wrappers.tsx

route.ts
    
    
    /** * LangGraph TypeScript agent — CopilotKit showcase integration * * Defines a graph with a chat node and all showcase tools, * wired to CopilotKit via the sdk-js LangGraph adapter so frontend actions * and shared state flow seamlessly. */import { z } from "zod";import type { RunnableConfig } from "@langchain/core/runnables";import { tool } from "@langchain/core/tools";import { ToolNode } from "@langchain/langgraph/prebuilt";import type { AIMessage } from "@langchain/core/messages";import { SystemMessage } from "@langchain/core/messages";import {  MemorySaver,  START,  StateGraph,  Annotation,} from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import { getA2UITools } from "@ag-ui/langgraph";import { makeChatOpenAI } from "./openai-headers";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";import {  getWeatherImpl,  queryDataImpl,  manageSalesTodosImpl,  getSalesTodosImpl,  scheduleMeetingImpl,  searchFlightsImpl,} from "../../shared-tools";// ---------------------------------------------------------------------------// 1. Agent state — extends CopilotKit state with a proverbs list// ---------------------------------------------------------------------------const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,  proverbs: Annotation<string[]>,});export type AgentState = typeof AgentStateAnnotation.State;// ---------------------------------------------------------------------------// 2. Tools — shared implementations wrapped for LangChain// ---------------------------------------------------------------------------const getWeather = tool(  async ({ location }) => JSON.stringify(getWeatherImpl(location)),  {    name: "get_weather",    description: "Get current weather for a location",    schema: z.object({      location: z.string().describe("City name"),    }),  },);const queryData = tool(  async ({ query }) => JSON.stringify(queryDataImpl(query)),  {    name: "query_data",    description: "Query financial database for chart data",    schema: z.object({      query: z.string().describe("Natural language query"),    }),  },);const manageSalesTodos = tool(  async ({ todos }) => JSON.stringify(manageSalesTodosImpl(todos)),  {    name: "manage_sales_todos",    description: "Create or update the sales todo list",    schema: z.object({      todos: z        .array(          z.object({            id: z.string().optional(),            title: z.string(),            stage: z.string().optional(),            value: z.number().optional(),            dueDate: z.string().optional(),            assignee: z.string().optional(),            completed: z.boolean().optional(),          }),        )        .describe("Array of sales todo items"),    }),  },);const getSalesTodos = tool(  async ({ currentTodos }) => JSON.stringify(getSalesTodosImpl(currentTodos)),  {    name: "get_sales_todos",    description: "Get the current sales todo list",    schema: z.object({      currentTodos: z        .array(          z.object({            id: z.string().optional(),            title: z.string().optional(),            stage: z.string().optional(),            value: z.number().optional(),            dueDate: z.string().optional(),            assignee: z.string().optional(),            completed: z.boolean().optional(),          }),        )        .optional()        .nullable()        .describe("Current todos if any"),    }),  },);const scheduleMeeting = tool(  async ({ reason, durationMinutes }) =>    JSON.stringify(scheduleMeetingImpl(reason, durationMinutes)),  {    name: "schedule_meeting",    description: "Schedule a meeting (requires user approval via HITL)",    schema: z.object({      reason: z.string().describe("Reason for the meeting"),      durationMinutes: z.number().optional().describe("Duration in minutes"),    }),  },);const searchFlights = tool(  async ({ flights }) => JSON.stringify(searchFlightsImpl(flights)),  {    name: "search_flights",    description: "Search for available flights",    schema: z.object({      flights: z        .array(          z.object({            airline: z.string(),            airlineLogo: z.string().optional(),            flightNumber: z.string(),            origin: z.string(),            destination: z.string(),            date: z.string(),            departureTime: z.string(),            arrivalTime: z.string(),            duration: z.string(),            status: z.string(),            statusColor: z.string().optional(),            price: z.string(),            currency: z.string().optional(),          }),        )        .describe("Array of flight results"),    }),  },);// Dynamic A2UI via the canonical ag-ui factory (same as beautiful_chat /// a2ui_dynamic). A secondary LLM designs the surface; the factory forces the// host catalog and emits the a2ui_operations envelope. Replaces the prior// hand-rolled generate_a2ui tool.const generateA2ui = getA2UITools({  model: new ChatOpenAI({ model: "gpt-5-mini" }),  defaultCatalogId: "copilotkit://app-dashboard-catalog",});const tools = [  getWeather,  queryData,  manageSalesTodos,  getSalesTodos,  scheduleMeeting,  searchFlights,  generateA2ui,];// ---------------------------------------------------------------------------// 3. Chat node — binds backend + frontend tools, invokes the model// ---------------------------------------------------------------------------async function chatNode(state: AgentState, config: RunnableConfig) {  const model = makeChatOpenAI(config, { model: "gpt-5-mini" });  const modelWithTools = model.bindTools!([    ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),    ...tools,  ]);  const systemMessage = new SystemMessage({    content: `You are a helpful assistant. The current proverbs are ${JSON.stringify(state.proverbs)}.`,  });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    config,  );  return { messages: response };}// ---------------------------------------------------------------------------// 4. Routing — send tool calls to tool_node unless they're CopilotKit actions// ---------------------------------------------------------------------------function shouldContinue({ messages, copilotkit }: AgentState) {  const lastMessage = messages[messages.length - 1] as AIMessage;  if (lastMessage.tool_calls?.length) {    const actions = copilotkit?.actions;    const toolCallName = lastMessage.tool_calls![0].name;    if (!actions || actions.every((action) => action.name !== toolCallName)) {      return "tool_node";    }  }  return "__end__";}// ---------------------------------------------------------------------------// 5. Compile the graph// ---------------------------------------------------------------------------const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNode)  .addNode("tool_node", new ToolNode(tools))  .addEdge(START, "chat_node")  .addEdge("tool_node", "chat_node")  .addConditionalEdges("chat_node", shouldContinue as any);const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

## What is this?#

Every CopilotKit chat component is built from composable **slots** , named sub-components you can override individually. The slot system gives you three levels of customization without needing to rebuild the entire UI:

  1. **Tailwind classes** — pass a string to add/override CSS classes
  2. **Props override** — pass an object to override specific props on the default component
  3. **Custom component** — pass your own React component to fully replace a slot



Slots are recursive: you can drill into nested sub-components at any depth.

## What it looks like in code#

The `chat-slots` cell above overrides three slots on a single `<CopilotChat>` — the welcome screen, the assistant message card, and the input's disclaimer. Each slot is just a prop; the demo extracts them into locals so the override points are easy to see.

### Welcome screen slot#

The `welcomeScreen` prop replaces the empty-state view shown before the first message is sent. The demo swaps in a gradient card that still renders the default input and suggestions:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;

### Assistant message slot#

Drill into `messageView={{ assistantMessage: ... }}` to wrap every assistant response. The cell wraps the default component with a tinted card and a small "slot" badge so you can see the override is active during the message flow:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;  const messageView = {    assistantMessage:      CustomAssistantMessage as unknown as typeof CopilotChatAssistantMessage,  };

### Disclaimer slot#

The `input={{ disclaimer: ... }}` sub-slot lets you replace the small text shown below the input. The demo uses it to display a visibly tagged disclaimer so reviewers can tell the override is still in effect once the welcome screen is gone:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;  const messageView = {    assistantMessage:      CustomAssistantMessage as unknown as typeof CopilotChatAssistantMessage,  };  const input = {    disclaimer:      CustomDisclaimer as unknown as typeof CopilotChatInput.Disclaimer,  };

## Tailwind Classes#

The simplest way to customize a slot. Pass a Tailwind class string and it will be merged with the default component's classes.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    export function Chat() {
      return (
        <CopilotChat
          messageView="bg-gray-50 dark:bg-gray-900 p-4"
          input="border-2 border-blue-400 rounded-xl"
        />
      );
    }

## Props Override#

Pass an object to override specific props on the default component. This is useful for adding `className`, event handlers, data attributes, or any other prop the default component accepts.

page.tsx
    
    
    <CopilotChat
      messageView={{
        className: "my-custom-messages",
        "data-testid": "message-view",
      }}
      input={{ autoFocus: true }}
    />

## Custom Components#

For full control, pass your own React component. It receives all the same props as the default component.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    const CustomMessageView = ({ messages, isRunning }) => (
      <div className="space-y-4 p-6">
        {messages?.map((msg) => (
          <div key={msg.id} className={msg.role === "user" ? "text-right" : "text-left"}>
            {msg.content}
          </div>
        ))}
        {isRunning && <div className="animate-pulse">Thinking...</div>}
      </div>
    );
    
    export function Chat() {
      return <CopilotChat messageView={CustomMessageView} />;
    }

## Nested Slots (Drill-Down)#

Slots are recursive. You can customize sub-components at any depth by nesting objects.

### Two levels deep#

Override the assistant message's toolbar within the message view:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          toolbar: CustomToolbar,
          copyButton: CustomCopyButton,
        },
        userMessage: CustomUserMessage,
      }}
    />

### Three levels deep#

Override a specific button inside the assistant message toolbar:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          copyButton: ({ onClick }) => (
            <button onClick={onClick}>Copy</button>
          ),
        },
      }}
    />

The `assistantMessage` slot also holds `markdownRenderer`, which controls how assistant markdown is rendered. It has its own guide: [Markdown Rendering](https://docs.copilotkit.ai/langgraph-typescript/custom-look-and-feel/markdown).

## Labels#

Customize any text string in the UI via the `labels` prop. This is a separate convenience prop on `CopilotChat`, `CopilotSidebar`, and `CopilotPopup`, not part of the slot system.

page.tsx
    
    
    <CopilotChat
      labels={{
        chatInputPlaceholder: "Ask your agent anything...",
        welcomeMessageText: "How can I help you today?",
        chatDisclaimerText: "AI responses may be inaccurate.",
      }}
    />

## Available Slots#

### `CopilotChat` / `CopilotSidebar` / `CopilotPopup`#

These are the root-level slot props available on all chat components:

Slot| Description  
---|---  
`messageView`| The message list container.  
`scrollView`| The scroll container with auto-scroll behavior.  
`input`| The text input area with send/transcribe controls.  
`suggestionView`| The suggestion pills shown below messages.  
`welcomeScreen`| The initial empty-state screen (pass `false` to disable).  
  
`CopilotSidebar` and `CopilotPopup` also have:

Slot| Description  
---|---  
`header`| The modal header bar.  
`toggleButton`| The open/close toggle button.  
  
### On this page

What is this?What it looks like in codeWelcome screen slotAssistant message slotDisclaimer slotTailwind ClassesProps OverrideCustom ComponentsNested Slots (Drill-Down)Two levels deepThree levels deepLabelsAvailable SlotsCopilotChat / CopilotSidebar / CopilotPopup
