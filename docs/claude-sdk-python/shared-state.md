---
url: https://docs.copilotkit.ai/claude-sdk-python/shared-state/
title: Shared State
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:53:51.392995+00:00
---

# Shared State

> Source: https://docs.copilotkit.ai/claude-sdk-python/shared-state/

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

[Shared State](https://docs.copilotkit.ai/claude-sdk-python/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/claude-sdk-python/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/claude-sdk-python/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/claude-sdk-python/shared-state/agent-readonly)

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

Shared State

InteractivityShared state

# Shared State

Create a two-way connection between your UI and agent state.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is shared state?#

Agentic Copilots maintain a shared state that seamlessly connects your UI with the agent's execution. This shared state system allows you to:

  * Display the agent's current progress and intermediate results
  * Update the agent's state through UI interactions
  * React to state changes in real-time across your application

![Shared State Demo](https://cdn.copilotkit.ai/docs/copilotkit/images/coagents/SharedStateCoAgents.gif)

See this in Inspector

Open Inspector on localhost. Open a thread, then click **State**. Agent state updates here as the run proceeds.

More detail: [Inspector](https://docs.copilotkit.ai/claude-sdk-python/inspector).

## When should I use this?#

Use shared state when you want the agent and the user to collaborate through the same application state. The agent's outputs are reflected in the UI, and user updates in the UI are reflected in the agent's execution.

[Building stateful agents?Persistent threads ship with CopilotKit Intelligence on the free Developer tier.Get CopilotKit Intelligence free](https://ssr-placeholder.invalid/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_shared_state&utm_frontend=react&utm_backend=claude-sdk-python)

## Reading agent state#

### Put shared state in the system prompt and tools

The demo exposes frontend preferences to Claude and gives the agent a tool for writing notes back into CopilotKit state. Keep the state contract small, typed, and mirrored by the UI components that read the same values.

shared_state_read_write_agent.py
    
    
    SYSTEM_PROMPT = dedent("""
        You are a helpful, concise assistant.
    
        The user's preferences are supplied via shared state and added at the
        start of every turn — always respect them. Address the user by name
        when known, match the requested tone, and respond in the requested
        language.
    
        When the user asks you to "remember" something, or you observe
        something worth surfacing in the UI's notes panel, call the
        ``set_notes`` tool with the FULL updated list of short notes
        (existing notes + new ones, not a diff). Keep each note short
        (< 120 characters). After updating notes, briefly acknowledge what
        you remembered.
    """).strip()
    
    
    SET_NOTES_TOOL: dict[str, Any] = {
        "name": "set_notes",
        "description": (
            "Replace the notes array in shared state with the FULL updated "
            "list. Always include every existing note plus any new ones, "
            "not a diff. Keep each note short (< 120 chars)."
        ),
        "input_schema": {
            "type": "object",
            "properties": {
                "notes": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Full list of short note strings to persist.",
                },
            },
            "required": ["notes"],
        },
    }
    
    
    def build_preferences_block(prefs: dict[str, Any] | None) -> str | None:
        """Render the user-supplied preferences as an injectable prompt block.
    
        Returns ``None`` when no recognised keys are present so the system
        prompt is left untouched.
        """
        if not isinstance(prefs, dict) or not prefs:
            return None
        lines = ["The user has shared these preferences with you:"]
        if prefs.get("name"):
            lines.append(f"- Name: {prefs['name']}")
        if prefs.get("tone"):
            lines.append(f"- Preferred tone: {prefs['tone']}")
        if prefs.get("language"):
            lines.append(f"- Preferred language: {prefs['language']}")
        interests = prefs.get("interests") or []
        if isinstance(interests, list) and interests:
            lines.append(f"- Interests: {', '.join(str(i) for i in interests)}")
        if len(lines) == 1:
            # No recognised fields — don't emit a header with no content.
            return None
        lines.append(
            "Tailor every response to these preferences. Address the user "
            "by name when appropriate."
        )
        return "\n".join(lines)
    
    
    def _state_dict(state: dict[str, Any]) -> dict[str, Any]:
        """Coerce the AG-UI raw state envelope into the slots we care about."""
        return {
            "preferences": state.get("preferences") or {},
            "notes": list(state.get("notes") or []),
        }
    
    

### Register `set_notes` with Claude

This dedicated demo uses the Anthropic Messages API directly. Pass the schema to `client.messages.stream` so Claude can call `set_notes`.

shared_state_read_write_agent.py
    
    
    stream_request = client.messages.stream(
        model=normalize_claude_model(
            os.getenv("ANTHROPIC_MODEL", DEFAULT_ANTHROPIC_MODEL)
        ),
        max_tokens=2048,
        system=system,
        messages=messages,
        tools=[SET_NOTES_TOOL],
    )

### Write the tool result back to shared state

When Claude calls `set_notes`, replace the notes array, emit a `StateSnapshotEvent` for the UI, and return a `ToolCallResultEvent` to Claude before the loop continues.

shared_state_read_write_agent.py
    
    
    # Execute set_notes by mutating shared state and emitting a
    # StateSnapshotEvent so the UI re-renders the agent-authored
    # notes. This is the agent-side half of the WRITE direction.
    tool_results: list[dict[str, Any]] = []
    for tc in tool_calls:
        if tc["name"] == "set_notes":
            notes = tc["input"].get("notes") or []
            if isinstance(notes, list):
                state["notes"] = [str(n) for n in notes]
            result_text = json.dumps({"status": "ok", "count": len(state["notes"])})
            yield encoder.encode(
                StateSnapshotEvent(type=EventType.STATE_SNAPSHOT, snapshot=state)
            )
        else:
            result_text = json.dumps({"error": f"unknown tool {tc['name']}"})
    
        yield encoder.encode(
            ToolCallResultEvent(
                type=EventType.TOOL_CALL_RESULT,
                tool_call_id=tc["id"],
                message_id=f"{msg_id}-tool-result-{tc['id']}",
                content=result_text,
            )
        )
        tool_results.append(
            {
                "type": "tool_result",
                "tool_use_id": tc["id"],
                "content": result_text,
            }
        )
    messages.append({"role": "user", "content": tool_results})

### Serve the shared-state loop

Mount the dedicated runner on `/shared-state-read-write` and return its AG-UI events as a streaming response.

agent_server.py
    
    
    @app.post("/shared-state-read-write")
    async def shared_state_read_write_endpoint(request: Request) -> StreamingResponse:
        """Bidirectional shared state demo — UI writes preferences, agent writes notes.
    
        Uses its own streaming loop (not the shared sales-assistant
        ``run_agent``) because the state schema, tools, and prompt-injection
        middleware are all demo-specific.
        """
        body = await request.json()
        input_data = RunAgentInput(**body)
    
        async def event_stream() -> AsyncIterator[str]:
            async for chunk in run_shared_state_read_write_agent(input_data):
                yield chunk
    
        return StreamingResponse(
            event_stream(),
            media_type="text/event-stream",
            headers={
                "Cache-Control": "no-cache",
                "X-Accel-Buffering": "no",
            },
        )
    
    

This Python route intentionally uses its own Messages API loop. It does not use `ClaudeAgentAdapter` or an MCP server.

Subscribe a component to the agent's state with `useAgent`. Any time the agent mutates its state, for example via a tool call, the hook fires and your UI re-renders with the new values.

page.tsx
    
    
      // Subscribe the component to agent state changes. Any time the agent  // mutates its state (e.g. via its `set_notes` tool) this hook fires,  // we re-render, and the sidebar panels reflect the new values.  const { agent } = useAgent({    agentId: "shared-state-read-write",    updates: [UseAgentUpdate.OnStateChanged],  });

The returned `agent.state` is just a plain object. Read it like any other piece of React state and render the parts you care about: agent-written notes, structured outputs, progress indicators, anything the agent has put there.

## Writing agent state#

The same `agent` object exposes a `setState` setter. Calling it from a UI event handler pushes the new value into shared state, and the agent reads it back on its next turn. The UI's writes visibly steer the model.

page.tsx
    
    
      // WRITE: every edit in the sidebar goes straight into agent state.  // On the agent's next turn, `PreferencesInjectorMiddleware` reads this  // back out of state and adds it to the system prompt — so the UI's  // writes visibly steer the model.  const handlePreferencesChange = (next: Preferences) => {    agent.setState({      preferences: next,      notes: latestNotesRef.current, // preserve what the agent has written    } as RWAgentState);  };

This is what makes the channel two-way: the UI doesn't just observe the agent, it can hand the agent fresh inputs (preferences, selections, partial work) without going through the chat thread.

## Rendering shared state in the UI#

Because `agent.state` is plain React data, the UI layer is whatever you'd normally build. The demo on this page wires the agent's outputs into a small card component and feeds user edits back through `setState`.

notes-card.tsx
    
    
    // Read-side render: this card reflects the agent-authored `notes` slice// of shared state. The parent page passes `state.notes` in; we never// touch agent state ourselves — we just render it. The Clear button is// a small write-back, exposed as an `onClear` prop.export function NotesCard({ notes, onClear }: NotesCardProps) {  return (    <Card data-testid="notes-card" className="w-full">      <CardHeader>        <div className="flex items-start justify-between gap-3">          <div className="space-y-1.5">            <CardTitle>Agent Scratch pad</CardTitle>            <CardDescription>              The agent writes here via its{" "}              <code className="font-mono text-[11px] text-[#010507]">                set_notes              </code>{" "}              tool. The UI re-renders from shared state.            </CardDescription>          </div>          {notes.length > 0 && (            <Button              type="button"              onClick={onClear}              data-testid="notes-clear-button"              variant="destructive"              size="sm"              className="uppercase tracking-[0.14em] text-[10px]"            >              Clear            </Button>          )}        </div>      </CardHeader>      <CardContent>        {notes.length === 0 ? (          <div            data-testid="notes-empty"            className="text-sm text-[#838389] italic min-h-[160px] flex items-center justify-center text-center px-4 border border-dashed border-[#E9E9EF] rounded-xl bg-[#FAFAFC]"          >            the agent will make observations about you and note them here!          </div>        ) : (          <ul            data-testid="notes-list"            className="space-y-2 text-sm text-[#010507]"          >            {notes.map((note, i) => (              <li                key={i}                data-testid="note-item"                className="flex gap-2 rounded-lg border border-[#E9E9EF] bg-[#FAFAFC] px-3 py-2"              >                <span className="text-[#838389] font-mono text-xs leading-5 select-none">                  {String(i + 1).padStart(2, "0")}                </span>                <span className="flex-1">{note}</span>              </li>            ))}          </ul>        )}      </CardContent>    </Card>  );}

Nothing about this is chat-specific: `useAgent` works in any component under `<CopilotKit>`, so you can render `agent.state` in your main view or canvas, not just inside the chat panel. See **[Render agent state in your app](https://docs.copilotkit.ai/claude-sdk-python/shared-state/rendering-in-app)** for the full main-view pattern.

## Streaming partial state updates#

By default, agent state only updates _between_ backend checkpoints, so a long-running tool call appears as one big burst at the end. State streaming forwards a specific tool argument straight into a state key _as it's being generated_ , so the UI can watch the answer assemble token-by-token.

state_streaming_backend.py
    
    
    import jsonfrom collections.abc import AsyncIteratorfrom typing import Anyfrom ag_ui.core import EventType, StateSnapshotEventfrom ag_ui.encoder import EventEncoderfrom pydantic import BaseModelclass AgentState(BaseModel):    document: str = ""WRITE_DOCUMENT_TOOL_SCHEMA: dict[str, Any] = {    "name": "write_document",    "description": "Write a document into shared agent state.",    "input_schema": {        "type": "object",        "properties": {            "document": {                "type": "string",                "description": "The full document text to render in shared state.",            },        },        "required": ["document"],    },}def _partial_json_string_property(source: str, key: str) -> str | None:    """Return the current value of a streamed JSON string property."""    marker = json.dumps(key)    key_pos = source.find(marker)    if key_pos < 0:        return None    colon_pos = source.find(":", key_pos)    if colon_pos < 0:        # The colon hasn't streamed yet (e.g. source is `{"document`); bail out        # rather than letting find(":") return -1 and matching the key's own        # opening quote, which would report the key name as the value.        return None    value_start = source.find('"', colon_pos + 1)    if value_start < 0:        return None    raw_chars: list[str] = []    escaped = False    for char in source[value_start + 1 :]:        if escaped:            raw_chars.append("\\" + char)            escaped = False        elif char == "\\":            escaped = True        elif char == '"':            break        else:            raw_chars.append(char)    try:        return json.loads(f'"{"".join(raw_chars)}"')    except json.JSONDecodeError:        return Noneasync def stream_document_state(    anthropic_stream: AsyncIterator[Any],    state: AgentState,) -> AsyncIterator[str]:    encoder = EventEncoder()    current_tool_name: str | None = None    current_tool_args = ""    last_streamed_document = state.document    async for event in anthropic_stream:        if (            event.type == "content_block_start"            and event.content_block.type == "tool_use"        ):            current_tool_name = event.content_block.name            current_tool_args = ""            continue        if (            event.type != "content_block_delta"            or event.delta.type != "input_json_delta"        ):            continue        current_tool_args += event.delta.partial_json        if current_tool_name != "write_document":            continue        streamed_document = _partial_json_string_property(            current_tool_args,            "document",        )        if streamed_document is None or streamed_document == last_streamed_document:            continue        state.document = streamed_document        last_streamed_document = streamed_document        yield encoder.encode(            StateSnapshotEvent(                type=EventType.STATE_SNAPSHOT,                snapshot=state.model_dump(),            )        )

See **[State streaming](https://docs.copilotkit.ai/claude-sdk-python/shared-state/streaming)** for the full walkthrough, including the corresponding `useAgent` subscription on the frontend.

## Read-only context#

When the value is **UI-owned** and the agent should read it but never write it back, such as current user, selected record, or scroll position, reach for `useAgentContext` instead of full shared state. It publishes values as a one-way UI-to-agent channel that auto-unregisters on unmount.

See **[Agent read-only context](https://docs.copilotkit.ai/claude-sdk-python/shared-state/agent-readonly)** for the full pattern.

### On this page

What is shared state?When should I use this?Reading agent stateWriting agent stateRendering shared state in the UIStreaming partial state updatesRead-only context
