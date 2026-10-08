---
url: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/mcp-apps/
title: MCP Apps
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:11:18.252646+00:00
---

# MCP Apps

> Source: https://docs.copilotkit.ai/langgraph-typescript/generative-ui/mcp-apps/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

[MCP Apps](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/mcp-apps)[Open Generative UI](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/open-generative-ui)

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/langgraph-typescript/webmcp)

Agent capabilities

LangGraph (TypeScript)

[Sub-agents](https://docs.copilotkit.ai/langgraph-typescript/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/langgraph-typescript/learning)

[User Memories](https://docs.copilotkit.ai/langgraph-typescript/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/langgraph-typescript/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/langgraph-typescript/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/langgraph-typescript/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/langgraph-typescript/intelligence/analytics)[Channels](https://docs.copilotkit.ai/langgraph-typescript/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/langgraph-typescript/telemetry)[Community frameworks](https://docs.copilotkit.ai/langgraph-typescript/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

MCP Apps

Generative UIOpen-ended

# MCP Apps

Render interactive UI components from MCP servers directly in your chat interface.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

mcp-apps.ts

page.tsx

route.ts
    
    
    /** * LangGraph TypeScript agent for the CopilotKit MCP Apps demo. * * This agent has no bespoke tools — the CopilotKit runtime is wired with * `mcpApps: { servers: [...] }` pointing at the public Excalidraw MCP * server (see `src/app/api/copilotkit-mcp-apps/route.ts`). The runtime * auto-applies the MCP Apps middleware which exposes the remote MCP * server's tools to this agent at request time and emits the activity * events that CopilotKit's built-in `MCPAppsActivityRenderer` renders in * the chat as a sandboxed iframe. * * Ported from `src/agents/mcp_apps_agent.py`. * * NOTE: The TS runtime performs MCP tool injection via the A2UI/MCP-Apps * middleware before the graph sees the request. The graph itself doesn't * need bespoke MCP client wiring. */import { RunnableConfig } from "@langchain/core/runnables";import { AIMessage, SystemMessage } from "@langchain/core/messages";import {  MemorySaver,  START,  END,  StateGraph,  Annotation,} from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import { makeChatOpenAI } from "./openai-headers";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";const SYSTEM_PROMPT = `You draw simple diagrams in Excalidraw via the MCP tool.SPEED MATTERS. Produce a correct-enough diagram fast; do not optimizefor polish. Target: one tool call, done in seconds.When the user asks for a diagram:1. Call \`create_view\` ONCE with 3-5 elements total: shapes + arrows +   an optional title text.2. Use straightforward shapes (rectangle, ellipse, diamond) with plain   \`label\` fields (\`{"text": "...", "fontSize": 18}\`) on them.3. Connect with arrows. Endpoints can be element centers or simple   coordinates — you don't need edge anchors / fixedPoint bindings.4. Include ONE \`cameraUpdate\` at the END of the elements array that   frames the whole diagram. Use an approved 4:3 size (600x450 or   800x600). No opening camera needed.5. Reply with ONE short sentence describing what you drew.Every element needs a unique string \`id\` (e.g. \`"b1"\`, \`"a1"\`,\`"title"\`). Standard sizes: rectangles 160x70, ellipses/diamonds120x80, 40-80px gap between shapes.Do NOT:- Call \`read_me\`. You already know the basic shape API.- Make multiple \`create_view\` calls.- Iterate or refine. Ship on the first shot.- Add decorative colors / fills / zone backgrounds unless the user  explicitly asks for them.- Add labels on arrows unless crucial.If the user asks for something specific (colors, more elements,particular layout), follow their lead — but still in ONE call.`;const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,});export type AgentState = typeof AgentStateAnnotation.State;async function chatNode(state: AgentState, config: RunnableConfig) {  // gpt-5-mini for speed — Excalidraw element emission is simple JSON and  // we're biasing hard toward sub-30s generation.  const model = makeChatOpenAI(config, {    temperature: 0,    model: "gpt-5-mini",  });  // The MCP Apps middleware injects MCP tools into state.copilotkit.actions  // alongside any frontend actions, so a single bind picks up everything.  const copilotActions = convertActionsToDynamicStructuredTools(    state.copilotkit?.actions ?? [],  );  const modelWithTools =    copilotActions.length > 0 ? model.bindTools!(copilotActions) : model;  const systemMessage = new SystemMessage({ content: SYSTEM_PROMPT });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    config,  );  return { messages: response };}function shouldContinue({ messages }: AgentState) {  const lastMessage = messages[messages.length - 1] as AIMessage;  // All tool calls are frontend (MCP-injected) actions — never locally  // handled. End the run and let the runtime dispatch them.  return lastMessage.tool_calls?.length ? END : END;}const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNode)  .addEdge(START, "chat_node")  .addConditionalEdges("chat_node", shouldContinue as any);const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

## What is this?#

MCP Apps are MCP servers that expose tools with associated UI resources. When the agent calls one of these tools, CopilotKit automatically fetches the resource and renders the UI component in the chat; no additional frontend code required.

**Free course:** See this pattern built end-to-end in [Build Interactive Agents with Generative UI](https://www.deeplearning.ai/short-courses/build-interactive-agents-with-generative-ui/) — a free DeepLearning.AI short course taught by CopilotKit's CEO covering the full Generative UI spectrum (Controlled, Declarative, and Open-Ended).

Key benefits:

  * **Zero frontend code** — UI components are served by the MCP server
  * **Full interactivity** — components can use HTML, CSS, and JavaScript
  * **Secure sandboxing** — content runs in isolated iframes
  * **Thread persistence** — MCP Apps are stored in conversation history and restored on reconnect



## Wire the runtime to your MCP server(s)#

A single `mcpApps.servers` entry on the runtime is all it takes. The runtime auto-applies the MCP Apps middleware to every registered agent: each time an agent calls a tool backed by an MCP UI resource, the middleware fetches the resource and emits an `activity` event that the built-in `MCPAppsActivityRenderer` renders inline in the chat as a sandboxed iframe.

route.ts
    
    
    // The `mcpApps.servers` config is all you need server-side. The runtime// auto-applies the MCP Apps middleware to every registered agent: on each// MCP tool call it fetches the associated UI resource and emits an// `activity` event that the built-in `MCPAppsActivityRenderer` renders// inline in the chat.const runtime = new CopilotRuntime({  // @ts-ignore -- Published CopilotRuntime agents type wraps Record in  // MaybePromise<NonEmptyRecord<...>> which rejects plain Records; fixed in  // source, pending release.  agents: {    "headless-complete": headlessCompleteAgent,    "mcp-apps": mcpAppsAgent,  },  mcpApps: {    servers: [      {        type: "http",        url: process.env.MCP_SERVER_URL || "https://mcp.excalidraw.com",        // Always pin a stable `serverId`. Without it CopilotKit hashes the        // URL, and a URL change silently breaks restoration of persisted        // MCP Apps in prior conversation threads.        serverId: "excalidraw",      },    ],  },});

Always pin a serverId

In production, always provide a stable `serverId`. Without it, CopilotKit hashes the server URL, and a URL change (for example between environments) silently breaks restoration of MCP Apps persisted in earlier conversation threads.

## No frontend renderer needed#

Unlike custom activity types, the MCP Apps renderer is already registered by `CopilotKit` out of the box. A plain `<CopilotChat />` is enough; no `renderActivityMessages` prop, no manual `useRenderActivityMessage` wiring.

page.tsx
    
    
      // No `renderActivityMessages`, no `useRenderActivityMessage` — the  // CopilotKitProvider auto-registers the built-in `MCPAppsActivityRenderer`  // for the "mcp-apps" activity type. A plain <CopilotChat /> is enough.  return (    <CopilotKit runtimeUrl="/api/copilotkit-mcp-apps" agent="mcp-apps">      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );

## Transport types#

The middleware supports two transport types:

### HTTP#

Use this format to connect to an MCP server that accepts standard HTTP requests:
    
    
    {
      type: "http",
      url: "http://localhost:3101/mcp",
      serverId: "my-http-server"
    }

### SSE#

Use this format to connect to an MCP server that streams events over a persistent connection:
    
    
    {
      type: "sse",
      url: "https://mcp.example.com/sse",
      headers: {
        "Authorization": "Bearer token"
      },
      serverId: "my-sse-server"
    }

## Example MCP servers#

Try these open-source MCP Apps servers to get started:

  * [Excalidraw](https://mcp.excalidraw.com) — collaborative whiteboard rendered in-chat
  * [modelcontextprotocol/ext-apps](https://github.com/modelcontextprotocol/ext-apps) — canonical reference implementations



### On this page

What is this?Wire the runtime to your MCP server(s)No frontend renderer neededTransport typesHTTPSSEExample MCP servers
