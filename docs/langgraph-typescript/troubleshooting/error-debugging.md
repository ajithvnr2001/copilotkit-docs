---
url: https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/error-debugging/
title: Error Debugging & Observability
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:12:16.311411+00:00
---

# Error Debugging & Observability

> Source: https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/error-debugging/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

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

[Common Copilot Issues](https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/common-issues)[Error message reference](https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/error-reference)[Error Debugging & Observability](https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/error-debugging)[Inspector and dev console](https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/inspector-dev-console)[Debug Mode](https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/debug-mode)[AG-UI Event Inspector](https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/event-inspector)[Hook Explorer](https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/hook-explorer)

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Error Debugging & Observability

OtherTroubleshooting

# Error Debugging & Observability

Surface errors visually in development, and wire programmatic error handlers for Sentry / Datadog / your analytics pipeline in production.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

# How to debug errors

CopilotKit provides a visual error console for local development and a programmatic `onError` callback for production observability. The visual console is completely free and requires no API keys.

## Quick setup#
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    export default function App() {
      return (
        <CopilotKit
          runtimeUrl="/api/copilotkit"
          showDevConsole={true} 
        >
          {/* your app */}
        </CopilotKit>
      );
    }

Avoid showing the dev console in production — it exposes internal error details to end users.

## When to use development debugging#

  * **Local development** — errors appear immediately in your UI
  * **Quick debugging** — no setup required, works out of the box
  * **Testing** — verify error handling during development



## Programmatic error handling#

The v2 API provides an `onError` callback on both `CopilotKit` and `CopilotChat`. No `publicApiKey` is required.

### Provider-level error handling#

Catches every error across the entire application:
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      onError={(event) => {
        // event.code    — error type (e.g. "runtime_info_fetch_failed", "agent_run_failed")
        // event.error   — the Error object
        // event.context — additional context (agentId, toolName, etc.)
        console.error(`[CopilotKit ${event.code}]`, event.error.message);
        errorTracker.capture(event);
      }}
    >
      <App />
    </CopilotKit>;

### Chat-level error handling#

Scoped to a specific chat's agent — fires **in addition to** the provider-level handler:
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    <CopilotChat
      agentId="my-agent"
      onError={(event) => {
        showToast(`Agent error: ${event.error.message}`);
      }}
    />;

### Error codes#

Code| Description  
---|---  
`runtime_info_fetch_failed`| Could not reach the runtime's `/info` endpoint  
`agent_connect_failed`| Agent connection (thread setup) failed  
`agent_run_failed`| Agent run rejected (e.g. network error)  
`agent_run_failed_event`| The agent's `onRunFailed` subscriber fired  
`agent_run_error_event`| Agent emitted a `RUN_ERROR` event  
`tool_argument_parse_failed`| Tool call arguments were not valid JSON  
`tool_handler_failed`| A frontend tool handler threw  
  
Need to see the full event pipeline: what events your agent emits, whether they reach the client, and where they are dropped? Open the [Inspector](https://docs.copilotkit.ai/langgraph-typescript/troubleshooting/inspector). The launcher turns red, and where there is room a pill names the failure. Click the launcher to land on the pane that shows the agent, the tool if one failed, and the error.

## Troubleshooting#

### Dev console not showing#

  * Confirm `showDevConsole={true}`
  * Check for JavaScript errors in the browser console
  * Ensure no CSS is hiding the error banner



### Production error pipeline checklist#

  * Provider-level `onError` is wired and forwards to your error tracker
  * `showDevConsole` is **false** in production builds
  * Agent IDs in errors match the agents registered on your runtime
  * Critical error codes (`agent_run_failed`, `tool_handler_failed`) are alerted on, not just logged



### On this page

Quick setupWhen to use development debuggingProgrammatic error handlingProvider-level error handlingChat-level error handlingError codesTroubleshootingDev console not showingProduction error pipeline checklist
