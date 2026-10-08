---
url: https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput/
title: CopilotChatInput
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:53.380598+00:00
---

# CopilotChatInput

> Source: https://docs.copilotkit.ai/reference/angular/components/CopilotChatInput/

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

[Reference](https://docs.copilotkit.ai/reference)[angular](https://docs.copilotkit.ai/reference/angular)Components

# CopilotChatInput

Angular standalone component for chat input, tools, file upload, and audio transcription

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatInput` is the input area of the chat. It renders the textarea, the send button, an optional tools menu, an add-file button, and the audio transcription controls. It has three modes: `"input"` (the default textarea), `"transcribe"` (records audio and shows transcription controls), and `"processing"` (disables the textarea and send button while the agent runs).

`CopilotChatInput` requires a parent injector to provide `ChatState`. It reads that state through `injectChatState` and wires submission, value changes, transcription, and file uploads to it. Its outputs fire in addition to that built-in behavior, so you can observe interactions without disabling them.

## Usage

`CopilotChatInput` is a standalone component with the selector `copilot-chat-input`. The example below provides the required `ChatState`. Use [`CopilotChat`](https://docs.copilotkit.ai/reference/angular/components/CopilotChat) when you want CopilotKit to manage this state for you.

src/app/chat.component.ts
    
    
    import { Component, forwardRef, signal } from "@angular/core";
    import { ChatState, CopilotChatInput } from "@copilotkit/angular";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      imports: [CopilotChatInput],
      providers: [
        {
          provide: ChatState,
          useExisting: forwardRef(() => ChatComponent),
        },
      ],
      template: `
        <copilot-chat-input
          [autoFocus]="true"
          (submitMessage)="onSubmit($event)"
        />
      `,
    })
    export class ChatComponent extends ChatState {
      readonly inputValue = signal("");
    
      submitInput(value: string) {
        // Send the message through your chat state owner.
        console.log("user submitted:", value);
      }
    
      changeInput(value: string) {
        this.inputValue.set(value);
      }
    }

## Inputs

### Behavior inputs

Prop

Type

`mode?`"input" | "transcribe" | "processing"

Prop

Type

`toolsMenu?`(ToolsMenuItem | "-")[]

Prop

Type

`autoFocus?`boolean

Prop

Type

`value?`string

Prop

Type

`inputClass?`string

Prop

Type

`additionalToolbarItems?`TemplateRef<any>

### Textarea inputs

Prop

Type

`textAreaClass?`string

Prop

Type

`textAreaMaxRows?`number

Prop

Type

`textAreaPlaceholder?`string

### Slot override inputs

Each interactive piece can be replaced with a component class (`*Component`). Templates for the same slots are read from content projection.

Prop

Type

`sendButtonComponent?`Type<any>

Prop

Type

`toolbarComponent?`Type<any>

Prop

Type

`textAreaComponent?`Type<any>

Prop

Type

`audioRecorderComponent?`Type<any>

Prop

Type

`startTranscribeButtonComponent?`Type<any>

Prop

Type

`cancelTranscribeButtonComponent?`Type<any>

Prop

Type

`finishTranscribeButtonComponent?`Type<any>

Prop

Type

`addFileButtonComponent?`Type<any>

Prop

Type

`toolsButtonComponent?`Type<any>

The current release declares class inputs for the toolbar, audio recorder, transcription buttons, add-file button, and tools button, but does not apply them. `sendButtonClass` and `textAreaClass` do apply.

## Outputs

These events fire in addition to the input's built-in handling, so you can observe interactions without replacing default behavior.

Prop

Type

`submitMessage?`string

Prop

Type

`valueChange?`string

Prop

Type

`startTranscribe?`void

Prop

Type

`cancelTranscribe?`void

Prop

Type

`finishTranscribe?`void

Prop

Type

`finishTranscribeWithAudio?`Blob

Prop

Type

`addFile?`void

## Slots

For deep customization, provide named `<ng-template>` elements inside `<copilot-chat-input>`. Each is read with `contentChild` and takes precedence over the corresponding `*Component` input. The send button and toolbar templates receive a typed context.

Prop

Type

`sendButton?`TemplateRef<SendButtonContext>

Prop

Type

`toolbar?`TemplateRef<ToolbarContext>

Prop

Type

`textArea?`TemplateRef<any>

Prop

Type

`audioRecorder?`TemplateRef<any>

Prop

Type

`startTranscribeButton?`TemplateRef<any>

Prop

Type

`cancelTranscribeButton?`TemplateRef<any>

Prop

Type

`finishTranscribeButton?`TemplateRef<any>

Prop

Type

`addFileButton?`TemplateRef<any>

Prop

Type

`toolsButton?`TemplateRef<any>

### Tools menu example

src/app/chat.component.ts
    
    
    import { Component, forwardRef, signal } from "@angular/core";
    import { ChatState, CopilotChatInput } from "@copilotkit/angular";
    import type { ToolsMenuItem } from "@copilotkit/angular";
    
    @Component({
      selector: "app-chat",
      standalone: true,
      imports: [CopilotChatInput],
      providers: [
        {
          provide: ChatState,
          useExisting: forwardRef(() => ChatComponent),
        },
      ],
      template: `
        <copilot-chat-input [toolsMenu]="toolsMenu" />
      `,
    })
    export class ChatComponent extends ChatState {
      readonly inputValue = signal("");
      toolsMenu: (ToolsMenuItem | "-")[] = [
        { label: "Summarize", action: () => this.summarize() },
        "-",
        { label: "Translate", action: () => this.translate() },
      ];
    
      summarize() {}
      translate() {}
    
      submitInput(value: string) {
        // Send the message through your chat state owner.
      }
    
      changeInput(value: string) {
        this.inputValue.set(value);
      }
    }

## Related

### [CopilotChatThe all-in-one component that wires an agent and renders this input through the chat view.](https://docs.copilotkit.ai/reference/angular/components/CopilotChat)### [CopilotChatViewThe layout-only chat view that renders this input by default.](https://docs.copilotkit.ai/reference/angular/components/CopilotChatView)### [provideCopilotKitConfigures the runtime connection and agents that power the chat.](https://docs.copilotkit.ai/reference/angular/functions/provideCopilotKit)
