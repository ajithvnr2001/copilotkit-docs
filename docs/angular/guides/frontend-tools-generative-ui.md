---
url: https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui/
title: Frontend tools and generative UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:28.314121+00:00
---

# Frontend tools and generative UI

> Source: https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui/

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

Frontend tools and generative UI

LearnAngular guides

# Frontend tools and generative UI

Let an agent run browser code and render typed, protocol-driven, or sandboxed UI in Angular.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Frontend tools let an agent call code inside the user's browser. Add a renderer to the same registration when the tool should show progress or a result in chat.

## Let the agent display one of your components#

The simplest generative UI there is, and the only kind that needs nothing on the agent side. `registerComponent` registers a standalone component as a tool the agent can call to show it. The agent decides when, and fills the props.

src/app/incident-card.component.ts
    
    
    import { Component, input } from "@angular/core";
    import { AngularToolCall, ToolRenderer } from "@copilotkit/angular";
    
    type IncidentArgs = { id: string; severity: string };
    
    @Component({
      selector: "app-incident-card",
      standalone: true,
      template: `
        @let call = toolCall();
        @if (call.status === "in-progress") {
          <p>Loading incident…</p>
        } @else {
          <article>
            <strong>{{ call.args.id }}</strong>
            <span>{{ call.args.severity }}</span>
          </article>
        }
      `,
    })
    export class IncidentCardComponent implements ToolRenderer<IncidentArgs> {
      readonly toolCall = input.required<AngularToolCall<IncidentArgs>>();
    }
    
    
    registerComponent({
      name: "show_incident",
      description: "Show one incident from the incident table.",
      parameters: z.object({
        id: z.string().describe("The incident id, such as INC-4711"),
        severity: z.string().describe("One of sev1, sev2, sev3"),
      }),
      component: IncidentCardComponent,
    });

There is no `handler`, and nothing changes in your agent. The tool is declared by the frontend and forwarded over AG-UI, so this works the same behind a Python agent as a TypeScript one.

A well-formed component is not a correct one

The model fills these props from what it knows. A card rendered over records your application does not hold looks the same in the browser, in a screenshot, and in a video as a correct one. Share the page's data with the agent using [`CopilotKitAgentContext`](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext), then read the rendered fields against the records you hold.

## Register a browser tool#

Call `registerFrontendTool` from an Angular injection context. The live Showcase example builds a typed tool config around a writable signal:

tool-feature-model.ts
    
    
    /** Create the frontend tool that applies a requested CSS gradient. */export function createBackgroundTool(  background: WritableSignal<string>,): FrontendToolConfig<BackgroundToolArgs> {  return {    name: "change_background",    description: "Change the application background to a CSS gradient.",    parameters: z.object({      background: z.string().optional(),      color: z.string().optional(),    }),    handler: async (args) => {      const next = resolveGradient(args.background ?? args.color);      background.set(next);      return { background: next };    },  };}

Register that config from a component or service with `registerFrontendTool(createBackgroundTool(background))`. The registration is removed when that injector is destroyed.

The schema advertises the input shape and supplies TypeScript inference. Runtime arguments arrive as parsed JSON; validate inside the handler when the action needs a hard trust boundary. The handler receives the calling agent, the raw tool call, and an optional abort signal as its second argument.

## Render a tool result#

A renderer is a standalone component with a required `toolCall` signal input. Its status moves through `"in-progress"`, `"executing"`, and `"complete"`.

src/app/weather-card.component.ts
    
    
    import { Component, input } from "@angular/core";
    import {
      type AngularToolCall,
      type ToolRenderer,
    } from "@copilotkit/angular";
    
    type WeatherArgs = { city: string };
    
    @Component({
      selector: "app-weather-card",
      template: `
        @let call = toolCall();
        @if (call.status === "complete") {
          <article>
            <strong>{{ call.args.city }}</strong>
            <p>{{ call.result }}</p>
          </article>
        } @else {
          <p>Loading weather for {{ call.args.city ?? "…" }}</p>
        }
      `,
    })
    export class WeatherCardComponent implements ToolRenderer<WeatherArgs> {
      readonly toolCall = input.required<AngularToolCall<WeatherArgs>>();
    }

Pass the class as `component` when the tool runs in the browser:
    
    
    registerFrontendTool({
      name: "getWeather",
      description: "Get the current weather for a city",
      parameters: z.object({ city: z.string() }),
      component: WeatherCardComponent,
      handler: async ({ city }, { signal }) => {
        const response = await fetch(`/api/weather?city=${encodeURIComponent(city)}`, {
          signal,
        });
        return response.text();
      },
    });

Use `registerRenderToolCall` instead when the tool runs on the server and the browser only renders its call:
    
    
    registerRenderToolCall({
      name: "getWeather",
      args: z.object({ city: z.string() }),
      component: WeatherCardComponent,
    });

## Choose a generative UI path#

Path| Best fit| Angular setup  
---|---|---  
Your components, display only| The agent should show a component and nothing else runs| `registerComponent`  
Your components| Known data shapes and application actions| `registerFrontendTool` or `registerRenderToolCall` with a component  
A2UI| A server emits A2UI operations or snapshots| Set `a2ui.catalog` in `provideCopilotKit` to turn on the built-in renderer; without a catalog A2UI stays off  
Open Generative UI| The agent produces streamed HTML, CSS, and script expressions| Set `openGenerativeUI` in `provideCopilotKit`  
MCP Apps| An MCP server returns an interactive app resource| Add `provideMCPApps()` from `@copilotkit/angular/mcp-apps`  
  
### Open Generative UI#

An `openGenerativeUI` object opts the frontend into the built-in sandboxed renderer. Expose narrow host functions when generated UI must ask the application to act.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import {
      provideCopilotKit,
      type SandboxFunction,
    } from "@copilotkit/angular";
    import { z } from "zod";
    
    const setDashboardFilter: SandboxFunction<{ filter: string }> = {
      name: "setDashboardFilter",
      description: "Set the active dashboard filter",
      parameters: z.object({ filter: z.string() }),
      handler: async ({ filter }) => {
        sessionStorage.setItem("dashboard-filter", filter);
        return { applied: filter };
      },
    };
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "/api/copilotkit",
          openGenerativeUI: {
            sandboxFunctions: [setDashboardFilter],
          },
        }),
      ],
    };

Generated code runs in a sandboxed iframe without same-origin access. It calls only the host functions you list in `sandboxFunctions`.

### MCP Apps#

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular";
    import { provideMCPApps } from "@copilotkit/angular/mcp-apps";
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({ runtimeUrl: "/api/copilotkit" }),
        provideMCPApps(),
      ],
    };

MCP resource and tool requests travel through the selected AG-UI agent. The browser provider does not take a server URL.

## Next steps#

  * [registerComponent API](https://docs.copilotkit.ai/reference/angular/functions/registerComponent)
  * [registerFrontendTool API](https://docs.copilotkit.ai/reference/angular/functions/registerFrontendTool)
  * [registerRenderToolCall API](https://docs.copilotkit.ai/reference/angular/functions/registerRenderToolCall)
  * [Activity renderers](https://docs.copilotkit.ai/reference/angular/functions/registerRenderActivityMessage)
  * [Runnable tool and generative UI examples](https://docs.copilotkit.ai/angular/features#frontend-tools)



### On this page

Let the agent display one of your componentsRegister a browser toolRender a tool resultChoose a generative UI pathOpen Generative UIMCP AppsNext steps
