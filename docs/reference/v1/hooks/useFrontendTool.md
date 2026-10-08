---
url: https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool/
title: useFrontendTool
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:01.814136+00:00
---

# useFrontendTool

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useFrontendTool/

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

# useFrontendTool

The useFrontendTool hook allows the Copilot to execute tools in the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

This is the v1 `useFrontendTool`, which takes an array of parameter definitions. It is still supported, but we recommend migrating to the [v2 `useFrontendTool`](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool) (from `@copilotkit/react-core/v2`), which uses Zod schemas for parameters.

`useFrontendTool` allows you to define executable actions that the AI can call with a handler function. This is the primary way to give your AI agent the ability to perform actions in your application, whether that's updating state, making API calls, or triggering side effects.

The hook requires three main pieces:

  1. A name and description so the AI knows when to call it
  2. A parameters definition describing what inputs the tool accepts
  3. A handler function that executes when the AI calls the tool



Optionally, you can provide a `render` function to display custom UI showing the tool's execution status and results in the chat interface.

## Usage

### Simple Usage
    
    
    import { useFrontendTool } from "@copilotkit/react-core";
    
    useFrontendTool({
      name: "sayHello",
      description: "Say hello to someone.",
      parameters: [
        {
          name: "name",
          type: "string",
          description: "name of the person to greet",
          required: true,
        },
      ],
      handler: async ({ name }) => {
        alert(`Hello, ${name}!`);
      },
    });

### With Custom UI Rendering
    
    
    import { useFrontendTool } from "@copilotkit/react-core";
    
    useFrontendTool({
      name: "showWeatherCard",
      description: "Display weather information for a location",
      parameters: [
        {
          name: "location",
          type: "string",
          description: "The location to show weather for",
          required: true,
        },
        {
          name: "temperature",
          type: "number",
          description: "Temperature in celsius",
          required: true,
        },
      ],
      handler: async ({ location, temperature }) => {
        // Fetch and return weather data
        return { location, temperature, conditions: "Sunny" };
      },
      render: ({ args, status, result }) => {
        if (status === "inProgress") {
          return <div>Loading weather for {args.location}...</div>;
        }
        if (status === "complete" && result) {
          return (
            <WeatherCard
              location={result.location}
              temperature={result.temperature}
              conditions={result.conditions}
            />
          );
        }
        return null;
      },
    });

## Generative UI

This hook enables you to dynamically generate UI elements and render them in the copilot chat. For more information, check out the [Generative UI](https://docs.copilotkit.ai/generative-ui/your-components/display-only) page.

## Migration from useCopilotAction

If you're migrating from `useCopilotAction`, here are the key differences:

  1. The render component props include `name` and `description`



### Migration Example
    
    
    // Before with useCopilotAction
    useCopilotAction({
      name: "addTodo",
      parameters: [
        {
          name: "text",
          type: "string",
          description: "The todo text",
          required: true,
        },
      ],
      handler: ({ text }) => {
        addTodo(text);
      },
    });
    
    // After with useFrontendTool
    useFrontendTool({
      name: "addTodo",
      parameters: [
        {
          name: "text",
          type: "string",
          description: "The todo text",
          required: true,
        },
      ],
      handler: ({ text }) => {
        addTodo(text);
      },
    });

## Parameters

Prop

Type

`name`string

Prop

Type

`description?`string

Prop

Type

`parameters?`T

Prop

Type

`handler?`FrontendAction<T>['handler']

Prop

Type

`followUp?`boolean

Prop

Type

`render?`FrontendAction<T>['render']

Prop

Type

`available?`'disabled' | 'enabled'
