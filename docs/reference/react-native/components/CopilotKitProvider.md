---
url: https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider/
title: CopilotKitProvider
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:45.753807+00:00
---

# CopilotKitProvider

> Source: https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React NativeSDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[AssistantMessage](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage)[CopilotChat](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat)[CopilotKitProvider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)[CopilotMarkdown](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown)[CopilotModal](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal)[CopilotPopup](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar)[UserMessage](https://docs.copilotkit.ai/reference/react-native/components/UserMessage)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)[useAgentContext](https://docs.copilotkit.ai/reference/react-native/hooks/useAgentContext)[useAttachments](https://docs.copilotkit.ai/reference/react-native/hooks/useAttachments)[useCapabilities](https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities)[useComponent](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent)[useConfigureSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useConfigureSuggestions)[useCopilotKit](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit)[useFrontendTool](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/react-native/hooks/useHumanInTheLoop)[useInterrupt](https://docs.copilotkit.ai/reference/react-native/hooks/useInterrupt)[useRenderTool](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)[useSuggestions](https://docs.copilotkit.ai/reference/react-native/hooks/useSuggestions)[useThreads](https://docs.copilotkit.ai/reference/react-native/hooks/useThreads)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)Components

# CopilotKitProvider

The React Native provider that configures the CopilotKit runtime connection and shares it with all hooks and components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`CopilotKitProvider` is the React Native provider for CopilotKit. Wrap your app (or the sub-tree that needs a copilot) with it to configure the runtime connection. Every hook and component below it reads the configured client from context.

Importing the package auto-installs the [polyfills](https://docs.copilotkit.ai/reference/react-native#polyfills) CopilotKit needs on Hermes, so you do not have to import them manually before using the provider.

Cloud features (`publicLicenseKey` / license-gated functionality) are not yet supported on React Native. Point `runtimeUrl` at a self-hosted runtime.

Native iOS and Android applications do not have a built-in Inspector yet. The browser Inspector requires a DOM and is intentionally excluded from the React Native dependency graph, so this provider does not expose an inspector prop.

## Import
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native";

## Props

Prop

Type

`children`ReactNode

Prop

Type

`runtimeUrl`string

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

`useSingleEndpoint?`boolean

Prop

Type

`properties?`Record<string, unknown>

Prop

Type

`onError?`(event: { error: Error; code: CopilotKitCoreErrorCode; context: Record<string, any> }) => void | Promise<void>

Prop

Type

`debug?`DebugConfig

Prop

Type

`defaultThrottleMs?`number

## Usage
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native";
    import { SafeAreaProvider } from "react-native-safe-area-context";
    import { ChatScreen } from "./ChatScreen";
    
    export default function App() {
      return (
        <SafeAreaProvider>
          <CopilotKitProvider runtimeUrl="https://your-server/api/copilotkit">
            <ChatScreen />
          </CopilotKitProvider>
        </SafeAreaProvider>
      );
    }

## Behavior

  * **Auto-polyfills** : importing the package installs the Web API polyfills CopilotKit relies on (`ReadableStream`, `TextEncoder`, `crypto.getRandomValues`, `DOMException`, `location`) before any CopilotKit code runs.
  * **Shared render-tool registry** : the provider instantiates the CopilotKit client whose renderer registry is shared with the rest of CopilotKit. Render functions registered by [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool), [`useFrontendTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool) or [`useComponent`](https://docs.copilotkit.ai/reference/react-native/hooks/useComponent) write into that one registry, so they and [`useRenderToolCall`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool#rendering-a-tool-call-outside-the-chat) work anywhere below the provider. There is no second registry and no extra provider to mount for rendering.
  * **Stable references** : header functions and `properties` are memoized internally to avoid effect churn on re-render.



## Related

  * [`useCopilotKit`](https://docs.copilotkit.ai/reference/react-native/hooks/useCopilotKit): access the configured client from any descendant
  * [`useAgent`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent): connect to an agent and read its state
  * [Polyfills](https://docs.copilotkit.ai/reference/react-native#polyfills): what gets installed and how to bring your own


