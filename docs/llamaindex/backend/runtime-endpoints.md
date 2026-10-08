---
url: https://docs.copilotkit.ai/llamaindex/backend/runtime-endpoints/
title: Runtime HTTP endpoints
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:14:17.886852+00:00
---

# Runtime HTTP endpoints

> Source: https://docs.copilotkit.ai/llamaindex/backend/runtime-endpoints/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)Runtime

# Runtime HTTP endpoints

The HTTP routes exposed by the CopilotKit runtime for self-hosting, proxying, and debugging.

When you mount the CopilotKit runtime with `createCopilotExpressHandler`, `createCopilotHonoHandler`, `copilotRuntimeNextJSAppRouterEndpoint`, or any of the other framework adapters, it serves a small set of HTTP routes under the `basePath` you choose, such as `/api/copilotkit`. Most applications never call these routes directly. The frontend proxy (`ProxiedCopilotRuntimeAgent`) calls them for you. When you self-host behind a reverse proxy, lock down auth, or debug a connection failure with `curl`, use this page to confirm what the runtime exposes.

Other runtime languages

Python, Go, Ruby, and C#/.NET runtimes require Intelligence and serve multi-route endpoints. Use `useSingleEndpoint={false}` with the React provider; do not send a single-route envelope to those servers. The JavaScript handler factories, legacy endpoints, and optional TypeScript features below are specific to the TypeScript runtime. See the [Intelligence quickstart](https://docs.copilotkit.ai/llamaindex/intelligence/quickstart#connect-your-runtime) for native server setup.

## Provider and handler pairs#

The browser provider and the Runtime handler have to agree on the **transport**. CopilotKit ships more than one name for each half, and they are not interchangeable: each provider setting requires a matching handler mode. Different pages and older apps show different pairs, so this table is the mapping:

Provider| `useSingleEndpoint`| Transport| Needs handler| Route file  
---|---|---|---|---  
`<CopilotKit>` or `<CopilotKitProvider>`| omitted| `auto` — detected from the Runtime| either| matches the handler  
`<CopilotKit>` or `<CopilotKitProvider>`| `{true}`| `single`| single-route| `route.ts`, `POST`  
`<CopilotKit>` or `<CopilotKitProvider>`| `{false}`| `rest`| multi-route| `[[...slug]]/route.ts`, 4 verbs  
  
`<CopilotKit>` is a backward-compatible wrapper that renders `<CopilotKitProvider>` internally. Both are exported from `@copilotkit/react-core/v2`, and since 1.70.2 both treat an omitted `useSingleEndpoint` the same way: the transport is `auto`, so the client probes the Runtime and matches whichever mode it serves.

Pinning the wrong mode 404s silently

Passing `useSingleEndpoint={true}` to a multi-route Runtime sends an envelope that matches no route, so the Runtime 404s while `GET /info` still returns 200 and the app looks connected. The Runtime's error body names the fix.

Before 1.70.2, `<CopilotKit>` pinned the flag to `true` internally, so omitting it selected the single-route transport and 404'd against a multi-route handler. On those versions, pass `useSingleEndpoint={false}` explicitly.

Both ship from the same package entry point, so moving between them is an import change, not a migration. One prop does get renamed: `<CopilotKit>` names the agent with `agent`, and `<CopilotKitProvider>` names it with `agentId`.
    
    
    // v1 wrapper
    <CopilotKit runtimeUrl="/api/copilotkit" agent="my_agent" useSingleEndpoint={false}>
    
    // v2 provider
    <CopilotKitProvider runtimeUrl="/api/copilotkit" agentId="my_agent">

You can also name the agent per chat with `<CopilotChat agentId="my_agent">`, or for a subtree with `<CopilotChatConfigurationProvider agentId="my_agent">`. A provider-level `agentId` is the default that those two override.

### Which handlers serve which mode#

Mode| Handlers  
---|---  
Multi-route (default)| `createCopilotRuntimeHandler`, `createCopilotHonoHandler`, `createCopilotExpressHandler`, `createCopilotNodeHandler`, `createCopilotNodeListener`  
Single-route| Any of the above with `mode: "single-route"`  
Single-route only, no option| `copilotRuntimeNextJSAppRouterEndpoint`, `copilotRuntimeNextJSPagesRouterEndpoint`, `copilotRuntimeNodeHttpEndpoint`, `copilotRuntimeNodeExpressEndpoint`, `copilotRuntimeNestEndpoint`  
  
