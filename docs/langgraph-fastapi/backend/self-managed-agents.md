---
url: https://docs.copilotkit.ai/langgraph-fastapi/backend/self-managed-agents/
title: Self-managed agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:04:31.628425+00:00
---

# Self-managed agents

> Source: https://docs.copilotkit.ai/langgraph-fastapi/backend/self-managed-agents/

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

[Copilot Runtime](https://docs.copilotkit.ai/langgraph-fastapi/backend/copilot-runtime)[Runtime HTTP endpoints](https://docs.copilotkit.ai/langgraph-fastapi/backend/runtime-endpoints)[Use any model router](https://docs.copilotkit.ai/langgraph-fastapi/backend/custom-agent)[Write your own AG-UI agent](https://docs.copilotkit.ai/langgraph-fastapi/backend/custom-ag-ui-agent)[AgentRunner and persistence](https://docs.copilotkit.ai/langgraph-fastapi/backend/agent-runner)[Message history](https://docs.copilotkit.ai/langgraph-fastapi/backend/message-history)[Self-managed agents](https://docs.copilotkit.ai/langgraph-fastapi/backend/self-managed-agents)[Connect AG-UI agents](https://docs.copilotkit.ai/langgraph-fastapi/backend/ag-ui)[Deploy to any runtime](https://docs.copilotkit.ai/langgraph-fastapi/runtime-server-adapter)[Authentication](https://docs.copilotkit.ai/langgraph-fastapi/auth)

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

Self-managed agents

BackendRuntime

# Self-managed agents

Connect AG-UI agents that you host and secure yourself.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The frontend provider usually talks to your agents through the [runtime](https://docs.copilotkit.ai/langgraph-fastapi/backend/copilot-runtime): the frontend hits `runtimeUrl`, the runtime discovers agents from `/info`, and a proxy forwards every run server-side. But you can also hand the provider **AG-UI agent instances directly** and skip the runtime for those agents. There are separate production and local-development options, and choosing the right one matters.

## Production: self-managed agents#

`selfManagedAgents` is the supported configuration option for connecting agents you manage yourself, for example an [`HttpAgent`](https://docs.copilotkit.ai/langgraph-fastapi/backend/ag-ui) pointing at an AG-UI-compatible backend you own and have already secured:

Part of CopilotKit Intelligence

`selfManagedAgents` is part of CopilotKit's [Enterprise Intelligence tier](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/intelligence-platform). [Talk to an engineer](https://copilotkit.ai/talk-to-an-engineer) about licensing for production use.
    
    
    import { HttpAgent } from "@ag-ui/client";
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    const supportAgent = new HttpAgent({
      url: "https://agents.example.com/support",
    });
    
    <CopilotKit
      selfManagedAgents={{ "support-agent": supportAgent }}
    >
      <YourApp />
    </CopilotKit>;

Each key is the `agentId` that chat components and frontend agent APIs use to address that agent. Self-managed agents use your transport and your security model. Because the requests don't pass through the CopilotKit runtime, the runtime's server-side auth, middleware, and routing do not apply. Your agent endpoint must authenticate and authorize every request.

You can combine `selfManagedAgents` with `runtimeUrl`. Runtime-discovered agents and self-managed agents coexist; address each by its `agentId`.

## Development: local agents#

`agents__unsafe_dev_only` accepts the same shape: a map of `agentId` to `AbstractAgent`. The name is intentionally loud. Use it only for local development and prototyping.
    
    
    import { HttpAgent } from "@ag-ui/client";
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    const myAgent = new HttpAgent({ url: "http://localhost:8000" });
    
    <CopilotKit agents__unsafe_dev_only={{ "my-agent": myAgent }}>
      <YourApp />
    </CopilotKit>;

Reach for it when you're wiring up an agent locally and don't want to stand up a runtime yet. Don't ship it to production. Switch to `selfManagedAgents` if you intend to manage and secure the connection yourself, or move the agent behind the [runtime](https://docs.copilotkit.ai/langgraph-fastapi/backend/copilot-runtime).

## How they relate#

Both sources feed the same client-side agent registry. When both are supplied they are merged, and **`selfManagedAgents` wins on a key collision**:
    
    
    // effective agents ≈ { ...agents__unsafe_dev_only, ...selfManagedAgents }

Supplying agents through either provider option also satisfies the frontend configuration check when at least one local agent is registered.

You won't get the `Missing required prop: 'runtimeUrl' or 'publicApiKey' or 'publicLicenseKey'` error; see the [error reference](https://docs.copilotkit.ai/langgraph-fastapi/troubleshooting/error-reference).

| `selfManagedAgents`| Local agents  
---|---|---  
**Intended for**|  Production, agents you manage| Local dev / prototyping  
**Auth**|  Your responsibility| Your responsibility  
**Runtime middleware / routing**|  Not applied| Not applied  
**Precedence on collision**|  Wins| Overridden by `selfManagedAgents`  
  
## Related#

  * [Copilot Runtime](https://docs.copilotkit.ai/langgraph-fastapi/backend/copilot-runtime): the recommended runtime-backed path and its trade-offs compared with direct connections.
  * [Connect AG-UI agents](https://docs.copilotkit.ai/langgraph-fastapi/backend/ag-ui): the `AbstractAgent` / `HttpAgent` interface these options accept.
  * [Auth](https://docs.copilotkit.ai/langgraph-fastapi/auth): securing agent traffic when you self-manage the connection.



### On this page

Production: self-managed agentsDevelopment: local agentsHow they relateRelated
