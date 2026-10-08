---
url: https://docs.copilotkit.ai/agno/agent-spec/
title: Open Agent Spec
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:45:53.520490+00:00
---

# Open Agent Spec

> Source: https://docs.copilotkit.ai/agno/agent-spec/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAgno

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/agno)[Quickstart](https://docs.copilotkit.ai/agno/quickstart)[Build with agents](https://docs.copilotkit.ai/agno/build-with-agents)[Intelligence](https://docs.copilotkit.ai/agno/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/agno/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/agno/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/agno/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/agno/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/agno/learning)

[User Memories](https://docs.copilotkit.ai/agno/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/agno/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/agno/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/agno/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/agno/intelligence/analytics)[Channels](https://docs.copilotkit.ai/agno/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/agno/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Agno](https://docs.copilotkit.ai/agno)

# Open Agent Spec

Bring your Agent‑Spec agents to your users with CopilotKit via AG‑UI.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

# Open Agent Spec x CopilotKit

Open Agent Spec (Agent Spec), originally developed by Oracle, is a portable language for defining agentic systems. It defines building blocks for standalone agents and structured agentic workflows as well as common ways of composing them into multi-agent systems. Agent Spec enables users to author agents once and run them with any compatible runtime. Agent Spec decouples design from execution, helping deliver more predictable behavior across frameworks.

Now, with the CopilotKit integration, you can bring your Agent Spec agents to an interactive UI using CopilotKit and AG‑UI. Use our Next.js starter to connect a CopilotKit UI to your Agent Spec FastAPI endpoint that streams AG‑UI events.

This integration is centered on two components:

  * **Backend:** AG‑UI exporter for Agent Spec (`pyagentspec` Python package) at [the AG-UI GitHub repo](https://github.com/ag-ui-protocol/ag-ui/tree/main/integrations/agent-spec/python). It loads an Agent Spec config (yaml/json) and runs it on your chosen framework via supported Agent Spec adapters (currently LangGraph or WayFlow), translating Agent Spec tracing events into AG‑UI events and sending them to the CopilotKit-powered frontend via a FastAPI endpoint.
  * **Frontend:** CopilotKit UI (Next.js) that consumes AG‑UI events and renders chat, tool calls/results, and generative UI.



Quickly scaffold the UI, then wire your backend endpoint that streams AG‑UI events.

## Quickstart#
    
    
    npx copilotkit@latest create

Then set your backend endpoint (default `http://localhost:8000/copilotkit`):

.env.local
    
    
    COPILOTKIT_REMOTE_ENDPOINT=http://localhost:8000/copilotkit

Run your Agent Spec FastAPI server and start the Next.js app. For backend installation and endpoint wiring, follow the [Quickstart](https://docs.copilotkit.ai/agent-spec/quickstart) and the per‑adapter guides: [LangGraph integration](https://docs.copilotkit.ai/agent-spec/langgraph) and [WayFlow integration](https://docs.copilotkit.ai/agent-spec/wayflow).

## How it works#

  * Backend: Your FastAPI endpoint (from the AG-UI Agent Spec integration) emits AG‑UI SSE events.
  * Frontend: The Next.js template proxies requests to your backend using CopilotKit Runtime.
  * Protocol: AG‑UI spans/events power streaming text, tool calls and results, and run lifecycle.



## Repos and references#

  * Example FastAPI server: `ag-ui/integrations/agent-spec/python/examples/server.py`
  * Endpoint helper: `ag-ui/integrations/agent-spec/python/ag_ui_agentspec/endpoint.py`
  * AG‑UI Agent Spec integration (Python): <https://github.com/ag-ui-protocol/ag-ui/tree/main/integrations/agent-spec/python>
  * AG‑UI Agent Spec tutorial (Agent Spec docs): <https://oracle.github.io/agent-spec/26.1.0/howtoguides/howto_ag_ui.html>



## Learn more about Agent Spec#

  * Agent Spec docs home: <https://oracle.github.io/agent-spec/development/docs_home.html>
  * Specification overview: <https://oracle.github.io/agent-spec/development/agentspec/index.html>
  * API reference: <https://oracle.github.io/agent-spec/development/api/index.html>
  * Reference sheet: <https://oracle.github.io/agent-spec/development/misc/reference_sheet.html>



### On this page

QuickstartHow it worksRepos and referencesLearn more about Agent Spec
