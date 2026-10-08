---
url: https://docs.copilotkit.ai/claude-sdk-python/frontend-tools/
title: Frontend Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:18.558307+00:00
---

# Frontend Tools

> Source: https://docs.copilotkit.ai/claude-sdk-python/frontend-tools/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-python/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-python/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Frontend-tools

Basics

# Frontend Tools

Let your agent interact with and update your application's UI.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

frontend_tools.py

page.tsx

route.ts
    
    
    """Claude Agent SDK backing the Frontend Tools demo.The demo illustrates `useFrontendTool` with a sync handler. The frontendregisters a `change_background` tool; CopilotKit forwards its schema tothe agent at runtime and the handler executes in the browser.The shared Claude backend in `src/agents/agent.py` already acceptsfrontend-registered tool schemas via AG-UI message forwarding, so thismodule is documentation-only — there is no separate Python graph tomount for this cell. The agent instance served by `agent_server.py`handles the `frontend-tools` agent name via the route.ts registration."""# The demo shares the default Claude agent (see src/agents/agent.py).# This module exists so the manifest's `highlight` paths can point to a# per-demo Python reference, mirroring the langgraph-python layout.SYSTEM_PROMPT_HINT = (    "You are a helpful assistant. The frontend has registered a "    "`change_background` tool via `useFrontendTool`. When the user asks "    "to change the background, call that tool with a CSS-valid background "    "value (prefer gradients).")

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Frontend Tools**. Your tool and its schema are listed.

More detail: [Inspector](https://docs.copilotkit.ai/claude-sdk-python/inspector).

## What is this?#

Frontend tools let your agent define and invoke client-side functions that run entirely in the user's browser. Because the handler executes on the frontend, it has direct access to component state, browser APIs, and any third-party UI library the page already uses. That's how an agent can "reach into" the app: update React state, trigger animations, read `localStorage`, pop a toast, or steer the user's view.

This page covers the "agent drives the UI" shape of frontend tools. The same primitive also powers Generative UI and Human-in-the-loop; see those pages for interaction patterns.

## When should I use this?#

Use frontend tools when your agent needs to:

  * Read or modify React component state
  * Access browser APIs like `localStorage`, `sessionStorage`, or cookies
  * Trigger UI updates, animations, or transitions
  * Show alerts, toasts, or notifications
  * Interact with third-party frontend libraries
  * Perform anything that requires the user's immediate browser context



## How it works in code#

### Forward browser tools to Claude

Frontend tools registered with `useFrontendTool` arrive in the AG-UI run input. This demo's server calls the Anthropic Messages API directly for runs that carry frontend tools, so it converts each AG-UI tool definition into a Messages API tool schema first.

The published `ClaudeAgentAdapter` from `ag_ui_claude_sdk` needs no such conversion. It registers each frontend tool on its own in-process MCP tool server as `mcp__ag_ui__<name>`, allows it, and ends the run when Claude calls it so the browser can execute the tool. Pass the run input to the adapter and frontend tools work with no extra wiring.

agent.py
    
    
    def _build_frontend_tools(input_data: RunAgentInput) -> list[dict[str, Any]]:
        """Extract frontend-defined tools from the AG-UI request.
    
        The CopilotKit runtime forwards frontend tool definitions (registered
        via ``useFrontendTool``, ``useHumanInTheLoop``, etc.) in
        ``input_data.tools``. We convert them to the Anthropic ``tools``
        schema so the LLM can call them. The runtime intercepts the resulting
        tool-call events and routes them to the frontend for resolution.
        """
        out: list[dict[str, Any]] = []
        for t in input_data.tools or []:
            name = getattr(t, "name", None) or (
                t.get("name") if isinstance(t, dict) else None
            )
            description = getattr(t, "description", None) or (
                t.get("description", "") if isinstance(t, dict) else ""
            )
            parameters = getattr(t, "parameters", None) or (
                t.get("parameters", {}) if isinstance(t, dict) else {}
            )
            if not name:
                continue
            out.append(
                {
                    "name": name,
                    "description": description or "",
                    "input_schema": parameters or {"type": "object", "properties": {}},
                }
            )
        return out
    
    

Register a frontend tool with `useFrontendTool`. Give it a name, a Zod schema for parameters, and a handler. The agent can then call it like any other tool and your frontend runs it in the browser.

page.tsx
    
    
    import React, { useState } from "react";import {  CopilotKit,  CopilotSidebar,  useFrontendTool,} from "@copilotkit/react-core/v2";import { z } from "zod";import { Background, DEFAULT_BACKGROUND } from "./background";import { useFrontendToolsSuggestions } from "./suggestions";function Chat() {  const [background, setBackground] = useState<string>(DEFAULT_BACKGROUND);  useFrontendTool({    name: "change_background",    description:      "Change the page background. Accepts any valid CSS background value — colors, linear or radial gradients, etc.",    parameters: z.object({      background: z        .string()        .describe("The CSS background value. Prefer gradients."),    }),    handler: async ({ background }) => {      setBackground(background);      return { status: "success" };    },  });

The handler receives the parsed, type-safe parameters and can do anything the browser can: update state, call an API, touch the DOM. Its return value is sent back to the agent as the tool result so the model can reason about what happened.

page.tsx
    
    
        handler: async ({ background }) => {      setBackground(background);      return { status: "success" };    },

## Registering a list of tools#

`useFrontendTool` registers one tool per call, so it cannot be called in a loop over a list whose length changes between renders. When the set of tools comes from state, from props, or from a backend response, use [`useFrontendTools`](https://docs.copilotkit.ai/reference/hooks/useFrontendTools) instead. It takes an array and runs a single effect over it, so the array can be empty on one render and hold twenty entries on the next.
    
    
    useFrontendTools(
      reports.map((report) => ({
        name: `open_${report.id}`,
        description: `Open the ${report.title} report`,
        handler: async () => navigate(`/reports/${report.id}`),
      })),
      [navigate],
    );

Tools that leave the array are unregistered, tools that join it are registered, and a re-render that produces an equal list does not re-register anything. A description built from your data stays current on its own. The second argument is for values a handler closes over, such as `navigate` above.

### On this page

What is this?When should I use this?How it works in codeRegistering a list of tools
