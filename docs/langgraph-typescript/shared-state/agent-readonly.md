---
url: https://docs.copilotkit.ai/langgraph-typescript/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:12:05.054000+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/langgraph-typescript/shared-state/agent-readonly/

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

# Agent Read-Only Context

Publish UI values to the agent as a one-way read-only channel via useAgentContext.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

readonly-state.ts

page.tsx

route.ts
    
    
    /** * LangGraph TypeScript agent backing the Shared State (Agent Read-Only) demo. * * Demonstrates the `useAgentContext` hook from @copilotkit/react-core/v2: * the frontend provides READ-ONLY context *to* the agent. This is the * reverse direction of writable-shared-state — the UI cannot be edited by * the agent, but the agent reads this context on every turn via * CopilotKit's state forwarding, which routes the context entries into the * model's message history. * * No custom state, no tools: this is the minimal shape of the * useAgentContext pattern. The agent just reads whatever context the * frontend registered and answers accordingly. */import type { RunnableConfig } from "@langchain/core/runnables";import { SystemMessage } from "@langchain/core/messages";import { MemorySaver, START, StateGraph } from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import { makeChatOpenAI } from "./openai-headers";import { CopilotKitStateAnnotation } from "@copilotkit/sdk-js/langgraph";const AgentStateAnnotation = CopilotKitStateAnnotation;export type AgentState = typeof AgentStateAnnotation.State;const SYSTEM_PROMPT =  "You are a helpful, concise assistant. The frontend may provide " +  "read-only context about the user (e.g. name, timezone, recent " +  "activity) via the `useAgentContext` hook. Always consult that " +  "context when it is relevant — address the user by name if known, " +  "respect their timezone when mentioning times, and reference " +  "recent activity when it helps you answer. Keep responses short.";async function runChatNode(  state: AgentState,  config: RunnableConfig,  model: ChatOpenAI,) {  // Inject read-only context from useAgentContext / useCopilotReadable.  // Mirrors the `createAppContextBeforeAgent` logic in CopilotKitMiddleware:  // context may be a string or an object — stringify it and prepend as a  // system message right after the main system prompt.  const appContext = state.copilotkit?.context;  const isEmptyContext =    !appContext ||    (typeof appContext === "string" && appContext.trim() === "") ||    (typeof appContext === "object" && Object.keys(appContext).length === 0);  const systemMessages: SystemMessage[] = [    new SystemMessage({ content: SYSTEM_PROMPT }),  ];  if (!isEmptyContext) {    const contextContent =      typeof appContext === "string"        ? appContext        : JSON.stringify(appContext, null, 2);    systemMessages.push(      new SystemMessage({ content: `App Context:\n${contextContent}` }),    );  }  const response = await model.invoke(    [...systemMessages, ...state.messages],    config,  );  return { messages: response };}export async function chatNode(state: AgentState, config: RunnableConfig) {  return runChatNode(state, config, new ChatOpenAI({ model: "gpt-5.4" }));}// Keep the executable showcase graph on the header-forwarding model while the// extracted chat node above uses only the public ChatOpenAI constructor.async function chatNodeWithHeaders(state: AgentState, config: RunnableConfig) {  return runChatNode(    state,    config,    makeChatOpenAI(config, { model: "gpt-5.4" }),  );}const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNodeWithHeaders)  .addEdge(START, "chat_node")  .addEdge("chat_node", "__end__");const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Context**. The values you publish with `useAgentContext` appear here.

More detail: [Inspector](https://docs.copilotkit.ai/langgraph-typescript/inspector).

## What is this?#

Sometimes you want the agent to _know_ something about the current UI, like the logged-in user, the current page, or a recent activity log, but you don't want the agent to be able to modify it. That's what `useAgentContext` is for: a one-way **UI → agent** channel for read-only context.

Unlike full shared state (where the agent can call tools that mutate the state back to the UI), `useAgentContext` values are pure inputs. The agent sees them on every turn via the runtime's context injection, but it has no setter and no tool to write them back.

## When should I use this?#

Reach for `useAgentContext` instead of full shared state when:

  * The value is **UI-owned** and has no meaning to the agent beyond "what the user is looking at right now".
  * The agent should read but never write (user identity, feature flags, selected record, scroll position).
  * You want the value to automatically unregister on unmount (e.g. the "current record" context disappears when you leave the page).



Think of it as "props for the agent".

## How it works in code#

### Install the CopilotKit LangGraph SDK
    
    
    npm install @copilotkit/sdk-js

### Read CopilotKit context in your graph

`useAgentContext` entries arrive on `state.copilotkit.context`. Extend your graph state with `CopilotKitStateAnnotation`, then prepend that read-only context as a system message before invoking the model.

readonly-state.ts
    
    
    async function runChatNode(
      state: AgentState,
      config: RunnableConfig,
      model: ChatOpenAI,
    ) {
      // Inject read-only context from useAgentContext / useCopilotReadable.
      // Mirrors the `createAppContextBeforeAgent` logic in CopilotKitMiddleware:
      // context may be a string or an object — stringify it and prepend as a
      // system message right after the main system prompt.
      const appContext = state.copilotkit?.context;
      const isEmptyContext =
        !appContext ||
        (typeof appContext === "string" && appContext.trim() === "") ||
        (typeof appContext === "object" && Object.keys(appContext).length === 0);
    
      const systemMessages: SystemMessage[] = [
        new SystemMessage({ content: SYSTEM_PROMPT }),
      ];
    
      if (!isEmptyContext) {
        const contextContent =
          typeof appContext === "string"
            ? appContext
            : JSON.stringify(appContext, null, 2);
        systemMessages.push(
          new SystemMessage({ content: `App Context:\n${contextContent}` }),
        );
      }
    
      const response = await model.invoke(
        [...systemMessages, ...state.messages],
        config,
      );
    
      return { messages: response };
    }
    
    export async function chatNode(state: AgentState, config: RunnableConfig) {
      return runChatNode(state, config, new ChatOpenAI({ model: "gpt-5.4" }));
    }

Call `useAgentContext({ description, value })` once per value you want to publish. Each call registers a dynamic context entry with the runtime that is:

  * Refreshed whenever `value` changes (React re-renders).
  * Automatically removed when the component unmounts.
  * Surfaced to the agent via the backend's `CopilotKitMiddleware`, which threads the entries into the model's message history on every turn.



page.tsx
    
    
      useAgentContext({    description: "The currently logged-in user's display name",    value: userName,  });  useAgentContext({    description: "The user's IANA timezone (used when mentioning times)",    value: userTimezone,  });  useAgentContext({    description: "The user's recent activity in the app, newest first",    value: recentActivity,  });

The `description` is important: it's a short human-readable label the agent sees alongside the value, so it knows what to do with it. Treat it like a parameter docstring.

## Wire it to your own state#

`useAgentContext` doesn't care where the value comes from: local state, a React Context, Redux, a query cache, anything. The only requirement is that the identity of the value is stable enough for React to avoid a render loop. In the demo we use a handful of `useState` hooks; in a real app these would likely come from an auth provider, a router hook, and your domain state stores.

page.tsx
    
    
    import React, { useState } from "react";import {  CopilotKit,  CopilotPopup,  useAgentContext,} from "@copilotkit/react-core/v2";import { ACTIVITIES, DemoLayout } from "./demo-layout";import { useReadonlyStateAgentContextSuggestions } from "./suggestions";export default function ReadonlyStateAgentContextDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit"      agent="readonly-state-agent-context"    >      <DemoContent />      <CopilotPopup        agentId="readonly-state-agent-context"        defaultOpen={true}        labels={{ chatInputPlaceholder: "Ask about your context..." }}      />    </CopilotKit>  );}function DemoContent() {  const [userName, setUserName] = useState("Atai");  const [userTimezone, setUserTimezone] = useState("America/Los_Angeles");  const [recentActivity, setRecentActivity] = useState<string[]>([    ACTIVITIES[0],    ACTIVITIES[2],  ]);

## Read-only, by design#

Because the agent never sees a setter or a mutation tool for these values, there's no way for a confused LLM to "update" them. That makes `useAgentContext` the right tool whenever the value in question is an input, not a field: the "context object passed to the agent on every turn", rather than "shared workspace you both edit".

When you need both reads _and_ writes, you want full **[shared state](https://docs.copilotkit.ai/langgraph-typescript/shared-state)** instead.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/langgraph-typescript/shared-state)** — bidirectional reads + writes.
  * **[State streaming](https://docs.copilotkit.ai/langgraph-typescript/shared-state/streaming)** — stream agent-written state back to the UI during a run.


