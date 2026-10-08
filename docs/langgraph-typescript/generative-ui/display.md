---
url: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:18.622523+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/display/

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

[LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript)[Build Generative UI](https://docs.copilotkit.ai/langgraph-typescript/generative-ui)

# Display components

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

gen-ui-tool-based.ts

page.tsx

bar-chart.tsx

route.ts
    
    
    /** * Tool-Based Generative UI agent — TypeScript port of gen_ui_tool_based.py. * * The frontend registers `render_bar_chart` and `render_pie_chart` via * `useComponent`. CopilotKit's LangGraph middleware forwards those as actions * on `state.copilotkit.actions`; we bind them so the model can call them. * * There are no backend tools — the chart components are rendered on the * frontend — so the graph ends after the model turn (no tool_node). */import { RunnableConfig } from "@langchain/core/runnables";import { SystemMessage } from "@langchain/core/messages";import {  Annotation,  MemorySaver,  START,  StateGraph,  messagesStateReducer,  BaseMessage,} from "@langchain/langgraph";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";import { makeChatOpenAI } from "./openai-headers";const SYSTEM_PROMPT = `You are a data visualization assistant.When the user asks for a chart, call \`render_bar_chart\` or \`render_pie_chart\`with a concise title, short description, and a \`data\` array of\`{label, value}\` items. Pick bar for comparisons over a small set ofcategories; pick pie for composition / share-of-whole.If the user names a chart subject but does NOT supply concrete numbers(e.g. "show me a pie chart of website traffic by source"), do NOT askthem for data. Invent plausible illustrative sample values yourself,call the appropriate \`render_*\` tool immediately, and briefly note inthe follow-up that the values are illustrative samples. Always renderthe chart on the first turn -- never reply with a clarifying questionasking for the data.Keep chat responses brief -- let the chart do the talking.`;// Define `messages` explicitly (concrete channel type) rather than relying on// the spread of `CopilotKitStateAnnotation.spec` alone — the langgraph-api// schema pre-warmer skips graphs whose state exposes no concrete channel, so// this graph must carry an explicit `messages` annotation like every other// registering graph in this package.const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,  messages: Annotation<BaseMessage[]>({    reducer: messagesStateReducer,    default: () => [],  }),});type AgentState = typeof AgentStateAnnotation.State;async function chatNode(state: AgentState, config: RunnableConfig) {  const model = makeChatOpenAI(config, { temperature: 0, model: "gpt-5-mini" });  const modelWithTools = model.bindTools!(    convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),  );  const response = await modelWithTools.invoke(    [new SystemMessage({ content: SYSTEM_PROMPT }), ...state.messages],    config,  );  return { messages: response };}const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNode)  .addEdge(START, "chat_node");const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

## What is this?#

Render-only generative UI lets you register React components as tools your agent can invoke. When the agent calls the tool, CopilotKit renders your component directly in the chat with the tool's arguments as props; no handler logic or user interaction required.

page.tsxchart.tsx
    
    
    useComponent({
    name: "showChart",
    description: "Populate data and show the user a chart",
    parameters: ChartProps,
    render: Chart
    });
    
    
    
    export const ChartProps = z.object({
      title: z.string(),
      data: z.array(z.object({ label: z.string(), value: z.number() })),
    });
    
    export function Chart({ title, data }: z.infer<typeof ChartProps>) {
      return (
        <div>
          <h3>{title}</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
              <XAxis dataKey="label" /><YAxis /><Tooltip />
              <Bar dataKey="value" fill="#6366f1" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      );
    }

## When should I use this?#

Use render-only generative UI when you want to:

  * Display rich UI (cards, charts, tables) inline in the chat
  * Show structured data from agent responses
  * Render previews, status indicators, or visual feedback
  * Let the agent present information beyond plain text



## How it works in code#

### Install the CopilotKit LangGraph SDK
    
    
    npm install @copilotkit/sdk-js

### Wire CopilotKit state + tools into your graph

Frontend tools registered with `useFrontendTool` arrive on the agent's state at `state.copilotkit.actions`. Use `CopilotKitStateAnnotation` to expose that channel on your graph, then call `convertActionsToDynamicStructuredTools(...)` inside your chat node to bind the LLM to those actions.

frontend-tools.ts
    
    
    import type { RunnableConfig } from "@langchain/core/runnables";
    import { SystemMessage } from "@langchain/core/messages";
    import { MemorySaver, START, StateGraph } from "@langchain/langgraph";
    import { ChatOpenAI } from "@langchain/openai";
    import {
      convertActionsToDynamicStructuredTools,
      CopilotKitStateAnnotation,
    } from "@copilotkit/sdk-js/langgraph";
    
    // CopilotKit forwards frontend tools to the agent via
    // `state.copilotkit.actions`. `CopilotKitStateAnnotation` adds that
    // channel to your graph's state; `convertActionsToDynamicStructuredTools`
    // turns the forwarded action schemas into LangChain tools you can bind
    // at model-invocation time.
    const AgentStateAnnotation = CopilotKitStateAnnotation;
    export type AgentState = typeof AgentStateAnnotation.State;
    
    const SYSTEM_PROMPT = "You are a helpful, concise assistant.";
    
    async function runChatNode(
      state: AgentState,
      config: RunnableConfig,
      model: ChatOpenAI,
    ) {
      const modelWithTools = model.bindTools!([
        ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),
      ]);
    
      const response = await modelWithTools.invoke(
        [new SystemMessage({ content: SYSTEM_PROMPT }), ...state.messages],
        config,
      );
    
      return { messages: response };
    }
    
    async function chatNode(state: AgentState, config: RunnableConfig) {
      return runChatNode(
        state,
        config,
        new ChatOpenAI({ temperature: 0, model: "gpt-5-mini" }),
      );
    }
    
    function compileGraph(node: typeof chatNode) {
      return new StateGraph(AgentStateAnnotation)
        .addNode("chat_node", node)
        .addEdge(START, "chat_node")
        .addEdge("chat_node", "__end__")
        .compile({ checkpointer: new MemorySaver() });
    }
    
    export const graph = compileGraph(chatNode);

