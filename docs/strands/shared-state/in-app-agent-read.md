---
url: https://docs.copilotkit.ai/strands/shared-state/in-app-agent-read/
title: Reading agent state
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:31:53.494076+00:00
---

# Reading agent state

> Source: https://docs.copilotkit.ai/strands/shared-state/in-app-agent-read/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands)[Quickstart](https://docs.copilotkit.ai/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](https://docs.copilotkit.ai/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands/learning)

[User Memories](https://docs.copilotkit.ai/strands/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[AWS Strands (Python)](https://docs.copilotkit.ai/strands)[Shared State](https://docs.copilotkit.ai/strands/shared-state)

# Reading agent state

Read the realtime agent state in your native application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates reading from shared state in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/aws-strands/feature/shared_state).

## What is this?#

You can easily use the realtime agent state not only in the chat UI, but also in the native application UX.

## When should I use this?#

You can use this when you want to provide the user with feedback about your agent's state. As your agent's state updates, you can reflect these updates natively in your application.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Setup your agent with state#

Define your agent's state schema. AWS Strands maintains state throughout execution.

PythonTypeScript

agent/main.py
    
    
    from ag_ui_strands import StrandsAgent, StrandsAgentConfig, create_strands_app
    from strands import Agent
    from strands.models.openai import OpenAIModel
    
    model = OpenAIModel(
        client_args={"api_key": os.getenv("OPENAI_API_KEY", "")},
        model_id="gpt-4o",
    )
    
    # Create the Strands agent
    strands_agent = Agent(
        model=model,
        system_prompt="Always communicate in the preferred language of the user as defined in your state. Do not communicate in any other language.",
    )
    
    # Inject state into the prompt
    def language_prompt(input_data, user_message: str) -> str:
        state_dict = getattr(input_data, "state", None)
        if isinstance(state_dict, dict) and "language" in state_dict:
            return f"Current language: {state_dict['language']}\n\nUser request: {user_message}"
        return user_message
    
    config = StrandsAgentConfig(state_context_builder=language_prompt)
    
    # Wrap with AG-UI integration
    agui_agent = StrandsAgent(
        agent=strands_agent,
        name="languageAgent",
        description="Always communicate in the preferred language of the user",
        config=config,
    )
    
    app = create_strands_app(agui_agent)

agent/main.ts
    
    
    import { Agent } from "@strands-agents/sdk";
    import { OpenAIModel } from "@strands-agents/sdk/models/openai";
    import { StrandsAgent, type StrandsAgentConfig } from "@ag-ui/aws-strands";
    import { createStrandsApp } from "@ag-ui/aws-strands/server";
    
    const model = new OpenAIModel({
      apiKey: process.env.OPENAI_API_KEY ?? "",
      modelId: "gpt-4o",
    });
    
    // Create the Strands agent
    const strandsAgent = new Agent({
      model,
      systemPrompt:
        "Always communicate in the preferred language of the user as defined in your state. Do not communicate in any other language.",
    });
    
    await strandsAgent.initialize();
    
    // Inject state into the prompt
    const config: StrandsAgentConfig = {
      stateContextBuilder: (inputData, userMessage) => {
        const state = (inputData.state ?? {}) as { language?: string };
        if (state.language) {
          return `Current language: ${state.language}\n\nUser request: ${userMessage}`;
        }
        return userMessage;
      },
    };
    
    // Wrap with AG-UI integration
    const aguiAgent = new StrandsAgent({
      agent: strandsAgent,
      name: "languageAgent",
      description: "Always communicate in the preferred language of the user",
      config,
    });
    
    const app = await createStrandsApp(aguiAgent);
    app.listen(8000);

### Use the `useAgent` Hook#

With your agent connected and running, call the `useAgent` hook, wait for the real agent, and initialize any missing UI-owned state with `agent.setState`.

ui/app/page.tsx
    
    
    import { useEffect } from "react";
    import { useAgent } from "@copilotkit/react-core/v2";
    
    // Define the agent state type to match your Strands agent
    type AgentState = {
    language: "english" | "spanish";
    };
    
    function YourMainContent() {
      const { agent, isReady } = useAgent({
        agentId: "strands_agent",
      });
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      useEffect(() => {
    if (!isReady || state.language !== undefined) return;
        agent.setState({ ...(agent.state ?? {}), language: "spanish" });
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

The `agent.state` in `useAgent` is reactive and will automatically update when the agent state changes.

### Give it a try!#

As the agent state updates, your `state` variable will automatically update with it! In this case, you'll see the language set to "spanish" after the connected agent is ready.

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
        agentId: "strands_agent",
      });
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      if (!state.language) return null;
      return <div>Language: {state.language}</div>;
    }

The `agent.state` in `useAgent` is reactive and will automatically update when the agent state changes.

### On this page

What is this?When should I use this?ImplementationRendering agent state in your app
