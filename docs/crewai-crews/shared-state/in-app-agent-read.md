---
url: https://docs.copilotkit.ai/crewai-crews/shared-state/in-app-agent-read/
title: Reading agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:58:04.824264+00:00
---

# Reading agent state

> Source: https://docs.copilotkit.ai/crewai-crews/shared-state/in-app-agent-read/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/crewai-crews/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/crewai-crews/shared-state/in-app-agent-write)[Predictive state updates](https://docs.copilotkit.ai/crewai-crews/shared-state/predictive-state-updates)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Reading agent state

InteractivityShared state

# Reading agent state

Read the realtime agent state in your native application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

![read agent state](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/read-agent-state.png)

Pictured above is the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter-crewai-flows) with the implementation section applied!

## What is this?#

You can easily use the realtime agent state not only in the chat UI, but also in the native application UX.

## When should I use this?#

You can use this when you want to provide the user with feedback about your agent's state. As your agent's state updates, you can reflect these updates natively in your application.

## Implementation#

### Run and Connect Your Agent to CopilotKit#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/crewai-flows/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter-crewai-flows) as a starting point as this guide uses it as a starting point.

### Define the Agent State#

CrewAI Flows are stateful. As you transition through the flow, that state is updated and available to the next function. For this example, let's assume that our agent state looks something like this.

Python

agent.py
    
    
    from copilotkit.crewai import CopilotKitState
    from typing import Literal
    
    class AgentState(CopilotKitState):
        language: Literal["english", "spanish"] = "english"

### Use the `useAgent` Hook#

With your agent connected and running all that is left is to call the `useAgent` hook, pass the agent's name, and initialize missing UI-owned state after the connected agent is ready.

ui/app/page.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    
    // Define the agent state type, should match the actual state of your agent
    type AgentState = {
    language: "english" | "spanish";
    }
    
    function YourMainContent() {
      const { agent, isReady } = useAgent({
        agentId: "sample_agent",
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

The `agent.state` in `useAgent` is reactive and will automatically update when the agent's state changes.

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
        agentId: "sample_agent",
      });
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      if (!state.language) return null;
      return <div>Language: {state.language}</div>;
    }

The `agent.state` in `useAgent` is reactive and will automatically update when the agent's state changes.

## Intermediately Stream and Render Agent State#

By default, the CrewAI Flow agent state will only update _between_ CrewAI Flow node transitions -- which means state updates will be discontinuous and delayed.

You likely want to render the agent state as it updates **continuously.**

See **[emit intermediate state](https://docs.copilotkit.ai/crewai-flows/shared-state/predictive-state-updates).**

### On this page

What is this?When should I use this?ImplementationRendering agent state in your appIntermediately Stream and Render Agent State
