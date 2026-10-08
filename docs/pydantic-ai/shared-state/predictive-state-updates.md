---
url: https://docs.copilotkit.ai/pydantic-ai/shared-state/predictive-state-updates/
title: Predictive state updates
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:31.239436+00:00
---

# Predictive state updates

> Source: https://docs.copilotkit.ai/pydantic-ai/shared-state/predictive-state-updates/

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

[PydanticAI](https://docs.copilotkit.ai/pydantic-ai)[Shared State](https://docs.copilotkit.ai/pydantic-ai/shared-state)

# Predictive state updates

Stream in-progress agent state updates to the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

This example demonstrates predictive state updates in the [CopilotKit Feature Viewer](https://feature-viewer.copilotkit.ai/pydantic-ai/feature/shared_state).

## What is this?#

A Pydantic AI Agent's state updates discontinuosly; only across function transitions in the flow. But even a _single function_ in the flow often takes many seconds to run and contain sub-steps of interest to the user.

**Agent-native applications** reflect to the end-user what the agent is doing **as continuously possible.**

CopilotKit enables this through its concept of **_predictive state updates_**.

## When should I use this?#

You can use this when you want to provide the user with feedback about what your agent is doing, specifically to:

  * **Keep users engaged** by avoiding long loading indicators
  * **Build trust** by demonstrating what the agent is working on
  * Enable **agent steering** \- allowing users to course-correct the agent if needed



## Important Note#

When a function in your Pydantic AI agent finishes executing, **its returned state becomes the single source of truth**. While intermediate state updates are great for real-time feedback, any changes you want to persist must be explicitly included in the function's final returned state. Otherwise, they will be overwritten when the function completes.

## Implementation#

### Define the state#

Create your Pydantic AI agent with a stateful structure. Here's a complete example that tracks observed steps:

agent.py
    
    
    from pydantic import BaseModel
    from pydantic_ai import Agent
    from pydantic_ai.ui import StateDeps
    from pydantic_ai.ui.ag_ui import AGUIAdapter
    from starlette.applications import Starlette
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.routing import Route
    
    
    class AgentState(BaseModel):
        """State for the agent."""
        observed_steps: list[str] = []
    
    
    agent = Agent('openai:gpt-5.4-mini', deps_type=StateDeps[AgentState])
    
    
    async def run_agent(request: Request) -> Response:
        # Build the deps fresh on every request: `dispatch_request` writes the state
        # the client sent into `deps.state`, so a shared instance leaks state between
        # concurrent requests and users.
        return await AGUIAdapter.dispatch_request(
            request, agent=agent, deps=StateDeps(AgentState())
        )
    
    
    app = Starlette(routes=[Route("/", run_agent, methods=["POST"])])
    
    if __name__ == "__main__":
        import uvicorn
    
        uvicorn.run(app, host="0.0.0.0", port=8000)

Then render the predicted state in your frontend:

ui/app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2";
    
    // ...
    
    const YourMainContent = () => {
        // Get access to both predicted and final states
        const { agent } = useAgent({ agentId: "my_agent" });
    
        // Add a state renderer to observe predictions
        useAgent({
            agentId: "my_agent",
            render: ({ state }) => {
                if (!state.observed_steps?.length) return null;
                return (
                    <div>
                        <h3>Current Progress:</h3>
                        <ul>
                            {state.observed_steps.map((step, i) => (
                                <li key={i}>{step}</li>
                            ))}
                        </ul>
                    </div>
                );
            },
        });
    
        return (
            <div>
                <h1>Agent Progress</h1>
                {agent.state?.observed_steps?.length > 0 && (
                    <div>
                        <h3>Final Steps:</h3>
                        <ul>
                            {agent.state.observed_steps.map((step, i) => (
                                <li key={i}>{step}</li>
                            ))}
                        </ul>
                    </div>
                )}
            </div>
        )
    }

Important

The `name` parameter must exactly match the agent name you defined in your CopilotRuntime configuration (e.g., `my_agent` from the quickstart).

### Give it a try!#

Now you'll notice that the state predictions are emitted as the agent makes progress, giving you insight into its work before the final state is determined. You can apply this pattern to any long-running task in your agent.

### On this page

What is this?When should I use this?Important NoteImplementation
