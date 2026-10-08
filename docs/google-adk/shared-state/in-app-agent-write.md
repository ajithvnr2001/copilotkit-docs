---
url: https://docs.copilotkit.ai/google-adk/shared-state/in-app-agent-write/
title: Writing agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:35.422804+00:00
---

# Writing agent state

> Source: https://docs.copilotkit.ai/google-adk/shared-state/in-app-agent-write/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Google ADK](https://docs.copilotkit.ai/google-adk)[Shared State](https://docs.copilotkit.ai/google-adk/shared-state)

# Writing agent state

Write to agent's state from your application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates writing to shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/adk-middleware/feature/shared_state).

## What is this?#

This guide shows you how to write to your agent's state from your application.

## When should I use this?#

You can use this when you want to provide the user with feedback about what your agent is doing, specifically when your agent is calling tools. CopilotKit allows you to fully customize how these tools are rendered in the chat.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Define the Agent State#

Create your ADK agent with a stateful structure. Here's a complete example that tracks language:

agent.py
    
    
    from typing import Dict
    from fastapi import FastAPI
    from pydantic import BaseModel
    from ag_ui_adk import ADKAgent, add_adk_fastapi_endpoint
    from google.adk.agents import LlmAgent
    from google.adk.tools import ToolContext
    
    
    class AgentState(BaseModel):
        """State for the agent."""
        language: str = "english"
    
    
    def set_language(tool_context: ToolContext, new_language: str) -> Dict[str, str]:
        """Sets the language preference for the user.
    
        Args:
            tool_context (ToolContext): The tool context for accessing state.
            new_language (str): The language to save in state.
    
        Returns:
            Dict[str, str]: A dictionary indicating success status and message.
        """
        tool_context.state["language"] = new_language
        return {"status": "success", "message": f"Language set to {new_language}"}
    
    
    agent = LlmAgent(
        name="my_agent",
        model="gemini-2.5-flash",
        instruction="""
        You are a helpful assistant. Help users by answering their questions.
        Please use the language specified in state when responding to the user.
        You can set the language in state by using the set_language tool.
        """,
        tools=[set_language],
    )
    
    adk_agent = ADKAgent(
        adk_agent=agent,
        app_name="demo_app",
        user_id="demo_user",
        session_timeout_seconds=3600,
        use_in_memory_services=True,
    )
    
    app = FastAPI()
    add_adk_fastapi_endpoint(app, adk_agent, path="/")
    
    if __name__ == "__main__":
        uvicorn.run(app, host="0.0.0.0", port=8000)

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
        agentId: "my_agent",
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

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

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

### On this page

What is this?When should I use this?ImplementationAdvanced UsageRe-run the agent with a hint about what's changed
