---
url: https://docs.copilotkit.ai/langgraph-typescript/reference/v2/hooks/useCapabilities/
title: useCapabilities
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:12:05.151720+00:00
---

# useCapabilities

> Source: https://docs.copilotkit.ai/langgraph-typescript/reference/v2/hooks/useCapabilities/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript)ReferenceV2Hooks

# useCapabilities

React hook for reading an agent's declared capabilities

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

`useCapabilities` returns the [AG-UI `AgentCapabilities`](https://docs.ag-ui.com/concepts/capabilities) declared by an agent. Capabilities describe what an agent supports -- tool calling, streaming, multi-agent coordination, human-in-the-loop, and more.

Capabilities are populated from the runtime `/info` response at connection time. The value is `undefined` until the runtime handshake completes or if the agent doesn't declare capabilities.

## Signature#
    
    
    import { useCapabilities } from "@copilotkit/react-core/v2";
    
    function useCapabilities(agentId?: string): AgentCapabilities | undefined

## Parameters#

Prop

Type

`agentId?`string

## Return Value#

Prop

Type

`capabilities?`AgentCapabilities | undefined

## Usage#

### Conditionally render UI based on capabilities#

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

### Read capabilities for a specific agent#

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

## Behavior#

  * **Synchronous read** \-- The hook reads `capabilities` directly from the agent instance. There is no separate loading state or async fetch -- the value is `undefined` until the runtime `/info` handshake populates it, then becomes defined.
  * **Re-renders** \-- The hook calls `useAgent()` internally, so the component re-renders on agent state, message, and run-status changes (the default `updates` set). If you only need capabilities and want fewer re-renders, read `agent.capabilities` directly via `useAgent({ updates: [] })`.
  * **Stable reference** \-- The capabilities object reference only changes when the agent reconnects or the runtime response changes. It does not change on every render.



## Related#

  * [`useAgent`](https://docs.copilotkit.ai/reference/v2/hooks/useAgent) \-- access the full agent instance (capabilities are a property of the agent)
  * [AG-UI Protocol](https://docs.copilotkit.ai/langgraph-typescript/agentic-protocols/ag-ui) \-- the protocol that defines the capabilities schema



### On this page

OverviewSignatureParametersReturn ValueUsageConditionally render UI based on capabilitiesRead capabilities for a specific agentBehaviorRelated
