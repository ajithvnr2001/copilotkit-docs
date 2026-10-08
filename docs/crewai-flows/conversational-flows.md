---
url: https://docs.copilotkit.ai/crewai-flows/conversational-flows/
title: Conversational Flows
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:36:02.638632+00:00
---

# Conversational Flows

> Source: https://docs.copilotkit.ai/crewai-flows/conversational-flows/

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

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)

# Conversational Flows

Promote an existing CrewAI Flow to a session-aware Conversational Flow and connect it to CopilotKit through AG-UI.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

CrewAI Conversational Flows are an execution mode for CrewAI Flows, not a separate CopilotKit integration. Start with the [CrewAI Quickstart](https://docs.copilotkit.ai/crewai-flows/quickstart), then opt your existing Flow and its AG-UI endpoint into conversational execution.

Each CopilotKit turn is passed to CrewAI's `stream_turn` API. The integration maps the CopilotKit `threadId` to CrewAI's `session_id`, so each browser thread gets an isolated, multi-turn conversation.

Full CopilotKit support

Conversational Flows support the same CopilotKit features as regular CrewAI Flows, including chat components, headless chat, frontend tools, tool rendering, generative UI, shared state, reasoning, human-in-the-loop, subagents, voice, and multimodal input. Your CopilotKit frontend code does not change when you promote a Flow.

## Prerequisites#

  * Complete the [CrewAI Quickstart](https://docs.copilotkit.ai/crewai-flows/quickstart) with a working Flow and AG-UI endpoint.
  * Install CrewAI 1.15.11 or later. Earlier versions do not provide the `stream_turn` behavior required by this integration.
  * Use the latest `ag-ui-crewai` release.



Terminal
    
    
    pip install -U "crewai>=1.15.11,<2" ag-ui-crewai

## Promote your Flow#

### Enable conversational execution on the Flow#

Add `conversational = True` to the Flow class you created in the Quickstart. You do not need a second agent or a separate deployment.

flow.py
    
    
    class SupportFlow(Flow[AppState]):
        conversational = True
    
        # Keep your Flow methods, tools, and state here.

### Enable conversational execution on the endpoint#

Pass the same opt-in when you register the Flow with FastAPI:

server.py
    
    
    from fastapi import FastAPI
    from ag_ui_crewai import add_crewai_flow_fastapi_endpoint
    
    from flow import SupportFlow
    
    app = FastAPI()
    
    add_crewai_flow_fastapi_endpoint(
        app,
        SupportFlow(),
        "/",
        conversational=True,  
    )

The endpoint now calls `stream_turn(message, session_id=thread_id)` instead of starting the Flow through the regular `kickoff` or `astream` path.

### Keep the CopilotKit frontend unchanged#

Continue using the same `<CopilotKit>`, chat component, hooks, tools, and generative UI components from the Quickstart and feature guides. The execution-mode change is entirely in the CrewAI backend.

## Feature-specific notes#

Most CopilotKit features require no additional Conversational Flow configuration. These are the exceptions to keep in mind:

When you use| What to do  
---|---  
Custom Pydantic state| Inherit from `ag_ui_crewai.CopilotKitState`. It includes the conversation fields CrewAI needs alongside CopilotKit messages, tools, and shared state.  
CrewAI conversational routes| Route a turn with `route_turn()` and `@listen(...)`. Return the public reply or call `append_assistant_message()` once; CrewAI already appends the current user message.  
Native interrupts with `useInterrupt`| Register the endpoint with `emit_interrupt_outcome=True` and `enable_legacy_on_interrupt_event=False`, just as you would for a regular CrewAI Flow.  
CrewAI persistence| Keep using CrewAI's `@persist` support. CopilotKit supplies a stable `threadId`, and the integration uses it as the CrewAI `session_id`.  
  
For an interrupt-enabled endpoint, the registration looks like this:

server.py
    
    
    add_crewai_flow_fastapi_endpoint(
        app,
        SupportFlow(),
        "/",
        conversational=True,
        emit_interrupt_outcome=True,
        enable_legacy_on_interrupt_event=False,
    )

## Existing Flow routing#

Enabling conversational mode adds CrewAI's turn router to your Flow. If your existing Flow already produces one public response from an `@start` graph, make sure the conversational router does not also send a built-in `converse` response. For intent-based conversations, move the per-turn entry points behind `route_turn()` and `@listen(...)` handlers.

flow.py
    
    
    from crewai.flow import listen
    
    class SupportFlow(Flow[AppState]):
        conversational = True
    
        def route_turn(self, _context):
            return "support"
    
        @listen("support")
        def answer(self):
            return self.run_existing_support_logic()

## Runtime contract#

Both opt-ins are required. If the endpoint requests conversational execution but the Flow does not declare `conversational = True` or expose `stream_turn`, the integration returns a correlated `RUN_ERROR` instead of silently falling back to regular Flow execution.

## Next steps#

  * **Build the base integration:** [CrewAI Quickstart](https://docs.copilotkit.ai/crewai-flows/quickstart) — create the Flow and CopilotKit application that this guide promotes.
  * **Add generative UI:** [Tool rendering](https://docs.copilotkit.ai/crewai-flows/generative-ui/tool-rendering) — render CrewAI tool activity with application components.
  * **Synchronize application state:** [Shared state](https://docs.copilotkit.ai/crewai-flows/shared-state) — let your Conversational Flow read and update frontend state.
  * **Pause for user input:** [Human in the loop](https://docs.copilotkit.ai/crewai-flows/human-in-the-loop) — suspend a turn and resume it with structured user feedback.



### On this page

PrerequisitesPromote your FlowFeature-specific notesExisting Flow routingRuntime contractNext steps
