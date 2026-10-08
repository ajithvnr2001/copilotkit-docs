---
url: https://docs.copilotkit.ai/angular/guides/chat-ui/
title: Chat UI and customization
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:22.476933+00:00
---

# Chat UI and customization

> Source: https://docs.copilotkit.ai/angular/guides/chat-ui/

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

Chat UI and customization

LearnAngular guides

# Chat UI and customization

Add a full Angular chat, choose its layout, and customize messages, slots, labels, and styles.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`CopilotChat` gives you a complete chat surface backed by the agent from your Copilot Runtime. It owns message streaming, suggestions, the composer, attachments, transcription, and the active thread.

This guide starts from the provider in the [Angular quickstart](https://docs.copilotkit.ai/angular) and shows how to choose and customize the visible chat.

## Choose a chat surface#

Surface| Use it when  
---|---  
`CopilotChat`| Chat belongs inside an existing page or panel.  
`CopilotPopup`| Chat should open from a floating launcher.  
`CopilotSidebar`| Chat should sit beside the main application or open as an overlay.  
`CopilotChatView`| You own the agent wiring and only need the chat layout.  
  
All four are standalone Angular components.

## Add an inline chat#

Import `CopilotChat`, give its host a real height, and point it at an agent when you do not want the default agent.

src/app/support-chat.component.ts
    
    
    import { ChangeDetectionStrategy, Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular";
    
    @Component({
      selector: "app-support-chat",
      imports: [CopilotChat],
      changeDetection: ChangeDetectionStrategy.OnPush,
      template: `
        <section class="chat-shell" aria-label="Support assistant">
          <copilot-chat agentId="support" />
        </section>
      `,
      styles: `
        .chat-shell {
          height: min(48rem, 80vh);
          overflow: hidden;
          border: 1px solid #dbe3eb;
          border-radius: 1rem;
        }
      `,
    })
    export class SupportChatComponent {}

Import the package stylesheet once in the application's global stylesheet:

src/styles.css
    
    
    @import "@copilotkit/angular/styles.css";

## Use a popup or sidebar#

Both modal surfaces manage focus, Escape closing, and launcher-focus restore. Their `open` model supports two-way binding.

src/app/app.component.ts
    
    
    import { Component, signal } from "@angular/core";
    import { CopilotPopup, CopilotSidebar } from "@copilotkit/angular";
    
    @Component({
      selector: "app-root",
      imports: [CopilotPopup, CopilotSidebar],
      template: `
        <copilot-popup
          [(open)]="popupOpen"
          title="Support assistant"
          [clickOutsideToClose]="true"
        />
    
        <copilot-sidebar
          [(open)]="sidebarOpen"
          mode="docked"
          position="right"
          title="Workspace assistant"
          [width]="480"
        />
      `,
    })
    export class AppComponent {
      readonly popupOpen = signal(false);
      readonly sidebarOpen = signal(false);
    }

Compact viewports render the sidebar as a modal even when `mode` is `"docked"`. Only one open docked sidebar can own the page margin at a time.

## Replace an assistant message#

Pass a standalone component class to `assistantMessageComponent`. CopilotKit creates it for each assistant message and binds its `message` input.

src/app/custom-assistant-message.component.ts
    
    
    import { ChangeDetectionStrategy, Component, input } from "@angular/core";
    
    type AssistantMessage = {
      id: string;
      role: "assistant";
      content?: string;
    };
    
    @Component({
      selector: "app-custom-assistant-message",
      changeDetection: ChangeDetectionStrategy.OnPush,
      template: `
        <article class="answer">
          <span class="answer__label">Assistant</span>
          <p>{{ message().content }}</p>
        </article>
      `,
    })
    export class CustomAssistantMessageComponent {
      readonly message = input.required<AssistantMessage>();
    }

src/app/support-chat.component.ts
    
    
    import { Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular";
    import { CustomAssistantMessageComponent } from "./custom-assistant-message.component";
    
    @Component({
      selector: "app-support-chat",
      imports: [CopilotChat],
      template: `
        <copilot-chat
          [assistantMessageComponent]="assistantMessageComponent"
          assistantMessageClass="support-answer"
        />
      `,
    })
    export class SupportChatComponent {
      protected readonly assistantMessageComponent =
        CustomAssistantMessageComponent;
    }

`CopilotChat` also accepts component or template slots for reasoning messages, the composer, and content after the transcript. Use `CopilotChatView` directly when you need its scroll view, disclaimer, feather, input-container, or scroll-to-bottom slots.

## Scope CSS changes#

The package stylesheet exposes stable chat classes. Put a scope class on your feature host so the change stays local.

src/styles.css
    
    
    .support-chat .copilotKitUserMessage {
      color: white;
      background: #2563eb;
      border-radius: 0.75rem;
    }
    
    .support-chat .copilotKitAssistantMessage {
      padding: 0.75rem;
      color: #172554;
      background: #eff6ff;
      border-radius: 0.75rem;
    }

## Next steps#

  * [CopilotChat API](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)
  * [CopilotChatView slots](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)
  * [CopilotPopup API](https://docs.copilotkit.ai/reference/angular/components/CopilotPopup)
  * [CopilotSidebar API](https://docs.copilotkit.ai/reference/angular/components/CopilotSidebar)
  * [Runnable chat examples](https://docs.copilotkit.ai/angular/features#agentic-chat)



### On this page

Choose a chat surfaceAdd an inline chatUse a popup or sidebarReplace an assistant messageScope CSS changesNext steps
