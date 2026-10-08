---
url: https://docs.copilotkit.ai/angular/agentic-protocols/ag-ui-middleware/
title: AG-UI Middleware
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:15.896433+00:00
---

# AG-UI Middleware

> Source: https://docs.copilotkit.ai/angular/agentic-protocols/ag-ui-middleware/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

[Architecture](https://docs.copilotkit.ai/angular/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/angular/concepts/generative-ui-overview)[Open source vs Intelligence](https://docs.copilotkit.ai/angular/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/angular/agentic-protocols)

[AG-UI](https://docs.copilotkit.ai/angular/agentic-protocols/ag-ui)[AG-UI Middleware](https://docs.copilotkit.ai/angular/agentic-protocols/ag-ui-middleware)[A2A](https://docs.copilotkit.ai/angular/agentic-protocols/a2a)

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

LearnConceptsAgentic Protocols

# AG-UI Middleware

Configure AG-UI middleware for your CopilotKit application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

> AG-UI middleware is fundamentally an [AG-UI protocol](https://docs.copilotkit.ai/angular/agentic-protocols/ag-ui-middleware/ag-ui) concept defined upstream in `@ag-ui/client`. This page covers how to wire it into a CopilotKit runtime; for the protocol-level reference (lifecycle, `runNextWithState`, the `Middleware` base class), see the upstream guide at [docs.ag-ui.com/sdk/js/client/middleware](https://docs.ag-ui.com/sdk/js/client/middleware).

AG-UI agents expose a middleware layer via `agent.use(middleware)`, a powerful hook for logging, guardrails, request transformation, and event rewriting. Because CopilotKit runs the middleware server-side inside the [Copilot Runtime](https://docs.copilotkit.ai/angular/backend/copilot-runtime), it executes in a trusted environment where the client cannot tamper with it.

## Defining a Middleware#

A middleware extends the `Middleware` base class from `@ag-ui/client` and implements `run(input, next)`. It receives the incoming `RunAgentInput` and returns an `Observable<BaseEvent>`, typically by subscribing to `runNextWithState(input, next)` and transforming the stream:

my-middleware.ts
    
    
    import {
      Middleware,
      RunAgentInput,
      AbstractAgent,
      BaseEvent,
    } from "@ag-ui/client";
    import { Observable } from "rxjs";
    
    export class LoggingMiddleware extends Middleware {
      run(input: RunAgentInput, next: AbstractAgent): Observable<BaseEvent> {
        return new Observable<BaseEvent>((subscriber) => {
          const sub = this.runNextWithState(input, next).subscribe({
            next: ({ event }) => {
              console.log("[agent event]", event.type);
              subscriber.next(event);
            },
            error: (err) => subscriber.error(err),
            complete: () => subscriber.complete(),
          });
          return () => sub.unsubscribe();
        });
      }
    }

## Attaching Middleware to an Agent#

Call `.use(...)` on the agent before registering it with the runtime:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { CopilotRuntime, InMemoryAgentRunner } from "@copilotkit/runtime/v2";
    import { LangGraphAgent } from "@copilotkit/runtime/langgraph";
    import { LoggingMiddleware } from "./my-middleware";
    
    const agent = new LangGraphAgent({
      deploymentUrl: process.env.LANGGRAPH_DEPLOYMENT_URL!,
      graphId: "sample_agent",
    });
    agent.use(new LoggingMiddleware());
    
    const runtime = new CopilotRuntime({
      agents: { default: agent },
      runner: new InMemoryAgentRunner(),
    });

## Built-in Middleware#

The runtime ships first-class middleware options you can enable directly on `CopilotRuntime` without calling `.use()` on each agent:

  * **`a2ui`** — apply `A2UIMiddleware` to all (or a subset of) registered agents. See [Copilot Runtime → A2UI](https://docs.copilotkit.ai/angular/backend/copilot-runtime#a2ui).
  * **`mcpApps`** — configure MCP servers for all agents from a single place. See [Copilot Runtime → mcpApps](https://docs.copilotkit.ai/angular/backend/copilot-runtime#mcpapps).



## Related#

  * [Copilot Runtime](https://docs.copilotkit.ai/angular/backend/copilot-runtime) — the server-side layer that executes middleware.
  * [AG-UI Protocol](https://docs.copilotkit.ai/angular/backend/ag-ui) — the event stream the middleware operates on.


