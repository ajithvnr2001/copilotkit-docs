---
url: https://docs.copilotkit.ai/crewai-crews/generative-ui/reasoning/
title: Reasoning
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:57:05.002874+00:00
---

# Reasoning

> Source: https://docs.copilotkit.ai/crewai-crews/generative-ui/reasoning/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)[Build Generative UI](https://docs.copilotkit.ai/crewai-crews/generative-ui)

# Reasoning

Surface the agent's thinking chain in the chat — default or fully custom.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

reasoning_flow.py

page.tsx

reasoning-block.tsx
    
    
    """Native CrewAI Flow for reasoning-display demos.The CrewAI bridge translates the OpenAI Responses API's reasoning summary andanswer stream into AG-UI reasoning and text lifecycles. This Flow deliberatelyemits no protocol events itself."""from __future__ import annotationsimport osimport uuidfrom crewai.flow.flow import Flow, startfrom ag_ui_crewai import (    CopilotKitState,    copilotkit_responses,    copilotkit_stream,)from agents.responses_reasoning import ResponsesReasoningCaptureSYSTEM_PROMPT = (    "You are a helpful assistant. Use private reasoning and expose only a "    "safe high-level rationale before a concise answer. If the user asks to "    "show reasoning step by step without giving a concrete problem, compare "    "train and car travel for a 300 km trip, summarize the decision factors, "    "and recommend one. Never reveal hidden chain-of-thought.")REASONING_MODEL = os.environ.get("OPENAI_REASONING_MODEL", "gpt-5.4")class ReasoningFlow(Flow[CopilotKitState]):    """Stream native model reasoning and the final answer through AG-UI."""    @start()    async def chat(self) -> None:        captured = ResponsesReasoningCapture(            await copilotkit_responses(                model=f"openai/{REASONING_MODEL}",                messages=[                    {"role": "system", "content": SYSTEM_PROMPT},                    *[                        message                        for message in self.state.messages                        if not (                            isinstance(message, dict)                            and message.get("role") == "reasoning"                        )                    ],                ],                reasoning={"effort": "medium", "summary": "detailed"},            )        )        response = await copilotkit_stream(captured)        reasoning = "".join(captured.reasoning_parts)        if reasoning:            self.state.messages.append(                {"id": str(uuid.uuid4()), "role": "reasoning", "content": reasoning}            )        self.state.messages.append(response.choices[0].message)reasoning_flow = ReasoningFlow()

## What is this?#

Some models (OpenAI's `o1`, `o3`, and `o4-mini`, Anthropic's thinking variants) emit **reasoning tokens** , internal chain-of-thought traces that explain how the model is working toward its answer. CopilotKit surfaces these as first-class messages: when a `REASONING_MESSAGE_*` event arrives from the agent, the chat renders it inline so the user can follow the agent's thinking.

Reasoning isn't a custom-renderer plumb-in; it's a dedicated message type on the chat view. You can either accept the built-in rendering or override the `reasoningMessage` slot with your own component.

## When should I use this?#

Expose reasoning in the UI when you want to:

  * Give users real-time insight into the agent's thought process
  * Show progress on long or multi-step problems
  * Debug prompt behavior during development
  * Brand the reasoning card to match the rest of your product



## Default reasoning rendering (zero-config)#

Out of the box, reasoning events render inside CopilotKit's built-in `CopilotChatReasoningMessage` card:

  * A **"Thinking…"** label with a pulsing indicator while the model reasons.
  * Auto-expanded content so users can follow the chain of thought live.
  * Collapses to **"Thought for X seconds"** once reasoning finishes, with a chevron to re-expand.
  * Reasoning text rendered as Markdown.



No configuration is needed; if your model emits reasoning tokens, the card appears automatically:

page.tsx
    
    
    const AGENT_ID = "reasoning-default";export default function ReasoningDefaultDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningDefaultSuggestions();  return <CopilotChat agentId={AGENT_ID} className="h-full rounded-2xl" />;}

Here's what the built-in card looks like while the model thinks through a multi-step problem:

DemoCode

reasoning_flow.py

page.tsx

