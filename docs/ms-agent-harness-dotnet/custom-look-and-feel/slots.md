---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/slots/
title: Slots (Subcomponents)
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:20:26.744384+00:00
---

# Slots (Subcomponents)

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/slots/

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

Slots (Subcomponents)

BasicsChatCustom Look and Feel

# Slots (Subcomponents)

Customize any part of the chat UI by overriding individual sub-components via slots.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

Program.cs

page.tsx

custom-welcome-screen.tsx

route.ts
    
    
    using System.ClientModel;using System.Net.Http;using System.Text.Json.Serialization;using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;using Microsoft.AspNetCore.Http.Json;using Microsoft.Extensions.Options;using OpenAI;var builder = WebApplication.CreateBuilder(args);builder.Services.ConfigureHttpJsonOptions(options =>{    // Beautiful-chat types (shipped) + the full-column Sales/Flight/parity types    // ported by the family slots. Both source-generated contexts are chained so    // every feature agent's tool I/O serializes through the fast path.    options.SerializerOptions.TypeInfoResolverChain.Add(BeautifulChatSerializerContext.Default);    options.SerializerOptions.TypeInfoResolverChain.Add(SalesAgentSerializerContext.Default);    // Serialize enum types as their member-name strings rather than numeric    // ordinals (matches the Framework column's wire format).    options.SerializerOptions.Converters.Add(new JsonStringEnumConverter());});builder.Services.AddAGUI();// STOPGAP: IHttpContextAccessor lets AimockHeaderPolicy read the current// request's forwarded x-* headers (stashed on HttpContext.Items by// AimockHeaderMiddleware) at outbound-LLM-call time. HttpContext flows across// the AG-UI SSE-pump ExecutionContext boundary, unlike a middleware-set// AsyncLocal. TODO(copilotkit-sdk-dotnet): migrate to SDK-level header propagation.builder.Services.AddHttpContextAccessor();var app = builder.Build();// STOPGAP: seed the static accessor the outbound header-forwarding policy reads// (the policy is created without DI, mirroring CvDiag.Logger).AimockHeaderPolicy.HttpContextAccessor = app.Services.GetRequiredService<IHttpContextAccessor>();// Forward D5/aimock x-* headers from incoming AG-UI requests to outgoing// OpenAI calls until the .NET SDK owns this propagation centrally.app.UseMiddleware<AimockHeaderMiddleware>();// CVDIAG: backend flap-observability emitter (plan unit L1-F; spec §3). OFF by// default (CVDIAG_BACKEND_EMITTER=on to arm). Seed the static singleton the// outbound LLM policy reads (created without DI), then register the// request-pipeline instrumentation AFTER AimockHeaderMiddleware so the forwarded// x-* correlation headers are already captured for this request.CvdiagBackend.Instance = new CvdiagBackend();app.UseMiddleware<CvdiagInstrumentationMiddleware>();var loggerFactory = app.Services.GetRequiredService<ILoggerFactory>();// CVDIAG: seed the static logger used by AimockHeaderPolicy (created without DI)// to emit the outbound-LLM header-forwarding breadcrumb.CvDiag.Logger = loggerFactory.CreateLogger("CvDiag");var jsonOptions = app.Services.GetRequiredService<IOptions<JsonOptions>>().Value.SerializerOptions;// Single shared OpenAIClient for the whole column. Built once via the harness// ApiKeyResolver (env OPENAI_API_KEY -> config OPENAI_API_KEY -> GitHubToken,// fail-fast for non-mock endpoints) so EVERY feature agent hits the same// upstream with the same credential resolution — no per-feature GitHubToken// dance. Threaded into each feature factory's ctor. See the W0 contract §1.var openAiClient = CreateOpenAiClient(builder.Configuration, loggerFactory.CreateLogger("Program"));// ── Root agentic-chat agent (the Sales pipeline agent) ──────────────────────// agentic-chat, chat-slots, chat-customization-css, prebuilt-{sidebar,popup},// frontend-tools{,-async}, headless-simple, shared-state-read, and the two// tool-rendering catch-all demos all proxy to this root agent via the shared// Next.js `copilotkit/` runtime route.var salesFactory = new SalesAgentFactory(builder.Configuration, openAiClient, jsonOptions, loggerFactory);app.MapAGUI("/", salesFactory.CreateSalesAgent());// ── D5 parity agents (one factory hosts the parity-feature surface) ─────────var d5ParityFactory = new D5ParityAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/headless-complete", d5ParityFactory.CreateHeadlessCompleteAgent());app.MapAGUI("/voice", d5ParityFactory.CreateVoiceAgent());app.MapAGUI("/gen-ui-agent", d5ParityFactory.CreateGenUiAgent());app.MapAGUI("/gen-ui-tool-based", d5ParityFactory.CreateGenUiToolBasedAgent());app.MapAGUI("/shared-state-streaming", d5ParityFactory.CreateSharedStateStreamingAgent());app.MapAGUI("/readonly-state-agent-context", d5ParityFactory.CreateReadonlyStateAgentContext());app.MapAGUI("/tool-rendering", d5ParityFactory.CreateToolRenderingAgent(reasoning: false));app.MapAGUI("/tool-rendering-reasoning-chain", d5ParityFactory.CreateToolRenderingAgent(reasoning: true));// ── Interrupt agent (NOT-SUPPORTED, wired for parity) ───────────────────────// gen-ui-interrupt and interrupt-headless share this single backend; the// differentiation is on the frontend (in-chat picker vs. headless button grid).// Marked not_supported in manifest.yaml (skipped-incapable) pending a// @copilotkit/react-core resume-path fix — wired here so the column is 1:1.var interruptFactory = new InterruptAgentFactory(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/interrupt-adapted", interruptFactory.CreateInterruptAgent());// ── Multimodal (raw MapPost — the AG-UI adapter rejects content arrays) ─────// Parses the request body directly and emits the small AG-UI SSE event subset// the chat UI needs for text streaming over a vision-capable chat client.app.MapPost("/multimodal", (HttpContext context) => MultimodalEndpoint.HandleAsync(    context,    salesFactory.CreateMultimodalChatClient(),    loggerFactory.CreateLogger("MultimodalEndpoint")));// ── Beautiful Chat flagship demo (shipped) ──────────────────────────────────var beautifulChatFactory = new BeautifulChatAgentFactory(    builder.Configuration,    openAiClient,    jsonOptions,    loggerFactory.CreateLogger<BeautifulChatAgentFactory>());app.MapAGUI("/beautiful-chat", beautifulChatFactory.Create());// ── Agent Config (wraps a neutral inner agent in AgentConfigAgent) ──────────app.MapAGUI("/agent-config", salesFactory.CreateAgentConfigAgent());// ── Reasoning (reasoning-default + reasoning-custom share this backend) ─────app.MapAGUI("/reasoning", salesFactory.CreateReasoningAgent());// ── Declarative Gen UI (A2UI canonical BYOC) ────────────────────────────────var declarativeGenUiAgent = new DeclarativeGenUiAgent(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/declarative-gen-ui", declarativeGenUiAgent.Create());// ── A2UI fixed-schema demo ──────────────────────────────────────────────────var a2uiFixedSchemaAgent = new A2uiFixedSchemaAgent(builder.Configuration, openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/a2ui-fixed-schema", a2uiFixedSchemaAgent.Create());// ── Open Generative UI — basic + advanced ───────────────────────────────────var openGenUiFactory = new OpenGenUiAgentFactory(openAiClient);app.MapAGUI("/open-gen-ui", openGenUiFactory.CreateAgent());var openGenUiAdvancedFactory = new OpenGenUiAdvancedAgentFactory(openAiClient);app.MapAGUI("/open-gen-ui-advanced", openGenUiAdvancedFactory.CreateAgent());// ── BYOC demos (hashbrown + json-render) ────────────────────────────────────var byocHashbrownFactory = new ByocHashbrownAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/byoc-hashbrown", byocHashbrownFactory.CreateAgent());var byocJsonRenderFactory = new ByocJsonRenderAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/byoc-json-render", byocJsonRenderFactory.CreateAgent());// ── MCP Apps demo ───────────────────────────────────────────────────────────var mcpAppsFactory = new McpAppsAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/mcp-apps", mcpAppsFactory.CreateMcpAppsAgent());// ── In-app HITL demo (frontend tools + async HITL) ──────────────────────────var hitlInAppFactory = new HitlInAppAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/hitl-in-app", hitlInAppFactory.CreateHitlInAppAgent());// ── In-chat HITL demo (useHumanInTheLoop) ───────────────────────────────────var hitlInChatFactory = new HitlInChatAgentFactory(openAiClient, loggerFactory);app.MapAGUI("/hitl-in-chat", hitlInChatFactory.CreateHitlInChatAgent());// ── Shared State (Read + Write) demo ────────────────────────────────────────var sharedStateReadWriteFactory = new SharedStateReadWriteAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/shared-state-read-write", sharedStateReadWriteFactory.CreateAgent());// ── Sub-Agents demo (supervisor delegates to research/writing/critique) ─────var subagentsFactory = new SubagentsAgentFactory(openAiClient, loggerFactory, jsonOptions);app.MapAGUI("/subagents", subagentsFactory.CreateAgent());app.MapGet("/health", () => Results.Ok(new { status = "ok" }));await app.RunAsync();static OpenAIClient CreateOpenAiClient(IConfiguration configuration, ILogger logger){    // Use the shared resolver so the primary OpenAI client and the secondary    // tool-calling HTTP client (A2uiSecondaryToolCaller) agree on which upstream    // endpoint to hit (see ApiKeyResolver for the env/config precedence and the    // non-mock fail-fast).    var endpoint = ApiKeyResolver.ResolveEndpoint(configuration);    var endpointEnv = Environment.GetEnvironmentVariable("OPENAI_BASE_URL");    var endpointConfig = configuration["OPENAI_BASE_URL"];    if (!string.IsNullOrEmpty(endpointEnv))    {        logger.LogInformation("Using OpenAI endpoint from OPENAI_BASE_URL env: {Endpoint}", endpoint);    }    else if (!string.IsNullOrEmpty(endpointConfig))    {        logger.LogInformation("Using OpenAI endpoint from configuration OPENAI_BASE_URL: {Endpoint}", endpoint);    }    else    {        logger.LogInformation("OPENAI_BASE_URL not set; using default OpenAI endpoint: {Endpoint}", endpoint);    }    var apiKey = ApiKeyResolver.ResolveApiKey(configuration, logger);    return new OpenAIClient(        new ApiKeyCredential(apiKey),        AimockHeaderPolicy.CreateOpenAIClientOptions(endpoint));}public class WeatherInfo{    [JsonPropertyName("temperature")]    public int Temperature { get; init; }    [JsonPropertyName("conditions")]    public string Conditions { get; init; } = string.Empty;    [JsonPropertyName("humidity")]    public int Humidity { get; init; }    [JsonPropertyName("wind_speed")]    public int WindSpeed { get; init; }    [JsonPropertyName("feels_like")]    public int FeelsLike { get; init; }    [JsonPropertyName("city")]    public string City { get; init; } = string.Empty;}public partial class Program { }[JsonSerializable(typeof(WeatherInfo))][JsonSerializable(typeof(BeautifulChatTodo))][JsonSerializable(typeof(List<BeautifulChatTodo>))][JsonSerializable(typeof(BeautifulChatFlight))][JsonSerializable(typeof(List<BeautifulChatFlight>))]internal partial class BeautifulChatSerializerContext : JsonSerializerContext{}

## What is this?#

Every CopilotKit chat component is built from composable **slots** , named sub-components you can override individually. The slot system gives you three levels of customization without needing to rebuild the entire UI:

  1. **Tailwind classes** — pass a string to add/override CSS classes
  2. **Props override** — pass an object to override specific props on the default component
  3. **Custom component** — pass your own React component to fully replace a slot



Slots are recursive: you can drill into nested sub-components at any depth.

## What it looks like in code#

The `chat-slots` cell above overrides three slots on a single `<CopilotChat>` — the welcome screen, the assistant message card, and the input's disclaimer. Each slot is just a prop; the demo extracts them into locals so the override points are easy to see.

### Welcome screen slot#

The `welcomeScreen` prop replaces the empty-state view shown before the first message is sent. The demo swaps in a gradient card that still renders the default input and suggestions:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;

### Assistant message slot#

Drill into `messageView={{ assistantMessage: ... }}` to wrap every assistant response. The cell wraps the default component with a tinted card and a small "slot" badge so you can see the override is active during the message flow:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;  const messageView = {    assistantMessage:      CustomAssistantMessage as unknown as typeof CopilotChatAssistantMessage,  };

### Disclaimer slot#

The `input={{ disclaimer: ... }}` sub-slot lets you replace the small text shown below the input. The demo uses it to display a visibly tagged disclaimer so reviewers can tell the override is still in effect once the welcome screen is gone:

slot-overrides.tsx
    
    
    import type {  CopilotChatAssistantMessage,  CopilotChatInput,  CopilotChatView,} from "@copilotkit/react-core/v2";declare const CustomWelcomeScreen: React.ComponentType;declare const CustomAssistantMessage: React.ComponentType;declare const CustomDisclaimer: React.ComponentType;export function ChatSlotsTeachingExtracts() {  const welcomeScreen =    CustomWelcomeScreen as unknown as typeof CopilotChatView.WelcomeScreen;  const messageView = {    assistantMessage:      CustomAssistantMessage as unknown as typeof CopilotChatAssistantMessage,  };  const input = {    disclaimer:      CustomDisclaimer as unknown as typeof CopilotChatInput.Disclaimer,  };

## Tailwind Classes#

The simplest way to customize a slot. Pass a Tailwind class string and it will be merged with the default component's classes.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    export function Chat() {
      return (
        <CopilotChat
          messageView="bg-gray-50 dark:bg-gray-900 p-4"
          input="border-2 border-blue-400 rounded-xl"
        />
      );
    }

## Props Override#

Pass an object to override specific props on the default component. This is useful for adding `className`, event handlers, data attributes, or any other prop the default component accepts.

page.tsx
    
    
    <CopilotChat
      messageView={{
        className: "my-custom-messages",
        "data-testid": "message-view",
      }}
      input={{ autoFocus: true }}
    />

## Custom Components#

For full control, pass your own React component. It receives all the same props as the default component.

page.tsx
    
    
    import { CopilotChat } from "@copilotkit/react-core/v2";
    
    const CustomMessageView = ({ messages, isRunning }) => (
      <div className="space-y-4 p-6">
        {messages?.map((msg) => (
          <div key={msg.id} className={msg.role === "user" ? "text-right" : "text-left"}>
            {msg.content}
          </div>
        ))}
        {isRunning && <div className="animate-pulse">Thinking...</div>}
      </div>
    );
    
    export function Chat() {
      return <CopilotChat messageView={CustomMessageView} />;
    }

## Nested Slots (Drill-Down)#

Slots are recursive. You can customize sub-components at any depth by nesting objects.

### Two levels deep#

Override the assistant message's toolbar within the message view:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          toolbar: CustomToolbar,
          copyButton: CustomCopyButton,
        },
        userMessage: CustomUserMessage,
      }}
    />

