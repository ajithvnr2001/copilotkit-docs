---
url: https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall/
title: registerRenderToolCall
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:10.681742+00:00
---

# registerRenderToolCall

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁AngularSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Guides

[Public API inventory](https://docs.copilotkit.ai/reference/angular/public-api)[Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle)

Components

[CopilotActivity](https://docs.copilotkit.ai/reference/angular/components/CopilotActivity)[CopilotChat](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/angular/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)[CopilotPopup](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)

Functions

[connectAgentContext](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)[injectAgentStore](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)[injectCapabilities](https://docs.copilotkit.ai/reference/angular/functions/injectCapabilities)[injectChatLabels](https://docs.copilotkit.ai/reference/angular/functions/injectChatLabels)[injectCopilotKitConfig](https://docs.copilotkit.ai/reference/angular/functions/injectCopilotKitConfig)[injectInterrupt](https://docs.copilotkit.ai/reference/angular/functions/injectInterrupt)[injectThreads](https://docs.copilotkit.ai/reference/angular/functions/injectThreads)[provideCopilotChatLabels](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotChatLabels)[provideCopilotKit](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)[provideMCPApps](https://docs.copilotkit.ai/reference/angular/functions/provideMCPApps)[registerComponent](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)[registerFrontendTool](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)[registerHumanInTheLoop](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)[registerRenderActivityMessage](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)[registerRenderToolCall](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)

Services

[CopilotKit](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)

Directives

[CopilotKitAgentContext](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Functions

# registerRenderToolCall

Angular function for registering a renderer component for a tool call with CopilotKit, with access to streaming arguments, status, and result

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`registerRenderToolCall` registers a renderer for a tool call. It does not run a handler. It tells CopilotKit which standalone Angular component to render whenever a tool call with a matching `name` appears in the conversation. Use it to visualize tool calls that execute somewhere other than the browser, for example a server-side tool or an agentic (long-running) tool, where you only want to show progress and results in the chat.

You call `registerRenderToolCall` inside an Angular injection context (a component or service constructor, or a field initializer). The renderer registers immediately. When the owning injector is destroyed, CopilotKit removes tool and renderer registrations with the same name and optional agent id.

If you want to run a browser handler and render UI, use [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool) with its `component` field instead. If the agent does not already have the tool and you only want it to display one of your components, use [`registerComponent`](https://docs.copilotkit.ai/reference/angular/functions/registerComponent), which declares the tool from the frontend so nothing has to be added on the agent side.

Import from the package root, `@copilotkit/angular`. There is no `/v2` subpath. `registerRenderToolCall` must run in an injection context that has [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) in scope.

## Signature
    
    
    import { registerRenderToolCall } from "@copilotkit/angular";
    
    function registerRenderToolCall<Args extends Record<string, unknown>>(
      renderToolCall: RenderToolCallConfig<Args>,
    ): void;

## Parameters

Prop

Type

`renderToolCall`RenderToolCallConfig<Args>

## Return Value

`registerRenderToolCall` returns `void`. It registers the renderer as a side effect and wires up name-and-agent-id cleanup for the owning injector. Frontend tools, human-in-the-loop tools, and renderer registrations sharing that key are removed together.

## The renderer component

Your `component` implements the `ToolRenderer<Args>` interface. CopilotKit binds the inputs by name, so declare them with Angular's `input()`:
    
    
    import { Signal } from "@angular/core";
    import { AbstractAgent } from "@ag-ui/client";
    
    interface ToolRenderer<Args extends Record<string, unknown>> {
      // Required: the current state of the tool call.
      toolCall: Signal<AngularToolCall<Args>>;
      // Bound only when the config sets passAgent: true.
      agent?: Signal<AbstractAgent | undefined>;
    }

### AngularToolCall

`toolCall()` returns a discriminated union keyed on `status`. The shape of `args` and `result` depends on the status:
    
    
    type AngularToolCall<Args extends Record<string, unknown>> =
      | {
          name?: string;
          args: Partial<Args>; // streaming, may be incomplete
          status: "in-progress";
          result: undefined;
        }
      | {
          name?: string;
          args: Args; // fully parsed
          status: "executing";
          result: undefined;
        }
      | {
          name?: string;
          args: Args; // fully parsed
          status: "complete";
          result: string; // the tool result, as a string
        };

  * **`in-progress`** means the arguments are still streaming in, so `args` is `Partial<Args>` and `result` is `undefined`.
  * **`executing`** means the arguments have fully arrived and the tool is running, so `args` is the complete `Args` and `result` is still `undefined`.
  * **`complete`** means the tool finished, so `args` is complete and `result` holds the string result.



## Usage

### A renderer component for a server-side tool

This renderer shows a spinner while the tool runs and then renders the result. It narrows on `status` so the template only reads `result` once it is available.

src/app/search-tool-view.component.ts
    
    
    import { Component, input } from "@angular/core";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type SearchArgs = { query: string };
    
    @Component({
      selector: "app-search-tool-view",
      standalone: true,
      template: `
        @let call = toolCall();
        @switch (call.status) {
          @case ("in-progress") {
            <div class="text-sm opacity-70">Preparing search...</div>
          }
          @case ("executing") {
            <div class="text-sm opacity-70">Searching for "{{ call.args.query }}"...</div>
          }
          @case ("complete") {
            <pre class="rounded border p-3 text-sm">{{ call.result }}</pre>
          }
        }
      `,
    })
    export class SearchToolViewComponent implements ToolRenderer<SearchArgs> {
      readonly toolCall = input.required<AngularToolCall<SearchArgs>>();
    }

Register it for the tool name your agent emits:

src/app/chat.component.ts
    
    
    import { Component } from "@angular/core";
    import { z } from "zod";
    import { registerRenderToolCall } from "@copilotkit/angular";
    import { SearchToolViewComponent } from "./search-tool-view.component";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      template: ``,
    })
    export class ChatComponent {
      constructor() {
        registerRenderToolCall({
          name: "searchDocuments",
          args: z.object({ query: z.string() }),
          component: SearchToolViewComponent,
        });
      }
    }

### Receiving the agent instance

Set `passAgent: true` to have CopilotKit bind the `agent` signal input as well. Declare it on the component as an optional `input()`.

src/app/handoff-tool-view.component.ts
    
    
    import { Component, input } from "@angular/core";
    import { AbstractAgent } from "@ag-ui/client";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type HandoffArgs = { target: string };
    
    @Component({
      selector: "app-handoff-tool-view",
      standalone: true,
      template: `<div>Handing off to {{ toolCall().args.target }}</div>`,
    })
    export class HandoffToolViewComponent implements ToolRenderer<HandoffArgs> {
      readonly toolCall = input.required<AngularToolCall<HandoffArgs>>();
      readonly agent = input<AbstractAgent | undefined>();
    }

src/app/chat.component.ts
    
    
    registerRenderToolCall({
      name: "handoff",
      args: z.object({ target: z.string() }),
      component: HandoffToolViewComponent,
      passAgent: true,
    });

## Related

### [registerComponentLet the agent display one of your components, with no handler and nothing to add on the agent side.](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)### [registerFrontendToolRegister a client-side tool with an async handler and an optional renderer component.](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)### [registerHumanInTheLoopRegister a tool that pauses the agent and waits for the user to respond from a rendered component.](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)### [CopilotKit serviceThe central service that holds agents, tools, and the runtime connection.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)
