---
url: https://docs.copilotkit.ai/angular/crewai-crews/advanced/emit-messages/
title: Manually emitting messages
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:05.006568+00:00
---

# Manually emitting messages

> Source: https://docs.copilotkit.ai/angular/crewai-crews/advanced/emit-messages/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/crewai-crews)[Quickstart](https://docs.copilotkit.ai/angular/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

Advanced

[Disabling state streaming](https://docs.copilotkit.ai/angular/crewai-crews/advanced/disabling-state-streaming)[Manually emitting messages](https://docs.copilotkit.ai/angular/crewai-crews/advanced/emit-messages)[Exiting the agent loop](https://docs.copilotkit.ai/angular/crewai-crews/advanced/exit-agent)

[Multi-Agent Flows](https://docs.copilotkit.ai/angular/crewai-crews/multi-agent/subagents)

[Sub-agents](https://docs.copilotkit.ai/angular/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Manually emitting messages

Agent capabilitiesCrewAI FlowsAdvanced

# Manually emitting messages

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

While most agent interactions happen automatically through shared state updates as the agent runs, you can also **manually send messages from within your agent code** to provide immediate feedback to users.

This video shows the result of `npx copilotkit@latest init` with the implementation section applied to it!

## What is this?#

In CrewAI, messages are only emitted when a function is completed. CopilotKit allows you to manually emit messages in the middle of a function's execution to provide immediate feedback to the user.

## When should I use this?#

Manually emitted messages are great for **when you don't want to wait for the function** to complete **and you** :

  * Have a long running task that you want to provide feedback on
  * Want to provide a status update to the user
  * Want to provide a warning or error message



## Implementation#

### Run and Connect Your Agent to CopilotKit#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/angular/langgraph-python/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Install the CopilotKit SDK#

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Manually emit a message#

The `copilotkit_emit_message` method allows you to emit messages early in a functions's execution to communicate status updates to the user. This is particularly useful for long running tasks.

Python
    
    
    from litellm import completion
    from crewai.flow.flow import start
    from copilotkit.crewai import copilotkit_emit_message 
    # ...
    
    @start()
    async def start(self):
        intermediate_message = "Thinking really hard..."
        await copilotkit_emit_message(intermediate_message)
    
        # simulate a long running task
        await asyncio.sleep(2)
    
        response = copilotkit_stream(
            completion(
                model="openai/gpt-5.4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    *self.state["messages"]
                ],
                stream=True
            )
        )
         message = response.choices[0]["message"]
    
        self.state["messages"].append(message)

### Give it a try!#

Now when you talk to your agent you'll notice that it immediately responds with the message "Thinking really hard..." before giving you a response 2 seconds later.

### On this page

What is this?When should I use this?Implementation
