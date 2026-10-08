---
url: https://docs.copilotkit.ai/mastra/shared-state/in-app-agent-write/
title: Writing agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:17:09.824277+00:00
---

# Writing agent state

> Source: https://docs.copilotkit.ai/mastra/shared-state/in-app-agent-write/

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

Writing agent state

InteractivityShared state

# Writing agent state

Write to agent's state from your application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates writing to shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/mastra/feature/shared_state).

## What is this?#

You can easily write to your agent's state from your native application, allowing you to update the agent's working memory from your UI.

Important

This guide assumes you are embedding your Mastra agent inside of Copilot Runtime, like so.
    
    
    const runtime = new CopilotRuntime({
      agents: MastraAgent.getLocalAgents({ mastra, resourceId: "user-1" }),
    });

This feature will **not work** if you are using a **remote Mastra agent**.

## When should I use this?#

You can use this when you want to provide user input or control to your agent's working memory. As your application state changes, you can update the agent state to reflect these changes.

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

With your agent connected and running all that is left is to call the `useAgent` hook, pass the agent's name, and use `agent.setState` to update the agent state.

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
    
      const toggleLanguage = () => {
        agent.setState({ ...(agent.state ?? {}), language: state.language === "english" ? "spanish" : "english" }); 
      };
    
      return (
        // style excluded for brevity
        <div>
          <h1>Your main content</h1>
          <p>Language: {agent.state?.language}</p>
          <button onClick={toggleLanguage}>Toggle Language</button>
        </div>
      );
    }

The `agent.setState` function in `useAgent` will update the working memory and trigger a rerender when the state changes.

### Give it a try!#

You can now use the `setState` function to update the agent state and `state` to read it. Try toggling the language button and talking to your agent. You'll see the language change to match the agent's state.

Important

Shared-state in Mastra is prompt-driven. This means that your Agent's awareness of the shared state will be augmented by the instructions you provide to your agent.

### On this page

What is this?When should I use this?Implementation
