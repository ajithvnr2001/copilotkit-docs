---
url: https://docs.copilotkit.ai/angular/multi-agent/subagents/
title: Sub-Agents
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:50:59.483038+00:00
---

# Sub-Agents

> Source: https://docs.copilotkit.ai/angular/multi-agent/subagents/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Agent capabilities

# Sub-Agents

Decompose work across multiple specialized agents with a visible delegation log.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

page.tsx

delegation-log.tsx

subagent-tools.ts

route.ts
    
    
    "use client";import React from "react";import {  CopilotKit,  useAgent,  UseAgentUpdate,  useRenderTool,} from "@copilotkit/react-core/v2";import { z } from "zod";import type { Delegation } from "./delegation-log";import { SubAgentActivityCard } from "./subagent-activity-card";import type { SubAgentToolStatus } from "./subagent-activity-card";import { DemoLayout } from "./demo-layout";import { inferActiveSubAgent } from "./active-subagent";import { useSubagentsSuggestions } from "./suggestions";interface SubagentsAgentState {  delegations?: Delegation[];}export default function SubagentsDemo() {  return (    <CopilotKit runtimeUrl="/api/copilotkit" agent="subagents">      <DemoContent />    </CopilotKit>  );}function DemoContent() {  const { agent } = useAgent({    agentId: "subagents",    updates: [UseAgentUpdate.OnStateChanged, UseAgentUpdate.OnRunStatusChanged],  });  useSubagentsSuggestions();  // Per-tool renderers — one for each sub-agent tool the supervisor can  // call. These surface "Researcher is running task Y" inline in the  // chat stream so the user can see what is happening without staring  // at the side panel. Each tool's `render` receives streaming  // parameters + the eventual result + a status that walks  // inProgress → executing → complete.  useRenderTool(    {      name: "research_agent",      parameters: z.object({ task: z.string() }),      render: ({ parameters, status, result }) => (        <SubAgentActivityCard          subAgent="research_agent"          task={parameters?.task}          status={status as SubAgentToolStatus}          result={typeof result === "string" ? result : undefined}        />      ),    },    [],  );  useRenderTool(    {      name: "writing_agent",      parameters: z.object({ task: z.string() }),      render: ({ parameters, status, result }) => (        <SubAgentActivityCard          subAgent="writing_agent"          task={parameters?.task}          status={status as SubAgentToolStatus}          result={typeof result === "string" ? result : undefined}        />      ),    },    [],  );  useRenderTool(    {      name: "critique_agent",      parameters: z.object({ task: z.string() }),      render: ({ parameters, status, result }) => (        <SubAgentActivityCard          subAgent="critique_agent"          task={parameters?.task}          status={status as SubAgentToolStatus}          result={typeof result === "string" ? result : undefined}        />      ),    },    [],  );  const agentState = agent.state as SubagentsAgentState | undefined;  const delegations = agentState?.delegations ?? [];  const isRunning = agent.isRunning;  const activeSubAgent = isRunning    ? inferActiveSubAgent(delegations, agent.messages)    : null;  return (    <DemoLayout      delegations={delegations}      isRunning={isRunning}      activeSubAgent={activeSubAgent}    />  );}

## What is this?#

Sub-agents are the canonical multi-agent pattern: a top-level **supervisor** LLM orchestrates one or more specialized **sub-agents** by exposing each of them as a tool. The supervisor decides what to delegate, the sub-agents do their narrow job, and their results flow back up to the supervisor's next step.

This is fundamentally the same shape as tool-calling, but each "tool" is itself a full-blown agent with its own system prompt and (often) its own tools, memory, and model.

## When should I use this?#

Reach for sub-agents when a task has distinct specialized sub-tasks that each benefit from their own focus:

  * **Research → Write → Critique** pipelines, where each stage needs a different system prompt and temperature.
  * **Router + specialists** , where one agent classifies the request and dispatches to the right expert.
  * **Divide-and-conquer** — any problem that fits cleanly into parallel or sequential sub-problems.



The example below uses the Research → Write → Critique shape as the canonical example.

## Setting up sub-agents#

Each sub-agent is an isolated agent call with its own model, system prompt, and optional tools. They don't share memory or tools with the supervisor; the supervisor only ever sees what the sub-agent returns.

subagent-tools.ts
    
    
    import { z } from "zod";import { chat, toolDefinition } from "@tanstack/ai";import { openaiText } from "@tanstack/ai-openai";// Custom fetch that injects ALS-bound inbound x-* headers (e.g.// x-aimock-context) onto every outbound OpenAI call. Required so aimock// can match fixtures by integration context. See ../header-forwarding.ts// for the full rationale; mirrors the Mastra precedent.import { forwardingFetch } from "../header-forwarding";// Each role becomes its own nested chat() with a dedicated system prompt.// They don't share memory or tools with the supervisor — the supervisor// only sees the role's return value via the delegate tool below.//// Tool names match the LangGraph Python reference agent (`subagents.py`)://   research_agent, writing_agent, critique_agent// This alignment is load-bearing: the D5 fixtures are recorded against// the LGP agent's tool names, and aimock matches on tool name.const subagentRoles = [  {    id: "research_agent",    systemPrompt:      "You are a research sub-agent. Given a topic, produce a concise " +      "bulleted list of 3-5 key facts. No preamble, no closing.",  },  {    id: "writing_agent",    systemPrompt:      "You are a writing sub-agent. Given a brief and optional source " +      "facts, produce a polished 1-paragraph draft. Be clear and " +      "concrete. No preamble.",  },  {    id: "critique_agent",    systemPrompt:      "You are an editorial critique sub-agent. Given a draft, give " +      "2-3 crisp, actionable critiques. No preamble.",  },] as const;

Keep sub-agent system prompts narrow and focused. The point of this pattern is that each one does one thing well. If a sub-agent needs to know the whole user context to do its job, that's a signal the boundary is wrong.

## Exposing sub-agents as tools#

The supervisor delegates by calling tools. Each delegation tool is a thin wrapper around a specialized agent call that:

  1. Runs the sub-agent on the supplied `task` string.
  2. Records the delegation into a `delegations` slot in shared agent state (so the UI can render a live log).
  3. Returns the sub-agent's final message as the tool result, which the supervisor sees on its next turn.



subagent-tools.ts
    
    
    import { z } from "zod";import { chat, toolDefinition } from "@tanstack/ai";import { openaiText } from "@tanstack/ai-openai";// Custom fetch that injects ALS-bound inbound x-* headers (e.g.// x-aimock-context) onto every outbound OpenAI call. Required so aimock// can match fixtures by integration context. See ../header-forwarding.ts// for the full rationale; mirrors the Mastra precedent.import { forwardingFetch } from "../header-forwarding";// Each role becomes its own nested chat() with a dedicated system prompt.// They don't share memory or tools with the supervisor — the supervisor// only sees the role's return value via the delegate tool below.//// Tool names match the LangGraph Python reference agent (`subagents.py`)://   research_agent, writing_agent, critique_agent// This alignment is load-bearing: the D5 fixtures are recorded against// the LGP agent's tool names, and aimock matches on tool name.const subagentRoles = [  {    id: "research_agent",    systemPrompt:      "You are a research sub-agent. Given a topic, produce a concise " +      "bulleted list of 3-5 key facts. No preamble, no closing.",  },  {    id: "writing_agent",    systemPrompt:      "You are a writing sub-agent. Given a brief and optional source " +      "facts, produce a polished 1-paragraph draft. Be clear and " +      "concrete. No preamble.",  },  {    id: "critique_agent",    systemPrompt:      "You are an editorial critique sub-agent. Given a draft, give " +      "2-3 crisp, actionable critiques. No preamble.",  },] as const;// Builder takes the parent run's AbortController so subagent `chat()` calls// abort with the parent. Constructing tools at module-import time leaves them// with their own fresh AbortController, which means a user cancel never reaches// the in-flight subagent call — orphan async work, billed tokens, hung// promises. Each parent run threads its controller through here.// Each `<role>_agent` tool wraps a nested chat() call with the// role's system prompt. The supervisor LLM "calls" these tools to// delegate work; each invocation runs the matching subagent and returns// its output for the supervisor's next step.// Cap the supervisor → critique sub-agent loop at a single iteration, matching// the reference's `_MAX_CRITIQUE_ITERATIONS`. Without it the supervisor LLM// occasionally re-calls `critique_agent` on the same draft, which shows up as// stacking 🧐 cards in the chat and duplicate rows in the delegation log. The// critic only adds value once per draft.const MAX_CRITIQUE_ITERATIONS = 1;export function buildSubagentTools(parentAbortController: AbortController) {  // Per-run counter. `buildSubagentTools` is already called once per run (so  // each run's nested chat() aborts with its parent), so a closure here is  // naturally run-scoped — module scope would leak the cap across requests.  let critiqueCalls = 0;  return subagentRoles.map((role) =>    toolDefinition({      name: role.id,      description: `Delegate a task to the ${role.id.replace(/_/g, " ")}.`,      inputSchema: z.object({        task: z          .string()          .describe(`Task description for the ${role.id.replace(/_/g, " ")}`),      }),    }).server(async ({ task }) => {      if (role.id === "critique_agent") {        critiqueCalls += 1;        if (critiqueCalls > MAX_CRITIQUE_ITERATIONS) {          // Return a no-op result rather than throwing: a throw would surface          // as a failed tool call and derail the supervisor's final summary.          return {            role: role.id,            text: "Critique already provided for this draft; skipping further review.",          };        }      }      const text = await chat({        adapter: openaiText("gpt-5.4", { fetch: forwardingFetch }),        messages: [{ role: "user", content: task }],        systemPrompts: [role.systemPrompt],        abortController: parentAbortController,        stream: false,      });      return { role: role.id, text };    }),  );}

This is where CopilotKit's shared-state channel earns its keep: the supervisor's tool calls mutate `delegations` as they happen, and the frontend renders every new entry live.

Give every delegation a stable `id` and merge new entries by that `id`. The client sends its copy of shared state back as run input on every run, so a slot that blindly appends whatever it receives — a LangGraph `Annotated[list, operator.add]` reducer, for example — concatenates the entries the client just echoed onto the ones the agent already has, and the log doubles when a thread is continued.

## Rendering a live delegation log#

On the frontend, the delegation log is a reactive render of the `delegations` slot.

Read the selected agent's state through `injectAgentStore`, derive the delegations with `computed`, and register one typed renderer for each sub-agent tool. The Angular Showcase uses this source:

agent-state-feature.component.ts
    
    
      private readonly agentStore = injectAgentStore(this.agentId);  protected readonly delegations = computed(() =>    readDelegations(this.agentStore().state()),  );  constructor() {    if (this.feature === "subagents") {      this.registerSubAgent("research_agent");      this.registerSubAgent("writing_agent");      this.registerSubAgent("critique_agent");    }  }  private registerSubAgent(name: SubAgentName): void {    registerRenderToolCall(subAgentRendererConfig(name));  }

The result: as the supervisor fans work out to its sub-agents, the log grows in real time, giving the user visibility into a process that would otherwise be a long opaque spinner.

## Related#

  * **[Shared State](https://docs.copilotkit.ai/angular/guides/shared-state)** — the channel that makes the delegation log live.
  * **[State streaming](https://docs.copilotkit.ai/angular/guides/shared-state)** — stream _individual_ sub-agent outputs token-by-token inside each log entry.


