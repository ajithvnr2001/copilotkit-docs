---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput/
title: CopilotChatInput
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:06.671112+00:00
---

# CopilotChatInput

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁VueSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/vue/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/vue/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/vue/components/CopilotChatView)[CopilotKitProvider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider)[CopilotPopup](https://docs.copilotkit.ai/reference/vue/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/vue/components/CopilotSidebar)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/vue/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/vue/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/vue/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/vue/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/vue/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/vue/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)Components

# CopilotChatInput

Primary text input and control surface for chat interactions in Vue 3

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatInput` is the Vue 3 primary text input and control surface for chat interactions. It provides a multi-line textarea that auto-grows up to a configurable maximum number of rows (default 5), action buttons for sending messages and voice transcription, and an optional tools menu for declarative command surfaces (which also surfaces a file-attachment item when you bind `@add-file`, and is reachable via inline `/` slash commands).

The component operates in three modes: `"input"` (default text entry), `"transcribe"` (replaces the textarea with an audio recorder), and `"processing"` (shows a spinner while background processing is underway). When text spans multiple rows, the layout stacks the textarea above the control row.

It supports both `v-model` (via `modelValue` / `update:modelValue`) and uncontrolled usage. When uncontrolled, the component manages its own text state internally and clears on submit (configurable via `clearOnSubmit`).

The transcription buttons (microphone, cancel, finish) are only rendered when their corresponding event has a listener attached — for example, the microphone button appears only when you bind `@start-transcribe`. The send button, by contrast, always renders: it stays disabled until a `@submit-message` listener is attached and the input is non-empty, and while the agent is running it switches to a stop affordance that is enabled only when a `@stop` listener is attached. Binding `@add-file` adds a file-attachment item to the tools menu rather than a standalone button. This means you opt into features by listening for the events you intend to handle.

## Import
    
    
    <script setup lang="ts">
    import { CopilotChatInput } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>

## Example
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatInput } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    
    const value = ref("");
    
    function handleSubmit(text: string) {
      sendMessage(text);
    }
    </script>
    
    <template>
      <CopilotChatInput v-model="value" @submit-message="handleSubmit" />
    </template>

## Props

Prop

Type

`modelValue?`string

Prop

Type

`mode?`"input" | "transcribe" | "processing"

Prop

Type

`disabled?`boolean

Prop

Type

`placeholder?`string

Prop

Type

`autoFocus?`boolean

Prop

Type

`clearOnSubmit?`boolean

Prop

Type

`isRunning?`boolean

Prop

Type

`toolsMenu?`(ToolsMenuItem | '-')[]

Prop

Type

`maxRows?`number

Prop

Type

`positioning?`"static" | "absolute"

Prop

Type

`keyboardHeight?`number

Prop

Type

`showDisclaimer?`boolean

Prop

Type

`bottomAnchored?`boolean

## Events

`CopilotChatInput` emits the following events. Bind handlers with `v-on` (the `@` shorthand). Several action buttons only render when their corresponding event has a listener attached.

Prop

Type

`update:modelValue?`(value: string) => void

Prop

Type

`submit-message?`(value: string) => void

Prop

Type

`stop?`() => void

Prop

Type

`add-file?`() => void

Prop

Type

`start-transcribe?`() => void

Prop

Type

`cancel-transcribe?`() => void

Prop

Type

`finish-transcribe?`() => void

Prop

Type

`finish-transcribe-with-audio?`(audioBlob: Blob) => void

## Slots

`CopilotChatInput` exposes named slots so you can override individual parts of the UI while keeping the component's behavior. Each slot receives scoped slot props (event handlers, state, and labels) so your custom markup can drive the same logic as the defaults.

Prop

Type

`text-area?`slot

Prop

Type

`send-button?`slot

Prop

Type

`add-menu-button?`slot

Prop

Type

`start-transcribe-button?`slot

Prop

Type

`cancel-transcribe-button?`slot

Prop

Type

`finish-transcribe-button?`slot

Prop

Type

`audio-recorder?`slot

Prop

Type

`disclaimer?`slot

Prop

Type

`layout?`slot

## ToolsMenuItem

The `ToolsMenuItem` type defines items in the tools menu. Items can trigger actions directly or contain nested submenus.
    
    
    type ToolsMenuItem = { label: string } & (
      | { action: () => void; items?: never }
      | { action?: never; items: (ToolsMenuItem | "-")[] }
    );

Prop

Type

`label`string

Prop

Type

`action?`() => void

Prop

Type

`items?`(ToolsMenuItem | '-')[]

### Separators

Use the string `"-"` as an array entry to render a visual separator between menu items:
    
    
    const toolsMenu = [
      { label: "Search", action: () => search() },
      "-",
      { label: "Settings", action: () => openSettings() },
    ];

### Nested Submenus

Menu items with an `items` array render as expandable submenus:
    
    
    const toolsMenu = [
      {
        label: "Export",
        items: [
          { label: "As PDF", action: () => exportPDF() },
          { label: "As CSV", action: () => exportCSV() },
          "-",
          { label: "Print", action: () => printDoc() },
        ],
      },
    ];

## CopilotChatAudioRecorder

A visual audio waveform component used during transcription mode. It displays a real-time waveform visualization of the microphone input and exposes an imperative API via a template `ref`.

### Import
    
    
    <script setup lang="ts">
    import { CopilotChatAudioRecorder } from "@copilotkit/vue/v2";
    </script>

### Imperative API (CopilotChatAudioRecorderRef)

The component exposes the following members via a template `ref`:

Prop

Type

`state?`"idle" | "recording" | "processing"

Prop

Type

`start?`() => Promise<void>

Prop

Type

`stop?`() => Promise<Blob>

Prop

Type

`dispose?`() => void

### Usage
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatAudioRecorder } from "@copilotkit/vue/v2";
    
    // The component exposes `start()` / `stop()` via its instance type.
    const recorder = ref<InstanceType<typeof CopilotChatAudioRecorder> | null>(null);
    </script>
    
    <template>
      <CopilotChatAudioRecorder ref="recorder" />
      <button @click="recorder?.start()">Record</button>
      <button @click="recorder?.stop()">Stop</button>
    </template>

## Usage

### With Voice Transcription
    
    
    <script setup lang="ts">
    import { ref } from "vue";
    import { CopilotChatInput } from "@copilotkit/vue/v2";
    
    const value = ref("");
    const mode = ref<"input" | "transcribe">("input");
    
    async function handleFinishWithAudio(blob: Blob) {
      value.value = await transcribeAudio(blob);
      mode.value = "input";
    }
    </script>
    
    <template>
      <CopilotChatInput
        v-model="value"
        :mode="mode"
        @submit-message="(text) => sendMessage(text)"
        @start-transcribe="mode = 'transcribe'"
        @cancel-transcribe="mode = 'input'"
        @finish-transcribe-with-audio="handleFinishWithAudio"
      />
    </template>

### With Tools Menu
    
    
    <script setup lang="ts">
    import { CopilotChatInput, type ToolsMenuItem } from "@copilotkit/vue/v2";
    
    const toolsMenu: (ToolsMenuItem | "-")[] = [
      { label: "Search the web", action: () => triggerSearch() },
      { label: "Analyze data", action: () => triggerAnalysis() },
      "-",
      {
        label: "Export",
        items: [
          { label: "As PDF", action: () => exportPDF() },
          { label: "As Markdown", action: () => exportMarkdown() },
        ],
      },
    ];
    </script>
    
    <template>
      <CopilotChatInput
        :tools-menu="toolsMenu"
        @submit-message="(text) => sendMessage(text)"
      />
    </template>

### With Stop Button During Execution
    
    
    <script setup lang="ts">
    import { CopilotChatInput, useAgent, useCopilotKit } from "@copilotkit/vue/v2";
    
    const { agent } = useAgent();
    const { copilotkit } = useCopilotKit();
    
    function handleSubmit(text: string) {
      if (!agent.value) return;
      agent.value.addMessage({
        role: "user",
        content: text,
        id: crypto.randomUUID(),
      });
      // Drive the run through CopilotKit so registered frontend tools execute and
      // the run is tracked for stop/abort.
      copilotkit.value.runAgent({ agent: agent.value });
    }
    
    function handleStop() {
      if (!agent.value) return;
      copilotkit.value.stopAgent({ agent: agent.value });
    }
    </script>
    
    <template>
      <CopilotChatInput
        :is-running="agent?.isRunning ?? false"
        auto-focus
        @submit-message="handleSubmit"
        @stop="handleStop"
      />
    </template>

### Styled Slots
    
    
    <script setup lang="ts">
    import { CopilotChatInput } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotChatInput @submit-message="(text) => sendMessage(text)">
        <template #send-button="{ disabled, onClick }">
          <button
            :disabled="disabled"
            class="rounded-full bg-green-500 px-3 py-1 text-white"
            @click="onClick"
          >
            Send
          </button>
        </template>
      </CopilotChatInput>
    </template>

## Behavior

  * **Auto-Growing Textarea** : The default textarea automatically expands as the user types, up to `maxRows` rows (default 5). After reaching the maximum, the textarea becomes scrollable.
  * **Layout Stacking** : When the input text spans multiple rows, the layout switches from inline (textarea and buttons side by side) to stacked (textarea above the control row containing the action buttons). On narrow viewports the stacked layout is used unconditionally.
  * **Mode Switching** : Setting `mode` to `"transcribe"` replaces the textarea with the `audio-recorder` slot and automatically starts the recorder. The cancel and finish buttons replace the standard send button. Setting `mode` to `"processing"` shows a spinner in place of the textarea.
  * **Controlled and Uncontrolled** : The component supports controlled mode (via `v-model` / `modelValue`) and uncontrolled mode (internal state). With `clearOnSubmit` enabled (the default), the input clears after each submission.
  * **Tools Menu and Slash Commands** : A non-empty `toolsMenu` renders a menu button and also exposes the leaf actions as `/` slash commands typed inline. Use arrow keys to navigate the slash menu and Enter to run the highlighted command.
  * **Listener-Gated Controls** : The transcription buttons (microphone, cancel, finish) are only rendered when their corresponding event listener is attached. The send button always renders but stays disabled until a `@submit-message` listener is attached and the input is non-empty; while the agent is running it switches to a stop affordance, enabled only when a `@stop` listener is attached. Binding `@add-file` adds a file-attachment item to the tools menu (not a standalone button). You opt into each feature by handling its event.



## Related

  * [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotChatConfiguration) \-- Provider/composable for localized input labels
  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \-- Access the active agent to drive submission and stop handling


