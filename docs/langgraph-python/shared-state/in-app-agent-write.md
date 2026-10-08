---
url: https://docs.copilotkit.ai/langgraph-python/shared-state/in-app-agent-write/
title: Writing agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:08:51.140664+00:00
---

# Writing agent state

> Source: https://docs.copilotkit.ai/langgraph-python/shared-state/in-app-agent-write/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-python)[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-python/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)[Shared State](https://docs.copilotkit.ai/langgraph-python/shared-state)

# Writing agent state

Write to agent's state from your application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates writing to shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/langgraph/feature/shared_state).

## What is this?#

This guide shows you how to write to your agent's state from your application.

## When should I use this?#

You can use this when you want to provide the user with feedback about what your agent is doing, specifically when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Define the Agent State#

LangGraph is stateful. As you transition between nodes, that state is updated and passed to the next node. For this example, let's assume that our agent state looks something like this.

PythonTypeScript

agent.py
    
    
    from copilotkit import CopilotKitState
    from typing import Literal
    
    class AgentState(CopilotKitState):
        language: Literal["english", "spanish"] = "english"

agent-js/src/agent.ts
    
    
    import { StateSchema } from "@langchain/langgraph";
    import { CopilotKitStateSchema } from "@copilotkit/sdk-js/langgraph";
    import { z } from "zod";
    
    export const AgentStateSchema = new StateSchema({
        language: z.enum(["english", "spanish"]).default("english"),
        ...CopilotKitStateSchema.fields,
    });
    export type AgentState = typeof AgentStateSchema.State;

### Use the `useAgent` hook to read and write state#

`useAgent` gives you access to the agent, including its state. You can update state by calling `agent.setState`.

ui/app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    // Example usage in a pseudo React component
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "sample_agent",
      });
    
      const language = (agent.state.language as string) ?? "english";
    
      // ...
    
      const toggleLanguage = () => {
        agent.setState({ language: language === "english" ? "spanish" : "english" }); 
      };
    
      // ...
    
      return (
        // style excluded for brevity
        <div>
          <h1>Your main content</h1>
          <p>Language: {language}</p>
          <button onClick={toggleLanguage}>Toggle Language</button>
        </div>
      );
    }

### Give it a try!#

You can now use the `setState` function to update the agent state and `state` to read it. Try toggling the language button and talking to your agent. You'll see the language change to match the agent's state.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it!

## Advanced Usage#

### Re-run the agent with updated state#

The new agent state will be used next time the agent runs. If you want to re-run it manually, call `copilotkit.runAgent({ agent })` after updating state. Running through `copilotkit` sends your frontend tools and context with the run and executes any frontend tool calls.

ui/app/page.tsx
    
    
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2"; 
    
    // ...
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "sample_agent",
      });
      const { copilotkit } = useCopilotKit(); 
    
      const language = (agent.state.language as string) ?? "english";
    
      // setup to be called when some event in the app occurs
      const toggleLanguage = () => {
        const newLanguage = language === "english" ? "spanish" : "english";
        agent.setState({ language: newLanguage });
    
        // re-run the agent with updated state
        copilotkit.runAgent({ agent });
      };
    
      return (
        // ...
      );
    }

### Intermediately Stream and Render Agent State#

By default, the LangGraph agent state will only update _between_ LangGraph node transitions -- which means state updates will be discontinuous and delayed.

You likely want to render the agent state as it updates **continuously.**

See **[predictive state updates](https://docs.copilotkit.ai/langgraph/shared-state/predictive-state-updates).**

### On this page

What is this?When should I use this?ImplementationAdvanced UsageRe-run the agent with updated stateIntermediately Stream and Render Agent State
