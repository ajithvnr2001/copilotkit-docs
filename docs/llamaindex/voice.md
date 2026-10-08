---
url: https://docs.copilotkit.ai/llamaindex/voice/
title: Voice
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:15:44.635888+00:00
---

# Voice

> Source: https://docs.copilotkit.ai/llamaindex/voice/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)

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
    
    
    """LlamaIndex AG-UI AgentUses llama-index-protocols-ag-ui to expose a LlamaIndex workflow as anAG-UI compatible FastAPI router. The router handles all four demoscenarios (agentic-chat, tool-rendering, hitl, gen-ui-tool-based) througha single endpoint since LlamaIndex's get_ag_ui_workflow_router buildsthe full AG-UI protocol surface automatically.NOTE: Uses FixedAGUIChatWorkflow from hitl_in_chat_agent to fix threeupstream library bugs (duplicate tool-call rendering, missingparent_message_id, and incorrect tool-result message roles). Seehitl_in_chat_agent.py module docstring for details."""import asyncioimport jsonimport osfrom typing import Annotatedfrom llama_index.llms.openai import OpenAIfrom llama_index.protocols.ag_ui.router import get_ag_ui_workflow_routerfrom agents.hitl_in_chat_agent import FixedAGUIChatWorkflow# Import shared tool implementationsfrom tools import (    get_weather_impl,    query_data_impl,    manage_sales_todos_impl,    get_sales_todos_impl,    schedule_meeting_impl,    search_flights_impl,    build_a2ui_operations_from_tool_call,)# --- Frontend tools (executed client-side, agent just returns a confirmation) ---def change_background(    background: Annotated[str, "CSS background value. Prefer gradients."],) -> str:    """Change the background color/gradient of the chat area."""    return f"Background changed to {background}"def generate_haiku(    japanese: Annotated[list[str], "3 lines of haiku in Japanese"],    english: Annotated[list[str], "3 lines of haiku translated to English"],    image_name: Annotated[str, "One relevant image name from the valid set"],    gradient: Annotated[str, "CSS Gradient color for the background"],) -> str:    """Generate a haiku with Japanese text, English translation, and a background image."""    return "Haiku generated!"def generate_task_steps(    steps: Annotated[        list[dict],        "Array of step objects with 'description' (string) and 'status' ('enabled' or 'disabled')",    ],) -> str:    """Generate a list of task steps for the user to review and approve."""    return f"Generated {len(steps)} steps for review"def book_call(    topic: Annotated[str, "What the call is about (e.g. 'Intro with sales')"],    attendee: Annotated[str, "Who the call is with (e.g. 'Alice from Sales')"],) -> str:    """Ask the user to pick a time slot for a call. The picker UI presents fixed candidate slots; the user's choice is returned to the agent."""    return f"Booking call about {topic} with {attendee}"def show_card(    title: Annotated[str, "Short heading for the card."],    body: Annotated[str, "Body text for the card."],) -> str:    """Display a titled card with a short body of text. Rendered on the frontend via useComponent."""    return f"Displayed card: {title}"# --- Backend tools (executed server-side, using shared implementations) ---async def get_weather(    location: Annotated[str, "The location to get the weather for."],) -> str:    """Get the weather for a given location. Returns temperature, conditions, humidity, wind speed, and feels-like temperature."""    return json.dumps(get_weather_impl(location))async def query_data(    query: Annotated[str, "Natural language query for financial data."],) -> str:    """Query financial database for chart data. Always call before showing a chart or graph."""    return json.dumps(query_data_impl(query))async def manage_sales_todos(    todos: Annotated[        list[dict], "Complete list of sales todos to replace the current list."    ],) -> str:    """Manage the sales pipeline by replacing the entire list of todos."""    result = manage_sales_todos_impl(todos)    return json.dumps(        {"status": "updated", "count": len(result), "todos": [dict(t) for t in result]}    )async def get_sales_todos_tool() -> str:    """Get the current sales pipeline todos."""    return json.dumps(get_sales_todos_impl(None))async def schedule_meeting(    reason: Annotated[str, "Reason for the meeting."],) -> str:    """Schedule a meeting with the user. Requires human approval."""    return json.dumps(schedule_meeting_impl(reason))async def search_flights(    flights: Annotated[        list[dict],        "List of flight objects to search and display as rich cards. Return exactly 2 flights.",    ],) -> str:    """Search for flights and display the results as rich A2UI cards.    Each flight must have: airline, airlineLogo, flightNumber, origin, destination,    date, departureTime, arrivalTime, duration, status, statusColor, price, currency.    """    result = search_flights_impl(flights)    return json.dumps(result)def _generate_a2ui(context: str) -> str:    """Blocking secondary-LLM round-trip for `generate_a2ui`.    Kept synchronous and offloaded via ``asyncio.to_thread`` from the async    tool wrapper below: the synchronous ``openai.OpenAI().chat.completions``    call would otherwise block the uvicorn asyncio event loop for the full    LLM round-trip, wedging the ``:8000`` ``/health`` endpoint under load.    """    from openai import OpenAI    client = OpenAI()    tool_schema = {        "type": "function",        "function": {            "name": "render_a2ui",            "description": "Render a dynamic A2UI v0.9 surface.",            "parameters": {                "type": "object",                "properties": {                    "surfaceId": {"type": "string"},                    "catalogId": {"type": "string"},                    "components": {"type": "array", "items": {"type": "object"}},                    "data": {"type": "object"},                },                "required": ["surfaceId", "catalogId", "components"],            },        },    }    response = client.chat.completions.create(        model="gpt-5-mini",        messages=[            {"role": "system", "content": context or "Generate a useful dashboard UI."},            {                "role": "user",                "content": "Generate a dynamic A2UI dashboard based on the conversation.",            },        ],        tools=[tool_schema],        tool_choice={"type": "function", "function": {"name": "render_a2ui"}},    )    if not response.choices[0].message.tool_calls:        return json.dumps({"error": "LLM did not call render_a2ui"})    tool_call = response.choices[0].message.tool_calls[0]    args = json.loads(tool_call.function.arguments)    result = build_a2ui_operations_from_tool_call(args)    return json.dumps(result)async def generate_a2ui(    context: Annotated[str, "Conversation context to generate UI from."],) -> str:    """Generate dynamic A2UI components based on the conversation.    A secondary LLM designs the UI schema and data. The result is    returned as an a2ui_operations container for the middleware to detect.    The blocking LLM round-trip runs in ``_generate_a2ui`` and is offloaded    via ``asyncio.to_thread`` so it never blocks the event loop.    """    return await asyncio.to_thread(_generate_a2ui, context)_openai_kwargs = {}if os.environ.get("OPENAI_BASE_URL"):    _openai_kwargs["api_base"] = os.environ["OPENAI_BASE_URL"]_AGENT_SYSTEM_PROMPT = (    "You are a polished, professional demo assistant for CopilotKit. "    "Keep responses brief and clear -- 1 to 2 sentences max.\n\n"    "You can:\n"    "- Chat naturally with the user\n"    "- Change the UI background when asked (via frontend tool)\n"    "- Query data and render charts (via query_data tool)\n"    "- Get weather information (via get_weather tool)\n"    "- Schedule meetings with the user (via schedule_meeting tool)\n"    "- Manage sales pipeline todos (via manage_sales_todos / get_sales_todos tools)\n"    "- Search flights and display rich A2UI cards (via search_flights tool)\n"    "- Generate dynamic A2UI dashboards from conversation context (via generate_a2ui tool)\n"    "- Generate step-by-step plans for user review (human-in-the-loop)\n"    "- Book calls with people (via book_call frontend tool)\n"    "- Show titled cards with a body of text (via show_card frontend tool)\n"    "When asked about weather, always use the get_weather tool. "    "When asked about financial data or charts, use query_data first. "    "When asked to book a call, use the book_call tool with topic and name.")async def _agent_workflow_factory():    wf = FixedAGUIChatWorkflow(        llm=OpenAI(model="gpt-5-mini", **_openai_kwargs),        frontend_tools=[            change_background,            generate_haiku,            generate_task_steps,            book_call,            show_card,            get_weather,        ],        backend_tools=[            query_data,            manage_sales_todos,            get_sales_todos_tool,            schedule_meeting,            search_flights,            generate_a2ui,        ],        system_prompt=_AGENT_SYSTEM_PROMPT,        initial_state={            "todos": [],        },    )    # Tools that use useRenderTool on the frontend — emit    # TOOL_CALL_RESULT so the render transitions to "complete".    wf.render_only_tool_names = {"get_weather"}    return wfagent_router = get_ag_ui_workflow_router(    workflow_factory=_agent_workflow_factory,)

