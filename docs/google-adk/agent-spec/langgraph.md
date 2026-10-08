---
url: https://docs.copilotkit.ai/google-adk/agent-spec/langgraph/
title: Agent Spec LangGraph Integration with AG-UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:16.112727+00:00
---

# Agent Spec LangGraph Integration with AG-UI

> Source: https://docs.copilotkit.ai/google-adk/agent-spec/langgraph/

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

[Google ADK](https://docs.copilotkit.ai/google-adk)[Open Agent Spec](https://docs.copilotkit.ai/google-adk/agent-spec)

# Agent Spec LangGraph Integration with AG-UI

Install pyagentspec with the LangGraph adapter and expose a FastAPI endpoint that streams AG‑UI events for CopilotKit.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

Wire an Agent Spec agent backed by LangGraph to CopilotKit’s UI via the AG‑UI event protocol. You’ll run a FastAPI endpoint that emits AG‑UI events and point your Next.js app at it.

Key pieces:

  * Backend endpoint: `ag-ui/integrations/agent-spec/python/ag_ui_agentspec/endpoint.py`
  * Example server: `ag-ui/integrations/agent-spec/python/examples/server.py`
  * Template UI: `npx copilotkit@latest create`



## When should I use this?#

Use this integration when you already have a LangGraph-based agent described by an Agent Spec and want a turnkey UI that streams assistant text, tool calls/results, and run lifecycle with minimal wiring.

## Prerequisites#

  * Python 3.10–3.14
  * Node.js 20+
  * An Agent Spec config JSON/YAML file (or Python code via `pyagentspec`)



## Install the Agent Spec AG-UI integration#

From the AG‑UI repo’s Agent Spec integration package:
    
    
    git clone https://github.com/ag-ui-protocol/ag-ui.git
    cd ag-ui/integrations/agent-spec/python
    uv pip install -e .[langgraph]

Note that this installs `pyagentspec` from source. Alternatively, you may install it with pip:
    
    
    pip install pyagentspec[langgraph]

## Steps#

### 1\. Start a FastAPI endpoint (minimal example)#

Use the LangGraph runtime to execute your Agent Spec and stream AG‑UI events.
    
    
    from fastapi import FastAPI
    from ag_ui_agentspec.agent import AgentSpecAgent
    from ag_ui_agentspec.endpoint import add_agentspec_fastapi_endpoint
    
    agentspec_json = <loaded json/yaml string of your Agent Spec config>
    
    app = FastAPI()
    agent = AgentSpecAgent(agentspec_json, runtime="langgraph")
    add_agentspec_fastapi_endpoint(app, agentspec_agent=agent, path="/")

Run locally:
    
    
    uvicorn backend.app:app --reload --port 8000

### 2\. Scaffold and connect the UI#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

If you already have the starter, make sure your agent runs on port 8000.

Then run the app (for example with `pnpm dev`) and open `http://localhost:3000`.

## How it works#

  * `AgentSpecAgent(runtime="langgraph")` executes your Agent Spec agent with the LangGraph framework.
  * In the `AgentSpecAgent` wrapper, `AgUiSpanProcessor` maps Agent Spec tracing spans to AG‑UI events on a per‑request queue (`EVENT_QUEUE`).
  * The FastAPI endpoint streams those events as SSE for CopilotKit to render: 
    * assistant text: `TEXT_MESSAGE_START/CONTENT/END`
    * tool calls: `TOOL_CALL_START/ARGS/END` and `TOOL_CALL_RESULT`
    * lifecycle: `RUN_STARTED/RUN_FINISHED`



## Troubleshooting#

  * The endpoint path must match your UI’s expected agent endpoint (port 8000 in our starter repo).
  * The endpoint asserts a queue is bound. If you get queue errors, check that requests go through the provided FastAPI route.
  * If you are not receiving any events, make sure the agent is running and did not crash.



## Next steps#

  * Build richer UIs with agentic chat and generative UI.
  * Pass full chat history between turns. The adapter and processor handle messages and tool‑call lifecycle for you.
  * Check out the [WayFlow runtime](https://docs.copilotkit.ai/agent-spec/wayflow)



Starter template: <https://github.com/CopilotKit/CopilotKit/tree/main/examples/integrations/agent-spec> (see the README for installation options)

## Learn more#

  * AG-UI docs: <https://docs.ag-ui.com/introduction>
  * Agent Spec docs home: <https://oracle.github.io/agent-spec/development/docs_home.html>
  * Specification overview: <https://oracle.github.io/agent-spec/development/agentspec/index.html>
  * Agent Spec tracing docs: <https://oracle.github.io/agent-spec/26.1.0/agentspec/tracing.html>
  * Agent Spec LangGraph adapter docs: <https://oracle.github.io/agent-spec/26.1.0/adapters/langgraph/index.html>



### On this page

What is this?When should I use this?PrerequisitesInstall the Agent Spec AG-UI integrationSteps1\. Start a FastAPI endpoint (minimal example)2\. Scaffold and connect the UIHow it worksTroubleshootingNext stepsLearn more
