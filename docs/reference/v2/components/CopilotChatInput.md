---
url: https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput/
title: CopilotChatInput
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:34:34.147123+00:00
---

# CopilotChatInput

> Source: https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V2)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotChat](https://docs.copilotkit.ai/reference/v2/components/CopilotChat)[CopilotChatAssistantMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatAssistantMessage)[CopilotChatInput](https://docs.copilotkit.ai/reference/v2/components/CopilotChatInput)[CopilotChatMessageView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatMessageView)[CopilotChatUserMessage](https://docs.copilotkit.ai/reference/v2/components/CopilotChatUserMessage)[CopilotChatView](https://docs.copilotkit.ai/reference/v2/components/CopilotChatView)[CopilotKit](https://docs.copilotkit.ai/reference/v2/components/CopilotKit)[CopilotPopup](https://docs.copilotkit.ai/reference/v2/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v2/components/CopilotSidebar)[CopilotThreadsDrawer](https://docs.copilotkit.ai/reference/v2/components/CopilotThreadsDrawer)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v2/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext)[useCapabilities](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useConfigureSuggestions)[useCopilotChatConfiguration](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotChatConfiguration)[useCopilotKit](https://docs.copilotkit.ai/reference/v2/hooks/useCopilotKit)[useDefaultRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useDefaultRenderTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool)[useFrontendTools](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTools)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/v2/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/v2/hooks/useRenderTool)[useRenderToolCall](https://docs.copilotkit.ai/reference/v2/hooks/useRenderToolCall)[useSuggestions](https://docs.copilotkit.ai/reference/v2/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/v2/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Components

# CopilotChatInput

Primary text input and control surface for chat interactions

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotChatInput` is the primary text input and control surface for chat interactions. It provides a multi-line textarea that auto-grows up to a configurable maximum number of rows (default 5), action buttons for sending messages, voice transcription, and file attachment, and an optional tools menu for declarative command surfaces.

The component operates in three modes: `"input"` (default text entry), `"transcribe"` (replaces the textarea with an audio recorder), and `"processing"` (indicates background processing is underway). When text spans multiple rows, the layout stacks the textarea above the control row.

## Import
    
    
    import { CopilotChatInput } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

## Props

Prop

Type

`mode?`"input" | "transcribe" | "processing"

Prop

Type

`value?`string

Prop

Type

`onChange?`(value: string) => void

Prop

Type

`autoFocus?`boolean

Prop

Type

`isRunning?`boolean

Prop

Type

`onSubmitMessage?`(value: string) => void

Prop

Type

`onStop?`() => void

Prop

Type

`onStartTranscribe?`() => void

Prop

Type

`onCancelTranscribe?`() => void

Prop

Type

`onFinishTranscribe?`() => void

Prop

Type

`onFinishTranscribeWithAudio?`(audioBlob: Blob) => Promise<void>

Prop

Type

`onAddFile?`() => void

Prop

Type

`toolsMenu?`(ToolsMenuItem | '-')[]

Prop

Type

`children?`(props: { isMultiline: boolean }) => React.ReactElement

## Slots

All slot props follow the CopilotKit slot system: each accepts a replacement React component, a `className` string that is merged into the default component's classes, or a partial props object that extends the default component.

Prop

Type

`textArea?`SlotProp

Prop

Type

`sendButton?`SlotProp

Prop

Type

`startTranscribeButton?`SlotProp

Prop

Type

`cancelTranscribeButton?`SlotProp

Prop

Type

`finishTranscribeButton?`SlotProp

Prop

Type

`addMenuButton?`SlotProp

Prop

Type

`audioRecorder?`SlotProp

## ToolsMenuItem

The `ToolsMenuItem` type defines items in the tools menu. Items can trigger actions directly or contain nested submenus.
    
    
    type ToolsMenuItem = { label: string } & (
      | { action: () => void }
      | { items: (ToolsMenuItem | "-")[] }
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
    
    
    toolsMenu={[
      { label: "Search", action: () => search() },
      "-",
      { label: "Settings", action: () => openSettings() },
    ]}

### Nested Submenus

Menu items with an `items` array render as expandable submenus:
    
    
    toolsMenu={[
      {
        label: "Export",
        items: [
          { label: "As PDF", action: () => exportPDF() },
          { label: "As CSV", action: () => exportCSV() },
          "-",
          { label: "Print", action: () => printDoc() },
        ],
      },
    ]}

## CopilotChatAudioRecorder

A visual audio waveform component used during transcription mode. It displays a real-time waveform visualization of the microphone input and exposes an imperative API via `ref`.

### Import


### Imperative API

The component exposes the following imperative methods via React `ref`:

Prop

Type

`state?`string

Prop

Type

`start?`() => void

Prop

Type

`stop?`() => void

Prop

Type

`dispose?`() => void

### Usage
    
    
    function CustomRecorder() {
      const recorderRef = useRef(null);
    
      return (
        <div>
          <CopilotChatAudioRecorder ref={recorderRef} />
          <button onClick={() => recorderRef.current?.start()}>Record</button>
          <button onClick={() => recorderRef.current?.stop()}>Stop</button>
        </div>
      );
    }

## Usage

### Basic Chat Input
    
    
    function ChatInput() {
      const [value, setValue] = useState("");
    
      return (
        <CopilotChatInput
          value={value}
          onChange={setValue}
          onSubmitMessage={(text) => {
            sendMessage(text);
            setValue("");
          }}
          autoFocus
        />
      );
    }

### With Voice Transcription
    
    
    function VoiceInput() {
      const [mode, setMode] = useState<"input" | "transcribe">("input");
      const [value, setValue] = useState("");
    
      return (
        <CopilotChatInput
          mode={mode}
          value={value}
          onChange={setValue}
          onSubmitMessage={(text) => sendMessage(text)}
          onStartTranscribe={() => setMode("transcribe")}
          onCancelTranscribe={() => setMode("input")}
          onFinishTranscribeWithAudio={async (blob) => {
            const text = await transcribeAudio(blob);
            setValue(text);
            setMode("input");
          }}
        />
      );
    }

### With Tools Menu
    
    
    function InputWithTools() {
      return (
        <CopilotChatInput
          onSubmitMessage={(text) => sendMessage(text)}
          toolsMenu={[
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
          ]}
        />
      );
    }

### With Stop Button During Execution
    
    
    function ChatInputWithAgent() {
      const { agent } = useAgent();
      const { copilotkit } = useCopilotKit();
    
      return (
        <CopilotChatInput
          isRunning={agent.isRunning}
          onSubmitMessage={(text) => {
            agent.addMessage({
              role: "user",
              content: text,
              id: crypto.randomUUID(),
            });
            // Drive the run through CopilotKit so registered frontend tools
            // execute and the run is tracked for stop.
            copilotkit.runAgent({ agent });
          }}
          onStop={() => copilotkit.stopAgent({ agent })}
          autoFocus
        />
      );
    }

### Custom Layout with Children Render Prop
    
    
    function AdaptiveInput() {
      return (
        <CopilotChatInput onSubmitMessage={(text) => sendMessage(text)}>
          {({ isMultiline }) => (
            <div
              className={
                isMultiline ? "border-2 border-blue-300 rounded-xl p-2" : ""
              }
            >
              {isMultiline && (
                <div className="text-xs text-gray-400 mb-1">Multi-line mode</div>
              )}
            </div>
          )}
        </CopilotChatInput>
      );
    }

### Styled Slots
    
    
    function StyledInput() {
      return (
        <CopilotChatInput
          onSubmitMessage={(text) => sendMessage(text)}
          textArea="font-mono text-sm bg-gray-50 rounded-lg"
          sendButton="bg-green-500 hover:bg-green-600 text-white rounded-full"
        />
      );
    }

## Behavior

  * **Auto-Growing Textarea** : The default textarea automatically expands as the user types, up to a maximum of 5 rows. After reaching the maximum, the textarea becomes scrollable.
  * **Layout Stacking** : When the input text spans multiple rows, the layout switches from inline (textarea and buttons side by side) to stacked (textarea above the control row containing the action buttons).
  * **Mode Switching** : Setting `mode` to `"transcribe"` replaces the textarea with the `audioRecorder` slot component. The transcription control buttons (`cancelTranscribeButton`, `finishTranscribeButton`) replace the standard send button.
  * **Controlled and Uncontrolled** : The component supports both controlled mode (via `value` and `onChange`) and uncontrolled mode (internal state management).
  * **Tools Menu** : The `toolsMenu` prop enables a declarative menu with support for flat items, separators (`"-"`), and nested submenus. The menu button is only rendered when `toolsMenu` is provided.
  * **Slot System** : Each slot prop accepts three forms -- a replacement component, a className string merged into the default, or a partial props object that extends the default component's props.



## Related

  * [`CopilotChatView`](https://docs.copilotkit.ai/reference/components/CopilotChatView) \-- Higher-level chat view that composes this component
  * `CopilotChatAudioRecorder` \-- Audio recorder used during transcription mode
  * [`useCopilotChatConfiguration`](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration) \-- Provider for localized input labels


