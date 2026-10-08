---
url: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c/
title: useCopilotChatHeadless_c
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:25:59.649614+00:00
---

# useCopilotChatHeadless_c

> Source: https://docs.copilotkit.ai/reference/v1/hooks/useCopilotChatHeadless_c/

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

# useCopilotChatHeadless_c

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

`useCopilotChatHeadless_c` is for building fully custom UI (headless UI) implementations.

This is a CopilotKit Intelligence feature

Read more about [CopilotKit Intelligence](https://docs.copilotkit.ai/intelligence/overview).

Usage is generous and free to get started.

## Key Features

  * Fully headless: Build your own fully custom UI's for your agentic applications.
  * Advanced Suggestions: Direct access to suggestions array with full control
  * Interrupt Handling: Support for advanced interrupt functionality
  * MCP Server Support: Model Context Protocol server configurations
  * Chat Controls: Complete set of chat management functions
  * Loading States: Comprehensive loading state management



## Usage

### Basic Setup
    
    
    import { CopilotKit } from "@copilotkit/react-core";
    import { useCopilotChatHeadless_c } from "@copilotkit/react-core";
     
    export function App() {
      return (
        <CopilotKit runtimeUrl="/api/copilotkit">
          <YourComponent />
        </CopilotKit>
      );
    }
     
    export function YourComponent() {
      const { messages, sendMessage, isLoading } = useCopilotChatHeadless_c();
     
      const handleSendMessage = async () => {
        await sendMessage({
          id: "123",
          role: "user",
          content: "Hello World",
        });
      };
     
      return (
        <div>
          {messages.map(msg => <div key={msg.id}>{msg.content}</div>)}
          <button onClick={handleSendMessage} disabled={isLoading}>
            Send Message
          </button>
        </div>
      );
    }

### Working with Suggestions
    
    
    import { useCopilotChatHeadless_c, useCopilotChatSuggestions } from "@copilotkit/react-core";
     
    export function SuggestionExample() {
      const {
        suggestions,
        setSuggestions,
        generateSuggestions,
        isLoadingSuggestions
      } = useCopilotChatHeadless_c();
     
      // Configure AI suggestion generation
      useCopilotChatSuggestions({
        instructions: "Suggest helpful actions based on the current context",
        maxSuggestions: 3
      });
     
      return (
        <div>
          {suggestions.map(suggestion => (
            <button key={suggestion.title}>{suggestion.title}</button>
          ))}
          <button onClick={generateSuggestions} disabled={isLoadingSuggestions}>
            Generate Suggestions
          </button>
        </div>
      );
    }

## Return Values

The following properties are returned from the hook:

Prop

Type

`messages?`Message[]

Prop

Type

`sendMessage?`(message: Message, options?) => Promise<void>

Prop

Type

`setMessages?`(messages: Message[] | DeprecatedGqlMessage[]) => void

Prop

Type

`deleteMessage?`(messageId: string) => void

Prop

Type

`reloadMessages?`(messageId: string) => Promise<void>

Prop

Type

`stopGeneration?`() => void

Prop

Type

`reset?`() => void

Prop

Type

`isLoading?`boolean

Prop

Type

`runChatCompletion?`() => Promise<Message[]>

Prop

Type

`mcpServers?`MCPServerConfig[]

Prop

Type

`setMcpServers?`(servers: MCPServerConfig[]) => void

Prop

Type

`suggestions?`SuggestionItem[]

Prop

Type

`setSuggestions?`(suggestions: SuggestionItem[]) => void

Prop

Type

`generateSuggestions?`() => Promise<void>

Prop

Type

`resetSuggestions?`() => void

Prop

Type

`isLoadingSuggestions?`boolean

Prop

Type

`interrupt?`string | React.ReactElement | null
