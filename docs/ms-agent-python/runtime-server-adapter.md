---
url: https://docs.copilotkit.ai/ms-agent-python/runtime-server-adapter/
title: Deploy to any runtime
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:22:40.748928+00:00
---

# Deploy to any runtime

> Source: https://docs.copilotkit.ai/ms-agent-python/runtime-server-adapter/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-python)[Quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-python/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-python/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)

# Deploy to any runtime

Deploy the CopilotKit runtime on any backend framework — Node.js, Express, Hono, Bun, Deno, Cloudflare Workers, and more.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

The TypeScript CopilotKit runtime is **framework-agnostic**. At its core, it's a pure Fetch handler — a function that takes a `Request` and returns a `Response`. This means it runs natively on any platform that supports the [Fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API), and thin adapters are provided for Node.js-based frameworks like Express and Hono.

TypeScript server adapters

This guide covers the TypeScript runtime, which works with or without Intelligence. For Python, Go, Ruby, or C#/.NET servers, follow the [Intelligence quickstart](https://docs.copilotkit.ai/ms-agent-python/intelligence/quickstart#connect-your-runtime). Those runtimes require Intelligence and expose multi-route endpoints.

## Quick Overview#

Runtime| Import Path| Key Function  
---|---|---  
**Fetch-native** (Bun, Deno, CF Workers, Next.js App Router)| `@copilotkit/runtime/v2`| `createCopilotRuntimeHandler`  
**Node.js HTTP**| `@copilotkit/runtime/v2/node`| `createCopilotNodeHandler` / `createCopilotNodeListener`  
**Express**| `@copilotkit/runtime/v2/express`| `createCopilotExpressHandler`  
**Hono**| `@copilotkit/runtime/v2/hono`| `createCopilotHonoHandler`  
  
## Multi-Route vs Single-Route#

The runtime supports two endpoint modes:

  * **Multi-route** (default) — exposes individual URL endpoints:

    * `GET {basePath}/info`
    * `POST {basePath}/agent/:agentId/run`
    * `POST {basePath}/agent/:agentId/connect`
    * `POST {basePath}/agent/:agentId/stop/:threadId`
    * `POST {basePath}/transcribe`
  * **Single-route** — a single `POST {basePath}` endpoint that accepts a JSON envelope:
        
        { "method": "agent/run", "params": { "agentId": "default" }, "body": { ... } }




Both modes use the same Runtime handlers. A current client and Runtime also carry Intelligence thread, memory, and annotation operations through the single endpoint. They negotiate this support through Runtime info, so older clients and servers keep their existing behavior.

Single-route mode is useful when your platform only allows one route handler, or when you prefer a simpler URL structure.

The mode you pick here binds the frontend

Both `<CopilotKit>` and `<CopilotKitProvider>` detect the mode when you pass no transport prop, so either one follows whichever mode you pick here. Pin it with `useSingleEndpoint` only if you want to skip that detection — and then it has to match. The full mapping is in [Provider and handler pairs](https://docs.copilotkit.ai/ms-agent-python/backend/runtime-endpoints#provider-and-handler-pairs).

## Fetch-Native Runtimes#

If your platform supports the Fetch API natively (Bun, Deno, Cloudflare Workers, etc.), you can use `createCopilotRuntimeHandler` directly — no adapter needed.
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    // 1. Create the runtime with your agent(s)
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // 2. Create a Fetch handler — takes Request, returns Response
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: true,
    });
    
    // 3. Serve it (Bun example — works the same with Deno.serve, CF Workers, etc.)
    Bun.serve({ fetch: handler, port: 4000 });

For framework-specific examples, see the sections below.

## Bun#

Multi-routeSingle-routeExisting server

server.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    // Configure the runtime with your agent(s)
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Create a Fetch handler with multi-route endpoints (GET /info, POST /agent/:id/run, etc.)
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: true,
    });
    
    // Bun natively supports Fetch handlers
    Bun.serve({ fetch: handler, port: 4000 });

server.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Single-route mode: one POST endpoint that dispatches via JSON envelope
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
      cors: true,
    });
    
    Bun.serve({ fetch: handler, port: 4000 });

