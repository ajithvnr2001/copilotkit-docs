---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/headless-ui/
title: Headless UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:22.294744+00:00
---

# Headless UI

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/headless-ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Prebuilt Components

Custom Look and Feel

[CSS Customization](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/css)[Slots (Subcomponents)](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/slots)[Markdown Rendering](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/markdown)[Headless UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/headless-ui)[Reasoning Messages](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/reasoning-messages)

[Multimodal Attachments](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multimodal-attachments)[Voice](https://docs.copilotkit.ai/ms-agent-harness-dotnet/voice)[Reasoning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/reasoning)

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

[Sub-agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-harness-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-harness-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-harness-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Headless UI

BasicsChatCustom Look and Feel

# Headless UI

Build any UI — chat or not — on top of the CopilotKit primitives with zero UI opinions.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

Program.cs

page.tsx

message-list.tsx

use-rendered-messages.tsx

route.ts
    
    
    using System.ClientModel;using System.Net.Http;using System.Text.Json.Serialization;using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;using Microsoft.AspNetCore.Http.Json;using Microsoft.Extensions.Options;using OpenAI;var builder = WebApplication.CreateBuilder(args);builder.Services.ConfigureHttpJsonOptions(options =>{    // Beautiful-chat types (shipped) + the full-column Sales/Flight/parity types    // ported by the family slots. Both source-generated contexts are chained so    // every feature agent's tool I/O serializes through the fast path.    options.SerializerOptions.TypeInfoResolverChain.Add(BeautifulChatSerializerContext.Default);    options.SerializerOptions.TypeInfoResolverChain.Add(SalesAgentSerializerContext.Default);    // Serialize enum types as their member-name strings rather than numeric    // ordinals (matches the Framework column's wire format).    options.SerializerOptions.Converters.Add(new JsonStringEnumConverter());});builder.Services.AddAGUI();// STOPGAP: IHttpContextAccessor lets AimockHeaderPolicy read the current// request's forwarded x-* headers (stashed on HttpContext.Items by// AimockHeaderMiddleware) at outbound-LLM-call time. HttpContext flows across// the AG-UI SSE-pump ExecutionContext boundary, unlike a middleware-set// AsyncLocal. TODO(copilotkit-sdk-dotnet): migrate to SDK-level header propagation.builder.Services.AddHttpContextAccessor();var app = builder.Build();// STOPGAP: seed the static accessor the outbound header-forwarding policy reads// (the policy is created without DI, mirroring CvDiag.Logger).AimockHeaderPolicy.HttpContextAccessor = app.Services.GetRequiredService<IHttpContextAccessor>();// Forward D5/aimock x-* headers from incoming AG-UI requests to outgoing// OpenAI calls until the .NET SDK owns this propagation centrally.app.UseMiddleware<AimockHeaderMiddleware>();// CVDIAG: backend flap-observability emitter (plan unit L1-F; spec §3). OFF by// default (CVDIAG_BACKEND_EMITTER=on to arm). Seed the static singleton the// outbound LLM policy reads (created without DI), then register the// request-pipeline instrumentation AFTER AimockHeaderMiddleware so the forwarded// x-* correlation headers are already captured for this request.CvdiagBackend.Instance = new CvdiagBackend();app.UseMiddleware<CvdiagInstrumentationMiddleware>();var loggerFactory = app.Services.GetRequiredService<ILoggerFactory>();// CVDIAG: seed the static logger used by AimockHeaderPolicy (created without DI)// to emit the outbound-LLM header-forwarding breadcrumb.CvDiag.Logger = loggerFactory.CreateLogger("CvDiag");var jsonOptions = app.Services.GetRequiredService<IOptions<JsonOptions>>().Value.SerializerOptions;// Single shared OpenAIClient for the whole column. Built once via the harness// ApiKeyResolver (env OPENAI_API_KEY -> config OPENAI_API_KEY -> GitHubToken,// fail-fast for non-mock endpoints) so EVERY feature agent hits the same// upstream with the same credential resolution — no per-feature GitHubToken// dance. Threaded into each feature factory's ctor. See the W0 contract §1.var openAiClient = CreateOpenAiClient(builder.Configuration, loggerFactory.CreateLogger("Program"));// ── Root agentic-chat agent (the Sales pipeline agent) ──────────────────────// agentic-chat, chat-slots, chat-customization-css, prebuilt-{sidebar,popup},// frontend-tools{,-async}, headless-simple, shared-state-read, and the two// tool-rendering catch-all demos all proxy to this root agent via the shared// Next.js `copilotkit/` runtime route.var salesFactory = new SalesAgentFactory(builder.Configuration, openAiClient, jsonOptions, loggerFactory);app.MapAGUI("/", salesFactory.CreateSalesAgent());// ── D5 parity agents (one factory hosts the parity-feature surface) ─────────var d5ParityFactory = new D5ParityAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/headless-complete", d5ParityFactory.CreateHeadlessCompleteAgent());app.MapAGUI("/voice", d5ParityFactory.CreateVoiceAgent());app.MapAGUI("/gen-ui-agent", d5ParityFactory.CreateGenUiAgent());app.MapAGUI("/gen-ui-tool-based", d5ParityFactory.CreateGenUiToolBasedAgent());app.MapAGUI("/shared-state-streaming", d5ParityFactory.CreateSharedStateStreamingAgent());app.MapAGUI("/readonly-state-agent-context", d5ParityFactory.CreateReadonlyStateAgentContext());app.MapAGUI("/tool-rendering", d5ParityFactory.CreateToolRenderingAgent(reasoning: false));app.MapAGUI("/tool-rendering-reasoning-chain", d5ParityFactory.CreateToolRenderingAgent(reasoning: true));// ── Interrupt agent (NOT-SUPPORTED, wired for parity) ───────────────────────// gen-ui-interrupt and interrupt-headless share this single backend; the// differentiation is on the frontend (in-chat picker vs. headless button grid).// Marked not_supported in manifest.yaml (skipped-incapable) pending a// @copilotkit/react-core resume-path fix — wired here so the column is 1:1.var interruptFactory = new InterruptAgentFactory(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/interrupt-adapted", interruptFactory.CreateInterruptAgent());// ── Multimodal (raw MapPost — the AG-UI adapter rejects content arrays) ─────// Parses the request body directly and emits the small AG-UI SSE event subset// the chat UI needs for text streaming over a vision-capable chat client.app.MapPost("/multimodal", (HttpContext context) => MultimodalEndpoint.HandleAsync(    context,    salesFactory.CreateMultimodalChatClient(),    loggerFactory.CreateLogger("MultimodalEndpoint")));// ── Beautiful Chat flagship demo (shipped) ──────────────────────────────────var beautifulChatFactory = new BeautifulChatAgentFactory(    builder.Configuration,    openAiClient,    jsonOptions,    loggerFactory.CreateLogger<BeautifulChatAgentFactory>());app.MapAGUI("/beautiful-chat", beautifulChatFactory.Create());// ── Agent Config (wraps a neutral inner agent in AgentConfigAgent) ──────────app.MapAGUI("/agent-config", salesFactory.CreateAgentConfigAgent());// ── Reasoning (reasoning-default + reasoning-custom share this backend) ─────app.MapAGUI("/reasoning", salesFactory.CreateReasoningAgent());// ── Declarative Gen UI (A2UI canonical BYOC) ────────────────────────────────var declarativeGenUiAgent = new DeclarativeGenUiAgent(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/declarative-gen-ui", declarativeGenUiAgent.Create());// ── A2UI fixed-schema demo ──────────────────────────────────────────────────var a2uiFixedSchemaAgent = new A2uiFixedSchemaAgent(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/a2ui-fixed-schema", a2uiFixedSchemaAgent.Create());// ── Open Generative UI — basic + advanced ───────────────────────────────────var openGenUiFactory = new OpenGenUiAgentFactory(openAiClient);app.MapAGUI("/open-gen-ui", openGenUiFactory.CreateAgent());var openGenUiAdvancedFactory = new OpenGenUiAdvancedAgentFactory(openAiClient);app.MapAGUI("/open-gen-ui-advanced", openGenUiAdvancedFactory.CreateAgent());// ── BYOC demos (hashbrown + json-render) ────────────────────────────────────var byocHashbrownFactory = new ByocHashbrownAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/byoc-hashbrown", byocHashbrownFactory.CreateAgent());var byocJsonRenderFactory = new ByocJsonRenderAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/byoc-json-render", byocJsonRenderFactory.CreateAgent());// ── MCP Apps demo ───────────────────────────────────────────────────────────var mcpAppsFactory = new McpAppsAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/mcp-apps", mcpAppsFactory.CreateMcpAppsAgent());// ── In-app HITL demo (frontend tools + async HITL) ──────────────────────────var hitlInAppFactory = new HitlInAppAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/hitl-in-app", hitlInAppFactory.CreateHitlInAppAgent());// ── In-chat HITL demo (useHumanInTheLoop) ───────────────────────────────────var hitlInChatFactory = new HitlInChatAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/hitl-in-chat", hitlInChatFactory.CreateHitlInChatAgent());// ── Shared State (Read + Write) demo ────────────────────────────────────────var sharedStateReadWriteFactory = new SharedStateReadWriteAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/shared-state-read-write", sharedStateReadWriteFactory.CreateAgent());// ── Sub-Agents demo (supervisor delegates to research/writing/critique) ─────var subagentsFactory = new SubagentsAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/subagents", subagentsFactory.CreateAgent());app.MapGet("/health", () => Results.Ok(new { status = "ok" }));await app.RunAsync();static OpenAIClient CreateOpenAiClient(IConfiguration configuration, ILogger logger){    // Use the shared resolver so the primary OpenAI client and the secondary    // tool-calling HTTP client (A2uiSecondaryToolCaller) agree on which upstream    // endpoint to hit (see ApiKeyResolver for the env/config precedence and the    // non-mock fail-fast).    var endpoint = ApiKeyResolver.ResolveEndpoint(configuration);    var endpointEnv = Environment.GetEnvironmentVariable("OPENAI_BASE_URL");    var endpointConfig = configuration["OPENAI_BASE_URL"];    if (!string.IsNullOrEmpty(endpointEnv))    {        logger.LogInformation("Using OpenAI endpoint from OPENAI_BASE_URL env: {Endpoint}", endpoint);    }    else if (!string.IsNullOrEmpty(endpointConfig))    {        logger.LogInformation("Using OpenAI endpoint from configuration OPENAI_BASE_URL: {Endpoint}", endpoint);    }    else    {        logger.LogInformation("OPENAI_BASE_URL not set; using default OpenAI endpoint: {Endpoint}", endpoint);    }    var apiKey = ApiKeyResolver.ResolveApiKey(configuration, logger);    return new OpenAIClient(        new ApiKeyCredential(apiKey),        AimockHeaderPolicy.CreateOpenAIClientOptions(endpoint));}public class WeatherInfo{    [JsonPropertyName("temperature")]    public int Temperature { get; init; }    [JsonPropertyName("conditions")]    public string Conditions { get; init; } = string.Empty;    [JsonPropertyName("humidity")]    public int Humidity { get; init; }    [JsonPropertyName("wind_speed")]    public int WindSpeed { get; init; }    [JsonPropertyName("feels_like")]    public int FeelsLike { get; init; }    [JsonPropertyName("city")]    public string City { get; init; } = string.Empty;}public partial class Program { }[JsonSerializable(typeof(WeatherInfo))][JsonSerializable(typeof(BeautifulChatTodo))][JsonSerializable(typeof(List<BeautifulChatTodo>))][JsonSerializable(typeof(BeautifulChatFlight))][JsonSerializable(typeof(List<BeautifulChatFlight>))]internal partial class BeautifulChatSerializerContext : JsonSerializerContext{}

## What is this?#

A headless UI gives you **full control** over the chat experience. You bring your own components, layout, and styling while CopilotKit handles agent communication, message management, tool-call rendering, and streaming. No `<CopilotChat>`, no slot overrides, just your components composed on top of the low-level hooks.

## When should I use this?#

Use headless UI when:

  * The [slot system](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/slots) isn't enough: you need a completely different layout.
  * You're embedding chat into an existing UI with its own patterns.
  * You're building a **non-chat surface** that still talks to an agent (a dashboard, a canvas, an inspector) and want `useRenderToolCall` / `useRenderActivityMessage` on their own.
  * You want to render generative UI primitives outside of a chat entirely.



## The core hooks#

Three hooks power it, and they're the same ones `<CopilotChat>` uses internally.

  * `useAgent({ agentId })` — exposes the current conversation (`messages`, `isRunning`) and the run-state object.
  * `useCopilotKit()` — returns the runtime handle you call `runAgent({ agent })` on.
  * `useRenderToolCall()` — returns a function that paints any registered tool call inline.



## Minimal example#

Start with a hand-rolled message list and composer built from `useAgent` \+ `useCopilotKit`:

Missing snippet

Region `use-agent-simple` not found in `ms-agent-harness-dotnet::headless-simple`. Tag the relevant source lines with `// @region[use-agent-simple]` / `// @endregion[use-agent-simple]`.

The message list is a plain `.map()` over `agent.messages`: user messages render as right-aligned bubbles, assistant messages render streamed text plus inline tool calls via `renderToolCall({ toolCall })`:

Missing snippet

Region `message-list-simple` not found in `ms-agent-harness-dotnet::headless-simple`. Tag the relevant source lines with `// @region[message-list-simple]` / `// @endregion[message-list-simple]`.

No `<CopilotChat />`, no slots. The trade-off: you only get text and tool calls. Reasoning messages, activity messages, and custom before/after slots won't show up unless you wire them in yourself, which is exactly what the complete example covers.

## Complete example#

The `headless-complete` cell rebuilds the **full** generative-UI composition from the low-level hooks directly, without importing `<CopilotChatMessageView>`: text, tool calls, reasoning cards, A2UI + MCP Apps activity messages, and custom before/after message slots.

### The `useRenderedMessages` hook#

The cell's central piece is a hand-rolled `useRenderedMessages(messages, isRunning)` that returns the same flat list of messages, each augmented with a `renderedContent: ReactNode` field. This hook is a **manual recreation of what`<CopilotChatMessageView>` does**:

use-rendered-messages.tsx
    
    
    import React, { useMemo } from "react";import type {  Message,  AssistantMessage,  UserMessage,  ReasoningMessage,  ActivityMessage,  ToolMessage,} from "@ag-ui/core";import {  CopilotChatReasoningMessage,  useRenderToolCall,  useRenderActivityMessage,  useRenderCustomMessages,} from "@copilotkit/react-core/v2";/** * Manual per-message composition for the TRULY headless chat cell. * * This hook mirrors — line-for-line in spirit — the role-dispatch that happens * inside `renderMessageBlock` in the canonical primitive: * *   packages/react-core/src/v2/components/chat/CopilotChatMessageView.tsx:542-612 * * The point of this cell is to demonstrate that the FULL generative-UI weave * (assistant text + tool-call renders + reasoning + activity + custom before / * after slots) can be re-composed from the low-level hooks directly, without * importing `<CopilotChatMessageView>` or `<CopilotChatAssistantMessage>`. * Only the reasoning-message LEAF component is imported — it's a pure * presentational primitive, not a dispatcher. * * Return shape: the original messages, each augmented with a `renderedContent` * field that the parent list drops directly into a `<UserBubble>` or * `<AssistantBubble>` chrome wrapper. * * Text rendering: we intentionally use plain text (a `<div>` with * `whitespace-pre-wrap`) rather than a markdown pipeline. Rationale: the cell's * goal is to show what "truly headless" looks like — every piece of composition * lives in user code — so pulling in a markdown library here would re-hide * a chunk of formatting decisions behind an opaque black box. Apps that want * markdown can drop Streamdown / react-markdown in at this exact line. */export type RenderedMessage = Message & { renderedContent: React.ReactNode };export function useRenderedMessages(  messages: Message[],  isRunning: boolean,): RenderedMessage[] {  const renderToolCall = useRenderToolCall();  const { renderActivityMessage } = useRenderActivityMessage();  const renderCustomMessage = useRenderCustomMessages();  return useMemo(() => {    return messages.map((message): RenderedMessage => {      const renderedContent = renderMessageContent({        message,        messages,        isRunning,        renderToolCall,        renderActivityMessage,        renderCustomMessage,      });      return { ...message, renderedContent } as RenderedMessage;    });    // `renderToolCall`, `renderActivityMessage`, and `renderCustomMessage` are    // callbacks produced by their respective hooks; their identity turns over    // whenever the underlying registries / agent / config change, which is    // exactly when we want to recompute.  }, [    messages,    isRunning,    renderToolCall,    renderActivityMessage,    renderCustomMessage,  ]);}

Three low-level hooks feed it:

  * `useRenderToolCall()` — returns the renderer for any registered tool call (per-tool via `useRenderTool` / `useComponent`, plus the wildcard from `useDefaultRenderTool`).
  * `useRenderActivityMessage()` — renders A2UI + MCP Apps activity messages for the current agent scope.
  * `useRenderCustomMessages()` — invokes `renderCustomMessage` hooks registered against the active `CopilotChatConfigurationProvider`, emitting `"before"` and `"after"` slots around every message.



### Per-role dispatch#

The role-switch mirrors `CopilotChatMessageView`'s `renderMessageBlock` exactly: assistant bodies get text and tool calls, user bodies get their text content, reasoning messages go through the `<CopilotChatReasoningMessage>` leaf, and activity messages route through `renderActivityMessage`:

use-rendered-messages.tsx
    
    
      if (message.role === "assistant") {    body = renderAssistantBody({      message: message as AssistantMessage,      messages,      renderToolCall,    });  } else if (message.role === "user") {    body = renderUserBody(message as UserMessage);  } else if (message.role === "reasoning") {    body = (      <CopilotChatReasoningMessage        message={message as ReasoningMessage}        messages={messages}        isRunning={isRunning}      />    );  } else if (message.role === "activity") {    body = renderActivityMessage(message as ActivityMessage);  }

### Tool-call composition#

For each `toolCall` on an assistant message, we look up the sibling `tool`-role message (keyed by `toolCallId`) and hand both to `renderToolCall`:

use-rendered-messages.tsx
    
    
    function renderAssistantBody(args: {  message: AssistantMessage;  messages: Message[];  renderToolCall: ReturnType<typeof useRenderToolCall>;}): React.ReactNode {  const { message, messages, renderToolCall } = args;  const text = message.content ?? "";  const hasText = text.trim().length > 0;  const toolCalls = message.toolCalls ?? [];  return (    <>      {hasText && <div className="whitespace-pre-wrap break-words">{text}</div>}      {toolCalls.map((toolCall) => {        // Tool result lives on a sibling `tool`-role message keyed by toolCallId.        // Mirrors CopilotChatToolCallsView (react-core/v2/components/chat/CopilotChatToolCallsView.tsx).        const toolMessage = messages.find(          (m) => m.role === "tool" && m.toolCallId === toolCall.id,        ) as ToolMessage | undefined;        return (          <React.Fragment key={toolCall.id}>            {renderToolCall({ toolCall, toolMessage })}          </React.Fragment>        );      })}    </>  );}

### Bubble chrome#

The `UserBubble` and `AssistantBubble` components are **pure chrome** : they receive the pre-rendered node from `useRenderedMessages` and drop it into a styled container. No chat primitives are imported here:

message-list.tsx
    
    
    function UserBubble({ children }: { children: React.ReactNode }) {  return (    <div className="flex justify-end">      <div className="max-w-[75%] rounded-2xl rounded-br-sm bg-[#010507] text-white px-4 py-2 text-sm whitespace-pre-wrap break-words">        {children}      </div>    </div>  );}function AssistantBubble({ children }: { children: React.ReactNode }) {  if (isEmpty(children)) return null;  return (    <div className="flex justify-start">      <div className="max-w-[85%] flex flex-col gap-2">        <div className="rounded-2xl rounded-bl-sm bg-[#F0F0F4] text-[#010507] px-4 py-2 text-sm">          {children}        </div>      </div>    </div>  );}

## Next steps#

  * [Slots](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/slots) — less work than going fully headless, often enough.
  * [CSS customization](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/css) — when you just need to re-skin the defaults.



### On this page

What is this?When should I use this?The core hooksMinimal exampleComplete exampleThe useRenderedMessages hookPer-role dispatchTool-call compositionBubble chromeNext steps