The framework wrappers support Intelligence resources

Every `copilotRuntime*Endpoint` wrapper builds its handler with `mode: "single-route"`. A current client and Runtime carry AG-UI Streams, Memory, and annotation requests through that endpoint. Setting `useSingleEndpoint={false}` still points the browser at REST routes that these wrappers do not serve.

Older code may use these deprecated aliases:

Deprecated| Use instead  
---|---  
`createCopilotEndpoint`| `createCopilotHonoHandler`  
`createCopilotEndpointSingleRoute`| `createCopilotHonoHandler` with `mode: "single-route"`  
`createCopilotEndpointExpress`| `createCopilotExpressHandler`  
`createCopilotEndpointSingleRouteExpress`| `createCopilotExpressHandler` with `mode: "single-route"`  
  
A mismatched pair fails at discovery

A mismatch fails at discovery, not at your application code. A multi-route provider against a single-route Runtime 404s on `GET {basePath}/info`; a single-route provider against a multi-route Runtime posts an envelope the Runtime does not accept. See Connect route 404 on a fresh thread.

## Multi-route mode (default)#

By default the runtime runs in **multi-route** mode, exposing a separate route per operation. Given a `basePath` of `/api/copilotkit`, the routes are:

Method & path| Purpose  
---|---  
`GET /api/copilotkit/info`| Runtime info. The frontend calls this on startup to discover registered agents and their metadata.  
`GET /api/copilotkit/inspector-metadata`| Optional trusted project, plan, license, action, usage, and expiry context for the Inspector. Intelligence-backed runtimes advertise this route with `inspectorMetadata: true` in the runtime-info response.  
`POST /api/copilotkit/agent/:agentId/run`| Start an agent run. The request body is an AG-UI `RunAgentInput`; the response is an SSE stream of AG-UI events. With Intelligence, the response is JSON. See Run and connect with Intelligence.  
`POST /api/copilotkit/agent/:agentId/connect`| Connect to an agent's thread. Used to resume streaming after a reconnect or page refresh. Also an SSE stream, or JSON with Intelligence.  
`POST /api/copilotkit/agent/:agentId/stop/:threadId`| Stop the in-progress run on a given thread. An optional JSON body `{ "runId": "..." }` stops only that run. A body that is not valid JSON, or carries any other key, is rejected with 400 and stops nothing.  
`POST /api/copilotkit/transcribe`| Transcribe audio (used by the voice / transcription input).  
  
`:agentId` is the key under which you registered the agent in `new CopilotRuntime({ agents: { ... } })`, for example `default` or `research-agent`. `:threadId` is the thread the run belongs to.

The `GET /info` route is the same endpoint the frontend uses for agent discovery. If it isn't reachable from the runtime, the frontend reports a `runtime_info_fetch_failed` error. See [Error Debugging](https://docs.copilotkit.ai/llamaindex/troubleshooting/error-debugging).

An Intelligence runtime also returns `runtimeEntitlements`. `ready` includes the normalized feature and limit values. `degraded`, `misconfigured`, and `unavailable` include a structured error with a code, message, and retry flag. The `/info` request still succeeds when entitlement lookup fails so core Runtime behavior can continue; features that need a proven entitlement stay off. If Intelligence rejects the project key with a `401`, the Runtime still returns `200` from `/info`. The body reports `runtimeEntitlements.status` as `misconfigured` with the non-retryable `runtime_entitlements_misconfigured` error code.

### Run and connect with Intelligence#

When the runtime has an `intelligence` client, the run and connect routes do not stream events. They return JSON that tells the client where to read the events:
    
    
    {
      "threadId": "<thread id>",
      "runId": "<run id>",
      "joinToken": "<join token>",
      "realtime": {
        "clientUrl": "<Intelligence websocket URL>",
        "topic": "thread:<thread id>"
      }
    }

The client opens a websocket to `realtime.clientUrl` and joins the `realtime.topic` channel with the `joinToken`. The AG-UI events of the run arrive on that channel. `CopilotKitProvider` does this for you when runtime info reports Intelligence. The connect route returns the same body without `runId`, or `204` with no body when the platform returns no connection.

