---
url: https://docs.copilotkit.ai/agno/auth/
title: Authentication
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:46:13.807081+00:00
---

# Authentication

> Source: https://docs.copilotkit.ai/agno/auth/

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

[Open-source telemetry](https://docs.copilotkit.ai/agno/telemetry)[Community frameworks](https://docs.copilotkit.ai/agno/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[Agno](https://docs.copilotkit.ai/agno)

# Authentication

Pass user auth context from your frontend to the agent so it can scope tools, data, and decisions to the signed-in user.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

auth-banner.tsx

use-demo-auth.ts

demo-token.ts

route.ts
    
    
    "use client";// Auth demo — framework-native request authentication via the V2 runtime's// `onRequest` hook. The runtime route (/api/copilotkit-auth) rejects any// request whose `Authorization: Bearer <demo-token>` header is missing or// wrong.//// UX shape: the demo defaults to UNAUTHENTICATED on first paint so visitors// land on a clear sign-in card. We don't render `<CopilotKit>` until the user// has signed in at least once — that sidesteps the transport 401 that would// otherwise crash `<CopilotChat>` during its initial `/info` handshake.// After the user signs in once, `<CopilotKit>` stays mounted across the// sign-out → sign-in cycle so the post-sign-out state can actually// demonstrate the runtime rejecting unauthenticated requests in the chat// surface (the whole point of the demo).//// Error surfacing: the post-sign-out 401 is captured via the AGENT-SCOPED// `<CopilotChat onError>` channel, NOT the provider-level `<CopilotKit// onError>` alone. Agent-run errors (`agent_run_failed`) are reliably// delivered to the chat-scoped subscription, whereas the provider-level// handler does not fire for them in this flow — so a demo that relies only// on `<CopilotKit onError>` never renders the rejection banner. We register// the same handler on BOTH channels: `<CopilotKit onError>` covers any// provider-level errors (e.g. the initial `/info` handshake) and// `<CopilotChat onError>` covers agent-run rejections, which is what the// sign-out path produces.import { useCallback, useEffect, useMemo, useState } from "react";import {  CopilotKit,  CopilotChat,  type CopilotKitCoreErrorCode,} from "@copilotkit/react-core/v2";import { AuthBanner } from "./auth-banner";import { SignInCard } from "./sign-in-card";import { useDemoAuth } from "./use-demo-auth";import { DEMO_TOKEN } from "./demo-token";interface AuthDemoErrorState {  message: string;  code: CopilotKitCoreErrorCode | string;}interface AuthErrorEvent {  error?: { message?: string } | null;  code: CopilotKitCoreErrorCode;}export default function AuthDemoPage() {  const {    isAuthenticated,    authorizationHeader,    hasEverSignedIn,    signIn,    signOut,  } = useDemoAuth();  const headers = useMemo<Record<string, string>>(    () => (authorizationHeader ? { Authorization: authorizationHeader } : {}),    [authorizationHeader],  );  const [authError, setAuthError] = useState<AuthDemoErrorState | null>(null);  // Shared error handler wired to BOTH the provider-level and chat-level  // `onError` channels (see the file header for why both are needed).  const handleAuthError = useCallback((event: AuthErrorEvent) => {    setAuthError({      message:        (event.error?.message && event.error.message.trim()) ||        (event.code          ? `Request rejected (${event.code})`          : "The request was rejected."),      code: event.code,    });  }, []);  // Clear stale errors as soon as the user re-authenticates. This is the  // ONLY thing that gates the amber error surface on auth state — the render  // condition below keys off `authError` alone. Coupling the render to a  // second `!isAuthenticated` slice (the obvious-but-wrong guard) created a  // post-sign-out race: the rejection's `onError` fires and calls  // `setAuthError`, but if that commit landed in a render where the auth  // state hadn't yet settled to false, `authError && !isAuthenticated`  // evaluated false and the banner never appeared. Driving the surface off  // `authError` and clearing it here on re-auth removes the cross-slice  // ordering dependency: a rejection always renders, and signing back in  // always wipes it.  useEffect(() => {    if (isAuthenticated) setAuthError(null);  }, [isAuthenticated]);  if (!hasEverSignedIn) {    return (      <div className="flex h-screen flex-col">        <SignInCard onSignIn={signIn} />      </div>    );  }  return (    // `useSingleEndpoint={false}` opts into the V2 multi-endpoint protocol    // (separate /info, /agents/<id>/run, etc.), which is what this demo's    // runtime route is wired up for.    <CopilotKit      runtimeUrl="/api/copilotkit-auth"      agent="auth-demo"      headers={headers}      useSingleEndpoint={false}      onError={handleAuthError}    >      <div className="flex h-screen flex-col gap-3 p-6">        <AuthBanner          authenticated={isAuthenticated}          onSignOut={signOut}          onSignIn={() => signIn(DEMO_TOKEN)}        />        <header>          <h1 className="text-lg font-semibold">Authentication</h1>        </header>        {authError && (          <div            data-testid="auth-demo-error"            className="rounded-md border border-amber-300 bg-amber-50 px-3 py-2 text-sm text-amber-900"          >            <strong className="font-semibold">              Runtime rejected the request:            </strong>{" "}            <span data-testid="auth-demo-error-message">              {authError.message}            </span>{" "}            <code className="ml-1 rounded bg-amber-100 px-1 py-0.5 font-mono text-xs">              {authError.code}            </code>          </div>        )}        <div className="flex-1 overflow-hidden rounded-md border border-neutral-200">          <CopilotChat            agentId="auth-demo"            className="h-full"            onError={handleAuthError}          />        </div>      </div>    </CopilotKit>  );}

You have a chat surface or a hook driving an agent and you want every agent run to know _who_ the request came from. By the end of this guide, your frontend will forward a token, the runtime will pass it through, and your agent code will read the resulting user info on every turn.

## When to use this#

  * **Multi-tenant apps** where the agent reads or writes per-user data.
  * **Tool gating** where some tools should only run for authorised users.
  * **Audit and billing** where every run needs an identity to attribute it to.
  * **Session-aware UX** where the agent's behaviour depends on the user's role or permissions.



If you run the TypeScript runtime without Intelligence and do not need any of those, your agent can run anonymously. Intelligence runtimes require a trusted application-user identity for protected web requests.

Runtime authentication APIs

The runtime hooks on this page use the TypeScript API. Python, Go, Ruby, and C#/.NET use their host's request and authentication APIs; follow their [Intelligence setup examples](https://docs.copilotkit.ai/agno/intelligence/quickstart#connect-your-runtime). In every language, resolve the user from a verified session or token and keep the Intelligence API key on the server.

## Frontend#

Pass your token via the `headers` prop on `<CopilotKit>`. CopilotKit forwards every request with that header attached.

frontend/src/app/page.tsx
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit
      runtimeUrl="/api/copilotkit"
      headers={{
        Authorization: `Bearer ${userToken}`,
      }}
      useSingleEndpoint={false}
    >
      <YourApp />
    </CopilotKit>

About the explicit useSingleEndpoint

The `createCopilotRuntimeHandler` route below serves multi-route, the default. `<CopilotKitProvider>` negotiates the transport when the prop is omitted, but every released `<CopilotKit>` still pins it to `true` internally — which selects the single-route transport and 404s against this route. Keep the `{false}`. See [Provider and handler pairs](https://docs.copilotkit.ai/agno/backend/runtime-endpoints#provider-and-handler-pairs).

## Backend#

Wire authentication into the V2 runtime via the `onRequest` hook. The hook runs before any agent code and operates on the raw `Request`, so it's the right place to read the `Authorization` header, run your verifier, and either let the request through or short-circuit with a 401:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import type { NextRequest } from "next/server";
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    
    const runtime = new CopilotRuntime({ agents: { default: myAgent } });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      hooks: {
        onRequest: ({ request }) => {
          const authHeader = request.headers.get("authorization");
          if (!authHeader?.startsWith("Bearer ")) {
            throw new Response(
              JSON.stringify({ error: "unauthorized" }),
              { status: 401, headers: { "content-type": "application/json" } },
            );
          }
          const token = authHeader.slice("Bearer ".length);
          const user = verifyJwt(token); // your validation
          // attach user to request-scoped context here
        },
      },
    });
    
    export const POST = (req: NextRequest) => handler(req);
    export const GET = (req: NextRequest) => handler(req);
    export const PATCH = (req: NextRequest) => handler(req);
    export const DELETE = (req: NextRequest) => handler(req);

