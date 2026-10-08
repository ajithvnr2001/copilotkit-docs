---
url: https://docs.copilotkit.ai/ag2/shared-state/write/
title: Writing agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:53.925070+00:00
---

# Writing agent state

> Source: https://docs.copilotkit.ai/ag2/shared-state/write/

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

Writing agent state

InteractivityShared state

# Writing agent state

Write to agent's state from your application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it.

## What is this?#

This guide shows you how to write to your agent's state from your application.

CopilotKit consumes AG-UI protocol events streamed by AG2 over `/chat`. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

## When should I use this?#

You can use this when you want to keep your interface and backend agent state synchronized. CopilotKit lets you update state from the UI, while AG2 consumes that state in subsequent turns.

## Implementation#

### Run and connect your agent#

Start your AG2 backend and connect your CopilotKit frontend to the AG-UI `/chat` endpoint.

### Define the Agent State#

In AG2, shared state lives in the agent's **conversation variables**. `AGUIStream` synchronizes them in both directions: state written from the UI (`agent.setState`) arrives on `RunAgentInput.state` and is merged into the variables for the run, and variable changes made by tools are streamed back as `STATE_SNAPSHOT` events automatically.

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

Don't set a default for a UI-written key via `Agent(variables=...)` — agent variables take precedence over the incoming `RunAgentInput.state` on every run, so they would overwrite whatever the UI wrote with `agent.setState`. Provide defaults in the UI (or via `context.variables.setdefault` inside a tool) instead.

### Call `setState` function from the `useAgent` hook#

`useAgent` returns an `agent` object with a `setState` function that you can use to update the agent state. Calling this will update the agent state and trigger a rerender of anything that depends on the agent state.

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
        agentId: "my_agent", // MUST match the agent name in CopilotRuntime
      });
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      useEffect(() => {
    if (!isReady || state.language !== undefined) return;
        agent.setState({ ...(agent.state ?? {}), language: "english" });
      }, [agent, isReady, state.language]);
    
      // default to english until the UI or the agent sets it
      const language = state.language ?? "english";
    
      const toggleLanguage = () => {
        agent.setState({ ...(agent.state ?? {}), language: state.language === "english" ? "spanish" : "english" }); 
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

Important

The `agentId` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

### Give it a try#

You can now use `agent.setState` to update the agent state and `agent.state` to read it. Try toggling the language button and talking to your agent. You'll see the language change to match the agent's state.

## Advanced Usage#

### Re-run the agent with a hint about what's changed#

The new agent state will be used next time the agent runs. If you want to re-run it manually, use `copilotkit.runAgent()`.

The agent will be re-run with the latest updated state. You can also add a hint message before re-running.

ui/app/page.tsx
    
    
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2";
    
    // ...
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "my_agent",
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

By default, `AGUIStream` emits a `STATE_SNAPSHOT` at the start of the run (only when the merged variables differ from the state the client sent) and at the end of the run (if `context.variables` changed since the last snapshot). A snapshot replaces the client's state wholesale, so each one carries the client's keys and the server's variables together. For smoother long-running workflows, emit intermediate snapshots from an async tool with `context.send(AGUIEvent(StateSnapshotEvent(snapshot=...)))` — see [Reading agent state](https://docs.copilotkit.ai/ag2/shared-state/read) for a complete example.

### On this page

What is this?When should I use this?ImplementationAdvanced UsageRe-run the agent with a hint about what's changedIntermediately Stream and Render Agent State
