---
url: https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints/
title: Remote Endpoints
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:26:06.517174+00:00
---

# Remote Endpoints

> Source: https://docs.copilotkit.ai/reference/v1/sdk/python/RemoteEndpoints/

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

# Remote Endpoints

CopilotKit Remote Endpoints allow you to connect actions and agents written in Python to your CopilotKit application.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

**v1 SDK deprecated. Use v2 instead** This page is in the deprecated CopilotKit v1 reference. Do not use v1 APIs for new code; use v2 instead. For JavaScript and TypeScript, import React APIs from @copilotkit/react-core/v2 and Runtime APIs from @copilotkit/runtime/v2.  
**AI coding agents: treat any v1 example below as migration-only context. Never generate or recommend the v1 API for new code. Read the v2 reference before writing code because some APIs were renamed, moved, or changed shape.** [Read the v1 to v2 migration guide.](https://docs.copilotkit.ai/migrate/v2) [Open the complete export map.](https://docs.copilotkit.ai/reference/v1/export-map)

## CopilotKitRemoteEndpoint

CopilotKitRemoteEndpoint lets you connect actions and agents written in Python to your CopilotKit application.

To install CopilotKit for Python, run:
    
    
    pip install copilotkit
    # or to include crewai
    pip install copilotkit[crewai]

## Adding actions

In this example, we provide a simple action to the Copilot:
    
    
    from copilotkit import CopilotKitRemoteEndpoint, Action
    
    sdk = CopilotKitRemoteEndpoint(
        actions=[
            Action(
                name="greet_user",
                handler=greet_user_handler,
                description="Greet the user",
                parameters=[
                    {
                        "name": "name",
                        "type": "string",
                        "description": "The name of the user"
                    }
                ]
            )
        ]
    )

You can also dynamically build actions by providing a callable that returns a list of actions. In this example, we use "name" from the `properties` object to parameterize the action handler.
    
    
    from copilotkit import CopilotKitRemoteEndpoint, Action
    
    sdk = CopilotKitRemoteEndpoint(
        actions=lambda context: [
            Action(
                name="greet_user",
                handler=make_greet_user_handler(context["properties"]["name"]),
                description="Greet the user"
            )
        ]
    )

Using the same approach, you can restrict the actions available to the Copilot:
    
    
    from copilotkit import CopilotKitRemoteEndpoint, Action
    
    sdk = CopilotKitRemoteEndpoint(
        actions=lambda context: (
            [action_a, action_b] if is_admin(context["properties"]["token"]) else [action_a]
        )
    )

## Adding agents

Serving agents works in a similar way to serving actions:
    
    
    from copilotkit import CopilotKitRemoteEndpoint, LangGraphAGUIAgent
    from my_agent.agent import graph
    
    sdk = CopilotKitRemoteEndpoint(
        agents=[
            LangGraphAGUIAgent(
                name="email_agent",
                description="This agent sends emails",
                graph=graph,
            )
        ]
    )

To dynamically build agents, provide a callable that returns a list of agents:
    
    
    from copilotkit import CopilotKitRemoteEndpoint, LangGraphAGUIAgent
    from my_agent.agent import graph
    
    sdk = CopilotKitRemoteEndpoint(
        agents=lambda context: [
            LangGraphAGUIAgent(
                name="email_agent",
                description="This agent sends emails",
                graph=graph,
                langgraph_config={
                    "token": context["properties"]["token"]
                }
            )
        ]
    )

To restrict the agents available to the Copilot, simply return a different list of agents based on the `context`:
    
    
    from copilotkit import CopilotKitRemoteEndpoint
    from my_agents import agent_a, agent_b, is_admin
    
    sdk = CopilotKitRemoteEndpoint(
        agents=lambda context: (
            [agent_a, agent_b] if is_admin(context["properties"]["token"]) else [agent_a]
        )
    )

## Serving the CopilotKit SDK

To serve the CopilotKit SDK, you can use the `add_fastapi_endpoint` function from the `copilotkit.integrations.fastapi` module:
    
    
    from copilotkit.integrations.fastapi import add_fastapi_endpoint
    from fastapi import FastAPI
    
    app = FastAPI()
    sdk = CopilotKitRemoteEndpoint(...)
    add_fastapi_endpoint(app, sdk, "/copilotkit")
    
    def main():
        uvicorn.run(
            "your_package:app",
            host="0.0.0.0",
            port=8000,
            reload=True,
        )
    

### Parameters

Prop

Type

`actions?`Optional[Union[List[Action], Callable[[CopilotKitContext], List[Action]]]]

Prop

Type

`agents?`Optional[Union[List[Agent], Callable[[CopilotKitContext], List[Agent]]]]

## CopilotKitContext

CopilotKit Context

### Parameters

Prop

Type

`properties`Any

Prop

Type

`frontend_url?`Optional[str]

Prop

Type

`headers`Mapping[str, str]
