---
url: https://docs.copilotkit.ai/google-adk/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:04.550102+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/google-adk/generative-ui/state-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/google-adk/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/google-adk/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/google-adk/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

State Rendering

Generative UIControlled

# State Rendering

Render your agent's state with custom UI components in real-time.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

shared_state_streaming_agent.py

page.tsx

document-view.tsx

route.ts
    
    
    """Agent backing the State Streaming demo.
    
    The agent writes a long `document` string into shared agent state via a
    `write_document` tool. The UI renders `state["document"]` live as the
    tool arguments arrive.
    
    How the per-token "live" feel is produced:
    
    1. `PredictStateMapping(state_key="document", tool="write_document",
       tool_argument="content", stream_tool_call=True)` is declared on the
       ADKAgent middleware in `registry.py`. The middleware emits a
       STATE_DELTA every time the corresponding tool argument grows.
    2. `streaming_function_call_arguments=True` is also set on the ADKAgent
       middleware so ag_ui_adk subscribes to incremental TOOL_CALL_ARGS
       events from the underlying ADK runner. This requires google-adk
       >= 1.24.0 via Vertex AI for true per-token streaming; on older
       versions or via Gemini Studio the middleware emits a UserWarning at
       startup and falls back to chunk-level streaming, which still drives
       STATE_DELTAs but at coarser granularity. The UI's "LIVE" badge stays
       honest in both modes — it just updates fewer times per second on the
       fallback path.
    
    The model itself does not need a `GenerateContentConfig` override for
    this — the streaming behaviour is entirely controlled by the ADKAgent
    middleware. This matches langgraph-python's StateStreamingMiddleware
    setup.
    """
    
    from __future__ import annotations
    
    from ag_ui_adk import AGUIToolset
    from ag_ui_adk.config import PredictStateMapping
    from google.adk.agents import LlmAgent
    from google.adk.tools import ToolContext
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    
    def write_document(tool_context: ToolContext, document: str) -> dict:
        """Write a document into shared state.
    
        Whenever the user asks you to write or draft anything (essay, poem,
        email, summary, etc.), call this tool with the full content as a
        single string. The UI renders state["document"] live as you type.
    
        Argument name `document` mirrors langgraph-python's `write_document`
        signature so the shared D5 fixture (`tool_argument="document"`) and
        the LGP-aligned PredictStateMapping below stay in lock-step.
        """
        tool_context.state["document"] = document
        return {"status": "ok", "length": len(document)}
    
    
    _INSTRUCTION = (
        "You are a collaborative writing assistant. Whenever the user asks "
        "you to write, draft, or revise any piece of text, ALWAYS call the "
        "`write_document` tool with the full content as a single string. "
        "Never paste the document into a chat message directly — the document "
        "belongs in shared state and the UI renders it live as you type."
    )
    
    shared_state_streaming_agent = LlmAgent(
        name="SharedStateStreamingAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[write_document, AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    
    
    SHARED_STATE_STREAMING_PREDICT_STATE = [
        PredictStateMapping(
            state_key="document",
            tool="write_document",
            tool_argument="document",
            emit_confirm_tool=False,
            stream_tool_call=True,
        ),
    ]
    

## What is this?#

State rendering lets you build UI that reflects your agent's state in real-time. As your agent progresses through nodes and emits state updates, your frontend renders those changes, showing progress, drafts, or intermediate results.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

## When should I use this?#

Use state rendering when you want to:

  * Show real-time progress (e.g. "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside of the chat



## How it works in code#

On the frontend, subscribe to the agent's state. Each time the backend forwards a fresh value, your component re-renders with the latest partial output.

page.tsx
    
    
      // Subscribe to BOTH state changes and run-status changes. The former  // drives the per-token document rerender; the latter toggles the  // "LIVE" badge when the agent starts / stops.  const { agent } = useAgent({    agentId: "shared-state-streaming",    updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],  });

On the backend, a state-streaming mapping forwards a specific tool argument straight into a state key _as it's being generated_. Some frameworks provide that as middleware; direct SDK adapters can emit `STATE_SNAPSHOT` events from their streaming loop. Either way, the UI can watch the answer assemble token-by-token rather than appearing in one burst between checkpoints.

### Install the ADK + AG-UI bridge
    
    
    pip install ag-ui-adk

### Declare the predicted state mapping

ADK state streaming uses `PredictStateMapping` to map the streaming `write_document` tool argument into `state["document"]`. Add `AGUIToolset()` to the agent so CopilotKit can forward the state deltas to the UI.

shared_state_streaming_agent.py
    
    
    from __future__ import annotations
    
    from ag_ui_adk import AGUIToolset
    from ag_ui_adk.config import PredictStateMapping
    from google.adk.agents import LlmAgent
    from google.adk.tools import ToolContext
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    
    def write_document(tool_context: ToolContext, document: str) -> dict:
        """Write a document into shared state.
    
        Whenever the user asks you to write or draft anything (essay, poem,
        email, summary, etc.), call this tool with the full content as a
        single string. The UI renders state["document"] live as you type.
    
        Argument name `document` mirrors langgraph-python's `write_document`
        signature so the shared D5 fixture (`tool_argument="document"`) and
        the LGP-aligned PredictStateMapping below stay in lock-step.
        """
        tool_context.state["document"] = document
        return {"status": "ok", "length": len(document)}
    
    
    _INSTRUCTION = (
        "You are a collaborative writing assistant. Whenever the user asks "
        "you to write, draft, or revise any piece of text, ALWAYS call the "
        "`write_document` tool with the full content as a single string. "
        "Never paste the document into a chat message directly — the document "
        "belongs in shared state and the UI renders it live as you type."
    )
    
    shared_state_streaming_agent = LlmAgent(
        name="SharedStateStreamingAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[write_document, AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    
    
    SHARED_STATE_STREAMING_PREDICT_STATE = [
        PredictStateMapping(
            state_key="document",
            tool="write_document",
            tool_argument="document",
            emit_confirm_tool=False,
            stream_tool_call=True,
        ),
    ]

### Stop after the final model response

The agent above imports `stop_on_terminal_text` and registers it as its `after_model_callback`. This prevents Gemini from issuing the same tool call again after its final text response. See the canonical [`stop_on_terminal_text` implementation](https://github.com/CopilotKit/CopilotKit/blob/main/showcase/integrations/google-adk/src/agents/shared_chat.py) when adapting the callback for your project.

shared_state_streaming_agent.py
    
    
    from __future__ import annotations
    
    from ag_ui_adk import AGUIToolset
    from ag_ui_adk.config import PredictStateMapping
    from google.adk.agents import LlmAgent
    from google.adk.tools import ToolContext
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    
    def write_document(tool_context: ToolContext, document: str) -> dict:
        """Write a document into shared state.
    
        Whenever the user asks you to write or draft anything (essay, poem,
        email, summary, etc.), call this tool with the full content as a
        single string. The UI renders state["document"] live as you type.
    
        Argument name `document` mirrors langgraph-python's `write_document`
        signature so the shared D5 fixture (`tool_argument="document"`) and
        the LGP-aligned PredictStateMapping below stay in lock-step.
        """
        tool_context.state["document"] = document
        return {"status": "ok", "length": len(document)}
    
    
    _INSTRUCTION = (
        "You are a collaborative writing assistant. Whenever the user asks "
        "you to write, draft, or revise any piece of text, ALWAYS call the "
        "`write_document` tool with the full content as a single string. "
        "Never paste the document into a chat message directly — the document "
        "belongs in shared state and the UI renders it live as you type."
    )
    
    shared_state_streaming_agent = LlmAgent(
        name="SharedStateStreamingAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[write_document, AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    
    
    SHARED_STATE_STREAMING_PREDICT_STATE = [
        PredictStateMapping(
            state_key="document",
            tool="write_document",
            tool_argument="document",
            emit_confirm_tool=False,
            stream_tool_call=True,
        ),
    ]
    

### On this page

What is this?When should I use this?How it works in code
