---
url: https://docs.copilotkit.ai/reference/react-native/
title: React Native
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:43.783994+00:00
---

# React Native

> Source: https://docs.copilotkit.ai/reference/react-native/

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

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)

# React Native

API reference for @copilotkit/react-native: the headless provider, prebuilt UI components, and hooks for building CopilotKit into a React Native app.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

`@copilotkit/react-native` brings CopilotKit to React Native. It ships a lightweight [provider](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider), a set of prebuilt UI components, hooks built for React Native, and re-exports of the platform-agnostic hooks from `@copilotkit/react-core`. Everything is built on the [AG-UI](https://docs.ag-ui.com) agent protocol, with no DOM, CSS, or web framework dependencies.

The package root **is** the v2 API. Unlike the web SDK, which exposes v2 under a `/v2` subpath, React Native exports the v2 surface directly from `@copilotkit/react-native`.

## Installation
    
    
    npm install @copilotkit/react-native

The prebuilt UI components and native attachments rely on a few peer dependencies. Install the ones you use:
    
    
    npm install @gorhom/bottom-sheet react-native-gesture-handler react-native-reanimated react-native-streamdown

## Polyfills

React Native's JS runtime (Hermes) lacks several Web APIs that CopilotKit depends on (`ReadableStream`, `TextEncoder`, `crypto.getRandomValues`, `DOMException`, `location`). Importing `@copilotkit/react-native` **auto-installs** these polyfills, so no manual import is required.

If you bring your own polyfills, import only the pieces you need before any other code in your entry point:

index.js
    
    
    import "@copilotkit/react-native/polyfills/streams";
    import "@copilotkit/react-native/polyfills/encoding";
    import "@copilotkit/react-native/polyfills/crypto";
    import "@copilotkit/react-native/polyfills/dom";
    import "@copilotkit/react-native/polyfills/location";

## Provider setup

Wrap your app (or a sub-tree) with [`CopilotKitProvider`](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider) to configure the runtime connection:
    
    
    import { CopilotKitProvider } from "@copilotkit/react-native";
    
    export default function App() {
      return (
        <CopilotKitProvider runtimeUrl="https://your-server/api/copilotkit">
          <ChatScreen />
        </CopilotKitProvider>
      );
    }

## Two ways to build the chat UI

The package is organized into two tiers, so you can pick how much UI you write yourself:

Tier| Import| What you get  
---|---|---  
**Headless**| `@copilotkit/react-native`| Primitives that wire up an agent and expose its state. [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat) and [`CopilotModal`](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal) render no UI; you build the interface from React Native views.  
**Prebuilt UI**| `@copilotkit/react-native/components`| Drop-in chat UI: a full-screen [`CopilotChat`](https://docs.copilotkit.ai/reference/react-native/components/CopilotChat#prebuilt-ui), a bottom-sheet [`CopilotModal`](https://docs.copilotkit.ai/reference/react-native/components/CopilotModal#prebuilt-ui), [`CopilotMarkdown`](https://docs.copilotkit.ai/reference/react-native/components/CopilotMarkdown), and [message bubbles](https://docs.copilotkit.ai/reference/react-native/components/AssistantMessage).  
  
The root also exports two prebuilt chrome components: [`CopilotSidebar`](https://docs.copilotkit.ai/reference/react-native/components/CopilotSidebar) (a slide-in drawer) and [`CopilotPopup`](https://docs.copilotkit.ai/reference/react-native/components/CopilotPopup) (a floating action button + overlay).

`CopilotChat` and `CopilotModal` exist in **both** tiers with different props. The root exports are headless; the `/components` exports are prebuilt UI. Each component page documents both, disambiguated by import path.

## API Reference

### [ComponentsProvider, headless primitives, and prebuilt UI: CopilotKitProvider, CopilotChat, CopilotModal, CopilotSidebar, CopilotPopup, and message components.](https://docs.copilotkit.ai/reference/react-native/components/CopilotKitProvider)### [HooksNative attachments and tool rendering plus the platform-agnostic hooks re-exported from react-core: useAgent, useFrontendTool, useHumanInTheLoop, and more.](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent)

## Related

  * [React Native quickstart](https://docs.copilotkit.ai/react-native): create an app, install, and connect your first agent
  * [React (V2) reference](https://docs.copilotkit.ai/reference/v2): the web SDK, where the re-exported hooks behave identically