server.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const copilotHandler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: true,
    });
    
    Bun.serve({
      port: 4000,
      fetch(request) {
        const url = new URL(request.url);
    
        // Route CopilotKit requests to the handler
        if (url.pathname.startsWith("/api/copilotkit")) {
          return copilotHandler(request);
        }
    
        // Your other routes
        if (url.pathname === "/health") {
          return Response.json({ status: "healthy" });
        }
    
        return Response.json({ status: "ok" });
      },
    });

## Deno#

Multi-routeSingle-routeExisting server

server.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: true,
    });
    
    // Deno.serve natively accepts a Fetch handler
    Deno.serve({ port: 4000 }, handler);

server.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Single-route mode: one POST endpoint that dispatches via JSON envelope
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
      cors: true,
    });
    
    Deno.serve({ port: 4000 }, handler);

server.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const copilotHandler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: true,
    });
    
    Deno.serve({ port: 4000 }, (request) => {
      const url = new URL(request.url);
    
      // Route CopilotKit requests to the handler
      if (url.pathname.startsWith("/api/copilotkit")) {
        return copilotHandler(request);
      }
    
      // Your other routes
      if (url.pathname === "/health") {
        return Response.json({ status: "healthy" });
      }
    
      return Response.json({ status: "ok" });
    });

## Cloudflare Workers#

Do not construct an agent at module scope

Workers do not allow random values in global scope, and an agent generates a thread ID when you construct it. An agent created at the top level of the module stops the Worker from starting, with `Disallowed operation called within global scope`. The examples below construct everything inside `fetch`. To create the runtime once at module scope, pass `agents` as a factory. The runtime calls the factory on each request:
    
    
    const runtime = new CopilotRuntime({
      agents: () => ({
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      }),
    });

Multi-routeSingle-routeExisting worker

src/index.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    export interface Env {
      OPENAI_API_KEY: string;
    }
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        const runtime = new CopilotRuntime({
          agents: {
            default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
          },
        });
    
        // Workers use the Fetch API natively — handler plugs in directly
        const handler = createCopilotRuntimeHandler({
          runtime,
          basePath: "/api/copilotkit",
          cors: true,
        });
    
        return handler(request);
      },
    };

src/index.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    export interface Env {
      OPENAI_API_KEY: string;
    }
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        const runtime = new CopilotRuntime({
          agents: {
            default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
          },
        });
    
        // Single-route: one POST endpoint with JSON envelope dispatch
        const handler = createCopilotRuntimeHandler({
          runtime,
          basePath: "/api/copilotkit",
          mode: "single-route",
          cors: true,
        });
    
        return handler(request);
      },
    };

src/index.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    export interface Env {
      OPENAI_API_KEY: string;
    }
    
    export default {
      async fetch(request: Request, env: Env): Promise<Response> {
        const url = new URL(request.url);
    
        // Route CopilotKit requests to the handler
        if (url.pathname.startsWith("/api/copilotkit")) {
          const runtime = new CopilotRuntime({
            agents: {
              default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
            },
          });
    
          const handler = createCopilotRuntimeHandler({
            runtime,
            basePath: "/api/copilotkit",
            cors: true,
          });
    
          return handler(request);
        }
    
        // Your other routes
        if (url.pathname === "/health") {
          return Response.json({ status: "healthy" });
        }
    
        return Response.json({ status: "ok" });
      },
    };

## Next.js App Router#

Multi-routeSingle-route

app/api/copilotkit/[...path]/route.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    // Export every method used by the multi-route Runtime.
    export { handler as GET, handler as POST, handler as PATCH, handler as DELETE };

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Single-route: only POST needed, no catch-all [...path] required
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
    });
    
    export { handler as POST };

In single-route mode, no `[...path]` catch-all is needed — everything goes through a single `POST /api/copilotkit`.

No `cors: true` needed for Next.js — same-origin requests don't require CORS headers.

## React Router (Framework Mode)#

React Router v7 in framework mode uses file-based routing with Fetch API handlers — the CopilotKit handler works directly as a resource route.

Multi-routeSingle-route

app/routes/api.copilotkit.$.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    import type { Route } from "./+types/api.copilotkit.$";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    // loader handles GET requests (e.g. /info)
    export function loader({ request }: Route.LoaderArgs) {
      return handler(request);
    }
    
    // action handles POST requests (e.g. /agent/:id/run)
    export function action({ request }: Route.ActionArgs) {
      return handler(request);
    }

