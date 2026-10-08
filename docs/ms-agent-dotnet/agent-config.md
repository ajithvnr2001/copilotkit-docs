---
url: https://docs.copilotkit.ai/ms-agent-dotnet/agent-config/
title: Agent Config
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:17:41.819698+00:00
---

# Agent Config

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/agent-config/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendMS Agent Framework (.NET)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/ms-agent-dotnet)[Quickstart](https://docs.copilotkit.ai/ms-agent-dotnet/quickstart)[Build with agents](https://docs.copilotkit.ai/ms-agent-dotnet/build-with-agents)[Intelligence](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/ms-agent-dotnet/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-dotnet/webmcp)

Agent capabilities

Microsoft Agent Framework

[Sub-agents](https://docs.copilotkit.ai/ms-agent-dotnet/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/ms-agent-dotnet/learning)

[User Memories](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/analytics)[Channels](https://docs.copilotkit.ai/ms-agent-dotnet/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/ms-agent-dotnet/telemetry)[Community frameworks](https://docs.copilotkit.ai/ms-agent-dotnet/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[MS Agent Framework (.NET)](https://docs.copilotkit.ai/ms-agent-dotnet)

# Agent Config

Forward typed configuration from your UI into the agent's reasoning loop.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

DemoCode

AgentConfigAgent.cs

page.tsx

config-card.tsx

use-agent-config.ts

config-types.ts

route.ts
    
    
    using System.Diagnostics.CodeAnalysis;using System.Runtime.CompilerServices;using System.Text.Json;using Microsoft.Agents.AI;using Microsoft.Extensions.AI;using Microsoft.Extensions.Logging;using Microsoft.Extensions.Logging.Abstractions;// AgentConfigAgent — the /agent-config demo.//// Reads three forwarded properties — tone, expertise, responseLength — from// the AG-UI shared-state payload (attached as `ag_ui_state` on// ChatClientAgentRunOptions.AdditionalProperties, matching the convention// already used by SharedStateAgent) and builds a dynamic system prompt per// turn.//// The frontend <CopilotKitProvider agent="agent-config-demo" />'s// useAgent().setState(...) call pushes the typed config into shared state;// this agent reads it on every run and prepends a system message that adapts// the inner ChatClientAgent's behavior. Missing / unrecognized values fall// back to the documented defaults — the agent never throws on malformed// config, so a misbehaving frontend can't kill the demo.[SuppressMessage("Performance", "CA1812:Avoid uninstantiated internal classes", Justification = "Instantiated by SalesAgentFactory")]internal sealed class AgentConfigAgent : DelegatingAIAgent{    private static readonly HashSet<string> ValidTones = new(StringComparer.Ordinal)    {        "professional",        "casual",        "enthusiastic",    };    private static readonly HashSet<string> ValidExpertise = new(StringComparer.Ordinal)    {        "beginner",        "intermediate",        "expert",    };    private static readonly HashSet<string> ValidResponseLengths = new(StringComparer.Ordinal)    {        "concise",        "detailed",    };    private const string DefaultTone = "professional";    private const string DefaultExpertise = "intermediate";    private const string DefaultResponseLength = "concise";    private readonly ILogger<AgentConfigAgent> _logger;    public AgentConfigAgent(AIAgent innerAgent, ILogger<AgentConfigAgent>? logger = null)        : base(innerAgent)    {        ArgumentNullException.ThrowIfNull(innerAgent);        _logger = logger ?? NullLogger<AgentConfigAgent>.Instance;    }    public override Task<AgentRunResponse> RunAsync(IEnumerable<ChatMessage> messages, AgentThread? thread = null, AgentRunOptions? options = null, CancellationToken cancellationToken = default)    {        return RunStreamingAsync(messages, thread, options, cancellationToken).ToAgentRunResponseAsync(cancellationToken);    }    public override async IAsyncEnumerable<AgentRunResponseUpdate> RunStreamingAsync(        IEnumerable<ChatMessage> messages,        AgentThread? thread = null,        AgentRunOptions? options = null,        [EnumeratorCancellation] CancellationToken cancellationToken = default)    {        ArgumentNullException.ThrowIfNull(messages);        // Materialize up-front so we can both inspect it (to read the state)        // and forward it to the inner agent without re-enumerating a        // single-use iterator.        var messageList = messages as IReadOnlyList<ChatMessage> ?? messages.ToList();        var (tone, expertise, responseLength) = ReadConfig(options);        var systemPrompt = BuildSystemPrompt(tone, expertise, responseLength);        _logger.LogInformation(            "AgentConfigAgent: tone={Tone}, expertise={Expertise}, responseLength={ResponseLength}",            tone, expertise, responseLength);        var systemMessage = new ChatMessage(ChatRole.System, systemPrompt);        var augmentedMessages = new List<ChatMessage>(messageList.Count + 1) { systemMessage };        augmentedMessages.AddRange(messageList);        await foreach (var update in InnerAgent.RunStreamingAsync(augmentedMessages, thread, options, cancellationToken).ConfigureAwait(false))        {            yield return update;        }    }    /// <summary>    /// Reads the forwarded config triple from the AG-UI shared-state payload    /// attached to the run options. Any missing / unrecognized value falls    /// back to the corresponding default constant. Never throws.    /// </summary>    internal static (string Tone, string Expertise, string ResponseLength) ReadConfig(AgentRunOptions? options)    {        if (options is not ChatClientAgentRunOptions { ChatOptions.AdditionalProperties: { } properties } ||            !properties.TryGetValue("ag_ui_state", out JsonElement state) ||            state.ValueKind != JsonValueKind.Object)        {            return (DefaultTone, DefaultExpertise, DefaultResponseLength);        }        var tone = ReadStringProperty(state, "tone", ValidTones, DefaultTone);        var expertise = ReadStringProperty(state, "expertise", ValidExpertise, DefaultExpertise);        var responseLength = ReadStringProperty(state, "responseLength", ValidResponseLengths, DefaultResponseLength);        return (tone, expertise, responseLength);    }    private static string ReadStringProperty(JsonElement state, string name, HashSet<string> valid, string defaultValue)    {        if (!state.TryGetProperty(name, out var element) || element.ValueKind != JsonValueKind.String)        {            return defaultValue;        }        var value = element.GetString();        return value is not null && valid.Contains(value) ? value : defaultValue;    }    internal static string BuildSystemPrompt(string tone, string expertise, string responseLength)    {        var toneRule = tone switch        {            "casual" => "Use friendly, conversational language. Contractions OK. Light humor welcome.",            "enthusiastic" => "Use upbeat, energetic language. Exclamation points OK. Emoji OK.",            _ => "Use neutral, precise language. No emoji. Short sentences.",        };        var expertiseRule = expertise switch        {            "beginner" => "Assume no prior knowledge. Define jargon. Use analogies.",            "expert" => "Assume technical fluency. Use precise terminology. Skip basics.",            _ => "Assume common terms are understood; explain specialized terms.",        };        var lengthRule = responseLength switch        {            "detailed" => "Respond in multiple paragraphs with examples where relevant.",            _ => "Respond in 1-3 sentences.",        };        return "You are a helpful assistant.\n\n" +            $"Tone: {toneRule}\n" +            $"Expertise level: {expertiseRule}\n" +            $"Response length: {lengthRule}";    }}

You have a working agent and want the user to be able to tune how it behaves: tone, expertise level, response length, language, persona. By the end of this guide, your UI will own a typed config object that the agent reads on every run and rebuilds its system prompt from.

## When to use this#

Reach for agent config whenever the agent's behaviour depends on user-controllable settings that don't fit naturally as chat input:

  * **Tone, voice, persona** : "playful", "formal", "casual"
  * **Expertise level** : "beginner", "intermediate", "expert"
  * **Response shape** : short / medium / long, structured / prose, language
  * **Domain switches** : which knowledge base to consult, which tool subset to enable



If the values are a _channel_ the user occasionally tunes (a settings panel, a toolbar of selects), agent config is the right shape. If the values are _content_ the agent should write back to (notes, a document, a plan), use [Shared State](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state) instead.

How agent config flows from the UI into the agent's reasoning loop depends on your runtime architecture. Agents living behind a runtime read it from agent state on every run, while in-process agents receive the same object as forwarded properties on the provider — same UX, slightly different wiring on each side.

## How it works#

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

The agent reads the latest typed config at the start of every turn, rebuilds the system prompt, runs the turn. This is the same shape as the [shared-state write-side pattern](https://docs.copilotkit.ai/ms-agent-dotnet/shared-state#writing-to-agent-state); agent config is just a specific use of that pattern with a UI-owned typed object on top.

### On this page

When to use thisHow it works
