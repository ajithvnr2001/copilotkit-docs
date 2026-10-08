---
url: https://docs.copilotkit.ai/strands-typescript/troubleshooting/error-reference/
title: Error message reference
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:30:19.146072+00:00
---

# Error message reference

> Source: https://docs.copilotkit.ai/strands-typescript/troubleshooting/error-reference/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands-typescript)[Quickstart](https://docs.copilotkit.ai/strands-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/strands-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands-typescript/webmcp)

Agent capabilities

AWS Strands (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/strands-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands-typescript/learning)

[User Memories](https://docs.copilotkit.ai/strands-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands-typescript/intelligence/channels)

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

[Common Copilot Issues](https://docs.copilotkit.ai/strands-typescript/troubleshooting/common-issues)[Error message reference](https://docs.copilotkit.ai/strands-typescript/troubleshooting/error-reference)[Error Debugging & Observability](https://docs.copilotkit.ai/strands-typescript/troubleshooting/error-debugging)[Inspector and dev console](https://docs.copilotkit.ai/strands-typescript/troubleshooting/inspector-dev-console)[Debug Mode](https://docs.copilotkit.ai/strands-typescript/troubleshooting/debug-mode)[AG-UI Event Inspector](https://docs.copilotkit.ai/strands-typescript/troubleshooting/event-inspector)[Hook Explorer](https://docs.copilotkit.ai/strands-typescript/troubleshooting/hook-explorer)

[Open-source telemetry](https://docs.copilotkit.ai/strands-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Error message reference

OtherTroubleshooting

# Error message reference

Find the cause and fix for common CopilotKit console, network, and error UI messages.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This page lists the error strings CopilotKit surfaces in your console, network responses, and error UI. If you hit an error, search this page with Cmd/Ctrl-F for a distinctive phrase from the message.

For the programmatic `onError` **codes** (`runtime_info_fetch_failed`, `tool_handler_failed`, ...) rather than these human-readable strings, see [Error Debugging](https://docs.copilotkit.ai/strands-typescript/troubleshooting/error-debugging).

## Missing runtime configuration#

Error string:
    
    
    Missing required prop: 'runtimeUrl' or 'publicApiKey' or 'publicLicenseKey'

**Where:** the **v2** provider, `<CopilotKitProvider>`, imported from `@copilotkit/react-core/v2`. In production (`NODE_ENV === "production"`) it's a thrown `Error`; in development it's a `console.warn` so local-agent and test setups still run.

v1 behaves differently

The **v1** `<CopilotKit>` provider throws in **both development and production** when nothing is configured, whereas the v2 `<CopilotKitProvider>` only warns in development. Either way, registering `selfManagedAgents` or `agents__unsafe_dev_only` satisfies the check — no `runtimeUrl` or Copilot Cloud key required.

**Cause:** the provider has no way to reach an agent. You didn't pass a `runtimeUrl`, a Copilot Cloud key (`publicApiKey` / `publicLicenseKey`), **and** you didn't register any local agents.

**Fix (v2):** provide one of these values to `CopilotKitProvider`, imported from `@copilotkit/react-core/v2`:
    
    
    // Runtime-backed (recommended)
    <CopilotKitProvider runtimeUrl="/api/copilotkit">{children}</CopilotKitProvider>
    
    // Copilot Cloud
    <CopilotKitProvider publicApiKey="ck_pub_...">{children}</CopilotKitProvider>
    
    // Agents you manage yourself — the `selfManagedAgents` prop is also accepted by the v1 `<CopilotKit>` wrapper
    <CopilotKitProvider selfManagedAgents={{ "my-agent": myAgent }}>{children}</CopilotKitProvider>

See [Self-managed agents](https://docs.copilotkit.ai/strands-typescript/backend/self-managed-agents) for the local-agent path.

## Agent discovery failed#

Error name:
    
    
    CopilotKitAgentDiscoveryError

This is the error **name** (`error.name`). The accompanying message is one of:

  * `Agent '<name>' was not found. Available agents are: <list>. Please verify the agent name in your configuration and ensure it matches one of the available agents.`
  * `The requested agent was not found. Available agents are: <list>. ...`
  * `Agent '<name>' was not found. Please set up at least one agent before proceeding.` (when **no** agents are registered)



**Cause:** the frontend asked for an `agentId` that the runtime didn't return from its `/info` discovery. This is usually a typo, a missing registration, or a runtime that has no agents at all. The prebuilt components default to the agent named `"default"`.

**Fix:**

  * Register the agent under the id you're requesting (or under `"default"` if you pass no `agentId`): 
        
        new CopilotRuntime({ agents: { default: myAgent } });

  * Confirm the id matches the "Available agents" list in the message.
  * Verify the runtime is reachable by hitting `GET {runtimeUrl}/info` directly (see [Runtime HTTP endpoints](https://docs.copilotkit.ai/strands-typescript/backend/runtime-endpoints)). A discovery failure here cascades into this error.



`CopilotKitAgentDiscoveryError` is a **banner** error. It renders as a fixed banner in the dev console rather than a dismissible toast.

## Agent route returned 404#

Error strings:
    
    
    Agent not found
    Agent '<id>' does not exist

**Where:** an HTTP `404` JSON body from the runtime's agent routes:
    
    
    { "error": "Agent not found", "message": "Agent 'my-agent' does not exist" }

**Cause:** a `POST /agent/:agentId/run`, `/connect`, or `/stop/:threadId` request named an `agentId` that isn't registered on the runtime. This is the server-side counterpart to the client-side `CopilotKitAgentDiscoveryError`.

**Fix:** register the agent under that key in `new CopilotRuntime({ agents: { ... } })`. If you see this on the `/connect` route **before sending any message** , also read [the `/connect` 404 entry](https://docs.copilotkit.ai/strands-typescript/troubleshooting/common-issues#connect-route-returns-404-on-a-fresh-thread).

## Agent run failed#

Error string:
    
    
    Failed to run agent

**Where:** a `500` JSON body from the runtime's run/connect routes, with a `message` field carrying the underlying error.

**Cause:** the agent threw while executing. Common causes include a bad model string, a missing API key on the server, a provider error, or an exception inside the agent itself.

**Fix:** read the `message` field and check your server logs (the runtime logs the error name, message, and stack). Common culprits: an unset `OPENAI_API_KEY` (or equivalent) on the server, or a model string the provider doesn't recognize.

## Capability discovery failed#

Error string:
    
    
    Failed to fetch capabilities for agent "<name>"

**Where:** logged on the client when capability discovery for an agent fails.

**Cause:** the runtime couldn't be reached, or the named agent's capabilities endpoint errored.

**Fix:** confirm `runtimeUrl` is correct and the runtime is up; verify `GET {runtimeUrl}/info` returns the agent. See [Common Issues: Network errors](https://docs.copilotkit.ai/strands-typescript/troubleshooting/common-issues#network-errors--api-not-found).

## Related#

  * [Error Debugging](https://docs.copilotkit.ai/strands-typescript/troubleshooting/error-debugging): the `onError` callback and its programmatic error **codes**.
  * [Common Issues](https://docs.copilotkit.ai/strands-typescript/troubleshooting/common-issues): network, endpoint, and tunnel problems.
  * [Runtime HTTP endpoints](https://docs.copilotkit.ai/strands-typescript/backend/runtime-endpoints): probing `/info` and the agent routes with `curl`.



### On this page

Missing runtime configurationAgent discovery failedAgent route returned 404Agent run failedCapability discovery failedRelated
