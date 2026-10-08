---
url: https://docs.copilotkit.ai/ag2/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:04.129123+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/ag2/frontend-tools/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Frontend-tools

Basics

# Frontend Tools

Create frontend actions and use them within your agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it.

## What is this?#

Frontend actions are powerful tools that allow your AI agents to directly interact with and update your application's user interface. Think of them as bridges that connect your agent's decision-making capabilities with your frontend's interactive elements.

CopilotKit consumes AG-UI protocol events streamed by AG2 over `/chat`. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

## When should I use this?#

Frontend actions are essential when you want to create truly interactive AI applications where your agent needs to:

  * Dynamically update UI elements
  * Trigger frontend animations or transitions
  * Show alerts or notifications
  * Modify application state
  * Handle user interactions programmatically



Without frontend actions, agents are limited to just processing and returning data. By implementing frontend actions, you can create rich, interactive experiences where your agent actively drives the user interface.

## Implementation#

### Setup CopilotKit#

To use frontend actions, you'll need to setup CopilotKit first. For the sake of brevity, we won't cover it here.

Check out our [getting started guide](https://docs.copilotkit.ai/ag2/quickstart) and come back here when you're setup.

### Create a frontend action#

First, you'll need to create a frontend action using the [useFrontendTool](https://docs.copilotkit.ai/reference/v2/hooks/useFrontendTool) hook. Here's a simple one to get you started that says hello to the user.

page.tsx
    
    
    import { z } from "zod";
    import { useFrontendTool } from "@copilotkit/react-core/v2"
    
    export function Page() {
      // ...
    
      useFrontendTool({
        name: "sayHello",
        description: "Say hello to the user",
        parameters: z.object({
          name: z.string().describe("The name of the user to say hello to"),
        }),
        handler: async ({ name }) => {
          alert(`Hello, ${name}!`);
          return `Said hello to ${name}!`;
        },
      });
    
      // ...
    }

### Modify your agent#

Now, we'll need to modify the agent to access these frontend actions. Open your AG2 backend file and continue from there.

### Setup your AG2 backend over AG-UI#

AG2 can call frontend actions through AG-UI tool events with a standard `/chat` endpoint:

Python

agent.py
    
    
    from fastapi import FastAPI, Header
    from fastapi.responses import StreamingResponse
    
    from ag2 import Agent
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    agent = Agent(
        name="assistant",
        prompt="You are a helpful assistant.",
        config=OpenAIResponsesConfig(model="gpt-5.5"),
    )
    
    stream = AGUIStream(agent)
    app = FastAPI()
    
    @app.post("/chat")
    async def run_agent(
        message: RunAgentInput,
    accept: str | None = Header(None),
    ) -> StreamingResponse:
        return StreamingResponse(
            stream.dispatch(message, accept=accept),
            media_type=accept or "text/event-stream",
        )

That's it. Your AG2 backend can now receive frontend action tool definitions emitted by CopilotKit through AG-UI.

### Give it a try#

You've now given your agent the ability to directly call any CopilotActions you've defined. These actions will be available as tools to the agent where they can be used as needed.

### On this page

What is this?When should I use this?Implementation
