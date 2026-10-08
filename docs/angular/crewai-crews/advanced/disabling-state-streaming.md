---
url: https://docs.copilotkit.ai/angular/crewai-crews/advanced/disabling-state-streaming/
title: Disabling state streaming
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:04.923211+00:00
---

# Disabling state streaming

> Source: https://docs.copilotkit.ai/angular/crewai-crews/advanced/disabling-state-streaming/

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

Disabling state streaming

Agent capabilitiesCrewAI FlowsAdvanced

# Disabling state streaming

Granularly control what is streamed to the frontend.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

By default, CopilotKit will stream both your messages and tool calls to the frontend when you use `copilotkit_stream`. You can disable this by choosing when to use `copilotkit_stream` vs calling `completion` directly.

## When should I use this?#

Occasionally, you'll want to disable streaming temporarily — for example, the LLM may be doing something the current user should not see, like emitting tool calls or questions pertaining to other employees in an HR system.

## Implementation#

### Disable all streaming#

You can control whether to stream messages or tool calls by selectively wrapping calls to `completion` with `copilotkit_stream`.

Python
    
    
    from copilotkit.crewai import copilotkit_stream
    from typing import cast, Any
    from litellm import completion
    
    @start()
    async def start(self):
    
        # 1) Do not emit messages or tool calls, keeping the LLM call private.
        response = completion(
            model="openai/gpt-5.4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant"},
                *self.state.messages
            ],
        )
        message = response.choices[0].message
    
        # 2) Or wrap the LLM call with `copilotkit_stream` to stream message tokens.
        #    Note that we pass `stream=True` to the inner `completion` call.
        response = await copilotkit_stream(
            completion(
                model="openai/gpt-5.4",
                messages=[
                    {"role": "system", "content": "You are a helpful assistant"},
                    *self.state.messages
                ],
                stream=True
            )
        )
        message = cast(Any, response).choices[0]["message"]

### On this page

What is this?When should I use this?ImplementationDisable all streaming
