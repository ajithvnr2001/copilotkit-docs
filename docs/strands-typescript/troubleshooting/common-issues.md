---
url: https://docs.copilotkit.ai/strands-typescript/troubleshooting/common-issues/
title: Common Copilot Issues
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:30:16.539121+00:00
---

# Common Copilot Issues

> Source: https://docs.copilotkit.ai/strands-typescript/troubleshooting/common-issues/

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

Common Copilot Issues

OtherTroubleshooting

# Common Copilot Issues

Network errors, endpoint not found, tunnel timeouts, and other common issues when wiring up CopilotKit with the Built-in Agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Welcome to the CopilotKit troubleshooting guide. This page covers the most common issues you'll hit while wiring up a Built-in Agent, plus the usual fixes.

Have an issue not listed here? Open a ticket on [GitHub](https://github.com/CopilotKit/CopilotKit/issues) or reach out on [Discord](https://discord.com/invite/6dffbvGU3D) and we'll help. PRs adding your own troubleshooting notes are very welcome.

## Network errors / API not found#

If you're getting network or API errors, here's how to troubleshoot.

Check your endpoint configuration

Verify the configured `runtimeUrl`.
    
    
    <CopilotKit runtimeUrl="/api/copilotkit">
      {/* Your app */}
    </CopilotKit>

Or, if you're using CopilotCloud:
    
    
    <CopilotKit publicApiKey="<your-copilot-cloud-public-api-key>">
      {/* Your app */}
    </CopilotKit>

Common issues:

  * Missing leading slash in the endpoint path
  * Wrong path relative to your app's base URL (or, if absolute, wrong full URL)
  * Typos in the endpoint path


  * Using CopilotCloud but also setting `runtimeUrl`. Omit `runtimeUrl` and keep only `publicApiKey`



localhost vs 127.0.0.1

If you're running locally and getting connection errors, try `127.0.0.1` instead of `localhost`:
    
    
    # If this doesn't work:
    http://localhost:3000/api/copilotkit
    
    # Try this instead:
    http://127.0.0.1:3000/api/copilotkit

Usually caused by local DNS / `/etc/hosts` issues.

Verify your backend is running

Make sure your backend:

  * Is actually running on the port you expect
  * Is reachable from your frontend
  * Isn't blocked by CORS or a firewall



Revisit the [quickstart](https://docs.copilotkit.ai/strands-typescript/troubleshooting/quickstart) if you want to double-check your setup.

## "Remote Endpoint not found" error#

If you're getting a _"CopilotKit's Remote Endpoint not found"_ error, the `/info` endpoint isn't reachable from the runtime.

Check your FastAPI / backend setup

Confirm the CopilotKit SDK is mounted. If you're using Python + FastAPI, follow the [Remote Python Endpoint](https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints) guide.

Test the /info endpoint directly
    
    
    curl -v -d '{}' http://localhost:8000/copilotkit/info

You should see a `200 OK` and a JSON body like:
    
    
    {
      "actions": [],
      "agents": [
        { "name": "my_agent", "description": "A helpful agent.", "type": "langgraph_agui" }
      ],
      "sdkVersion": "0.1.32"
    }

If you see a different response, check your server logs.

## Tunnel creation hangs#

If the tunnel creation process spins indefinitely, your router or ISP might be blocking the tunnel service.

Router / ISP blocking tunnel connections

Verify connectivity:
    
    
    ping tunnels.devcopilotkit.com
    curl -I https://tunnels.devcopilotkit.com
    telnet tunnels.devcopilotkit.com 443

If any of these fail:

  * Check your router security settings
  * Contact your ISP to see if they're blocking the connection
  * Try a different network to confirm



## The Built-in Agent responds with an empty message#

Usually one of:

  * The LLM model string isn't supported by the runtime's provider. Check it against [Model Selection](https://docs.copilotkit.ai/strands-typescript/model-selection).
  * The Built-in Agent's `prompt` is empty and the user message gives it nothing useful to do. Give the agent a system prompt.
  * A frontend tool is throwing during its handler and the agent is treating the empty result as the turn output. See [Error Debugging](https://docs.copilotkit.ai/strands-typescript/troubleshooting/common-issues/error-debugging) for the `tool_handler_failed` code.



## Tools I registered don't show up#

  * Open the [Inspector](https://docs.copilotkit.ai/strands-typescript/troubleshooting/inspector). Go to **Agents** , then **Frontend Tools**. If the tool isn't listed, the hook call didn't land. Confirm the component is actually mounted.
  * If the tool is listed but the agent never calls it, the model may not know when to use it. Tweak the `description` to include the trigger phrase. For LangGraph agents, also add an explicit instruction in `system_prompt` — especially for mandatory data-fetch tools where the agent must call the tool before answering. See [Ensuring your agent reliably calls frontend tools](https://docs.copilotkit.ai/integrations/langgraph/frontend-tools#ensuring-your-agent-reliably-calls-frontend-tools) for the recommended pattern.
  * For v1 to v2 migrations, `useCopilotAction` split into `useFrontendTool`, `useComponent`, and `useHumanInTheLoop`. Make sure you're using the right one.



## Connect route returns 404 on a fresh thread#

If you self-host the runtime and see a `404` from `POST /agent/:agentId/connect` right after the page loads, before any message is sent, it's almost always one of two things:

The agentId isn't registered (most common)

The runtime returns a `404` with this body when no agent matches the id in the URL:
    
    
    { "error": "Agent not found", "message": "Agent 'default' does not exist" }

The prebuilt components connect to the agent named `"default"` unless you pass an explicit `agentId`. Register one under that key:
    
    
    new CopilotRuntime({ agents: { default: myAgent } });

Confirm the agent shows up by hitting [`GET {runtimeUrl}/info`](https://docs.copilotkit.ai/strands-typescript/backend/runtime-endpoints) directly. See also the [error reference](https://docs.copilotkit.ai/strands-typescript/troubleshooting/common-issues/error-reference#agent-not-found--agent-id-does-not-exist).

connect() runs before run() on a new thread

The frontend mints a thread id and may call `connect()` to re-attach **before** the first `run()` has produced any events. A persistence backend that only learns about a thread once a run starts can 404 (or error) on that first connect.

The built-in [`InMemoryAgentRunner`](https://docs.copilotkit.ai/strands-typescript/backend/agent-runner) handles the common cases, but a custom runner backed by an external memory layer must handle the "unknown thread" path explicitly. Return an empty `RUN_STARTED`, `MESSAGES_SNAPSHOT`, `RUN_FINISHED` sequence instead of failing. The [AWS AgentCore integration](https://docs.copilotkit.ai/strands-typescript/deploy/agentcore) shows the exact pattern.

## Runtime memory keeps growing or the process runs out of heap#

A long-lived server on the default `InMemoryAgentRunner` accumulates thread history in process memory.

Tune or lower the in-memory bounds

The store is bounded by default (1000 threads, 100 runs per thread, ~512 MiB of retained history), but those defaults assume a reasonably sized heap. If your process runs with a small `--max-old-space-size`, or your threads carry unusually large payloads, lower the limits:
    
    
    new InMemoryAgentRunner({ maxThreads: 200, maxBytes: 64 * 1024 ** 2 });

See [bounding in-memory history](https://docs.copilotkit.ai/strands-typescript/backend/agent-runner#bounding-in-memory-history) for what each bound covers and what it deliberately does not.

You saw an eviction warning in the logs

`InMemoryAgentRunner evicted in-memory thread history...` means the bounds are doing their job — the process is safe, but that thread's scrollback is gone and will not come back. If losing history matters, move to a durable runner: [Self-host CopilotKit Intelligence](https://docs.copilotkit.ai/strands-typescript/intelligence/self-hosting), or your own [custom runner](https://docs.copilotkit.ai/strands-typescript/backend/agent-runner#extending-a-runner-for-a-custom-backend) backed by your datastore.

### On this page

Network errors / API not found"Remote Endpoint not found" errorTunnel creation hangsThe Built-in Agent responds with an empty messageTools I registered don't show upConnect route returns 404 on a fresh threadRuntime memory keeps growing or the process runs out of heap
