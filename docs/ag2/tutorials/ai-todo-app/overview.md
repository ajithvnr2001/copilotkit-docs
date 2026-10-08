---
url: https://docs.copilotkit.ai/ag2/tutorials/ai-todo-app/overview/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:45:24.067568+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/ag2/tutorials/ai-todo-app/overview/

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

# Quickstart

Turn your AG2 Agents into an agent-native application in 5 minutes.

## Start with your coding agent#

Use this prompt to connect your AG2 agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Introduction#

This quickstart guide shows how to build a **Weather Agent** using AG2 and CopilotKit. In just minutes, you'll have a working application where users can ask for real-time weather conditions in any city worldwide — powered by AG2's `AGUIStream` over the AG-UI protocol and rendered with CopilotKit's chat UI.

CopilotKit consumes AG-UI 1.0 protocol events streamed by AG2 (1.1.2 or newer) over HTTP. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

## AG2 Bootstrap Template#

If you prefer a generated starter instead of cloning the repo, use the CopilotKit bootstrap template and select **AG2** during setup. This wires up an AG2 backend over AG-UI and a ready-to-run frontend.
    
    
    npx copilotkit@latest init

Follow the prompts to pick AG2 and the features you want, then run the install/start commands it prints.

## Prerequisites#

Before you begin, you'll need the following:

  * **Python 3.10–3.14** for running the AG2 backend
  * [uv](https://docs.astral.sh/uv/getting-started/installation/) (for Python dependency management)
  * [Node.js](https://nodejs.org/en/download) 20.9 or newer
  * [pnpm](https://pnpm.io/installation) (for frontend package management)
  * [OpenAI API key](https://platform.openai.com/api-keys)



## Getting started#

### Set up CopilotKit Intelligence#

[Sign in to cloud-hosted Intelligence](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_ag2_quickstart_step1&utm_frontend=react&utm_backend=ag2). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you clone it below.

### Clone the AG2 Samples Repository#
    
    
    git clone https://github.com/ag2ai/ag2-samples.git
    cd ag2-samples
    npx copilotkit@latest project select

`project select` creates or selects an Intelligence project and writes its server-side API key to `.env` as `CPK_INTELLIGENCE_API_KEY`.

### Set Up the AG2 Backend#

#### Install the dependencies:
    
    
    uv sync

#### Set your `OPENAI_API_KEY` and `AUTH_SECRET`:

The sample serves the agent only to a signed-in user. `AUTH_SECRET` signs and verifies the user's access token, so the backend and the frontend must use the same value. Any long random string works.
    
    
    export OPENAI_API_KEY="your_openai_api_key"
    export AUTH_SECRET="a-long-random-string"

#### Launch the AG2 weather agent:
    
    
    uv run python -m backend

The backend server will start at <http://localhost:8000> and serve the agent at `/weather`.

### Set Up the CopilotKit UI#

The last step is to use CopilotKit's UI components to render the chat interaction with your agent.

In a new terminal:
    
    
    cd ui
    pnpm install
    AUTH_SECRET="a-long-random-string" pnpm dev

The frontend application will start at <http://localhost:3000>. Use the same `AUTH_SECRET` as the backend.

The sample's sign-in is a demonstration: it accepts any name and keeps the token in `localStorage`. Replace `verify_access_token` in `backend/auth.py` and the token route in the UI before reusing the pattern. See [Authentication](https://docs.copilotkit.ai/ag2/auth).

### 🎉 Talk to your agent!#

Congrats! You've successfully integrated an AG2 Agent chatbot into your application. Enter a name to sign in, then try asking a few questions:
    
    
    What's the weather in London?
    
    
    Weather in Tokyo
    
    
    What's the weather here?

The sample also shows the AG-UI 1.0 features next to the chat:

Feature| Try it  
---|---  
[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents) (`ClothingAdvisor`, `TripPlanner`)| "What should I wear in Oslo?"  
[Interrupts](https://docs.copilotkit.ai/ag2/human-in-the-loop#approve-a-tool-call-with-interrupts) (`save_favorite_city` waits for approval)| "Save Lisbon to my favorites"  
[Shared state](https://docs.copilotkit.ai/ag2/shared-state) (the favorites panel)| Save a city, then watch the panel  
Capabilities| `curl localhost:8000/weather`  
  
Asking "What's the weather here?" will use your browser's location if you allow it. If location access is denied, the agent will ask you for a city name instead.

### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/ag2/inspector).

* * *

## Connect your own AG2 agent#

The samples repository is a ready-made example. To expose any AG2 agent over AG-UI, install AG2 (1.1.2+) with the AG-UI and OpenAI extras and wrap the agent in `AGUIStream`:
    
    
    pip install "ag2[ag-ui,openai]>=1.1.2"

run_ag_ui.py
    
    
    from fastapi import FastAPI, Header
    from fastapi.responses import StreamingResponse
    
    from ag2 import Agent
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    agent = Agent(
        name="support_bot",
        prompt="You help users with billing questions.",
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

If you don't need custom auth, logging, or middleware around the endpoint, `AGUIStream.build_asgi()` builds a ready-to-mount ASGI endpoint instead:

run_ag_ui.py
    
    
    from fastapi import FastAPI
    
    from ag2 import Agent
    from ag2.ag_ui import AGUIStream
    from ag2.config import OpenAIResponsesConfig
    
    agent = Agent(
        name="support_bot",
        prompt="You help users with billing questions.",
        config=OpenAIResponsesConfig(model="gpt-5.5"),
    )
    
    stream = AGUIStream(agent)
    app = FastAPI()
    app.mount("/chat", stream.build_asgi())

Point the `HttpAgent` in your Copilot Runtime at `http://localhost:8000/chat` and your agent is live in the UI. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/) for supported protocol events, interrupts, capabilities, and shared-state details.

## What's next?#

You've now got a Weather Agent running with CopilotKit! This demonstrates how quickly you can build practical AI applications by combining AG2's `AGUIStream` with CopilotKit's user interface components.

[👤Implement Human in the LoopAllow your users and agents to collaborate together on tasks.](https://docs.copilotkit.ai/ag2/human-in-the-loop)
