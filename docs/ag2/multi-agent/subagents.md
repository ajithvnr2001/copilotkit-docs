---
url: https://docs.copilotkit.ai/ag2/multi-agent/subagents/
title: Subagents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:44:34.621512+00:00
---

# Subagents

> Source: https://docs.copilotkit.ai/ag2/multi-agent/subagents/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAG2

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ag2)[Quickstart](https://docs.copilotkit.ai/ag2/quickstart)[Build with agents](https://docs.copilotkit.ai/ag2/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ag2/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ag2/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ag2/webmcp)

Agent capabilities

AG2

[Sub-agents](https://docs.copilotkit.ai/ag2/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ag2/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ag2/learning)

[User Memories](https://docs.copilotkit.ai/ag2/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ag2/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ag2/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ag2/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ag2/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ag2/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ag2/telemetry)[Community frameworks](https://docs.copilotkit.ai/ag2/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Sub-agents

Agent capabilities

# Subagents

Delegate work from one AG2 agent to another and render each delegation in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Introduction#

AG2 (1.0+) delegates by turning an agent into a tool. `Agent.as_tool()` returns a regular tool that, when the coordinator's model calls it, runs the other agent on its own isolated stream with its own history. The coordinator's context stays small, and the decision to delegate stays with the model.

CopilotKit sees each delegation twice: as an ordinary tool call, and as an AG-UI 1.0 **subagent invocation** (`SUBAGENT_STARTED`, `SUBAGENT_FINISHED`, `SUBAGENT_ERROR`), so you can render "researching…" / "writing…" progress without any extra wiring on the backend.

CopilotKit consumes AG-UI protocol events streamed by AG2 over `/chat`. See the [AG2 AG-UI integration docs](https://docs.ag2.ai/docs/user-guide/ag-ui/) and the upstream [AG2 subagents guide](https://docs.ag2.ai/docs/user-guide/subagents/).

## Backend#

Install AG2 with the AG-UI and OpenAI extras:
    
    
    pip install "ag2[ag-ui,openai]>=1.1.2"

Build each specialist as a plain `Agent`, then hand them to the coordinator as tools. Only the coordinator is wrapped in `AGUIStream` — the specialists are reached through it:

agent.py
    
    
    from typing import Annotated
    
    from fastapi import FastAPI, Header
    from fastapi.responses import StreamingResponse
    from pydantic import Field
    
    from ag2 import Agent, tool
    from ag2.ag_ui import AGUIStream, RunAgentInput
    from ag2.config import OpenAIResponsesConfig
    
    @tool
    def search_docs(
        query: Annotated[str, Field(description="What to look up")],
    ) -> str:
        """Look a topic up in the product documentation."""
        return f"Docs say: {query} is supported since v1.0."
    
    researcher = Agent(
        name="researcher",
        prompt="You research topics using the documentation tool and report findings plainly.",
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[search_docs],
    )
    
    writer = Agent(
        name="writer",
        prompt="You turn research notes into a single tight paragraph.",
        config=OpenAIResponsesConfig(model="gpt-5.5"),
    )
    
    coordinator = Agent(
        name="coordinator",
        prompt=(
            "You coordinate specialists. Delegate research to `task_researcher`, "
            "then hand the findings to `task_writer`. Do not answer from memory."
        ),
        config=OpenAIResponsesConfig(model="gpt-5.5"),
        tools=[
            researcher.as_tool(description="Research a topic in the product docs."),
            writer.as_tool(description="Turn research notes into one paragraph."),
        ],
    )
    
    stream = AGUIStream(coordinator)
    app = FastAPI()
    
    @app.post("/chat")
    async def run_agent(
        message: RunAgentInput,
        accept: str | None = Header(None),
    ) -> StreamingResponse:
        return StreamingResponse(
            stream.dispatch(message, accept=accept),
            media_type=accept or "text/event-stream",
        )

`as_tool()` names the tool `task_<agent name>` by default — `task_researcher` and `task_writer` above. Pass `name=` to override it, and `description=` is required: it is the only thing the coordinator's model reads when deciding whether to delegate.

## What reaches the frontend#

Each delegation produces one tool call and one subagent invocation with its own `subagentRunId`, so two parallel delegations to the same agent can be told apart:
    
    
    RUN_STARTED
    TOOL_CALL_START      toolCallName: "task_researcher"
    TOOL_CALL_ARGS
    SUBAGENT_STARTED     subagentRunId: "4f1c…", name: "researcher", description: "<the objective>"
    SUBAGENT_FINISHED    subagentRunId: "4f1c…", result: "<what it returned>"
    TOOL_CALL_RESULT
    TOOL_CALL_END
    …
    TEXT_MESSAGE_CHUNK
    RUN_FINISHED

  * A failed delegation ends with `SUBAGENT_ERROR` carrying the message, and the run carries on: the coordinator's model is told the delegation failed and may recover. A cancelled or timed-out one also ends with `SUBAGENT_ERROR` (`cancelled` or `expired`).
  * The events carry no usage; the run's own usage already includes what the delegation spent.
  * Delegations are no longer reported as `STEP_STARTED` / `STEP_FINISHED`. If you filtered on `task:<agent name>` steps, subscribe to the `SUBAGENT_*` events instead.
  * If a specialist asks the human a question, it reaches the client like any other [interrupt](https://docs.copilotkit.ai/ag2/human-in-the-loop#approve-a-tool-call-with-interrupts), tagged with the invocation's `subagentRunId`.



Two consequences worth knowing before you build UI on top of it:

  * **Delegations are ordinary tool calls.** Anything you can do for a tool call you can do for a subagent — render it with `useRenderTool`, or let the default tool renderer show it. See [Tool rendering](https://docs.copilotkit.ai/ag2/generative-ui/tool-rendering).
  * **The specialist's own tool calls stay inside its stream.** `search_docs` above runs in the researcher's isolated stream, so it does not appear as a separate `TOOL_CALL_*` pair in the coordinator's AG-UI output. If you need that visibility, give the specialist its own endpoint instead of delegating to it.
  * **Shared state does not flow back out of a specialist.** A delegation gets a _copy_ of the coordinator's conversation variables, and the specialist's writes to `context.variables` are deliberately not merged back — concurrent delegations would otherwise clobber each other. A specialist that writes state changes nothing the UI sees, and nothing fails. Return the value from the delegation and have the coordinator write it instead. Dependencies are copied in the same way, so `Inject(...)` keeps working inside a specialist.



## Track delegations with `agent.subscribe`#

For a side panel or a progress list, subscribe to the invocation events on the agent from `useAgent`. A run is still running until a finished or error event with its `subagentRunId` arrives, so no separate run record is needed:

components/agent-panel.tsx
    
    
    import type {
      SubagentErrorEvent,
      SubagentFinishedEvent,
      SubagentStartedEvent,
    } from "@ag-ui/client";
    import { useAgent } from "@copilotkit/react-core/v2";
    import { useEffect, useState } from "react";
    
    export function SubagentPanel() {
      const { agent } = useAgent({ agentId: "my_agent" });
      const [started, setStarted] = useState<SubagentStartedEvent[]>([]);
      const [finished, setFinished] = useState<Record<string, SubagentFinishedEvent>>({});
      const [failed, setFailed] = useState<Record<string, SubagentErrorEvent>>({});
    
      useEffect(() => {
        const subscription = agent.subscribe({
          onRunStartedEvent: () => {
            setStarted([]);
            setFinished({});
            setFailed({});
          },
          onSubagentStartedEvent: ({ event }) => setStarted((all) => [...all, event]),
          onSubagentFinishedEvent: ({ event }) =>
            setFinished((all) => ({ ...all, [event.subagentRunId]: event })),
          onSubagentErrorEvent: ({ event }) =>
            setFailed((all) => ({ ...all, [event.subagentRunId]: event })),
        });
        return () => subscription.unsubscribe();
      }, [agent]);
    
      return (
        <ul>
          {started.map((run) => (
            <li key={run.subagentRunId}>
              {run.name}:{" "}
              {failed[run.subagentRunId] ? "failed" : finished[run.subagentRunId] ? "done" : "running…"}
            </li>
          ))}
        </ul>
      );
    }

## Render the delegation in the chat#

Because a delegation is a tool call, rendering it is the ordinary tool-rendering path:

app/page.tsx
    
    
    import { z } from "zod";
    import { useRenderTool } from "@copilotkit/react-core/v2";
    // ...
    
    const YourMainContent = () => {
      // ...
      useRenderTool({
        name: "task_researcher",
        parameters: z.object({
          objective: z.string(),
          context: z.string().optional(),
        }),
        render: ({ status }) => (
          <p className="text-gray-500 mt-2">
            {status !== "complete" && "Researching..."}
            {status === "complete" && "Research done."}
          </p>
        ),
      });
      // ...
    };

A named `useRenderTool` registration needs a `parameters` schema — only the wildcard (`name: "*"`) overload may omit it. Every `as_tool()` delegation takes the same two arguments, `objective` and an optional `context`, so the schema above works for any subagent.

## Choosing between delegation and one agent#

Reach for `as_tool()` when a step needs its own instructions, its own tools, or its own history — a researcher that may make a dozen tool calls should not pollute the coordinator's context. Keep one agent when the work is a single prompt with a couple of tools: delegation costs an extra model round trip per hand-off.

## What's next?#

### [Tool renderingRender each delegation as it happens in the chat.](https://docs.copilotkit.ai/ag2/generative-ui/tool-rendering)### [Shared stateLet the coordinator and your UI read and write the same state.](https://docs.copilotkit.ai/ag2/shared-state)

### On this page

IntroductionBackendWhat reaches the frontendTrack delegations with agent.subscribeRender the delegation in the chatChoosing between delegation and one agentWhat's next?
