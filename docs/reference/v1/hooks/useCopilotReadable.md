---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable/
title: useCopilotReadable
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:01.951437+00:00
---

# useCopilotReadable

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

🪁React (V1)SDK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

Components

[CopilotKit](https://docs.copilotkit.ai/reference/v1/components/CopilotKit)[CopilotTextarea](https://docs.copilotkit.ai/reference/v1/components/CopilotTextarea)[CopilotChat](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotChat)[CopilotPopup](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotPopup)[CopilotSidebar](https://docs.copilotkit.ai/reference/v1/components/chat/CopilotSidebar)[All Chat Components](https://docs.copilotkit.ai/reference/v1/components/chat)

Hooks

[useAgent](https://docs.copilotkit.ai/reference/v1/hooks/useAgent)[useCoAgent](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgent)[useCoAgentStateRender](https://docs.copilotkit.ai/reference/v1/hooks/useCoAgentStateRender)[useCopilotAction](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAction)[useCopilotAdditionalInstructions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotAdditionalInstructions)[useCopilotChat](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChat)[useCopilotChatHeadless_c](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c)[useCopilotChatSuggestions](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatSuggestions)[useCopilotReadable](https://docs.copilotkit.ai/reference/v1/hooks/useCopilotReadable)[useDefaultTool](https://docs.copilotkit.ai/reference/v1/hooks/useDefaultTool)[useFrontendTool](https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool)[useHumanInTheLoop](https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop)[useLangGraphInterrupt](https://docs.copilotkit.ai/reference/v1/hooks/useLangGraphInterrupt)[useRenderToolCall](https://docs.copilotkit.ai/reference/v1/hooks/useRenderToolCall)

Classes

[CopilotRuntime](https://docs.copilotkit.ai/reference/v1/classes/CopilotRuntime)[CopilotTask](https://docs.copilotkit.ai/reference/v1/classes/CopilotTask)[AnthropicAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/AnthropicAdapter)[GoogleGenerativeAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GoogleGenerativeAIAdapter)[GroqAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/GroqAdapter)[LangChainAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/LangChainAdapter)[OpenAIAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAdapter)[OpenAIAssistantAdapter](https://docs.copilotkit.ai/reference/v1/classes/llm-adapters/OpenAIAssistantAdapter)

SDKs

[LangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/js/LangGraph)[CrewAI SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAI)[CrewAIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/CrewAIAgent)[LangGraph SDK](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph)[LangGraphAGUIAgent](https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraphAGUIAgent)[Remote Endpoints](https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[Reference](https://docs.copilotkit.ai/reference)[v1](https://docs.copilotkit.ai/reference/v1)Hooks

# useCopilotReadable

The useCopilotReadable hook allows you to provide knowledge to your copilot (e.g. application state).

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useCopilotReadable` is a React hook that provides app-state and other information to the Copilot.

## Usage

### Simple Usage

In its most basic usage, useCopilotReadable accepts a single string argument representing any piece of app state, making it available for the Copilot to use as context when responding to user input.
    
    
    import { useCopilotReadable } from "@copilotkit/react-core";
     
    export function MyComponent() {
      const [employees, setEmployees] = useState([]);
     
      useCopilotReadable({
        description: "The list of employees",
        value: employees,
      });
    }

### Custom Serialization

By default the value is serialized with `JSON.stringify`. Pass `convert` to control the string the Copilot sees. It is called with the description and the value, in that order:
    
    
    useCopilotReadable({
      description: "The current user",
      value: user,
      convert: (description, value) => `${description}: ${value.firstName} ${value.lastName}`,
    });

### Conditional Usage

Toggle `available` to add or remove the context as your app state changes. Switching to `"disabled"` removes the entry from the Copilot context; switching back to `"enabled"` re-adds it.
    
    
    useCopilotReadable({
      description: "The list of employees",
      value: employees,
      available: showEmployees ? "enabled" : "disabled",
    });

### Re-running on Custom Dependencies

The context is refreshed whenever `description`, `value`, `convert` or `available` change. Pass a second argument to add your own dependencies:
    
    
    useCopilotReadable(
      {
        description: "The selected employee",
        value: employee,
      },
      [departmentId],
    );

## Parameters

Prop

Type

`description`string

Prop

Type

`value`any

Prop

Type

`available?`'enabled' | 'disabled'

Prop

Type

`convert?`(description: string, value: any) => string
