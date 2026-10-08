---
url: https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop/
title: useHumanInTheLoop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:01.878094+00:00
---

# useHumanInTheLoop

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useHumanInTheLoop/

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

# useHumanInTheLoop

The useHumanInTheLoop hook enables human approval and interaction workflows.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

This is the v1 `useHumanInTheLoop`, which takes an array of parameter definitions. It is still supported, but we recommend migrating to the [v2 `useHumanInTheLoop`](https://docs.copilotkit.ai/reference/v2/hooks/useHumanInTheLoop) (from `@copilotkit/react-core/v2`), which uses Zod schemas for parameters.

`useHumanInTheLoop` pauses AI execution to request human input or approval. When the AI calls this tool, it stops and waits for the user to respond through your custom UI before continuing. This is essential for sensitive operations, confirmations, or collecting information that only the user can provide.

Unlike `useFrontendTool`, there's no handler function. Instead, your render function receives a `respond` callback that sends the user's input back to the AI. The AI execution remains paused until `respond` is called, making this a true blocking interaction.

## Usage

### Simple Confirmation Example
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core";
    
    useHumanInTheLoop({
      name: "confirmDeletion",
      description: "Ask user to confirm before deleting items",
      parameters: [
        {
          name: "itemName",
          type: "string",
          description: "Name of the item to delete",
          required: true,
        },
        {
          name: "itemCount",
          type: "number",
          description: "Number of items to delete",
          required: true,
        },
      ],
      render: ({ args, status, respond, result }) => {
        if (status === "executing" && respond) {
          return (
            <div className="p-4 border rounded">
              <p>Are you sure you want to delete {args.itemCount} {args.itemName}(s)?</p>
              <div className="flex gap-2 mt-4">
                <button
                  onClick={() => respond({ confirmed: true })}
                  className="bg-red-500 text-white px-4 py-2 rounded"
                >
                  Delete
                </button>
                <button
                  onClick={() => respond({ confirmed: false })}
                  className="bg-gray-300 px-4 py-2 rounded"
                >
                  Cancel
                </button>
              </div>
            </div>
          );
        }
    
        if (status === "complete" && result) {
          return (
            <div className="p-2 text-sm text-gray-600">
              {result.confirmed ? "Items deleted" : "Deletion cancelled"}
            </div>
          );
        }
    
        return null;
      },
    });

### Complex Input Collection Example
    
    
    import { useHumanInTheLoop } from "@copilotkit/react-core";
    import { useState } from "react";
    
    useHumanInTheLoop({
      name: "collectUserPreferences",
      description: "Collect detailed preferences from the user",
      parameters: [
        {
          name: "context",
          type: "string",
          description: "Context for why preferences are needed",
          required: true,
        },
        {
          name: "requiredFields",
          type: "string[]",
          description: "Fields to collect",
          required: true,
        },
      ],
      render: ({ args, status, respond }) => {
        const [preferences, setPreferences] = useState({
          theme: "light",
          notifications: true,
          language: "en",
        });
    
        if (status === "executing" && respond) {
          return (
            <div className="p-4 border rounded">
              <h3 className="font-bold mb-2">{args.context}</h3>
              <form onSubmit={(e) => {
                e.preventDefault();
                respond(preferences);
              }}>
                <button
                  type="submit"
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Save Preferences
                </button>
              </form>
            </div>
          );
        }
    
        return null;
      },
    });

## Best Practices

  1. Always check for the `respond` function before rendering interactive elements
  2. Handle all status states to provide good user feedback
  3. Validate user input before calling `respond`
  4. Provide clear instructions in your UI about what input is expected
  5. Consider timeout scenarios for time-sensitive operations



## Migration from useCopilotAction

If you're migrating from `useCopilotAction` with `renderAndWaitForResponse`:
    
    
    // Before with useCopilotAction
    useCopilotAction({
      name: "confirmAction",
      parameters: [
        { name: "message", type: "string", required: true },
      ],
      renderAndWaitForResponse: ({ args, respond, status }) => {
        return (
          <ConfirmDialog
            message={args.message}
            onConfirm={() => respond(true)}
            onCancel={() => respond(false)}
            isActive={status === "executing"}
          />
        );
      },
    });
    
    // After with useHumanInTheLoop
    useHumanInTheLoop({
      name: "confirmAction",
      parameters: [
        {
          name: "message",
          type: "string",
          description: "The message to display",
          required: true,
        },
      ],
      render: ({ args, respond, status }) => {
        if (status === "executing" && respond) {
          return (
            <ConfirmDialog
              message={args.message}
              onConfirm={() => respond(true)}
              onCancel={() => respond(false)}
              isActive={true}
            />
          );
        }
        return null;
      },
    });

The main differences are:

  1. The property is called `render` instead of `renderAndWaitForResponse`
  2. You need to check for the `respond` function's existence



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

`render`FrontendAction<T>['renderAndWaitForResponse']

Prop

Type

`available?`'disabled' | 'enabled'
