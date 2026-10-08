---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotPopup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:09.211827+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotPopup/

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

# CopilotPopup

Vue 3 popup variant of CopilotChat that renders in a floating panel with a toggle button.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This is the Vue 3 popup component. Import it from `@copilotkit/vue/v2`.

`CopilotPopup` renders a floating chat popup with a toggle button. It wraps [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) and provides popup-specific layout, sizing, and open/close behavior. The popup includes a header with a title and close button, and can optionally be dismissed by clicking outside.

The `"popup"` feature requires a license. When it is not licensed, the component renders an inline warning and logs a console warning; see [copilotkit.ai/pricing](https://copilotkit.ai/pricing).

## Example
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup
        agent-id="my-agent"
        :labels="{ modalHeaderTitle: 'Assistant' }"
      />
    </template>

## Props

### Own props

Prop

Type

`defaultOpen?`boolean

Prop

Type

`width?`number | string

Prop

Type

`height?`number | string

Prop

Type

`clickOutsideToClose?`boolean

### Inherited CopilotChat props

`CopilotPopup` extends [`CopilotChatProps`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat), so it accepts the same agent-wiring and chat-view props. The most common ones:

Prop

Type

`agentId?`string

Prop

Type

`threadId?`string

Prop

Type

`labels?`Partial<CopilotChatLabels>

Prop

Type

`autoScroll?`AutoScrollMode | boolean

Prop

Type

`welcomeScreen?`boolean

Prop

Type

`inputValue?`string

Prop

Type

`inputMode?`CopilotChatInputMode

Prop

Type

`inputToolsMenu?`(ToolsMenuItem | "-")[]

Prop

Type

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

## Slots

All slots are forwarded down to the internal `CopilotPopupView`. Each slot receives scoped props you can bind to.

Prop

Type

`header?`(props: CopilotPopupViewHeaderSlotProps) => unknown

Prop

Type

`toggle-button?`(props: CopilotPopupViewToggleButtonSlotProps) => unknown

Prop

Type

`chat-view?`(props: CopilotChatViewOverrideSlotProps) => unknown

Prop

Type

`message-view?`(props: CopilotChatMessageViewSlotProps) => unknown

Prop

Type

`input?`(props: CopilotSidebarWelcomeScreenInputSlotProps) => unknown

Prop

Type

`suggestion-view?`(props: CopilotSidebarWelcomeScreenSuggestionViewSlotProps) => unknown

Prop

Type

`welcome-screen?`(props: CopilotChatWelcomeScreenSlotProps) => unknown

Prop

Type

`welcome-message?`() => unknown

## Events

`CopilotPopup` emits the following events (use kebab-case in templates):

Event| Payload  
---|---  
`submit-message`| `value: string`  
`stop`| (none)  
`input-change`| `value: string`  
`select-suggestion`| `suggestion: Suggestion, index: number`  
`add-file`| (none)  
`start-transcribe`| (none)  
`cancel-transcribe`| (none)  
`finish-transcribe`| (none)  
  
## Usage

### Basic usage
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup
        agent-id="my-agent"
        :labels="{ modalHeaderTitle: 'Assistant' }"
      />
    </template>

### Custom size and click-outside-to-close
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup
        agent-id="my-agent"
        :default-open="false"
        :width="450"
        height="80vh"
        :click-outside-to-close="true"
      />
    </template>

### Custom header slot
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotPopup agent-id="my-agent">
        <template #header="{ title, onClose }">
          <div class="flex items-center justify-between bg-blue-600 px-4 py-2 text-white">
            <span>{{ title }}</span>
            <button type="button" @click="onClose">Close</button>
          </div>
        </template>
      </CopilotPopup>
    </template>

### Handling events
    
    
    <script setup lang="ts">
    import { CopilotPopup } from "@copilotkit/vue/v2";
    
    function onSubmit(value: string) {
      console.log("submitted:", value);
    }
    </script>
    
    <template>
      <CopilotPopup agent-id="my-agent" @submit-message="onSubmit" />
    </template>

## Behavior

  * **Toggle button** : Renders a floating toggle button that opens and closes the popup. Override it with the `toggle-button` slot.
  * **Modal state** : The initial state is set by `defaultOpen`; after mount, state changes come from user interaction (toggle button, close button, clicking outside).
  * **Click outside** : When `clickOutsideToClose` is `true`, clicking outside the popup panel closes it. The default is `false`.
  * **Layout** : Internally uses `CopilotPopupView`, which provides a popup-specific welcome screen layout.
  * **Agent connection** : All agent wiring (messages, running state, suggestions) is handled by the inner `CopilotChat`.



## Related

  * [`CopilotChat`](https://docs.copilotkit.ai/reference/vue/components/CopilotChat) \-- the base chat component used internally
  * [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) \-- supplies the copilot context
  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \-- composable for accessing the agent instance