The `$` splat segment in the filename (`api.copilotkit.$.ts`) captures all subpaths under `/api/copilotkit/`, allowing the CopilotKit router to handle `/info`, `/agent/:id/run`, etc.

app/routes/api.copilotkit.ts
    
    
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    import type { Route } from "./+types/api.copilotkit";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Single-route: only action (POST) needed, no splat segment required
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
    });
    
    export function action({ request }: Route.ActionArgs) {
      return handler(request);
    }

In single-route mode, no `$` splat is needed — the filename is just `api.copilotkit.ts` and all dispatch happens via the JSON envelope.

## TanStack Start#

TanStack Start uses API routes that receive standard `Request` objects and return `Response` objects.

Multi-routeSingle-route

app/routes/api/copilotkit/$.ts
    
    
    import { createAPIFileRoute } from "@tanstack/react-start/api";
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    // The $ splat matches all subpaths and forwards every Runtime method.
    export const APIRoute = createAPIFileRoute("/api/copilotkit/$")({
      GET: ({ request }) => handler(request),
      POST: ({ request }) => handler(request),
      PATCH: ({ request }) => handler(request),
      DELETE: ({ request }) => handler(request),
    });

The `$` in the filename is TanStack Start's splat parameter, matching all subpaths under `/api/copilotkit/`.

app/routes/api/copilotkit.ts
    
    
    import { createAPIFileRoute } from "@tanstack/react-start/api";
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Single-route: only POST needed, no $ splat required
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
    });
    
    export const APIRoute = createAPIFileRoute("/api/copilotkit")({
      POST: ({ request }) => handler(request),
    });

In single-route mode, no `$` splat is needed — the file is `copilotkit.ts` (not `$.ts`) and only `POST` is required.

## Node.js HTTP#

For vanilla Node.js HTTP servers, use the `/node` subpath which bridges Fetch to Node's `IncomingMessage`/`ServerResponse`.

Multi-routeSingle-routeExisting server

server.ts
    
    
    import { createServer } from "node:http";
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotNodeListener } from "@copilotkit/runtime/v2/node";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // createCopilotNodeListener returns a Node request listener (req, res) => void
    // that bridges to the Fetch handler internally
    const listener = createCopilotNodeListener({
      runtime,
      basePath: "/api/copilotkit",
      cors: true,
    });
    
    createServer(listener).listen(4000, () => {
      console.log("Listening at http://localhost:4000/api/copilotkit");
    });

server.ts
    
    
    import { createServer } from "node:http";
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotNodeListener } from "@copilotkit/runtime/v2/node";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const listener = createCopilotNodeListener({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
      cors: true,
    });
    
    createServer(listener).listen(4000, () => {
      console.log("Listening at http://localhost:4000/api/copilotkit");
    });

server.ts
    
    
    import { createServer } from "node:http";
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotNodeHandler } from "@copilotkit/runtime/v2/node";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // 1. Create the Fetch handler
    const copilotHandler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: true,
    });
    
    // 2. Wrap it as a Node (req, res) handler
    const copilotNodeHandler = createCopilotNodeHandler(copilotHandler);
    
    // 3. Use it in your existing server with manual routing
    const server = createServer(async (req, res) => {
      const url = new URL(req.url ?? "/", `http://${req.headers.host}`);
    
      // Route CopilotKit requests to the handler
      if (url.pathname.startsWith("/api/copilotkit")) {
        return copilotNodeHandler(req, res);
      }
    
      // Your other routes
      if (url.pathname === "/health") {
        res.writeHead(200, { "Content-Type": "application/json" });
        res.end(JSON.stringify({ status: "healthy" }));
        return;
      }
    
      res.writeHead(200, { "Content-Type": "application/json" });
      res.end(JSON.stringify({ status: "ok" }));
    });
    
    server.listen(4000, () => {
      console.log("Listening at http://localhost:4000");
    });

## Express#

The Express adapter returns a router that you mount with `app.use()`. The value is a real `express.Router()`. Its declared type is `CopilotExpressRouter`, which names no Express major, so it mounts on Express 4 and Express 5 alike.

`express` is an optional peer dependency of `@copilotkit/runtime`, so install it in your own app. Both majors are supported.
    
    
    npm install express cors

Multi-routeSingle-routeExisting server

