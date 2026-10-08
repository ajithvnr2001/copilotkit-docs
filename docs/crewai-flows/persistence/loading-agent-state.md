---
url: https://docs.copilotkit.ai/crewai-flows/persistence/loading-agent-state/
title: Loading Agent State
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:36:00.532635+00:00
---

# Loading Agent State

> Source: https://docs.copilotkit.ai/crewai-flows/persistence/loading-agent-state/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)Persistence

# Loading Agent State

Learn how threadId is used to load previous agent states.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

### Setting the threadId#

When setting the `threadId` property in CopilotKit, i.e:
    
    
    <CopilotKit threadId="2140b272-7180-410d-9526-f66210918b13">
      <YourApp />
    </CopilotKit>

CopilotKit will restore the complete state of the thread, including the messages, from the database. (See [Message Persistence](https://docs.copilotkit.ai/crewai-flows/persistence/message-persistence) for more details.)

### Loading Agent State#

**Important:** For agent state to be loaded correctly, you must first ensure that message history and persistence are properly configured. Follow the guides on [Threads & Persistence](https://docs.copilotkit.ai/crewai-flows/persistence/loading-message-history) and [Message Persistence](https://docs.copilotkit.ai/crewai-flows/persistence/message-persistence).

This means that the state of any agent will also be restored. For example:
    
    
    const { state } = useAgent({ agentId: "research_agent" });
    
    // state will now be the state of research_agent in the thread id given above

### Learn More#

To learn more about persistence and state in CopilotKit, see:

  * [Reading agent state](https://docs.copilotkit.ai/crewai-flows/shared-state/in-app-agent-read)
  * [Writing agent state](https://docs.copilotkit.ai/crewai-flows/shared-state/in-app-agent-write)
  * [Loading Message History](https://docs.copilotkit.ai/crewai-flows/persistence/loading-message-history)



### On this page

Setting the threadIdLoading Agent StateLearn More
