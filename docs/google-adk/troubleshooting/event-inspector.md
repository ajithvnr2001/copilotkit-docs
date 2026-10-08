---
url: https://docs.copilotkit.ai/google-adk/troubleshooting/event-inspector/
title: AG-UI Event Inspector
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:39.926510+00:00
---

# AG-UI Event Inspector

> Source: https://docs.copilotkit.ai/google-adk/troubleshooting/event-inspector/

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

[Common Copilot Issues](https://docs.copilotkit.ai/google-adk/troubleshooting/common-issues)[Error message reference](https://docs.copilotkit.ai/google-adk/troubleshooting/error-reference)[Error Debugging & Observability](https://docs.copilotkit.ai/google-adk/troubleshooting/error-debugging)[Inspector and dev console](https://docs.copilotkit.ai/google-adk/troubleshooting/inspector-dev-console)[Debug Mode](https://docs.copilotkit.ai/google-adk/troubleshooting/debug-mode)[AG-UI Event Inspector](https://docs.copilotkit.ai/google-adk/troubleshooting/event-inspector)[Hook Explorer](https://docs.copilotkit.ai/google-adk/troubleshooting/hook-explorer)

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

AG-UI Event Inspector

OtherTroubleshooting

# AG-UI Event Inspector

Inspect AG-UI events in real time with the VSCode extension

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The AG-UI Event Inspector gives you a live view of every event flowing between your CopilotKit runtime and client. Instead of sprinkling `console.log` statements through your agent code, you can watch the full AG-UI event stream in a filterable, color-coded panel inside VS Code.

Use it when:

  * An agent interaction isn't behaving as expected and you need to see which events the runtime is actually emitting
  * You want to understand the AG-UI event lifecycle (e.g., how `RUN_STARTED` flows through `TEXT_MESSAGE_CONTENT` chunks to `RUN_FINISHED`)
  * You need to inspect tool call arguments or state deltas for a specific interaction



The in-app Inspector locks the Threads tab when the Runtime does not advertise the Threads list capability, regardless of license metadata. The locked view offers **Copy setup prompt** and **Talk to an Engineer**. See [Inspector](https://docs.copilotkit.ai/google-adk/inspector#enable-or-repair-intelligence) for the setup flow.

## Prerequisites#

  * A CopilotKit runtime running locally with `NODE_ENV` set to `development`, or with `debug` enabled on the runtime
  * The [CopilotKit VS Code extension](https://docs.copilotkit.ai/google-adk/vs-code-extension) installed



The `/cpk-debug-events` endpoint streams every event of every thread, including full message content, to any subscriber. It is served in exactly two cases: `NODE_ENV` is `development`, or the runtime sets `debug`. Everywhere else it returns 404.

An _unset_ `NODE_ENV` counts as everywhere else. A plain `node server.js` sets no value, so a self-hosted runtime does not expose the feed by accident. If you need it on such a host, ask for it explicitly:
    
    
    const runtime = new CopilotRuntime({ agents, debug: true });

Treat that as you would any other way of reading conversation content, and do not enable it on a runtime the public can reach.

This stream carries the AG-UI events a **self-hosted** runtime sends over SSE. A runtime configured with `intelligence` does not send them: it answers runs over CopilotKit Intelligence's realtime connection instead. On that runtime `/cpk-debug-events` still connects and reports `: connected`, then stays empty. To trace an Intelligence-backed run, use the in-app [Inspector](https://docs.copilotkit.ai/google-adk/inspector), which reads the events on the client.

## Connect and inspect#

### Ensure your runtime is running in development mode#

The debug event endpoint is available at `GET {runtimeUrl}/cpk-debug-events`. It activates automatically when `NODE_ENV` is `development`, which `next dev` and most dev servers set for you — no extra configuration needed. On a host that sets no `NODE_ENV`, set `debug: true` on the runtime instead.

The path is relative to the `basePath` the runtime is mounted at, not to the server's origin. A runtime mounted at `/api/copilotkit` on port 8200 serves the stream at `http://localhost:8200/api/copilotkit/cpk-debug-events`; requesting `http://localhost:8200/cpk-debug-events` returns `404 {"error":"Not found"}`. Confirm the URL before you connect:
    
    
    curl -N http://localhost:8200/api/copilotkit/cpk-debug-events

A working endpoint responds immediately with `: connected` and then holds the connection open.

### Open the AG-UI Inspector#

Open the VS Code command palette (`Ctrl+Shift+P` / `Cmd+Shift+P`) and run:
    
    
    CopilotKit: Open AG-UI Inspector

This opens a dedicated webview panel.

### Enter your runtime URL and connect#

Type your runtime URL in the input field at the top of the panel (default: `http://localhost:4000`) and click **Connect**. Use the full mounted runtime URL — the same value your frontend passes as `runtimeUrl`, including its base path — not just the origin. The panel status indicator turns green when the SSE connection is established.

### Trigger an agent interaction#

Go to your app and perform an action that triggers an agent run — send a chat message, invoke a tool, or interact with any CopilotKit-powered component. Events start streaming into the inspector immediately.

### Read the event stream#

Each event row shows:

  * **Timestamp** — relative time since the first event (e.g., `+0.142s`)
  * **Event type badge** — color-coded by category (see table below)
  * **Summary** — key fields like message ID, tool name, or a text preview



### Filter events#

Use the category filter buttons at the top of the panel to show or hide event categories. You can also search event payloads with the search field to find specific tool names, message IDs, or content.

### Inspect event details#

Click any event row to expand the full JSON payload in the detail panel. This shows every field the runtime emitted for that event, including `agentId`, `threadId`, `runId`, and the complete event data.

## Event type reference#

Category| Color| Event Types| Description  
---|---|---|---  
**Lifecycle**|  Purple| `RUN_STARTED`, `RUN_FINISHED`| Marks the start and end of an agent run  
**Errors**|  Red| `RUN_ERROR`| An error occurred during the agent run  
**Text Messages**|  Blue| `TEXT_MESSAGE_START`, `TEXT_MESSAGE_CONTENT`, `TEXT_MESSAGE_END`, `TEXT_MESSAGE_CHUNK`| Text streamed from the agent to the client  
**Tool Calls**|  Orange| `TOOL_CALL_START`, `TOOL_CALL_ARGS`, `TOOL_CALL_END`, `TOOL_CALL_CHUNK`, `TOOL_CALL_RESULT`| Tool invocation lifecycle — name, arguments, and result  
**Reasoning**|  Green| `REASONING_START`, `REASONING_MESSAGE_START`, `REASONING_MESSAGE_CONTENT`, `REASONING_MESSAGE_END`, `REASONING_END`| Model reasoning/chain-of-thought events  
**State**|  Teal| `STATE_SNAPSHOT`, `STATE_DELTA`| Agent state snapshots and incremental updates  
**Activity/UI**|  Yellow| `ACTIVITY_SNAPSHOT`, `ACTIVITY_DELTA`| UI activity indicators and progress updates  
  
For console-level debug logging and programmatic error handling in your app, see [Error Debugging](https://docs.copilotkit.ai/google-adk/troubleshooting/error-debugging). If you're debugging a render prop rather than a runtime event stream, the [Hook Explorer](https://docs.copilotkit.ai/google-adk/troubleshooting/hook-explorer) is the offline, render-first complement to this tool.

### On this page

PrerequisitesConnect and inspectEnsure your runtime is running in development modeOpen the AG-UI InspectorEnter your runtime URL and connectTrigger an agent interactionRead the event streamFilter eventsInspect event detailsEvent type reference