> The V1 Next.js adapter (`copilotRuntimeNextJSAppRouterEndpoint`) does not forward the `hooks` option. Use `createCopilotRuntimeHandler` from `@copilotkit/runtime/v2` directly when you need the `onRequest` gate.

## Tool gating#

The most common reason to wire auth is so individual tools can decline to run. Read the resolved user inside the tool's handler and bail if the role doesn't match:
    
    
    def delete_record(record_id: str, *, user: User):
        if "admin" not in user.permissions:
            raise PermissionError("admin role required")
        # do the delete

This composes with [Human in the loop](https://docs.copilotkit.ai/agno/human-in-the-loop): gate on auth first, surface a confirmation card next, execute last.

## Thread authorization#

Verifying _who_ the caller is doesn't yet stop them reaching _someone else's conversation_. How much of that you have to build depends on which runtime you're running.

Runtime| Who scopes threads to a user  
---|---  
`CopilotRuntime` with `intelligence`| Mostly the runtime, via `identifyUser` — with three routes you still have to guard.  
Anything else — SSE runtime, custom store, local in-memory runner| You do. See Scope threads yourself.  
  
### CopilotKit Intelligence scopes most thread routes#

The Intelligence runtime requires an `identifyUser` callback — construction throws without one (or without at least one Channel). It runs on the server, once per request, and the id it returns is the scope the runtime hands to the platform. (`intelligence` below is a `CopilotKitIntelligence` instance; [Connect your runtime to Intelligence](https://docs.copilotkit.ai/agno/intelligence/quickstart) covers building it.)

app/api/copilotkit/[[...slug]]/route.ts
    
    
    const runtime = new CopilotRuntime({
      agents: { default: agent },
      intelligence,
      identifyUser: async (request) => {
        const session = await verifyAppSession(request); // Your server-side auth.
        if (!session?.user) throw new Error("Unauthorized"); // Backstop; see below.
    
        return { id: session.user.id, name: session.user.name };
      },
    });

`identifyUser` is not an authentication gate

Most routes resolve the caller through `identifyUser`, but **not all of them do** — and the ones that don't never invoke your callback at all. Rejecting unauthenticated requests is `onRequest`'s job: it runs before routing, on every route, without exception. Treat `identifyUser` as the thing that _names_ an already-authenticated caller, never as the thing that decides whether a caller gets in.

Where a route does resolve the caller, what matters next is whether that id is actually _carried to the platform_ as a scope:

Route| Scoped to the resolved user?  
---|---  
`agent/run`, `agent/connect`| Yes  
`threads/list`| Yes — and filtered by `agentId`, so `useThreads` returns the caller's threads rather than the project's  
`threads/messages`| Yes  
`threads/update` (rename via `PATCH`, delete via `DELETE`), `threads/archive`| Yes  
Thread subscription token| Yes  
`threads/events`, `threads/state`| **No** — resolves the caller, then ignores it  
`agent/stop`| Yes — the thread is fetched as the caller before the run is aborted  
  
Two routes are not user-scoped

**`threads/events` and `threads/state`** back the [inspector](https://docs.copilotkit.ai/agno/inspector). Both resolve the caller and then discard the result, reading the thread by id alone — the runtime calls the platform's project-authenticated `_inspect` endpoints, which take no user parameter. Any caller can read the full event log and current agent state of any thread in the project, given its `threadId`.

Guard both yourself. The `onBeforeHandler` pattern below applies on the CopilotKit Intelligence path too, narrowed to these routes:
    
    
    onBeforeHandler: async ({ request, route }) => {
      // Switch rather than an array `includes`, so `route` narrows and
      // `route.threadId` type-checks — both variants carry one.
      switch (route.method) {
        case "threads/events":
        case "threads/state":
          break;
        default:
          return;
      }
    
      // None of these is scoped platform-side; check your own ownership record.
      const user = await verifyRequest(request);
      if (!(await userOwnsThread(user.id, route.threadId))) {
        throw new Response("Not found", { status: 404 });
      }
    },

Without an ownership record of your own, reject these routes outright rather than leaving them open.

For everything in the Yes rows there is no ownership table to build. What you own is `identifyUser` itself:

  * **Derive the id from a server-verified credential.** The callback receives the raw `Request`; whatever it returns is trusted from there on. Reading a user id straight out of a header or request body hands every caller the ability to name themselves.
  * **Return a stable id.** It is the key threads hang off. Change it — swapping an email for a subject claim, say — and that user's existing threads stop resolving.
  * **Send the`401` from `onRequest`.** Beyond the status codes being wrong — an `identifyUser` that throws surfaces as a `500`, a malformed id as a `400` — routes like `transcribe` and `agent/suggest` never call it, so a check placed only here isn't reached on every request. Authenticate in `onRequest`, which runs on every route and can throw a `Response` directly, and keep the throw inside `identifyUser` as a backstop.



A static `identifyUser` value is suitable only for a single-user demo. In a multi-user application every request must resolve the authenticated user, or those users share one thread scope.

See [Scope AG-UI Streams to the signed-in user](https://docs.copilotkit.ai/agno/threads-lifecycle#scope-rich-threads-to-the-signed-in-user) for the full runtime contract.

### Scope threads yourself#

Without CopilotKit Intelligence there is no server-side binding between a `threadId` and a user. A `threadId` is just an opaque id travelling in a request: if user A learns user B's, every thread route accepts it. The rest of this section is the pattern for a custom store, a plain SSE runtime, or the local in-memory runner — and it's also what you narrow to `threads/events` and `threads/state` if you _are_ on the platform.

The default `InMemoryAgentRunner` is the plainest case. It holds threads in a process-global map keyed by `threadId` with no owner field, so every [thread route](https://docs.copilotkit.ai/agno/backend/runtime-endpoints#thread-routes) answers for any id it is handed: `GET /threads` lists every thread in the process, and `GET /threads/:threadId/messages` returns that thread's history to whoever asks. Anything extending it, such as `AgentCoreRunner`, inherits the same store. `SqliteAgentRunner` does not serve them at all: its read routes answer `422`. A runner swap is therefore a fix for durability, not for thread authorization.

#### Own the mapping

Whatever stores your threads, keep a record of who each one belongs to. The minimum is a table your runtime can query:
    
    
    create table thread_owners (
      thread_id text primary key,
      user_id   text not null
    );
    create index on thread_owners (user_id);

Write a row when a conversation is first created — see [minting a thread with your own API](https://docs.copilotkit.ai/agno/threads-lifecycle#creating-a-thread-with-your-own-api-on-the-first-message) for where that hooks into the chat lifecycle.

#### Enforce it in `onBeforeHandler`

`onRequest` runs before routing, so it can't see which thread is being addressed. `onBeforeHandler` runs after, and receives a `route` that names the operation and — for thread-scoped routes — the `threadId`:
    
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
      hooks: {
        onRequest: async ({ request }) => {
          // Authenticate first: reject anonymous callers outright.
          const user = await verifyRequest(request);
          if (!user) throw new Response("Unauthorized", { status: 401 });
        },
    
        onBeforeHandler: async ({ request, route }) => {
          const user = await verifyRequest(request);
    
          // Routes that name a thread directly.
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

The routes that carry a `threadId` on `route` are `agent/stop`, `threads/update`, `threads/archive`, `threads/messages`, `threads/events`, and `threads/state`.

A thread id is not a secret

Treat `threadId` as a public identifier, like a database primary key in a URL. It travels through the browser, appears in logs, and is trivially enumerable if you mint sequential ids. Authorization has to be an explicit ownership check — never "they knew the id, so they must own it". Minting UUIDs makes guessing impractical but is not itself a control.

#### Filter the thread list

`threads/list` has no `threadId` to check, so `onBeforeHandler` has nothing to authorize against. Off the platform the route returns whatever the configured store holds — the local in-memory runner filters by `agentId` only, and a custom store returns exactly what you wrote. Build the list from your own ownership table instead, and drive the chat with the selected id.

Filter server-side. Hiding rows in the UI leaves the underlying route open.

`threads/clear` is the other route with no `threadId` on `route`. On the in-memory runner it wipes every thread in the process and returns `204`, so the only decision `onBeforeHandler` can make is whether to allow the call. With more than one user on the deployment, reject it unless the caller is an operator.

With no platform thread store, the ownership table above _is_ your thread list.

## Security checklist#

  * **Always validate** the token on the backend. Never trust the frontend's claim.
  * **Scope every read and write** to the resolved user. Auth context only matters if you actually use it to filter data.
  * **Authenticate in`onRequest`.** It is the only hook that runs on every route. `identifyUser` names a caller; it does not gate one, and some routes never invoke it.
  * **Bind threads to a user.** On CopilotKit Intelligence that means a correct `identifyUser`, plus your own guard on `threads/events` and `threads/state`; off it, an ownership check on every thread route rather than only at login. See Thread authorization.
  * **Don't log raw tokens.** Log the resolved user id (or `anonymous`) instead.
  * **Use HTTPS in production.** The Bearer token is sensitive.
  * **Refresh strategy.** Your frontend is responsible for rotating expired tokens before they reach the agent. CopilotKit doesn't refresh on your behalf.



### On this page

When to use thisFrontendBackendTool gatingThread authorizationCopilotKit Intelligence scopes most thread routesScope threads yourselfSecurity checklist
