---
url: https://docs.copilotkit.ai/agno/troubleshooting/error-debugging/
title: Error Debugging & Observability
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:47:53.626077+00:00
---

# Error Debugging & Observability

> Source: https://docs.copilotkit.ai/agno/troubleshooting/error-debugging/

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

[Migrate to V2](https://docs.copilotkit.ai/agno/troubleshooting/migrate-to-v2)[Error Debugging & Observability](https://docs.copilotkit.ai/agno/troubleshooting/error-debugging)[Common Copilot Issues](https://docs.copilotkit.ai/agno/troubleshooting/common-issues)[Migrate to 1.10.X](https://docs.copilotkit.ai/agno/troubleshooting/migrate-to-1.10.X)[Migrate to 1.8.2](https://docs.copilotkit.ai/agno/troubleshooting/migrate-to-1.8.2)

[Open-source telemetry](https://docs.copilotkit.ai/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/agno/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Error Debugging & Observability

OtherTroubleshooting

# Error Debugging & Observability

Learn how to debug errors in CopilotKit with dev console and set up error observability for monitoring services.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

# How to Debug Errors

CopilotKit provides visual error display for local development and debugging. This feature is completely free and requires no API keys.

## Quick Setup#
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    export default function App() {
      return (
        <CopilotKit
          runtimeUrl="<your-runtime-url>"
          showDevConsole={true} 
        >
          {/* Your app */}
        </CopilotKit>
      );
    }

Avoid showing the dev console in production as it exposes internal error details to end users.

## When to Use Development Debugging#

  * **Local development** \- See errors immediately in your UI
  * **Quick debugging** \- No setup required, works out of the box
  * **Testing** \- Verify error handling during development



## Programmatic Error Handling (v2)#

The v2 API provides an `onError` callback on both `CopilotKit` and `CopilotChat` for programmatic error handling. No `publicApiKey` is required.

### Provider-Level Error Handling#

Catches all errors across the entire application:
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      onError={(event) => {
        // event.code — error type (e.g. "runtime_info_fetch_failed", "agent_run_failed")
        // event.error — the Error object
        // event.context — additional context (agentId, toolName, etc.)
        console.error(`[CopilotKit ${event.code}]`, event.error.message);
        errorTracker.capture(event);
      }}
    >
      <App />
    </CopilotKit>

### Chat-Level Error Handling#

Scoped to a specific chat's agent — fires in addition to the provider-level handler:
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    <CopilotChat
      agentId="my-agent"
      onError={(event) => {
        showToast(`Agent error: ${event.error.message}`);
      }}
    />

### Error Codes#

Code| Description  
---|---  
`runtime_info_fetch_failed`| Could not reach the runtime `/info` endpoint  
`agent_connect_failed`| Agent connection (thread setup) failed  
`agent_run_failed`| Agent run rejected (e.g. network error)  
`agent_run_failed_event`| Agent's `onRunFailed` subscriber fired  
`agent_run_error_event`| Agent sent a `RUN_ERROR` event  
`tool_argument_parse_failed`| Tool call arguments were not valid JSON  
`tool_handler_failed`| A frontend tool handler threw an error  
  
Need to see the raw AG-UI events flowing between runtime and client? Use the [AG-UI Event Inspector](https://docs.copilotkit.ai/agno/troubleshooting/event-inspector) in VS Code for a live, filterable event stream.

Need to see the full event pipeline — what events your agent emits, whether they reach the client, and where they're dropped? See [Debug Mode](https://docs.copilotkit.ai/agno/troubleshooting/debug-mode) for detailed AG-UI event logging.

## Troubleshooting#

### Development Debugging Issues#

  * **Dev console not showing:**
    * Confirm `showDevConsole={true}`
    * Check for JavaScript errors in the browser console
    * Ensure no CSS is hiding the error banner



### On this page

Quick SetupWhen to Use Development DebuggingProgrammatic Error Handling (v2)Provider-Level Error HandlingChat-Level Error HandlingError CodesTroubleshootingDevelopment Debugging Issues
