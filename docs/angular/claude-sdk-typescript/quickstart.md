---
url: https://docs.copilotkit.ai/angular/claude-sdk-typescript/quickstart/
title: Angular quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:59.003598+00:00
---

# Angular quickstart

> Source: https://docs.copilotkit.ai/angular/claude-sdk-typescript/quickstart/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendClaude Agent SDK (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/claude-sdk-typescript)[Quickstart](https://docs.copilotkit.ai/angular/claude-sdk-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/claude-sdk-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/claude-sdk-typescript/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/claude-sdk-typescript/webmcp)

Agent capabilities

Angular Guides

[Sub-agents](https://docs.copilotkit.ai/angular/claude-sdk-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/claude-sdk-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/claude-sdk-typescript/learning)

[User Memories](https://docs.copilotkit.ai/angular/claude-sdk-typescript/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/claude-sdk-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/claude-sdk-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/claude-sdk-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/claude-sdk-typescript/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/claude-sdk-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/claude-sdk-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# Angular

Connect an Angular app to Copilot Runtime with CopilotKit.

`@copilotkit/angular` provides Angular components, directives, and services for CopilotKit. This guide gets you to a working Angular app with a chat UI backed by [Copilot Runtime](https://docs.copilotkit.ai/angular/claude-sdk-typescript/backend/copilot-runtime). When you select an agent backend in the sidebar, the backend step below changes with it; without a selection, the guide uses CopilotKit's `BuiltInAgent`.

The runtime runs on your server, keeps model credentials out of the browser, and exposes the `default` agent that `CopilotChat` uses automatically.

[Take your Angular copilot from local to productionAdd threads, inspection, and cloud-hosted or self-hosted CopilotKit Intelligence without changing the Angular frontend APIs in this guide.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs%3Aangular%2Fquickstart%3Aproduction&utm_frontend=angular&utm_backend=claude-sdk-typescript)

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

### Install the Claude Agent SDK packages
    
    
    npm install @ag-ui/core @ag-ui/encoder @ag-ui/claude-agent-sdk @anthropic-ai/claude-agent-sdk@^0.2.58 @anthropic-ai/sdk zod

### Bridge Claude Agent SDK to AG-UI

Use `ClaudeAgentAdapter` from `@ag-ui/claude-agent-sdk`. The adapter receives the AG-UI run input, emits AG-UI events back to CopilotKit, and can expose backend tools through an in-process Claude SDK MCP server.

claude-agent-sdk-adapter.ts
    
    
    function createClaudeAgentAdapter({
      toolSchemas,
      emit,
      getState,
      setState,
      executeTool,
      model,
      systemPrompt,
    }: {
      toolSchemas: Anthropic.Tool[];
      emit: Emit;
      getState: () => Record<string, unknown>;
      setState: (state: Record<string, unknown>) => void;
      executeTool: ExecuteTool;
      model: string;
      systemPrompt: string;
    }) {
      const backendToolServer = buildBackendToolServer({
        toolSchemas,
        emit,
        getState,
        setState,
        executeTool,
      });
    
      return new ClaudeAgentAdapter({
        agentId: "claude-sdk-typescript",
        model: normalizeClaudeAgentSdkModel(model),
        systemPrompt,
        tools: [],
        mcpServers: backendToolServer.mcpServers,
        allowedTools: backendToolServer.allowedTools,
        permissionMode: "dontAsk",
        maxTurns: 10,
      });
    }

claude-agent-sdk-adapter.ts
    
    
    export async function runWithClaudeAgentSdk({
      input,
      emit,
      runId,
      threadId,
      systemPrompt,
      toolSchemas,
      initialState,
      model,
      executeTool,
      forwardedHeaders,
    }: {
      input: RunAgentInput;
      emit: Emit;
      runId: string;
      threadId: string;
      systemPrompt: string;
      toolSchemas: Anthropic.Tool[];
      initialState: Record<string, unknown>;
      model: string;
      executeTool: ExecuteTool;
      forwardedHeaders?: Record<string, string>;
    }): Promise<void> {
      let state = { ...initialState };
      const pendingStateSnapshots: Record<string, unknown>[] = [];
      const adapter = createClaudeAgentAdapter({
        toolSchemas,
        emit,
        getState: () => state,
        setState: (nextState) => {
          state = nextState;
          pendingStateSnapshots.push(state);
        },
        executeTool,
        systemPrompt,
        model,
      });
    
      if (forwardedHeaders && Object.keys(forwardedHeaders).length > 0) {
        adapter.headers = forwardedHeaders;
      }
    
      const runInput: RunAgentInput = {
        ...input,
        runId,
        threadId,
        state: input.state ?? initialState,
      };
    
      await new Promise<void>((resolve) => {
        adapter.run(runInput).subscribe({
          next: (event) => {
            if (event.type === EventType.TOOL_CALL_RESULT) {
              const snapshot = pendingStateSnapshots.shift();
              if (snapshot) {
                emit({ type: EventType.STATE_SNAPSHOT, snapshot });
              }
            }
            emit(event);
          },
          error: (error) => {
            const message =
              error instanceof Error ? error.stack || error.message : String(error);
            emit({ type: EventType.RUN_ERROR, runId, threadId, message });
            resolve();
          },
          complete: () => resolve(),
        });
      });
    }

Expose the selected backend through Copilot Runtime

Configure Copilot Runtime to register this backend as the `default` agent at `/api/copilotkit`. Continue with the selected backend's [Copilot Runtime guide](https://docs.copilotkit.ai/angular/claude-sdk-typescript/quickstart/backend/copilot-runtime) for its runtime adapter, credentials, and server command. Do not replace it with the `BuiltInAgent` server from the standalone Angular path.

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



More detail: [Inspector](https://docs.copilotkit.ai/angular/claude-sdk-typescript/inspector).

## Next steps#

  * [Runtime and backend docs](https://docs.copilotkit.ai/angular/claude-sdk-typescript/quickstart/backend/copilot-runtime): configure the server, secure requests, and deploy without leaving the selected Angular surface.
  * [CopilotKit Intelligence](https://docs.copilotkit.ai/angular/claude-sdk-typescript/quickstart/intelligence/overview): add threads, inspection, and cloud-hosted or self-hosted operations.
  * [Angular task guides](https://docs.copilotkit.ai/angular/claude-sdk-typescript/quickstart/guides/chat-ui): build chat UI, tools, generative UI, interrupts, shared state, threads, memory, attachments, and headless UI.
  * [Angular feature examples](https://docs.copilotkit.ai/angular/claude-sdk-typescript/quickstart/features): find runnable examples and canonical shared Angular source for each supported feature.
  * [Angular API reference](https://docs.copilotkit.ai/reference/angular): use components, signals, tools, context, and runtime services.
  * [Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle): handle cleanup, errors, server rendering, hydration, zoneless Angular, and browser-only features.


