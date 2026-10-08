---
url: https://docs.copilotkit.ai/langgraph-typescript/advanced/persistence/message-persistence/
title: Message Persistence
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:10:04.592497+00:00
---

# Message Persistence

> Source: https://docs.copilotkit.ai/langgraph-typescript/advanced/persistence/message-persistence/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript)AdvancedPersistence

# Message Persistence

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

To learn about how to load previous messages and agent states, check out the [Loading Message History](https://docs.copilotkit.ai/langgraph/advanced/persistence/loading-message-history) and [Loading Agent State](https://docs.copilotkit.ai/langgraph/advanced/persistence/loading-agent-state) pages.

To persist LangGraph messages to a database, you can use either `AsyncPostgresSaver` or `AsyncSqliteSaver`. Set up the asynchronous memory by configuring the graph within a lifespan function, as follows:
    
    
    from fastapi import FastAPI
    from contextlib import asynccontextmanager
    from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
    from copilotkit import LangGraphAGUIAgent
    from ag_ui_langgraph import add_langgraph_fastapi_endpoint
    
    graph = None
    @asynccontextmanager
    async def lifespan(app: FastAPI):
        async with AsyncPostgresSaver.from_conn_string(
            "postgresql://postgres:postgres@127.0.0.1:5432/postgres"
        ) as checkpointer:
            # NOTE: you need to call .setup() the first time you're using your checkpointer
            await checkpointer.setup()
            # Create an async graph
            graph = workflow.compile(checkpointer=checkpointer)
            yield
            # Create SDK with the graph
    
    app = FastAPI(lifespan=lifespan)
    
    add_langgraph_fastapi_endpoint(
        app=app,
        agent=LangGraphAGUIAgent(
            name="research_agent",
            description="Research agent.",
            graph=graph,
        ),
        path="/agents/research_agent"
    )
    

To learn more about persistence in LangGraph, check out the [LangGraph documentation](https://docs.langchain.com/oss/python/langgraph/persistence).