A direct `POST` to the run route, for example from `curl` or a test script, gets this JSON body and no events. To read the events of a thread without a websocket client, call `GET {basePath}/threads/:threadId/events`. It returns `{ "events": [...] }`. See Thread routes.

### Inspector metadata#

An Intelligence-backed runtime adds `inspectorMetadata: true` to its runtime-info response. After the main connection completes, `@copilotkit/core` uses that flag to request `GET {basePath}/inspector-metadata` in the background. Older runtimes omit the flag, so newer clients skip the optional request.

A valid response is a versioned `InspectorMetadataV1` JSON object. The response always uses `Cache-Control: no-store, private`. The route returns `204` with the same cache policy when data is absent, the schema is unsupported, the runtime is not backed by Intelligence, or the provider request fails. A metadata failure does not change the runtime connection or agent state. The upstream Intelligence request has a five-second deadline; a timeout follows the same private `204` path.
    
    
    {
      "schemaVersion": 1,
      "identity": {
        "organizationName": "Acme",
        "projectName": "Support"
      },
      "plan": {
        "code": "team",
        "label": "Team"
      },
      "license": {
        "state": "valid"
      },
      "action": {
        "kind": "manage_plan",
        "url": "https://ops.example.com/account/organization/org_123/organization-billing"
      },
      "usage": {
        "used": 42,
        "limit": {
          "kind": "finite",
          "value": 1000
        },
        "expiringSoonCount": 7
      }
    }

Every module is optional and independent. `usage.expiringSoonCount` is an additive V1 leaf for deadlines in the next 24 hours: `0` is a known count, while absence means no trusted expiry count is available. Shared removes a malformed expiry leaf without removing valid `used`, `limit`, or sibling modules. Older V1 producers may omit the leaf, and older consumers may ignore it without a synchronized deployment.
    
    
    curl -i http://localhost:4000/api/copilotkit/inspector-metadata

The runtime uses its server-side Intelligence API key for the upstream request. It does not forward browser headers or cookies to Intelligence, and it does not expose provider error bodies to the browser. Auth headers and cookies can still protect the browser-to-runtime request like any other runtime route.

### Thread routes#

The runtime also serves the conversation history behind the threads UI. These routes exist in multi-route mode whichever runner you use:

Method & path| Purpose  
---|---  
`GET /api/copilotkit/threads`| List threads. With Intelligence, the `agentId` query parameter is required. Without Intelligence, it is optional and filters the list.  
`GET /api/copilotkit/threads/:threadId/messages`| That thread's full message history.  
`GET /api/copilotkit/threads/:threadId/events`| That thread's compacted AG-UI event stream.  
`GET /api/copilotkit/threads/:threadId/state`| That thread's last state snapshot.  
`POST /api/copilotkit/threads/clear`| Wipe the in-memory thread history. Always answers `204`, and clears nothing on a runner that keeps no local store.  
`PATCH` or `DELETE /api/copilotkit/threads/:threadId`| Rename or delete a thread. Intelligence only.  
`POST /api/copilotkit/threads/:threadId/archive`| Archive a thread. Intelligence only.  
`POST /api/copilotkit/threads/subscribe`| Subscribe to thread changes. Intelligence only.  
  
An Intelligence runtime answers `GET /threads` with `400` when the request has no `agentId`. Send the agent key you registered in `CopilotRuntime`. The request also has to carry the auth that your `identifyUser` reads, because the list holds only that user's threads:
    
    
    curl -s "http://localhost:4000/api/copilotkit/threads?agentId=default"

The response is `{ "threads": [...], "nextCursor": ... }`. To page through it, pass `limit` and the `cursor` from the previous response. Add `includeArchived=true` to include archived threads. Those three parameters apply only with Intelligence.

Thread routes are not authorized for you

On the default `InMemoryAgentRunner` — and on anything extending it, such as `AgentCoreRunner` — these routes read the runner's local store and resolve no user at all: any caller that reaches the route reads the thread it names, `GET /threads` lists every thread in the process, and `POST /threads/clear` wipes them all. A runner that keeps no local store, such as `SqliteAgentRunner`, answers the four read routes with a `422` instead.

