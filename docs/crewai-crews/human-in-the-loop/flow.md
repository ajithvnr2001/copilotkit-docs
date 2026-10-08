---
url: https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/flow/
title: CrewAI Flows
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:10.102067+00:00
---

# CrewAI Flows

> Source: https://docs.copilotkit.ai/crewai-crews/human-in-the-loop/flow/

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

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)[Human-in-the-Loop](https://docs.copilotkit.ai/crewai-crews/human-in-the-loop)

# CrewAI Flows

Learn how to implement Human-in-the-Loop (HITL) using CrewAI Flows.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

Pictured above is the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter-crewai-flows) with the implementation below applied!

## What is this?#

[Flow based agents](https://docs.crewai.com/concepts/flows) are stateful agents that can be interrupted and resumed to allow for user input.

CopilotKit lets you to add custom UI to take user input and then pass it back to the agent upon completion.

## Why should I use this?#

Human-in-the-loop is a powerful way to implement complex workflows that are production ready. By having a human in the loop, you can ensure that the agent is always making the right decisions and ultimately is being steered in the right direction.

Flow based agents are a great way to implement HITL for more complex workflows where you want to ensure the agent is aware of everything that has happened during a HITL interaction.

## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/crewai-flows/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/CopilotKit/CopilotKit/tree/main/examples/coagents-starter-crewai-flows) as a starting point as this guide uses it as a starting point.

### Install the CopilotKit SDK#

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Add a `useFrontendTool` to your Frontend#

First, we'll create a component that renders the agent's essay draft and waits for user approval.

ui/app/page.tsx
    
    
    function YourMainContent() {
      // ...
    
      useFrontendTool({
        name: "writeEssay",
        available: "remote",
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

### Setup the CrewAI Agent#

Now we'll setup the CrewAI agent. The flow is hard to understand without a complete example, so below is the complete implementation of the agent with explanations.

Some main things to note:

  * The agent's state inherits from `CopilotKitState` to bring in the CopilotKit actions.
  * CopilotKit's actions are bound to the model as tools.
  * If the `writeEssay` action is found in the model's response, the agent will pass control back to the frontend to get user feedback.



Python

agent.py
    
    
    from typing import Any, cast
    from crewai.flow.flow import Flow, start, listen
    from copilotkit import CopilotKitState
    from copilotkit.crewai import copilotkit_stream
    from litellm import completion
    
    
    class AgentState(CopilotKitState):
        pass
    
    
    class SampleAgentFlow(Flow[AgentState]):
    
        @start()
        async def check_for_user_feedback(self):
            if not self.state.get("messages"):
                return
    
            last_message = cast(Any, self.state["messages"][-1])
    
            # Expecting the result of a CopilotKit tool call (SEND/CANCEL)
            if last_message["role"] == "tool":
                user_response = last_message.get("content")
    
                if user_response == "SEND":
                    self.state["messages"].append({
                        "role": "assistant",
                        "content": "✅ Great! Sending your essay via email.",
                    })
                    return
    
                if user_response == "CANCEL":
                    self.state["messages"].append({
                        "role": "assistant",
                        "content": "❌ Okay, we can improve the draft. What would you like to change?",
                    })
                    return
    
            # If no tool result yet, or it's a user message, prompt next step
            if last_message.get("role") == "user":
                self.state["messages"].append({
                    "role": "system",
                    "content": (
                        "You write essays. Use your tools to write an essay; "
                        "don’t just write it in plain text."
                    )
                })
    
        @listen(check_for_user_feedback)
        async def chat(self):
            messages = self.state.get("messages", [])
    
            system_message = {
                "role": "system",
                "content": (
                    "You write essays. Use your tools to write an essay; "
                    "don’t just write it in plain text."
                )
            }
    
            response = await copilotkit_stream(
                completion(
                    model="openai/gpt-5.4",
                    messages=[system_message, *messages],
                    tools=self.state["copilotkit"]["actions"],
                    stream=True
                )
            )
    
            self.state["messages"].append(response.choices[0].message)

### Give it a try!#

Try asking your agent to write an essay about the benefits of AI. You'll see that it will generate an essay, stream the progress and eventually ask you to review it.

### On this page

What is this?Why should I use this?Implementation
