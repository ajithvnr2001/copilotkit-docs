---
url: https://docs.copilotkit.ai/crewai-flows/shared-state/in-app-agent-write/
title: Writing agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:36:01.826411+00:00
---

# Writing agent state

> Source: https://docs.copilotkit.ai/crewai-flows/shared-state/in-app-agent-write/

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

Writing agent state

InteractivityShared state

# Writing agent state

Write to agent's state from your application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it!

## What is this?#

This guide shows you how to write to your agent's state from your application.

## When should I use this?#

You can use this when you want to provide the user with feedback about what your agent is doing, specifically when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## Implementation#

### Run and Connect Your Agent to CopilotKit#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/crewai-flows/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter-crewai-flows) as a starting point as this guide uses it as a starting point.

### Define the Agent State#

CrewAI Flows are stateful. As you transition through the flow, that state is updated and available to the next function. For this example, let's assume that our agent state looks something like this.

PythonTypeScript

agent.py
    
    
    from copilotkit.crewai import CopilotKitState
    from typing import Literal
    
    class AgentState(CopilotKitState):
        language: Literal["english", "spanish"] = "english"

### Call `agent.setState` from the `useAgent` hook#

`useAgent` returns an `agent` object with a `setState` method that you can use to update the agent state. Calling this will update the agent state and trigger a rerender of anything that depends on the agent state.

ui/app/page.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    
    // Define the agent state type, should match the actual state of your agent
    type AgentState = {
    language: "english" | "spanish";
    }
    
    // Example usage in a pseudo React component
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
    
      const toggleLanguage = () => {
        agent.setState({ ...(agent.state ?? {}), language: state.language === "english" ? "spanish" : "english" }); 
      };
    
      // ...
    
      return (
        // style excluded for brevity
        <div>
          <h1>Your main content</h1>
          <p>Language: {agent.state?.language}</p>
          <button onClick={toggleLanguage}>Toggle Language</button>
        </div>
      );
    }

### Give it a try!#

You can now use `agent.setState` to update the agent state and `agent.state` to read it. Try toggling the language button and talking to your agent. You'll see the language change to match the agent's state.

## Advanced Usage#

### Re-run the agent with a hint about what's changed#

The new agent state will be used next time the agent runs. If you want to re-run it manually, use `copilotkit.runAgent()`.

The agent will be re-run with the latest updated state. You can also add a hint message before re-running.

ui/app/page.tsx
    
    
    // ...
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "sample_agent",
      });
      const { copilotkit } = useCopilotKit(); 
    
      // setup to be called when some event in the app occurs
      const toggleLanguage = async () => {
        const newLanguage = agent.state?.language === "english" ? "spanish" : "english";
        agent.setState({ language: newLanguage });
    
        // add a hint message and re-run the agent
        agent.addMessage({
          id: crypto.randomUUID(),
          role: "user",
          content: `the language has been updated to ${newLanguage}`,
        });
        await copilotkit.runAgent({ agent });
      };
    
      return (
        // ...
      );
    }

### Intermediately Stream and Render Agent State#

By default, the CrewAI Flow agent state will only update _between_ CrewAI Flow node transitions -- which means state updates will be discontinuous and delayed.

You likely want to render the agent state as it updates **continuously.**

See **[predictive state updates](https://docs.copilotkit.ai/crewai-flows/shared-state/predictive-state-updates).**

### On this page

What is this?When should I use this?ImplementationAdvanced UsageRe-run the agent with a hint about what's changedIntermediately Stream and Render Agent State
