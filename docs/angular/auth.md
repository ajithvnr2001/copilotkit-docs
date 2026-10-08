---
url: https://docs.copilotkit.ai/angular/auth/
title: Authentication
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:21.906899+00:00
---

# Authentication

> Source: https://docs.copilotkit.ai/angular/auth/

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

Runtime

[Copilot Runtime](https://docs.copilotkit.ai/angular/backend/copilot-runtime)[Runtime HTTP endpoints](https://docs.copilotkit.ai/angular/backend/runtime-endpoints)[Use any model router](https://docs.copilotkit.ai/angular/backend/custom-agent)[Write your own AG-UI agent](https://docs.copilotkit.ai/angular/backend/custom-ag-ui-agent)[AgentRunner and persistence](https://docs.copilotkit.ai/angular/backend/agent-runner)[Message history](https://docs.copilotkit.ai/angular/backend/message-history)[Self-managed agents](https://docs.copilotkit.ai/angular/backend/self-managed-agents)[Connect AG-UI agents](https://docs.copilotkit.ai/angular/backend/ag-ui)[Deploy to any runtime](https://docs.copilotkit.ai/angular/runtime-server-adapter)[Authentication](https://docs.copilotkit.ai/angular/auth)

Deployment

Debugging

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Authentication

BackendRuntimeRuntime

# Authentication

Authenticate Angular requests at Copilot Runtime and forward only the identity context your agent needs.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What authentication protects#

CopilotKit authentication covers two boundaries:

  1. Your Angular app sends its current session token to Copilot Runtime.
  2. Copilot Runtime validates that token before a run starts and forwards only the approved identity or tenant context to the selected agent.



Keep model credentials and service-to-service agent tokens on the server. Browser headers prove the end user's session; they are not a safe place for backend secrets.

## Send the current session#

Set initial headers in `provideCopilotKit`:

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
          headers: {
            Authorization: `Bearer ${readSessionToken()}`,
          },
        }),
      ],
    };

When sign-in state changes after bootstrap, update the runtime connection through the `CopilotKit` service:
    
    
    import { inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    const copilotKit = inject(CopilotKit);
    
    copilotKit.updateRuntime({
      headers: sessionToken
        ? { Authorization: `Bearer ${sessionToken}` }
        : {},
    });

The runnable Angular Showcase uses the same header shape:

app-settings-feature.component.ts
    
    
    const DEMO_AUTH_HEADERS: Readonly<Record<string, string>> = {  Authorization: "Bearer demo-token-123",};

## Send cookies to a cross-origin runtime#

To enable HTTP-only cookie authentication, set `credentials: "include"` and configure CORS on your runtime endpoint:

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "https://runtime.example.com/api/copilotkit",
          credentials: "include",
        }),
      ],
    };

Configure the runtime with `credentials: true` and the Angular app's exact origin. Credentialed CORS requests cannot use `*` as the allowed origin.

## Validate every runtime request#

Use the runtime adapter's request hook to reject missing, expired, or unauthorized sessions before CopilotKit discovers or runs an agent:

server.ts
    
    
    const handler = createCopilotExpressHandler({
      runtime,
      basePath: "/api/copilotkit",
      hooks: {
        onRequest: async ({ request }) => {
          const token = request.headers
            .get("authorization")
            ?.replace(/^Bearer\s+/i, "");
          const session = token ? await verifySession(token) : null;
    
          if (!session) {
            throw new Response("Unauthorized", { status: 401 });
          }
        },
      },
    });

Apply authorization as well as authentication. A valid user token does not automatically grant access to every agent, tenant, or thread.

## Forward identity deliberately#

Copilot Runtime forwards `authorization` and eligible `x-*` headers to a self-hosted agent, subject to its denylist. Prefer a small allowlist when your agent needs only specific context:
    
    
    const runtime = new CopilotRuntime({
      agents: { default: myAgent },
      forwardHeaders: {
        allow: ["authorization", "x-tenant-id"],
      },
    });

Server-configured agent headers win over forwarded browser headers. Use that separation for service credentials, and never allow a browser-supplied header to override a backend token.

## Production checklist#

  * Validate `/info`, run, connect, stop, thread, and memory requests—not just chat sends.
  * Derive user and tenant identifiers from the verified session instead of trusting arbitrary browser values.
  * Scope thread operations to the authenticated user and project.
  * Clear frontend headers on sign-out with `updateRuntime({ headers: {} })`.
  * Configure CORS for the deployed Angular origin.
  * Log authorization failures without logging bearer tokens.



## Next steps#

  * [Copilot Runtime](https://docs.copilotkit.ai/angular/backend/copilot-runtime)
  * [Runtime HTTP endpoints](https://docs.copilotkit.ai/angular/backend/runtime-endpoints)
  * [Deploy to any runtime](https://docs.copilotkit.ai/angular/runtime-server-adapter)
  * [Angular API: CopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)



### On this page

What authentication protectsSend the current sessionSend cookies to a cross-origin runtimeValidate every runtime requestForward identity deliberatelyProduction checklistNext steps
