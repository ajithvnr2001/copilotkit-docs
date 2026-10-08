---
url: https://docs.copilotkit.ai/angular/mastra/quickstart/
title: Angular quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:50:44.504290+00:00
---

# Angular quickstart

> Source: https://docs.copilotkit.ai/angular/mastra/quickstart/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendMastra

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/mastra)[Quickstart](https://docs.copilotkit.ai/angular/mastra/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/mastra/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/mastra/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/mastra/webmcp)

Agent capabilities

Mastra

[Sub-agents](https://docs.copilotkit.ai/angular/mastra/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/mastra/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/mastra/learning)

[User Memories](https://docs.copilotkit.ai/angular/mastra/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/mastra/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/mastra/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/mastra/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/mastra/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/mastra/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/mastra/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# Angular

Connect an Angular app to Copilot Runtime with CopilotKit.

`@copilotkit/angular` provides Angular components, directives, and services for CopilotKit. This guide gets you to a working Angular app with a chat UI backed by [Copilot Runtime](https://docs.copilotkit.ai/angular/mastra/backend/copilot-runtime). When you select an agent backend in the sidebar, the backend step below changes with it; without a selection, the guide uses CopilotKit's `BuiltInAgent`.

The runtime runs on your server, keeps model credentials out of the browser, and exposes the `default` agent that `CopilotChat` uses automatically.

[Take your Angular copilot from local to productionAdd threads, inspection, and cloud-hosted or self-hosted CopilotKit Intelligence without changing the Angular frontend APIs in this guide.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs%3Aangular%2Fquickstart%3Aproduction&utm_frontend=angular&utm_backend=mastra)

## Start with your coding agent#

Use this prompt to connect your Angular app to Copilot Runtime with the selected agent backend, then verify a working conversation. You can also follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is CopilotKit for Angular?#

CopilotKit for Angular is the first-party, signal-based Angular frontend for AG-UI agents and Copilot Runtime. It provides complete chat surfaces and headless APIs, and it supports zoneless applications.

## Prerequisites#

  * An OpenAI API key (or another model provider supported by [Model Selection](https://docs.copilotkit.ai/angular/model-selection))
  * Angular 22
  * Node.js 22



## Getting started#

### Create your Angular app#

If you don't have one already, pin the CLI to the supported major:
    
    
    npx @angular/cli@22 new my-copilot-app
    cd my-copilot-app

### Install CopilotKit#

Install the Angular frontend package, `@angular/cdk`, and `@copilotkit/runtime` for your local Copilot Runtime server:

npmpnpmyarn
    
    
    npm install @copilotkit/angular @angular/cdk @copilotkit/runtime
    npm install -D tsx typescript @types/node
    
    
    pnpm add @copilotkit/angular @angular/cdk @copilotkit/runtime
    pnpm add -D tsx typescript @types/node
    
    
    yarn add @copilotkit/angular @angular/cdk @copilotkit/runtime
    yarn add -D tsx typescript @types/node

Match @angular/cdk to your Angular version

`@angular/cdk` must share your Angular major version. Most package managers resolve this for you, but if you hit a peer-dependency error, pin it explicitly (for example `@angular/cdk@^22`).

### Connect the selected agent backend#

This URL keeps the agent backend selected. The Angular setup remains shared; the backend setup below comes from that integration's canonical showcase source.

Expose the selected backend through Copilot Runtime

Configure Copilot Runtime to register this backend as the `default` agent at `/api/copilotkit`. Continue with the selected backend's [Copilot Runtime guide](https://docs.copilotkit.ai/angular/mastra/quickstart/backend/copilot-runtime) for its runtime adapter, credentials, and server command. Do not replace it with the `BuiltInAgent` server from the standalone Angular path.

### Import the styles#

Add the package stylesheet to your global styles. It's self-contained, so the chat renders without any other CSS.

src/styles.css
    
    
    @import "@copilotkit/angular/styles.css"; 

### Connect to Copilot Runtime#

Point `provideCopilotKit` at the runtime endpoint. The chat uses the agent that your runtime registers as `default`.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular"; 
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "http://localhost:8200/api/copilotkit",
        }),
      ],
    };

### Add the chat UI#

Import the `CopilotChat` component into your root component and drop it into the template.

src/app/app.ts
    
    
    import { Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular"; 
    
    @Component({
      selector: "app-root",
      imports: [CopilotChat], 
      template: `
        <div style="height: 100vh">
          <copilot-chat />
        </div>
      `,
    })
    export class App {}

### Run the backend, runtime, and Angular app#

Start the selected agent backend and Copilot Runtime with the commands from its runtime guide. Confirm `http://localhost:8200/api/copilotkit/info` reports the `default` agent, then start Angular:
    
    
    npm start

Open the Angular CLI URL (usually `http://localhost:4200`) and send a message. The request now follows the selected path end to end: Angular → Copilot Runtime → your selected agent backend.

### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/angular/mastra/inspector).

## Next steps#

  * [Runtime and backend docs](https://docs.copilotkit.ai/angular/mastra/quickstart/backend/copilot-runtime): configure the server, secure requests, and deploy without leaving the selected Angular surface.
  * [CopilotKit Intelligence](https://docs.copilotkit.ai/angular/mastra/quickstart/intelligence/overview): add threads, inspection, and cloud-hosted or self-hosted operations.
  * [Angular task guides](https://docs.copilotkit.ai/angular/mastra/quickstart/guides/chat-ui): build chat UI, tools, generative UI, interrupts, shared state, threads, memory, attachments, and headless UI.
  * [Angular feature examples](https://docs.copilotkit.ai/angular/mastra/quickstart/features): find runnable examples and canonical shared Angular source for each supported feature.
  * [Angular API reference](https://docs.copilotkit.ai/reference/angular): use components, signals, tools, context, and runtime services.
  * [Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle): handle cleanup, errors, server rendering, hydration, zoneless Angular, and browser-only features.


