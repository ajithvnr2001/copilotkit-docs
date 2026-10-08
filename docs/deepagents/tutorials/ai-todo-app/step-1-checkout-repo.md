---
url: https://docs.copilotkit.ai/deepagents/tutorials/ai-todo-app/step-1-checkout-repo/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:01:37.172162+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/deepagents/tutorials/ai-todo-app/step-1-checkout-repo/

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

Quickstart

# Quickstart

Get started with Deep Agents and CopilotKit in minutes.

## Start with your coding agent#

Use this prompt to connect your Deep Agents agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

Before you begin, you'll need the following:

  * An OpenAI API key
  * Node.js 20+
  * Your favorite package manager
  * A LangGraph Platform API key - only required if deploying to the Deep Agent platform



## Getting started#

### Set up CopilotKit Intelligence#

[Sign in to cloud-hosted Intelligence](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_deepagents_quickstart_step1&utm_frontend=react&utm_backend=deepagents). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you create it below.

### Initialize your agent project#

PythonTypeScript

If you don't already have a Python project set up, create one using `uv`:
    
    
    uv init my-agent
    cd my-agent

If you don't already have a Node.js project set up, create one using `npm`:
    
    
    mkdir my-agent
    cd my-agent
    npm init -y

### Add necessary dependencies#

PythonTypeScript

Add the `deepagents`, `langchain-openai`, and `copilotkit` packages:
    
    
    uv add deepagents copilotkit langchain-openai

Add the `deepagents`, `@langchain/langgraph`, `@copilotkit/sdk-js`, and `@langchain/openai` packages:
    
    
    npm install deepagents @langchain/langgraph @copilotkit/sdk-js @langchain/openai

### Create your Deep Agent#

PythonTypeScriptFastAPI

Create a simple Deep Agent:

main.py
    
    
    from deepagents import create_deep_agent
    from copilotkit import CopilotKitMiddleware
    
    def get_weather(location: str):
        """Get weather for a location"""
        return f"The weather in {location} is sunny."
    
    agent = create_deep_agent(
        model="openai:gpt-4o",
        tools=[get_weather],
        middleware=[CopilotKitMiddleware()], # for frontend tools and context
        system_prompt="You are a helpful research assistant.",
    )

Then to test and deploy with Deep Agent, create a `langgraph.json`:
    
    
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

Create a simple Deep Agent:

agent.ts
    
    
    import { createDeepAgent } from "deepagents";
    import { copilotkitMiddleware } from "@copilotkit/sdk-js/langgraph";
    import { tool } from "langchain";
    import { z } from "zod";
    
    const getWeather = tool(
        async ({ location }) => `The weather in ${location} is sunny.`,
        {
            name: "get_weather",
            description: "Get the weather for a given location.",
            schema: z.object({ location: z.string().describe("The location to get the weather for") }),
        }
    );
    
    export const agent = createDeepAgent({
        model: "openai:gpt-4o",
        tools: [getWeather],
        middleware: [copilotkitMiddleware],
        systemPrompt: "You are a helpful research assistant.",
    });

Then to test and deploy with Deep Agent, create a `langgraph.json`:
    
    
    touch langgraph.json

langgraph.json
    
    
    {
        "node_version": "20",
        "dependencies": ["."],
        "package_manager": "npm",
        "graphs": {
            "sample_agent": "./agent.ts:agent"
        },
        "env": ".env"
    }

When setting up the Copilot Runtime in the next steps, select the **Deep Agent** tab.

Add the `ag-ui-langgraph`, `fastapi`, and `uvicorn` packages:
    
    
    uv add ag-ui-langgraph fastapi uvicorn

Create a Deep Agent and expose it as an AG-UI endpoint:

main.py
    
    
    from ag_ui_langgraph import add_langgraph_fastapi_endpoint
    from copilotkit import CopilotKitMiddleware, LangGraphAGUIAgent
    from deepagents import create_deep_agent
    from fastapi import FastAPI
    from langgraph.checkpoint.memory import MemorySaver
    
    app = FastAPI()
    
    def get_weather(location: str):
        """Get weather for a location"""
        return f"The weather in {location} is sunny."
    
    agent = create_deep_agent(
        model="openai:gpt-4o",
        tools=[get_weather],
        middleware=[CopilotKitMiddleware()], # for frontend tools and context
        system_prompt="You are a helpful research assistant.",
        checkpointer=MemorySaver()
    )
    
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
        import uvicorn
        uvicorn.run(
            "main:app",
            host="0.0.0.0",
            port=8123,
            reload=True,
        )
    
    if __name__ == "__main__":
        main()

What is AG-UI?

AG-UI is an open protocol for frontend-agent communication. Deep Agents use it to stream state and tool calls to your frontend in real-time.

### Configure your environment#

Create a `.env` file in your agent directory and add your OpenAI API key:

.env
    
    
    OPENAI_API_KEY=your_openai_api_key

Other models

