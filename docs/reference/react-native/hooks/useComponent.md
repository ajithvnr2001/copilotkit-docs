---
url: https://docs.copilotkit.ai/reference/react-native/hooks/useComponent/
title: useComponent
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:47.828132+00:00
---

# useComponent

> Source: https://docs.copilotkit.ai/reference/react-native/hooks/useComponent/

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

# useComponent

Register a React component as a frontend tool renderer in chat

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview

`useComponent` is a convenience hook built on top of `useFrontendTool`. It registers a tool and renders a React Native component in chat using the tool call parameters.

Re-exported from `@copilotkit/react-core/v2`. It is identical to the [React (V2) `useComponent`](https://docs.copilotkit.ai/reference/v2/hooks/useComponent); only the import path differs.

Use this when you want a visual component renderer without writing a full frontend tool config manually. The component you pass to `render` returns React Native elements that CopilotKit surfaces in the chat — it registers into the same shared renderer registry that [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool) and `useFrontendTool` write to, and that the chat reads through `useRenderToolCall`.

## Signature
    
    
    import { z } from "zod";
    import type { ComponentType } from "react";
    import { useComponent } from "@copilotkit/react-native";
    
    function useComponent<TSchema extends z.ZodTypeAny | undefined = undefined>(
      config: {
        name: string;
        description?: string;
        parameters?: TSchema;
        // When parameters is provided, props are inferred via z.infer.
        // When omitted, render accepts any props.
        render: ComponentType<InferRenderProps<TSchema>>;
        agentId?: string;
      },
      deps?: ReadonlyArray<unknown>,
    ): void;

## Parameters

  * `config.name`: tool name used by the agent to invoke this component tool.
  * `config.description`: optional extra description for model guidance.
  * `config.parameters`: optional Zod schema for the tool's parameters. When provided, `render` props are inferred from the schema. When omitted, the tool is advertised with an empty parameter schema (`{ "type": "object", "properties": {} }`), so the agent invokes it with no arguments.
  * `config.render`: React Native component rendered with parsed tool parameters. Accepts any props when `parameters` is omitted.
  * `config.agentId`: optional agent scope for the registration.
  * `deps`: optional dependency array for refreshing registration.



## Behavior

  * Prepends a default instruction to the description: _"Use this tool to display the " <name>" component in the chat..."_.
  * Calls `useFrontendTool` internally with a render function that spreads the tool parameters as component props.
  * Inherits `useFrontendTool` lifecycle behavior: duplicate-name override warning, tool removal on unmount, and renderer retention for chat history.
  * Tracks updates by `config.name` plus `deps` (include any changing captured values in `deps`).



## Usage
    
    
    import { Text, View } from "react-native";
    import { useComponent } from "@copilotkit/react-native";
    import { z } from "zod";
    
    const weatherCardSchema = z.object({
      city: z.string().describe("City name"),
      unit: z.enum(["c", "f"]).default("c"),
    });
    
    type WeatherCardProps = z.infer<typeof weatherCardSchema>;
    
    function WeatherCard({ city, unit }: WeatherCardProps) {
      return (
        <View style={{ borderWidth: 1, borderRadius: 8, padding: 12 }}>
          <Text style={{ fontSize: 12, color: "#71717a" }}>Weather request</Text>
          <Text style={{ fontWeight: "500" }}>
            {city} ({unit.toUpperCase()})
          </Text>
        </View>
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

  * [`useFrontendTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useFrontendTool)
  * [`useRenderTool`](https://docs.copilotkit.ai/reference/react-native/hooks/useRenderTool)
  * [React (V2) reference](https://docs.copilotkit.ai/reference/v2/hooks/useComponent)


