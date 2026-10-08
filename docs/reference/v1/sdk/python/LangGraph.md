---
url: https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph/
title: LangGraph SDK
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:03.613598+00:00
---

# LangGraph SDK

> Source: https://docs.copilotkit.ai/reference/v1/sdk/python/LangGraph/

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

[Reference](https://docs.copilotkit.ai/reference)[v1](https://docs.copilotkit.ai/reference/v1)Sdk

# LangGraph SDK

The CopilotKit LangGraph SDK for Python allows you to build and run LangGraph workflows with CopilotKit.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

## copilotkit_customize_config

Customize the LangGraph configuration for use in CopilotKit.

To install the CopilotKit SDK, run:
    
    
    pip install copilotkit

### Examples

Disable emitting messages and tool calls:
    
    
    from copilotkit.langgraph import copilotkit_customize_config
    
    config = copilotkit_customize_config(
        config,
        emit_messages=False,
        emit_tool_calls=False
    )

To emit a tool call as streaming LangGraph state, pass the destination key in state, the tool name and optionally the tool argument. (If you don't pass the argument name, all arguments are emitted under the state key.)
    
    
    from copilotkit.langgraph import copilotkit_customize_config
    
    config = copilotkit_customize_config(
        config,
        emit_intermediate_state=[
           {
                "state_key": "steps",
                "tool": "SearchTool",
                "tool_argument": "steps"
            },
        ]
    )

### Parameters

Prop

Type

`base_config?`Optional[RunnableConfig]

Prop

Type

`emit_messages?`Optional[bool]

Prop

Type

`emit_tool_calls?`Optional[Union[bool, str, List[str]]]

Prop

Type

`emit_intermediate_state?`Optional[List[IntermediateStateConfig]]

### Returns

Prop

Type

`returns?`RunnableConfig

## copilotkit_exit

Exits the current agent after the run completes. Calling copilotkit_exit() will not immediately stop the agent. Instead, it signals to CopilotKit to stop the agent after the run completes.

### Examples
    
    
    from copilotkit.langgraph import copilotkit_exit
    
    def my_node(state: Any):
        await copilotkit_exit(config)
        return state

### Parameters

Prop

Type

`config`RunnableConfig

### Returns

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_emit_state

Emits intermediate state to CopilotKit. Useful if you have a longer running node and you want to update the user with the current state of the node.

### Examples
    
    
    from copilotkit.langgraph import copilotkit_emit_state
    
    for i in range(10):
        await some_long_running_operation(i)
        await copilotkit_emit_state(config, {"progress": i})

### Parameters

Prop

Type

`config`RunnableConfig

Prop

Type

`state`Any

### Returns

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_emit_message

Manually emits a message to CopilotKit. Useful in longer running nodes to update the user. Important: You still need to return the messages from the node.

### Examples
    
    
    from copilotkit.langgraph import copilotkit_emit_message
    
    message = "Step 1 of 10 complete"
    await copilotkit_emit_message(config, message)
    
    # Return the message from the node
    return {
        "messages": [AIMessage(content=message)]
    }

### Parameters

Prop

Type

`config`RunnableConfig

Prop

Type

`message`str

### Returns

Prop

Type

`returns?`Awaitable[bool]

## copilotkit_emit_tool_call

Manually emits a tool call to CopilotKit.
    
    
    from copilotkit.langgraph import copilotkit_emit_tool_call
    
    auto_id = await copilotkit_emit_tool_call(config, name="SearchTool", args={"steps": 10})
    
    # With a custom ID for correlation/idempotency:
    custom_id = await copilotkit_emit_tool_call(config, name="SearchTool", args={"steps": 10}, tool_call_id="my-custom-id")

### Parameters

Prop

Type

`config`RunnableConfig

Prop

Type

`name`str

Prop

Type

`args`Dict[str, Any]

Prop

Type

`tool_call_id?`Optional[str]

### Returns

Prop

Type

`returns?`str
