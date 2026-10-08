---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/shared-state/in-app-agent-read/
title: Reading agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:21:04.379381+00:00
---

# Reading agent state

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/shared-state/in-app-agent-read/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Harness (.NET)](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Shared State](https://docs.copilotkit.ai/ms-agent-harness-dotnet/shared-state)

# Reading agent state

Read the realtime agent state in your native application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates reading from shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/microsoft-agent-framework-dotnet/feature/shared_state).

## What is this?#

You can easily use the realtime agent state not only in the chat UI, but also in the native application UX.

## When should I use this?#

You can use this when you want to provide the user with feedback about your agent's state. As your agent's state updates, you can reflect these updates natively in your application.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Define the Agent State#

Decide which parts of agent state you want to reflect in the UI and allow updating from the UI.

.NETPython

agent/Program.cs (excerpt)
    
    
    public class AgentStateSnapshot
    {
        public string Language { get; set; } = "english";
    }

main.py
    
    
    from __future__ import annotations
    import os
    import uvicorn
    from agent_framework import Agent, tool, SupportsChatGetResponse
    from agent_framework.openai import OpenAIChatClient
    from agent_framework.ag_ui import add_agent_framework_fastapi_endpoint
    from agent_framework.ag_ui import AgentFrameworkAgent
    from azure.identity import DefaultAzureCredential
    from dotenv import load_dotenv
    from fastapi import FastAPI
    from typing import Annotated
    from pydantic import BaseModel, Field
    
    load_dotenv()
    
    class SearchItem(BaseModel):
        query: str
        done: bool
        
    STATE_SCHEMA: dict[str, object] = {
        "language": {
            "type": "string",
            "enum": ["english", "spanish"],
            "description": "Preferred language.",
        }
    }
    PREDICT_STATE_CONFIG: dict[str, dict[str, str]] = {
        "language": {"tool": "update_language", "tool_argument": "language"}
    }
    
    @tool
    def update_language(
        language: Annotated[str, Field(description="Preferred language: 'english' or 'spanish'")],
    ) -> str:
        normalized = (language or "").strip().lower()
        if normalized not in ("english", "spanish"):
            return "Language unchanged. Use 'english' or 'spanish'."
        return f"Language updated to {normalized}."
    
    
    def _build_chat_client():
        if os.getenv("AZURE_OPENAI_ENDPOINT"):
            azure_api_key = os.getenv("AZURE_OPENAI_API_KEY")
            return OpenAIChatClient(
                model=os.getenv("AZURE_OPENAI_CHAT_DEPLOYMENT_NAME", "gpt-4o-mini"),
                api_key=azure_api_key,
                credential=None if azure_api_key else DefaultAzureCredential(),
                azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
            )
        if os.getenv("OPENAI_API_KEY"):
            return OpenAIChatClient(
                model=os.getenv("OPENAI_CHAT_MODEL_ID", "gpt-4o-mini"),
                api_key=os.getenv("OPENAI_API_KEY"),
            )
        raise RuntimeError(
            "Set AZURE_OPENAI_ENDPOINT (uses az login unless AZURE_OPENAI_API_KEY is set) or OPENAI_API_KEY."
        )
    
    
    
    def create_agent(chat_client: SupportsChatGetResponse) -> AgentFrameworkAgent:
        base_agent = Agent(
            name="sample_agent",
            instructions="You are a helpful assistant.",
            client=chat_client,
            tools=[update_language],   
        )
        return AgentFrameworkAgent(
            agent=base_agent,
            name="CopilotKitMicrosoftAgentFrameworkAgent",
            description="Assistant that tracks a simple language state.",
            state_schema=STATE_SCHEMA,               
            predict_state_config=PREDICT_STATE_CONFIG, 
            require_confirmation=False,
        )
        
    
    chat_client = _build_chat_client()
    
    agent = create_agent(chat_client)
    
    app = FastAPI(title="Microsoft Agent Framework - Quickstart")
    add_agent_framework_fastapi_endpoint(app=app, agent=agent, path="/")
    
    if __name__ == "__main__":
        uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

ui/app/page.tsx
    
    
    type AgentState = {
    language: "english" | "spanish";
    }

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

![read agent state](https://cdn.copilotkit.ai/docs/copilotkit/images/microsoft-agent-framework/read-agent-state.png)

Pictured above is the [agent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/agents-starter) with the implementation section applied!

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

## Advanced: Emitting Intermediate State#

By default, agent state updates arrive at natural checkpoints during agent execution. For more granular, real-time updates during long-running operations, you can emit state snapshots from within your agent logic. Consult the [Microsoft Agent Framework documentation](https://learn.microsoft.com/en-us/agent-framework/user-guide/overview) for patterns on streaming custom state events during execution.

### On this page

What is this?When should I use this?ImplementationRendering agent state in your appAdvanced: Emitting Intermediate State
