---
url: https://docs.copilotkit.ai/reference/components/CopilotKit/
title: CopilotKit
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:30.370901+00:00
---

# CopilotKit

> Source: https://docs.copilotkit.ai/reference/components/CopilotKit/

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

# CopilotKit

The CopilotKit provider component, wrapping your application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This is the v1 provider, re-exported for back-compat

`<CopilotKit>` is the v1 provider. It is re-exported from `@copilotkit/react-core/v2` so that a v1 application keeps working after the import path changes, and it renders `<CopilotKitProvider>` internally. **The v2 provider is`<CopilotKitProvider>`** — reach for that one in new v2 code.

The two are not aliases: they name the agent with different props.

| v1 `<CopilotKit>`| v2 `<CopilotKitProvider>`  
---|---|---  
Name the agent| `agent="my_agent"`| `agentId="my_agent"`  
  
You can also name the agent per chat with `<CopilotChat agentId="my_agent">`, or for a subtree with `<CopilotChatConfigurationProvider agentId="my_agent">`. Both of those override the provider-level default. See [Provider and handler pairs](https://docs.copilotkit.ai/backend/runtime-endpoints#provider-and-handler-pairs).

Both providers treat an omitted `useSingleEndpoint` the same way: the transport is negotiated from the Runtime info response. Versions before 1.70.2 pinned `<CopilotKit>` to the single-route transport.

This component will typically wrap your entire application (or a sub-tree of your application where you want to have a copilot). It provides the copilot context to all other components and hooks.

## Example

You can find more information about self-hosting CopilotKit [here](https://docs.copilotkit.ai/direct-to-llm/guides/self-hosting).
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";
    
    <CopilotKit runtimeUrl="<your-runtime-url>">// ... your app ...</CopilotKit>;

## Properties

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

`guardrails_c?`{ validTopics?: string[]; invalidTopics?: string[]; }

Prop

Type

`runtimeUrl?`string

Prop

Type

`transcribeAudioUrl?`string

Prop

Type

`textToSpeechUrl?`string

Prop

Type

`headers?`Record<string, string> | (() => Record<string, string>)

Prop

Type

`children`ReactNode

Prop

Type

`properties?`Record<string, any>

Prop

Type

`credentials?`RequestCredentials

Prop

Type

`showDevConsole?`boolean

Prop

Type

`showIntelligenceIndicator?`boolean

Prop

Type

`selfManagedAgents?`Record<string, AbstractAgent>

Prop

Type

`agents__unsafe_dev_only?`Record<string, AbstractAgent>

Prop

Type

`a2ui?`{ theme?: Theme }

Prop

Type

`openGenerativeUI?`{ sandboxFunctions?: SandboxFunction[]; designSkill?: string }

Prop

Type

`defaultThrottleMs?`number

Prop

Type

`agent?`string

Prop

Type

`forwardedParameters?`Pick<ForwardedParametersInput, 'temperature'>

Prop

Type

`authConfig_c?`{ SignInComponent: React.ComponentType<{ onSignInComplete: (authState: AuthState) => void; }>; }

Prop

Type

`threadId?`string

Prop

Type

`onError?`CopilotErrorHandler

Prop

Type

`enableInspector?`boolean

Prop

Type

`debug?`DebugConfig
