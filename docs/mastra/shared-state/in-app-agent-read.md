---
url: https://docs.copilotkit.ai/mastra/shared-state/in-app-agent-read/
title: Reading agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:17:10.707135+00:00
---

# Reading agent state

> Source: https://docs.copilotkit.ai/mastra/shared-state/in-app-agent-read/

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

Reading agent state

InteractivityShared state

# Reading agent state

Read the realtime agent state in your native application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates reading from shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/mastra/feature/shared_state).

## What is this?#

You can easily use the realtime agent state not only in the chat UI, but also in the native application UX.

Important

This guide assumes you are embedding your Mastra agent inside of Copilot Runtime, like so.
    
    
    const runtime = new CopilotRuntime({
      agents: MastraAgent.getLocalAgents({ mastra, resourceId: "user-1" }),
    });

This feature will **not work** if you are using a **remote Mastra agent**.

## When should I use this?#

You can use this when you want to provide the user with feedback about what your working memory. As your agent's state updates, you can reflect these updates natively in your application.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Define the Agent State#

Mastra has advanced [working memory concepts](https://mastra.ai/en/docs/memory/working-memory) to provide statefulness to your agents. CopilotKit leverages Mastra's working memory concept to allow you to implement shared state between your agent and your application.

Providing working memory to your agent is as simple as providing a Zod schema to your agent.

mastra/agents/language-agent.ts
    
    
    import { openai } from "@ai-sdk/openai";
    import { Agent } from "@mastra/core/agent";
    import { LibSQLStore } from "@mastra/libsql";
    import { z } from "zod";
    import { Memory } from "@mastra/memory";
    
    // 1. Define the agent state schema
    export const AgentStateSchema = z.object({
      language: z.enum(["english", "spanish"]),
    });
    
    // 2. Infer the agent state type from the schema
    export const AgentState = z.infer<typeof AgentStateSchema>;
    
    // 3. Create the agent
    export const languageAgent = new Agent({
      id: "language-agent",
      name: "Language Agent",
      model: openai("gpt-5.4"),
      instructions: "Always communicate in the preferred language of the user as defined in your working memory. Do not communicate in any other language.",
      memory: new Memory({
        storage: new LibSQLStore({ id: "mastra-storage", url: ":memory:" }),
        options: {
          workingMemory: {
            enabled: true,
            schema: AgentStateSchema,
          },
        },
      }),
    });

### Use the `useAgent` Hook#

With your agent connected and running all that is left is to call the `useAgent` hook, pass the agent's name, and initialize missing UI-owned state after the connected agent is ready.

ui/app/page.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2"; 
    import { AgentState } from "@/mastra/agents/language-agent";
    
    function YourMainContent() {
      const { agent, isReady } = useAgent({
        agentId: "your-mastra-agent-name",
      });
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      useEffect(() => {
    if (!isReady || state.language !== undefined) return;
        agent.setState({ ...(agent.state ?? {}), language: "english" });
      }, [agent, isReady, state.language]);
    
      // ...
    
      return (
        // style excluded for brevity
        <div>
          <h1>Your main content</h1>
          <p>Language: {agent.state?.language}</p>
        </div>
      );
    }

The `agent.state` in `useAgent` is reactive and will automatically update when the working memory changes.

### Give it a try!#

As the agent state updates, your `state` variable will automatically update with it! In this case, you'll see the language set to "english" after the connected agent is ready.

## Rendering agent state in your app#

You can render the agent state in any React component under `<CopilotKit>`. Read `agent.state` and return ordinary JSX.

ui/app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
    type AgentState = {
      language: "english" | "spanish";
    };
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "your-mastra-agent-name",
      });
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      if (!state.language) return null;
      return <div>Language: {state.language}</div>;
    }

The `agent.state` in `useAgent` is reactive and will automatically update when the working memory changes.

### On this page

What is this?When should I use this?ImplementationRendering agent state in your app
