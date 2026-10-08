---
url: https://docs.copilotkit.ai/pydantic-ai/agent-app-context/
title: Readables
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:23:12.096106+00:00
---

# Readables

> Source: https://docs.copilotkit.ai/pydantic-ai/agent-app-context/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendPydanticAI

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/pydantic-ai)[Quickstart](https://docs.copilotkit.ai/pydantic-ai/quickstart)[Build with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/pydantic-ai/webmcp)

Agent capabilities

Pydantic AI

[Sub-agents](https://docs.copilotkit.ai/pydantic-ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/pydantic-ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/pydantic-ai/learning)

[User Memories](https://docs.copilotkit.ai/pydantic-ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/pydantic-ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/pydantic-ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/pydantic-ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/pydantic-ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/pydantic-ai/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/pydantic-ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/pydantic-ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[PydanticAI](https://docs.copilotkit.ai/pydantic-ai)

# Readables

Share app specific context with your Pydantic AI agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

One of the most common use cases for CopilotKit is to register app state and context using `useAgentContext`. This way, you can notify CopilotKit of what is going on in your app in real time. Some examples might be: the current user, the current page, etc.

This context can then be shared with your Pydantic AI agent.

## Implementation#

Context values arrive as JSON strings

The AG-UI protocol defines a context value as a string. Therefore `useAgentContext` calls `JSON.stringify` on any `value` that is not already a string, and your agent receives the JSON text instead of the object or the array.

Parse the value before you read a field from it. Use `json.loads(item["value"])` in Python, or `JSON.parse(item.value)` in TypeScript. If you skip the parse step, an index such as `colleagues[0]` returns a single character, and a shape check such as `isinstance(value, list)` can never pass.

Do not stringify the value again, because that produces double encoding. A `value` that is already a string is sent unchanged, so no parse step is needed for it.

Check out the [Frontend Data documentation](https://docs.copilotkit.ai/langgraph-python/agent-app-context) to understand what this is and how to use it.

Unlike `messages`, `tools` and `state`, Pydantic AI's AG-UI adapter does **not** pass `context` to your agent on its own — and it does not warn when it drops it, so an agent that never received your entries will still answer confidently about them. This is deliberate: entries are client-submitted, so Pydantic AI leaves it to you to decide what to trust. Read them off `run_input` and hand them to the agent yourself, as shown below. See Pydantic AI's [AG-UI Context guide](https://pydantic.dev/docs/ai/integrations/ui/ag-ui/#context).

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Add the data to the Copilot#

The [`useAgentContext` hook](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext) is used to add data as context to the Copilot.

YourComponent.tsx
    
    
    "use client" // only necessary if you are using Next.js with the App Router.
    import { useAgentContext } from "@copilotkit/react-core/v2"; 
    import { useState } from 'react';
    
    export function YourComponent() {
      // Create colleagues state with some sample data
      const [colleagues, setColleagues] = useState([
        { id: 1, name: "John Doe", role: "Developer" },
        { id: 2, name: "Jane Smith", role: "Designer" },
        { id: 3, name: "Bob Wilson", role: "Product Manager" }
      ]);
    
      // Share context with the agent
      useAgentContext({
        description: "The current user's colleagues",
        value: colleagues,
      });
      return (
        // Your custom UI component
        <>...</>
      );
    }

### Consume the data in your Pydantic AI agent#

The entries arrive on `RunAgentInput.context`. Build the adapter in two steps so you can reach `run_input`, pass the entries into `deps`, and expose them to the model through a tool.

agent.py
    
    
    import json
    from dataclasses import dataclass
    
    from ag_ui.core import Context
    from pydantic_ai import Agent, RunContext
    from pydantic_ai.ui.ag_ui import AGUIAdapter
    from starlette.applications import Starlette
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.routing import Route
    
    
    @dataclass
    class AppContextDeps:
        """The entries the frontend shared on this run."""
    
        context: list[Context]
    
    
    agent = Agent(
        "openai:gpt-5.4-mini",
        instructions="You are a helpful assistant that can help emailing colleagues.",
        deps_type=AppContextDeps, 
    )
    
    
    @agent.tool
    def colleagues(ctx: RunContext[AppContextDeps]) -> list[dict]:
        """The current user's colleagues, as the app shared them."""
        for entry in ctx.deps.context:
            if entry.description == "The current user's colleagues":
                # `useAgentContext` JSON-stringifies `value` before it leaves the
                # browser, and AG-UI types `Context.value` as a string, so parse it.
                return json.loads(entry.value)
        return []
    
    
    async def run_agent(request: Request) -> Response:
        # `dispatch_request` parses the request internally, so build the adapter in
        # two steps instead: `run_input` is what carries the frontend's entries.
        adapter = await AGUIAdapter.from_request(request, agent=agent)
        deps = AppContextDeps(context=adapter.run_input.context)
        return adapter.streaming_response(adapter.run_stream(deps=deps))
    
    
    app = Starlette(routes=[Route("/", run_agent, methods=["POST"])])
    
    if __name__ == "__main__":
        import uvicorn
        uvicorn.run(app, host="0.0.0.0", port=8000)

Two details are easy to miss:

  * **`value` is a string, not your object.** `useAgentContext` calls `JSON.stringify` on the value before the run leaves the browser, and AG-UI types `Context.value` as a string on both ends. So `json.loads` is required, and a shape check like `isinstance(entry.value, list)` can never pass.
  * **Reach for`from_request`, not `dispatch_request`.** The one-line `AGUIAdapter.dispatch_request(request, agent=agent)` used elsewhere in these docs parses the request for you, which leaves you no `run_input` to build `deps` from.



### Give it a try!#

Ask your agent a question about the context, like "Who are my colleagues?". It should be able to answer!

## Keep entries as data, not instructions#

Every entry is a claim your frontend made, so it describes a request — it never establishes who is making it. Deliver entries to the model as **data** , the way the tool above does. Do not build [`instructions`](https://pydantic.dev/docs/ai/agents/#instructions) out of them: instructions carry operator authority, so composing them from client-submitted text lets a prompt injection inherit that authority.

Facts your _server_ established — the authenticated user, the workspace, the tenant — are what belong in instructions. To let a client-supplied fact change how the agent behaves, authenticate it first, look up the policy your server holds for it, and write the instruction from that. The entry itself stays data.

### On this page

ImplementationKeep entries as data, not instructions
