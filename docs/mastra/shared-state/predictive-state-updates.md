---
url: https://docs.copilotkit.ai/mastra/shared-state/predictive-state-updates/
title: State streaming
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:17:09.726367+00:00
---

# State streaming

> Source: https://docs.copilotkit.ai/mastra/shared-state/predictive-state-updates/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/mastra/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/mastra/shared-state/in-app-agent-write)[State streaming](https://docs.copilotkit.ai/mastra/shared-state/predictive-state-updates)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

State streaming

InteractivityShared state

# State streaming

Stream in-progress agent state updates to the frontend as the agent writes them.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates streaming shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/mastra/feature/shared_state).

## What is this?#

An agent's working memory usually surfaces to the UI once, when a run finishes. But a single run can take many seconds and write a lot of content — a drafted document, a plan, a summary — that the user would rather watch appear **as it is generated**.

**Agent-native applications** reflect what the agent is doing to the end-user **as continuously as possible.** CopilotKit enables this for Mastra by streaming working-memory updates to the frontend token-by-token, so `agent.state` grows live during the run instead of jumping to the final value at the end.

## When should I use this?#

Use this when you want to give the user real-time feedback about what your agent is producing, specifically to:

  * **Keep users engaged** by avoiding long loading indicators
  * **Build trust** by showing the work as it is written
  * Enable **agent steering** — letting users react before the run completes



## How it works#

Mastra injects a built-in `updateWorkingMemory` tool whenever working memory is enabled. When the agent calls it during a run, CopilotKit's Mastra integration intercepts the tool call's **streaming arguments** , parses the growing payload, and emits an initial `STATE_SNAPSHOT` followed by incremental `STATE_DELTA` updates against the working-memory schema. The frontend's `useAgent` subscription re-renders on every delta.

Important

This guide assumes you are embedding your Mastra agent inside Copilot Runtime, like so.
    
    
    const runtime = new CopilotRuntime({
      agents: MastraAgent.getLocalAgents({ mastra, resourceId: "user-1" }),
    });

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Define the streamed state#

Provide a working-memory schema whose field holds the content you want to stream. Here `document` is a single string that the agent will fill in progressively.

mastra/agents/streaming-agent.ts
    
    
    import { openai } from "@ai-sdk/openai";
    import { Agent } from "@mastra/core/agent";
    import { LibSQLStore } from "@mastra/libsql";
    import { Memory } from "@mastra/memory";
    import { z } from "zod";
    
    // 1. Define the streamed state schema
    export const StreamingAgentState = z.object({
      document: z.string().default(""),
    });
    
    // 2. Create the agent with working memory enabled
    export const streamingAgent = new Agent({
      id: "streaming-agent",
      name: "Streaming Agent",
      model: openai("gpt-4o"),
      // The prompt drives the model to write the full document straight into
      // working memory via the built-in updateWorkingMemory tool, rather than
      // pasting it into a chat message.
      instructions: `You are a collaborative writing assistant. Whenever the user asks you to write, draft, or revise anything, call the \`updateWorkingMemory\` tool with the FULL content under the \`document\` field. Never paste the document into a chat message — it belongs in shared state, and the UI renders it live as you stream it.`,
      memory: new Memory({
        storage: new LibSQLStore({ id: "mastra-storage", url: ":memory:" }),
        options: {
          workingMemory: {
            enabled: true, 
            schema: StreamingAgentState, 
          },
        },
      }),
    });

### Observe the stream#

Subscribe to the agent state with `useAgent`. `agent.state.document` updates on every delta as the agent writes, so the panel fills in live.

ui/app/page.tsx
    
    
    import { useAgent, UseAgentUpdate } from "@copilotkit/react-core/v2"; 
    
    const YourMainContent = () => {
      const { agent } = useAgent({
        agentId: "streamingAgent",
        updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],
      });
    
      const document = (agent.state as { document?: string })?.document ?? "";
    
      return (
        <div>
          <h1>Document {agent.isRunning && <span>· LIVE</span>}</h1>
    <pre>{document || "Ask the agent to write something…"}</pre>
        </div>
      );
    };

### Give it a try!#

Ask the agent to write a poem, draft an email, or explain a topic. The document panel fills in token-by-token as the agent streams, and the run-end working-memory snapshot reconciles any drift.

### On this page

What is this?When should I use this?How it worksImplementation
