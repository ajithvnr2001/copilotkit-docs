---
url: https://docs.copilotkit.ai/angular/ag2/ag-ui/
title: AG-UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:15.992702+00:00
---

# AG-UI

> Source: https://docs.copilotkit.ai/angular/ag2/ag-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/ag2)[Quickstart](https://docs.copilotkit.ai/angular/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/ag2/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/angular/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/ag2/learning)

[User Memories](https://docs.copilotkit.ai/angular/ag2/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/ag2/intelligence/channels)

Hosting

Backend

Runtime

Runtime

[Copilot Runtime](https://docs.copilotkit.ai/angular/ag2/copilot-runtime)[AG-UI](https://docs.copilotkit.ai/angular/ag2/ag-ui)

Debugging

Debugging

Learn

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

AG-UI

BackendRuntimeRuntime

# AG-UI

The AG-UI protocol connects your frontend to your AI agents via event-based Server-Sent Events (SSE).

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

On the AG2 side, `AGUIStream` (from the `ag2.ag_ui` module, AG2 1.1.2+) exposes any agent as an AG-UI endpoint that CopilotKit consumes directly — see the [quickstart](https://docs.copilotkit.ai/angular/ag2/quickstart) and the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

AG2 1.1.2+ also describes the agent in a **capabilities** document (`stream.capabilities()`), which `stream.build_asgi()` serves on a `GET` to the same endpoint. It holds the agent's identity, whether it accepts client-provided tools and state snapshots, its named sub-agents, and whether it supports interrupts. It is read off the agent before any run starts. A group AG2 cannot vouch for is omitted, which AG-UI reads as "says nothing", not "unsupported". See the [AG2 capabilities reference](https://docs.ag2.ai/docs/user-guide/ag-ui/overview#capabilities).

A hand-written `@app.post("/chat")` route serves no `GET`, so a request to it returns 405. Add a route that returns the document:

agent.py
    
    
    @app.get("/chat")
    async def capabilities() -> JSONResponse:
        # The same serialization `build_asgi()` uses: camelCase keys, unset groups left out.
        return JSONResponse(stream.capabilities().model_dump(by_alias=True, exclude_none=True))

`JSONResponse` comes from `fastapi.responses`.

CopilotKit is built on the [AG-UI protocol](https://ag-ui.com), a lightweight, event-based standard that defines how AI agents communicate with user-facing applications over Server-Sent Events (SSE).

Messages, state updates, tool calls, and agent lifecycle events all flow through AG-UI. Understanding this layer helps you debug and extend any CopilotKit integration.

## Accessing your agent with `injectAgentStore`#

`injectAgentStore` exposes the AG-UI agent and projects its messages, state, and run status into Angular signals:

src/app/agent-status.component.ts
    
    
    import { Component, computed } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    @Component({
      selector: "app-agent-status",
      template: `
        <p>{{ messageCount() }} messages</p>
        @if (store().isRunning()) {
          <p>Agent is running…</p>
        }
      `,
    })
    export class AgentStatusComponent {
      readonly store = injectAgentStore("research-agent");
      readonly messageCount = computed(() => this.store().messages().length);
    }

The resolved agent is a standard AG-UI `AbstractAgent`. You can read its state, invoke protocol methods, and subscribe to its event stream.

### Subscribing to AG-UI events#

Subscribe to `store().agent` and release the subscription with the owning injector:
    
    
    private readonly destroyRef = inject(DestroyRef);
    readonly store = injectAgentStore("research-agent");
    
    constructor() {
      const subscription = this.store().agent.subscribe({
        onTextMessageContentEvent({ textMessageBuffer }) {
          console.log("Streaming text:", textMessageBuffer);
        },
        onToolCallEndEvent({ toolCallName, toolCallArgs }) {
          console.log("Tool called:", toolCallName, toolCallArgs);
        },
        onStateChanged({ agent }) {
          console.log("State changed:", agent.state);
        },
      });
      this.destroyRef.onDestroy(() => subscription.unsubscribe());
    }

The callback names map directly to the [AG-UI event types](https://docs.ag-ui.com/concepts/events):

Event| Callback  
---|---  
Run lifecycle| `onRunStartedEvent`, `onRunFinishedEvent`, `onRunErrorEvent`  
Steps| `onStepStartedEvent`, `onStepFinishedEvent`  
Text messages| `onTextMessageStartEvent`, `onTextMessageContentEvent`, `onTextMessageEndEvent`  
Tool calls| `onToolCallStartEvent`, `onToolCallArgsEvent`, `onToolCallEndEvent`, `onToolCallResultEvent`  
State| `onStateSnapshotEvent`, `onStateDeltaEvent`  
Messages| `onMessagesSnapshotEvent`  
Custom| `onCustomEvent`, `onRawEvent`  
High-level changes| `onMessagesChanged`, `onStateChanged`  
  
## The proxy pattern#

When you use CopilotKit with a runtime, your frontend does not talk directly to the backend agent. CopilotKit discovers agents through the runtime's `/info` endpoint and represents each one with a proxy that implements the same `AbstractAgent` interface.

What your component sees
    
    
    const store = injectAgentStore("default");
    const agent = store().agent;
    store().messages();
    store().state();
    agent.subscribe({ /* … */ });

What happens underneath
    
    
    // injectAgentStore() → registry checks /info → resolves a proxy agent
    // core.runAgent({ agent }) → runtime POST → agent execution → SSE events

This indirection lets the runtime provide authentication, middleware, agent routing, and CopilotKit Intelligence without changing how the frontend interacts with agents.

## How agents slot into the runtime#

On the server, `CopilotRuntime` accepts a map of AG-UI `AbstractAgent` instances. A framework adapter, an `HttpAgent` pointing at a remote server, and a custom implementation all use the same request path:

  1. The runtime resolves the target agent by ID.
  2. It clones the agent for request isolation and supplies messages, state, and thread context.
  3. `AgentRunner` executes the agent and receives AG-UI events.
  4. The runtime encodes those events as SSE and streams them to the frontend proxy.



The backend framework can change without forcing a corresponding change to the frontend AG-UI contract.

To write the custom implementation yourself, and keep its own fields through the clone in step 2, see [Write your own AG-UI agent](https://docs.copilotkit.ai/angular/ag2/backend/custom-ag-ui-agent).

### On this page

Accessing your agent with injectAgentStoreSubscribing to AG-UI eventsThe proxy patternHow agents slot into the runtime
