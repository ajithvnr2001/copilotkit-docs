---
url: https://docs.copilotkit.ai/langgraph-typescript/voice/
title: Voice
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:13:51.627213+00:00
---

# Voice

> Source: https://docs.copilotkit.ai/langgraph-typescript/voice/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (TypeScript)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-typescript)[Quickstart](https://docs.copilotkit.ai/langgraph-typescript/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-typescript/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-typescript/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/langgraph-typescript/multimodal-attachments)[Voice](https://docs.copilotkit.ai/langgraph-typescript/voice)[Reasoning](https://docs.copilotkit.ai/langgraph-typescript/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-typescript/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

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

Voice

BasicsChat

# Voice

Real-time speech-to-text in the chat composer. The user speaks, the runtime transcribes, the agent runs the resulting prompt.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

graph.ts

page.tsx

sample-audio-button.tsx

route.ts
    
    
    /** * LangGraph TypeScript agent — CopilotKit showcase integration * * Defines a graph with a chat node and all showcase tools, * wired to CopilotKit via the sdk-js LangGraph adapter so frontend actions * and shared state flow seamlessly. */import { z } from "zod";import type { RunnableConfig } from "@langchain/core/runnables";import { tool } from "@langchain/core/tools";import { ToolNode } from "@langchain/langgraph/prebuilt";import type { AIMessage } from "@langchain/core/messages";import { SystemMessage } from "@langchain/core/messages";import {  MemorySaver,  START,  StateGraph,  Annotation,} from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import { getA2UITools } from "@ag-ui/langgraph";import { makeChatOpenAI } from "./openai-headers";import {  convertActionsToDynamicStructuredTools,  CopilotKitStateAnnotation,} from "@copilotkit/sdk-js/langgraph";import {  getWeatherImpl,  queryDataImpl,  manageSalesTodosImpl,  getSalesTodosImpl,  scheduleMeetingImpl,  searchFlightsImpl,} from "../../shared-tools";// ---------------------------------------------------------------------------// 1. Agent state — extends CopilotKit state with a proverbs list// ---------------------------------------------------------------------------const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,  proverbs: Annotation<string[]>,});export type AgentState = typeof AgentStateAnnotation.State;// ---------------------------------------------------------------------------// 2. Tools — shared implementations wrapped for LangChain// ---------------------------------------------------------------------------const getWeather = tool(  async ({ location }) => JSON.stringify(getWeatherImpl(location)),  {    name: "get_weather",    description: "Get current weather for a location",    schema: z.object({      location: z.string().describe("City name"),    }),  },);const queryData = tool(  async ({ query }) => JSON.stringify(queryDataImpl(query)),  {    name: "query_data",    description: "Query financial database for chart data",    schema: z.object({      query: z.string().describe("Natural language query"),    }),  },);const manageSalesTodos = tool(  async ({ todos }) => JSON.stringify(manageSalesTodosImpl(todos)),  {    name: "manage_sales_todos",    description: "Create or update the sales todo list",    schema: z.object({      todos: z        .array(          z.object({            id: z.string().optional(),            title: z.string(),            stage: z.string().optional(),            value: z.number().optional(),            dueDate: z.string().optional(),            assignee: z.string().optional(),            completed: z.boolean().optional(),          }),        )        .describe("Array of sales todo items"),    }),  },);const getSalesTodos = tool(  async ({ currentTodos }) => JSON.stringify(getSalesTodosImpl(currentTodos)),  {    name: "get_sales_todos",    description: "Get the current sales todo list",    schema: z.object({      currentTodos: z        .array(          z.object({            id: z.string().optional(),            title: z.string().optional(),            stage: z.string().optional(),            value: z.number().optional(),            dueDate: z.string().optional(),            assignee: z.string().optional(),            completed: z.boolean().optional(),          }),        )        .optional()        .nullable()        .describe("Current todos if any"),    }),  },);const scheduleMeeting = tool(  async ({ reason, durationMinutes }) =>    JSON.stringify(scheduleMeetingImpl(reason, durationMinutes)),  {    name: "schedule_meeting",    description: "Schedule a meeting (requires user approval via HITL)",    schema: z.object({      reason: z.string().describe("Reason for the meeting"),      durationMinutes: z.number().optional().describe("Duration in minutes"),    }),  },);const searchFlights = tool(  async ({ flights }) => JSON.stringify(searchFlightsImpl(flights)),  {    name: "search_flights",    description: "Search for available flights",    schema: z.object({      flights: z        .array(          z.object({            airline: z.string(),            airlineLogo: z.string().optional(),            flightNumber: z.string(),            origin: z.string(),            destination: z.string(),            date: z.string(),            departureTime: z.string(),            arrivalTime: z.string(),            duration: z.string(),            status: z.string(),            statusColor: z.string().optional(),            price: z.string(),            currency: z.string().optional(),          }),        )        .describe("Array of flight results"),    }),  },);// Dynamic A2UI via the canonical ag-ui factory (same as beautiful_chat /// a2ui_dynamic). A secondary LLM designs the surface; the factory forces the// host catalog and emits the a2ui_operations envelope. Replaces the prior// hand-rolled generate_a2ui tool.const generateA2ui = getA2UITools({  model: new ChatOpenAI({ model: "gpt-5-mini" }),  defaultCatalogId: "copilotkit://app-dashboard-catalog",});const tools = [  getWeather,  queryData,  manageSalesTodos,  getSalesTodos,  scheduleMeeting,  searchFlights,  generateA2ui,];// ---------------------------------------------------------------------------// 3. Chat node — binds backend + frontend tools, invokes the model// ---------------------------------------------------------------------------async function chatNode(state: AgentState, config: RunnableConfig) {  const model = makeChatOpenAI(config, { model: "gpt-5-mini" });  const modelWithTools = model.bindTools!([    ...convertActionsToDynamicStructuredTools(state.copilotkit?.actions ?? []),    ...tools,  ]);  const systemMessage = new SystemMessage({    content: `You are a helpful assistant. The current proverbs are ${JSON.stringify(state.proverbs)}.`,  });  const response = await modelWithTools.invoke(    [systemMessage, ...state.messages],    config,  );  return { messages: response };}// ---------------------------------------------------------------------------// 4. Routing — send tool calls to tool_node unless they're CopilotKit actions// ---------------------------------------------------------------------------function shouldContinue({ messages, copilotkit }: AgentState) {  const lastMessage = messages[messages.length - 1] as AIMessage;  if (lastMessage.tool_calls?.length) {    const actions = copilotkit?.actions;    const toolCallName = lastMessage.tool_calls![0].name;    if (!actions || actions.every((action) => action.name !== toolCallName)) {      return "tool_node";    }  }  return "__end__";}// ---------------------------------------------------------------------------// 5. Compile the graph// ---------------------------------------------------------------------------const workflow = new StateGraph(AgentStateAnnotation)  .addNode("chat_node", chatNode)  .addNode("tool_node", new ToolNode(tools))  .addEdge(START, "chat_node")  .addEdge("tool_node", "chat_node")  .addConditionalEdges("chat_node", shouldContinue as any);const memory = new MemorySaver();export const graph = workflow.compile({  checkpointer: memory,});

