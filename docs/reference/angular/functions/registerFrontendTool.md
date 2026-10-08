---
url: https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool/
title: registerFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:10.169349+00:00
---

# registerFrontendTool

> Source: https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool/

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

# registerFrontendTool

Angular function for registering a client-side frontend tool with CopilotKit, with an optional Angular renderer component, that runs in the browser when an agent calls it

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`registerFrontendTool` registers a client-side tool with CopilotKit. When the agent decides to call the tool, the provided `handler` function executes in the browser, and the value it resolves to is surfaced back to the agent as the tool result. Optionally, you can supply a `component` (a standalone Angular component) to render custom UI in the chat that shows the tool call's progress and result.

You call `registerFrontendTool` inside an Angular injection context (a component or service constructor, or a field initializer). The tool registers immediately. When the owning injector is destroyed, CopilotKit removes tool and renderer registrations with the same name and optional agent id. Parameter schemas use a [Standard Schema](https://standardschema.dev), such as a [Zod](https://zod.dev) object, for the advertised tool schema and TypeScript inference. Runtime arguments are JSON-parsed but are not validated against that schema.

The handler runs inside the same injector that registered the tool, so it can call `inject()` to reach your other Angular services.

If there is nothing to run in the browser and you only want the agent to display a component with the arguments it supplies, use [`registerComponent`](https://docs.copilotkit.ai/reference/angular/functions/registerComponent) instead of a stub handler.

Import from the package root, `@copilotkit/angular`. There is no `/v2` subpath. `registerFrontendTool` must run in an injection context that has [`provideCopilotKit`](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit) in scope.

## Signature
    
    
    import { registerFrontendTool } from "@copilotkit/angular";
    
    function registerFrontendTool<Args extends Record<string, unknown>>(
      frontendTool: FrontendToolConfig<Args>,
    ): void;

## Parameters

Prop

Type

`frontendTool`FrontendToolConfig<Args>

## Return Value

`registerFrontendTool` returns `void`. It performs the registration as a side effect and wires up name-and-agent-id cleanup for the owning injector.

## Behavior

  * **Immediate registration.** The tool is added to CopilotKit as soon as the function runs, so call it during construction or field initialization, not inside an event handler.
  * **Runs in the injection context.** The `handler` is invoked with `runInInjectionContext` using the injector that registered the tool, so `inject()` works inside it.
  * **Cleanup by key.** When the owning component or service is destroyed, CopilotKit removes frontend tools, human-in-the-loop tools, and tool-call renderers with the same `name` and optional `agentId`. Registrations sharing that key are removed together.
  * **Optional renderer.** When you pass a `component`, it is registered alongside the tool so the chat can render the tool call's progress and result.
  * **WebMCP registration.** With `webmcp` set, the tool is also registered on `document.modelContext` for as long as the owning injector is alive. The tool needs a `description` for this (WebMCP rejects tools without one).



## Usage

### Basic tool with a Zod schema and async handler

Register the tool in the component constructor. The handler reads and writes a local signal, then returns a string result for the agent.

src/app/todo.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { z } from "zod";
    import { registerFrontendTool } from "@copilotkit/angular";
    
    @Component({
      selector: "app-todo",
      standalone: true,
      template: `
        <ul>
          @for (todo of todos(); track todo) {
            <li>{{ todo }}</li>
          }
        </ul>
      `,
    })
    export class TodoComponent {
      readonly todos = signal<string[]>([]);
    
      constructor() {
        registerFrontendTool({
          name: "addTodo",
          description: "Add a new item to the user's todo list",
          parameters: z.object({
            text: z.string().describe("The todo item text"),
            priority: z.enum(["low", "medium", "high"]).describe("Priority level"),
          }),
          handler: async ({ text, priority }) => {
            this.todos.update((current) => [...current, text]);
            return `Added "${text}" with ${priority} priority`;
          },
        });
      }
    }

Because the handler runs in the injection context, you can call `inject()` for a service instead of capturing it from the component:

src/app/weather.component.ts
    
    
    import { Component, inject } from "@angular/core";
    import { z } from "zod";
    import { registerFrontendTool } from "@copilotkit/angular";
    import { WeatherService } from "./weather.service";
    
    @Component({
      selector: "app-weather",
      standalone: true,
      template: ``,
    })
    export class WeatherComponent {
      constructor() {
        registerFrontendTool({
          name: "getWeather",
          description: "Fetch weather information for a city",
          parameters: z.object({
            city: z.string().describe("City name"),
            units: z.enum(["celsius", "fahrenheit"]).default("celsius"),
          }),
          handler: async ({ city, units }, { signal }) => {
            const weather = inject(WeatherService);
            const result = await weather.fetch(city, units, { signal });
            return JSON.stringify(result);
          },
        });
      }
    }

### Tool with a custom Angular renderer component

Pass a standalone component as `component` to visualize the tool call in chat. The renderer implements `ToolRenderer<Args>`, so it exposes a `toolCall` signal input that carries the `status`, the (possibly partial) `args`, and the `result`.

src/app/weather-tool-view.component.ts
    
    
    import { Component, input } from "@angular/core";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type WeatherArgs = { city: string; units: "celsius" | "fahrenheit" };
    
    @Component({
      selector: "app-weather-tool-view",
      standalone: true,
      template: `
        @let call = toolCall();
        @if (call.status === "in-progress") {
          <div class="animate-pulse">Fetching weather for {{ call.args.city }}...</div>
        } @else if (call.status === "complete") {
          @let data = parse(call.result);
          <div class="rounded border p-4">
            <h3>{{ data.city }}</h3>
            <p>{{ data.temperature }} {{ data.units }}</p>
            <p>{{ data.conditions }}</p>
          </div>
        }
      `,
    })
    export class WeatherToolViewComponent implements ToolRenderer<WeatherArgs> {
      readonly toolCall = input.required<AngularToolCall<WeatherArgs>>();
    
      protected parse(result: string) {
        return JSON.parse(result);
      }
    }

Register the tool with that component:

src/app/weather.component.ts
    
    
    import { Component, inject } from "@angular/core";
    import { z } from "zod";
    import { registerFrontendTool } from "@copilotkit/angular";
    import { WeatherService } from "./weather.service";
    import { WeatherToolViewComponent } from "./weather-tool-view.component";
    
    @Component({
      selector: "app-weather",
      standalone: true,
      template: ``,
    })
    export class WeatherComponent {
      constructor() {
        registerFrontendTool({
          name: "getWeather",
          description: "Fetch and display weather information for a city",
          parameters: z.object({
            city: z.string().describe("City name"),
            units: z.enum(["celsius", "fahrenheit"]).default("celsius"),
          }),
          handler: async ({ city, units }, { signal }) => {
            const result = await inject(WeatherService).fetch(city, units, { signal });
            return JSON.stringify(result);
          },
          component: WeatherToolViewComponent,
        });
      }
    }

## Related

### [registerComponentLet the agent display one of your components, with no handler and nothing to add on the agent side.](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)### [registerRenderToolCallRegister a renderer for a tool call (including server-side and agentic tools) with full access to status and results.](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)### [registerHumanInTheLoopRegister a tool that pauses the agent and waits for the user to respond from a rendered component.](https://docs.copilotkit.ai/reference/angular/functions/registerHumanInTheLoop)### [CopilotKit serviceThe central service that holds agents, tools, and the runtime connection.](https://docs.copilotkit.ai/reference/angular/services/CopilotKit)
