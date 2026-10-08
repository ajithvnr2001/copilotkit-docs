---
url: https://docs.copilotkit.ai/ms-agent-python/voice/
title: Voice
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:23:03.023790+00:00
---

# Voice

> Source: https://docs.copilotkit.ai/ms-agent-python/voice/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-python)[Quickstart](https://docs.copilotkit.ai/ms-agent-python/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-python/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-python/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-python/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-python/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-python/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-python/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-python/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (Python)](https://docs.copilotkit.ai/ms-agent-python)

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
    
    
    """MS Agent Framework agent with sales todos state, weather tool, query data,and HITL schedule meeting tool.Adapted from examples/integrations/ms-agent-framework-python/agent/src/agent.py"""from __future__ import annotationsimport jsonfrom textwrap import dedentfrom typing import Annotatedfrom agent_framework import Agent, BaseChatClient, toolfrom agent_framework_ag_ui import AgentFrameworkAgentfrom pydantic import Field# =====================================================================# Shared tool implementations# =====================================================================from tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,)STATE_SCHEMA: dict[str, object] = {    "salesTodos": {        "type": "array",        "items": {            "type": "object",            "properties": {                "id": {"type": "string"},                "title": {"type": "string"},                "stage": {"type": "string"},                "value": {"type": "number"},                "dueDate": {"type": "string"},                "assignee": {"type": "string"},                "completed": {"type": "boolean"},            },        },        "description": "Ordered list of the user's sales pipeline todos.",    }}PREDICT_STATE_CONFIG: dict[str, dict[str, str]] = {    "salesTodos": {        "tool": "manage_sales_todos",        "tool_argument": "todos",    }}@tool(    name="manage_sales_todos",    description=(        "Replace the entire list of sales todos with the provided values. "        "Always include every todo you want to keep."    ),)def manage_sales_todos(    todos: Annotated[        list[dict],        Field(            description=(                "The complete source of truth for the user's sales todos. "                "Maintain ordering and include the full list on each call."            )        ),    ],) -> str:    """Persist the provided set of sales todos."""    result = manage_sales_todos_impl(todos)    return f"Sales todos updated. Tracking {len(result)} item(s)."@tool(    name="get_sales_todos",    description="Get the current list of sales todos.",)def get_sales_todos() -> str:    """Return the current sales todos or defaults."""    result = get_sales_todos_impl()    return json.dumps(result)@tool(    name="get_weather",    description="Get the current weather for a location. Use this to render the frontend weather card.",)def get_weather(    location: Annotated[        str,        Field(            description="The city or region to describe. Use fully spelled out names."        ),    ],) -> str:    """Return weather data as JSON for UI rendering."""    result = get_weather_impl(location)    return json.dumps(result)@tool(    name="query_data",    description="Query the database. Takes natural language. Always call before showing a chart or graph.",)def query_data(    query: Annotated[        str, Field(description="Natural language query to run against the database.")    ],) -> str:    """Query the database and return results as JSON."""    result = query_data_impl(query)    return json.dumps(result)@tool(    name="schedule_meeting",    description="Schedule a meeting. The user will be asked to pick a time via the meeting time picker UI.",    approval_mode="always_require",)def schedule_meeting(    reason: Annotated[str, Field(description="Reason for scheduling the meeting.")],    duration_minutes: Annotated[        int, Field(description="Duration of the meeting in minutes.")    ] = 30,) -> str:    """Request human approval to schedule a meeting."""    result = schedule_meeting_impl(reason, duration_minutes)    return json.dumps(result)@tool(    name="search_flights",    description=(        "Search for flights and display the results as rich A2UI cards. Return exactly 2 flights. "        "Each flight must have: airline, airlineLogo, flightNumber, origin, destination, "        "date, departureTime, arrivalTime, duration, status, statusColor, price, currency."    ),)def search_flights(    flights: Annotated[        list[dict],        Field(description="List of flight objects to search and display."),    ],) -> str:    """Search for flights and display as rich cards."""    result = search_flights_impl(flights)    return json.dumps(result)def create_agent(chat_client: BaseChatClient) -> AgentFrameworkAgent:    """Instantiate the CopilotKit demo agent backed by Microsoft Agent Framework."""    base_agent = Agent(        client=chat_client,        name="sales_agent",        instructions=dedent(            """            You help users manage their sales pipeline, check weather, query data, and schedule meetings.            State sync:            - The current list of sales todos is provided in the conversation context.            - When you add, remove, or reorder todos, call `manage_sales_todos` with the full list.              Never send partial updates--always include every todo that should exist.            - CRITICAL: When asked to "add" a todo, you must:              1. First, identify ALL existing todos from the conversation history              2. Create EXACTLY ONE new todo (never more than one unless explicitly requested)              3. Call manage_sales_todos with: [all existing todos] + [the one new todo]            - When asked to "remove" a todo, remove exactly ONE item unless user specifies otherwise.            Tool usage rules:            - When user asks to schedule a meeting, you MUST call the `schedule_meeting` tool immediately.              Do NOT ask for approval yourself--the tool's approval workflow and the client UI will handle it.            Frontend integrations:            - `get_weather` renders a weather card in the UI. Only call this tool when the user explicitly              asks for weather. Do NOT call it after unrelated tasks or approvals.            - `query_data` fetches database records. Always call before showing charts or graphs.            - `schedule_meeting` requires explicit user approval before you proceed. Only use it when a              user asks to schedule or set up a meeting. Always call the tool instead of asking manually.            Conversation tips:            - Reference the latest todo list before suggesting changes.            - Keep responses concise and friendly unless the user requests otherwise.            - After you finish executing tools for the user's request, provide a brief, final assistant              message summarizing exactly what changed. Do NOT call additional tools or switch topics              after that summary unless the user asks. ALWAYS send this conversational summary so the message persists.            """.strip()        ),        tools=[            manage_sales_todos,            get_sales_todos,            get_weather,            query_data,            schedule_meeting,            search_flights,        ],    )    return AgentFrameworkAgent(        agent=base_agent,        name="CopilotKitMicrosoftAgentFrameworkAgent",        description="Manages sales pipeline todos, weather, data queries, and meeting scheduling.",        predict_state_config=PREDICT_STATE_CONFIG,        require_confirmation=False,    )

