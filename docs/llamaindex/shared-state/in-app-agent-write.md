---
url: https://docs.copilotkit.ai/llamaindex/shared-state/in-app-agent-write/
title: Writing agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:28.465237+00:00
---

# Writing agent state

> Source: https://docs.copilotkit.ai/llamaindex/shared-state/in-app-agent-write/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Reading agent state](https://docs.copilotkit.ai/llamaindex/shared-state/in-app-agent-read)[Writing agent state](https://docs.copilotkit.ai/llamaindex/shared-state/in-app-agent-write)[Workflow Execution](https://docs.copilotkit.ai/llamaindex/shared-state/workflow-execution)[Predictive state updates](https://docs.copilotkit.ai/llamaindex/shared-state/predictive-state-updates)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

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

This example demonstrates writing to shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/llama-index/feature/shared_state).

## What is this?#

You can easily write to your agent's state from your native application, allowing you to update the agent's working memory from your UI.

## When should I use this?#

You can use this when you want to provide user input or control to your agent's working memory. As your application state changes, you can update the agent state to reflect these changes.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Define the Agent State#

Create your LlamaIndex agent with a stateful structure using `initial_state`. Here's a complete example that tracks language:

agent.py
    
    
    from fastapi import FastAPI
    from llama_index.llms.openai import OpenAI
    from llama_index.protocols.ag_ui.router import get_ag_ui_workflow_router
    
    # Initialize the LLM
    llm = OpenAI(model="gpt-5.4")
    
    # Create the AG-UI workflow router
    agentic_chat_router = get_ag_ui_workflow_router(
        llm=llm,
        system_prompt="""
        You are a helpful assistant for tracking the language.
    
        IMPORTANT:
        - ALWAYS use the lower case for the language
        - ALWAYS respond in the current language from the state
        """,
        initial_state={
            "language": "english"
        },
    )
    
    # Create FastAPI app
    app = FastAPI(
        title="LlamaIndex Agent",
        description="A LlamaIndex agent integrated with CopilotKit",
        version="1.0.0"
    )
    
    # Include the router
    app.include_router(agentic_chat_router)
    
    # Health check endpoint
    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "agent": "llamaindex"}
    
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="localhost", port=8000)

### Use the `useAgent` Hook#

With your agent connected and running all that is left is to call the `useAgent` hook, pass the agent's name, and use `agent.setState` to update the agent state.

ui/app/page.tsx
    
    
    "use client";
    
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

The `agent.setState` function in `useAgent` will update the state and trigger a rerender when the state changes.

### Give it a try!#

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

### On this page

What is this?When should I use this?ImplementationAdvanced UsageRe-run the agent with a hint about what's changed