You have a working chat surface and you want users to be able to speak instead of type. By the end of this guide, the chat composer will sprout a mic button, recorded audio will be transcribed by the runtime, and the transcript will auto-send to the agent like any other message.

## When to use this#

  * **Hands-free or accessibility flows** where typing isn't the right input modality.
  * **Mobile or kiosk surfaces** where a long voice query is faster than thumb-typing.
  * **Demo and test loops** where you want canned audio to drive the chat without a microphone.



If you only need file uploads (audio, images, video, documents), use [Multimodal Attachments](https://docs.copilotkit.ai/langgraph-typescript/multimodal-attachments) instead. Voice is specifically about live transcription of recorded speech into chat input.

## Frontend#

`<CopilotChat />` from `@copilotkit/react-core/v2` renders the mic button automatically when the runtime advertises `audioFileTranscriptionEnabled: true` on its `/info` endpoint. There's nothing to wire up on the chat surface itself:

page.tsx
    
    
    import { CopilotKit } from "@copilotkit/react-core/v2";import { VoiceChat } from "./voice-chat";export default function VoiceDemoPage() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit-voice"      agent="voice-demo"      useSingleEndpoint={false}      // The dev-only `<cpk-web-inspector>` overlay (auto-enabled on      // localhost via shouldShowDevConsole) intercepts pointer events      // on top of the voice sample-audio button, so dev/D5 probe runs      // can't click it through Playwright. Production isn't localhost      // so the inspector never mounts there — voice is D5 in prod and      // D4 locally for this reason alone. Disable explicitly here so      // the demo behaves the same in both environments.      enableInspector={false}    >      <VoiceChat />    </CopilotKit>  );}

The `runtimeUrl="/api/copilotkit-voice"` points the browser to your Next.js API route. When the user clicks the mic, the chat captures audio, POSTs it to that runtime route's `/transcribe` endpoint, drops the resulting transcript into the composer, and submits.

### Driving the demo without a mic#

For Playwright runs, screenshots, or any flow where prompting for mic permissions is awkward, ship a button that emits a canned sample phrase through an `onTranscribed` callback, bypassing the transcription endpoint entirely:

sample-audio-button.tsx
    
    
    export function SampleAudioButton({  onTranscribed,  sampleText,}: SampleAudioButtonProps) {  return (    <button      type="button"      data-testid="voice-sample-audio-button"      onClick={() => onTranscribed(sampleText)}      title={`Inserts: "${sampleText}"`}      className="inline-flex w-fit items-center gap-2 rounded-md border border-black/10 bg-white px-3 py-1.5 text-xs font-medium hover:bg-black/5 dark:border-white/10 dark:bg-black/30 dark:hover:bg-white/10"    >      <span aria-hidden>🎙</span>      <span>Try a sample audio</span>    </button>  );}

The parent chat component can then drop that text into the composer's textarea (matched via `data-testid="copilot-chat-textarea"`) using the native value setter and a synthetic `input` event so React's managed state updates correctly.

## Backend#

### Next.js API route#

Create a dedicated API route at `app/api/copilotkit-voice/[[...slug]]/route.ts`. The `[[...slug]]` catch-all pattern lets the V2 runtime handle its internal URL routing (`/info`, `/agent/:id/run`, `/transcribe`, etc.) under the `/api/copilotkit-voice` base path.

Wire up the V2 runtime with a `TranscriptionService`. The V1 wrapper drops the `transcriptionService` option, so use `createCopilotRuntimeHandler` from `@copilotkit/runtime/v2` directly:

route.ts
    
    
    import type { NextRequest } from "next/server";import {  CopilotRuntime,  TranscriptionService,  createCopilotRuntimeHandler,} from "@copilotkit/runtime/v2";import type { TranscribeFileOptions } from "@copilotkit/runtime/v2";import { LangGraphAgent } from "@copilotkit/runtime/langgraph";import { TranscriptionServiceOpenAI } from "@copilotkit/voice";import OpenAI from "openai";const LANGGRAPH_URL =  process.env.AGENT_URL ||  process.env.LANGGRAPH_DEPLOYMENT_URL ||  "http://localhost:8123";const voiceDemoAgent = new LangGraphAgent({  deploymentUrl: `${LANGGRAPH_URL}/`,  graphId: "starterAgent",});/** * Transcription service wrapper that reports a clean, typed auth error when * OPENAI_API_KEY is not configured. When the key is present we delegate to * the real OpenAI-backed service; any upstream Whisper error keeps its * natural categorization. */class GuardedOpenAITranscriptionService extends TranscriptionService {  private delegate: TranscriptionServiceOpenAI | null;  constructor() {    super();    const apiKey = process.env.OPENAI_API_KEY;    this.delegate = apiKey      ? new TranscriptionServiceOpenAI({ openai: new OpenAI({ apiKey }) })      : null;  }  async transcribeFile(options: TranscribeFileOptions): Promise<string> {    if (!this.delegate) {      // "api key" substring → handleTranscribe maps to AUTH_FAILED → 401.      throw new Error(        "OPENAI_API_KEY not configured for this deployment (api key missing). " +          "Set OPENAI_API_KEY to enable voice transcription.",      );    }    return this.delegate.transcribeFile(options);  }}// Cache the runtime + handler across invocations so the transcription service// is constructed once per Node process instead of per request. The guarded// service reads OPENAI_API_KEY lazily in its transcribeFile call path, so// deferring construction past module load is not required for cold-start// safety under missing-key conditions.let cachedHandler: ((req: Request) => Promise<Response>) | null = null;function getHandler(): (req: Request) => Promise<Response> {  if (cachedHandler) return cachedHandler;  const runtime = new CopilotRuntime({    // @ts-ignore -- Published CopilotRuntime agents type wraps Record in    // MaybePromise<NonEmptyRecord<...>> which rejects plain Records; fixed in    // source, pending release.    agents: {      // The page mounts <CopilotKit agent="voice-demo">; resolve that to      // the neutral sample_agent graph.      "voice-demo": voiceDemoAgent,      // useAgent() with no args defaults to "default"; alias so any internal      // default-agent lookups resolve against the same graph.      default: voiceDemoAgent,    },    transcriptionService: new GuardedOpenAITranscriptionService(),  });  cachedHandler = createCopilotRuntimeHandler({    runtime,    basePath: "/api/copilotkit-voice",  });  return cachedHandler;}// Next.js App Router bindings. This file lives at// `src/app/api/copilotkit-voice/[[...slug]]/route.ts` — the catchall slug// pattern forwards every sub-path (`/info`, `/agent/:id/run`,// `/transcribe`, ...) to the V2 handler so its URL router can dispatch.export const POST = (req: NextRequest) => getHandler()(req);export const GET = (req: NextRequest) => getHandler()(req);export const PUT = (req: NextRequest) => getHandler()(req);export const DELETE = (req: NextRequest) => getHandler()(req);

The `basePath: "/api/copilotkit-voice"` in `createCopilotRuntimeHandler` must match the API route's directory path. With `transcriptionService` set, the runtime advertises `audioFileTranscriptionEnabled: true` on `/info` (which is what tells the chat to render the mic button) and routes `POST /transcribe` to the service.

Without a service, `/transcribe` answers 503

A runtime with no `transcriptionService` still serves the route, and answers every request `503` with `{ "error": "service_not_configured" }`. The mic button never appears, so the symptom is a chat with no voice input rather than a visible server error — check `/info` for `audioFileTranscriptionEnabled` when voice silently doesn't show up.

Calling `/transcribe` yourself

The chat handles this for you; these are the rules if you post to the route directly. As multipart, the audio field must be named `audio` — any other name reads as absent and the route answers `invalid_request`. As JSON, `mimeType` is required alongside the base64 `audio`, and a payload without it is rejected the same way.

### Custom transcription backends#

`TranscriptionService` from `@copilotkit/runtime/v2` is an abstract class. Subclass it to plug in any transcription provider — Whisper, AssemblyAI, Deepgram, your own model. The library ships `TranscriptionServiceOpenAI` as the canonical reference implementation.

Return a string, and let provider errors through

`transcribe` returns the transcript as a string — the handler wraps it into `{ transcription }` itself, so returning a richer object is a type error.

Let the provider's own errors propagate unchanged. The runtime classifies failures by reading the error text for markers like `rate`, `429`, `auth` and `too long`, so a provider message such as `OpenAI returned 429 rate limited` maps to the right error code on its own. Replacing it with your own wording bypasses that and everything lands as a generic provider error.

A useful pattern is constructing the service only when its dedicated credential is configured. Without it, omit `transcriptionService`; the runtime reports the capability as disabled, hides the mic, and returns the documented 503 if `/transcribe` is called directly:

route.ts
    
    
    import type { NextRequest } from "next/server";import {  CopilotRuntime,  TranscriptionService,  createCopilotRuntimeHandler,} from "@copilotkit/runtime/v2";import type { TranscribeFileOptions } from "@copilotkit/runtime/v2";import { LangGraphAgent } from "@copilotkit/runtime/langgraph";import { TranscriptionServiceOpenAI } from "@copilotkit/voice";import OpenAI from "openai";const LANGGRAPH_URL =  process.env.AGENT_URL ||  process.env.LANGGRAPH_DEPLOYMENT_URL ||  "http://localhost:8123";const voiceDemoAgent = new LangGraphAgent({  deploymentUrl: `${LANGGRAPH_URL}/`,  graphId: "starterAgent",});/** * Transcription service wrapper that reports a clean, typed auth error when * OPENAI_API_KEY is not configured. When the key is present we delegate to * the real OpenAI-backed service; any upstream Whisper error keeps its * natural categorization. */class GuardedOpenAITranscriptionService extends TranscriptionService {  private delegate: TranscriptionServiceOpenAI | null;  constructor() {    super();    const apiKey = process.env.OPENAI_API_KEY;    this.delegate = apiKey      ? new TranscriptionServiceOpenAI({ openai: new OpenAI({ apiKey }) })      : null;  }  async transcribeFile(options: TranscribeFileOptions): Promise<string> {    if (!this.delegate) {      // "api key" substring → handleTranscribe maps to AUTH_FAILED → 401.      throw new Error(        "OPENAI_API_KEY not configured for this deployment (api key missing). " +          "Set OPENAI_API_KEY to enable voice transcription.",      );    }    return this.delegate.transcribeFile(options);  }}

### On this page

When to use thisFrontendDriving the demo without a micBackendNext.js API routeCustom transcription backends