You have a working chat surface and you want users to be able to speak instead of type. By the end of this guide, the chat composer will sprout a mic button, recorded audio will be transcribed by the runtime, and the transcript will auto-send to the agent like any other message.

## When to use this#

  * **Hands-free or accessibility flows** where typing isn't the right input modality.
  * **Mobile or kiosk surfaces** where a long voice query is faster than thumb-typing.
  * **Demo and test loops** where you want canned audio to drive the chat without a microphone.



If you only need file uploads (audio, images, video, documents), use [Multimodal Attachments](https://docs.copilotkit.ai/ms-agent-python/multimodal-attachments) instead. Voice is specifically about live transcription of recorded speech into chat input.

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
    
    
    import type { NextRequest } from "next/server";import {  CopilotRuntime,  TranscriptionService,  createCopilotRuntimeHandler,} from "@copilotkit/runtime/v2";import type { TranscribeFileOptions } from "@copilotkit/runtime/v2";import { HttpAgent } from "@ag-ui/client";import { TranscriptionServiceOpenAI } from "@copilotkit/voice";import OpenAI from "openai";const AGENT_URL = process.env.AGENT_URL || "http://localhost:8000";// Point at the tool-free /voice endpoint so aimock returns a direct text// response instead of a tool call that the agent can't summarize.//// No trailing slash on the URL. FastAPI mounts this agent at `/voice`// exactly (via `add_agent_framework_fastapi_endpoint(path="/voice")` in// agent_server.py); posting to `/voice/` triggers FastAPI's// redirect-to-canonical 307, which kills the streaming SSE response and// surfaces as `fetch failed` / `INCOMPLETE_STREAM` in the runtime.const voiceDemoAgent = new HttpAgent({ url: `${AGENT_URL}/voice` });/** * Transcription service wrapper that reports a clean, typed auth error when * OPENAI_API_KEY is not configured. When the key is present we delegate to * the real OpenAI-backed service; any upstream Whisper error keeps its * natural categorization. * * Note: We pin `baseURL` to real OpenAI (or `OPENAI_TRANSCRIPTION_BASE_URL` * when explicitly set) instead of falling through to `OPENAI_BASE_URL`. In * local docker / Railway preview environments `OPENAI_BASE_URL` points at * aimock so LLM completions stay deterministic, but aimock has a catchall * `endpoint: "transcription"` fixture that would otherwise intercept every * real mic recording and return the canned "What is the weather in Tokyo?" * phrase regardless of what the user actually said — and on production * aimock's transcription proxy returns a 502 "Invalid file format" before * any phrase reaches the user. The sample-audio button is the deterministic * affordance (synchronous text injection); the mic is the only path that * should exercise real Whisper. * * Mirrors langgraph-python's voice route exactly. */class GuardedOpenAITranscriptionService extends TranscriptionService {  private delegate: TranscriptionServiceOpenAI | null;  constructor() {    super();    const apiKey = process.env.OPENAI_API_KEY;    const baseURL =      process.env.OPENAI_TRANSCRIPTION_BASE_URL ?? "https://api.openai.com/v1";    this.delegate = apiKey      ? new TranscriptionServiceOpenAI({          openai: new OpenAI({ apiKey, baseURL }),        })      : null;  }  async transcribeFile(options: TranscribeFileOptions): Promise<string> {    if (!this.delegate) {      throw new Error(        "OPENAI_API_KEY not configured for this deployment (api key missing). " +          "Set OPENAI_API_KEY to enable voice transcription.",      );    }    return this.delegate.transcribeFile(options);  }}let cachedHandler: ((req: Request) => Promise<Response>) | null = null;function getHandler(): (req: Request) => Promise<Response> {  if (cachedHandler) return cachedHandler;  const runtime = new CopilotRuntime({    // @ts-ignore -- Published CopilotRuntime agents type wraps Record in    // MaybePromise<NonEmptyRecord<...>> which rejects plain Records; fixed in    // source, pending release.    agents: {      "voice-demo": voiceDemoAgent,      default: voiceDemoAgent,    },    transcriptionService: new GuardedOpenAITranscriptionService(),  });  cachedHandler = createCopilotRuntimeHandler({    runtime,    basePath: "/api/copilotkit-voice",  });  return cachedHandler;}export const POST = (req: NextRequest) => getHandler()(req);export const GET = (req: NextRequest) => getHandler()(req);export const PUT = (req: NextRequest) => getHandler()(req);export const DELETE = (req: NextRequest) => getHandler()(req);

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
    
    
    import type { NextRequest } from "next/server";import {  CopilotRuntime,  TranscriptionService,  createCopilotRuntimeHandler,} from "@copilotkit/runtime/v2";import type { TranscribeFileOptions } from "@copilotkit/runtime/v2";import { HttpAgent } from "@ag-ui/client";import { TranscriptionServiceOpenAI } from "@copilotkit/voice";import OpenAI from "openai";const AGENT_URL = process.env.AGENT_URL || "http://localhost:8000";// Point at the tool-free /voice endpoint so aimock returns a direct text// response instead of a tool call that the agent can't summarize.//// No trailing slash on the URL. FastAPI mounts this agent at `/voice`// exactly (via `add_agent_framework_fastapi_endpoint(path="/voice")` in// agent_server.py); posting to `/voice/` triggers FastAPI's// redirect-to-canonical 307, which kills the streaming SSE response and// surfaces as `fetch failed` / `INCOMPLETE_STREAM` in the runtime.const voiceDemoAgent = new HttpAgent({ url: `${AGENT_URL}/voice` });/** * Transcription service wrapper that reports a clean, typed auth error when * OPENAI_API_KEY is not configured. When the key is present we delegate to * the real OpenAI-backed service; any upstream Whisper error keeps its * natural categorization. * * Note: We pin `baseURL` to real OpenAI (or `OPENAI_TRANSCRIPTION_BASE_URL` * when explicitly set) instead of falling through to `OPENAI_BASE_URL`. In * local docker / Railway preview environments `OPENAI_BASE_URL` points at * aimock so LLM completions stay deterministic, but aimock has a catchall * `endpoint: "transcription"` fixture that would otherwise intercept every * real mic recording and return the canned "What is the weather in Tokyo?" * phrase regardless of what the user actually said — and on production * aimock's transcription proxy returns a 502 "Invalid file format" before * any phrase reaches the user. The sample-audio button is the deterministic * affordance (synchronous text injection); the mic is the only path that * should exercise real Whisper. * * Mirrors langgraph-python's voice route exactly. */class GuardedOpenAITranscriptionService extends TranscriptionService {  private delegate: TranscriptionServiceOpenAI | null;  constructor() {    super();    const apiKey = process.env.OPENAI_API_KEY;    const baseURL =      process.env.OPENAI_TRANSCRIPTION_BASE_URL ?? "https://api.openai.com/v1";    this.delegate = apiKey      ? new TranscriptionServiceOpenAI({          openai: new OpenAI({ apiKey, baseURL }),        })      : null;  }  async transcribeFile(options: TranscribeFileOptions): Promise<string> {    if (!this.delegate) {      throw new Error(        "OPENAI_API_KEY not configured for this deployment (api key missing). " +          "Set OPENAI_API_KEY to enable voice transcription.",      );    }    return this.delegate.transcribeFile(options);  }}

### On this page

When to use thisFrontendDriving the demo without a micBackendNext.js API routeCustom transcription backends