server.ts
    
    
    import express from "express";
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotExpressHandler } from "@copilotkit/runtime/v2/express";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const app = express();
    
    // Mount the CopilotKit router — creates Express routes under /api/copilotkit
    app.use(
      createCopilotExpressHandler({
        runtime,
        basePath: "/api/copilotkit",
        cors: true,
      }),
    );
    
    app.listen(4000, () => {
      console.log("Listening at http://localhost:4000/api/copilotkit");
    });

server.ts
    
    
    import express from "express";
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotExpressHandler } from "@copilotkit/runtime/v2/express";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const app = express();
    
    // Single-route: one POST endpoint that dispatches via JSON envelope
    app.use(
      createCopilotExpressHandler({
        runtime,
        basePath: "/api/copilotkit",
        mode: "single-route",
        cors: true,
      }),
    );
    
    app.listen(4000, () => {
      console.log("Listening at http://localhost:4000/api/copilotkit");
    });

server.ts
    
    
    import express from "express";
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotExpressHandler } from "@copilotkit/runtime/v2/express";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const app = express();
    
    // Your existing routes
    app.get("/", (req, res) => {
      res.json({ status: "ok" });
    });
    
    app.get("/health", (req, res) => {
      res.json({ status: "healthy" });
    });
    
    // Mount CopilotKit alongside your existing routes
    app.use(
      createCopilotExpressHandler({
        runtime,
        basePath: "/api/copilotkit",
        cors: true,
      }),
    );
    
    app.listen(4000, () => {
      console.log("Listening at http://localhost:4000");
    });

### Express Options#

Option| Type| Default| Description  
---|---|---|---  
`runtime`| `CopilotRuntime`|  _required_|  The runtime instance  
`basePath`| `string`|  _required_|  URL path prefix (e.g. `"/api/copilotkit"`)  
`mode`| `"multi-route"` | `"single-route"`| `"multi-route"`| Multi-route exposes individual endpoints; single-route uses a JSON envelope  
`cors`| `boolean` | `CorsOptions`| `false`| CORS configuration. `true` for permissive defaults, or pass a `cors` options object  
`hooks`| `CopilotRuntimeHooks`| —| Lifecycle hooks  
  
The Express adapter is compatible with `express.json()` body parsing. If you have `app.use(express.json())` before the CopilotKit router, the adapter will detect the pre-parsed body and handle it correctly.

## Hono#

The Hono adapter returns a Hono app that you mount with `app.route()`.
    
    
    npm install

Multi-routeSingle-routeExisting server

server.ts
    
    
    import { serve } from "@hono/node-server";
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotHonoHandler } from "@copilotkit/runtime/v2/hono";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Returns a Hono app with CopilotKit routes mounted at basePath
    const endpoint = createCopilotHonoHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    // Serve the Hono app directly
    serve({ fetch: endpoint.fetch, port: 4000 }, () => {
      console.log("Listening at http://localhost:4000/api/copilotkit");
    });

server.ts
    
    
    import { serve } from "@hono/node-server";
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotHonoHandler } from "@copilotkit/runtime/v2/hono";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Single-route: one POST endpoint that dispatches via JSON envelope
    const endpoint = createCopilotHonoHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
    });
    
    serve({ fetch: endpoint.fetch, port: 4000 }, () => {
      console.log("Listening at http://localhost:4000/api/copilotkit");
    });

server.ts
    
    
    import { Hono } from "hono";
    import { serve } from "@hono/node-server";
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotHonoHandler } from "@copilotkit/runtime/v2/hono";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const app = new Hono();
    
    // Your existing routes
    app.get("/", (c) => c.json({ status: "ok" }));
    app.get("/health", (c) => c.json({ status: "healthy" }));
    
    // Mount CopilotKit as a sub-app via app.route()
    app.route("/", createCopilotHonoHandler({ runtime, basePath: "/api/copilotkit" }));
    
    serve({ fetch: app.fetch, port: 4000 }, () => {
      console.log("Listening at http://localhost:4000");
    });

## Elysia (Bun)#

Elysia runs on Bun and supports the Fetch API natively, so you use `createCopilotRuntimeHandler` directly.
    
    
    bun add elysia

Multi-routeSingle-routeExisting server

