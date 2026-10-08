---
url: https://docs.copilotkit.ai/reference/hooks/useComponent/
title: useComponent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:38.638709+00:00
---

# useComponent

> Source: https://docs.copilotkit.ai/reference/hooks/useComponent/

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

# useComponent

Register a React component as a frontend tool renderer in chat

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useComponent` is a convenience hook built on top of `useFrontendTool`. It registers a tool and renders a React component in chat using the tool call parameters.

This is part of the v2 tool rendering hook set with [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool), [`useDefaultRenderTool`](https://docs.copilotkit.ai/reference/hooks/useDefaultRenderTool), and [`useRenderToolCall`](https://docs.copilotkit.ai/reference/hooks/useRenderToolCall).

Use this when you want a visual component renderer without writing a full frontend tool config manually.

## Signature
    
    
    import { z } from "zod";
    import type { ComponentType } from "react";
    import { useComponent } from "@copilotkit/react-core/v2";
    
    function useComponent<TSchema extends z.ZodTypeAny | undefined = undefined>(
      config: {
        name: string;
        description?: string;
        parameters?: TSchema;
        // When parameters is provided, props are inferred via z.infer.
        // When omitted, render accepts any props.
        render: ComponentType<InferRenderProps<TSchema>>;
        agentId?: string;
        followUp?: boolean;
      },
      deps?: ReadonlyArray<unknown>,
    ): void;

## Parameters

  * `config.name`: tool name used by the agent to invoke this component tool.
  * `config.description`: optional extra description for model guidance.
  * `config.parameters`: optional Zod schema for the tool's parameters. When provided, `render` props are inferred from the schema. When omitted, the tool is advertised with an empty parameter schema (`{ "type": "object", "properties": {} }`), so the agent invokes it with no arguments.
  * `config.render`: React component rendered with parsed tool parameters. Accepts any props when `parameters` is omitted.
  * `config.agentId`: optional agent scope for the registration.
  * `config.followUp`: whether the agent should continue after rendering the component. Defaults to `true`; set it to `false` to stop after the tool call.
  * `deps`: optional dependency array for refreshing registration.



## Behavior

  * Prepends a default instruction to the description: _"Use this tool to display the " <name>" component in the chat..."_.
  * Calls `useFrontendTool` internally with a render function that spreads the tool parameters as component props.
  * Inherits `useFrontendTool` lifecycle behavior: duplicate-name override warning, tool removal on unmount, and renderer retention for chat history.
  * Tracks updates by `config.name` plus `deps` (include any changing captured values in `deps`).



## Usage
    
    
    const weatherCardSchema = z.object({
      city: z.string().describe("City name"),
      unit: z.enum(["c", "f"]).default("c"),
    });
    
    type WeatherCardProps = z.infer<typeof weatherCardSchema>;
    
    function WeatherCard({ city, unit }: WeatherCardProps) {
      return (
        <div className="rounded border p-3">
          <div className="text-sm text-zinc-500">Weather request</div>
          <div className="font-medium">
            {city} ({unit.toUpperCase()})
          </div>
        </div>
      );
    }
    
    function App() {
      useComponent(
        {
          name: "showWeatherCard",
          description: "Render a weather card in chat for the requested city.",
          parameters: weatherCardSchema,
          render: WeatherCard,
        },
        [],
      );
    
      return null;
    }

## Related

  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/hooks/useFrontendTool)
  * [`useRenderTool`](https://docs.copilotkit.ai/reference/hooks/useRenderTool)


