---
url: https://docs.copilotkit.ai/pydantic-ai/shared-state/in-app-agent-read/
title: Reading agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:31.306273+00:00
---

# Reading agent state

> Source: https://docs.copilotkit.ai/pydantic-ai/shared-state/in-app-agent-read/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/pydantic-ai/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/pydantic-ai/shared-state/in-app-agent-write)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/pydantic-ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/pydantic-ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/pydantic-ai/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/pydantic-ai/community-frameworks)

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

This example demonstrates reading from shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/pydantic-ai/feature/shared_state).

## What is this?#

You can easily use the realtime agent state not only in the chat UI, but also in the native application UX.

## When should I use this?#

You can use this when you want to provide the user with feedback about your agent's state. As your agent's state updates, you can reflect these updates natively in your application.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Define the Agent State#

Create your Pydantic AI agent with a stateful structure. Here's a complete example that tracks language:

agent.py
    
    
    from textwrap import dedent
    
    from pydantic import BaseModel
    from pydantic_ai import Agent, RunContext
    from pydantic_ai.ui import StateDeps
    from pydantic_ai.ui.ag_ui import AGUIAdapter
    from starlette.applications import Starlette
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.routing import Route
    
    
    class AgentState(BaseModel):
        """State for the agent."""
        language: str = "english"
    
    
    agent = Agent("openai:gpt-5.4-mini", deps_type=StateDeps[AgentState])
    
    
    @agent.instructions()
    async def language_instructions(ctx: RunContext[StateDeps[AgentState]]) -> str:
        """Instructions for the language tracking agent.
    
        Args:
            ctx: The run context containing language state information.
    
        Returns:
            Instructions string for the language tracking agent.
        """
        return dedent(
            f"""
            You are a helpful assistant for tracking the language.
    
            IMPORTANT:
            - ALWAYS use the lower case for the language
            - ALWAYS response in the current language: {ctx.deps.state.language}
            """
        )
    
    
    async def run_agent(request: Request) -> Response:
        # Build the deps fresh on every request: `dispatch_request` writes the state
        # the client sent into `deps.state`, so a shared instance leaks state between
        # concurrent requests and users.
        return await AGUIAdapter.dispatch_request(
            request, agent=agent, deps=StateDeps(AgentState())
        )
    
    
    app = Starlette(routes=[Route("/", run_agent, methods=["POST"])])
    
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)

### Use the `useAgent` Hook#

With your agent connected and running, call the `useAgent` hook, wait for the real agent, and initialize any missing UI-owned state with `agent.setState`.

ui/app/page.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    // Define the agent state type, should match the actual state of your agent
    type AgentState = {
    language: "english" | "spanish";
    }
    
    function YourMainContent() {
      const { agent, isReady } = useAgent({
        agentId: "my_agent",
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
          <p>Language: {state.language}</p>
        </div>
      );
    }

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

The `agent.state` in `useAgent` is reactive and will automatically update when the agent's state changes.

### Give it a try!#

As the agent state updates, your `state` variable will automatically update with it! In this case, you'll see the language set to "english" after the connected agent is ready.

## Rendering agent state in your app#

You can render the agent state in any React component under `<CopilotKit>`. Read `agent.state` and return ordinary JSX.

ui/app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    // Define the agent state type, should match the actual state of your agent
    type AgentState = {
      language: "english" | "spanish";
    };
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "my_agent",
      });
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      if (!state.language) return null;
      return <div>Language: {state.language}</div>;
    }

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

The `agent.state` in `useAgent` is reactive and will automatically update when the agent's state changes.

## Intermediately Stream and Render Agent State#

By default, the Pydantic AI Agent state will only update _between_ Pydantic AI Agent node transitions -- which means state updates will be discontinuous and delayed.

### On this page

What is this?When should I use this?ImplementationRendering agent state in your appIntermediately Stream and Render Agent State
