---
url: https://docs.copilotkit.ai/reference/angular/functions/registerComponent/
title: registerComponent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:10.104542+00:00
---

# registerComponent

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerComponent/

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

# registerComponent

Angular function for registering a standalone component the agent can call as a tool to display it in the chat, with no handler and nothing to add on the agent side

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`registerComponent` registers a standalone Angular component as a tool the agent can call to display it. When the agent calls the tool, CopilotKit renders your component in the chat with the tool call's arguments. There is no handler, no user interaction, and no server-side execution: the agent decides when to show the component and populates its data.

This is the simplest form of generative UI, and the only one that needs nothing on the agent side. The tool is declared by the frontend and forwarded to the agent over AG-UI, so it behaves the same behind a Python agent as a TypeScript one. Contrast [`registerRenderToolCall`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall), which draws a tool the agent already has and therefore requires that tool to exist in the agent.

You call `registerComponent` inside an Angular injection context (a component or service constructor, or a field initializer). The registration happens immediately and is removed when the owning injector is destroyed.

`registerComponent` is the Angular counterpart of `useComponent` in `@copilotkit/react-core/v2` and `@copilotkit/vue/v2`. It builds the same model-facing tool description, so the tool reads identically to the model whichever frontend registered the component.

Import from the package root, `@copilotkit/angular`. There is no `/v2` subpath. `registerComponent` must run in an injection context that has [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) in scope.

## Signature
    
    
    import { registerComponent } from "@copilotkit/angular";
    
    function registerComponent<Args extends Record<string, unknown>>(
      config: RegisterComponentConfig<Args>,
    ): void;

## Parameters

Prop

Type

`config`RegisterComponentConfig<Args>

There is no `handler` field. A display-only component runs no application code, and CopilotKit completes the agent's turn with an empty tool result rather than an invented one. If you want to run browser code as well as render, use [`registerFrontendTool`](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool) with both `handler` and `component`.

## Return Value

`registerComponent` returns `void`. It registers the tool and its renderer as a side effect, and removes both when the owning injector is destroyed.

## The component

Your `component` implements the `ToolRenderer<Args>` interface — the same contract every other Angular renderer uses. Declare the `toolCall` input with Angular's `input.required()` and read `toolCall().args`:
    
    
    import { Signal } from "@angular/core";
    
    interface ToolRenderer<Args extends Record<string, unknown>> {
      toolCall: Signal<AngularToolCall<Args>>;
    }

`toolCall()` is a discriminated union keyed on `status`. While the model is still streaming the payload the status is `in-progress` and `args` is `Partial<Args>`, so narrow on `status` before reading a field you require. See [`registerRenderToolCall`](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall#angulartoolcall) for the full union.

## Usage

### Display a card the agent fills in

src/app/incident-card.component.ts
    
    
    import { Component, input } from "@angular/core";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type IncidentArgs = { id: string; severity: string; summary: string };
    
    @Component({
      selector: "app-incident-card",
      standalone: true,
      template: `
        @let call = toolCall();
        @if (call.status === "in-progress") {
          <div class="text-sm opacity-70">Loading incident…</div>
        } @else {
          <article class="rounded-lg border p-4">
            <header class="flex items-baseline justify-between">
              <strong>{{ call.args.id }}</strong>
              <span class="text-xs uppercase">{{ call.args.severity }}</span>
            </header>
            <p class="text-sm">{{ call.args.summary }}</p>
          </article>
        }
      `,
    })
    export class IncidentCardComponent implements ToolRenderer<IncidentArgs> {
      readonly toolCall = input.required<AngularToolCall<IncidentArgs>>();
    }

Register it once, anywhere under `provideCopilotKit`:

src/app/chat.component.ts
    
    
    import { Component } from "@angular/core";
    import { z } from "zod";
    import { registerComponent } from "@copilotkit/angular";
    import { IncidentCardComponent } from "./incident-card.component";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      template: ``,
    })
    export class ChatComponent {
      constructor() {
        registerComponent({
          name: "show_incident",
          description: "Show one incident from the incident table.",
          parameters: z.object({
            id: z.string().describe("The incident id, such as INC-4711"),
            severity: z.string().describe("One of sev1, sev2, sev3"),
            summary: z.string().describe("One sentence on what happened"),
          }),
          component: IncidentCardComponent,
        });
      }
    }

Nothing is added to the agent. The tool reaches it in the run's tool list, and the agent calls it by name.

### Scoping to one agent
    
    
    registerComponent({
      name: "show_incident",
      parameters: incidentSchema,
      component: IncidentCardComponent,
      agentId: "support-agent",
    });

## Grounding the component in your own data

A component that renders correctly over records your application does not hold looks identical to a correct one, in the browser and in a screenshot alike. The model fills these props from what it knows, so a component whose data never reached the agent is drawn from what the agent invented.

Registering the component is the rendering half. Give the agent the data it should describe with [`CopilotKitAgentContext`](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext) or [`connectAgentContext`](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext), then check the rendered fields against the records your application holds.

## Related

### [registerFrontendToolRegister a client-side tool with an async handler and an optional renderer component.](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)### [registerRenderToolCallDraw a tool the agent already has, with access to streaming arguments, status, and result.](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)### [registerHumanInTheLoopRegister a tool that pauses the agent and waits for the user to respond from a rendered component.](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)### [CopilotKitAgentContextShare the data on the page with the agent, so a rendered component describes records you hold.](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)
