---
url: https://docs.copilotkit.ai/claude-sdk-python/tutorials/ai-powered-textarea/step-3-copilot-textarea/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:59.893780+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/claude-sdk-python/tutorials/ai-powered-textarea/step-3-copilot-textarea/

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

# Quickstart

Run a Claude Agent SDK Python agent behind CopilotKit.

## Start with your coding agent#

Use this prompt to connect your Claude Agent SDK for Python agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This quickstart gives you two working paths:

  * **Start from scratch** to scaffold the full Claude Agent SDK Python showcase.
  * **Use an existing agent** to expose your own Claude Agent SDK process over AG-UI and connect it to a React app.



## Prerequisites#

Before you begin, you'll need the following:

  * An Anthropic API key
  * Python 3.11+
  * Node.js 20+
  * `uv` for Python dependency management
  * Your favorite JavaScript package manager



## Getting started#

### Choose your starting point#

### Verify the integration#

Open `http://localhost:3000` and ask:
    
    
    Tell me in one sentence what this app can do.

If the chat streams a Claude response, CopilotKit is connected to your Claude Agent SDK Python agent.

Troubleshooting

  * If the runtime cannot reach the agent, check that the FastAPI server is running on `http://localhost:8000` or set `AGENT_URL` in the frontend.
  * If Claude returns an authentication error, make sure `ANTHROPIC_API_KEY` is available to the Python process.
  * If a custom tool call stalls, add the backend tool bridge shown below instead of leaving `"tools": []`.



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/claude-sdk-python/inspector).

## Backend tools and state#

The minimal server above is enough for text chat. To support backend tools, shared state snapshots, and richer demos, expose your tool schemas through the Claude SDK MCP bridge and emit AG-UI state events:

### Install the Claude Agent SDK packages
    
    
    uv add claude-agent-sdk ag-ui-claude-sdk ag-ui-protocol anthropic fastapi uvicorn python-dotenv

### Bridge Claude Agent SDK to AG-UI

Use `ClaudeAgentAdapter` from `ag_ui_claude_sdk`. The adapter receives the AG-UI run input, emits AG-UI events back to CopilotKit, and can expose backend tools through an in-process Claude SDK MCP server.

claude_agent_sdk_adapter.py
    
    
    async def run_with_claude_agent_sdk(
        input_data: RunAgentInput,
        *,
        system_prompt: str,
        tools: list[dict[str, Any]],
        state: Any,
        model: str,
        execute_tool: ExecuteTool,
        max_turns: int = 10,
    ) -> AsyncIterator[str]:
        """Run through the official AG-UI Claude adapter and emit SSE chunks."""
    
        encoder = EventEncoder()
        state_box = {"state": state}
        pending_state_snapshots: list[Any] = []
        sdk_tools = _build_sdk_tools(
            tools,
            execute_tool=execute_tool,
            get_state=lambda: state_box["state"],
            set_state=lambda next_state: _set_state(
                next_state,
                state_box,
                pending_state_snapshots,
            ),
        )
    
        options: dict[str, Any] = {
            "model": _normalize_claude_agent_sdk_model(model),
            "system_prompt": system_prompt,
            "tools": [],
            "permission_mode": "dontAsk",
            "max_turns": max_turns,
        }
    
        if sdk_tools:
            options["mcp_servers"] = {
                COPILOTKIT_MCP_SERVER_NAME: create_sdk_mcp_server(
                    COPILOTKIT_MCP_SERVER_NAME,
                    "1.0.0",
                    tools=sdk_tools,
                )
            }
            options["allowed_tools"] = [
                f"{COPILOTKIT_TOOL_PREFIX}{schema['name']}" for schema in tools
            ]
    
        adapter = ClaudeAgentAdapter(
            name="claude-sdk-python",
            options=options,
        )
        run_input = _with_initial_state(input_data, state)
    
        async for event in adapter.run(run_input):
            if event.type == EventType.TOOL_CALL_RESULT and pending_state_snapshots:
                yield encoder.encode(
                    StateSnapshotEvent(
                        type=EventType.STATE_SNAPSHOT,
                        snapshot=pending_state_snapshots.pop(0),
                    )
                )
            yield encoder.encode(event)
    
    
