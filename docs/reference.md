---
url: https://docs.copilotkit.ai/reference/
title: CopilotKit Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:50.197022+00:00
---

# CopilotKit Docs

> Source: https://docs.copilotkit.ai/reference/

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

Reference

# Overview

Reference documentation for the CopilotKit SDKs. Pick the SDK you're building with, then browse its components, hooks, classes, and types.

## Choose your SDK

### [ReactHooks and components for building CopilotKit into a React app.](https://docs.copilotkit.ai/reference/v2)### [React NativeHeadless provider, prebuilt UI, and hooks for building CopilotKit into a React Native app.](https://docs.copilotkit.ai/reference/react-native)### [VueComposables and components for building CopilotKit into a Vue app.](https://docs.copilotkit.ai/reference/vue)### [AngularComponents, services, and functions for building CopilotKit into an Angular app.](https://docs.copilotkit.ai/reference/angular)### [Core (TypeScript)The framework-agnostic @copilotkit/core client — runs anywhere JavaScript runs.](https://docs.copilotkit.ai/reference/core)### [Channels SDKAPI reference for managed Slack and Microsoft Teams agents built with @copilotkit/channels.](https://docs.copilotkit.ai/reference/channels)

## UI Components

### [<CopilotChat />High-level chat component that connects an agent to a chat view](https://docs.copilotkit.ai/reference/components/CopilotChat)### [<CopilotChatAssistantMessage />Component for displaying assistant messages with Markdown, tool calls, and an action toolbar](https://docs.copilotkit.ai/reference/components/CopilotChatAssistantMessage)### [<CopilotChatInput />Primary text input and control surface for chat interactions](https://docs.copilotkit.ai/reference/components/CopilotChatInput)### [<CopilotChatMessageView />Component for rendering a list of chat messages](https://docs.copilotkit.ai/reference/components/CopilotChatMessageView)### [<CopilotChatUserMessage />Component for displaying user-authored messages with branch navigation](https://docs.copilotkit.ai/reference/components/CopilotChatUserMessage)### [<CopilotChatView />Layout component that combines a scrollable transcript with the input area](https://docs.copilotkit.ai/reference/components/CopilotChatView)### [<CopilotKit />The CopilotKit provider component, wrapping your application.](https://docs.copilotkit.ai/reference/components/CopilotKit)### [<CopilotPopup />Popup variant of CopilotChat that renders in a floating panel with a toggle button](https://docs.copilotkit.ai/reference/components/CopilotPopup)### [<CopilotSidebar />Sidebar variant of CopilotChat that renders in a fixed side panel](https://docs.copilotkit.ai/reference/components/CopilotSidebar)### [<CopilotThreadsDrawer />Prebuilt threads drawer that lists, switches, and manages conversations next to CopilotChat](https://docs.copilotkit.ai/reference/components/CopilotThreadsDrawer)

## Hooks

### [useAgent()React hook for accessing AG-UI agent instances](https://docs.copilotkit.ai/reference/hooks/useAgent)### [useAgentContext()React hook for providing dynamic context to agents](https://docs.copilotkit.ai/reference/hooks/useAgentContext)### [useCapabilities()React hook for reading an agent's declared capabilities](https://docs.copilotkit.ai/reference/hooks/useCapabilities)### [useComponent()Register a React component as a frontend tool renderer in chat](https://docs.copilotkit.ai/reference/hooks/useComponent)### [useConfigureSuggestions()React hook for configuring chat suggestions](https://docs.copilotkit.ai/reference/hooks/useConfigureSuggestions)### [useCopilotChatConfiguration()React hook and provider for chat UI configuration and labels](https://docs.copilotkit.ai/reference/hooks/useCopilotChatConfiguration)### [useCopilotKit()Low-level React hook for accessing the CopilotKit context](https://docs.copilotkit.ai/reference/hooks/useCopilotKit)### [useDefaultRenderTool()Register a wildcard default renderer for unhandled tool calls](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool)### [useFrontendTool()React hook for registering client-side tool handlers with optional UI rendering](https://docs.copilotkit.ai/reference/hooks/useFrontendTool)### [useFrontendTools()React hook for registering a list of client-side tools whose length can change between renders](https://docs.copilotkit.ai/reference/hooks/useFrontendTools)### [useHumanInTheLoop()React hook for interactive tools that pause agent execution and wait for user input](https://docs.copilotkit.ai/reference/hooks/useHumanInTheLoop)### [useInterrupt()React hook for handling agent interrupt events and resuming execution with user input](https://docs.copilotkit.ai/reference/hooks/useInterrupt)### [useRenderTool()Register typed renderers for tool calls, by tool name or wildcard](https://docs.copilotkit.ai/reference/hooks/useRenderTool)### [useRenderToolCall()React hook that returns a renderer function for tool calls in the chat interface](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall)### [useSuggestions()React hook for accessing chat suggestions](https://docs.copilotkit.ai/reference/hooks/useSuggestions)### [useThreads()React hook for listing, managing, and syncing conversation threads with useThreads — rename, archive, delete, and paginate threads with realtime updates via WebSocket.](https://docs.copilotkit.ai/reference/hooks/useThreads)
