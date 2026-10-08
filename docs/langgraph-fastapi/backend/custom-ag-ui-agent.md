---
url: https://docs.copilotkit.ai/langgraph-fastapi/backend/custom-ag-ui-agent/
title: Write your own AG-UI agent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:04:25.132662+00:00
---

# Write your own AG-UI agent

> Source: https://docs.copilotkit.ai/langgraph-fastapi/backend/custom-ag-ui-agent/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-fastapi/webmcp)

Agent capabilities

LangGraph (FastAPI)

[Sub-agents](https://docs.copilotkit.ai/langgraph-fastapi/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-fastapi/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/channels)

Hosting

Backend

Runtime

[Copilot Runtime](https://docs.copilotkit.ai/langgraph-fastapi/backend/copilot-runtime)[Runtime HTTP endpoints](https://docs.copilotkit.ai/langgraph-fastapi/backend/runtime-endpoints)[Use any model router](https://docs.copilotkit.ai/langgraph-fastapi/backend/custom-agent)[Write your own AG-UI agent](https://docs.copilotkit.ai/langgraph-fastapi/backend/custom-ag-ui-agent)[AgentRunner and persistence](https://docs.copilotkit.ai/langgraph-fastapi/backend/agent-runner)[Message history](https://docs.copilotkit.ai/langgraph-fastapi/backend/message-history)[Self-managed agents](https://docs.copilotkit.ai/langgraph-fastapi/backend/self-managed-agents)[Connect AG-UI agents](https://docs.copilotkit.ai/langgraph-fastapi/backend/ag-ui)[Deploy to any runtime](https://docs.copilotkit.ai/langgraph-fastapi/runtime-server-adapter)[Authentication](https://docs.copilotkit.ai/langgraph-fastapi/auth)

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-fastapi/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-fastapi/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Write your own AG-UI agent

BackendRuntime

# Write your own AG-UI agent

Extend AG-UI's AbstractAgent, register it in the Copilot Runtime, and keep its fields across the runtime's per-request clone.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The Copilot Runtime's `agents` map takes AG-UI `AbstractAgent` instances. The framework adapters and `HttpAgent` are subclasses of it, and you can write your own. Use this when your agent logic lives in the same process as the runtime and is not built on a framework that CopilotKit already integrates with.

If you only want to call a model with your own code, [`BuiltInAgent` factory mode](https://docs.copilotkit.ai/langgraph-fastapi/backend/custom-agent) is shorter: it emits the run lifecycle events for you. If your agent is a separate service that already speaks AG-UI over HTTP, use `HttpAgent` instead.

## Install#
    
    
    npm install @copilotkit/runtime @ag-ui/client@1.0.2 rxjs

Your `@ag-ui/client` must be the version your `@copilotkit/runtime` depends on, so the app has one copy of it. Run `npm ls @ag-ui/client`: it should show a single, deduped version. If it shows two, reinstall `@ag-ui/client` at the version listed under `@copilotkit/runtime`.

## A minimal agent#

A subclass implements `run`. It receives the AG-UI `RunAgentInput` (messages, tools, context, state, `threadId`, `runId`) and returns an RxJS `Observable` of AG-UI events. Start with `RUN_STARTED`, end with `RUN_FINISHED`, and stream the reply in between:

lib/echo-agent.ts
    
    
    import {
      AbstractAgent,
      EventType,
      type BaseEvent,
      type RunAgentInput,
    } from "@ag-ui/client";
    import { Observable } from "rxjs";
    
    export class EchoAgent extends AbstractAgent {
      run(input: RunAgentInput): Observable<BaseEvent> {
        return new Observable<BaseEvent>((subscriber) => {
          const { threadId, runId } = input;
          const last = input.messages.at(-1);
          const text = typeof last?.content === "string" ? last.content : "";
          const messageId = crypto.randomUUID();
    
          subscriber.next({ type: EventType.RUN_STARTED, threadId, runId });
          subscriber.next({ type: EventType.TEXT_MESSAGE_START, messageId, role: "assistant" });
          subscriber.next({ type: EventType.TEXT_MESSAGE_CONTENT, messageId, delta: `You said: ${text}` });
          subscriber.next({ type: EventType.TEXT_MESSAGE_END, messageId });
          subscriber.next({ type: EventType.RUN_FINISHED, threadId, runId });
          subscriber.complete();
        });
      }
    }

Tool calls, state updates, and reasoning are more events on the same stream. See the [AG-UI event reference](https://docs.ag-ui.com/concepts/events).

## Register it in the runtime#

Pass an instance in the `agents` map. The key is the agent ID the frontend uses. The chat components use `default` when you do not name an agent.

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
      InMemoryAgentRunner,
    } from "@copilotkit/runtime/v2";
    import { EchoAgent } from "@/lib/echo-agent";
    
    const runtime = new CopilotRuntime({
      agents: { default: new EchoAgent() },
      runner: new InMemoryAgentRunner(),
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;
    export const PATCH = handler;
    export const DELETE = handler;

The agent runs inside the route handler's process. There is no separate agent server and no URL to configure. The frontend setup is the same as in the [quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart).

## Override `clone` when the agent has its own fields#

The runtime does not run the instance you registered. For every request it calls `agent.clone()` and runs the copy, so per-request changes never touch the original.

The base `AbstractAgent.clone()` copies only the fields `AbstractAgent` itself defines, such as the agent ID, thread ID, messages, state, subscribers, and middleware. It does not call your constructor. A field that your subclass sets in its constructor, such as an API client, a URL, or a config object, is `undefined` on the copy.

`EchoAgent` above has no fields of its own, so the base `clone` is enough. An agent that takes a client in its constructor needs to copy it:

lib/support-agent.ts
    
    
    import {
      AbstractAgent,
      EventType,
      type BaseEvent,
      type RunAgentInput,
    } from "@ag-ui/client";
    import { Observable } from "rxjs";
    
    export interface SupportClient {
      answer(question: string, signal: AbortSignal): Promise<string>;
    }
    
    export class SupportAgent extends AbstractAgent {
      constructor(private client: SupportClient) {
        super();
      }
    
      override clone(): SupportAgent {
        const copy = super.clone() as SupportAgent;
        copy.client = this.client;
        return copy;
      }
    
      run(input: RunAgentInput): Observable<BaseEvent> {
        return new Observable<BaseEvent>((subscriber) => {
          const controller = new AbortController();
          const { threadId, runId } = input;
          const last = input.messages.at(-1);
          const question = typeof last?.content === "string" ? last.content : "";
    
          subscriber.next({ type: EventType.RUN_STARTED, threadId, runId });
          this.client
            .answer(question, controller.signal)
            .then((answer) => {
              const messageId = crypto.randomUUID();
              subscriber.next({ type: EventType.TEXT_MESSAGE_START, messageId, role: "assistant" });
              subscriber.next({ type: EventType.TEXT_MESSAGE_CONTENT, messageId, delta: answer });
              subscriber.next({ type: EventType.TEXT_MESSAGE_END, messageId });
              subscriber.next({ type: EventType.RUN_FINISHED, threadId, runId });
              subscriber.complete();
            })
            .catch((error) => subscriber.error(error));
    
          return () => controller.abort();
        });
      }
    }

Start from `super.clone()` and add your fields to it, the same way `HttpAgent` copies its `url` and `headers`. Do not return `new SupportAgent(this.client)`: a new instance starts with no middleware, so anything you attached with `agent.use(...)` at startup silently stops running.

You only need to copy fields that hold configuration. A field that `run` resets at the start of every run holds per-run scratch state, and losing it on the copy changes nothing.

The function returned inside the `Observable` is its teardown. It runs when the run completes, fails, or is unsubscribed, so it is the place to cancel in-flight work.

### The symptom when `clone` is missing#

The registration succeeds and `/info` lists the agent, but every run fails as soon as `run` touches the missing field. The server logs:
    
    
    Agent execution failed: TypeError: Cannot read properties of undefined (reading 'answer')

With `InMemoryAgentRunner`, the run's event stream ends with a `RUN_ERROR` event that carries the same message and the code `INCOMPLETE_STREAM`. If the error names one of your own constructor fields, add a `clone` override that copies it.

## Remote agents: use `HttpAgent`#

If the agent runs as its own service and serves AG-UI over HTTP, do not write a subclass. Register an `HttpAgent` that points at the service:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { HttpAgent } from "@ag-ui/client";
    import { CopilotRuntime, InMemoryAgentRunner } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: { default: new HttpAgent({ url: process.env.AGENT_URL! }) },
      runner: new InMemoryAgentRunner(),
    });

`HttpAgent` already overrides `clone`. The URL is the agent service's own endpoint, not the runtime's. See [Copilot Runtime](https://docs.copilotkit.ai/langgraph-fastapi/backend/copilot-runtime#agents).

## Related#

  * [How agents slot into the runtime](https://docs.copilotkit.ai/langgraph-fastapi/backend/ag-ui#how-agents-slot-into-the-runtime): the request path every registered agent goes through.
  * [Use any model router](https://docs.copilotkit.ai/langgraph-fastapi/backend/custom-agent): `BuiltInAgent` factory mode, which handles lifecycle events for you.
  * [AG-UI middleware](https://docs.copilotkit.ai/langgraph-fastapi/agentic-protocols/ag-ui-middleware): attach behavior to any agent with `agent.use(...)`.



### On this page

InstallA minimal agentRegister it in the runtimeOverride clone when the agent has its own fieldsThe symptom when clone is missingRemote agents: use HttpAgentRelated
