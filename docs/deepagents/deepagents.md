---
url: https://docs.copilotkit.ai/deepagents/deepagents/
title: Deep Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:59:53.562430+00:00
---

# Deep Agents

> Source: https://docs.copilotkit.ai/deepagents/deepagents/

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

On this page

[Deep Agents](https://docs.copilotkit.ai/deepagents)

# Deep Agents

Leverage LangGraph Deep Agents to build sophisticated agentic applications.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

Before you begin, you'll need the following:

  * An OpenAI API key
  * Node.js 20+
  * Your favorite package manager
  * A LangSmith API key - only required if deploying to LangSmith Platform



## Getting started#

### Initialize your agent project#

If you don't already have a Python project set up, create one using `uv`:
    
    
    uv init my-agent
    cd my-agent

### Add necessary dependencies#

For this agent, we'll just need the `deepagents`, `langchain-openai`, and `copilotkit` packages:
    
    
    uv add deepagents copilotkit langchain-openai

If you already have a LangGraph agent written, just reference the following code. In this step we create a simple LangGraph agent for the sake of demonstration.

LangSmithFastAPI

First, we'll create a simple LangGraph agent:

main.py
    
    
    from deepagents import create_deep_agent
    from copilotkit import CopilotKitMiddleware
    from langgraph.checkpoint.memory import MemorySaver
    
    def get_weather(location: str):
        """Get weather for a location"""
        return f"The weather in {location} is sunny."
    
    agent = create_deep_agent(
        model="openai:gpt-5.4",
        tools=[get_weather],
        middleware=[CopilotKitMiddleware()], # for frontend tools and context
        system_prompt="You are a helpful research assistant.",
    )
    
    graph = agent

Then to test and deploy with LangSmith, we'll also need a `langgraph.json`
    
    
    touch langgraph.json

langgraph.json
    
    
    {
        "python_version": "3.12",
        "dockerfile_lines": [],
        "dependencies": ["."],
        "package_manager": "uv",
        "graphs": {
            "sample_agent": "./main.py:agent"
        },
        "env": ".env"
    }

First, add the `ag-ui-langgraph`, `fastapi`, and `uvicorn` packages to your project:
    
    
    uv add ag-ui-langgraph fastapi uvicorn

Then create a simple LangGraph agent, add a FastAPI app, and build attach our agent as an AG-UI endpoint.

main.py
    
    
    import os
    from fastapi import FastAPI 
    import uvicorn
    
    from ag_ui_langgraph import add_langgraph_fastapi_endpoint
    from copilotkit import CopilotKitMiddleware, CopilotKitState, LangGraphAGUIAgent
    from deepagents import create_deep_agent
    from langgraph.checkpoint.memory import MemorySaver
    
    def get_weather(location: str):
        """Get weather for a location"""
        return f"The weather in {location} is sunny."
    
    agent = create_deep_agent(
        model="openai:gpt-5.4",
        tools=[get_weather],
        middleware=[CopilotKitMiddleware()], # for frontend tools and context
        system_prompt="You are a helpful research assistant.",
        checkpointer=MemorySaver()
    )
    
    app = FastAPI()
    
    add_langgraph_fastapi_endpoint(
        app=app,
        agent=LangGraphAGUIAgent(
            name="sample_agent",
            description="An example agent to use as a starting point for your own agent.",
            graph=agent,
        ),
        path="/",
    )
    
    def main():
        """Run the uvicorn server."""
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8123,
            reload=True,
        )
    
    if __name__ == "__main__":
        main()

What is AG-UI?

AG-UI is an open protocol for frontend-agent communication.

### Configure your environment#

Create a `.env` file in your agent directory and add your OpenAI API key:

.env
    
    
    OPENAI_API_KEY=your_openai_api_key

What about other models?

The starter template is configured to use OpenAI's GPT-4o by default, but you can modify it to use any language model supported by LangGraph.

### Create your frontend#

CopilotKit works with any React-based frontend. We'll use Next.js for this example.
    
    
    npx create-next-app@latest frontend
    cd frontend

### Install CopilotKit packages#
    
    
    npm install @copilotkit/react-core @copilotkit/runtime

### Setup Copilot Runtime#

Create an API route to connect CopilotKit to your LangGraph agent:
    
    
    mkdir -p app/api/copilotkit && touch app/api/copilotkit/route.ts

LangSmithFastAPI

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
      InMemoryAgentRunner,
    } from "@copilotkit/runtime/v2";
    import { LangGraphAgent } from "@copilotkit/runtime/langgraph";
    
    const runtime = new CopilotRuntime({
        agents: {
            sample_agent: new LangGraphAgent({
    deploymentUrl:  process.env.LANGGRAPH_DEPLOYMENT_URL || "http://localhost:8123",
                graphId: "sample_agent",
    langsmithApiKey: process.env.LANGSMITH_API_KEY || "",
            }),
        },
      runner: new InMemoryAgentRunner(),
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
      InMemoryAgentRunner,
    } from "@copilotkit/runtime/v2";
    import { HttpAgent } from "@ag-ui/client";
    
    const runtime = new CopilotRuntime({
        agents: {
            sample_agent: new HttpAgent({
    url:  process.env.LANGGRAPH_DEPLOYMENT_URL || "http://localhost:8123",
            }),
        },
      runner: new InMemoryAgentRunner(),
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

### Configure CopilotKit Provider#

Wrap your application with the CopilotKit provider:

app/providers.tsx
    
    
    "use client";
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    export function Providers({ children }: { children: React.ReactNode }) {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit" agent="sample_agent" useSingleEndpoint={false}>
          {children}
        </CopilotKit>
      );
    }

`app/layout.tsx` is a server component and cannot import the provider directly, so it renders your client file instead:

app/layout.tsx
    
    
    import { Providers } from "./providers";
    import "@copilotkit/react-core/v2/styles.css";
    
    // ...
    
    export default function RootLayout({ children }: {children: React.ReactNode}) {
        return (
            <html lang="en">
                <body>
                    <Providers>
                        {children}
                    </Providers>
                </body>
            </html>
        );
    }

### Add the chat interface#

Add the CopilotSidebar component to your page:

app/page.tsx
    
    
    "use client";
    
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    import { useDefaultRenderTool } from "@copilotkit/react-core/v2";
    
    export default function Page() {
        useDefaultRenderTool({
        render: ({name, status, args, result}) => (
            <details>
                <summary>
                    {status === "complete"? `Called ${name}` : `Calling ${name}`}
                </summary>
    
                <p>Status: {status}</p>
                <p>Args: {JSON.stringify(args)}</p>
                <p>Result: {JSON.stringify(result)}</p>
            </details>
        )})
    
        return (
            <main>
                <h1>Your App</h1>
                <CopilotSidebar />
            </main>
        );
    }

### Start your agent#

From your agent directory, start the agent server:

LangSmithFastAPI
    
    
    cd ..
    npx @langchain/langgraph-cli dev --port 8123 --no-browser
    
    
    cd ..
    uv run main.py

Your agent will be available at `http://localhost:8123`.

### Start your UI#

In a separate terminal, navigate to your frontend directory and start the development server:

npmpnpmyarnbun
    
    
    cd frontend
    npm run dev
    
    
    cd frontend
    pnpm dev
    
    
    cd frontend
    yarn dev
    
    
    cd frontend
    bun dev

### On this page

PrerequisitesGetting started