suggestions.ts
    
    
    """Native CrewAI Flow for reasoning-display demos.The CrewAI bridge translates the OpenAI Responses API's reasoning summary andanswer stream into AG-UI reasoning and text lifecycles. This Flow deliberatelyemits no protocol events itself."""from __future__ import annotationsimport osimport uuidfrom crewai.flow.flow import Flow, startfrom ag_ui_crewai import (    CopilotKitState,    copilotkit_responses,    copilotkit_stream,)from agents.responses_reasoning import ResponsesReasoningCaptureSYSTEM_PROMPT = (    "You are a helpful assistant. Use private reasoning and expose only a "    "safe high-level rationale before a concise answer. If the user asks to "    "show reasoning step by step without giving a concrete problem, compare "    "train and car travel for a 300 km trip, summarize the decision factors, "    "and recommend one. Never reveal hidden chain-of-thought.")REASONING_MODEL = os.environ.get("OPENAI_REASONING_MODEL", "gpt-5.4")class ReasoningFlow(Flow[CopilotKitState]):    """Stream native model reasoning and the final answer through AG-UI."""    @start()    async def chat(self) -> None:        captured = ResponsesReasoningCapture(            await copilotkit_responses(                model=f"openai/{REASONING_MODEL}",                messages=[                    {"role": "system", "content": SYSTEM_PROMPT},                    *[                        message                        for message in self.state.messages                        if not (                            isinstance(message, dict)                            and message.get("role") == "reasoning"                        )                    ],                ],                reasoning={"effort": "medium", "summary": "detailed"},            )        )        response = await copilotkit_stream(captured)        reasoning = "".join(captured.reasoning_parts)        if reasoning:            self.state.messages.append(                {"id": str(uuid.uuid4()), "role": "reasoning", "content": reasoning}            )        self.state.messages.append(response.choices[0].message)reasoning_flow = ReasoningFlow()

## Custom reasoning rendering#

For full control over the reasoning card, pass a component to the `reasoningMessage` slot on `messageView`. Your component receives the `ReasoningMessage` object (`.content` holds the streaming text), the full `messages` list, and `isRunning`, enough to decide whether this block is still streaming and whether it's the active trailing message:

page.tsxreasoning-block.tsx
    
    
    const AGENT_ID = "reasoning-custom";export default function ReasoningCustomDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent={AGENT_ID}>      <div className="flex justify-center items-center h-screen w-full">        <div className="h-full w-full max-w-4xl">          <Chat />        </div>      </div>    </CopilotKit>  );}function Chat() {  useReasoningCustomSuggestions();  return (    <CopilotChat      agentId={AGENT_ID}      className="h-full rounded-2xl"      messageView={{        reasoningMessage:          ReasoningBlock as unknown as typeof CopilotChatReasoningMessage,      }}    />  );}
    
    
    "use client";// Custom `reasoningMessage` slot renderer.//// Receives the `ReasoningMessage` plus (optionally) the full message list and// the running state from the slot system. Renders the content inline with a// visibly tagged amber banner so the user can always see the agent's thinking// chain — this is the focal UI of the demo.import React from "react";import type { ReasoningMessage, Message } from "@ag-ui/core";export function ReasoningBlock({  message,  messages,  isRunning,}: {  message: ReasoningMessage;  messages?: Message[];  isRunning?: boolean;}) {  const isLatest = messages?.[messages.length - 1]?.id === message.id;  const isStreaming = !!(isRunning && isLatest);  const hasContent = !!(message.content && message.content.length > 0);  return (    <div      data-testid="reasoning-block"      className="my-2 rounded-xl border border-[#DBDBE5] bg-[#BEC2FF1A] px-3.5 py-2.5 text-sm"    >      <div className="flex items-center gap-2 font-medium text-[#010507]">        <span className="inline-block rounded-full border border-[#BEC2FF] bg-white px-2 py-0.5 text-[10px] uppercase tracking-[0.14em] text-[#57575B]">          Reasoning        </span>        <span className="text-[#57575B]">          {isStreaming ? "Thinking…" : hasContent ? "Agent reasoning" : "…"}        </span>      </div>      {hasContent && (        <div className="mt-1.5 whitespace-pre-wrap italic text-[#57575B]">          {message.content}        </div>      )}    </div>  );}

The `ReasoningBlock` (imported above) renders the reasoning as an amber-tagged inline banner, intentionally louder than the default card so the thinking chain is the focal UI of the demo. Swap in your own component to match your product's tone.

The `messageView.reasoningMessage` slot accepts either a full component (as shown) or a sub-slot object like `{ header, contentView, toggle }` if you just want to tweak parts of the default card. See the reference docs for sub-slot props.
