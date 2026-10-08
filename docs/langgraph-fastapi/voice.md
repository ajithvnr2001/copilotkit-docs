---
url: https://docs.copilotkit.ai/langgraph-fastapi/voice/
title: Voice
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:06:50.939978+00:00
---

# Voice

> Source: https://docs.copilotkit.ai/langgraph-fastapi/voice/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLangGraph (FastAPI)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/langgraph-fastapi)[Quickstart](https://docs.copilotkit.ai/langgraph-fastapi/quickstart)[Build with agents](https://docs.copilotkit.ai/langgraph-fastapi/build-with-agents)[Intelligence](https://docs.copilotkit.ai/langgraph-fastapi/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[Multimodal Attachments](https://docs.copilotkit.ai/langgraph-fastapi/multimodal-attachments)[Voice](https://docs.copilotkit.ai/langgraph-fastapi/voice)[Reasoning](https://docs.copilotkit.ai/langgraph-fastapi/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/langgraph-fastapi/frontend-tools)

Generative UI

Controlled

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

Voice

BasicsChat

# Voice

Real-time speech-to-text in the chat composer. The user speaks, the runtime transcribes, the agent runs the resulting prompt.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent.py

page.tsx

sample-audio-button.tsx

route.ts
    
    
    """LangGraph agent for the CopilotKit Showcase (FastAPI variant).Uses copilotkit's create_agent (wrapping langgraph) with CopilotKitMiddlewareso frontend-registered tools (useHumanInTheLoop, useFrontendTool) are properlyinjected into the LLM's tool list and executed on the frontend rather thanlocally."""from tools import (    get_weather_impl,    query_data_impl,    schedule_meeting_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,)from tools.types import SalesTodo, Flightimport jsonimport timefrom typing import Anyfrom langchain_openai import ChatOpenAIfrom langchain_core.tools import tool as lc_toolfrom langchain_core.messages import SystemMessagefrom langchain.agents import AgentState as BaseAgentState, create_agentfrom langchain.tools import ToolRuntime, toolfrom langchain.messages import ToolMessagefrom langgraph.types import Commandfrom copilotkit import CopilotKitMiddlewareclass AgentState(BaseAgentState):    todos: list[SalesTodo]@lc_tooldef get_weather(location: str):    """Get the current weather for a location."""    return get_weather_impl(location)@lc_tooldef query_data(query: str):    """Query the database. Takes natural language. Always call before showing a chart."""    return query_data_impl(query)@lc_tooldef schedule_meeting(reason: str, duration_minutes: int = 30):    """Schedule a meeting. The user will be asked to pick a time via the UI."""    return schedule_meeting_impl(reason, duration_minutes)@lc_tooldef search_flights(flights: list[Flight]) -> str:    """Search for flights and display the results as rich cards. Return exactly 2 flights.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date (short readable format like "Tue, Mar 18" -- use near-future dates),    departureTime, arrivalTime, duration (e.g. "4h 25m"),    status (e.g. "On Time" or "Delayed"),    statusColor (hex color for status dot),    price (e.g. "$289"), and currency (e.g. "USD").    For airlineLogo use Google favicon API:    https://www.google.com/s2/favicons?domain={airline_domain}&sz=128    """    result = search_flights_impl(flights)    return json.dumps(result)@tooldef manage_sales_todos(todos: list[SalesTodo], runtime: ToolRuntime) -> Command:    """    Manage the current sales todos. Pass the full updated list.    """    updated = manage_sales_todos_impl(todos)    return Command(        update={            "todos": updated,            "messages": [                ToolMessage(                    content="Successfully updated sales todos",                    tool_call_id=runtime.tool_call_id,                )            ],        }    )@tooldef get_sales_todos(runtime: ToolRuntime):    """    Get the current sales todos.    """    current = runtime.state.get("todos", [])    return get_sales_todos_impl(current if current else None)@lc_tooldef render_a2ui(    surfaceId: str,    catalogId: str,    components: list[dict],    data: dict | None = None,) -> str:    """Render a dynamic A2UI v0.9 surface."""    return "rendered"@tool()def generate_a2ui(runtime: ToolRuntime[Any]) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data.    """    t0 = time.time()    messages = runtime.state["messages"][:-1]    context_entries = runtime.state.get("copilotkit", {}).get("context", [])    context_text = "\n\n".join(        entry.get("value", "")        for entry in context_entries        if isinstance(entry, dict) and entry.get("value")    )    model = ChatOpenAI(model="gpt-5-mini")    model_with_tool = model.bind_tools([render_a2ui], tool_choice="render_a2ui")    response = model_with_tool.invoke(        [SystemMessage(content=context_text), *messages],    )    if not response.tool_calls:        return json.dumps({"error": "LLM did not call render_a2ui"})    args = response.tool_calls[0]["args"]    result = build_a2ui_operations_from_tool_call(args)    return json.dumps(result)model = ChatOpenAI(model="gpt-5-mini")SYSTEM_PROMPT = """You are a polished, professional demo assistant for CopilotKit.Keep responses brief and clear -- 1 to 2 sentences max.You can:- Chat naturally with the user- Change the UI background when asked (via frontend tool)- Query data and render charts (via query_data tool)- Get weather information (via get_weather tool)- Schedule meetings with the user (via schedule_meeting tool -- the user picks a time in the UI)- Manage sales pipeline todos (via manage_sales_todos / get_sales_todos tools)- Search flights and display rich A2UI cards (via search_flights tool)- Generate dynamic A2UI dashboards from conversation context (via generate_a2ui tool)- Generate step-by-step plans for user review (human-in-the-loop)"""graph = create_agent(    model=model,    tools=[        get_weather,        query_data,        schedule_meeting,        search_flights,        generate_a2ui,        manage_sales_todos,        get_sales_todos,    ],    middleware=[CopilotKitMiddleware()],    state_schema=AgentState,    system_prompt=SYSTEM_PROMPT,)

You have a working chat surface and you want users to be able to speak instead of type. By the end of this guide, the chat composer will sprout a mic button, recorded audio will be transcribed by the runtime, and the transcript will auto-send to the agent like any other message.

## When to use this#

  * **Hands-free or accessibility flows** where typing isn't the right input modality.
  * **Mobile or kiosk surfaces** where a long voice query is faster than thumb-typing.
  * **Demo and test loops** where you want canned audio to drive the chat without a microphone.



If you only need file uploads (audio, images, video, documents), use [Multimodal Attachments](https://docs.copilotkit.ai/langgraph-fastapi/multimodal-attachments) instead. Voice is specifically about live transcription of recorded speech into chat input.

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
    
    
    import type { NextRequest } from "next/server";import {  CopilotRuntime,  TranscriptionService,  createCopilotRuntimeHandler,} from "@copilotkit/runtime/v2";import type { TranscribeFileOptions } from "@copilotkit/runtime/v2";import { LangGraphAgent } from "@copilotkit/runtime/langgraph";import { TranscriptionServiceOpenAI } from "@copilotkit/voice";import OpenAI from "openai";const LANGGRAPH_URL =  process.env.AGENT_URL ||  process.env.LANGGRAPH_DEPLOYMENT_URL ||  "http://localhost:8123";const voiceDemoAgent = new LangGraphAgent({  deploymentUrl: `${LANGGRAPH_URL}/`,  graphId: "sample_agent",});/** * Transcription service wrapper that reports a clean, typed auth error when * OPENAI_API_KEY is not configured. When the key is present we delegate to * the real OpenAI-backed service; any upstream Whisper error keeps its * natural categorization. */class GuardedOpenAITranscriptionService extends TranscriptionService {  private delegate: TranscriptionServiceOpenAI | null;  constructor() {    super();    const apiKey = process.env.OPENAI_API_KEY;    this.delegate = apiKey      ? new TranscriptionServiceOpenAI({ openai: new OpenAI({ apiKey }) })      : null;  }  async transcribeFile(options: TranscribeFileOptions): Promise<string> {    if (!this.delegate) {      // "api key" substring → handleTranscribe maps to AUTH_FAILED → 401.      throw new Error(        "OPENAI_API_KEY not configured for this deployment (api key missing). " +          "Set OPENAI_API_KEY to enable voice transcription.",      );    }    return this.delegate.transcribeFile(options);  }}// Cache the runtime + handler across invocations so the transcription service// is constructed once per Node process instead of per request. The guarded// service reads OPENAI_API_KEY lazily in its transcribeFile call path, so// deferring construction past module load is not required for cold-start// safety under missing-key conditions.let cachedHandler: ((req: Request) => Promise<Response>) | null = null;function getHandler(): (req: Request) => Promise<Response> {  if (cachedHandler) return cachedHandler;  const runtime = new CopilotRuntime({    // @ts-ignore -- Published CopilotRuntime agents type wraps Record in    // MaybePromise<NonEmptyRecord<...>> which rejects plain Records; fixed in    // source, pending release.    agents: {      // The page mounts <CopilotKit agent="voice-demo">; resolve that to      // the neutral sample_agent graph.      "voice-demo": voiceDemoAgent,      // useAgent() with no args defaults to "default"; alias so any internal      // default-agent lookups resolve against the same graph.      default: voiceDemoAgent,    },    transcriptionService: new GuardedOpenAITranscriptionService(),  });  cachedHandler = createCopilotRuntimeHandler({    runtime,    basePath: "/api/copilotkit-voice",  });  return cachedHandler;}// Next.js App Router bindings. This file lives at// `src/app/api/copilotkit-voice/[[...slug]]/route.ts` — the catchall slug// pattern forwards every sub-path (`/info`, `/agent/:id/run`,// `/transcribe`, ...) to the V2 handler so its URL router can dispatch.export const POST = (req: NextRequest) => getHandler()(req);export const GET = (req: NextRequest) => getHandler()(req);export const PUT = (req: NextRequest) => getHandler()(req);export const DELETE = (req: NextRequest) => getHandler()(req);

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
    
    
    import type { NextRequest } from "next/server";import {  CopilotRuntime,  TranscriptionService,  createCopilotRuntimeHandler,} from "@copilotkit/runtime/v2";import type { TranscribeFileOptions } from "@copilotkit/runtime/v2";import { LangGraphAgent } from "@copilotkit/runtime/langgraph";import { TranscriptionServiceOpenAI } from "@copilotkit/voice";import OpenAI from "openai";const LANGGRAPH_URL =  process.env.AGENT_URL ||  process.env.LANGGRAPH_DEPLOYMENT_URL ||  "http://localhost:8123";const voiceDemoAgent = new LangGraphAgent({  deploymentUrl: `${LANGGRAPH_URL}/`,  graphId: "sample_agent",});/** * Transcription service wrapper that reports a clean, typed auth error when * OPENAI_API_KEY is not configured. When the key is present we delegate to * the real OpenAI-backed service; any upstream Whisper error keeps its * natural categorization. */class GuardedOpenAITranscriptionService extends TranscriptionService {  private delegate: TranscriptionServiceOpenAI | null;  constructor() {    super();    const apiKey = process.env.OPENAI_API_KEY;    this.delegate = apiKey      ? new TranscriptionServiceOpenAI({ openai: new OpenAI({ apiKey }) })      : null;  }  async transcribeFile(options: TranscribeFileOptions): Promise<string> {    if (!this.delegate) {      // "api key" substring → handleTranscribe maps to AUTH_FAILED → 401.      throw new Error(        "OPENAI_API_KEY not configured for this deployment (api key missing). " +          "Set OPENAI_API_KEY to enable voice transcription.",      );    }    return this.delegate.transcribeFile(options);  }}

### On this page

When to use thisFrontendDriving the demo without a micBackendNext.js API routeCustom transcription backends
