---
url: https://docs.copilotkit.ai/langgraph-typescript/advanced/persistence/loading-agent-state/
title: Loading Agent State
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:09:58.925388+00:00
---

# Loading Agent State

> Source: https://docs.copilotkit.ai/langgraph-typescript/advanced/persistence/loading-agent-state/

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

On this page

[LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript)AdvancedPersistence

# Loading Agent State

Learn how threadId is used to load previous agent states.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

### Setting the threadId#

When setting the `threadId` property in CopilotKit, i.e:

When using LangGraph platform, the `threadId` must be a UUID.
    
    
    <CopilotKit threadId="2140b272-7180-410d-9526-f66210918b13">
      <YourApp />
    </CopilotKit>

CopilotKit will restore the complete state of the thread, including the messages, from the database. (See [Message Persistence](https://docs.copilotkit.ai/langgraph/advanced/persistence/message-persistence) for more details.)

### Loading Agent State#

This means that the state of any agent will also be restored. For example:
    
    
    const { agent } = useAgent({ agentId: "research_agent" });
    
    // agent.state will now be the state of research_agent in the thread id given above

### Learn More#

To learn more about persistence and state in CopilotKit, see:

  * [Reading agent state](https://docs.copilotkit.ai/langgraph/shared-state/in-app-agent-read)
  * [Writing agent state](https://docs.copilotkit.ai/langgraph/shared-state/in-app-agent-write)
  * [Loading Message History](https://docs.copilotkit.ai/langgraph/advanced/persistence/loading-message-history)



### On this page

Setting the threadIdLoading Agent StateLearn More
