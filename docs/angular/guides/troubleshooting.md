---
url: https://docs.copilotkit.ai/angular/guides/troubleshooting/
title: Troubleshooting Angular apps
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:30.927145+00:00
---

# Troubleshooting Angular apps

> Source: https://docs.copilotkit.ai/angular/guides/troubleshooting/

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

Angular guides

[Using the Angular docs](https://docs.copilotkit.ai/angular/using-these-docs)[Feature examples](https://docs.copilotkit.ai/angular/features)[Angular API reference](https://docs.copilotkit.ai/reference/angular)[Chat UI and customization](https://docs.copilotkit.ai/angular/guides/chat-ui)[Frontend tools and generative UI](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)[A2UI schemas, styling, and recovery](https://docs.copilotkit.ai/angular/guides/a2ui)[Voice and multimodal input](https://docs.copilotkit.ai/angular/guides/voice-multimodal)[Human-in-the-loop and interrupts](https://docs.copilotkit.ai/angular/guides/human-in-the-loop)[Shared state and agent context](https://docs.copilotkit.ai/angular/guides/shared-state)[Threads, memory, attachments, and headless UI](https://docs.copilotkit.ai/angular/guides/threads-memory-attachments-headless)[Troubleshooting Angular apps](https://docs.copilotkit.ai/angular/guides/troubleshooting)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Troubleshooting Angular apps

LearnAngular guides

# Troubleshooting Angular apps

Diagnose Angular runtime connections, agent resolution, tools, threads, interrupts, SSR, and rendering failures.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Use this page for failures in the Angular application layer. Runtime and protocol diagnostics remain available in the shared troubleshooting pages, so you can investigate the complete request without switching frontend docs.

## Start at the connection boundary#

Confirm that the browser is calling the same Copilot Runtime URL your server actually exposes:

src/app/app.config.ts
    
    
    import { provideCopilotKit } from "@copilotkit/angular";
    
    export const appConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
        }),
      ],
    };

Then inspect `GET {runtimeUrl}/info`. A healthy response lists the expected agent ids. If the request fails:

  * verify the path, origin, proxy, and deployment base URL;
  * verify the runtime process is running and allows the Angular origin;
  * check authentication headers without logging their values;
  * try `127.0.0.1` when local `localhost` resolution is unreliable.



The [`CopilotKit` service](https://docs.copilotkit.ai/reference/angular/services/CopilotKit) exposes `runtimeConnectionStatus`, `runtimeUrl`, and the resolved `agents` as signals. Use them in a temporary diagnostic component:

src/app/copilot-diagnostics.component.ts
    
    
    import { Component, inject } from "@angular/core";
    import { CopilotKit } from "@copilotkit/angular";
    
    @Component({
      selector: "app-copilot-diagnostics",
      standalone: true,
      template: `
        <p>Runtime: {{ copilotKit.runtimeConnectionStatus() }}</p>
        <p>Agents: {{ agentIds().join(", ") || "none" }}</p>
      `,
    })
    export class CopilotDiagnosticsComponent {
      protected readonly copilotKit = inject(CopilotKit);
      protected readonly agentIds = () =>
        Object.keys(this.copilotKit.agents());
    }

Remove diagnostics that expose topology or identifiers before production.

## Agent id does not resolve#

`injectAgentStore("support")` and `<copilot-chat agentId="support" />` must use an id returned by the runtime or registered through `agents` or `selfManagedAgents`. After the runtime finishes connecting, `injectAgentStore` throws an error that includes the requested id and known agents when no match exists.

If you intend to use the default agent, either register an agent named `default` or pass the real id explicitly everywhere the chat, state, tools, or interrupt controller selects an agent.

## A frontend tool is missing or never runs#

Registrations are injector-scoped. Call `registerFrontendTool`, `registerRenderToolCall`, or `registerHumanInTheLoop` from a field initializer, constructor, provider factory, or another active injection context.

Check these in order:

  1. The component or service that registers the tool is instantiated.
  2. Its injector has not been destroyed by route or conditional-view changes.
  3. The registered `agentId` matches the chat's agent.
  4. The tool description tells the model when it should call the tool.
  5. The input schema accepts the arguments emitted by the agent.
  6. The handler catches expected application failures and returns a deliberate result instead of silently throwing.



For a source-backed registration, see [Frontend tools and generative UI](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui).

## A thread list or mutation fails#

Use `listError()` for user-visible thread-list and mutation failures. The broader `error()` signal can also contain developer configuration errors such as a missing runtime URL or unavailable thread endpoints.

Mutation methods return promises. Handle rejection and confirm before permanent deletion:
    
    
    await threads.renameThread(threadId, nextName).catch((error) => {
      console.error("Thread rename failed", error);
    });

See [`injectThreads`](https://docs.copilotkit.ai/reference/angular/functions/injectThreads) for loading, pagination, realtime, and optimistic-mutation behavior.

## An interrupt cannot resume#

Read `injectInterrupt().error()` after a failed predicate, handler, or resume. Expired decisions use `InterruptExpiredError`. Resolve or cancel every pending interrupt id when the backend emits multiple simultaneous decisions.

The controller clears stale decisions when a thread changes or a new run starts. Do not cache it outside the injector that created it.

## SSR, hydration, or zoneless problems#

  * Keep provider configuration and initial component inputs identical between the server render and first browser render.
  * Do not start agent runs, resume interrupts, or access browser APIs during server rendering.
  * Put application-owned DOM and media work behind an Angular platform guard or `afterNextRender`.
  * Read CopilotKit signals from templates or computed signals so zoneless change detection observes updates.



The complete contract is in [Angular production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle).

## Watch the live event stream#

The [Inspector](https://docs.copilotkit.ai/angular/inspector) overlays the running application and reports the AG-UI event stream, the advertised agents, agent state, your registered tools, and the context you sent. It is a web component that an Angular application mounts itself; that page has the mount component and the production guard.

## Continue through the shared stack#

  * [Common Copilot issues](https://docs.copilotkit.ai/angular/troubleshooting/common-issues)
  * [Runtime endpoints](https://docs.copilotkit.ai/angular/backend/runtime-endpoints)
  * [Runtime debug mode](https://docs.copilotkit.ai/angular/troubleshooting/debug-mode)
  * [AG-UI Event Inspector](https://docs.copilotkit.ai/angular/troubleshooting/event-inspector)
  * [Authentication](https://docs.copilotkit.ai/angular/auth)



### On this page

Start at the connection boundaryAgent id does not resolveA frontend tool is missing or never runsA thread list or mutation failsAn interrupt cannot resumeSSR, hydration, or zoneless problemsWatch the live event streamContinue through the shared stack
