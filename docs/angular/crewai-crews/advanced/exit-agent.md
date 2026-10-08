---
url: https://docs.copilotkit.ai/angular/crewai-crews/advanced/exit-agent/
title: Exiting the agent loop
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:05.114494+00:00
---

# Exiting the agent loop

> Source: https://docs.copilotkit.ai/angular/crewai-crews/advanced/exit-agent/

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

Agent capabilitiesCrewAI FlowsAdvanced

# Exiting the agent loop

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

After your agent has finished a workflow, you'll usually want to explicitly end that loop by calling the `copilotkit_exit()` method in your Python code.

Exiting the agent has different effects depending on mode:

  * **Router Mode** : Exiting the agent hands responsibility for handling input back to the router, which can initiate chat, call actions, other agents, etc. The router can return to this agent later (starting a new loop) to satisfy a user request.

  * **Agent Lock Mode** : Exiting the agent restarts the workflow loop for the current agent.




In this example from [our email-sending app](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-qa), the `send_email` node explicitly exits, then manually sends a response back to the user as a `ToolMessage`:

### Install the CopilotKit SDK#

Any LangGraph agent can be used with CopilotKit. However, creating deep agentic experiences with CopilotKit requires our LangGraph SDK.

PythonTypeScript

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

`npm npm install @copilotkit/sdk-js `

### Exit the agent loop#

This will exit the agent session as soon as the current CrewAI run is finished, either by a breakpoint or by reaching the `END` node.

Python
    
    
    from litellm import completion
    from crewai.flow.flow import start
    from copilotkit.crewai import copilotkit_exit
    # ...
    @start()
    async def send_email(self):
        """Send an email."""
    
    
        # get the last message and cast to ToolMessage
        last_message = self.state["messages"][-1]
        if last_message["content"] == "CANCEL":
            text_message = "❌ Cancelled sending email."
        else:
            text_message = "✅ Sent email."
        self.state["messages"].append({"role": "assistant", "content": text_message, "id": str(uuid.uuid4())})
        # Exit the agent loop after processing
        await copilotkit_exit() 
