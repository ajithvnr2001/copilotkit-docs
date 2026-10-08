---
url: https://docs.copilotkit.ai/langgraph/advanced/persistence/loading-message-history/
title: Threads
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:37:21.392474+00:00
---

# Threads

> Source: https://docs.copilotkit.ai/langgraph/advanced/persistence/loading-message-history/

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

[LangGraph (Python)](https://docs.copilotkit.ai/langgraph-python)AdvancedPersistence

# Threads

Learn how to load chat messages and threads within the CopilotKit framework.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

LangGraph supports threads, a way to group messages together and ultimately maintain a continuous chat history. CopilotKit provides a few different ways to interact with this concept.

This guide assumes you have already gone through the [quickstart](https://docs.copilotkit.ai/langgraph/quickstart) guide.

## Loading an Existing Thread#

To load an existing thread in CopilotKit, you can simply set the `threadId` property on `<CopilotKit>` like so.

When using LangGraph platform, the `threadId` must be a UUID.
    
    
    {
    }
    <CopilotKit threadId="37aa68d0-d15b-45ae-afc1-0ba6c3e11353">
      <YourApp />
    </CopilotKit>;

## Dynamically Switching Threads#

You can also make the `threadId` dynamic. Once it is set, CopilotKit will load the previous messages for that thread.
    
    
    const Page = () => {
      const [threadId, setThreadId] = useState("af2fa5a4-36bd-4e02-9b55-2580ab584f89"); 
      return (
        <CopilotKit threadId={threadId}>
          <YourApp setThreadId={setThreadId} />
        </CopilotKit>
      )
    }
    
    const YourApp = ({ setThreadId }) => {
      return (
        <Button onClick={() => setThreadId("679e8da5-ee9b-41b1-941b-80e0cc73a008")}>
          Change Thread
        </Button>
      )
    }

### On this page

Loading an Existing ThreadDynamically Switching Threads
