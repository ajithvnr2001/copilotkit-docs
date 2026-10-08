---
url: https://docs.copilotkit.ai/ag2/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:10.570613+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/ag2/generative-ui/state-rendering/

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

[Components as Tools](https://docs.copilotkit.ai/ag2/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/ag2/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/ag2/generative-ui/state-rendering)

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

State Rendering

Generative UIControlled

# State Rendering

Render the state of your agent with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

AG2 agents can maintain state across a session through **conversation variables** (`Context.variables`). CopilotKit can render this state in your application with custom UI components, which we call **Agentic Generative UI**.

CopilotKit consumes AG-UI protocol events streamed by AG2 over `/chat`. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/).

## When should I use this?#

Rendering the state of your agent in the UI is useful when you want to provide the user with feedback about the overall state of a session. A great example of this is a situation where a user and an agent are working together to solve a problem. The agent can store a draft in its state which is then rendered in the UI.

## Implementation#

### Run and connect your agent#

Start your AG2 backend with AG-UI streaming enabled on `/chat`.

### Set up your agent with state#

Store the state in the agent's conversation variables. Changes made by tools are streamed back as `STATE_SNAPSHOT` events automatically at the end of the run; for per-step updates during a long-running tool, emit intermediate snapshots with `context.send`:

agent.py
    
    
    from typing import Annotated
    
    from ag_ui.core import StateSnapshotEvent
    from fastapi import FastAPI, Header
    from fastapi.responses import StreamingResponse
    from pydantic import BaseModel, Field
    
    from ag2 import Agent, Context, tool
    from ag2.ag_ui import AGUIEvent, AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    class Search(BaseModel):
        query: str
        done: bool
    
    class AgentState(BaseModel):
        searches: list[Search] = Field(default_factory=list)
    
    def read_state(context: Context) -> AgentState:
        return AgentState.model_validate({"searches": context.variables.get("searches", [])})
    
    def write_state(context: Context, state: AgentState) -> None:
        context.variables["searches"] = state.model_dump()["searches"]
    
    @tool
    def add_search(
        new_query: Annotated[str, Field(description="The query to add to state")],
        context: Context,
    ) -> str:
        """Add a search to the state."""
        state = read_state(context)
        state.searches.append(Search(query=new_query, done=False))
        write_state(context, state)
        return f"Queued search: {new_query}"
    
    @tool
    async def run_searches(context: Context) -> str:
        """Run the queued searches and mark them done."""
        state = read_state(context)
        for search in state.searches:
            search.done = True
            write_state(context, state)
            # Stream an intermediate snapshot so the UI updates per search
            await context.send(
                AGUIEvent(StateSnapshotEvent(snapshot=dict(context.variables)))
            )
        return "All searches done."
    
    agent = Agent(
        name="assistant",
        prompt=(
            "You are a helpful assistant for storing searches. "
            "Use `add_search` once per query, then call `run_searches`."
        ),
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[add_search, run_searches],
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

### Render state in the UI#

Use the `useAgent` hook to access agent state anywhere in your app. You can render it in the chat, in dashboards, sidebars, or custom layouts.

app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    // ...
    
    // Define the state of the agent, should match the state streamed by your AG2 backend.
    type AgentState = {
      searches: {
        query: string;
        done: boolean;
      }[];
    };
    
    function YourMainContent() {
      // ...
    
      const { agent } = useAgent({
        agentId: "my_agent", // MUST match the agent name in CopilotRuntime
      })
      const state = (agent.state ?? {}) as Partial<AgentState>;
    
      // ...
    
      return (
        <div>
          {/* ... */}
          <div className="flex flex-col gap-2 mt-4">
            {state.searches?.map((search, index) => (
              <div key={index} className="flex flex-row">
                {search.done ? "✅" : "❌"} {search.query}
              </div>
            ))}
          </div>
        </div>
      )
    }

Important

The `agentId` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

### Give it a try#

You've now created a component that renders the agent's state in your UI.

### On this page

What is this?When should I use this?Implementation
