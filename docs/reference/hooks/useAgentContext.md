---
url: https://docs.copilotkit.ai/reference/hooks/useAgentContext/
title: useAgentContext
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:38.856364+00:00
---

# useAgentContext

> Source: https://docs.copilotkit.ai/reference/hooks/useAgentContext/

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

# useAgentContext

React hook for providing dynamic context to agents

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useAgentContext` registers a dynamic context object with the active Copilot runtime for the lifetime of the component. The hook adds the context on mount and removes it on unmount, so the agent always sees an up-to-date snapshot of your application state without manual cleanup.

Update the incoming context object to refresh what the agent sees. This is the v2 equivalent of `useCopilotReadable` \-- it lets you surface any serializable application state (user preferences, selected items, computed values, etc.) as context that agents can reference when generating responses or making decisions.

## Signature
    
    
    import { useAgentContext } from "@copilotkit/react-core/v2";
    
    function useAgentContext(context: AgentContextInput): void;

## Parameters

Prop

Type

`context`AgentContextInput

## Usage

### Basic Usage

Provide simple application state as context for the agent.
    
    
    function UserGreeting({ user }: { user: { name: string; role: string } }) {
      useAgentContext({
        description: "The currently logged-in user",
        value: { name: user.name, role: user.role },
      });
    
      return <div>Welcome, {user.name}</div>;
    }

### Dynamic Context from Component State

The context updates automatically when the value changes between renders.
    
    
    function ProductCatalog() {
      const [selectedCategory, setSelectedCategory] = useState("electronics");
      const [priceRange, setPriceRange] = useState({ min: 0, max: 500 });
    
      useAgentContext({
        description: "The user's current product filter settings",
        value: {
          category: selectedCategory,
          priceRange,
        },
      });
    
      return (
        <div>
          <select
            value={selectedCategory}
            onChange={(e) => setSelectedCategory(e.target.value)}
          >
            <option value="electronics">Electronics</option>
            <option value="books">Books</option>
            <option value="clothing">Clothing</option>
          </select>
          {/* ... price range controls ... */}
        </div>
      );
    }

### Multiple Contexts in Nested Components

Each component can register its own context. All registered contexts are visible to the agent simultaneously.
    
    
    function Dashboard() {
      useAgentContext({
        description: "Current dashboard view and layout",
        value: { view: "analytics", columns: 3 },
      });
    
      return (
        <div>
          <Sidebar />
          <MainPanel />
        </div>
      );
    }
    
    function Sidebar() {
      const [collapsed, setCollapsed] = useState(false);
    
      useAgentContext({
        description: "Sidebar navigation state",
        value: { collapsed, activeSection: "reports" },
      });
    
      return <nav>{/* ... */}</nav>;
    }

## What the agent receives

Every registered entry reaches the agent as `{ description, value }`, and `value` is a **JSON string** \-- not the object or array you passed. The AG-UI protocol types it as a string, so this is not an implementation detail you can ignore when writing the agent.

Registering this:
    
    
    useAgentContext({
      description: "Incident dashboard records",
      value: [{ id: "INC-1041", severity: "sev1" }],
    });

delivers this to the agent:
    
    
    {
      "description": "Incident dashboard records",
      "value": "[{\"id\":\"INC-1041\",\"severity\":\"sev1\"}]"
    }

Parse it before reading any field. In a Python agent:
    
    
    import json
    
    def dashboard_records(context):
        entry = next(
            (item for item in context if item["description"] == "Incident dashboard records"),
            None,
        )
        return None if entry is None else json.loads(entry["value"])

In a TypeScript agent:
    
    
    const entry = context.find(
      (item) => item.description === "Incident dashboard records",
    );
    const records = entry ? JSON.parse(entry.value) : undefined;

Where that context list surfaces in your agent depends on your framework's AG-UI adapter.

### Google ADK

`ag-ui-adk` stores the request's context list in ADK session state under `CONTEXT_STATE_KEY`, a public export whose value is `"_ag_ui_context"`:
    
    
    from ag_ui_adk import CONTEXT_STATE_KEY
    
    def dashboard_records_for_adk(ctx):
        return dashboard_records(ctx.state.get(CONTEXT_STATE_KEY, []))

Use the `ctx` passed to an ADK instruction provider, `callback_context` in a callback, or `tool_context` in a tool. The entries are dictionaries with string `description` and `value` fields. To make these values visible to the model, include them in an instruction provider or a before-model callback; `AGUIToolset()` alone does not inject them into the prompt. See the [Google ADK read-only context setup](https://docs.copilotkit.ai/google-adk/shared-state/agent-readonly) for a complete agent example.

Do not type-check `value` against the shape you registered. `isinstance(entry["value"], list)` in Python, or `Array.isArray(entry.value)` in TypeScript, can never be true, because `value` is always a string on the wire. An agent that reads such a failed check as "no context was sent" will refuse every request while the browser is registering context correctly, and the two cases are indistinguishable from the UI.

## Behavior

  * **Mount/Unmount lifecycle** : The context is registered when the component mounts and automatically removed when it unmounts. There is no manual cleanup required.
  * **Reactive updates** : When the `context` object changes between renders, the agent immediately sees the updated value.
  * **Serialization** : The `value` must conform to `JsonSerializable` (`string | number | boolean | null | JsonSerializable[] | { [key: string]: JsonSerializable }`). Non-serializable values such as functions, class instances, or symbols will cause errors. Strings are sent through unchanged; every other value is stringified, so the agent always reads a string -- see What the agent receives.
  * **Multiple contexts** : Multiple `useAgentContext` calls across your component tree are all visible to the agent concurrently. Each is identified by its description and value.
  * **No return value** : The hook returns `void`. Unlike `useCopilotReadable`, it does not return an ID for parent-child hierarchies.



## Related

  * [`useCopilotReadable`](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable) \-- v1 equivalent for providing context