An Intelligence runtime scopes **most** of them to the user your `identifyUser` returns, but not all: `threads/events`, `threads/state` and `POST /agent/:agentId/stop/:threadId` read the thread by id alone. Guard those three yourself even on the platform.

`:threadId` is chosen by the client on the run, so it is not a secret. If more than one person uses your deployment, authorize these routes yourself — see [Thread authorization](https://docs.copilotkit.ai/llamaindex/auth#thread-authorization).

### Probing the runtime with curl#

The fastest way to confirm a self-hosted runtime is wired up is to hit `/info` directly:
    
    
    curl -s http://localhost:4000/api/copilotkit/info

You should get back a JSON body describing the registered agents. If you get a 404, your `basePath` doesn't match the URL you're requesting (or the handler isn't mounted). If you get a connection error, the server isn't listening on that host/port.

## Enable AG-UI Streams routes#

If the Inspector shows the Rich Threads setup view, the client did not find the features used to list and inspect saved Threads. This view is based on Runtime Threads capability, not license metadata. Complete these steps so Runtime info advertises those features and the Inspector can load saved history.

### Start with your coding agent#

Use this prompt to configure Intelligence and verify that your Runtime exposes AG-UI Streams.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

### Choose a Runtime route mode#

Single-route and multi-route handlers both expose AG-UI Streams. Use single-route when your server should expose only one `POST` endpoint:
    
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      mode: "single-route",
    });

For multi-route, omit `mode`. Your server must mount the full Runtime subtree and allow `GET`, `POST`, `PATCH`, and `DELETE`.

With the v2 React provider, omit `useSingleEndpoint` to detect the mode. You can also pin single-route with `useSingleEndpoint` or multi-route with `useSingleEndpoint={false}`.
    
    
    import { CopilotKitProvider } from "@copilotkit/react-core/v2";
    
    <CopilotKitProvider runtimeUrl="/api/copilotkit">
      <YourApp />
    </CopilotKitProvider>;

The provider and handler modes must match.

### Construct the Intelligence client#

`intelligence` is a `CopilotKitIntelligence` instance. Build it from your project's Intelligence API key:
    
    
    import { CopilotKitIntelligence } from "@copilotkit/runtime/v2";
    
    const intelligence = new CopilotKitIntelligence({
      apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
    });

`apiKey` is the only required option. `copilotkit project select` writes this key into your project's `.env` as `CPK_INTELLIGENCE_API_KEY`, and this is what consumes it.

