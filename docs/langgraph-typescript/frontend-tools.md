---
url: https://docs.copilotkit.ai/langgraph-typescript/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:12.625853+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/langgraph-typescript/frontend-tools/

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

Frontend-tools

Basics

# Frontend Tools

Let your agent interact with and update your application's UI.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

frontend-tools.ts

page.tsx

route.ts
    
    
    /** * LangGraph TypeScript agent backing the Frontend Tools (In-App Actions) demo. * * The demo is about frontend tools — the agent has no custom backend tools. * CopilotKit forwards the frontend tool schemas to the agent at runtime via * `state.copilotkit.actions`; the agent binds them when invoking the model, * and the handler executes in the browser. */import { makeChatOpenAI } from "./openai-headers";// region: setupimport type { RunnableConfig } from "@langchain/core/runnables";import { SystemMessage } from "@langchain/core/messages";import { MemorySaver, START, StateGraph } from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";// CopilotKit forwards frontend tools to the agent via// `state.copilotkit.actions`. `CopilotKitStateAnnotation` adds that// channel to your graph's state; `convertActionsToDynamicStructuredTools`// turns the forwarded action schemas into LangChain tools you can bind// at model-invocation time.const AgentStateAnnotation = CopilotKitStateAnnotation;export type AgentState = typeof AgentStateAnnotation.State;const SYSTEM_PROMPT = "You are a helpful, concise assistant.";async function runChatNode(  state: AgentState,  config: RunnableConfig,  model: ChatOpenAI,) {  const modelWithTools = model.bindTools!([    ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),  ]);  const response = await modelWithTools.invoke(    [new SystemMessage({ content: SYSTEM_PROMPT }), ...state.messages],    config,  );  return { messages: response };}async function chatNode(state: AgentState, config: RunnableConfig) {  return runChatNode(    state,    config,    new ChatOpenAI({ temperature: 0, model: "gpt-5-mini" }),  );}function compileGraph(node: typeof chatNode) {  return new StateGraph(AgentStateAnnotation)    .addNode("chat_node", node)    .addEdge(START, "chat_node")    .addEdge("chat_node", "__end__")    .compile({ checkpointer: new MemorySaver() });}export const graph = compileGraph(chatNode);// endregion// The LangGraph CLI targets this export so showcase probes retain inbound// x-* header forwarding; the public `graph` above stays copy-pasteable.async function chatNodeWithHeaders(state: AgentState, config: RunnableConfig) {  return runChatNode(    state,    config,    makeChatOpenAI(config, { temperature: 0, model: "gpt-5-mini" }),  );}export const showcaseGraph = compileGraph(chatNodeWithHeaders);

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/langgraph-typescript/inspector).

## What is this?#

Frontend tools let your agent define and invoke client-side functions that run entirely in the user's browser. Because the handler executes on the frontend, it has direct access to component state, browser APIs, and any third-party UI library the page already uses. That's how an agent can "reach into" the app: update React state, trigger animations, read `localStorage`, pop a toast, or steer the user's view.

This page covers the "agent drives the UI" shape of frontend tools. The same primitive also powers Generative UI and Human-in-the-loop; see those pages for interaction patterns.

## When should I use this?#

Use frontend tools when your agent needs to:

  * Read or modify React component state
  * Access browser APIs like `localStorage`, `sessionStorage`, or cookies
  * Trigger UI updates, animations, or transitions
  * Show alerts, toasts, or notifications
  * Interact with third-party frontend libraries
  * Perform anything that requires the user's immediate browser context



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

Register a frontend tool with `useFrontendTool`. Give it a name, a Zod schema for parameters, and a handler. The agent can then call it like any other tool and your frontend runs it in the browser.

page.tsx
    
    
    import React, { useState } from "react";import {  CopilotKit,  CopilotSidebar,  useFrontendTool,} from "@copilotkit/react-core/v2";import { z } from "zod";import { Background, DEFAULT_BACKGROUND } from "./background";import { useFrontendToolsSuggestions } from "./suggestions";function Chat() {  const [background, setBackground] = useState<string>(DEFAULT_BACKGROUND);  useFrontendTool({    name: "change_background",    description:      "Change the page background. Accepts any valid CSS background value — colors, linear or radial gradients, etc.",    parameters: z.object({      background: z        .string()        .describe("The CSS background value. Prefer gradients."),    }),    handler: async ({ background }) => {      setBackground(background);      return { status: "success" };    },  });

The handler receives the parsed, type-safe parameters and can do anything the browser can: update state, call an API, touch the DOM. Its return value is sent back to the agent as the tool result so the model can reason about what happened.

page.tsx
    
    
        handler: async ({ background }) => {      setBackground(background);      return { status: "success" };    },

## Registering a list of tools#

`useFrontendTool` registers one tool per call, so it cannot be called in a loop over a list whose length changes between renders. When the set of tools comes from state, from props, or from a backend response, use [`useFrontendTools`](https://docs.copilotkit.ai/reference/hooks/useFrontendTools) instead. It takes an array and runs a single effect over it, so the array can be empty on one render and hold twenty entries on the next.
    
    
    useFrontendTools(
      reports.map((report) => ({
        name: `open_${report.id}`,
        description: `Open the ${report.title} report`,
        handler: async () => navigate(`/reports/${report.id}`),
      })),
      [navigate],
    );

Tools that leave the array are unregistered, tools that join it are registered, and a re-render that produces an equal list does not re-register anything. A description built from your data stays current on its own. The second argument is for values a handler closes over, such as `navigate` above.

### On this page

What is this?When should I use this?How it works in codeRegistering a list of tools
