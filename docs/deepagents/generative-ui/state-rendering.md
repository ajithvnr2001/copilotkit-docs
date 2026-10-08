---
url: https://docs.copilotkit.ai/deepagents/generative-ui/state-rendering/
title: State Rendering
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:00:10.787548+00:00
---

# State Rendering

> Source: https://docs.copilotkit.ai/deepagents/generative-ui/state-rendering/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/deepagents/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/deepagents/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/deepagents/generative-ui/state-rendering)

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

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

## What is this?#

State rendering lets you build UI that reflects your agent's state in real-time. As your agent progresses through nodes and emits state updates, your frontend renders those changes — showing progress, drafts, or intermediate results.

## When should I use this?#

Use state rendering when you want to:

  * Show real-time progress (e.g. "Researching... 2/5 complete")
  * Display drafts that update as the agent works
  * Build dashboards that reflect agent state
  * Render structured output outside of the chat



## Implementation#

### Run and connect your agent#

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Build an agent that produces state#

Define the `searches` state, then add a tool that returns each completed update.

PythonTypeScript

agent.py
    
    
    from typing import Any, TypedDict
    
    from copilotkit import (
        CopilotKitMiddleware,
        CopilotKitState,
        StateItem,
        StateStreamingMiddleware,
    )
    from deepagents import create_deep_agent
    from langchain.agents.middleware import AgentMiddleware
    from langchain.messages import ToolMessage
    from langchain.tools import ToolRuntime, tool
    from langgraph.types import Command
    
    class Search(TypedDict):
        query: str
        done: bool
    
    class AgentState(CopilotKitState):
        searches: list[Search]
    
    class SearchesStateMiddleware(AgentMiddleware[AgentState, Any, Any]):
        state_schema = AgentState
    
    @tool
    def report_research_progress(
        searches: list[Search],
        runtime: ToolRuntime[None, AgentState],
    ) -> Command:
        """Report the current research tasks and completion status."""
        return Command(
            update={
                "searches": searches,
                "messages": [
                    ToolMessage(
                        content="Research progress saved.",
                        tool_call_id=runtime.tool_call_id,
                    )
                ],
            }
        )
    
    agent = create_deep_agent(
        model="openai:gpt-5.4",
        tools=[report_research_progress],
        middleware=[
            SearchesStateMiddleware(),
            CopilotKitMiddleware(),
            StateStreamingMiddleware(
                StateItem(
                    state_key="searches",
                    tool="report_research_progress",
                    tool_argument="searches",
                )
            ),
        ],
        system_prompt=(
            "You are a research assistant. Use report_research_progress "
            "to show each task and mark it done when complete."
        ),
    )

agent.ts
    
    
    import { ToolMessage } from "@langchain/core/messages";
    import { tool, type ToolRuntime } from "@langchain/core/tools";
    import { Command } from "@langchain/langgraph";
    import {
      copilotkitMiddleware,
      zodState,
    } from "@copilotkit/sdk-js/langgraph";
    import {
      stateItem,
      stateStreamingMiddleware,
    } from "@copilotkit/sdk-js/langgraph-middlewares";
    import { createDeepAgent } from "deepagents";
    import { createMiddleware } from "langchain";
    import { z } from "zod";
    
    const SearchSchema = z.object({
      query: z.string(),
      done: z.boolean(),
    });
    type Search = z.infer<typeof SearchSchema>;
    
    const SearchesStateSchema = z.object({
      searches: z.array(SearchSchema),
    });
    
    const searchesStateMiddleware = createMiddleware({
      name: "SearchesState",
      stateSchema: z.object({
        searches: zodState(z.array(SearchSchema).default(() => [])),
      }),
    });
    
    const reportResearchProgress = tool(
      (
        input: { searches: Search[] },
        runtime: ToolRuntime<typeof SearchesStateSchema>,
      ) =>
        new Command({
          update: {
            searches: input.searches,
            messages: [
              new ToolMessage({
                content: "Research progress saved.",
                tool_call_id: runtime.toolCallId,
              }),
            ],
          },
        }),
      {
        name: "report_research_progress",
        description:
          "Report the current research tasks and completion status.",
        schema: z.object({ searches: z.array(SearchSchema) }),
      },
    );
    
    export const agent = createDeepAgent({
      model: "openai:gpt-5.4",
      tools: [reportResearchProgress],
      middleware: [
        searchesStateMiddleware,
        copilotkitMiddleware,
        stateStreamingMiddleware(
          stateItem({
            stateKey: "searches",
            tool: "report_research_progress",
            toolArgument: "searches",
          }),
        ),
      ],
      systemPrompt:
        "You are a research assistant. Use report_research_progress " +
        "to show each task and mark it done when complete.",
    });

### Understand the two update phases#

The state-streaming middleware sends partial `searches` arguments while the model creates them. The frontend can show each partial value immediately.

The tool then returns a `Command` that saves the completed list. Its `ToolMessage` closes the active tool call.

Keep the state key, tool name, and tool argument identical. A mismatch sends updates to the wrong state field.

### Render state in the UI#

Use the `useAgent` hook to access agent state anywhere in your app. You can render it in the chat, in dashboards, sidebars, or custom layouts.

app/page.tsx
    
    
    import { useAgent } from "@copilotkit/react-core/v2"; 
    
    function YourMainContent() {
      const { agent } = useAgent({
        agentId: "sample_agent",
      });
    
      const state = (agent.state ?? {}) as {
        searches?: { query: string; done: boolean }[];
      };
      const searches = state.searches ?? [];
    
      return (
        <div>
          {searches.map((search, index) => (
            <div key={index}>
              {search.done ? "✅" : "⏳"} {search.query}
            </div>
          ))}
        </div>
      );
    }

### Give it a try!#

Ask the agent to research a topic. The search items appear and update while the agent works.

### On this page

What is this?When should I use this?Implementation
