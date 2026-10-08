---
url: https://docs.copilotkit.ai/crewai-crews/persistence/loading-message-history/
title: Threads
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:51.832941+00:00
---

# Threads

> Source: https://docs.copilotkit.ai/crewai-crews/persistence/loading-message-history/

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

# Threads

Learn how to maintain persistent conversations across sessions with CrewAI Flows.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

# Understanding Thread Persistence

CrewAI Flows supports threads, a way to group messages together and maintain a continuous chat history across sessions. CopilotKit provides mechanisms to ensure conversation state is properly persisted between the frontend and backend.

This guide assumes you have already gone through the [quickstart](https://docs.copilotkit.ai/crewai-flows/quickstart) guide.

**Note:** While the frontend uses `threadId` to manage conversation sessions, true persistence across sessions requires backend setup. The backend agent needs to implement a persistence mechanism (like the one shown in [Message Persistence](https://docs.copilotkit.ai/crewai-flows/persistence/message-persistence)) to save and load the state associated with each `threadId`.

See the [sample agent implementation](https://github.com/CopilotKit/CopilotKit/blob/main/examples/coagents-starter-crewai-flows/agent-py/sample_agent/agent.py#L291) for a concrete example.

## Frontend: Setting the ThreadId#

### Loading an Existing Thread#

To load an existing thread in CopilotKit, set the `threadId` property on `<CopilotKit>`:
    
    
    <CopilotKit threadId="37aa68d0-d15b-45ae-afc1-0ba6c3e11353">
      <YourApp />
    </CopilotKit>

### Dynamically Switching Threads#

You can make the `threadId` dynamic. Once set, CopilotKit will load previous messages for that thread.
    
    
    const Page = () => {
      const [threadId, setThreadId] = useState(
        "af2fa5a4-36bd-4e02-9b55-2580ab584f89",
      );
      return (
        <CopilotKit threadId={threadId}>
          <YourApp setThreadId={setThreadId} />
        </CopilotKit>
      );
    };
    
    const YourApp = ({ setThreadId }) => {
      return (
        <Button onClick={() => setThreadId("679e8da5-ee9b-41b1-941b-80e0cc73a008")}>
          Change Thread
        </Button>
      );
    };

### On this page

Frontend: Setting the ThreadIdLoading an Existing ThreadDynamically Switching Threads
