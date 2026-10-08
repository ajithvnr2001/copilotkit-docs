---
url: https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider/
title: CopilotKitProvider
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:09.269937+00:00
---

# CopilotKitProvider

> Source: https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider/

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

# CopilotKitProvider

The Vue 3 provider component that wraps your application and supplies the CopilotKit context.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This is the Vue 3 provider component. Import it from `@copilotkit/vue/v2`.

`CopilotKitProvider` typically wraps your entire application (or a sub-tree where you want a copilot). It creates the CopilotKit core instance and provides the copilot context to all descendant components and composables (such as [`useCopilotKit`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit) and [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)).

The wrapped application is rendered through the component's default slot, since Vue uses slots rather than a `children` prop.

## Example
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <!-- ... your app ... -->
      </CopilotKitProvider>
    </template>

Connect to Copilot Cloud with a public API key instead of a self-hosted runtime:
    
    
    <script setup lang="ts">
    import { CopilotKitProvider } from "@copilotkit/vue/v2";
    </script>
    
    <template>
      <CopilotKitProvider public-api-key="ck_pub_your_key">
        <!-- ... your app ... -->
      </CopilotKitProvider>
    </template>

## Properties

You must provide at least one of `runtimeUrl`, `publicApiKey`, or `publicLicenseKey` (or a set of local agents), otherwise the provider warns in development and throws in production.

Prop

Type

`runtimeUrl?`string

Prop

Type

`headers?`Record<string, string> | (() => Record<string, string>)

Prop

Type

`credentials?`RequestCredentials

Prop

Type

`messageFilter?`(messages: Message[], context: { agentId: string }) => Message[]

Prop

Type

`defaultThrottleMs?`number

Prop

Type

`publicApiKey?`string

Prop

Type

`publicLicenseKey?`string

Prop

Type

`licenseToken?`string

Prop

Type

`properties?`Record<string, unknown>

Prop

Type

`useSingleEndpoint?`boolean

Prop

Type

`agents__unsafe_dev_only?`Record<string, AbstractAgent>

Prop

Type

`selfManagedAgents?`Record<string, AbstractAgent>

Prop

Type

`renderToolCalls?`VueToolCallRenderer<any>[]

Prop

Type

`renderActivityMessages?`VueActivityMessageRenderer<unknown>[]

Prop

Type

`renderCustomMessages?`VueCustomMessageRenderer[]

Prop

Type

`frontendTools?`VueFrontendTool[]

Prop

Type

`humanInTheLoop?`VueHumanInTheLoop[]

Prop

Type

`openGenerativeUI?`{ sandboxFunctions?: SandboxFunction[]; designSkill?: string }

Prop

Type

`enableInspector?`boolean

Prop

Type

`showDevConsole?`boolean | "auto"

Prop

Type

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

Prop

Type

`a2ui?`{ theme?: A2UITheme; catalog?: any; loadingComponent?: Component; includeSchema?: boolean }

Prop

Type

`debug?`DebugConfig

## Slots

Prop

Type

`default`slot

## Related

  * [`useCopilotKit`](https://docs.copilotkit.ai/reference/vue/hooks/useCopilotKit) \-- Low-level composable for accessing the provider context
  * [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) \-- High-level composable for accessing agent instances
  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool) \-- Register frontend tools dynamically
  * [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop) \-- Register human-in-the-loop tools dynamically


