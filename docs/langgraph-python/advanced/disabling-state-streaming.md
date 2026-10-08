---
url: https://docs.copilotkit.ai/langgraph-python/advanced/disabling-state-streaming/
title: Disabling state streaming
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:06:55.187696+00:00
---

# Disabling state streaming

> Source: https://docs.copilotkit.ai/langgraph-python/advanced/disabling-state-streaming/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-python)[Quickstart](https://docs.copilotkit.ai/langgraph-python/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-python/webmcp)

Agent capabilities

LangGraph (Python)

[Sub-agents](https://docs.copilotkit.ai/langgraph-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-python/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)Advanced

# Disabling state streaming

Granularly control what is streamed to the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

By default, CopilotKit will stream both your state and tool calls to the frontend. You can disable this by using CopilotKit's custom `RunnableConfig`.

## When should I use this?#

Occasionally, you'll want to disable streaming temporarily — for example, the LLM may be doing something the current user should not see, like emitting tool calls or questions pertaining to other employees in an HR system.

## Implementation#

### Disable all streaming#

You can disable all message streaming and tool call streaming by passing `emit_messages=False` and `emit_tool_calls=False` to the CopilotKit config.

PythonTypeScript
    
    
    from langchain_core.runnables import RunnableConfig
    from copilotkit.langgraph import copilotkit_customize_config
    
    async def frontend_actions_node(state: AgentState, config: RunnableConfig):
    
        # 1) Configure CopilotKit not to emit messages
        modifiedConfig = copilotkit_customize_config(
            config,
            emit_messages=False, # if you want to disable message streaming 
            emit_tool_calls=False # if you want to disable tool call streaming 
        )
    
        # 2) Provide the actions to the LLM
        model = ChatOpenAI(model="gpt-5.4").bind_tools([
          *state["copilotkit"]["actions"],
          # ... any tools you want to make available to the model
        ])
    
        # 3) Call the model with CopilotKit's modified config  
        response = await model.ainvoke(state["messages"], modifiedConfig) 
    
        # don't return the new response to hide it from the user
        return state

BEWARE!

In LangGraph Python, the `config` variable in the surrounding namespace is **implicitly** passed into LangChain LLM calls, even when not explicitly provided.

This is why we create a new variable `modifiedConfig` rather than modifying `config` directly. If we modified `config` itself, it would change the default configuration for all subsequent LLM calls in that namespace.
    
    
    # if we override the config variable name with a new value
    config = copilotkit_customize_config(config, ...)
    
    # it will affect every subsequent LangChain LLM call in the same namespace, even when `config` is not explicitly provided
    response = await model2.ainvoke(*state["messages"]) # implicitly uses the modified config!
    
    
    async function frontendActionsNode(state: AgentState, config: RunnableConfig): Promise<AgentState> {
        // 1) Configure CopilotKit not to emit messages
        const modifiedConfig = copilotkitCustomizeConfig(config, {
            emitMessages: false, // if you want to disable message streaming
            emitToolCalls: false, // if you want to disable tool call streaming
        });
    
        // 2) Provide the actions to the LLM
        const model = new ChatOpenAI({ temperature: 0, model: "gpt-5.4" });
        const modelWithTools = model.bindTools!([
    ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions || []),
            ...tools,
        ]);
    
        // 3) Call the model with CopilotKit's modified config
        const response = await modelWithTools.invoke(state.messages, modifiedConfig);
    
        // don't return the new response to hide it from the user
        return state;
    }

### On this page

What is this?When should I use this?ImplementationDisable all streaming
