---
url: https://docs.copilotkit.ai/strands/agent-spec/quickstart/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:30:42.083749+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/strands/agent-spec/quickstart/

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

[AWS Strands (Python)](https://docs.copilotkit.ai/strands)[Open Agent Spec](https://docs.copilotkit.ai/strands/agent-spec)

# Quickstart

Set up Agent Spec + AG‑UI and connect a CopilotKit UI. Includes per‑adapter install steps and a minimal endpoint.

## Start with your coding agent#

Use this prompt to connect your Agent Spec agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Prerequisites#

  * Node.js 20+
  * Python 3.10–3.13



## Getting started#

### Set up CopilotKit Intelligence#

[Sign in to cloud-hosted Intelligence](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_agent_spec_quickstart_step1&utm_frontend=react&utm_backend=strands). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you create or clone it below.

### Choose your starting point#

You can either start fresh with our starter template or connect CopilotKit to an existing Agent Spec agent.

## Tools and tool registry#

If your Agent Spec includes server-side tools that execute in the same environment as the agent, map them by name to Python callables in a dictionary `tool_registry` when loading `AgentSpecAgent`.

Bind backend tools by name
    
    
    from __future__ import annotations
    from fastapi import FastAPI
    from ag_ui_agentspec.agent import AgentSpecAgent
    from ag_ui_agentspec.endpoint import add_agentspec_fastapi_endpoint
    
    def get_weather(city: str) -> Dict[str, Any]:
        return {"city": city, "temp_c": 22}
    
    tool_registry = {"get_weather": get_weather}
    
    app = FastAPI()
    agent = AgentSpecAgent(
        agent_spec_config=<json/yaml string of your Agent Spec Agent>,
        runtime="langgraph",  # or "wayflow"
        tool_registry=tool_registry,
    )
    add_agentspec_fastapi_endpoint(app, agentspec_agent=agent, path="/")

Frontend tools (corresponding to Agent Spec `ClientTool`) run in the browser and don't need to be added to the tool registry — see [Generative UI Frontend Tools](https://docs.copilotkit.ai/strands/frontend-tools) for details.

## What is happening under the hood#

Agent Spec, and the `pyagentspec` SDK, helps you define agents and workflows in a readable and portable config object/JSON file. The different adapters, LangGraph and WayFlow, loads your Agent Spec configs into framework-specific objects and executes them. In other words, Agent Spec is the "compiler", and the frameworks are the "runtimes". During this conversion process, the adapter configures the loaded object so that it would emit Agent Spec Tracing events. These are standardized across runtimes. Finally, the AG-UI Agent Spec integration listens to Agent Spec Tracing events and exports them to AG-UI events. These include agent execution, tool calls, messages being sent by the agent, etc. In other words, if the agent emits an event during execution (this is runtime-dependent), a corresponding AG-UI event will be created. In the frontend, CopilotKit converts and renders AG-UI events into the UI.

## Next steps#

Follow per-adapter tutorials: [LangGraph integration](https://docs.copilotkit.ai/agent-spec/langgraph) and [WayFlow integration](https://docs.copilotkit.ai/agent-spec/wayflow).

## Learn more#

  * AG-UI docs: <https://docs.ag-ui.com/introduction>
  * Agent Spec docs: <https://oracle.github.io/agent-spec/development/docs_home.html>
  * Agent Spec x AG-UI tutorial: <https://oracle.github.io/agent-spec/26.1.0/howtoguides/howto_ag_ui.html>
  * Agent Spec Tracing: <https://oracle.github.io/agent-spec/development/agentspec/tracing.html>


