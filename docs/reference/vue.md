---
url: https://docs.copilotkit.ai/reference/vue/
title: Vue
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:06.262207+00:00
---

# Vue

> Source: https://docs.copilotkit.ai/reference/vue/

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

[Reference](https://docs.copilotkit.ai/reference)[vue](https://docs.copilotkit.ai/reference/vue)

# Vue

API reference for @copilotkit/vue: the CopilotKit provider, prebuilt chat components, and composables for building CopilotKit into a Vue 3 app.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`@copilotkit/vue` brings CopilotKit to Vue 3. It ships a [provider](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider), a set of prebuilt chat components, and composables that mirror the React SDK. Everything is built on the [AG-UI](https://docs.ag-ui.com) agent protocol.

The v2 API lives under the `/v2` subpath, the same convention used by the web SDK. Import the provider, components, and composables from `@copilotkit/vue/v2`.

## Installation
    
    
    npm install @copilotkit/vue

## Styling

When using the prebuilt UI components, import the stylesheet once at your app entry point:
    
    
    import "@copilotkit/vue/styles.css";

## Provider setup

Wrap your app (or a sub-tree) with [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/vue/components/CopilotKitProvider) to configure the runtime connection. Composables and components read this context through Vue's [provide/inject](https://vuejs.org/guide/components/provide-inject), so they must be used within the provider.
    
    
    <script setup lang="ts">
    import { CopilotKitProvider, CopilotChat } from "@copilotkit/vue/v2";
    import "@copilotkit/vue/styles.css";
    </script>
    
    <template>
      <CopilotKitProvider runtime-url="/api/copilotkit">
        <CopilotChat />
      </CopilotKitProvider>
    </template>

## Vue conventions

A few patterns recur across this reference and differ from the React SDK:

  * **Composables return refs.** A composable such as [`useAgent`](https://docs.copilotkit.ai/reference/vue/hooks/useAgent) returns reactive refs (for example `{ agent }`). Read them with `.value` in `<script setup>`, or unwrapped directly in templates.
  * **Reactive arguments.** Many composables accept `MaybeRefOrGetter` arguments, so you can pass a plain value, a `ref`, or a getter and the composable stays reactive to changes.
  * **Props are kebab-case in templates.** Component props are documented with their camelCase names but are written as kebab-case attributes in templates (for example `runtimeUrl` becomes `runtime-url`).
  * **Slots replace render props.** Where the React SDK uses render props or `children`, the Vue components expose named [slots](https://vuejs.org/guide/components/slots) for the same customization.



## API Reference

Looking for tool rendering composables? Start with [`useFrontendTool`](https://docs.copilotkit.ai/reference/vue/hooks/useFrontendTool), [`useRenderTool`](https://docs.copilotkit.ai/reference/vue/hooks/useRenderTool), and [`useHumanInTheLoop`](https://docs.copilotkit.ai/reference/vue/hooks/useHumanInTheLoop).

### [ComposablesVue composables for agents, tools, context, suggestions, and chat configuration.](https://docs.copilotkit.ai/reference/vue/hooks/useAgent)### [UI ComponentsPrebuilt chat components: CopilotChat, CopilotPopup, CopilotSidebar, and more.](https://docs.copilotkit.ai/reference/vue/components/CopilotChat)
