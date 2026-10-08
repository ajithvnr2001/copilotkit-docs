---
url: https://docs.copilotkit.ai/langgraph-typescript/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:10:04.889586+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/langgraph-typescript/agent-config/

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

On this page

[LangGraph (TypeScript)](https://docs.copilotkit.ai/langgraph-typescript)

# Agent Config

Forward typed configuration from your UI into the agent's reasoning loop.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

agent-config.ts

page.tsx

config-card.tsx

use-agent-config.ts

config-types.ts

route.ts
    
    
    /** * LangGraph TypeScript agent backing the Agent Config Object demo. * * Reads three frontend-published context values — tone, expertise, * responseLength — from ``state.copilotkit.context`` and builds its system * prompt dynamically per turn. * * The frontend uses `useAgentContext` to publish the config object on each * render. This graph reads the latest matching context entry with defensive * defaults (unknown / missing values fall back to the defaults) and composes * the system prompt from three small rulebooks before invoking the model. */import { makeChatOpenAI } from "./openai-headers";import type { RunnableConfig } from "@langchain/core/runnables";import type { AIMessage } from "@langchain/core/messages";import { SystemMessage } from "@langchain/core/messages";import {  MemorySaver,  START,  StateGraph,  Annotation,} from "@langchain/langgraph";import { ChatOpenAI } from "@langchain/openai";import { CopilotKitStateAnnotation } from "@copilotkit/sdk-js/langgraph";type Tone = "professional" | "casual" | "enthusiastic";type Expertise = "beginner" | "intermediate" | "expert";type ResponseLength = "concise" | "detailed";const DEFAULT_TONE: Tone = "professional";const DEFAULT_EXPERTISE: Expertise = "intermediate";const DEFAULT_RESPONSE_LENGTH: ResponseLength = "concise";const VALID_TONES = new Set<string>(["professional", "casual", "enthusiastic"]);const VALID_EXPERTISE = new Set<string>(["beginner", "intermediate", "expert"]);const VALID_RESPONSE_LENGTHS = new Set<string>(["concise", "detailed"]);interface ResolvedProps {  tone: Tone;  expertise: Expertise;  responseLength: ResponseLength;}const AgentStateAnnotation = Annotation.Root({  ...CopilotKitStateAnnotation.spec,});type AgentState = typeof AgentStateAnnotation.State;function isRecord(value: unknown): value is Record<string, unknown> {  return typeof value === "object" && value !== null && !Array.isArray(value);}function containsConfigKeys(value: Record<string, unknown>): boolean {  return "tone" in value || "expertise" in value || "responseLength" in value;}function extractConfigContext(context: unknown): Record<string, unknown> {  if (typeof context === "string") {    try {      return extractConfigContext(JSON.parse(context));    } catch {      return {};    }  }  if (Array.isArray(context)) {    for (const entry of [...context].toReversed()) {      const extracted = extractConfigContext(entry);      if (containsConfigKeys(extracted)) return extracted;    }    return {};  }  if (!isRecord(context)) return {};  const value = context.value;  if (typeof value === "string") {    const parsed = extractConfigContext(value);    if (containsConfigKeys(parsed)) return parsed;  }  if (isRecord(value) && containsConfigKeys(value)) return value;  return containsConfigKeys(context) ? context : {};}function readForwardedProperties(  config: RunnableConfig | undefined,): Record<string, unknown> {  const configurable =    (config?.configurable as Record<string, unknown> | undefined) ?? {};  return (configurable.properties as Record<string, unknown> | undefined) ?? {};}function readConfig(state: AgentState, config: RunnableConfig): ResolvedProps {  const contextConfig = extractConfigContext(state.copilotkit?.context);  const properties = containsConfigKeys(contextConfig)    ? contextConfig    : readForwardedProperties(config);  const toneRaw = properties.tone;  const expertiseRaw = properties.expertise;  const responseLengthRaw = properties.responseLength;  const tone =    typeof toneRaw === "string" && VALID_TONES.has(toneRaw)      ? (toneRaw as Tone)      : DEFAULT_TONE;  const expertise =    typeof expertiseRaw === "string" && VALID_EXPERTISE.has(expertiseRaw)      ? (expertiseRaw as Expertise)      : DEFAULT_EXPERTISE;  const responseLength =    typeof responseLengthRaw === "string" &&    VALID_RESPONSE_LENGTHS.has(responseLengthRaw)      ? (responseLengthRaw as ResponseLength)      : DEFAULT_RESPONSE_LENGTH;  return { tone, expertise, responseLength };}const TONE_RULES: Record<Tone, string> = {  professional: "Use neutral, precise language. No emoji. Short sentences.",  casual:    "Use friendly, conversational language. Contractions OK. Light humor welcome.",  enthusiastic:    "Use upbeat, energetic language. Exclamation points OK. Emoji OK.",};const EXPERTISE_RULES: Record<Expertise, string> = {  beginner: "Assume no prior knowledge. Define jargon. Use analogies.",  intermediate:    "Assume common terms are understood; explain specialized terms.",  expert: "Assume technical fluency. Use precise terminology. Skip basics.",};const LENGTH_RULES: Record<ResponseLength, string> = {  concise: "Respond in 1-3 sentences.",  detailed: "Respond in multiple paragraphs with examples where relevant.",};function buildSystemPrompt(props: ResolvedProps): string {  return [    "You are a helpful assistant.",    "",    `Tone: ${TONE_RULES[props.tone]}`,    `Expertise level: ${EXPERTISE_RULES[props.expertise]}`,    `Response length: ${LENGTH_RULES[props.responseLength]}`,  ].join("\n");}async function runChatNode(  state: AgentState,  config: RunnableConfig,  model: ChatOpenAI,) {  const props = readConfig(state, config);  const systemPrompt = buildSystemPrompt(props);  const response = (await model.invoke(    [new SystemMessage({ content: systemPrompt }), ...state.messages],    config,  )) as AIMessage;  return { messages: response };}async function chatNode(state: AgentState, config: RunnableConfig) {  return runChatNode(    state,    config,    new ChatOpenAI({ model: "gpt-5-mini", temperature: 0.4 }),  );}function compileGraph(node: typeof chatNode) {  return new StateGraph(AgentStateAnnotation)    .addNode("chat_node", node)    .addEdge(START, "chat_node")    .addEdge("chat_node", "__end__")    .compile({ checkpointer: new MemorySaver() });}export const graph = compileGraph(chatNode);// The LangGraph CLI targets this export so showcase probes retain inbound// x-* header forwarding; the public `graph` above stays copy-pasteable.async function chatNodeWithHeaders(state: AgentState, config: RunnableConfig) {  return runChatNode(    state,    config,    makeChatOpenAI(config, { model: "gpt-5-mini", temperature: 0.4 }),  );}export const showcaseGraph = compileGraph(chatNodeWithHeaders);

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/langgraph-typescript/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

### Install the CopilotKit LangGraph SDK
    
    
    npm install @copilotkit/sdk-js

### Wire CopilotKit state into your graph

Agent config flows from the UI through `useAgentContext` and arrives on `state.copilotkit.context`. Use `CopilotKitStateAnnotation` to expose that channel — your chat node reads it to assemble the system prompt on every turn.

agent-config.ts
    
    
    import type { RunnableConfig } from "@langchain/core/runnables";
    import type { AIMessage } from "@langchain/core/messages";
    import { SystemMessage } from "@langchain/core/messages";
    import {
      MemorySaver,
      START,
      StateGraph,
      Annotation,
    } from "@langchain/langgraph";
    import { ChatOpenAI } from "@langchain/openai";
    import { CopilotKitStateAnnotation } from "@copilotkit/sdk-js/langgraph";
    
    type Tone = "professional" | "casual" | "enthusiastic";
    type Expertise = "beginner" | "intermediate" | "expert";
    type ResponseLength = "concise" | "detailed";
    
    const DEFAULT_TONE: Tone = "professional";
    const DEFAULT_EXPERTISE: Expertise = "intermediate";
    const DEFAULT_RESPONSE_LENGTH: ResponseLength = "concise";
    
    const VALID_TONES = new Set<string>(["professional", "casual", "enthusiastic"]);
    const VALID_EXPERTISE = new Set<string>(["beginner", "intermediate", "expert"]);
    const VALID_RESPONSE_LENGTHS = new Set<string>(["concise", "detailed"]);
    
    interface ResolvedProps {
      tone: Tone;
      expertise: Expertise;
      responseLength: ResponseLength;
    }
    
    const AgentStateAnnotation = Annotation.Root({
      ...CopilotKitStateAnnotation.spec,
    });
    
    type AgentState = typeof AgentStateAnnotation.State;
    
    function isRecord(value: unknown): value is Record<string, unknown> {
      return typeof value === "object" && value !== null && !Array.isArray(value);
    }
    
    function containsConfigKeys(value: Record<string, unknown>): boolean {
      return "tone" in value || "expertise" in value || "responseLength" in value;
    }
    
    function extractConfigContext(context: unknown): Record<string, unknown> {
      if (typeof context === "string") {
        try {
          return extractConfigContext(JSON.parse(context));
        } catch {
          return {};
        }
      }
    
      if (Array.isArray(context)) {
        for (const entry of [...context].toReversed()) {
          const extracted = extractConfigContext(entry);
          if (containsConfigKeys(extracted)) return extracted;
        }
        return {};
      }
    
      if (!isRecord(context)) return {};
      const value = context.value;
      if (typeof value === "string") {
        const parsed = extractConfigContext(value);
        if (containsConfigKeys(parsed)) return parsed;
      }
      if (isRecord(value) && containsConfigKeys(value)) return value;
      return containsConfigKeys(context) ? context : {};
    }
    
    function readForwardedProperties(
      config: RunnableConfig | undefined,
    ): Record<string, unknown> {
      const configurable =
        (config?.configurable as Record<string, unknown> | undefined) ?? {};
      return (configurable.properties as Record<string, unknown> | undefined) ?? {};
    }
    
    function readConfig(state: AgentState, config: RunnableConfig): ResolvedProps {
      const contextConfig = extractConfigContext(state.copilotkit?.context);
      const properties = containsConfigKeys(contextConfig)
        ? contextConfig
        : readForwardedProperties(config);
    
      const toneRaw = properties.tone;
      const expertiseRaw = properties.expertise;
      const responseLengthRaw = properties.responseLength;
    
      const tone =
        typeof toneRaw === "string" && VALID_TONES.has(toneRaw)
          ? (toneRaw as Tone)
          : DEFAULT_TONE;
      const expertise =
        typeof expertiseRaw === "string" && VALID_EXPERTISE.has(expertiseRaw)
          ? (expertiseRaw as Expertise)
          : DEFAULT_EXPERTISE;
      const responseLength =
        typeof responseLengthRaw === "string" &&
        VALID_RESPONSE_LENGTHS.has(responseLengthRaw)
          ? (responseLengthRaw as ResponseLength)
          : DEFAULT_RESPONSE_LENGTH;
    
      return { tone, expertise, responseLength };
    }
    
    const TONE_RULES: Record<Tone, string> = {
      professional: "Use neutral, precise language. No emoji. Short sentences.",
      casual:
        "Use friendly, conversational language. Contractions OK. Light humor welcome.",
      enthusiastic:
        "Use upbeat, energetic language. Exclamation points OK. Emoji OK.",
    };
    
    const EXPERTISE_RULES: Record<Expertise, string> = {
      beginner: "Assume no prior knowledge. Define jargon. Use analogies.",
      intermediate:
        "Assume common terms are understood; explain specialized terms.",
      expert: "Assume technical fluency. Use precise terminology. Skip basics.",
    };
    
    const LENGTH_RULES: Record<ResponseLength, string> = {
      concise: "Respond in 1-3 sentences.",
      detailed: "Respond in multiple paragraphs with examples where relevant.",
    };
    
    function buildSystemPrompt(props: ResolvedProps): string {
      return [
        "You are a helpful assistant.",
        "",
        `Tone: ${TONE_RULES[props.tone]}`,
        `Expertise level: ${EXPERTISE_RULES[props.expertise]}`,
        `Response length: ${LENGTH_RULES[props.responseLength]}`,
      ].join("\n");
    }
    
    async function runChatNode(
      state: AgentState,
      config: RunnableConfig,
      model: ChatOpenAI,
    ) {
      const props = readConfig(state, config);
      const systemPrompt = buildSystemPrompt(props);
    
      const response = (await model.invoke(
        [new SystemMessage({ content: systemPrompt }), ...state.messages],
        config,
      )) as AIMessage;
    
      return { messages: response };
    }
    
    async function chatNode(state: AgentState, config: RunnableConfig) {
      return runChatNode(
        state,
        config,
        new ChatOpenAI({ model: "gpt-5-mini", temperature: 0.4 }),
      );
    }
    
    function compileGraph(node: typeof chatNode) {
      return new StateGraph(AgentStateAnnotation)
        .addNode("chat_node", node)
        .addEdge(START, "chat_node")
        .addEdge("chat_node", "__end__")
        .compile({ checkpointer: new MemorySaver() });
    }
    
    export const graph = compileGraph(chatNode);

Agent config is a typed object the frontend owns and publishes to the agent as runtime context. The backend reads that context entry and turns it into a system prompt.

Hold the typed config in React state, then mirror every change into the agent through `useAgentContext`:

frontend/src/app/page.tsx — UI publishes the typed config
    
    
    function ConfigContextRelay({ config }: { config: AgentConfig }) {
      useAgentContext({
        description: "Agent response preferences",
        value: {
          tone: config.tone,
          expertise: config.expertise,
          responseLength: config.responseLength,
        },
      });
      return null;
    }

The framework setup above shows the exact backend bridge for the selected agent. In every framework, the flow is the same: read the latest valid context from the current run and use it to build the system prompt for that turn.

Backend flow
    
    
    config = latestValidConfig(currentRun.context)
    systemPrompt = buildSystemPrompt(config)
    model.invoke(systemPrompt, currentUserRequest)

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/langgraph-typescript/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
