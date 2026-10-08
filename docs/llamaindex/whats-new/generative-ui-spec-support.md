---
url: https://docs.copilotkit.ai/llamaindex/whats-new/generative-ui-spec-support/
title: Generative UI Spec Support
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:46.362497+00:00
---

# Generative UI Spec Support

> Source: https://docs.copilotkit.ai/llamaindex/whats-new/generative-ui-spec-support/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)[What's New](https://docs.copilotkit.ai/llamaindex/whats-new)

# Generative UI Spec Support

CopilotKit now supports all major Generative UI specifications

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

![Generative UI Specs](https://docs.copilotkit.ai/images/gen-ui-specs-light.webp)![Generative UI Specs](https://docs.copilotkit.ai/images/gen-ui-specs-dark.webp)

## **Generative UI Specifications**#

Several recently released specifications enable agents to return generative UI, increasing the power and flexibility of the Agent-to-User conversation.

**A2UI** , **MCP Apps** , and **Open-JSON-UI** are all generative UI specifications that allow agents to respond to users not only with text but also with dynamic UI components. CopilotKit now provides universal support for all major Generative UI specifications.

**Specification**| **Origin / Maintainer**| **Purpose**  
---|---|---  
**A2UI**|  Google| A declarative, LLM-friendly Generative UI spec. JSONL-based and streaming, designed for platform-agnostic rendering.  
**Open-JSON-UI**|  OpenAI| An open standardization of OpenAI's internal declarative Generative UI schema.  
**MCP Apps**|  MCP Ecosystem| Iframe-based Generative UI extending MCP, enabling servers to return interactive UI components.  
  
## **AG-UI vs Generative UI Specs**#

Despite the naming similarities, **AG-UI is not a generative UI specification** — it's a **User Interaction protocol** that provides the **bi-directional runtime connection** between the agent and the application.

AG-UI natively supports all of the above generative UI specs and allows developers to define **their own custom generative UI standards** as well.

## **Learn More**#

Explore each specification in detail:

  * [A2UI](https://docs.copilotkit.ai/llamaindex/generative-ui/a2ui) \- Google's declarative Generative UI spec
  * [MCP Apps](https://docs.copilotkit.ai/llamaindex/generative-ui/mcp-apps) \- Iframe-based Generative UI extending MCP



Or learn about related Generative UI capabilities:

  * [Open Generative UI](https://docs.copilotkit.ai/llamaindex/generative-ui/open-generative-ui) \- Let agents generate fully interactive HTML/CSS/JS UIs that stream live into the chat
  * [AG-UI Protocol](https://docs.copilotkit.ai/ag-ui-protocol) \- The user interaction protocol that supports all these specs
  * [Generative UI Guide](https://docs.copilotkit.ai/generative-ui) \- Build with Generative UI in CopilotKit



## **Supported Frameworks**#

Generative UI works with every agent framework CopilotKit integrates with — pick yours to get started:

  * [LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python/quickstart) · [LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript/quickstart)
  * [Google ADK](https://docs.copilotkit.ai/google-adk/quickstart)
  * [Microsoft Agent Framework](https://docs.copilotkit.ai/ms-agent-python/quickstart)
  * [AWS Strands](https://docs.copilotkit.ai/strands/quickstart)
  * [Mastra](https://docs.copilotkit.ai/mastra/quickstart)
  * [PydanticAI](https://docs.copilotkit.ai/pydantic-ai/quickstart)
  * [CrewAI](https://docs.copilotkit.ai/crewai-crews/quickstart)
  * [Agno](https://docs.copilotkit.ai/agno/quickstart)
  * [AG2](https://docs.copilotkit.ai/ag2/quickstart)
  * [LlamaIndex](https://docs.copilotkit.ai/llamaindex/quickstart)
  * [Claude Agent SDK](https://docs.copilotkit.ai/claude-sdk-python/quickstart)
  * [Deep Agents](https://docs.copilotkit.ai/deepagents/quickstart)


