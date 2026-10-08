---
url: https://docs.copilotkit.ai/deepagents/backend/self-managed-agents/
title: Self-managed agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:58:58.363565+00:00
---

# Self-managed agents

> Source: https://docs.copilotkit.ai/deepagents/backend/self-managed-agents/

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

[Deep Agents](https://docs.copilotkit.ai/deepagents)Runtime

# Self-managed agents

Connect AG-UI agents that you host and secure yourself.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The frontend provider usually talks to your agents through the [runtime](https://docs.copilotkit.ai/deepagents/backend/copilot-runtime): the frontend hits `runtimeUrl`, the runtime discovers agents from `/info`, and a proxy forwards every run server-side. But you can also hand the provider **AG-UI agent instances directly** and skip the runtime for those agents. There are separate production and local-development options, and choosing the right one matters.

## Production: self-managed agents#

`selfManagedAgents` is the supported configuration option for connecting agents you manage yourself, for example an [`HttpAgent`](https://docs.copilotkit.ai/deepagents/backend/ag-ui) pointing at an AG-UI-compatible backend you own and have already secured:

Part of CopilotKit Intelligence

`selfManagedAgents` is part of CopilotKit's [Enterprise Intelligence tier](https://docs.copilotkit.ai/deepagents/intelligence/intelligence-platform). [Talk to an engineer](https://copilotkit.ai/talk-to-an-engineer) about licensing for production use.
    
    
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

Reach for it when you're wiring up an agent locally and don't want to stand up a runtime yet. Don't ship it to production. Switch to `selfManagedAgents` if you intend to manage and secure the connection yourself, or move the agent behind the [runtime](https://docs.copilotkit.ai/deepagents/backend/copilot-runtime).

## How they relate#

Both sources feed the same client-side agent registry. When both are supplied they are merged, and **`selfManagedAgents` wins on a key collision**:
    
    
    // effective agents ≈ { ...agents__unsafe_dev_only, ...selfManagedAgents }

Supplying agents through either provider option also satisfies the frontend configuration check when at least one local agent is registered.

You won't get the `Missing required prop: 'runtimeUrl' or 'publicApiKey' or 'publicLicenseKey'` error; see the [error reference](https://docs.copilotkit.ai/deepagents/troubleshooting/error-reference).

| `selfManagedAgents`| Local agents  
---|---|---  
**Intended for**|  Production, agents you manage| Local dev / prototyping  
**Auth**|  Your responsibility| Your responsibility  
**Runtime middleware / routing**|  Not applied| Not applied  
**Precedence on collision**|  Wins| Overridden by `selfManagedAgents`  
  
## Related#

  * [Copilot Runtime](https://docs.copilotkit.ai/deepagents/backend/copilot-runtime): the recommended runtime-backed path and its trade-offs compared with direct connections.
  * [Connect AG-UI agents](https://docs.copilotkit.ai/deepagents/backend/ag-ui): the `AbstractAgent` / `HttpAgent` interface these options accept.
  * [Auth](https://docs.copilotkit.ai/deepagents/auth): securing agent traffic when you self-manage the connection.



### On this page

Production: self-managed agentsDevelopment: local agentsHow they relateRelated
