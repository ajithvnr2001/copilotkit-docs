---
url: https://docs.copilotkit.ai/google-adk/generative-ui/display/
title: Display components
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:01.765312+00:00
---

# Display components

> Source: https://docs.copilotkit.ai/google-adk/generative-ui/display/

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

[Google ADK](https://docs.copilotkit.ai/google-adk)[Build Generative UI](https://docs.copilotkit.ai/google-adk/generative-ui)

# Display components

Register React components that your agent can render in the chat.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

gen_ui_tool_based_agent.py

page.tsx

route.ts
    
    
    """Agent backing the Tool-Based Generative UI demo.
    
    The frontend registers `render_bar_chart` and `render_pie_chart` tools via
    `useComponent`. The ADKAgent middleware injects those tools into the model
    request at runtime so the agent can call them.
    """
    
    from __future__ import annotations
    
    from google.adk.agents import LlmAgent
    from ag_ui_adk import AGUIToolset
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    _INSTRUCTION = (
        "You are a data visualization assistant.\n\n"
        "When the user asks for a chart, call `render_bar_chart` or "
        "`render_pie_chart` with a concise title, short description, and a "
        "`data` array of `{label, value}` items. Pick bar for comparisons over "
        "a small set of categories; pick pie for composition / share-of-whole.\n\n"
        "If the user names a chart subject but does NOT supply concrete numbers "
        '(e.g. "show me a pie chart of website traffic by source"), do NOT '
        "ask them for data. Invent plausible illustrative sample values "
        "yourself, call the appropriate `render_*` tool immediately, and "
        "briefly note in the follow-up that the values are illustrative "
        "samples. Always render the chart on the first turn -- never reply "
        "with a clarifying question asking for the data.\n\n"
        "Keep chat responses brief -- let the chart do the talking."
    )
    
    gen_ui_tool_based_agent = LlmAgent(
        name="GenUiToolBasedAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )
    

## What is this?#

Render-only generative UI lets you register React components as tools your agent can invoke. When the agent calls the tool, CopilotKit renders your component directly in the chat with the tool's arguments as props; no handler logic or user interaction required.

page.tsxchart.tsx
    
    
    useComponent({
    name: "showChart",
    description: "Populate data and show the user a chart",
    parameters: ChartProps,
    render: Chart
    });
    
    
    
    export const ChartProps = z.object({
      title: z.string(),
      data: z.array(z.object({ label: z.string(), value: z.number() })),
    });
    
    export function Chart({ title, data }: z.infer<typeof ChartProps>) {
      return (
        <div>
          <h3>{title}</h3>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={data}>
              <XAxis dataKey="label" /><YAxis /><Tooltip />
              <Bar dataKey="value" fill="#6366f1" />
            </BarChart>
          </ResponsiveContainer>
        </div>
      );
    }

## When should I use this?#

Use render-only generative UI when you want to:

  * Display rich UI (cards, charts, tables) inline in the chat
  * Show structured data from agent responses
  * Render previews, status indicators, or visual feedback
  * Let the agent present information beyond plain text



## How it works in code#

### Install the ADK + AG-UI bridge
    
    
    pip install ag-ui-adk

### Add `AGUIToolset()` to your agent

`AGUIToolset()` exposes CopilotKit's frontend tools to the model. Add it to your `LlmAgent`'s `tools=` list. Use an ADK-supported model available to your project.

The callback below preserves the Gemini termination safeguard: it stops on final text with a `STOP` finish reason, while leaving partial responses and pending tool calls alone. It is defined here in full, not imported from `ag-ui-adk` or a showcase-only module.
    
    
    from ag_ui_adk import AGUIToolset
    from google.adk.agents import LlmAgent
    from google.adk.agents.callback_context import CallbackContext
    from google.adk.models.llm_response import LlmResponse
    
    
    def stop_on_terminal_text(
        callback_context: CallbackContext, llm_response: LlmResponse
    ) -> None:
        content = llm_response.content
        if llm_response.partial or not content or content.role != "model":
            return
        finish_reason = llm_response.finish_reason
        if getattr(finish_reason, "name", finish_reason) != "STOP":
            return
        parts = content.parts or []
        if not any(part.text for part in parts) or any(part.function_call for part in parts):
            return
        # ADK's invocation context is private; tolerate SDK changes.
        invocation = getattr(callback_context, "_invocation_context", None)
        if invocation is not None:
            try:
                invocation.end_invocation = True
            except AttributeError:
                pass
    
    
    agent = LlmAgent(
        name="assistant",
        model="gemini-3.1-flash-lite",
        instruction="Help the user and call the available frontend tools when appropriate.",
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )

The renderer component receives the tool's arguments as typed props and mounts inline in the chat. Below is the chart renderer wired up in the canonical demo — the agent emits the data, the component draws it.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });
