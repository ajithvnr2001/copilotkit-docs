---
url: https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities/
title: useCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:06.419344+00:00
---

# useCapabilities

> Source: https://docs.copilotkit.ai/reference/v2/hooks/useCapabilities/

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

[Reference](https://docs.copilotkit.ai/reference)[v2](https://docs.copilotkit.ai/reference/v2)Hooks

# useCapabilities

React hook for reading an agent's declared capabilities

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by an agent. Capabilities describe what an agent supports -- tool calling, streaming, multi-agent coordination, human-in-the-loop, and more.

Capabilities are populated from the runtime `/info` response at connection time. The value is `undefined` until the runtime handshake completes or if the agent doesn't declare capabilities.

## Signature
    
    
    import { useCapabilities } from "@copilotkit/react-core/v2";
    
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
    
    
    import { useCapabilities } from "@copilotkit/react-core/v2";
    
    function ToolPanel() {
      const capabilities = useCapabilities();
    
      if (!capabilities?.tools?.supported) {
        return null; // Agent doesn't support tools — hide the panel
      }
    
      return (
        <div>
          <h3>Tools</h3>
          {capabilities.tools.clientProvided && (
            <p>This agent accepts client-provided tools.</p>
          )}
        </div>
      );
    }

### Read capabilities for a specific agent

AgentInfo.tsx
    
    
    import { useCapabilities } from "@copilotkit/react-core/v2";
    
    function AgentInfo({ agentId }: { agentId: string }) {
      const capabilities = useCapabilities(agentId);
    
      if (!capabilities) {
        return <p>Loading capabilities…</p>;
      }
    
      return (
        <ul>
          <li>Streaming: {capabilities.transport?.streaming ? "Yes" : "No"}</li>
          <li>Tools: {capabilities.tools?.supported ? "Yes" : "No"}</li>
          <li>Human-in-the-loop: {capabilities.humanInTheLoop?.supported ? "Yes" : "No"}</li>
        </ul>
      );
    }

## Behavior

  * **Synchronous read** \-- The hook reads `capabilities` directly from the agent instance. There is no separate loading state or async fetch -- the value is `undefined` until the runtime `/info` handshake populates it, then becomes defined.
  * **Re-renders** \-- The hook calls `useAgent()` internally, so the component re-renders on agent state, message, and run-status changes (the default `updates` set). If you only need capabilities and want fewer re-renders, read `agent.capabilities` directly via `useAgent({ updates: [] })`.
  * **Stable reference** \-- The capabilities object reference only changes when the agent reconnects or the runtime response changes. It does not change on every render.



## Related

  * [`useAgent`](https://docs.copilotkit.ai/reference/v2/hooks/useAgent) \-- access the full agent instance (capabilities are a property of the agent)
  * [AG-UI Protocol](https://docs.copilotkit.ai/agentic-protocols/ag-ui) \-- the protocol that defines the capabilities schema


