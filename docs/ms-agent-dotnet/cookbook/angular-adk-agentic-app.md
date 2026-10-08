---
url: https://docs.copilotkit.ai/ms-agent-dotnet/cookbook/angular-adk-agentic-app/
title: Angular + Google ADK
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:18:07.176932+00:00
---

# Angular + Google ADK

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/cookbook/angular-adk-agentic-app/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-dotnet/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (.NET)](https://docs.copilotkit.ai/ms-agent-dotnet)[Cookbook](https://docs.copilotkit.ai/ms-agent-dotnet/cookbook)

# Angular + Google ADK

Connect an Angular frontend to a Google ADK agent over AG-UI, then add request identity, server-side policy, threads, and memory.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This recipe assembles a production agentic app from three pieces: an **Angular** frontend built with [`@copilotkit/angular`](https://docs.copilotkit.ai/ms-agent-dotnet/angular), a **Google ADK** agent served over the open [AG-UI](https://docs.ag-ui.com/) protocol, and an optional [CopilotKit Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview) layer for persistent threads and cross-session memory.

Start with these two quickstarts:

  * [Angular frontend](https://docs.copilotkit.ai/ms-agent-dotnet/angular) gets you a working Angular app with a chat UI backed by a local Copilot Runtime.
  * [ADK quickstart](https://docs.copilotkit.ai/integrations/adk/quickstart) serves an ADK agent over AG-UI.



This recipe covers production concerns that arise after the two quickstarts are connected: shared chat state, request identity, model choice, server-side policy, threads, and memory.

## How the pieces fit#

The app has three processes:

  1. The **Angular client** renders chat and generative UI and runs the agent.
  2. A **runtime / backend-for-frontend (BFF)** wires the Copilot Runtime, resolves the per-request user, enforces tool policy, proxies memory, and forwards each run to your agent. This layer handles identity, policy, and memory access.
  3. The **Google ADK agent** does the reasoning and emits generative UI. An optional deterministic specialist agent handles fixed payloads.



Validate identity and policy in the BFF

Treat data from the browser as untrusted. Resolve the authenticated user, enforce tool policy, and scope memory requests on the server.

## Share agent state across the chat surface#

Calls to `injectAgentStore("default")` resolve the same underlying agent. Components that use the same agent id observe the same messages and run state.

chat.component.ts
    
    
    import { Component } from "@angular/core";
    import { CopilotChat, injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-chat",
      imports: [CopilotChat],
      template: `<copilot-chat agentId="default" />`,
      // Give the surface a bounded height to keep the composer visible on long threads.
      styles: [`:host { display: block; height: 100%; min-height: 0; }`],
    })
    export class ChatComponent {
      readonly agentStore = injectAgentStore("default");
    }

Use one owner for custom submission logic

A second composer may inject the same agent id and will observe the same agent. For consistent validation, attachments, and message submission, pass one submit function or service to each custom composer.

Do not fetch history for a brand-new thread

**Symptom:** starting a new conversation throws before the first message. **Cause:** a fresh thread id has no messages, so the history request errors. **Fix:** only fetch history for an existing, user-selected thread. Run new conversations on a fresh id, and reload stored messages only when the bound thread id changes.

Change runtime configuration between runs

The runtime URL and request headers take part in agent resolution. Apply configuration changes before a run starts. Put non-secret values that change on each request in the run body instead.

## Send changing context with each run#

Do not use browser context as authorization

A user id sent by the browser is untrusted. Resolve the authenticated user on the server. Use run context only to give the agent current, non-secret application state, and validate any identity value against the server session before using it to scope data.

Use [`connectAgentContext`](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext) to send current, non-secret application state with each run:

chat.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { connectAgentContext } from "@copilotkit/angular";
    
    @Component({ /* ... */ })
    export class ChatComponent {
      readonly userId = signal(currentUserId);
    
      constructor() {
        // Re-registers reactively when the signal changes (e.g. an in-session user switch).
        connectAgentContext(() => ({ description: "userId", value: this.userId() }));
      }
    }

Do not use this browser value as proof of identity. The BFF must compare it with the authenticated session or replace it with the server identity. If an ADK tool needs the validated user id, map that value into ADK session state in the BFF or agent adapter. The tool can then read the application-defined state key:

agent/main.py
    
    
    def _user_id(tool_context) -> str | None:
        return tool_context.state.get("user_id")
    
    def recall_for_user(tool_context) -> dict:
        user_id = _user_id(tool_context)
        # ...scope every read and write to user_id
        return {"ok": True}

The exact mapping belongs to your server bridge. Keep it explicit and test it with the version of the ADK adapter you deploy.

## Choose a capable model#

ADK uses Google's Gemini by default and also supports other models. See the [ADK quickstart](https://docs.copilotkit.ai/integrations/adk/quickstart) for configuration.

  * Prefer a current model with reliable instruction following and tool use.
  * Test older or smaller models against your full tool and policy flow. They may skip steps in multi-part instructions.
  * Use a reasoning model when the task needs it, and account for its added latency and cost.



Check model access with your provider

Confirm a model id actually exists for your account before wiring it in. On Gemini, for example:
    
    
    curl "https://generativelanguage.googleapis.com/v1beta/models?key=$GOOGLE_API_KEY" | grep '"name"'

Two more agent-side habits:

  * **Keep MCP and tool timeouts short.** A long timeout lets a slow external tool server delay the first reply. A shorter timeout reports the failure sooner.
  * **Emit fixed generated-UI payloads from code.** A model may change JSON even when asked to return it unchanged.



## Enforce governance on the server#

A client-side tool guard is presentation only

**Symptom:** a tool you "hid" in the UI still gets called by the agent. **Cause:** the browser is untrusted, and hiding a tool in the UI does nothing to the agent's tool list. **Fix:** on the BFF, strip disallowed tools from the inbound run body so the model cannot call them, and filter the outbound generative-UI stream. Emit a single governance receipt rather than silently dropping output.

  * **Include the per-request allow-list in the run body.** A capability change then takes effect on the next run.
  * **Normalize capability-name casing** (for example `pieChart` versus `PieChart`) in both the inbound and outbound checks. A casing mismatch can bypass a policy check.
  * **Let generative-UI cards reflow, do not truncate.** Long dynamic labels overflow fixed-size cards. Let the layout grow rather than clipping content.



## Add persistent threads and memory (optional)#

[CopilotKit Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview) adds persistent [threads](https://docs.copilotkit.ai/ms-agent-dotnet/threads) and durable cross-session memory. Handle a missing or unreachable platform without failing every request:

  * **Auto-detect:** at startup, probe the platform health endpoint with a short timeout. If it is unreachable or unlicensed, fall back to an in-memory runner.
  * **Configurable endpoint:** use one base-URL environment variable for the runtime, the agent's memory client, and the health probe. Check the endpoint again after a restart.



Memory tools call the platform's streaming JSON-RPC `/mcp` endpoint, scoped per user:
    
    
    POST {INTELLIGENCE_API_URL}/mcp
    Authorization: Bearer <key>
    X-Cpki-User-Id: <user_id>
    Accept: application/json, text/event-stream
    
    {"jsonrpc":"2.0","id":1,"method":"tools/call",
     "params":{"name":"recall_memory","arguments":{}}}

The response is a server-sent event stream. Read the JSON-RPC body from the first `data:` line and join the text content. Writes may include an embedding step and can take several seconds, so run them asynchronously and set a suitable timeout.

Query each supported memory scope

**Symptom:** the agent clearly remembers things a custom memory panel never shows. **Cause:** recall often defaults to _user_ scope and caps at a small top-N, so a panel that hard-codes user scope hides project- or team-scoped memories. **Fix:** if you build a memory browser, query both user and project scopes, de-duplicate, and merge.

Self-hosting the platform

Running CopilotKit Intelligence yourself has its own setup notes (license verification and the embedding service). See [Self-hosting](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/self-hosting).

## Production checklist#

  1. Use one agent id across the chat surface. Share one submit function or service across custom composers.
  2. Resolve identity on the server. Send changing, non-secret application context with each run.
  3. Apply runtime URL and header changes between runs.
  4. Enforce tool policy on the server. Strip disallowed tools from inbound runs and filter outbound generated UI.
  5. Test a current agentic model against your full tool and policy flow, and confirm that your provider offers it.



## Going further#

  * **Local dev:** only your frontend dev server hot-reloads. A `tsx`/`node` BFF and a Python agent do not, so restart them after edits. Give each service a stable, non-colliding port and write them down.
  * **Custom chat UI:** Build welcome and empty states in your application, customize message rendering through `messageViewComponent`, and iterate the full message list when you need to interleave generated UI. See the [Angular guide](https://docs.copilotkit.ai/ms-agent-dotnet/angular).
  * **Threads in depth:** see [Threads explained](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/threads-explained).



## Get started with a coding agent#

Paste this into your coding agent (Cursor, Claude Code, etc.) once you have the Angular and ADK quickstarts running:
    
    
    Update my Angular + Google ADK + CopilotKit app for multi-user production:
    
    1. Use one agent id across the chat surface. Calls to `injectAgentStore("default")` resolve the
       same agent. Route custom composers through one shared submit function or service.
    2. Resolve the authenticated user on the BFF. If ADK tools need that id, map the server-validated
       value into an application-defined ADK session-state key. Do not trust browser context alone.
    3. Apply runtime config changes (runtimeUrl/headers) between runs. Carry changing, non-secret
       application context in the run body.
    4. Enforce tool policy on the server: strip disallowed tools from the inbound run body and filter the
       outbound generative-UI stream. Include the allow-list in the run body, and normalize tool-name casing.
    5. Give the chat surface a bounded height, and only fetch thread history for an existing thread id.
    
    Keep my existing Angular and ADK setup otherwise unchanged.

### On this page

How the pieces fitShare agent state across the chat surfaceSend changing context with each runChoose a capable modelEnforce governance on the serverAdd persistent threads and memory (optional)Production checklistGoing furtherGet started with a coding agent