You have a working chat surface and you want users to be able to speak instead of type. By the end of this guide, the chat composer will sprout a mic button, recorded audio will be transcribed by the runtime, and the transcript will auto-send to the agent like any other message.

## When to use this#

  * **Hands-free or accessibility flows** where typing isn't the right input modality.
  * **Mobile or kiosk surfaces** where a long voice query is faster than thumb-typing.
  * **Demo and test loops** where you want canned audio to drive the chat without a microphone.



If you only need file uploads (audio, images, video, documents), use [Multimodal Attachments](https://docs.copilotkit.ai/llamaindex/multimodal-attachments) instead. Voice is specifically about live transcription of recorded speech into chat input.

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
    
    
    import type { NextRequest } from "next/server";import {  CopilotRuntime,  TranscriptionService,  createCopilotRuntimeHandler,} from "@copilotkit/runtime/v2";import type { TranscribeFileOptions } from "@copilotkit/runtime/v2";import { HttpAgent } from "@ag-ui/client";import { TranscriptionServiceOpenAI } from "@copilotkit/voice";import OpenAI from "openai";const AGENT_URL = process.env.AGENT_URL || "http://localhost:8000";// Point at the tool-free /voice endpoint so aimock returns a direct text// response instead of a tool call that the agent can't summarize.const voiceDemoAgent = new HttpAgent({ url: `${AGENT_URL}/voice/run` });class GuardedOpenAITranscriptionService extends TranscriptionService {  private delegate: TranscriptionServiceOpenAI | null;  constructor() {    super();    const apiKey = process.env.OPENAI_API_KEY;    this.delegate = apiKey      ? new TranscriptionServiceOpenAI({ openai: new OpenAI({ apiKey }) })      : null;  }  async transcribeFile(options: TranscribeFileOptions): Promise<string> {    if (!this.delegate) {      throw new Error(        "OPENAI_API_KEY not configured for this deployment (api key missing). " +          "Set OPENAI_API_KEY to enable voice transcription.",      );    }    return this.delegate.transcribeFile(options);  }}let cachedHandler: ((req: Request) => Promise<Response>) | null = null;function getHandler(): (req: Request) => Promise<Response> {  if (cachedHandler) return cachedHandler;  const runtime = new CopilotRuntime({    // @ts-ignore -- Published CopilotRuntime agents type wraps Record in    // MaybePromise<NonEmptyRecord<...>> which rejects plain Records; fixed in    // source, pending release.    agents: {      "voice-demo": voiceDemoAgent,      default: voiceDemoAgent,    },    transcriptionService: new GuardedOpenAITranscriptionService(),  });  cachedHandler = createCopilotRuntimeHandler({    runtime,    basePath: "/api/copilotkit-voice",  });  return cachedHandler;}export const POST = (req: NextRequest) => getHandler()(req);export const GET = (req: NextRequest) => getHandler()(req);export const PUT = (req: NextRequest) => getHandler()(req);export const DELETE = (req: NextRequest) => getHandler()(req);

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
    
    
    import type { NextRequest } from "next/server";import {  CopilotRuntime,  TranscriptionService,  createCopilotRuntimeHandler,} from "@copilotkit/runtime/v2";import type { TranscribeFileOptions } from "@copilotkit/runtime/v2";import { HttpAgent } from "@ag-ui/client";import { TranscriptionServiceOpenAI } from "@copilotkit/voice";import OpenAI from "openai";const AGENT_URL = process.env.AGENT_URL || "http://localhost:8000";// Point at the tool-free /voice endpoint so aimock returns a direct text// response instead of a tool call that the agent can't summarize.const voiceDemoAgent = new HttpAgent({ url: `${AGENT_URL}/voice/run` });class GuardedOpenAITranscriptionService extends TranscriptionService {  private delegate: TranscriptionServiceOpenAI | null;  constructor() {    super();    const apiKey = process.env.OPENAI_API_KEY;    this.delegate = apiKey      ? new TranscriptionServiceOpenAI({ openai: new OpenAI({ apiKey }) })      : null;  }  async transcribeFile(options: TranscribeFileOptions): Promise<string> {    if (!this.delegate) {      throw new Error(        "OPENAI_API_KEY not configured for this deployment (api key missing). " +          "Set OPENAI_API_KEY to enable voice transcription.",      );    }    return this.delegate.transcribeFile(options);  }}

### On this page

When to use thisFrontendDriving the demo without a micBackendNext.js API routeCustom transcription backends
