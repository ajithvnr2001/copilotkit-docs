---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities/
title: useCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:47.919284+00:00
---

# useCapabilities

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useCapabilities/

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

[Reference](https://docs.copilotkit.ai/reference)[react-native](https://docs.copilotkit.ai/reference/react-native)Hooks

# useCapabilities

React hook for reading an agent's declared capabilities

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by an agent. Capabilities describe what an agent supports: tool calling, streaming, multi-agent coordination, human-in-the-loop, and more.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useCapabilities`](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities); only the import path differs.

Capabilities are populated from the runtime `/info` response at connection time. The value is `undefined` until the runtime handshake completes or if the agent doesn't declare capabilities.

## Signature
    
    
    import { useCapabilities } from "@copilotkit/react-native";
    
    function useCapabilities(agentId?: string): AgentCapabilities | undefined

## Parameters

Prop

Type

`agentId?`string

## Return Value

Prop

Type

`capabilities?`AgentCapabilities | undefined

## Usage

### Conditionally render UI based on capabilities

ToolPanel.tsx
    
    
    import { useCapabilities } from "@copilotkit/react-native";
    import { Text, View } from "react-native";
    
    function ToolPanel() {
      const capabilities = useCapabilities();
    
      if (!capabilities?.tools?.supported) {
        return null; // Agent doesn't support tools, so hide the panel
      }
    
      return (
        <View>
          <Text>Tools</Text>
          {capabilities.tools.clientProvided && (
            <Text>This agent accepts client-provided tools.</Text>
          )}
        </View>
      );
    }

### Read capabilities for a specific agent

AgentInfo.tsx
    
    
    import { useCapabilities } from "@copilotkit/react-native";
    import { Text, View } from "react-native";
    
    function AgentInfo({ agentId }: { agentId: string }) {
      const capabilities = useCapabilities(agentId);
    
      if (!capabilities) {
        return <Text>Loading capabilities…</Text>;
      }
    
      return (
        <View>
          <Text>Streaming: {capabilities.transport?.streaming ? "Yes" : "No"}</Text>
          <Text>Tools: {capabilities.tools?.supported ? "Yes" : "No"}</Text>
          <Text>Human-in-the-loop: {capabilities.humanInTheLoop?.supported ? "Yes" : "No"}</Text>
        </View>
      );
    }

## Behavior

  * **Synchronous read** : The hook reads `capabilities` directly from the agent instance. There is no separate loading state or async fetch. The value stays `undefined` until the runtime `/info` handshake populates it, then becomes defined.
  * **Re-renders** : The hook calls `useAgent()` internally, so the component re-renders on agent state, message, and run-status changes (the default `updates` set). If you only need capabilities and want fewer re-renders, read `agent.capabilities` directly via `useAgent({ updates: [] })`.
  * **Stable reference** : The capabilities object reference only changes when the agent reconnects or the runtime response changes. It does not change on every render.



## Related

  * [`useAgent`](https://docs.copilotkit.ai/reference/react-native/hooks/useAgent): access the full agent instance (capabilities are a property of the agent)
  * [AG-UI Protocol](https://docs.copilotkit.ai/agentic-protocols/ag-ui): the protocol that defines the capabilities schema
  * [React (V2) reference](https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities): the web `useCapabilities` this hook mirrors


