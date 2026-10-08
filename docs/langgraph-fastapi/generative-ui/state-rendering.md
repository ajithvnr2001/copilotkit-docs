---
url: https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:05:17.405987+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/state-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-fastapi/webmcp)

Agent capabilities

LangGraph (FastAPI)

[Sub-agents](https://docs.copilotkit.ai/langgraph-fastapi/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-fastapi/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-fastapi/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-fastapi/community-frameworks)

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

page.tsx

demo-layout.tsx

document-view.tsx

suggestions.ts
    
    
    "use client";import React from "react";import {  CopilotKit,  useAgent,  UseAgentUpdate,} from "@copilotkit/react-core/v2";import { DemoLayout } from "./demo-layout";import { useSharedStateStreamingSuggestions } from "./suggestions";interface StreamingAgentState {  document?: string;}export default function SharedStateStreamingDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="shared-state-streaming">      <DemoContent />    </CopilotKit>  );}function DemoContent() {  // Subscribe to BOTH state changes and run-status changes. The former  // drives the per-token document rerender; the latter toggles the  // "LIVE" badge when the agent starts / stops.  const { agent } = useAgent({    agentId: "shared-state-streaming",    updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],  });  useSharedStateStreamingSuggestions();  const agentState = agent.state as StreamingAgentState | undefined;  const document = agentState?.document ?? "";  const isRunning = agent.isRunning;  return <DemoLayout document={document} isStreaming={isRunning} />;}

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

### Install the LangGraph Python SDK

uvpoetrypipconda
    
    
    uv add copilotkit
    
    
    poetry add copilotkit
    
    
    pip install copilotkit --extra-index-url https://copilotkit.gateway.scarf.sh/simple/
    
    
    conda install copilotkit -c copilotkit-channel

### Add state streaming middleware

`StateStreamingMiddleware` maps a tool argument to an agent state key and forwards partial tool-call arguments as state updates while the model is still generating.

shared_state_streaming.py
    
    
    import uuid
    
    from langchain.agents import AgentState as BaseAgentState, create_agent
    from langchain.tools import ToolRuntime, tool
    from langchain_core.messages import ToolMessage
    from langchain_openai import ChatOpenAI
    from langgraph.types import Command
    
    from copilotkit import (
        CopilotKitMiddleware,
        StateItem,
        StateStreamingMiddleware,
    )
    
    
    class AgentState(BaseAgentState):
        """Shared state. `document` is streamed token-by-token."""
    
        document: str
    
    
    @tool
    def write_document(document: str, runtime: ToolRuntime) -> Command:
        """Write a document for the user.
    
        Always call this tool when the user asks you to write or draft
        something of any length (an essay, poem, email, summary, etc.).
        The `document` argument is streamed *per token* into shared agent
        state under the `document` key, so the UI can render it as it is
        generated.
        """
        return Command(
            update={
                "document": document,
                "messages": [
                    ToolMessage(
                        content="Document written to shared state.",
                        name="write_document",
                        id=str(uuid.uuid4()),
                        tool_call_id=runtime.tool_call_id,
                    )
                ],
            }
        )
    
    
    graph = create_agent(
        model=ChatOpenAI(model="gpt-5.4"),
        tools=[write_document],
        middleware=[
            CopilotKitMiddleware(),
            # Forward every token of write_document's `document` argument
            # straight into state["document"] while the tool call is still
            # streaming. Without this, `document` would only update once
            # the tool call completes.
            #
            # NOTE: the frontend `usePredictStateSubscription` hook indexes
            # the (partial-JSON-parsed) tool args by `state_key`, so the
            # tool's argument name MUST match `state_key` ("document") for
            # per-token deltas to land in `state.document`.
            StateStreamingMiddleware(
                StateItem(
                    state_key="document",
                    tool="write_document",
                    tool_argument="document",
                )
            ),
        ],
        state_schema=AgentState,
        system_prompt=(
            "You are a collaborative writing assistant. Whenever the user asks "
            "you to write, draft, or revise any piece of text, ALWAYS call the "
            "`write_document` tool with the full content as a single string in "
            "the `document` argument. Never paste the document into a chat "
            "message directly — the document belongs in shared state and the "
            "UI renders it live as you type."
        ),
    )

Missing snippet

Region `state-streaming-middleware` not found in `langgraph-fastapi::shared-state-streaming`. Tag the relevant source lines with `// @region[state-streaming-middleware]` / `// @endregion[state-streaming-middleware]`.

Available: frontend-use-coagent-state

### On this page

What is this?When should I use this?How it works in code
