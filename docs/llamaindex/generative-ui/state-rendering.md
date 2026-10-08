---
url: https://docs.copilotkit.ai/llamaindex/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:14:52.684324+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/llamaindex/generative-ui/state-rendering/

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

[Components as Tools](https://docs.copilotkit.ai/llamaindex/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/llamaindex/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/llamaindex/generative-ui/state-rendering)

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

State Rendering

Generative UIControlled

# State Rendering

Render the state of your agent with custom UI components.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

## What is this?#

LlamaIndex Agents using the AG-UI workflow router are stateful. This means that as your agent progresses through its workflow, a state object is maintained throughout the session. CopilotKit allows you to render this state in your application with custom UI components, which we call **Agentic Generative UI**.

## When should I use this?#

Rendering the state of your agent in the UI is useful when you want to provide the user with feedback about the overall state of a session. A great example of this is a situation where a user and an agent are working together to solve a problem. The agent can store a draft in its state which is then rendered in the UI.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Set up your agent with state#

Create your LlamaIndex agent with a stateful structure using `initial_state`. Here's a complete example that tracks searches:

agent.py
    
    
    import asyncio
    from typing import Annotated
    from fastapi import FastAPI
    from llama_index.llms.openai import OpenAI
    from llama_index.core.workflow import Context
    from llama_index.protocols.ag_ui.router import get_ag_ui_workflow_router
    from llama_index.protocols.ag_ui.events import StateSnapshotWorkflowEvent
    
    async def addSearch(
        ctx: Context,
        query: Annotated[str, "The search query to add."]
    ) -> str:
        """Add a search to the agent's list of searches."""
        async with ctx.store.edit_state() as global_state:
            state = global_state.get("state", {})
            if state is None:
                state = {}
    
            if "searches" not in state:
                state["searches"] = []
    
            # Add new search
            new_search = {"query": query, "done": False}
            state["searches"].append(new_search)
    
            # Emit state snapshot to frontend
            ctx.write_event_to_stream(
                StateSnapshotWorkflowEvent(
                    snapshot=state
                )
            )
    
            global_state["state"] = state
    
        return f"Added search: {query}"
    
    async def runSearches(ctx: Context) -> str:
        """Run all the searches that have been added."""
        async with ctx.store.edit_state() as global_state:
            state = global_state.get("state", {})
            if state is None:
                state = {}
    
            if "searches" not in state:
                state["searches"] = []
    
            # Update each search to done
            for search in state["searches"]:
                if not search.get("done", False):
                    await asyncio.sleep(1)  # Simulate search execution
                    search["done"] = True
    
                    # Emit state update as each search completes
                    ctx.write_event_to_stream(
                        StateSnapshotWorkflowEvent(
                            snapshot=state
                        )
                    )
    
            global_state["state"] = state
    
        return "All searches completed!"
    
    # Initialize the LLM
    llm = OpenAI(model="gpt-5.4")
    
    # Create the AG-UI workflow router
    agentic_chat_router = get_ag_ui_workflow_router(
        llm=llm,
        system_prompt="""
        You are a helpful assistant for storing searches.
    
        IMPORTANT:
        - Use the addSearch tool to add a search to the agent's state
        - After using the addSearch tool, YOU MUST ALWAYS use the runSearches tool to run the searches
        - ONLY USE THE addSearch TOOL ONCE FOR A GIVEN QUERY
    
        When adding searches, update the state to track:
        - query: the search query
        - done: whether the search is complete (false initially, true after running)
        """,
        backend_tools=[addSearch, runSearches],
        initial_state={
            "searches": []
        },
    )
    
    # Create FastAPI app
    app = FastAPI(
        title="LlamaIndex Agent",
        description="A LlamaIndex agent integrated with CopilotKit",
        version="1.0.0"
    )
    
    # Include the router
    app.include_router(agentic_chat_router)
    
    # Health check endpoint
    @app.get("/health")
    async def health_check():
        return {"status": "healthy", "agent": "llamaindex"}
    
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="localhost", port=8000)

### Render state of the agent in the chat#

Now we can utilize `useAgent` with a `render` function to render the state of our agent **in the chat**.

app/page.tsx
    
    
    // ...
    import { useAgent } from "@copilotkit/react-core/v2";
    // ...
    
    // Define the state of the agent, should match the state of your LlamaIndex Agent.
    type AgentState = {
      searches: {
        query: string;
        done: boolean;
      }[];
    };
    
    function YourMainContent() {
      // ...
    
      // styles omitted for brevity
      useAgent({
        agentId: "my_agent",
        render: ({ state }) => (
          <div>
            {state.searches?.map((search, index) => (
              <div key={index}>
                {search.done ? "✅" : "❌"} {search.query}{search.done ? "" : "..."}
              </div>
            ))}
          </div>
        ),
      });
    
      // ...
    
      return <div>...</div>;
    }

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

### Render state outside of the chat#

You can also render the state of your agent **outside of the chat**. This is useful when you want to render the state of your agent anywhere other than the chat.

app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    // ...
    
    // Define the state of the agent, should match the state of your LlamaIndex Agent.
    type AgentState = {
      searches: {
        query: string;
        done: boolean;
      }[];
    };
    
    function YourMainContent() {
      // ...
    
      const { agent } = useAgent({
        agentId: "my_agent",
      })
    
      // ...
    
      return (
        <div>
          {/* ... */}
          <div className="flex flex-col gap-2 mt-4">
            {agent.state?.searches?.map((search, index) => (
              <div key={index} className="flex flex-row">
                {search.done ? "✅" : "❌"} {search.query}
              </div>
            ))}
          </div>
        </div>
      )
    }

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

### Give it a try!#

You've now created a component that will render the agent's state in the chat.

### On this page

What is this?When should I use this?Implementation
