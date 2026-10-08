---
url: https://docs.copilotkit.ai/ms-agent-harness-dotnet/agent-app-context/
title: Readables
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:19:50.011651+00:00
---

# Readables

> Source: https://docs.copilotkit.ai/ms-agent-harness-dotnet/agent-app-context/

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

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/ms-agent-harness-dotnet/webmcp)

Agent capabilities

MS Agent Harness (.NET)

Your Components

Declarative Generative UI (A2UI)

[Readables](https://docs.copilotkit.ai/ms-agent-harness-dotnet/agent-app-context)[Copilot Runtime](https://docs.copilotkit.ai/ms-agent-harness-dotnet/copilot-runtime)[AG-UI](https://docs.copilotkit.ai/ms-agent-harness-dotnet/ag-ui)

Troubleshooting Copilots

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

Readables

Agent capabilitiesMS Agent Harness (.NET)

# Readables

Share app specific context with your agent.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

One of the most common use cases for CopilotKit is to register app state and context using `useAgentContext`. This way, you can notify CopilotKit of what is going in your app in real time. Some examples might be: the current user, the current page, etc.

This context can then be shared with your AG-UI server and agent logic.

## Implementation#

Check out the [Frontend Data documentation](https://docs.copilotkit.ai/integrations/langgraph/agent-app-context) to understand what this is and how to use it.

Context values arrive as JSON strings

The AG-UI protocol defines a context value as a string. Therefore `useAgentContext` calls `JSON.stringify` on any `value` that is not already a string, and your agent receives the JSON text instead of the object or the array.

Parse the value before you read a field from it. Use `json.loads(item["value"])` in Python, or `JSON.parse(item.value)` in TypeScript. If you skip the parse step, an index such as `colleagues[0]` returns a single character, and a shape check such as `isinstance(value, list)` can never pass.

Do not stringify the value again, because that produces double encoding. A `value` that is already a string is sent unchanged, so no parse step is needed for it.

You'll need to run your agent and connect it to CopilotKit before proceeding. If you haven't done so already, you can follow the instructions in the [Getting Started](https://docs.copilotkit.ai/langgraph/quickstart) guide.

If you don't already have an agent, you can use the [coagent starter](https://github.com/copilotkit/copilotkit/tree/main/examples/coagents-starter) as a starting point as this guide uses it as a starting point.

### Add the data to the Copilot#

The [`useAgentContext` hook](https://docs.copilotkit.ai/reference/v2/hooks/useAgentContext) is used to add data as context to the Copilot.

YourComponent.tsx
    
    
    "use client" // only necessary if you are using Next.js with the App Router.
    
    export function YourComponent() {
        // Create colleagues state with some sample data
        const [colleagues, setColleagues] = useState([
            { id: 1, name: "John Doe", role: "Developer" },
            { id: 2, name: "Jane Smith", role: "Designer" },
            { id: 3, name: "Bob Wilson", role: "Product Manager" }
        ]);
    
        // Define Copilot readable state
        useAgentContext({
            description: "The current user's colleagues",
            value: colleagues,
        });
        return (
            // Your custom UI component
            <>...</>
        );
    }

### Consume the data in your AG-UI server#

The `context` you register on the frontend is forwarded in the AG-UI `RunAgentInput`. Use middleware to read it and inject it into the agent's conversation.

.NETPython

Program.cs
    
    
    using System.Runtime.CompilerServices;
    using System.Text;
    using AGUI.Abstractions;
    using AGUI.Server;
    using Microsoft.Agents.AI;
    using Microsoft.Agents.AI.Hosting.AGUI.AspNetCore;
    using Microsoft.AspNetCore.Builder;
    using Microsoft.Extensions.AI;
    using OpenAI;
    using OpenAI.Chat;
    using AIChatMessage = Microsoft.Extensions.AI.ChatMessage;
    
    var builder = WebApplication.CreateBuilder(args);
    builder.Services.AddAGUIServer();
    var app = builder.Build();
    
    string openAiApiKey = builder.Configuration["OPENAI_API_KEY"]
        ?? throw new InvalidOperationException("Set OPENAI_API_KEY");
    
    // Create the base agent
    AIAgent baseAgent = new OpenAIClient(openAiApiKey)
        .GetChatClient("gpt-5.4-mini")
        .AsAIAgent(
            name: "AGUIAssistant",
            instructions: "You are a helpful assistant. Use the provided context about colleagues to answer questions.");
    
    // Wrap the agent with middleware to inject context
    AIAgent agent = baseAgent
        .AsBuilder()
        .Use(runFunc: null, runStreamingFunc: InjectContextMiddleware)
        .Build();
    
    // Map the AG-UI endpoint
    app.MapAGUIServer("/", agent);
    await app.RunAsync();
    
    // Middleware to inject useAgentContext context as a system message
    async IAsyncEnumerable<AgentResponseUpdate> InjectContextMiddleware(
        IEnumerable<AIChatMessage> messages,
        AgentSession? session,
        AgentRunOptions? options,
        AIAgent innerAgent,
        [EnumeratorCancellation] CancellationToken cancellationToken)
    {
        // Recover the AG-UI request and inject its context if present
        if (options is ChatClientAgentRunOptions { ChatOptions: { } chatOptions } &&
            chatOptions.TryGetRunAgentInput(out RunAgentInput? input) &&
            input?.Context is { Count: > 0 } context)
        {
            var contextBuilder = new StringBuilder();
            contextBuilder.AppendLine("The following context from the user's application is available:");
            foreach (AGUIContext item in context)
            {
                contextBuilder.AppendLine($"- {item.Description}: {item.Value}");
            }
    
            var contextMessage = new AIChatMessage(
                ChatRole.System,
                [new TextContent(contextBuilder.ToString())]);
    
            messages = messages.Append(contextMessage);
        }
    
        await foreach (var update in innerAgent.RunStreamingAsync(messages, session, options, cancellationToken))
        {
            yield return update;
        }
    }

main.py (excerpt)
    
    
    import json
    from collections.abc import AsyncGenerator
    from typing import Any
    from uuid import uuid4
    
    from ag_ui.core import BaseEvent
    from agent_framework import Agent, BaseChatClient
    from agent_framework_ag_ui import AgentFrameworkAgent
    
    
    def build_context_system_message(context: Any) -> str | None:
        if not isinstance(context, list) or not context:
            return None
    
        lines = ["## Context from the application"]
        for entry in context:
            if not isinstance(entry, dict):
                continue
    
            description = entry.get("description")
            value = entry.get("value")
            if not isinstance(description, str) or not description or value is None:
                continue
    
            if not isinstance(value, str):
                try:
                    value = json.dumps(value, ensure_ascii=False, indent=2)
                except (TypeError, ValueError):
                    value = str(value)
            lines.extend(["", description, value])
    
        return "\n".join(lines) if len(lines) > 1 else None
    
    
    class ContextAwareAgent(AgentFrameworkAgent):
        """Add app context to this request without mutating the shared agent."""
    
        async def run(
            self,
            input_data: dict[str, Any],
        ) -> AsyncGenerator[BaseEvent, None]:
            context_prompt = build_context_system_message(input_data.get("context"))
            messages = input_data.get("messages")
    
            # The adapter skips the model when messages are empty. Context
            # alone must not create an unsolicited model call.
            if context_prompt and isinstance(messages, list) and messages:
                run_id = input_data.get("runId") or str(uuid4())
                request_input = dict(input_data)
                request_input["runId"] = run_id
                request_input["messages"] = [
                    {
                        "id": f"{run_id}-app-context",
                        "role": "system",
                        "content": context_prompt,
                    },
                    *[
                        message
                        for message in messages
                        if not (
                            isinstance(message, dict)
                            and isinstance(message.get("id"), str)
                            and message["id"].endswith("-app-context")
                        )
                    ],
                ]
                input_data = request_input
    
            async for event in super().run(input_data):
                yield event
    
    
    def create_agent(chat_client: BaseChatClient) -> AgentFrameworkAgent:
        base_agent = Agent(
            name="sample_agent",
            instructions="You are a helpful assistant.",
            client=chat_client,
        )
    
        return ContextAwareAgent(
            agent=base_agent,
            name="CopilotKitMicrosoftAgentFrameworkAgent",
            description="Assistant using request-local app context.",
            require_confirmation=False,
        )

Context registered with `useAgentContext` is forwarded in `RunAgentInput.Context` as `AGUIContext` entries. `TryGetRunAgentInput` recovers the request without depending on hosting-layer keys.

**Configuration & Error Handling**: This example uses `OPENAI_API_KEY` for configuration. Set it with user secrets or an environment variable. For production deployments, add appropriate error handling and consider using the [Quickstart](https://docs.copilotkit.ai/microsoft-agent-framework/quickstart) or [Authentication](https://docs.copilotkit.ai/microsoft-agent-framework/auth) guides for complete setup patterns.

### Give it a try!#

Ask your agent a question about the context (e.g., "Who are my colleagues?"). The agent will use the forwarded context to answer!

### On this page

Implementation
