---
url: https://docs.copilotkit.ai/angular/claude-sdk-python/quickstart/
title: Angular quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:48:55.082926+00:00
---

# Angular quickstart

> Source: https://docs.copilotkit.ai/angular/claude-sdk-python/quickstart/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendClaude Agent SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular/claude-sdk-python)[Quickstart](https://docs.copilotkit.ai/angular/claude-sdk-python/quickstart)[Build with agents](https://docs.copilotkit.ai/angular/claude-sdk-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/claude-sdk-python/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/claude-sdk-python/webmcp)

Agent capabilities

Angular Guides

[Sub-agents](https://docs.copilotkit.ai/angular/claude-sdk-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/claude-sdk-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/claude-sdk-python/learning)

[User Memories](https://docs.copilotkit.ai/angular/claude-sdk-python/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/claude-sdk-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/claude-sdk-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/claude-sdk-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/claude-sdk-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/claude-sdk-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/claude-sdk-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# Angular

Connect an Angular app to Copilot Runtime with CopilotKit.

`@copilotkit/angular` provides Angular components, directives, and services for CopilotKit. This guide gets you to a working Angular app with a chat UI backed by [Copilot Runtime](https://docs.copilotkit.ai/angular/claude-sdk-python/backend/copilot-runtime). When you select an agent backend in the sidebar, the backend step below changes with it; without a selection, the guide uses CopilotKit's `BuiltInAgent`.

The runtime runs on your server, keeps model credentials out of the browser, and exposes the `default` agent that `CopilotChat` uses automatically.

[Take your Angular copilot from local to productionAdd threads, inspection, and cloud-hosted or self-hosted CopilotKit Intelligence without changing the Angular frontend APIs in this guide.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs%3Aangular%2Fquickstart%3Aproduction&utm_frontend=angular&utm_backend=claude-sdk-python)

## Start with your coding agent#

Use this prompt to connect your Angular app to Copilot Runtime with the selected agent backend, then verify a working conversation. You can also follow the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is CopilotKit for Angular?#

CopilotKit for Angular is the first-party, signal-based Angular frontend for AG-UI agents and Copilot Runtime. It provides complete chat surfaces and headless APIs, and it supports zoneless applications.

## Prerequisites#

  * An OpenAI API key (or another model provider supported by [Model Selection](https://docs.copilotkit.ai/angular/model-selection))
  * Angular 22
  * Node.js 22



## Getting started#

### Create your Angular app#

If you don't have one already, pin the CLI to the supported major:
    
    
    npx @angular/cli@22 new my-copilot-app
    cd my-copilot-app

### Install CopilotKit#

Install the Angular frontend package, `@angular/cdk`, and `@copilotkit/runtime` for your local Copilot Runtime server:

npmpnpmyarn
    
    
    npm install @copilotkit/angular @angular/cdk @copilotkit/runtime
    npm install -D tsx typescript @types/node
    
    
    pnpm add @copilotkit/angular @angular/cdk @copilotkit/runtime
    pnpm add -D tsx typescript @types/node
    
    
    yarn add @copilotkit/angular @angular/cdk @copilotkit/runtime
    yarn add -D tsx typescript @types/node

Match @angular/cdk to your Angular version

`@angular/cdk` must share your Angular major version. Most package managers resolve this for you, but if you hit a peer-dependency error, pin it explicitly (for example `@angular/cdk@^22`).

### Connect the selected agent backend#

This URL keeps the agent backend selected. The Angular setup remains shared; the backend setup below comes from that integration's canonical showcase source.

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
    
    

Expose the selected backend through Copilot Runtime

Configure Copilot Runtime to register this backend as the `default` agent at `/api/copilotkit`. Continue with the selected backend's [Copilot Runtime guide](https://docs.copilotkit.ai/angular/claude-sdk-python/quickstart/backend/copilot-runtime) for its runtime adapter, credentials, and server command. Do not replace it with the `BuiltInAgent` server from the standalone Angular path.

### Import the styles#

Add the package stylesheet to your global styles. It's self-contained, so the chat renders without any other CSS.

src/styles.css
    
    
    @import "@copilotkit/angular/styles.css"; 

### Connect to Copilot Runtime#

Point `provideCopilotKit` at the runtime endpoint. The chat uses the agent that your runtime registers as `default`.

src/app/app.config.ts
    
    
    import { ApplicationConfig } from "@angular/core";
    import { provideCopilotKit } from "@copilotkit/angular"; 
    
    export const appConfig: ApplicationConfig = {
      providers: [
        provideCopilotKit({
          runtimeUrl: "http://localhost:8200/api/copilotkit",
        }),
      ],
    };

### Add the chat UI#

Import the `CopilotChat` component into your root component and drop it into the template.

src/app/app.ts
    
    
    import { Component } from "@angular/core";
    import { CopilotChat } from "@copilotkit/angular"; 
    
    @Component({
      selector: "app-root",
      imports: [CopilotChat], 
      template: `
        <div style="height: 100vh">
          <copilot-chat />
        </div>
      `,
    })
    export class App {}

### Run the backend, runtime, and Angular app#

Start the selected agent backend and Copilot Runtime with the commands from its runtime guide. Confirm `http://localhost:8200/api/copilotkit/info` reports the `default` agent, then start Angular:
    
    
    npm start

Open the Angular CLI URL (usually `http://localhost:4200`) and send a message. The request now follows the selected path end to end: Angular → Copilot Runtime → your selected agent backend.

### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/angular/claude-sdk-python/inspector).

## Next steps#

  * [Runtime and backend docs](https://docs.copilotkit.ai/angular/claude-sdk-python/quickstart/backend/copilot-runtime): configure the server, secure requests, and deploy without leaving the selected Angular surface.
  * [CopilotKit Intelligence](https://docs.copilotkit.ai/angular/claude-sdk-python/quickstart/intelligence/overview): add threads, inspection, and cloud-hosted or self-hosted operations.
  * [Angular task guides](https://docs.copilotkit.ai/angular/claude-sdk-python/quickstart/guides/chat-ui): build chat UI, tools, generative UI, interrupts, shared state, threads, memory, attachments, and headless UI.
  * [Angular feature examples](https://docs.copilotkit.ai/angular/claude-sdk-python/quickstart/features): find runnable examples and canonical shared Angular source for each supported feature.
  * [Angular API reference](https://docs.copilotkit.ai/reference/angular): use components, signals, tools, context, and runtime services.
  * [Production and lifecycle](https://docs.copilotkit.ai/reference/angular/production-lifecycle): handle cleanup, errors, server rendering, hydration, zoneless Angular, and browser-only features.


