---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/prebuilt-components/popup/
title: CopilotPopup
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:54.991336+00:00
---

# CopilotPopup

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/prebuilt-components/popup/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Prebuilt Components

[CopilotChat](https://docs.copilotkit.ai/ms-agent-harness-dotnet/prebuilt-components/chat)[CopilotSidebar](https://docs.copilotkit.ai/ms-agent-harness-dotnet/prebuilt-components/sidebar)[CopilotPopup](https://docs.copilotkit.ai/ms-agent-harness-dotnet/prebuilt-components/popup)[Open, close, and feedback](https://docs.copilotkit.ai/ms-agent-harness-dotnet/prebuilt-components/chat-controls)

Custom Look and Feel

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

CopilotPopup

BasicsChatPrebuilt Components

# CopilotPopup

Floating chat bubble that toggles open an overlay chat window.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

Program.cs

page.tsx

route.ts
    
    
    using System.ClientModel;using System.Net.Http;using System.Text.Json.Serialization;using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;using Microsoft.AspNetCore.Http.Json;using Microsoft.Extensions.Options;using OpenAI;var builder = WebApplication.CreateBuilder(args);builder.Services.ConfigureHttpJsonOptions(options =>{    // Beautiful-chat types (shipped) + the full-column Sales/Flight/parity types    // ported by the family slots. Both source-generated contexts are chained so    // every feature agent's tool I/O serializes through the fast path.    options.SerializerOptions.TypeInfoResolverChain.Add(BeautifulChatSerializerContext.Default);    options.SerializerOptions.TypeInfoResolverChain.Add(SalesAgentSerializerContext.Default);    // Serialize enum types as their member-name strings rather than numeric    // ordinals (matches the Framework column's wire format).    options.SerializerOptions.Converters.Add(new JsonStringEnumConverter());});builder.Services.AddAGUI();// STOPGAP: IHttpContextAccessor lets AimockHeaderPolicy read the current// request's forwarded x-* headers (stashed on HttpContext.Items by// AimockHeaderMiddleware) at outbound-LLM-call time. HttpContext flows across// the AG-UI SSE-pump ExecutionContext boundary, unlike a middleware-set// AsyncLocal. TODO(copilotkit-sdk-dotnet): migrate to SDK-level header propagation.builder.Services.AddHttpContextAccessor();var app = builder.Build();// STOPGAP: seed the static accessor the outbound header-forwarding policy reads// (the policy is created without DI, mirroring CvDiag.Logger).AimockHeaderPolicy.HttpContextAccessor = app.Services.GetRequiredService<IHttpContextAccessor>();// Forward D5/aimock x-* headers from incoming AG-UI requests to outgoing// OpenAI calls until the .NET SDK owns this propagation centrally.app.UseMiddleware<AimockHeaderMiddleware>();// CVDIAG: backend flap-observability emitter (plan unit L1-F; spec §3). OFF by// default (CVDIAG_BACKEND_EMITTER=on to arm). Seed the static singleton the// outbound LLM policy reads (created without DI), then register the// request-pipeline instrumentation AFTER AimockHeaderMiddleware so the forwarded// x-* correlation headers are already captured for this request.CvdiagBackend.Instance = new CvdiagBackend();app.UseMiddleware<CvdiagInstrumentationMiddleware>();var loggerFactory = app.Services.GetRequiredService<ILoggerFactory>();// CVDIAG: seed the static logger used by AimockHeaderPolicy (created without DI)// to emit the outbound-LLM header-forwarding breadcrumb.CvDiag.Logger = loggerFactory.CreateLogger("CvDiag");var jsonOptions = app.Services.GetRequiredService<IOptions<JsonOptions>>().Value.SerializerOptions;// Single shared OpenAIClient for the whole column. Built once via the harness// ApiKeyResolver (env OPENAI_API_KEY -> config OPENAI_API_KEY -> GitHubToken,// fail-fast for non-mock endpoints) so EVERY feature agent hits the same// upstream with the same credential resolution — no per-feature GitHubToken// dance. Threaded into each feature factory's ctor. See the W0 contract §1.var openAiClient = CreateOpenAiClient(builder.Configuration, loggerFactory.CreateLogger("Program"));// ── Root agentic-chat agent (the Sales pipeline agent) ──────────────────────// agentic-chat, chat-slots, chat-customization-css, prebuilt-{sidebar,popup},// frontend-tools{,-async}, headless-simple, shared-state-read, and the two// tool-rendering catch-all demos all proxy to this root agent via the shared// Next.js `copilotkit/` runtime route.var salesFactory = new SalesAgentFactory(builder.Configuration, openAiClient, jsonOptions, loggerFactory);app.MapAGUI("/", salesFactory.CreateSalesAgent());// ── D5 parity agents (one factory hosts the parity-feature surface) ─────────var d5ParityFactory = new D5ParityAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/headless-complete", d5ParityFactory.CreateHeadlessCompleteAgent());app.MapAGUI("/voice", d5ParityFactory.CreateVoiceAgent());app.MapAGUI("/gen-ui-agent", d5ParityFactory.CreateGenUiAgent());app.MapAGUI("/gen-ui-tool-based", d5ParityFactory.CreateGenUiToolBasedAgent());app.MapAGUI("/shared-state-streaming", d5ParityFactory.CreateSharedStateStreamingAgent());app.MapAGUI("/readonly-state-agent-context", d5ParityFactory.CreateReadonlyStateAgentContext());app.MapAGUI("/tool-rendering", d5ParityFactory.CreateToolRenderingAgent(reasoning: false));app.MapAGUI("/tool-rendering-reasoning-chain", d5ParityFactory.CreateToolRenderingAgent(reasoning: true));// ── Interrupt agent (NOT-SUPPORTED, wired for parity) ───────────────────────// gen-ui-interrupt and interrupt-headless share this single backend; the// differentiation is on the frontend (in-chat picker vs. headless button grid).// Marked not_supported in manifest.yaml (skipped-incapable) pending a// @copilotkit/react-core resume-path fix — wired here so the column is 1:1.var interruptFactory = new InterruptAgentFactory(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/interrupt-adapted", interruptFactory.CreateInterruptAgent());// ── Multimodal (raw MapPost — the AG-UI adapter rejects content arrays) ─────// Parses the request body directly and emits the small AG-UI SSE event subset// the chat UI needs for text streaming over a vision-capable chat client.app.MapPost("/multimodal", (HttpContext context) => MultimodalEndpoint.HandleAsync(    context,    salesFactory.CreateMultimodalChatClient(),    loggerFactory.CreateLogger("MultimodalEndpoint")));// ── Beautiful Chat flagship demo (shipped) ──────────────────────────────────var beautifulChatFactory = new BeautifulChatAgentFactory(    builder.Configuration,    openAiClient,    jsonOptions,    loggerFactory.CreateLogger<BeautifulChatAgentFactory>());app.MapAGUI("/beautiful-chat", beautifulChatFactory.Create());// ── Agent Config (wraps a neutral inner agent in AgentConfigAgent) ──────────app.MapAGUI("/agent-config", salesFactory.CreateAgentConfigAgent());// ── Reasoning (reasoning-default + reasoning-custom share this backend) ─────app.MapAGUI("/reasoning", salesFactory.CreateReasoningAgent());// ── Declarative Gen UI (A2UI canonical BYOC) ────────────────────────────────var declarativeGenUiAgent = new DeclarativeGenUiAgent(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/declarative-gen-ui", declarativeGenUiAgent.Create());// ── A2UI fixed-schema demo ──────────────────────────────────────────────────var a2uiFixedSchemaAgent = new A2uiFixedSchemaAgent(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/a2ui-fixed-schema", a2uiFixedSchemaAgent.Create());// ── Open Generative UI — basic + advanced ───────────────────────────────────var openGenUiFactory = new OpenGenUiAgentFactory(openAiClient);app.MapAGUI("/open-gen-ui", openGenUiFactory.CreateAgent());var openGenUiAdvancedFactory = new OpenGenUiAdvancedAgentFactory(openAiClient);app.MapAGUI("/open-gen-ui-advanced", openGenUiAdvancedFactory.CreateAgent());// ── BYOC demos (hashbrown + json-render) ────────────────────────────────────var byocHashbrownFactory = new ByocHashbrownAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/byoc-hashbrown", byocHashbrownFactory.CreateAgent());var byocJsonRenderFactory = new ByocJsonRenderAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/byoc-json-render", byocJsonRenderFactory.CreateAgent());// ── MCP Apps demo ───────────────────────────────────────────────────────────var mcpAppsFactory = new McpAppsAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/mcp-apps", mcpAppsFactory.CreateMcpAppsAgent());// ── In-app HITL demo (frontend tools + async HITL) ──────────────────────────var hitlInAppFactory = new HitlInAppAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/hitl-in-app", hitlInAppFactory.CreateHitlInAppAgent());// ── In-chat HITL demo (useHumanInTheLoop) ───────────────────────────────────var hitlInChatFactory = new HitlInChatAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/hitl-in-chat", hitlInChatFactory.CreateHitlInChatAgent());// ── Shared State (Read + Write) demo ────────────────────────────────────────var sharedStateReadWriteFactory = new SharedStateReadWriteAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/shared-state-read-write", sharedStateReadWriteFactory.CreateAgent());// ── Sub-Agents demo (supervisor delegates to research/writing/critique) ─────var subagentsFactory = new SubagentsAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/subagents", subagentsFactory.CreateAgent());app.MapGet("/health", () => Results.Ok(new { status = "ok" }));await app.RunAsync();static OpenAIClient CreateOpenAiClient(IConfiguration configuration, ILogger logger){    // Use the shared resolver so the primary OpenAI client and the secondary    // tool-calling HTTP client (A2uiSecondaryToolCaller) agree on which upstream    // endpoint to hit (see ApiKeyResolver for the env/config precedence and the    // non-mock fail-fast).    var endpoint = ApiKeyResolver.ResolveEndpoint(configuration);    var endpointEnv = Environment.GetEnvironmentVariable("OPENAI_BASE_URL");    var endpointConfig = configuration["OPENAI_BASE_URL"];    if (!string.IsNullOrEmpty(endpointEnv))    {        logger.LogInformation("Using OpenAI endpoint from OPENAI_BASE_URL env: {Endpoint}", endpoint);    }    else if (!string.IsNullOrEmpty(endpointConfig))    {        logger.LogInformation("Using OpenAI endpoint from configuration OPENAI_BASE_URL: {Endpoint}", endpoint);    }    else    {        logger.LogInformation("OPENAI_BASE_URL not set; using default OpenAI endpoint: {Endpoint}", endpoint);    }    var apiKey = ApiKeyResolver.ResolveApiKey(configuration, logger);    return new OpenAIClient(        new ApiKeyCredential(apiKey),        AimockHeaderPolicy.CreateOpenAIClientOptions(endpoint));}public class WeatherInfo{    [JsonPropertyName("temperature")]    public int Temperature { get; init; }    [JsonPropertyName("conditions")]    public string Conditions { get; init; } = string.Empty;    [JsonPropertyName("humidity")]    public int Humidity { get; init; }    [JsonPropertyName("wind_speed")]    public int WindSpeed { get; init; }    [JsonPropertyName("feels_like")]    public int FeelsLike { get; init; }    [JsonPropertyName("city")]    public string City { get; init; } = string.Empty;}public partial class Program { }[JsonSerializable(typeof(WeatherInfo))][JsonSerializable(typeof(BeautifulChatTodo))][JsonSerializable(typeof(List<BeautifulChatTodo>))][JsonSerializable(typeof(BeautifulChatFlight))][JsonSerializable(typeof(List<BeautifulChatFlight>))]internal partial class BeautifulChatSerializerContext : JsonSerializerContext{}

## What is this?#

`<CopilotPopup>` is a prebuilt floating launcher that opens an overlay chat window on top of your page content. It's the lightest-weight way to add a copilot to an existing app. Drop it in once and a bubble appears in the corner ready to chat.

## When should I use this?#

Use the popup when you want:

  * A minimal-footprint copilot that overlays existing content on demand
  * A launcher you can place on top of any page without reflowing the layout
  * A quick assistant bubble that users open for short, task-focused chats



If you need chat to live alongside your content rather than on top of it, use [CopilotSidebar](https://docs.copilotkit.ai/ms-agent-harness-dotnet/prebuilt-components/sidebar). For a fully embedded chat pane, use [`<CopilotChat>`](https://docs.copilotkit.ai/ms-agent-harness-dotnet/prebuilt-components/chat) directly.

## Basic setup#

Wrap your app in `<CopilotKit>` once (the provider wires the runtime, session, and agent registry) and render `<CopilotPopup>` as a sibling of your main content. The example below opens the popup by default and customizes the input placeholder via `labels`:
    
    
    import { CopilotKit, CopilotPopup } from "@copilotkit/react-core/v2";
    import "@copilotkit/react-core/v2/styles.css";

`@copilotkit/react-ui` also exports a component named `CopilotPopup`. That one is the [deprecated v1 popup](https://docs.copilotkit.ai/ms-agent-harness-dotnet/migrate/v2). This page documents the v2 popup, which you import from `@copilotkit/react-core/v2`.

page.tsx
    
    
        <CopilotKit runtimeUrl="/api/copilotkit" agent="prebuilt-popup">      <MainContent />      <CopilotPopup        agentId="prebuilt-popup"        defaultOpen={true}        labels={{          chatInputPlaceholder: "Ask the popup anything...",        }}      />      <Suggestions />    </CopilotKit>

## Configuring the popup#

`<CopilotPopup>` accepts the same props as `<CopilotChat>` plus a few of its own. Commonly used options:

Prop| Description  
---|---  
`defaultOpen`| Whether the popup starts open on first render.  
`agentId`| Agent slug the popup should talk to (must match an agent configured on the runtime).  
`labels`| User-facing copy for the header, placeholder, and disclaimer.  
`header`| Slot for the popup header bar — see the [slot system](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/slots).  
`toggleButton`| Slot for the floating launcher button.  
  
## Styling#

`CopilotPopup` participates in the slot system, so every piece of its UI is customizable, from Tailwind classes on the message view to a full component swap for the header or toggle button. See [custom look and feel](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/slots) for the full slot reference.

### On this page

What is this?When should I use this?Basic setupConfiguring the popupStyling
