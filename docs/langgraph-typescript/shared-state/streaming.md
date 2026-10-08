---
url: https://docs.copilotkit.ai/langgraph-typescript/shared-state/streaming/
title: State Streaming
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:12:08.563189+00:00
---

# State Streaming

> Source: https://docs.copilotkit.ai/langgraph-typescript/shared-state/streaming/

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

[Shared State](https://docs.copilotkit.ai/langgraph-typescript/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/langgraph-typescript/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/langgraph-typescript/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/langgraph-typescript/shared-state/agent-readonly)

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

InteractivityShared state

# State Streaming

Stream partial agent state updates to the UI while a tool call is still running.

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

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call (writing a full document, drafting an email) appears to the UI as one big burst at the end. For agent-native apps, that feels broken: users expect to watch the output materialise.

**State streaming** forwards the value of a specific tool argument straight into an agent state key _as the argument is being generated_. The UI, subscribed via `useAgent`, re-renders every token.

## When should I use this?#

Use state streaming whenever a tool's output is long-form text or a growing structured value and you want the user to see it assemble in real time. Common shapes:

  * A collaborative writing agent that emits a document
  * A research agent that accumulates a list of findings
  * A planning agent that builds up a step-by-step plan



Without streaming, the user stares at a spinner. With streaming, they see the answer grow token-by-token.

## The backend: one streaming state mapping#

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

The backend pattern is always the same: map one streaming tool argument to one shared-state key. Middleware-backed frameworks usually expose this as a declarative mapping — for example, LangGraph Python's `StateStreamingMiddleware` with `StateItem(...)` entries, or `copilotkitCustomizeConfig` with an `emitIntermediateState` mapping for LangGraph TypeScript graphs. Direct SDK adapters do the same work in their streaming loop by parsing partial tool arguments and emitting `STATE_SNAPSHOT` whenever the mapped value changes. When the LLM streams that argument, CopilotKit writes every partial value into shared state before the tool even finishes executing.

shared-state-streaming.ts
    
    
      const streamingConfig = copilotkitCustomizeConfig(config, {    emitIntermediateState: [      {        stateKey: "document",        tool: "write_document",        toolArgument: "document",      },    ],  });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    streamingConfig,  );

A few things to note:

  * The state key must exist in your agent state (`document` in this demo).
  * The tool and argument names must match the exact LLM-facing tool call you want to forward (`write_document.document` here).
  * When the tool call completes, its final return value is written to the same key, so the streamed partial eventually becomes the authoritative final value.



## The frontend: useAgent + OnStateChanged#

The UI side is identical to any other shared-state subscription: `useAgent` with `OnStateChanged` gives you a reactive `agent.state`. Add `OnRunStatusChanged` if you want a "LIVE" / "done" indicator.

page.tsx
    
    
      // Subscribe to BOTH state changes and run-status changes. The former  // drives the per-token document rerender; the latter toggles the  // "LIVE" badge when the agent starts / stops.  const { agent } = useAgent({    agentId: "shared-state-streaming",    updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],  });

From there, `agent.state.document` is just a string that grows on every token, and `agent.isRunning` tells you whether to show a streaming indicator.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/langgraph-typescript/shared-state)** — the bidirectional read + write pattern this extends.
  * **[Agent read-only context](https://docs.copilotkit.ai/langgraph-typescript/shared-state/agent-readonly)** — for the inverse, UI → agent one-way channel.