### Call a frontend tool from a node with no model

A node does not need a model to call a frontend tool. Return an `AIMessage` with a `tool_calls` entry. This example calls the `change_background` tool that the frontend above registers. When the run ends, CopilotKit runs the matching `useFrontendTool` handler in the browser. Then it starts a follow-up run with the result as a `ToolMessage`. Route that run to a node that reads the result, so the graph does not call the tool again:

src/agent.ts
    
    
    import { randomUUID } from "node:crypto";
    import { AIMessage, ToolMessage } from "@langchain/core/messages";
    import { END, START, StateGraph } from "@langchain/langgraph";
    import { CopilotKitStateAnnotation } from "@copilotkit/sdk-js/langgraph";
    
    type AgentState = typeof CopilotKitStateAnnotation.State;
    
    // Ask the frontend to run `change_background`. No model call.
    async function requestBackground(state: AgentState) {
      return {
        messages: [
          new AIMessage({
            content: "",
            tool_calls: [
              {
                id: randomUUID(),
                name: "change_background",
                args: { background: "linear-gradient(135deg, #1e3a8a, #9333ea)" },
                type: "tool_call",
              },
            ],
          }),
        ],
      };
    }
    
    // Runs on the follow-up run, after the frontend returns the tool result.
    async function confirm(state: AgentState) {
      const result = state.messages.at(-1);
      return {
        messages: [new AIMessage(`The frontend returned: ${result?.content}`)],
      };
    }
    
    export const graph = new StateGraph(CopilotKitStateAnnotation)
      .addNode("request_background", requestBackground)
      .addNode("confirm", confirm)
      .addConditionalEdges(START, (state: AgentState) => {
        const last = state.messages.at(-1);
        return last && ToolMessage.isInstance(last)
          ? "confirm"
          : "request_background";
      })
      .addEdge("request_background", END)
      .addEdge("confirm", END)
      .compile();

The tool call must be in the graph state. `copilotkitEmitToolCall` alone only streams the call. At the end of the run, the messages from the graph state replace the streamed ones, so the handler never runs.

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });
