---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/tool-based/
title: Components as Tools
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:33.157280+00:00
---

# Components as Tools

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/tool-based/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Harness (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-harness-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-harness-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-harness-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-harness-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/frontend-tools)

Generative UI

Controlled

[Components as Tools](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/tool-based)[Tool Call Rendering](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/tool-rendering)[State Rendering](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/state-rendering)

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

Components as Tools

Generative UIControlled

# Components as Tools

Let your agent render rich React components directly in the chat by calling them as tools.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

Program.cs

page.tsx

route.ts
    
    
    using System.ClientModel;using System.Net.Http;using System.Text.Json.Serialization;using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;using Microsoft.AspNetCore.Http.Json;using Microsoft.Extensions.Options;using OpenAI;var builder = WebApplication.CreateBuilder(args);builder.Services.ConfigureHttpJsonOptions(options =>{    // Beautiful-chat types (shipped) + the full-column Sales/Flight/parity types    // ported by the family slots. Both source-generated contexts are chained so    // every feature agent's tool I/O serializes through the fast path.    options.SerializerOptions.TypeInfoResolverChain.Add(BeautifulChatSerializerContext.Default);    options.SerializerOptions.TypeInfoResolverChain.Add(SalesAgentSerializerContext.Default);    // Serialize enum types as their member-name strings rather than numeric    // ordinals (matches the Framework column's wire format).    options.SerializerOptions.Converters.Add(new JsonStringEnumConverter());});builder.Services.AddAGUI();// STOPGAP: IHttpContextAccessor lets AimockHeaderPolicy read the current// request's forwarded x-* headers (stashed on HttpContext.Items by// AimockHeaderMiddleware) at outbound-LLM-call time. HttpContext flows across// the AG-UI SSE-pump ExecutionContext boundary, unlike a middleware-set// AsyncLocal. TODO(copilotkit-sdk-dotnet): migrate to SDK-level header propagation.builder.Services.AddHttpContextAccessor();var app = builder.Build();// STOPGAP: seed the static accessor the outbound header-forwarding policy reads// (the policy is created without DI, mirroring CvDiag.Logger).AimockHeaderPolicy.HttpContextAccessor = app.Services.GetRequiredService<IHttpContextAccessor>();// Forward D5/aimock x-* headers from incoming AG-UI requests to outgoing// OpenAI calls until the .NET SDK owns this propagation centrally.app.UseMiddleware<AimockHeaderMiddleware>();// CVDIAG: backend flap-observability emitter (plan unit L1-F; spec §3). OFF by// default (CVDIAG_BACKEND_EMITTER=on to arm). Seed the static singleton the// outbound LLM policy reads (created without DI), then register the// request-pipeline instrumentation AFTER AimockHeaderMiddleware so the forwarded// x-* correlation headers are already captured for this request.CvdiagBackend.Instance = new CvdiagBackend();app.UseMiddleware<CvdiagInstrumentationMiddleware>();var loggerFactory = app.Services.GetRequiredService<ILoggerFactory>();// CVDIAG: seed the static logger used by AimockHeaderPolicy (created without DI)// to emit the outbound-LLM header-forwarding breadcrumb.CvDiag.Logger = loggerFactory.CreateLogger("CvDiag");var jsonOptions = app.Services.GetRequiredService<IOptions<JsonOptions>>().Value.SerializerOptions;// Single shared OpenAIClient for the whole column. Built once via the harness// ApiKeyResolver (env OPENAI_API_KEY -> config OPENAI_API_KEY -> GitHubToken,// fail-fast for non-mock endpoints) so EVERY feature agent hits the same// upstream with the same credential resolution — no per-feature GitHubToken// dance. Threaded into each feature factory's ctor. See the W0 contract §1.var openAiClient = CreateOpenAiClient(builder.Configuration, loggerFactory.CreateLogger("Program"));// ── Root agentic-chat agent (the Sales pipeline agent) ──────────────────────// agentic-chat, chat-slots, chat-customization-css, prebuilt-{sidebar,popup},// frontend-tools{,-async}, headless-simple, shared-state-read, and the two// tool-rendering catch-all demos all proxy to this root agent via the shared// Next.js `copilotkit/` runtime route.var salesFactory = new SalesAgentFactory(builder.Configuration, openAiClient, jsonOptions, loggerFactory);app.MapAGUI("/", salesFactory.CreateSalesAgent());// ── D5 parity agents (one factory hosts the parity-feature surface) ─────────var d5ParityFactory = new D5ParityAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/headless-complete", d5ParityFactory.CreateHeadlessCompleteAgent());app.MapAGUI("/voice", d5ParityFactory.CreateVoiceAgent());app.MapAGUI("/gen-ui-agent", d5ParityFactory.CreateGenUiAgent());app.MapAGUI("/gen-ui-tool-based", d5ParityFactory.CreateGenUiToolBasedAgent());app.MapAGUI("/shared-state-streaming", d5ParityFactory.CreateSharedStateStreamingAgent());app.MapAGUI("/readonly-state-agent-context", d5ParityFactory.CreateReadonlyStateAgentContext());app.MapAGUI("/tool-rendering", d5ParityFactory.CreateToolRenderingAgent(reasoning: false));app.MapAGUI("/tool-rendering-reasoning-chain", d5ParityFactory.CreateToolRenderingAgent(reasoning: true));// ── Interrupt agent (NOT-SUPPORTED, wired for parity) ───────────────────────// gen-ui-interrupt and interrupt-headless share this single backend; the// differentiation is on the frontend (in-chat picker vs. headless button grid).// Marked not_supported in manifest.yaml (skipped-incapable) pending a// @copilotkit/react-core resume-path fix — wired here so the column is 1:1.var interruptFactory = new InterruptAgentFactory(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/interrupt-adapted", interruptFactory.CreateInterruptAgent());// ── Multimodal (raw MapPost — the AG-UI adapter rejects content arrays) ─────// Parses the request body directly and emits the small AG-UI SSE event subset// the chat UI needs for text streaming over a vision-capable chat client.app.MapPost("/multimodal", (HttpContext context) => MultimodalEndpoint.HandleAsync(    context,    salesFactory.CreateMultimodalChatClient(),    loggerFactory.CreateLogger("MultimodalEndpoint")));// ── Beautiful Chat flagship demo (shipped) ──────────────────────────────────var beautifulChatFactory = new BeautifulChatAgentFactory(    builder.Configuration,    openAiClient,    jsonOptions,    loggerFactory.CreateLogger<BeautifulChatAgentFactory>());app.MapAGUI("/beautiful-chat", beautifulChatFactory.Create());// ── Agent Config (wraps a neutral inner agent in AgentConfigAgent) ──────────app.MapAGUI("/agent-config", salesFactory.CreateAgentConfigAgent());// ── Reasoning (reasoning-default + reasoning-custom share this backend) ─────app.MapAGUI("/reasoning", salesFactory.CreateReasoningAgent());// ── Declarative Gen UI (A2UI canonical BYOC) ────────────────────────────────var declarativeGenUiAgent = new DeclarativeGenUiAgent(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/declarative-gen-ui", declarativeGenUiAgent.Create());// ── A2UI fixed-schema demo ──────────────────────────────────────────────────var a2uiFixedSchemaAgent = new A2uiFixedSchemaAgent(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/a2ui-fixed-schema", a2uiFixedSchemaAgent.Create());// ── Open Generative UI — basic + advanced ───────────────────────────────────var openGenUiFactory = new OpenGenUiAgentFactory(openAiClient);app.MapAGUI("/open-gen-ui", openGenUiFactory.CreateAgent());var openGenUiAdvancedFactory = new OpenGenUiAdvancedAgentFactory(openAiClient);app.MapAGUI("/open-gen-ui-advanced", openGenUiAdvancedFactory.CreateAgent());// ── BYOC demos (hashbrown + json-render) ────────────────────────────────────var byocHashbrownFactory = new ByocHashbrownAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/byoc-hashbrown", byocHashbrownFactory.CreateAgent());var byocJsonRenderFactory = new ByocJsonRenderAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/byoc-json-render", byocJsonRenderFactory.CreateAgent());// ── MCP Apps demo ───────────────────────────────────────────────────────────var mcpAppsFactory = new McpAppsAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/mcp-apps", mcpAppsFactory.CreateMcpAppsAgent());// ── In-app HITL demo (frontend tools + async HITL) ──────────────────────────var hitlInAppFactory = new HitlInAppAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/hitl-in-app", hitlInAppFactory.CreateHitlInAppAgent());// ── In-chat HITL demo (useHumanInTheLoop) ───────────────────────────────────var hitlInChatFactory = new HitlInChatAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/hitl-in-chat", hitlInChatFactory.CreateHitlInChatAgent());// ── Shared State (Read + Write) demo ────────────────────────────────────────var sharedStateReadWriteFactory = new SharedStateReadWriteAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/shared-state-read-write", sharedStateReadWriteFactory.CreateAgent());// ── Sub-Agents demo (supervisor delegates to research/writing/critique) ─────var subagentsFactory = new SubagentsAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/subagents", subagentsFactory.CreateAgent());app.MapGet("/health", () => Results.Ok(new { status = "ok" }));await app.RunAsync();static OpenAIClient CreateOpenAiClient(IConfiguration configuration, ILogger logger){    // Use the shared resolver so the primary OpenAI client and the secondary    // tool-calling HTTP client (A2uiSecondaryToolCaller) agree on which upstream    // endpoint to hit (see ApiKeyResolver for the env/config precedence and the    // non-mock fail-fast).    var endpoint = ApiKeyResolver.ResolveEndpoint(configuration);    var endpointEnv = Environment.GetEnvironmentVariable("OPENAI_BASE_URL");    var endpointConfig = configuration["OPENAI_BASE_URL"];    if (!string.IsNullOrEmpty(endpointEnv))    {        logger.LogInformation("Using OpenAI endpoint from OPENAI_BASE_URL env: {Endpoint}", endpoint);    }    else if (!string.IsNullOrEmpty(endpointConfig))    {        logger.LogInformation("Using OpenAI endpoint from configuration OPENAI_BASE_URL: {Endpoint}", endpoint);    }    else    {        logger.LogInformation("OPENAI_BASE_URL not set; using default OpenAI endpoint: {Endpoint}", endpoint);    }    var apiKey = ApiKeyResolver.ResolveApiKey(configuration, logger);    return new OpenAIClient(        new ApiKeyCredential(apiKey),        AimockHeaderPolicy.CreateOpenAIClientOptions(endpoint));}public class WeatherInfo{    [JsonPropertyName("temperature")]    public int Temperature { get; init; }    [JsonPropertyName("conditions")]    public string Conditions { get; init; } = string.Empty;    [JsonPropertyName("humidity")]    public int Humidity { get; init; }    [JsonPropertyName("wind_speed")]    public int WindSpeed { get; init; }    [JsonPropertyName("feels_like")]    public int FeelsLike { get; init; }    [JsonPropertyName("city")]    public string City { get; init; } = string.Empty;}public partial class Program { }[JsonSerializable(typeof(WeatherInfo))][JsonSerializable(typeof(BeautifulChatTodo))][JsonSerializable(typeof(List<BeautifulChatTodo>))][JsonSerializable(typeof(BeautifulChatFlight))][JsonSerializable(typeof(List<BeautifulChatFlight>))]internal partial class BeautifulChatSerializerContext : JsonSerializerContext{}

## What is this?#

Tool-based Generative UI is the simplest form of Generative UI: you register a React component with `useComponent`, and CopilotKit exposes it to the agent as a tool. When the agent calls the tool, CopilotKit renders your component inline in the chat, passing the tool's arguments straight through as typed props.

Unlike [tool rendering](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/tool-rendering), which wraps a real backend tool in a custom UI, tool-based GenUI is the component. There is no handler, no user interaction, no server-side execution. The agent decides when to show it, populates the data, and CopilotKit paints it.

## When should I use this?#

Use `useComponent` when you want to:

  * Display rich UI (cards, charts, tables, dashboards) inline in the chat
  * Show structured data the agent has derived from its reasoning
  * Render previews, status indicators, or visual summaries
  * Let the agent present information beyond plain text



For components that need user interaction, see [Human-in-the-loop](https://docs.copilotkit.ai/ms-agent-harness-dotnet/human-in-the-loop). For operational transparency around a real backend tool, see [Tool rendering](https://docs.copilotkit.ai/ms-agent-harness-dotnet/generative-ui/tool-rendering).

## How it works in code#

### Nothing to wire on the agent

The AG-UI hosting layer merges the request's tool definitions into the tool list the model sees, so the agent declares none of its own. A component registered with `useComponent` reaches the model by name. The harness takes its tool list through `ChatOptions`, and leaving `Tools` empty is correct when the only tools in play are frontend ones.

agent/ChartAgent.cs
    
    
    using Microsoft.Agents.AI;
    using Microsoft.Extensions.AI;
    
    private const int HarnessMaxContextWindowTokens = 128_000;
    private const int HarnessMaxOutputTokens = 8_192;
    
    public AIAgent CreateChartAgent()
    {
        var chatClient = _openAiClient.GetChatClient("gpt-4o-mini").AsIChatClient();
    
        return chatClient.AsHarnessAgent(
            HarnessMaxContextWindowTokens,
            HarnessMaxOutputTokens,
            new HarnessAgentOptions
            {
                Name = "ChartAgent",
                Description = "Renders charts from data.",
                ChatOptions = new ChatOptions
                {
                    Instructions = SystemPrompt,
                    MaxOutputTokens = HarnessMaxOutputTokens,
                    Tools = [],
                },
            });
    }

### Tell the model when to call it

This is the part that is easy to miss. The tool arrives on every run, but a model with no instruction about it will answer in prose and never call it. Name the tool in `Instructions` and say what it is for.

agent/ChartAgent.cs
    
    
    private const string SystemPrompt = """
        You are a data visualization assistant.
        When the user asks for a chart, call render_bar_chart with a concise
        title, description, and data array of {label, value} items.
        Keep final chat responses brief.
        """;

Import the React hook and Zod in the component that registers the tool. This also applies to the built-in agent, which needs no backend tool-registration step.
    
    
    import { useComponent } from "@copilotkit/react-core/v2";
    import { z } from "zod";

`useComponent` takes a name, a Zod schema for its props, and the component to render. The runtime registers it as a frontend tool so the agent can discover it, and the schema becomes that tool's parameter definition — it is what tells the model which arguments to send.

`parameters` is optional, but leaving it out advertises the tool with an empty parameter schema (`{ "type": "object", "properties": {} }`). The model then has nothing to fill in, so it calls the tool with no arguments and your component renders with no props. Pass a schema for any component that needs data.

page.tsx
    
    
      useComponent({    name: "render_bar_chart",    description: "Display a bar chart with labeled numeric values.",    parameters: barChartPropsSchema,    render: BarChart,  });

The component itself is ordinary React: it reads only its props and can stream in as the agent fills the payload. The example above uses [Recharts](https://recharts.org) for the bar chart; it doesn't know anything about CopilotKit.

The `name` you pass to `useComponent` is what the agent sees as the tool name. Make it a verb like `render_bar_chart` or `show_weather` so the LLM reliably picks it when the user asks for that visualization.

## Rendering in a headless chat#

CopilotKit's built-in chat components paint registered components for you. A headless or custom chat renders the message list itself, so nothing paints a tool call unless you render it — the component is registered and the agent calls it, but the chat stays empty.

Render the tool calls on each assistant message with `CopilotChatToolCallsView`:
    
    
    import { CopilotChatToolCallsView } from "@copilotkit/react-core/v2";
    
    <CopilotChatToolCallsView message={assistantMessage} messages={allMessages} />;

It looks up the sibling `tool`-role message for each tool call and hands both to the registered renderer. For finer placement, call `useRenderToolCall()` and paint each tool call yourself — see [Headless UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/headless-ui).

### On this page

What is this?When should I use this?How it works in codeRendering in a headless chat