### Three levels deep#

Override a specific button inside the assistant message toolbar:

page.tsx
    
    
    <CopilotChat
      messageView={{
        assistantMessage: {
          copyButton: ({ onClick }) => (
            <button onClick={onClick}>Copy</button>
          ),
        },
      }}
    />

The `assistantMessage` slot also holds `markdownRenderer`, which controls how assistant markdown is rendered. It has its own guide: [Markdown Rendering](https://docs.copilotkit.ai/ms-agent-harness-dotnet/custom-look-and-feel/markdown).

## Labels#

Customize any text string in the UI via the `labels` prop. This is a separate convenience prop on `CopilotChat`, `CopilotSidebar`, and `CopilotPopup`, not part of the slot system.

page.tsx
    
    
    <CopilotChat
      labels={{
        chatInputPlaceholder: "Ask your agent anything...",
        welcomeMessageText: "How can I help you today?",
        chatDisclaimerText: "AI responses may be inaccurate.",
      }}
    />

## Available Slots#

### `CopilotChat` / `CopilotSidebar` / `CopilotPopup`#

These are the root-level slot props available on all chat components:

Slot| Description  
---|---  
`messageView`| The message list container.  
`scrollView`| The scroll container with auto-scroll behavior.  
`input`| The text input area with send/transcribe controls.  
`suggestionView`| The suggestion pills shown below messages.  
`welcomeScreen`| The initial empty-state screen (pass `false` to disable).  
  
`CopilotSidebar` and `CopilotPopup` also have:

Slot| Description  
---|---  
`header`| The modal header bar.  
`toggleButton`| The open/close toggle button.  
  
### On this page

What is this?What it looks like in codeWelcome screen slotAssistant message slotDisclaimer slotTailwind ClassesProps OverrideCustom ComponentsNested Slots (Drill-Down)Two levels deepThree levels deepLabelsAvailable SlotsCopilotChat / CopilotSidebar / CopilotPopup
