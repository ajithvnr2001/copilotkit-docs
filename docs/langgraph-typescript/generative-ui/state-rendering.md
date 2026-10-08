---
url: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:22.731063+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/state-rendering/

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

State Rendering

Generative UIControlled

# State Rendering

Render your agent's state with custom UI components in real-time.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

shared-state-streaming.ts

page.tsx

document-view.tsx

route.ts
    
    
    /** * LangGraph TypeScript agent backing the Shared State Streaming demo. * * Demonstrates per-token state-delta streaming. The agent writes a long * `document` string into shared agent state via a `write_document` tool; * `copilotkitCustomizeConfig(..., { emitIntermediateState })` tells * CopilotKit to forward every token of the tool's `document` argument * directly into the `document` state key as it is generated. The UI * (useAgent) sees `state.document` grow token-by-token, without waiting * for the tool call to finish. * * This is the canonical per-token state-streaming pattern: * docs.copilotkit.ai/integrations/langgraph/shared-state/predictive-state-updates */import { randomUUID } from "node:crypto";import { z } from "zod";import type { RunnableConfig } from "@langchain/core/runnables";import { tool } from "@langchain/core/tools";import { ToolNode } from "@langchain/langgraph/prebuilt";import type { AIMessage } from "@langchain/core/messages";import { SystemMessage, ToolMessage } from "@langchain/core/messages";import type { ToolRunnableConfig } from "@langchain/core/tools";import {  Annotation,  Command,  MemorySaver,  START,  StateGraph,} from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import { makeChatOpenAI } from "./openai-headers";import {  copilotkitCustomizeConfig,  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";// ---------------------------------------------------------------------------// 1. Shared state — `document` is streamed token-by-token.// ---------------------------------------------------------------------------const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,  document: Annotation<string>,});export type AgentState = typeof AgentStateAnnotation.State;// ---------------------------------------------------------------------------// 2. Tool — `write_document` writes the document into shared state.// ---------------------------------------------------------------------------const writeDocument = tool(  async ({ document }, config: ToolRunnableConfig) => {    const toolCallId = config.toolCall?.id;    if (typeof toolCallId !== "string" || toolCallId.length === 0) {      throw new Error(        "write_document: missing tool_call_id — tool was invoked outside a " +          "ToolNode context. Refusing to emit a ToolMessage with an empty " +          "tool_call_id (OpenAI rejects those).",      );    }    return new Command({      update: {        document,        messages: [          new ToolMessage({            content: "Document written to shared state.",            name: "write_document",            id: randomUUID(),            tool_call_id: toolCallId,          }),        ],      },    });  },  {    name: "write_document",    description:      "Write a document for the user.\n\n" +      "Always call this tool when the user asks you to write or draft " +      "something of any length (an essay, poem, email, summary, etc.). " +      "The `document` argument is streamed *per token* into shared agent " +      "state under the `document` key, so the UI can render it as it is " +      "generated.",    schema: z.object({      document: z.string(),    }),  },);const tools = [writeDocument];// ---------------------------------------------------------------------------// 3. Chat node.// ---------------------------------------------------------------------------const SYSTEM_PROMPT =  "You are a collaborative writing assistant. Whenever the user asks " +  "you to write, draft, or revise any piece of text, ALWAYS call the " +  "`write_document` tool with the full content as a single string in " +  "the `document` argument. Never paste the document into a chat " +  "message directly — the document belongs in shared state and the " +  "UI renders it live as you type.";async function chatNode(state: AgentState, config: RunnableConfig) {  const model = makeChatOpenAI(config, {    model: "gpt-5.4",    modelKwargs: { parallel_tool_calls: false },  });  const modelWithTools = model.bindTools!([    ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),    ...tools,  ]);  const systemMessage = new SystemMessage({ content: SYSTEM_PROMPT });  const streamingConfig = copilotkitCustomizeConfig(config, {    emitIntermediateState: [      {        stateKey: "document",        tool: "write_document",        toolArgument: "document",      },    ],  });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    streamingConfig,  );  return { messages: response };}// ---------------------------------------------------------------------------// 4. Routing — send tool calls to tool_node unless they're CopilotKit//    frontend actions.// ---------------------------------------------------------------------------function shouldContinue({ messages, copilotkit }: AgentState) {  const lastMessage = messages[messages.length - 1] as AIMessage;  if (lastMessage.tool_calls?.length) {    const actions = copilotkit?.actions;    const hasBackendToolCall = lastMessage.tool_calls.some((toolCall) => {      return (        !actions || actions.every((action) => action.name !== toolCall.name)      );    });    if (hasBackendToolCall) {      return "tool_node";    }  }  return "__end__";}// ---------------------------------------------------------------------------// 5. Compile the graph.// ---------------------------------------------------------------------------const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNode)  .addNode("tool_node", new ToolNode(tools))  .addEdge(START, "chat_node")  .addEdge("tool_node", "chat_node")  .addConditionalEdges("chat_node", shouldContinue as any);const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

## What is this?#

State rendering lets you build UI that reflects your agent's state in real-time. As your agent progresses through nodes and emits state updates, your frontend renders those changes, showing progress, drafts, or intermediate results.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## When should I use this?#

Use state rendering when you want to:

  * Show real-time progress (e.g. "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside of the chat



## How it works in code#

On the frontend, subscribe to the agent's state. Each time the backend forwards a fresh value, your component re-renders with the latest partial output.

page.tsx
    
    
      // Subscribe to BOTH state changes and run-status changes. The former  // drives the per-token document rerender; the latter toggles the  // "LIVE" badge when the agent starts / stops.  const { agent } = useAgent({    agentId: "shared-state-streaming",    updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],  });

On the backend, a state-streaming mapping forwards a specific tool argument straight into a state key _as it's being generated_. Some frameworks provide that as middleware; direct SDK adapters can emit `STATE_SNAPSHOT` events from their streaming loop. Either way, the UI can watch the answer assemble token-by-token rather than appearing in one burst between checkpoints.

### Install the CopilotKit LangGraph SDK
    
    
    npm install @copilotkit/sdk-js

### Map generated content into shared state while it streams

Extend your graph state with `CopilotKitStateAnnotation`, then call `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping. This forwards the `write_document.document` tool argument into `state.document` while the model is still generating it.

shared-state-streaming.ts
    
    
    const streamingConfig = copilotkitCustomizeConfig(config, {
      emitIntermediateState: [
        {
          stateKey: "document",
          tool: "write_document",
          toolArgument: "document",
        },
      ],
    });
    
    const response = await modelWithTools.invoke(
      [systemMessage, ...state.messages],
      streamingConfig,
    );

shared-state-streaming.ts
    
    
      const streamingConfig = copilotkitCustomizeConfig(config, {    emitIntermediateState: [      {        stateKey: "document",        tool: "write_document",        toolArgument: "document",      },    ],  });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    streamingConfig,  );

### On this page

What is this?When should I use this?How it works in code
