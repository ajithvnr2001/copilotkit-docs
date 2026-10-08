---
url: https://docs.copilotkit.ai/ag2/shared-state/read/
title: Reading agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:49.070054+00:00
---

# Reading agent state

> Source: https://docs.copilotkit.ai/ag2/shared-state/read/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/ag2/shared-state/read)[Writing agent state](https://docs.copilotkit.ai/ag2/shared-state/write)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Reading agent state

InteractivityShared state

# Reading agent state

Read the realtime agent state in your native application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it.

## What is this?#

You can easily use the realtime agent state not only in the chat UI, but also in the native application UX.

CopilotKit consumes AG-UI protocol events streamed by AG2 over `/chat`. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

## When should I use this?#

You can use this when you want to provide the user with feedback about your agent's state. As your agent's state updates, you can reflect these updates natively in your application.

## Implementation#

### Run and connect your agent#

Start your AG2 backend and connect your CopilotKit frontend to the AG-UI `/chat` endpoint.

### Define the Agent State#

In AG2, shared state lives in the agent's **conversation variables**. `AGUIStream` handles the synchronization for you: incoming state from the UI is merged into the variables for the run, and the variables are streamed back as `STATE_SNAPSHOT` events — at the start of the run (only when the agent or `dispatch()` defines initial variables) and, if a tool changed `context.variables`, at the end of the run. No manual event construction needed.

agent.py
    
    
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    from fastapi.responses import StreamingResponse
    from pydantic import Field
    
    from ag2 import Agent, Context, tool
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    @tool
    def set_language(
        language: Annotated[str, Field(description="language such as english or spanish")],
        context: Context,
    ) -> str:
        """Update the language in shared state."""
        context.variables["language"] = language.lower()
        return f"Language set to {language}"
    
    agent = Agent(
        name="assistant",
        prompt=(
            "You are a helpful assistant for tracking language. "
            "Always respond in the current language."
        ),
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[set_language],
    )
    
    stream = AGUIStream(agent)
    app = FastAPI()
    
    @app.post("/chat")
    async def run_agent(
        message: RunAgentInput,
    accept: str | None = Header(None),
    ) -> StreamingResponse:
        return StreamingResponse(
            stream.dispatch(message, accept=accept),
            media_type=accept or "text/event-stream",
        )

Don't seed the initial value with `Agent(variables={"language": "english"})` — agent variables take precedence over the incoming `RunAgentInput.state` on every run, so the agent would reset the language back to `english` on the turn after it set `spanish`. Provide the default in the UI (as the `?? "english"` fallback below does) or with `context.variables.setdefault` inside a tool.

### Use the `useAgent` Hook#

With your agent connected and running all that is left is to call the [useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent) hook, pass the agent's ID, and initialize missing UI-owned state after the connected agent is ready.

ui/app/page.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    // Define the agent state type, should match the actual state of your agent
    type AgentState = {
    language: "english" | "spanish";
    }
    
    function YourMainContent() {
      const { agent, isReady } = useAgent({
        agentId: "my_agent", // MUST match the agent name in CopilotRuntime
      });
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      useEffect(() => {
    if (!isReady || state.language !== undefined) return;
        agent.setState({ ...(agent.state ?? {}), language: "english" });
      }, [agent, isReady, state.language]);
    
      const language = state.language ?? "english";
    
      // ...
    
      return (
        // style excluded for brevity
        <div>
          <h1>Your main content</h1>
          <p>Language: {language}</p>
        </div>
      );
    }

Important

The `agentId` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

The `agent.state` in `useAgent` is reactive and will automatically update when the agent's state changes.

### Give it a try#

As the agent state updates, your `state` variable will automatically update with it. In this case, you'll see the language set to "english" after the connected agent is ready.

## Rendering agent state in your app#

You can render the agent state in any React component under `<CopilotKit>`. Read `agent.state` and return ordinary JSX.

ui/app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
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

## Intermediately Stream and Render Agent State#

By default, `AGUIStream` emits a `STATE_SNAPSHOT` at the start of the run (only when the merged variables differ from the state the client sent) and at the end of the run (if `context.variables` changed since the last snapshot). A snapshot replaces the client's state wholesale, so each one carries the client's keys and the server's variables together. For smoother long-running workflows, emit intermediate snapshots from an async tool with `context.send`:

agent.py
    
    
    from ag_ui.core import StateSnapshotEvent
    
    from ag2 import Context, tool
    from ag2.ag_ui import AGUIEvent
    
    @tool
    async def long_running_task(context: Context) -> str:
        """A long task that streams state updates as it progresses."""
        for step in range(3):
            context.variables["progress"] = step
            await context.send(
                AGUIEvent(StateSnapshotEvent(snapshot=dict(context.variables)))
            )
        return "Done"

### On this page

What is this?When should I use this?ImplementationRendering agent state in your appIntermediately Stream and Render Agent State
