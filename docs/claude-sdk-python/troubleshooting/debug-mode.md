---
url: https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/debug-mode/
title: Debug Mode
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:53.838431+00:00
---

# Debug Mode

> Source: https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/debug-mode/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-python/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-python/intelligence/channels)

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

[Common Copilot Issues](https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/common-issues)[Error message reference](https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/error-reference)[Error Debugging & Observability](https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/error-debugging)[Inspector and dev console](https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/inspector-dev-console)[Debug Mode](https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/debug-mode)[AG-UI Event Inspector](https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/event-inspector)[Hook Explorer](https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/hook-explorer)

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Debug Mode

OtherTroubleshooting

# Debug Mode

Enable debug mode to get detailed logging of the AG-UI event pipeline on both the server and client.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

# Debug Mode

When your agent isn't behaving as expected — events are missing, state isn't updating, or tool calls aren't executing — you need visibility into the event pipeline. Runtime debug mode provides structured server-side logging; the frontend can inspect the resulting stream with browser network tools or the AG-UI Event Inspector.

Enable it to see:

  * What events your agent is emitting and whether they reach the client
  * Where in the pipeline events are being dropped or failing validation
  * The full lifecycle of a request from start to finish



For visual error display during local development (error banners, dev console), see [Error Debugging](https://docs.copilotkit.ai/claude-sdk-python/troubleshooting/error-debugging). Debug mode focuses on event pipeline logging rather than UI-level error display.

## Enabling Debug Mode#

### Server-Side (Runtime)#

Pass `debug: true` to the `CopilotRuntime` constructor:

app/api/copilotkit/route.ts
    
    
    const runtime = new CopilotRuntime({
      agents: {
        // your agents
      },
      debug: true, 
    });

This produces structured Pino logs (formatted by `pino-pretty`) with a `copilotkit-debug` component label:
    
    
    [14:32:01.123] DEBUG (copilotkit-debug): Agent run started
        agentName: "default"
        threadId: "abc-123"
    [14:32:01.130] DEBUG (copilotkit-debug): SSE stream opened
    [14:32:01.145] DEBUG (copilotkit-debug): Event emitted
        type: "TEXT_MESSAGE_START"
        messageId: "msg-1"
        role: "assistant"
    [14:32:01.200] DEBUG (copilotkit-debug): Event emitted
        type: "TEXT_MESSAGE_CONTENT"
        deltaLength: 42
    [14:32:01.250] DEBUG (copilotkit-debug): Event emitted
        type: "TEXT_MESSAGE_END"
    [14:32:01.260] DEBUG (copilotkit-debug): Event emitted
        type: "RUN_FINISHED"
    [14:32:01.261] DEBUG (copilotkit-debug): SSE stream completed
        eventCount: 4
        loggedEventCount: 4

### Client-Side#

Pass `debug={true}` to the `<CopilotKit>` provider:
    
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      debug={true} 
    >
      <YourApp />
    </CopilotKit>

This forwards the debug configuration to the AG-UI client transport layer (`transformChunks`), which may produce transport-level debug output depending on the AG-UI library version. Note that the richest debug logging comes from the **server-side** `CopilotRuntime` — enable `debug: true` there for full structured Pino logs of every AG-UI event.

The server and client debug toggles are independent. Enabling debug on the client does not affect the server, and vice versa.

## Granular Configuration#

On `CopilotRuntime`, pass an object instead of `true` for fine-grained control over what gets logged:
    
    
    debug: {
      events: true,     // Log every event emitted/received
      lifecycle: true,  // Log request/run lifecycle (start, finish, error)
      verbose: false,   // Log full payloads instead of summaries
    }

### Defaults#

Input| `events`| `lifecycle`| `verbose`  
---|---|---|---  
`debug: true`| `true`| `true`| `false`  
`debug: {}`| `true`| `true`| `false`  
`debug: { events: false }`| `false`| `true`| `false`  
  
When `debug` is a boolean (`true`), events and lifecycle logging are enabled but verbose mode is **off** by default (to avoid leaking PII in logs). To get full event payloads, explicitly opt in with `debug: { verbose: true }`.

### Examples#

Log only lifecycle events (no per-event logs):
    
    
    debug: { events: false, lifecycle: true }

Log events with full payloads but skip lifecycle:
    
    
    debug: { events: true, lifecycle: false, verbose: true }

## Troubleshooting with Debug Mode#

### Events Not Reaching the Client#

Enable debug on the server side for the most detailed visibility:

  1. Check server logs for `Event emitted` — are the expected events being sent?
  2. Verify `SSE stream completed` shows the expected `eventCount`.
  3. Use the browser Network tab to confirm SSE events are arriving over the wire.



### Tool Calls Not Executing#

Enable server-side debug and look for:

  1. `TOOL_CALL_START` events being emitted on the server
  2. `TOOL_CALL_ARGS` and `TOOL_CALL_END` events following correctly
  3. Confirm the events appear in the SSE stream via the browser Network tab



### State Not Updating#

Look for `STATE_SNAPSHOT` or `STATE_DELTA` events in server logs. If they appear on the server but not in the browser's SSE stream, there may be a connection issue.

## What Gets Logged#

### Server-Side Logs#

Category| Log Message| Description  
---|---|---  
Lifecycle| `Agent run started`| An agent run was initiated, includes agent name and thread ID  
Lifecycle| `SSE stream opened`| The SSE response stream was created  
Lifecycle| `SSE stream completed`| The stream finished, includes total event count  
Lifecycle| `SSE stream errored`| The stream encountered an error  
Events| `Event emitted`| Each AG-UI event as it's written to the stream  
  
In **summary mode** (verbose off), event logs include key identifiers like `messageId`, `toolCallId`, `toolCallName`, `role`, and content lengths instead of full payloads.

### Client-Side#

On the client, the `debug` configuration is passed through to the AG-UI transport layer. The AG-UI client library controls what (if any) debug output is produced. CopilotKit itself does not emit `console.debug` calls — the debug flag configures the underlying AG-UI event pipeline.

Debug mode can produce a large volume of log output, especially in verbose mode. Use it during development and debugging, not in production.

### On this page

Enabling Debug ModeServer-Side (Runtime)Client-SideGranular ConfigurationDefaultsExamplesTroubleshooting with Debug ModeEvents Not Reaching the ClientTool Calls Not ExecutingState Not UpdatingWhat Gets LoggedServer-Side LogsClient-Side
