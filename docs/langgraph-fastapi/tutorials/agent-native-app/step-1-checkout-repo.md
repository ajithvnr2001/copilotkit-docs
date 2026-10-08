---
url: https://docs.copilotkit.ai/langgraph-fastapi/tutorials/agent-native-app/step-1-checkout-repo/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:06:11.728518+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/langgraph-fastapi/tutorials/agent-native-app/step-1-checkout-repo/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-fastapi/webmcp)

Agent capabilities

LangGraph (FastAPI)

[Sub-agents](https://docs.copilotkit.ai/langgraph-fastapi/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-fastapi/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-fastapi/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-fastapi/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# Quickstart

Turn your LangGraph agent into an agent-native application in 10 minutes.

## Start with your coding agent#

Use this prompt to connect your LangGraph agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

Before you begin, you'll need the following:

  * An OpenAI API key
  * Node.js 20+
  * Your favorite package manager
  * (Optional) A LangSmith API key - only required if using an existing LangGraph agent



Zod version for TypeScript agents

When adding `@copilotkit/sdk-js` 1.71.0 to a TypeScript agent, install Zod 3 alongside it:
    
    
    npm install @copilotkit/sdk-js@1.71.0 zod@3

An unversioned `zod` install selects Zod 4, which does not satisfy this SDK release's peer dependency. Use `zod@3` with pnpm or Yarn too. If your agent already requires Zod 4, check SDK compatibility before changing its dependencies; do not bypass the conflict with `--force` or `--legacy-peer-deps`.

## Getting started#

### Set up CopilotKit Intelligence#

[Sign in to cloud-hosted Intelligence](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_langgraph_quickstart_step1&utm_frontend=react&utm_backend=langgraph-fastapi). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you create it below.

### Choose your starting point#

You can either start fresh with our starter template or integrate CopilotKit into your existing LangGraph agent.

### 🎉 Start chatting!#

Your AI agent is now ready to use! Try asking it some questions:
    
    
    Can you tell me a joke?
    
    
    Can you help me understand AI?
    
    
    What do you think about React?

Troubleshooting

  * **Connection issues? Keep`localhost`, don't swap in a literal IP.** Which loopback address reaches the agent depends on the runtime, and `0.0.0.0` is a bind-all address for a server, never a valid target in a client URL.

PythonTypeScript

`langgraph dev` (the Python CLI) defaults to `--host 127.0.0.1`, so both `http://127.0.0.1:8123` and `http://localhost:8123` reach it. `http://[::1]:8123` does not — the server is not listening on IPv6.

`@langchain/langgraph-cli` (the `langgraphjs` binary) defaults to `--host localhost`, which Node resolves to IPv6 on a dual-stack machine, binding `::1` **only**. So `http://localhost:8123` and `http://[::1]:8123` reach it, while `http://127.0.0.1:8123` is refused by that same running server — switching to `127.0.0.1` is what breaks it. If you need IPv4, bind it explicitly with `langgraphjs dev --host 127.0.0.1`.

  * Make sure your agent folder contains a `langgraph.json` file

  * In the `langgraph.json` file, reference the path to a `.env` file

  * Check that your OpenAI API key is correctly set in the `.env` file

  * If using an existing agent, ensure your LangSmith API key is also configured

  * Make sure you're in the same folder as your `langgraph.json` file when running the `langgraph dev` command

  * **Connection refused from the runtime?** Check the port. A bare `langgraph dev` listens on `2024`; this guide's start command pins `8123` with `--port 8123`. The runtime's `LANGGRAPH_DEPLOYMENT_URL` (or its fallback) has to name the port the agent actually bound.

  * **"graph is nullish" error (JavaScript starters):** This means the LangGraph CLI couldn't load your graph. Ensure the export name in your `langgraph.json` matches your code (e.g., `"starterAgent": "./src/agent.ts:graph"` requires `export const graph = ...` in `agent.ts`). Also verify all dependencies are installed with `npm install` in your agent directory.

  * Make sure the runtime endpoint path matches the `runtimeUrl` in your CopilotKit provider




### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/langgraph-fastapi/inspector).

## Deploying to AWS?#

If you're planning to deploy your LangGraph agent to AWS Bedrock AgentCore, see the [AgentCore deploy guide](https://docs.copilotkit.ai/langgraph-fastapi/deploy-agentcore).

## What's next?#

Now that you have your basic agent setup, explore these advanced features:

[👤Implement Human in the LoopAllow your users and agents to collaborate together on tasks.](https://docs.copilotkit.ai/langgraph/human-in-the-loop)[🔄Utilize Shared StateLearn how to synchronize your agent's state with your UI's state, and vice versa.](https://docs.copilotkit.ai/langgraph/shared-state)[🎨Add some generative UIRender your agent's progress and output in the UI.](https://docs.copilotkit.ai/langgraph/generative-ui/tool-rendering)[🔧Setup frontend actionsGive your agent the ability to call frontend tools, directly updating your application.](https://docs.copilotkit.ai/langgraph/frontend-tools)