server.ts
    
    
    import { Elysia } from "elysia";
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Create a Fetch handler — Elysia passes the raw Request through
    const handler = createCopilotRuntimeHandler({ runtime, cors: true });
    
    new Elysia()
      .all("/api/copilotkit/*", ({ request }) => handler(request))
      .listen(4000);

server.ts
    
    
    import { Elysia } from "elysia";
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    // Single-route: one POST endpoint, no wildcard needed
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
      cors: true,
    });
    
    new Elysia()
      .post("/api/copilotkit", ({ request }) => handler(request))
      .listen(4000);

server.ts
    
    
    import { Elysia } from "elysia";
    import { CopilotRuntime, createCopilotRuntimeHandler, BuiltInAgent } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({
      agents: {
        default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({ runtime, cors: true });
    
    new Elysia()
      // Your existing routes
      .get("/", () => ({ status: "ok" }))
      .get("/health", () => ({ status: "healthy" }))
      // Mount CopilotKit
      .all("/api/copilotkit/*", ({ request }) => handler(request))
      .listen(4000);

## Lifecycle Hooks#

All adapters support lifecycle hooks for cross-cutting concerns like authentication, logging, and response modification.
    
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      hooks: {
        // Before routing — auth, correlation IDs
        onRequest: async ({ request, path, runtime }) => {
          const token = request.headers.get("authorization");
          if (!token) {
            throw new Response("Unauthorized", { status: 401 });
          }
        },
    
        // After routing — route-specific authorization
        onBeforeHandler: async ({ request, route }) => {
          console.log(`Handling ${route.method} for agent ${route.agentId}`);
        },
    
        // After handler — modify response headers
        onResponse: async ({ response, request }) => {
          const headers = new Headers(response.headers);
          headers.set("x-request-id", crypto.randomUUID());
          return new Response(response.body, {
            status: response.status,
            headers,
          });
        },
    
        // On error — custom error responses
        onError: async ({ error, request }) => {
          console.error("Handler error:", error);
        },
      },
    });

Hook| When| Can modify  
---|---|---  
`onRequest`| Before routing| Throw `Response` to short-circuit  
`onBeforeHandler`| After routing, before handler| Access `route` info (method, agentId, threadId)  
`onResponse`| After handler| Return a new `Response` to replace it  
`onError`| On unhandled error| Log or produce a custom error response  
  
## CORS Configuration#

### Fetch-native runtimes#

Pass `cors: true` for permissive defaults (`Access-Control-Allow-Origin: *`), or provide a config object:
    
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: {
        origin: "https://myapp.com",
        credentials: true,
      },
    });

### Express#

Pass `cors: true` for permissive defaults, or pass a [cors](https://www.npmjs.com/package/cors) options object:
    
    
    createCopilotExpressHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: {
        origin: "https://myapp.com",
        credentials: true,
      },
    });

### Hono#

Pass a `cors` config with explicit origin:
    
    
    createCopilotHonoHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: {
        origin: "https://myapp.com",
        credentials: true,
      },
    });

When using `credentials: true`, you must specify an explicit origin — wildcard (`*`) is not allowed by the CORS spec.

## Connecting Your Frontend#

Once your runtime is running, point your frontend at it:
    
    
    <CopilotKit runtimeUrl="http://localhost:4000/api/copilotkit" useSingleEndpoint={false}>
      <YourApp />
    </CopilotKit>

Match the prop to the mode you chose

`useSingleEndpoint={false}` is what a **multi-route** handler needs — the default, and what every example above uses unless you passed `mode: "single-route"`. If you did choose single-route, drop the prop: the v1 `<CopilotKit>` wrapper already defaults to that transport. `<CopilotKitProvider>` detects the mode and needs no prop either way. Getting this wrong 404s the startup `/info` call, and the runtime will say so in your server logs.

For same-origin deployments, use a relative path:
    
    
    <CopilotKit runtimeUrl="/api/copilotkit" useSingleEndpoint={false}>
      <YourApp />
    </CopilotKit>

### On this page

Quick OverviewMulti-Route vs Single-RouteFetch-Native RuntimesBunDenoCloudflare WorkersNext.js App RouterReact Router (Framework Mode)TanStack StartNode.js HTTPExpressExpress OptionsHonoElysia (Bun)Lifecycle HooksCORS ConfigurationFetch-native runtimesExpressHonoConnecting Your Frontend
