---
url: https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/in-app-agent-write/
title: Writing agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:19:09.045826+00:00
---

# Writing agent state

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/in-app-agent-write/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state/in-app-agent-write)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-dotnet/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-dotnet/community-frameworks)

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

This example demonstrates reading from shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/microsoft-agent-framework-dotnet/feature/shared_state).

## What is this?#

This guide shows you how to write to your agent's state from your application.

## When should I use this?#

You can use this when you need to update agent state from your application — for example, changing user preferences, toggling settings, or providing user input that affects agent behavior.

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

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it!

## Advanced Usage#

### Re-run the agent with a hint about what's changed#

The new agent state will be used next time the agent runs. If you want to re-run it manually, use `copilotkit.runAgent()`.

The agent will be re-run with the latest updated state. You can also add a hint message before re-running.

ui/app/page.tsx
    
    
    import { useAgent, useCopilotKit } from "@copilotkit/react-core/v2";
    
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

### Notes on state updates#

Depending on your agent implementation, you may choose to surface progress via tool responses or messages rather than frequent state snapshots. See [Generative UI](https://docs.copilotkit.ai/microsoft-agent-framework/generative-ui/tool-rendering) for recommended patterns.

### On this page

What is this?When should I use this?ImplementationAdvanced UsageRe-run the agent with a hint about what's changedNotes on state updates
