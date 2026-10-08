---
url: https://docs.copilotkit.ai/deepagents/shared-state/in-app-agent-read/
title: Reading agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:00:58.313053+00:00
---

# Reading agent state

> Source: https://docs.copilotkit.ai/deepagents/shared-state/in-app-agent-read/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/deepagents/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/deepagents/shared-state/in-app-agent-write)[State streaming](https://docs.copilotkit.ai/deepagents/shared-state/predictive-state-updates)[Input/Output Schemas](https://docs.copilotkit.ai/deepagents/shared-state/state-inputs-outputs)[Workflow Execution](https://docs.copilotkit.ai/deepagents/shared-state/workflow-execution)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

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

This example demonstrates reading from shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/langgraph/feature/shared_state).

## What is this?#

You can easily use the realtime agent state not only in the chat UI, but also in the native application UX.

## When should I use this?#

You can use this when you want to provide the user with feedback about your agent's state. As your agent's state updates, you can reflect these updates natively in your application.

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
    
    # The agent reads `state["language"]` from tools or middleware hooks
    # as it runs — no custom node required.

agent.ts
    
    
    import { createMiddleware } from "langchain";
    import { copilotkitMiddleware, zodState } from "@copilotkit/sdk-js/langgraph"; 
    import { z } from "zod";
    
    // Define the state as a middleware. The default flows through automatically.
    export const languageStateMiddleware = createMiddleware({
        name: "AgentState",
        stateSchema: z.object({
            language: zodState(z.enum(["english", "spanish"]).default("english")),
        }),
    });
    
    // Compose with copilotkitMiddleware when constructing the agent:
    // createDeepAgent({ middleware: [languageStateMiddleware, copilotkitMiddleware], ... })

### Use the `useAgent` Hook#

With your agent connected and running all that is left is to call the `useAgent` hook, pass the agent's ID, and read the state.

ui/app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "sample_agent",
      });
    
      const language = (agent.state.language as string) ?? "english";
    
      // ...
    
      return (
        // style excluded for brevity
        <div>
          <h1>Your main content</h1>
          <p>Language: {language}</p>
        </div>
      );
    }

The `agent.state` is reactive and will automatically update when the agent's state changes.

### Give it a try!#

As the agent state updates, your `state` variable will automatically update with it! In this case, you'll see the language set to "english" as that's the initial state we set.

![read agent state](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/read-agent-state.png)

Pictured above is the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) with the implementation section applied!

## Rendering agent state in the chat#

You can also render the agent's state in the chat UI using `useRenderTool` or by accessing `agent.state` from `useAgent`. The state is reactive and updates automatically.

ui/app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "sample_agent",
      });
    
      const language = (agent.state.language as string) ?? "english";
    
      return (
        <div>
          <p>Language: {language}</p>
        </div>
      );
    }

## Intermediately Stream and Render Agent State#

By default, the Deep Agents agent state will only update _between_ LangGraph node transitions -- which means state updates will be discontinuous and delayed.

You likely want to render the agent state as it updates **continuously.**

See **[emit intermediate state](https://docs.copilotkit.ai/deepagents/shared-state/predictive-state-updates).**

### On this page

What is this?When should I use this?ImplementationRendering agent state in the chatIntermediately Stream and Render Agent State
