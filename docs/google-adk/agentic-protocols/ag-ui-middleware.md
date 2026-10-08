---
url: https://docs.copilotkit.ai/google-adk/agentic-protocols/ag-ui-middleware/
title: AG-UI Middleware
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:02:22.275762+00:00
---

# AG-UI Middleware

> Source: https://docs.copilotkit.ai/google-adk/agentic-protocols/ag-ui-middleware/

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

[Architecture](https://docs.copilotkit.ai/google-adk/concepts/architecture)[Generative UI](https://docs.copilotkit.ai/google-adk/concepts/generative-ui-overview)[Which Hook for Which Job](https://docs.copilotkit.ai/google-adk/concepts/which-hook)[Open source vs Intelligence](https://docs.copilotkit.ai/google-adk/concepts/oss-vs-enterprise)

[Agentic Protocols](https://docs.copilotkit.ai/google-adk/agentic-protocols)

[AG-UI](https://docs.copilotkit.ai/google-adk/agentic-protocols/ag-ui)[AG-UI Middleware](https://docs.copilotkit.ai/google-adk/agentic-protocols/ag-ui-middleware)[MCP](https://docs.copilotkit.ai/google-adk/agentic-protocols/mcp)[A2A](https://docs.copilotkit.ai/google-adk/agentic-protocols/a2a)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

LearnConceptsAgentic Protocols

# AG-UI Middleware

Configure AG-UI middleware for your CopilotKit application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

> AG-UI middleware is fundamentally an [AG-UI protocol](https://docs.copilotkit.ai/google-adk/agentic-protocols/ag-ui-middleware/ag-ui) concept defined upstream in `@ag-ui/client`. This page covers how to wire it into a CopilotKit runtime; for the protocol-level reference (lifecycle, `runNextWithState`, the `Middleware` base class), see the upstream guide at [docs.ag-ui.com/sdk/js/client/middleware](https://docs.ag-ui.com/sdk/js/client/middleware).

AG-UI agents expose a middleware layer via `agent.use(middleware)`, a powerful hook for logging, guardrails, request transformation, and event rewriting. Because CopilotKit runs the middleware server-side inside the [Copilot Runtime](https://docs.copilotkit.ai/google-adk/backend/copilot-runtime), it executes in a trusted environment where the client cannot tamper with it.

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

  * **`a2ui`** — apply `A2UIMiddleware` to all (or a subset of) registered agents. See [Copilot Runtime → A2UI](https://docs.copilotkit.ai/google-adk/backend/copilot-runtime#a2ui).
  * **`mcpApps`** — configure MCP servers for all agents from a single place. See [Copilot Runtime → mcpApps](https://docs.copilotkit.ai/google-adk/backend/copilot-runtime#mcpapps).



## Related#

  * [Copilot Runtime](https://docs.copilotkit.ai/google-adk/backend/copilot-runtime) — the server-side layer that executes middleware.
  * [AG-UI Protocol](https://docs.copilotkit.ai/google-adk/backend/ag-ui) — the event stream the middleware operates on.


