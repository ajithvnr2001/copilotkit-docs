---
url: https://docs.copilotkit.ai/google-adk/shared-state/agent-readonly/
title: Agent Read-Only Context
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:03:31.261169+00:00
---

# Agent Read-Only Context

> Source: https://docs.copilotkit.ai/google-adk/shared-state/agent-readonly/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendGoogle ADK

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/google-adk)[Quickstart](https://docs.copilotkit.ai/google-adk/quickstart)[Build with agents](https://docs.copilotkit.ai/google-adk/build-with-agents)[Intelligence](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/google-adk/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

[Shared State](https://docs.copilotkit.ai/google-adk/shared-state)[Render agent state in your app](https://docs.copilotkit.ai/google-adk/shared-state/rendering-in-app)[State Streaming](https://docs.copilotkit.ai/google-adk/shared-state/streaming)[Agent Read-Only Context](https://docs.copilotkit.ai/google-adk/shared-state/agent-readonly)

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/google-adk/webmcp)

Agent capabilities

Google ADK

[Sub-agents](https://docs.copilotkit.ai/google-adk/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/google-adk/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/google-adk/learning)

[User Memories](https://docs.copilotkit.ai/google-adk/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/google-adk/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/google-adk/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/google-adk/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/google-adk/intelligence/analytics)[Channels](https://docs.copilotkit.ai/google-adk/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/google-adk/telemetry)[Community frameworks](https://docs.copilotkit.ai/google-adk/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

InteractivityShared state

# Agent Read-Only Context

Publish UI values to the agent as a one-way read-only channel via useAgentContext.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

readonly_state_agent_context_agent.py

page.tsx

route.ts
    
    
    """Agent backing the Readonly Agent-Context demo.
    
    The frontend exposes some read-only context to the agent via
    useAgentContext({ description, value }) — CopilotKit forwards those
    entries into session state under state["copilotkit"]["context"]. A
    before-model callback reads them every turn and prepends a context block
    so the LLM can reference them.
    """
    
    from __future__ import annotations
    
    import logging
    from typing import Optional
    
    from ag_ui_adk import AGUIToolset
    from google.adk.agents import LlmAgent
    from google.adk.agents.callback_context import CallbackContext
    from google.adk.models.llm_request import LlmRequest
    from google.adk.models.llm_response import LlmResponse
    from google.genai import types
    
    from agents.shared_chat import get_model, stop_on_terminal_text
    
    logger = logging.getLogger(__name__)
    
    CONTEXT_PREFIX_SIGNATURE = "[agent-context] frontend-supplied context:"
    # Single source of truth for the trailing sentence — the strip-prior-block
    # logic in `_inject_context` looks for this exact string.
    CONTEXT_END_MARKER = "Treat this context as read-only background information."
    
    
    def _format_context(context_entries: list[dict]) -> str | None:
        if not context_entries:
            return None
        lines = [CONTEXT_PREFIX_SIGNATURE]
        for entry in context_entries:
            if not isinstance(entry, dict):
                continue
            desc = entry.get("description") or ""
            value = entry.get("value")
            if value is None:
                continue
            if desc:
                lines.append(f"- {desc}: {value}")
            else:
                lines.append(f"- {value}")
        if len(lines) == 1:
            return None
        lines.append(CONTEXT_END_MARKER)
        return "\n".join(lines)
    
    
    def _inject_context(
        callback_context: CallbackContext, llm_request: LlmRequest
    ) -> Optional[LlmResponse]:
        copilotkit_state = callback_context.state.get("copilotkit")
        # Coerce malformed state to empty rather than early-return; a stale
        # context block from a prior turn would otherwise stay embedded in
        # `system_instruction` indefinitely (the strip path runs unconditionally
        # below). Log when shape drifts so the regression surfaces server-side.
        if copilotkit_state is None:
            raw_entries: list = []
        elif not isinstance(copilotkit_state, dict):
            logger.warning(
                "agent-context: state['copilotkit'] is %s, expected dict; "
                "treating as empty",
                type(copilotkit_state).__name__,
            )
            raw_entries = []
        else:
            raw_entries_candidate = copilotkit_state.get("context")
            if raw_entries_candidate is None:
                raw_entries = []
            elif not isinstance(raw_entries_candidate, list):
                logger.warning(
                    "agent-context: state['copilotkit']['context'] is %s, "
                    "expected list; treating as empty",
                    type(raw_entries_candidate).__name__,
                )
                raw_entries = []
            else:
                raw_entries = raw_entries_candidate
    
        block = _format_context(raw_entries)
    
        original = llm_request.config.system_instruction
        if original is None:
            original_text = ""
        elif isinstance(original, types.Content):
            parts = original.parts or []
            original_text = (parts[0].text or "") if parts else ""
        else:
            original_text = str(original)
    
        sig_idx = original_text.find(CONTEXT_PREFIX_SIGNATURE)
        stripped_prior_block = False
        if sig_idx != -1:
            end_idx = original_text.find(CONTEXT_END_MARKER, sig_idx)
            if end_idx != -1:
                stripped_prior_block = True
                # Splice out only the prior block (preserve head + tail).
                # See agent_config_agent.py for the full rationale.
                original_text = (
                    original_text[:sig_idx]
                    + original_text[end_idx + len(CONTEXT_END_MARKER) :]
                ).lstrip("\n")
            else:
                logger.warning(
                    "agent-context: prior context block has signature but no "
                    "end marker; leaving original_text untouched to avoid "
                    "losing user content"
                )
    
        if block:
            new_text = (block + "\n\n" + original_text) if original_text else block
        else:
            new_text = original_text
    
        if not new_text and not stripped_prior_block:
            # Nothing to inject AND we didn't strip anything. Leave
            # system_instruction as-is — writing Content(text="") would
            # clobber the LlmAgent's static `instruction=`. If we DID
            # strip a prior block we must fall through and write the
            # result so the stale block doesn't stay embedded in the
            # existing Content. See agent_config_agent.py for full
            # rationale.
            return None
    
        llm_request.config.system_instruction = types.Content(
            role="system", parts=[types.Part(text=new_text)]
        )
        return None
    
    
    _INSTRUCTION = (
        "You are an assistant that uses frontend-supplied context to give "
        "more relevant answers. The frontend passes read-only context entries "
        "via useAgentContext; they are added to your system prompt every "
        "turn. Use them when relevant."
    )
    
    readonly_state_agent_context_agent = LlmAgent(
        name="ReadonlyStateAgentContextAgent",
        model=get_model(),
        instruction=_INSTRUCTION,
        tools=[AGUIToolset()],
        before_model_callback=_inject_context,
        after_model_callback=stop_on_terminal_text,
    )
    

See this in Inspector

Open Inspector on localhost. Go to **Agents** , then **Context**. The values you publish with `useAgentContext` appear here.

More detail: [Inspector](https://docs.copilotkit.ai/google-adk/inspector).

## What is this?#

Sometimes you want the agent to _know_ something about the current UI, like the logged-in user, the current page, or a recent activity log, but you don't want the agent to be able to modify it. That's what `useAgentContext` is for: a one-way **UI → agent** channel for read-only context.

Unlike full shared state (where the agent can call tools that mutate the state back to the UI), `useAgentContext` values are pure inputs. The agent sees them on every turn via the runtime's context injection, but it has no setter and no tool to write them back.

## When should I use this?#

Reach for `useAgentContext` instead of full shared state when:

  * The value is **UI-owned** and has no meaning to the agent beyond "what the user is looking at right now".
  * The agent should read but never write (user identity, feature flags, selected record, scroll position).
  * You want the value to automatically unregister on unmount (e.g. the "current record" context disappears when you leave the page).



Think of it as "props for the agent".

## How it works in code#

### Install the ADK + AG-UI bridge
    
    
    pip install ag-ui-adk

### Read CopilotKit context before each model call

The adapter copies the AG-UI request's `context` list into ADK session state at `CONTEXT_STATE_KEY` (the public constant for `"_ag_ui_context"`). Read it from an instruction provider's `ctx.state`, a callback's `callback_context.state`, or a tool's `tool_context.state`.

Each entry is a dictionary with `description` and `value` strings. Object and array values registered with `useAgentContext` arrive as JSON strings; use `json.loads(entry["value"])` when you need structured data.

An instruction provider can include the context in the model's prompt. The fully defined callback preserves the Gemini termination safeguard without stopping partial responses or pending tool calls:
    
    
    from ag_ui_adk import AGUIToolset, CONTEXT_STATE_KEY
    from google.adk.agents import LlmAgent
    from google.adk.agents.readonly_context import ReadonlyContext
    from google.adk.agents.callback_context import CallbackContext
    from google.adk.models.llm_response import LlmResponse
    
    def stop_on_terminal_text(
        callback_context: CallbackContext, llm_response: LlmResponse
    ) -> None:
        content = llm_response.content
        if llm_response.partial or not content or content.role != "model":
            return
        finish_reason = llm_response.finish_reason
        if getattr(finish_reason, "name", finish_reason) != "STOP":
            return
        parts = content.parts or []
        if not any(part.text for part in parts) or any(part.function_call for part in parts):
            return
        # ADK's invocation context is private; tolerate SDK changes.
        invocation = getattr(callback_context, "_invocation_context", None)
        if invocation is not None:
            try:
                invocation.end_invocation = True
            except AttributeError:
                pass
    
    def instructions(ctx: ReadonlyContext) -> str:
        entries = ctx.state.get(CONTEXT_STATE_KEY, [])
        context = "\n".join(
            f"{entry['description']}: {entry['value']}" for entry in entries
        )
        return (
            "Help the user using the following read-only application context.\n"
            + context
        )
    
    agent = LlmAgent(
        name="assistant",
        model="gemini-3.1-flash-lite",
        instruction=instructions,
        tools=[AGUIToolset()],
        after_model_callback=stop_on_terminal_text,
    )

`AGUIToolset()` exposes frontend tools; it does not automatically add context to the model's instructions. The instruction provider above performs that step. Expose this agent through your `ADKAgent` endpoint.

Call `useAgentContext({ description, value })` once per value you want to publish. Each call registers a dynamic context entry with the runtime that is:

  * Refreshed whenever `value` changes (React re-renders).
  * Automatically removed when the component unmounts.
  * Surfaced to the agent via the backend's `CopilotKitMiddleware`, which threads the entries into the model's message history on every turn.



page.tsx
    
    
      useAgentContext({    description: "The currently logged-in user's display name",    value: userName,  });  useAgentContext({    description: "The user's IANA timezone (used when mentioning times)",    value: userTimezone,  });  useAgentContext({    description: "The user's recent activity in the app, newest first",    value: recentActivity,  });

The `description` is important: it's a short human-readable label the agent sees alongside the value, so it knows what to do with it. Treat it like a parameter docstring.

## Wire it to your own state#

`useAgentContext` doesn't care where the value comes from: local state, a React Context, Redux, a query cache, anything. The only requirement is that the identity of the value is stable enough for React to avoid a render loop. In the demo we use a handful of `useState` hooks; in a real app these would likely come from an auth provider, a router hook, and your domain state stores.

page.tsx
    
    
    import React, { useState } from "react";import {  CopilotKit,  CopilotPopup,  useAgentContext,} from "@copilotkit/react-core/v2";import { ACTIVITIES, DemoLayout } from "./demo-layout";import { useReadonlyStateAgentContextSuggestions } from "./suggestions";export default function ReadonlyStateAgentContextDemo() {  return (    <CopilotKit      runtimeUrl="/api/copilotkit"      agent="readonly-state-agent-context"    >      <DemoContent />      <CopilotPopup        agentId="readonly-state-agent-context"        defaultOpen={true}        labels={{ chatInputPlaceholder: "Ask about your context..." }}      />    </CopilotKit>  );}function DemoContent() {  const [userName, setUserName] = useState("Atai");  const [userTimezone, setUserTimezone] = useState("America/Los_Angeles");  const [recentActivity, setRecentActivity] = useState<string[]>([    ACTIVITIES[0],    ACTIVITIES[2],  ]);

## Read-only, by design#

Because the agent never sees a setter or a mutation tool for these values, there's no way for a confused LLM to "update" them. That makes `useAgentContext` the right tool whenever the value in question is an input, not a field: the "context object passed to the agent on every turn", rather than "shared workspace you both edit".

When you need both reads _and_ writes, you want full **[shared state](https://docs.copilotkit.ai/google-adk/shared-state)** instead.

## Related#

  * **[Shared State (overview)](https://docs.copilotkit.ai/google-adk/shared-state)** — bidirectional reads + writes.
  * **[State streaming](https://docs.copilotkit.ai/google-adk/shared-state/streaming)** — stream agent-written state back to the UI during a run.


