---
url: https://docs.copilotkit.ai/claude-sdk-typescript/tutorials/multi-conversation-chat/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:55:44.602892+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/claude-sdk-typescript/tutorials/multi-conversation-chat/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendClaude Agent SDK (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/claude-sdk-typescript)[Quickstart](https://docs.copilotkit.ai/claude-sdk-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/claude-sdk-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/claude-sdk-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/claude-sdk-typescript/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/claude-sdk-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/claude-sdk-typescript/learning)

[User Memories](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/claude-sdk-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/claude-sdk-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/claude-sdk-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# Quickstart

Run a Claude Agent SDK TypeScript agent behind CopilotKit.

## Start with your coding agent#

Use this prompt to connect your Claude Agent SDK for TypeScript agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

This quickstart gives you two working paths:

  * **Start from scratch** to scaffold the full Claude Agent SDK TypeScript showcase.
  * **Use an existing agent** to expose your own Claude Agent SDK process over AG-UI and connect it to a React app.



## Prerequisites#

Before you begin, you'll need the following:

  * An Anthropic API key
  * Node.js 20+
  * Your favorite package manager



## Getting started#

### Choose your starting point#

### Verify the integration#

Open `http://localhost:3000` and ask:
    
    
    Tell me in one sentence what this app can do.

If the chat streams a Claude response, CopilotKit is connected to your Claude Agent SDK TypeScript agent.

Troubleshooting

  * If the runtime cannot reach the agent, check that the agent server is running on `http://localhost:8000` or set `AGENT_URL` in the frontend.
  * If Claude returns an authentication error, make sure `ANTHROPIC_API_KEY` is available to the agent server process.
  * If a custom tool call stalls, add the backend tool bridge shown below instead of leaving `tools: []`.



### Open Inspector and confirm setup#

On localhost, click the Inspector button in the corner of the app.

  1. Open **Agents** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Agents** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with Enable Intelligence (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/claude-sdk-typescript/inspector).

## Backend tools and state#

The minimal server above is enough for text chat. To support backend tools, shared state snapshots, and richer demos, expose your tool schemas through the Claude SDK MCP bridge and emit AG-UI state events:

### Install the Claude Agent SDK packages
    
    
    npm install @ag-ui/core @ag-ui/encoder @ag-ui/claude-agent-sdk @anthropic-ai/claude-agent-sdk@^0.2.58 @anthropic-ai/sdk zod

### Bridge Claude Agent SDK to AG-UI

Use `ClaudeAgentAdapter` from `@ag-ui/claude-agent-sdk`. The adapter receives the AG-UI run input, emits AG-UI events back to CopilotKit, and can expose backend tools through an in-process Claude SDK MCP server.

claude-agent-sdk-adapter.ts
    
    
    function createClaudeAgentAdapter({
      toolSchemas,
      emit,
      getState,
      setState,
      executeTool,
      model,
      systemPrompt,
    }: {
      toolSchemas: Anthropic.Tool[];
      emit: Emit;
      getState: () => Record<string, unknown>;
      setState: (state: Record<string, unknown>) => void;
      executeTool: ExecuteTool;
      model: string;
      systemPrompt: string;
    }) {
      const backendToolServer = buildBackendToolServer({
        toolSchemas,
        emit,
        getState,
        setState,
        executeTool,
      });
    
      return new ClaudeAgentAdapter({
        agentId: "claude-sdk-typescript",
        model: normalizeClaudeAgentSdkModel(model),
        systemPrompt,
        tools: [],
        mcpServers: backendToolServer.mcpServers,
        allowedTools: backendToolServer.allowedTools,
        permissionMode: "dontAsk",
        maxTurns: 10,
      });
    }

claude-agent-sdk-adapter.ts
    
    
    export async function runWithClaudeAgentSdk({
      input,
      emit,
      runId,
      threadId,
      systemPrompt,
      toolSchemas,
      initialState,
      model,
      executeTool,
      forwardedHeaders,
    }: {
      input: RunAgentInput;
      emit: Emit;
      runId: string;
      threadId: string;
      systemPrompt: string;
      toolSchemas: Anthropic.Tool[];
      initialState: Record<string, unknown>;
      model: string;
      executeTool: ExecuteTool;
      forwardedHeaders?: Record<string, string>;
    }): Promise<void> {
      let state = { ...initialState };
      const pendingStateSnapshots: Record<string, unknown>[] = [];
      const adapter = createClaudeAgentAdapter({
        toolSchemas,
        emit,
        getState: () => state,
        setState: (nextState) => {
          state = nextState;
          pendingStateSnapshots.push(state);
        },
        executeTool,
        systemPrompt,
        model,
      });
    
      if (forwardedHeaders && Object.keys(forwardedHeaders).length > 0) {
        adapter.headers = forwardedHeaders;
      }
    
      const runInput: RunAgentInput = {
        ...input,
        runId,
        threadId,
        state: input.state ?? initialState,
      };
    
      await new Promise<void>((resolve) => {
        adapter.run(runInput).subscribe({
          next: (event) => {
            if (event.type === EventType.TOOL_CALL_RESULT) {
              const snapshot = pendingStateSnapshots.shift();
              if (snapshot) {
                emit({ type: EventType.STATE_SNAPSHOT, snapshot });
              }
            }
            emit(event);
          },
          error: (error) => {
            const message =
              error instanceof Error ? error.stack || error.message : String(error);
            emit({ type: EventType.RUN_ERROR, runId, threadId, message });
            resolve();
          },
          complete: () => resolve(),
        });
      });
    }