Keep the key server-side. It is a project API key, so it is a different credential from the browser-visible `NEXT_PUBLIC_COPILOTKIT_LICENSE_KEY` used by the [Inspector](https://docs.copilotkit.ai/llamaindex/inspector) — do not substitute one for the other.

`apiUrl` and `wsUrl` default to the cloud-hosted platform. The API and realtime planes are deployed to **different hosts** , so one cannot be derived from the other by swapping the scheme. Override them only for a self-hosted or non-production deployment, and override **both together** — setting one alone points the two planes at different deployments, which logs a warning:
    
    
    const intelligence = new CopilotKitIntelligence({
      apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
      apiUrl: process.env.INTELLIGENCE_API_URL,
      wsUrl: process.env.INTELLIGENCE_GATEWAY_WS_URL,
    });

### Identify the signed-in application user#

An Intelligence-backed web Runtime exposes Threads only when it can scope them to an application user. Add `identifyUser` and resolve the user from a server-verified session or token:
    
    
    const runtime = new CopilotRuntime({
      agents,
      intelligence,
      identifyUser: async (request) => {
        const user = await authenticateApplicationUser(request);
        if (!user) throw new Error("Unauthorized");
        return { id: user.id, name: user.name };
      },
    });

See [Scope AG-UI Streams to the signed-in user](https://docs.copilotkit.ai/llamaindex/threads-lifecycle#scope-rich-threads-to-the-signed-in-user) for the full identity and authorization pattern.

### Mount the Runtime handler#

For single-route, mount one exact path and allow `POST`:

app/api/copilotkit/route.ts
    
    
    export { handler as POST };

For multi-route, pass the full `basePath` subtree to the Runtime. In file-based routers, use a catch-all or splat route. Allow `GET`, `POST`, `PATCH`, and `DELETE`:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    export { handler as GET, handler as POST, handler as PATCH, handler as DELETE };

See [Deploy to any runtime](https://docs.copilotkit.ai/llamaindex/runtime-server-adapter#multi-route-vs-single-route) for complete adapter examples.

### Verify the advertised capabilities#

Restart the Runtime. For multi-route, request its info endpoint:
    
    
    curl -s http://localhost:4000/api/copilotkit/info

An Intelligence-backed web Runtime that is ready for AG-UI Streams includes:
    
    
    {
      "threadEndpoints": {
        "list": true,
        "inspect": true,
        "mutations": true,
        "realtimeMetadata": true
      }
    }

For single-route, post an info envelope:
    
    
    curl -s http://localhost:4000/api/copilotkit \
      -H 'content-type: application/json' \
      -d '{"method":"info"}'

The response advertises the resource bridge and its thread features:
    
    
    {
      "singleRoute": {
        "resourceOperations": true,
        "threadEndpoints": {
          "list": true,
          "inspect": true,
          "mutations": true,
          "realtimeMetadata": true
        }
      }
    }

Reload your app after this response is available. The Inspector will replace the setup state with the saved Threads list. Cloud-hosted and self-hosted Intelligence use the same Runtime route setup.

## Single-route mode#

If you prefer to expose a single `POST` endpoint, for example to simplify a reverse-proxy rule or an API gateway, pass `mode: "single-route"`. In that mode the runtime exposes one `POST {basePath}` endpoint that accepts a JSON envelope `{ method, params, body }` and dispatches internally to the same handlers:

app/api/copilotkit/route.ts (Express)
    
    
    import { CopilotRuntime, BuiltInAgent } from "@copilotkit/runtime/v2";
    import { createCopilotExpressHandler } from "@copilotkit/runtime/v2/express";
    
    const runtime = new CopilotRuntime({
      agents: { default: new BuiltInAgent({ model: "openai/gpt-4o-mini" }) },
    });
    
    app.use(
      createCopilotExpressHandler({
        runtime,
        basePath: "/api/copilotkit",
        mode: "single-route",
      }),
    );

Install `express` yourself

`express` is an optional peer dependency of `@copilotkit/runtime`, so it is not installed for you. Run `npm install express` (`^4.18.0 || ^5.0.0`) in the app that mounts the adapter. Calling `createCopilotExpressHandler` without it throws and names the fix. Nothing else in the runtime needs express, so Hono and Next.js apps install nothing.

`basePath` is required, in both modes

The Express and single-route handlers each throw at mount time when `basePath` is missing — `basePath must be provided for Express endpoint` and `... for single-route endpoint` respectively — so the server fails to start rather than serving on the wrong paths. Give it the same path the route is mounted at.

Keep every runtime import on `/v2`

Import the runtime from `@copilotkit/runtime/v2` (and the Express adapter from `@copilotkit/runtime/v2/express`). Reaching into the package root, `@copilotkit/runtime`, gets you the v1 surface: a `CopilotRuntime` built there does not serve these routes, and the mismatch shows up as routes that 404 rather than as an import error.

The optional Inspector metadata operation uses the same endpoint with this envelope:
    
    
    { "method": "inspector/metadata" }

Its response and failure rules match `GET {basePath}/inspector-metadata`.

The client sends thread, memory, and annotation operations through the same endpoint with a `resource/request` envelope. The Runtime accepts only known resource paths and routes them through the same handlers as multi-route mode.

The frontend detects this mode on its own, so no prop is required. To pin it explicitly, pass `useSingleEndpoint`:
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit runtimeUrl="/api/copilotkit" useSingleEndpoint>
      <YourApp />
    </CopilotKit>;

The frontend transport must match the runtime mode. If the runtime is in single-route mode but the frontend is making multi-route requests (or vice versa), every call 404s. Omitting the prop avoids that by construction, since the client then probes for the mode the runtime actually serves — so pin `useSingleEndpoint` only when you want to skip that probe.

## CORS#

The Express and Hono adapters apply permissive CORS by default (`origin: "*"`, all standard methods, all headers) so local development works out of the box. Pass `cors: false` to disable the built-in middleware and handle CORS yourself, or pass a configuration object to scope it for production:
    
    
    createCopilotExpressHandler({
      runtime,
      basePath: "/api/copilotkit",
      cors: {
        origin: "https://app.example.com",
        methods: ["GET", "POST", "OPTIONS"],
      },
    });

## Authenticating requests#

Because these routes run on your server, they're the right place to enforce auth. The adapters accept lifecycle `hooks`. An `onRequest` hook runs before every request and can reject the request by throwing a `Response`:
    
    
    createCopilotExpressHandler({
      runtime,
      basePath: "/api/copilotkit",
      hooks: {
        onRequest: ({ request }) => {
          if (!request.headers.get("authorization")) {
            throw new Response("Unauthorized", { status: 401 });
          }
        },
      },
    });

`onRequest` runs before routing, so it knows the path but not the route. For per-thread decisions use `onBeforeHandler`, which runs after routing and receives the resolved `route`, including its `threadId`:
    
    
    createCopilotExpressHandler({
      runtime,
      basePath: "/api/copilotkit",
      hooks: {
        onBeforeHandler: async ({ request, route }) => {
          const user = await resolveUser(request);
    
          // Routes that name a thread on `route`.
          if ("threadId" in route) {
            if (!(await userOwnsThread(user.id, route.threadId))) {
              throw new Response("Forbidden", { status: 403 });
            }
            return;
          }
    
          // agent/run and agent/connect carry the thread in the body instead.
          if (route.method === "agent/run" || route.method === "agent/connect") {
            // Clone: the handler still needs to read the original body.
            const { threadId } = await request.clone().json();
            if (threadId && !(await userOwnsThread(user.id, threadId))) {
              throw new Response("Forbidden", { status: 403 });
            }
          }
        },
      },
    });

`route.threadId` is present on `agent/stop`, `threads/messages`, `threads/events`, `threads/state`, `threads/update` and `threads/archive`. `threads/list`, `threads/clear` and `threads/subscribe` carry no thread at all, so the only decision available for those three is whether to allow them.

See [Auth](https://docs.copilotkit.ai/llamaindex/auth) for the full authentication guide and [Thread authorization](https://docs.copilotkit.ai/llamaindex/auth#thread-authorization) for the ownership map this example assumes.

For Inspector metadata, Core sends these current browser-to-runtime headers and fetch credentials on the optional request. The Runtime then starts a separate server-to-Intelligence request with only its configured Intelligence API key.

## Connect route 404 on a fresh thread#

A frequent self-hosting symptom is a `404` from the `POST /agent/:agentId/connect` route right after the page loads, before the user has sent a single message. This usually means one of two things:

  1. **The`agentId` in the URL isn't registered.** The runtime returns `{"error":"Agent not found","message":"Agent '<id>' does not exist"}` with a `404` when no agent matches. The prebuilt components default to the agent named `"default"`, so register one under that key (or pass an explicit `agentId`).
  2. **`connect()` is called before any `run()` for an auto-minted thread.** Some persistence backends only know about a thread once a run has produced events. See the [AgentRunner](https://docs.copilotkit.ai/llamaindex/backend/agent-runner) guide and the [`/connect` 404 troubleshooting entry](https://docs.copilotkit.ai/llamaindex/troubleshooting/common-issues#connect-route-returns-404-on-a-fresh-thread).



## Related#

  * [Copilot Runtime](https://docs.copilotkit.ai/llamaindex/backend/copilot-runtime): setting up the runtime and adapters.
  * [AgentRunner](https://docs.copilotkit.ai/llamaindex/backend/agent-runner): the persistence abstraction behind `run`/`connect`/`stop`.
  * [Connect AG-UI agents](https://docs.copilotkit.ai/llamaindex/backend/ag-ui): how the frontend proxy maps onto these routes.
  * [Error Debugging](https://docs.copilotkit.ai/llamaindex/troubleshooting/error-debugging): the `onError` codes that map to these routes.
  * [Inspector](https://docs.copilotkit.ai/llamaindex/inspector): how trusted project context and license-aware actions appear in the Inspector.



### On this page

Provider and handler pairsWhich handlers serve which modeMulti-route mode (default)Run and connect with IntelligenceInspector metadataThread routesProbing the runtime with curlEnable AG-UI Streams routesStart with your coding agentChoose a Runtime route modeConstruct the Intelligence clientIdentify the signed-in application userMount the Runtime handlerVerify the advertised capabilitiesSingle-route modeCORSAuthenticating requestsConnect route 404 on a fresh threadRelated
