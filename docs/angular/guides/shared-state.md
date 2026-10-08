---
url: https://docs.copilotkit.ai/angular/guides/shared-state/
title: Shared state and agent context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:30.864864+00:00
---

# Shared state and agent context

> Source: https://docs.copilotkit.ai/angular/guides/shared-state/

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

Shared state and agent context

LearnAngular guides

# Shared state and agent context

Read and write agent state with Angular signals, and send application-owned context to the agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Shared state and agent context solve two different data flows.

Data flow| Use  
---|---  
Agent and application both read and write the value| `injectAgentStore` and `agent.setState`  
The application owns the value and the agent only reads it| `connectAgentContext` or `CopilotKitAgentContext`  
  
## Read agent state#

`injectAgentStore` returns a signal that resolves one agent. The store exposes messages, state, and run status as nested signals.

src/app/workspace.component.ts
    
    
    import { Component, computed } from "@angular/core";
    import { injectAgentStore } from "@copilotkit/angular";
    
    type WorkspaceState = {
      notes: string[];
      priority: "low" | "normal" | "high";
    };
    
    const EMPTY_STATE: WorkspaceState = {
      notes: [],
      priority: "normal",
    };
    
    @Component({
      selector: "app-workspace",
      template: `
        <p>Priority: {{ state().priority }}</p>
        <ul>
          @for (note of state().notes; track note) {
            <li>{{ note }}</li>
          }
        </ul>
        <button type="button" (click)="setPriority('high')">
          Mark high priority
        </button>
      `,
    })
    export class WorkspaceComponent {
      readonly store = injectAgentStore("default");
      readonly state = computed(
        () => (this.store().state() as WorkspaceState | undefined) ?? EMPTY_STATE,
      );
    
      protected setPriority(priority: WorkspaceState["priority"]): void {
        const agent = this.store().agent;
        const current = (agent.state as WorkspaceState | undefined) ?? EMPTY_STATE;
        agent.setState({ ...current, priority });
      }
    }

Read through `store().state()` so Angular tracks changes. Write through the plain AG-UI agent at `store().agent`. Replace the object instead of mutating it in place.

The same store gives you:

  * `store().messages()` for the current conversation
  * `store().isRunning()` for loading controls
  * `store().agent` for `setState`, `addMessage`, `runAgent`, and `abortRun`



## Send read-only application context#

Use `connectAgentContext` for values such as the signed-in user's name, selected record, timezone, or current screen. Pass an accessor so signal reads stay reactive.

src/app/account-context.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { connectAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-account-context",
      template: `
        <button type="button" (click)="timezone.set('Europe/London')">
          Use London time
        </button>
      `,
    })
    export class AccountContextComponent {
      readonly userName = signal("Ada");
      readonly timezone = signal("America/Los_Angeles");
    
      constructor() {
        connectAgentContext(() => ({
          description: "Current account and timezone",
          value: JSON.stringify({
            userName: this.userName(),
            timezone: this.timezone(),
          }),
        }));
      }
    }

The internal effect removes the old context and registers the new value when a read signal changes. It removes the final registration when the owning injector is destroyed. If you already have an `Injector`, pass it as `{ injector }`; that injector takes precedence over the ambient one.

## Bind context in a template#

Use `CopilotKitAgentContext` when the context is already shaped in the template.

src/app/selection-context.component.ts
    
    
    import { Component, computed, signal } from "@angular/core";
    import { CopilotKitAgentContext } from "@copilotkit/angular";
    
    @Component({
      selector: "app-selection-context",
      imports: [CopilotKitAgentContext],
      template: `
        <div [copilotkitAgentContext]="selectionContext()"></div>
      `,
    })
    export class SelectionContextComponent {
      readonly selectedId = signal("record-42");
      readonly selectionContext = computed(() => ({
        description: "The record selected in the application",
        value: this.selectedId(),
      }));
    }

Render the directive only after you have a complete context. If it starts without one, later input changes do not create the first registration.

## Keep ownership clear#

  * Use shared state for data that the agent may change.
  * Use context for application-owned facts.
  * Keep durable user preferences in your own data store; publish only the part the current agent needs.
  * Scope `injectAgentStore` to the same agent id as the chat or workflow that reads the state.



## Next steps#

  * [injectAgentStore API](https://docs.copilotkit.ai/reference/angular/functions/injectAgentStore)
  * [connectAgentContext API](https://docs.copilotkit.ai/reference/angular/functions/connectAgentContext)
  * [CopilotKitAgentContext API](https://docs.copilotkit.ai/reference/angular/directives/CopilotKitAgentContext)
  * [Runnable state examples](https://docs.copilotkit.ai/angular/features#shared-state-read-write)



### On this page

Read agent stateSend read-only application contextBind context in a templateKeep ownership clearNext steps
