---
url: https://docs.copilotkit.ai/mastra/intelligence/quickstart/
title: Connect Intelligence in 5 minutes
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:16:50.257484+00:00
---

# Connect Intelligence in 5 minutes

> Source: https://docs.copilotkit.ai/mastra/intelligence/quickstart/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/mastra)[Quickstart](https://docs.copilotkit.ai/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/mastra/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/mastra/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/mastra/intelligence/overview)

Get started

[Quickstart](https://docs.copilotkit.ai/mastra/intelligence/quickstart)[Architecture](https://docs.copilotkit.ai/mastra/intelligence/intelligence-platform)[Plans](https://docs.copilotkit.ai/mastra/intelligence/plans)

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/mastra/learning)

[User Memories](https://docs.copilotkit.ai/mastra/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/mastra/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Quickstart

IntelligenceGet started

# Connect Intelligence in 5 minutes

Connect an existing CopilotKit app to Intelligence and store persistent threads in a cloud-hosted project.

## Overview#

You want AG-UI Streams, User Memory, Automatic Learning, Channels, and Product Analytics on the app you already have. Intelligence adds that layer. Your frontend and your agent stay where they are.

Keep your existing thread storage and native persistence configured. Intelligence automatically records its own copy of supported AG-UI interaction history as conversations run through the connected runtime. See [what Intelligence records](https://docs.copilotkit.ai/mastra/intelligence/bring-your-own-thread-system#how-recording-works) and the [existing LangGraph app example](https://docs.copilotkit.ai/mastra/intelligence/bring-your-own-thread-system#example-keep-an-existing-langgraph-conversation).

You are done when Inspector shows that Intelligence is connected and shows your first saved thread. A React Native app has no Inspector. Confirm the thread in the cloud-hosted project instead.

TypeScript is the default and most fully featured runtime. It can run with or without Intelligence. Python, Go, Ruby, and C#/.NET runtimes require Intelligence, either cloud-hosted or self-hosted. Pick the language of your **runtime server** below; your agent framework and frontend stay the same.

## Start with your coding agent#

Use this prompt to set up Intelligence in a new or existing app. Tell your coding agent which runtime language, agent framework, and frontend you want to use.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Set it up manually#

Before you start, have a working CopilotKit frontend and agent. The TypeScript tab connects your existing runtime; the other tabs mount a native runtime in front of an agent that already serves AG-UI over HTTP. Use your agent's AG-UI URL, not the CopilotKit runtime URL.

### Select an Intelligence project#

Sign in from your app directory. Then select the project that will store your threads.

Terminal
    
    
    npx copilotkit@latest login
    npx copilotkit@latest project select

`project select` creates a project API key and writes it to `.env` as `CPK_INTELLIGENCE_API_KEY`. Put that key in the environment of the process that runs your CopilotKit runtime. The command output does not print the key. Read it from `.env`.

.env
    
    
    CPK_INTELLIGENCE_API_KEY=cpk-...

The CLI writes `.env` in the directory where you run the command. If your runtime process loads a different file, copy the key into that file. A value that the host already sets stays as it is.

Keep the key on the server. Do not put it in a variable that the frontend build sends to the browser.

### Connect your runtime#

Choose your runtime language. The selection also applies to the self-hosted settings below. These examples use multi-route HTTP endpoints in every language.

TypeScriptPythonGoRubyC#/.NET

Keep your existing TypeScript runtime and agent registration. Install the current package if you have not already:
    
    
    npm install @copilotkit/runtime

Add an Intelligence client. The client is the same for every agent framework.

Your CopilotKit runtime
    
    
    import {
      CopilotKitIntelligence,
      CopilotRuntime,
    } from "@copilotkit/runtime/v2";
    
    // Create the Intelligence client with your project API key. Keep this key on the server.
    const intelligence = new CopilotKitIntelligence({
      apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
    });
    
    const runtime = new CopilotRuntime({
      agents,
      // Pass the Intelligence client to the runtime
      intelligence,
      // Identify the user from a verified session or token
      identifyUser: async (request) => {
        const user = await authenticateApplicationUser(request);
        if (!user) throw new Error("Unauthorized");
        return { id: user.id, name: user.name };
      },
    });

Use your existing authentication

`authenticateApplicationUser` represents your server-side authentication function. It must return the user from a verified session or token. The Runtime requires `identifyUser` to associate web threads with that user.

If no trusted user identity exists, add authentication before you continue. A fixed identity is suitable only for a local, single-user demo.

Protect every Runtime route before production

`identifyUser` names the caller, but it is not an authentication gate. Use the handler's `onRequest` hook to reject unauthenticated requests. You must also enforce thread ownership for `threads/events`, `threads/state`, and `agent/stop`. Follow the [thread authorization guide](https://docs.copilotkit.ai/mastra/auth#thread-authorization) for the complete pattern.

A web runtime requires `identifyUser`. A Channels-only runtime has no web surface. Pass a non-empty `channels` array instead.

The runtime reads the key from the client you pass. It does not read the key from the environment on its own. `apiKey` is the only required field. You do not pass an organization id or a project id.

#### An existing runtime that already has a runner

An open-source runtime often passes `runner`. That option chooses where runs are stored. Intelligence stores the runs itself. Remove `runner` when you add `intelligence`.
    
    
    const runtime = new CopilotRuntime({
      agents,
      runner: new InMemoryAgentRunner(), 
      intelligence, 
      identifyUser,
    });

TypeScript rejects both options together. A JavaScript runtime throws this error:
    
    
    Intelligence Runtime auto-wires its own `runner`; passing `runner` alongside
    `intelligence` is not supported.

You can keep `runner` and omit `intelligence`. The runtime then stays in SSE mode, and Threads in Inspector stay locked. See [AgentRunner and persistence](https://docs.copilotkit.ai/mastra/backend/agent-runner).

#### Mount the TypeScript handler

Create one handler and mount it for all runtime subpaths and HTTP methods in the server you already use. For Next.js, use a catch-all route:

app/api/copilotkit/[[...slug]]/route.ts
    
    
    import { createCopilotRuntimeHandler } from "@copilotkit/runtime/v2";
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;
    export const PATCH = handler;
    export const DELETE = handler;

Use this handler in the same module as the configured `runtime` above. It accepts a Web `Request` and returns a Web `Response`. For Express, Hono, and other hosts, use the [TypeScript server adapter guide](https://docs.copilotkit.ai/mastra/runtime-server-adapter).

TypeScript also supports `mode: "single-route"`. If your existing app uses that mode, keep its single POST route and matching frontend transport. That option does not apply to the other runtime languages.

Use Python 3.11 or later. Install the [Python runtime](https://pypi.org/project/copilotkit-intelligence-runtime/) and Uvicorn in your application's virtual environment:
    
    
    python -m pip install copilotkit-intelligence-runtime==0.1.0 uvicorn

Set these variables in the server environment. `AG_UI_AGENT_URL` must point to a running AG-UI endpoint that accepts run requests and streams events:
    
    
    export CPK_INTELLIGENCE_API_KEY="your-project-api-key"
    export AG_UI_AGENT_URL="http://localhost:8001/agent"
    export APP_AUTH_TOKEN="replace-with-a-random-local-development-token"
    export APP_USER_ID="local-user"

This local example verifies one application token and maps it to a server-owned user ID. Use a different value for the application token and the Intelligence API key. For production, replace this lookup with your application's verified session or token lookup; never trust a user ID supplied by the browser.

Save this as `app.py`:
    
    
    import hmac
    import os
    
    from starlette.requests import Request
    from copilotkit_runtime import HttpAgent, IntelligenceRuntime, RuntimeConfig, User
    
    app_token = os.environ["APP_AUTH_TOKEN"]
    user_id = os.environ["APP_USER_ID"]
    if not app_token or not user_id:
        raise ValueError("APP_AUTH_TOKEN and APP_USER_ID must not be empty")
    
    
    async def identify_user(request: Request) -> User | None:
        supplied = request.headers.get("authorization", "").encode()
        expected = f"Bearer {app_token}".encode()
        if not hmac.compare_digest(supplied, expected):
            return None
        return User(id=user_id)
    
    
    app = IntelligenceRuntime(
        RuntimeConfig(
            api_key=os.environ["CPK_INTELLIGENCE_API_KEY"],
            base_path="/api/copilotkit",
            allowed_origins=("http://localhost:3000",),
        ),
        agents={"default": HttpAgent(os.environ["AG_UI_AGENT_URL"])},
        identify_user=identify_user,
    )

Start the server:
    
    
    python -m uvicorn app:app --host 127.0.0.1 --port 8200

The multi-route runtime URL is `http://localhost:8200/api/copilotkit`. Send `Authorization: Bearer <APP_AUTH_TOKEN>` with frontend requests. Keep `CPK_INTELLIGENCE_API_KEY` on the server. The CORS configuration allows a frontend at `http://localhost:3000`; replace that origin for your deployment.

Uvicorn runs the ASGI lifespan, which closes the runtime on shutdown. If you mount it inside a host that manages lifespan separately, call `await app.aclose()` from that host's shutdown handler. `HttpAgent` does not forward browser credentials; configure its `headers` explicitly if your agent requires authentication.

Use Go 1.22 or later. In a new application directory, install the [Go runtime module](https://pkg.go.dev/github.com/CopilotKit/CopilotKit/packages/runtime-go):
    
    
    go mod init example.com/copilotkit-app
    go get github.com/CopilotKit/CopilotKit/packages/runtime-go@v0.0.0-20260930161409-37b078290a51

Set these variables in the server environment. Start your AG-UI agent at `AG_UI_AGENT_URL` before sending a message:
    
    
    export CPK_INTELLIGENCE_API_KEY="your-project-api-key"
    export AG_UI_AGENT_URL="http://localhost:8001/agent"
    export APP_AUTH_TOKEN="replace-with-a-random-local-development-token"
    export APP_USER_ID="local-user"

This local example verifies one application token and maps it to a server-owned user ID. Use a different value for the application token and the Intelligence API key. In production, replace the callback with your application's verified session or token lookup. Never use an unverified browser-supplied user ID.

Save this as `main.go`:
    
    
    package main
    
    import (
        "context"
        "crypto/subtle"
        "errors"
        "log"
        "net/http"
        "os"
        "os/signal"
        "syscall"
        "time"
    
        copilotkit "github.com/CopilotKit/CopilotKit/packages/runtime-go"
    )
    
    func required(name string) string {
        value := os.Getenv(name)
        if value == "" {
            log.Fatalf("Missing environment variable: %s", name)
        }
        return value
    }
    
    func main() {
        token, userID := required("APP_AUTH_TOKEN"), required("APP_USER_ID")
        rt, err := copilotkit.New(copilotkit.Config{
            APIKey: required("CPK_INTELLIGENCE_API_KEY"),
            BasePath: "/api/copilotkit",
            AllowedOrigins: []string{"http://localhost:3000"},
            Agents: map[string]copilotkit.Agent{
                "default": &copilotkit.HTTPAgent{URL: required("AG_UI_AGENT_URL")},
            },
            IdentifyUser: func(r *http.Request) (copilotkit.User, error) {
                if subtle.ConstantTimeCompare(
                    []byte(r.Header.Get("Authorization")), []byte("Bearer "+token),
                ) != 1 {
                    return copilotkit.User{}, errors.New("unauthorized")
                }
                return copilotkit.User{ID: userID, Name: "Local user"}, nil
            },
        })
        if err != nil {
            log.Fatal(err)
        }
        defer func() {
            if err := rt.Close(); err != nil {
                log.Printf("Runtime shutdown: %v", err)
            }
        }()
    
        mux := http.NewServeMux()
        mux.Handle("/api/copilotkit/", rt)
        server := &http.Server{Addr: "127.0.0.1:8200", Handler: mux, ReadHeaderTimeout: 10 * time.Second}
        stopped, stop := signal.NotifyContext(context.Background(), os.Interrupt, syscall.SIGTERM)
        defer stop()
        serverErrors := make(chan error, 1)
        go func() { serverErrors <- server.ListenAndServe() }()
        select {
        case <-stopped.Done():
        case err := <-serverErrors:
            if !errors.Is(err, http.ErrServerClosed) {
                log.Printf("HTTP server: %v", err)
            }
        }
        ctx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
        defer cancel()
        if err := server.Shutdown(ctx); err != nil {
            log.Printf("HTTP shutdown: %v", err)
        }
    }

Run `go run .`. The multi-route runtime URL is `http://localhost:8200/api/copilotkit`. Send `Authorization: Bearer <APP_AUTH_TOKEN>` with frontend requests; keep `CPK_INTELLIGENCE_API_KEY` on the server. Replace the allowed `http://localhost:3000` origin for your deployment.

The server drains HTTP requests on shutdown, then `rt.Close()` cancels agent work and drains runtime resources. `HTTPAgent.Headers` lets you supply server-owned credentials for a protected agent endpoint; browser credentials are not forwarded.

This Rack example uses Ruby 3.1 or later and the [Ruby runtime gem](https://rubygems.org/gems/copilotkit-runtime). Add this `Gemfile`, then run `bundle install`:
    
    
    source 'https://rubygems.org'
    gem 'copilotkit-runtime', '0.1.0.rc.1'
    gem 'rack', '~> 3.1'
    gem 'rackup', '~> 2.2'
    gem 'puma', '~> 6.0'

Set these variables in the server environment. Start your AG-UI agent at `AG_UI_AGENT_URL` before sending a message:
    
    
    export CPK_INTELLIGENCE_API_KEY="your-project-api-key"
    export AG_UI_AGENT_URL="http://localhost:8001/agent"
    export APP_AUTH_TOKEN="replace-with-a-random-local-development-token"
    export APP_USER_ID="local-user"

This local example verifies one application token and maps it to a server-owned user ID. Use a different value for the application token and the Intelligence API key. In production, replace the lookup with your application's verified session or token lookup. Never trust a browser-supplied user ID.

Save this as `config.ru`:
    
    
    require 'rack'
    require 'copilotkit/runtime'
    
    token = ENV.fetch('APP_AUTH_TOKEN')
    user_id = ENV.fetch('APP_USER_ID')
    raise 'APP_AUTH_TOKEN and APP_USER_ID must not be empty' if token.empty? || user_id.empty?
    
    runtime = CopilotKit::Runtime.new(
      api_key: ENV.fetch('CPK_INTELLIGENCE_API_KEY'),
      agents: {
        'default' => CopilotKit::HttpAgent.new(url: ENV.fetch('AG_UI_AGENT_URL'))
      },
      cors_origins: ['http://localhost:3000'],
    identify_user: lambda do |env|
        supplied = env.fetch('HTTP_AUTHORIZATION', '')
        if Rack::Utils.secure_compare(supplied, "Bearer #{token}")
          { id: user_id }
        end
      end
    )
    
    at_exit { runtime.close(timeout: 10) }
    
    map '/api/copilotkit' do
      run runtime
    end

Start a single-process server:
    
    
    bundle exec puma config.ru --bind tcp://127.0.0.1:8200 --workers 0

The multi-route runtime URL is `http://localhost:8200/api/copilotkit`. Rack strips the mount prefix, so leave the runtime's `base_path` at its empty default. Send `Authorization: Bearer <APP_AUTH_TOKEN>` with frontend requests, and keep `CPK_INTELLIGENCE_API_KEY` on the server. Replace the allowed `http://localhost:3000` origin for your deployment.

The exit handler closes this single-process runtime. For a worker-based deployment, create one runtime after each worker forks and call `runtime.close(timeout: 10)` from its worker shutdown hook. `HttpAgent` accepts a `headers:` hash for server-owned agent credentials; it does not forward browser credentials.

Use the .NET 8 SDK. Create an ASP.NET Core application and install the [runtime package](https://www.nuget.org/packages/CopilotKit.Intelligence.Runtime):
    
    
    dotnet new web --framework net8.0 --name CopilotKitApp
    cd CopilotKitApp
    dotnet add package CopilotKit.Intelligence.Runtime --version 0.1.0-rc.1

Set these variables in the server environment. Start your AG-UI agent at `AG_UI_AGENT_URL` before sending a message:
    
    
    export CPK_INTELLIGENCE_API_KEY="your-project-api-key"
    export AG_UI_AGENT_URL="http://localhost:8001/agent"
    export APP_AUTH_TOKEN="replace-with-a-random-local-development-token"
    export APP_USER_ID="local-user"

This local example verifies one application token and maps it to a server-owned user ID. Use a different value for the application token and the Intelligence API key. In production, replace `IdentifyUser` with your application's verified session or token lookup. Never trust a browser-supplied user ID.

Replace `Program.cs` with:
    
    
    using System.Security.Cryptography;
    using System.Text;
    using CopilotKit.Intelligence;
    
    static string Required(string name) =>
        Environment.GetEnvironmentVariable(name) is { Length: > 0 } value
            ? value : throw new InvalidOperationException($"Missing {name}");
    
    var token = Required("APP_AUTH_TOKEN");
    var userId = Required("APP_USER_ID");
    var expected = Encoding.UTF8.GetBytes($"Bearer {token}");
    using var agentClient = new HttpClient(new SocketsHttpHandler
    {
        PooledConnectionLifetime = TimeSpan.FromMinutes(2)
    }) { Timeout = Timeout.InfiniteTimeSpan };
    
    var builder = WebApplication.CreateBuilder(args);
    builder.Services.AddSingleton<IntelligenceRuntime>(_ => new IntelligenceRuntime(
        new RuntimeOptions
        {
            ApiKey = Required("CPK_INTELLIGENCE_API_KEY"),
            AllowedOrigins = new HashSet<string> { "http://localhost:3000" },
            Agents = new Dictionary<string, IRuntimeAgent>
            {
                ["default"] = new HttpAgent(new Uri(Required("AG_UI_AGENT_URL")), agentClient)
            },
            IdentifyUser = (context, cancellationToken) =>
            {
                cancellationToken.ThrowIfCancellationRequested();
                var supplied = Encoding.UTF8.GetBytes(context.Request.Headers.Authorization.ToString());
                RuntimeUser? user = CryptographicOperations.FixedTimeEquals(supplied, expected)
                    ? new RuntimeUser(userId) : null;
                return ValueTask.FromResult(user);
            }
        }));
    
    await using var app = builder.Build();
    app.Services.GetRequiredService<IntelligenceRuntime>().Map(app, "/api/copilotkit");
    await app.RunAsync("http://127.0.0.1:8200");

Run `dotnet run --no-launch-profile`. The multi-route runtime URL is `http://localhost:8200/api/copilotkit`. Send `Authorization: Bearer <APP_AUTH_TOKEN>` with frontend requests, and keep `CPK_INTELLIGENCE_API_KEY` on the server. Replace the allowed `http://localhost:3000` origin for your deployment.

ASP.NET Core disposes the singleton runtime asynchronously when the host shuts down. The application then disposes its agent HTTP client. `HttpAgent` accepts an optional `headers` dictionary for server-owned agent credentials; it does not forward browser credentials.

### Connect your frontend#

Point your frontend provider at the runtime base path. Use `/api/copilotkit` if your frontend proxies that path to the runtime. For a separate local server, use `http://localhost:8200/api/copilotkit` and allow your frontend's exact origin in the runtime's CORS configuration.

Keep your existing application authentication headers or session. The examples below connect to a TypeScript runtime. For a Python, Go, Ruby, or C#/.NET runtime from the tabs above, use `http://localhost:8200/api/copilotkit` and uncomment the `headers` line. Those native examples use a local application token: `Authorization: Bearer <APP_AUTH_TOKEN>`. This is a development token you set yourself, **not** `CPK_INTELLIGENCE_API_KEY`. Replace `<APP_AUTH_TOKEN>` with the same local token you configured on the server, and replace the local scheme with your application's authentication before deployment.

Set `useSingleEndpoint={false}` for the multi-route servers above. If you kept an existing TypeScript single-route server, keep `useSingleEndpoint={true}` instead.

Your CopilotKit provider
    
    
    import { CopilotKitProvider } from "@copilotkit/react-core/v2";
    
    export function App() {
      return (
        <CopilotKitProvider
          runtimeUrl="/api/copilotkit"
          useSingleEndpoint={false}
          // Native runtime: runtimeUrl="http://localhost:8200/api/copilotkit" and
          // headers={{ Authorization: "Bearer <APP_AUTH_TOKEN>" }}
        >
          <YourApp />
        </CopilotKitProvider>
      );
    }

### Confirm the connection#

Start the runtime and check discovery at `{runtimeUrl}/info`. For a Next.js TypeScript handler on port 3000:
    
    
    curl --fail http://localhost:3000/api/copilotkit/info

For the native examples, use `http://localhost:8200/api/copilotkit/info`.

The response should report `mode: "intelligence"` and your registered agent. Discovery alone does not prove persistence; create and inspect a thread next.

Start your app and open it on localhost. Click the Inspector button (Kite icon) in the corner of the app.

  1. Open **Home**. Make sure that **Intelligence connected** appears beside **What's going on**.
  2. Return to your app and send one message to create a thread.
  3. Open **Rich Threads** in Inspector. Your new thread must appear in the list.
  4. Open the thread. Make sure that **Messages** contains the message that you sent.



If Home does not show **Intelligence connected** , or Threads is locked, the setup is incomplete. Follow the action shown in Inspector or review the [Inspector setup states](https://docs.copilotkit.ai/mastra/inspector#project-context-and-usage).

A chat reply does not prove that the key is in use. An SSE runtime replies with the key unread. Use the Inspector check above, or open the thread in the [cloud-hosted project](https://docs.copilotkit.ai/mastra/intelligence/managed-intelligence-platform).

## Self-hosted deployments#

All runtimes default to cloud-hosted Intelligence. For self-hosting, replace the endpoint settings in your selected runtime's configuration. Keep the project key and authentication from the setup above. Use the public addresses that your runtime and browser can reach.

TypeScriptPythonGoRubyC#/.NET

Set both `apiUrl` and `wsUrl` on `CopilotKitIntelligence`. Pass a bare WebSocket base; the client appends `/runner` and `/client`.
    
    
    const intelligence = new CopilotKitIntelligence({
      apiUrl: "https://api.intelligence.internal",
      wsUrl: "wss://realtime.intelligence.internal",
      apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
    });

Set all three URLs on `RuntimeConfig`. The runner and browser URLs include different suffixes:
    
    
    config = RuntimeConfig(
        api_key=os.environ["CPK_INTELLIGENCE_API_KEY"],
        api_url="https://api.intelligence.internal",
        runner_url="wss://realtime.intelligence.internal/runner",
        client_url="wss://realtime.intelligence.internal/client",
        base_path="/api/copilotkit",
        allowed_origins=("http://localhost:3000",),
    )

Pass `config` to `IntelligenceRuntime` in place of the cloud-hosted configuration.

Add these fields to the existing `copilotkit.Config`:
    
    
    APIURL:    "https://api.intelligence.internal",
    RunnerURL: "wss://realtime.intelligence.internal/runner",
    ClientURL: "wss://realtime.intelligence.internal/client",

Add these keyword arguments to `CopilotKit::Runtime.new`:
    
    
    api_url: 'https://api.intelligence.internal',
    runner_url: 'wss://realtime.intelligence.internal/runner',
    client_url: 'wss://realtime.intelligence.internal/client',

Add these properties to the existing `RuntimeOptions`:
    
    
    ApiUrl = new Uri("https://api.intelligence.internal"),
    RunnerUrl = new Uri("wss://realtime.intelligence.internal/runner"),
    ClientUrl = new Uri("wss://realtime.intelligence.internal/client"),

Do not append `/api` to the API host or `/websocket` to either WebSocket URL. The clients add those path segments. Setting only some endpoints can leave requests split between your deployment and cloud-hosted Intelligence.

Install steps are on [Self-host on Kubernetes](https://docs.copilotkit.ai/mastra/intelligence/self-hosting) and [Self-host on ECS](https://docs.copilotkit.ai/mastra/intelligence/self-hosting-ecs).

## Troubleshooting#

Chat works, and the project has no thread

In TypeScript, check that `intelligence` was passed to `CopilotRuntime`; otherwise it stays in SSE mode. The other runtimes have no SSE-only fallback. Check their server diagnostics and Intelligence endpoint settings.

An auth error on the first request

`CPK_INTELLIGENCE_API_KEY` is empty, or it belongs to another project.

The socket stays on connecting, then reports that it did not settle in time

Check every endpoint in the self-hosted settings above. The realtime host differs from the API host. Native runtimes need separate `/runner` and `/client` URLs; TypeScript uses the bare `wsUrl`.

Request logs show /api/api/...

`apiUrl` included an `/api` suffix.

A type error or a throw that names runner

This is a TypeScript configuration error: `runner` and `intelligence` are both set. Intelligence wires its own runner.

### On this page

OverviewStart with your coding agentSet it up manuallySelf-hosted deploymentsTroubleshooting