Deep Agents support any model available via LangChain. Change the `model` parameter in `create_deep_agent` to switch providers.

### Create your frontend#

CopilotKit works with any React-based frontend. We'll use Next.js for this example.
    
    
    npx create-next-app@latest frontend
    cd frontend

### Install CopilotKit packages#
    
    
    npm install @copilotkit/react-ui @copilotkit/react-core @copilotkit/runtime

### Setup Copilot Runtime#

Create an API route to connect CopilotKit to your Deep Agent:
    
    
    mkdir -p app/api/copilotkit && touch app/api/copilotkit/route.ts

Using Next.js is optional

If you'd rather skip the Next.js API proxy, see LangChain's [CopilotKit integration guide](https://docs.langchain.com/oss/python/langchain/frontend/integrations/copilotkit) for how to add a custom CopilotKit route directly to your LangGraph deployment.

Deep AgentFastAPI

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotKitIntelligence,
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import { LangGraphAgent } from "@copilotkit/runtime/langgraph";
    
    const runtime = new CopilotRuntime({
        agents: {
            sample_agent: new LangGraphAgent({
    deploymentUrl: process.env.LANGGRAPH_DEPLOYMENT_URL || "http://localhost:8123",
                graphId: "sample_agent",
    langsmithApiKey: process.env.LANGSMITH_API_KEY || "",
            }),
        },
        intelligence: new CopilotKitIntelligence({
          apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
        }),
        // Threads are per-user. Without this, every visitor shares one history.
        identifyUser: (request) => ({
          id: request.headers.get("x-user-id") ?? "anonymous",
          name: request.headers.get("x-user-name") ?? "Anonymous",
        }),
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotKitIntelligence,
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import { HttpAgent } from "@ag-ui/client";
    
    const runtime = new CopilotRuntime({
        agents: {
            sample_agent: new HttpAgent({
    url: process.env.LANGGRAPH_DEPLOYMENT_URL || "http://localhost:8123",
            }),
        },
        intelligence: new CopilotKitIntelligence({
          apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
        }),
        // Threads are per-user. Without this, every visitor shares one history.
        identifyUser: (request) => ({
          id: request.headers.get("x-user-id") ?? "anonymous",
          name: request.headers.get("x-user-name") ?? "Anonymous",
        }),
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

From this frontend app directory, connect the runtime to an Intelligence project:

Terminal
    
    
    npx copilotkit@latest project select

The command writes the server-side project API key to `.env`. The runtime reads it here:

.env
    
    
    CPK_INTELLIGENCE_API_KEY=cpk-...

Running without the Intelligence Platform?

Drop the `intelligence` and `identifyUser` options and the runtime falls back to SSE mode with an in-memory runner. Chat still works, but Threads and the Inspector stay locked and the key is never read. See [Connect your runtime to Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/quickstart) for the full constructor and how to confirm the key is in use.

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
    
    export default function RootLayout({ children }: { children: React.ReactNode }) {
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

This relative runtimeUrl assumes Next.js serves the runtime

`/api/copilotkit` resolves only because Next.js serves your app and the runtime from the same origin. A client-only frontend has no shared origin, so it needs a standalone runtime server of its own and an absolute `runtimeUrl` such as `http://localhost:8200/api/copilotkit`. The per-frontend guides at `/react-spa`, `/vue`, `/angular` and `/react-native` each show that setup.

### Add the chat interface#

Add the CopilotSidebar component to your page:

app/page.tsx
    
    
    "use client";
    
    import { CopilotSidebar } from "@copilotkit/react-core/v2";
    import { useDefaultRenderTool } from "@copilotkit/react-core/v2";
    
    export default function Page() {
        useDefaultRenderTool({
            render: ({ name, status, parameters, result }) => (
                <details>
                    <summary>
                        {status === "complete" ? `Called ${name}` : `Calling ${name}`}
                    </summary>
                    <p>Status: {status}</p>
                    <p>Args: {JSON.stringify(parameters)}</p>
                    <p>Result: {JSON.stringify(result)}</p>
                </details>
            ),
        });
    
        return (
            <main>
                <h1>Your App</h1>
                <CopilotSidebar />
            </main>
        );
    }

### Start your agent#

Deep AgentFastAPI
    
    
    npx @langchain/langgraph-cli dev --port 8123 --no-browser
    
    
    uv run main.py

Your agent will be available at `http://localhost:8123`.

If port 8123 is already in use, change the `--port` flag (or the `port=` argument in the FastAPI `main.py`) and update `LANGGRAPH_DEPLOYMENT_URL` in Step 7 to match.

### Start your UI#

In a separate terminal, navigate to your frontend directory and start the development server:

npmpnpmyarnbun
    
    
    cd frontend && npm run dev
    
    
    cd frontend && pnpm dev
    
    
    cd frontend && yarn dev
    
    
    cd frontend && bun dev

### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/deepagents/inspector).

### On this page

Start with your coding agentPrerequisitesGetting started
