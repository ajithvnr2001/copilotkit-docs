---
url: https://docs.copilotkit.ai/crewai-crews/persistence/message-persistence/
title: Message Persistence
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:51.778348+00:00
---

# Message Persistence

> Source: https://docs.copilotkit.ai/crewai-crews/persistence/message-persistence/

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

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)Persistence

# Message Persistence

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

To learn about how to load previous messages and agent states, check out the [Loading Message History](https://docs.copilotkit.ai/crewai-flows/persistence/loading-message-history) and [Loading Agent State](https://docs.copilotkit.ai/crewai-flows/persistence/loading-agent-state) pages.

To persist CrewAI Flow messages to a database, you can use the `@persist` decorator. For example, you might use the default `SQLiteFlowPersistence` or provide your own custom persistence class.

Conversational Flow sessions

No separate CopilotKit persistence adapter is required. CopilotKit's `threadId` becomes the CrewAI `session_id`, so CrewAI's `@persist` support stores and restores the corresponding conversational session.

For a concrete example of how a custom persistence class like `InMemoryFlowPersistence` can be implemented and used with the `@persist` decorator, see the [sample agent implementation](https://github.com/CopilotKit/CopilotKit/blob/main/examples/coagents-starter-crewai-flows/agent-py/sample_agent/agent.py).

Read more about persistence in the [CrewAI Flows documentation](https://docs.crewai.com/concepts/flows#class-level-persistence).
