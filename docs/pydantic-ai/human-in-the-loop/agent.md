---
url: https://docs.copilotkit.ai/pydantic-ai/human-in-the-loop/agent/
title: Pydantic AI Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:24:05.808293+00:00
---

# Pydantic AI Agents

> Source: https://docs.copilotkit.ai/pydantic-ai/human-in-the-loop/agent/

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

[PydanticAI](https://docs.copilotkit.ai/pydantic-ai)[Human-in-the-Loop](https://docs.copilotkit.ai/pydantic-ai/human-in-the-loop)

# Pydantic AI Agents

Learn how to implement Human-in-the-Loop (HITL) using Pydantic AI Agents.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

[Flow based agents](https://docs.pydantic-ai.com/concepts/flows) are stateful agents that can be interrupted and resumed to allow for user input.

CopilotKit lets you to add custom UI to take user input and then pass it back to the agent upon completion.

## Why should I use this?#

Human-in-the-loop is a powerful way to implement complex workflows that are production ready. By having a human in the loop, you can ensure that the agent is always making the right decisions and ultimately is being steered in the right direction.

Flow based agents are a great way to implement HITL for more complex workflows where you want to ensure the agent is aware of everything that has happened during a HITL interaction.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/pydantic-ai/quickstart) guide.

If you don't already have an agent, you can use the [Pydantic AI starter](https://github.com/CopilotKit/CopilotKit/tree/main/examples/integrations/pydantic-ai) as a starting point as this guide uses it as a starting point.

### Add a `useFrontendTool` to your Frontend#

First, we'll create a component that renders the agent's essay draft and waits for user approval.

ui/app/page.tsx
    
    
    function YourMainContent() {
      // ...
    
      useFrontendTool({
        name: "write_essay",
        available: "frontend",
        description: "Writes an essay and takes the draft as an argument.",
        parameters: z.object({
          draft: z.string().describe("The draft of the essay"),
        }),
        renderAndWaitForResponse: ({ args, respond, status }) => {
          return (
            <div>
    <Markdown content={args.draft || 'Preparing your draft...'} />
    
              <div className={`flex gap-4 pt-4 ${status !== "executing" ? "hidden" : ""}`}>
                <button
                  onClick={() => respond?.("CANCEL")}
                  disabled={status !== "executing"}
                  className="border p-2 rounded-xl w-full"
                >
                  Try Again
                </button>
                <button
                  onClick={() => respond?.("SEND")}
                  disabled={status !== "executing"}
                  className="bg-blue-500 text-white p-2 rounded-xl w-full"
                >
                  Approve Draft
                </button>
              </div>
            </div>
          );
        },
      });
    
      // ...
    }

### Setup the Pydantic AI Agent#

Now we'll setup the Pydantic AI agent. The flow is hard to understand without a complete example, so below is the complete implementation of the agent with explanations.

Some main things to note:

  * The agent's state inherits from `CopilotKitState` to bring in the CopilotKit actions.
  * CopilotKit's actions are bound to the model as tools.
  * If the `writeEssay` action is found in the model's response, the agent will pass control back to the frontend to get user feedback.



Python

agent/sample_agent/agent.py
    
    
    from pydantic_ai import Agent
    from pydantic_ai.ui.ag_ui import AGUIAdapter
    from starlette.applications import Starlette
    from starlette.requests import Request
    from starlette.responses import Response
    from starlette.routing import Route
    
    agent = Agent('openai:gpt-5.4-mini')
    
    @agent.tool_plain
    async def write_essay(topic: str) -> str:
        """Write an essay on the given topic."""
        # This would typically generate an essay
        # The agent will wait for user feedback before proceeding
        return f"Essay draft on '{topic}' has been generated. Please review."
    
    
    async def run_agent(request: Request) -> Response:
        return await AGUIAdapter.dispatch_request(request, agent=agent)
    
    
    app = Starlette(routes=[Route("/", run_agent, methods=["POST"])])

### Give it a try!#

Try asking your agent to write an essay about the benefits of AI. You'll see that it will generate an essay, stream the progress and eventually ask you to review it.

### On this page

What is this?Why should I use this?Implementation
