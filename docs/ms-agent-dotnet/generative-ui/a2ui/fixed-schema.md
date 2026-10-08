---
url: https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/a2ui/fixed-schema/
title: Fixed Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:18:30.807155+00:00
---

# Fixed Schema A2UI

> Source: https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/a2ui/fixed-schema/

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

[A2UI](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/hashbrown)

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

Fixed Schema A2UI

Generative UIDeclarativeA2UI

# Fixed Schema A2UI

Pre-defined A2UI schema with dynamic data. The fastest approach — no LLM schema generation needed.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

In the fixed-schema approach, you design the UI schema once (in a JSON file or using the [A2UI Composer](https://a2ui-composer.ag-ui.com/)) and your agent tool only provides the data. The surface appears instantly when the tool returns.

## How it works#

  1. Schema is loaded from a JSON file at startup
  2. Agent tool receives data from the LLM (e.g., flight search results)
  3. Tool returns an `a2ui_operations` container with createSurface + updateComponents + updateDataModel
  4. The A2UI middleware intercepts the tool result and renders the surface



## Implementation#

### Create the A2UI schema#

Design your schema using the [A2UI Composer](https://a2ui-composer.ag-ui.com/) or write it by hand. Save it as a JSON file:
    
    
    apps/agent/src/a2ui/schemas/flight_schema.json

### Define the agent tool (Python)#

src/agents/a2ui_fixed.py
    
    
    import json
    from pathlib import Path
    from typing import Annotated
    
    from agent_framework import tool
    from pydantic import Field
    
    CATALOG_ID = "copilotkit://flight-fixed-catalog"
    SURFACE_ID = "flight-fixed-schema"
    
    FLIGHT_SCHEMA = json.load(
        open(Path(__file__).parent / "a2ui_schemas" / "flight_schema.json")
    )
    
    
    @tool(name="display_flight", description="Show a flight card for the given trip.")
    def display_flight(
        origin: Annotated[str, Field(description="3-letter origin code, e.g. 'SFO'.")],
        destination: Annotated[str, Field(description="3-letter destination code.")],
        airline: Annotated[str, Field(description="Airline name.")],
        price: Annotated[str, Field(description="Price string, e.g. '$289'.")],
    ) -> str:
        """Show a flight card for the given trip."""
        ops = [
            {"version": "v0.9", "createSurface": {"surfaceId": SURFACE_ID, "catalogId": CATALOG_ID}},
            {"version": "v0.9", "updateComponents": {"surfaceId": SURFACE_ID, "components": FLIGHT_SCHEMA}},
            {"version": "v0.9", "updateDataModel": {"surfaceId": SURFACE_ID, "path": "/", "value": {"origin": origin, "destination": destination, "airline": airline, "price": price}}},
        ]
        return json.dumps({"a2ui_operations": ops})

Key points:

  * The `Annotated` \+ `Field` parameters are essential — Microsoft Agent Framework serializes them into the tool's JSON schema, which is what the LLM sees when deciding what data to generate.
  * The tool builds the `a2ui_operations` container by hand and does not declare server-side action handlers. Button clicks are forwarded to the agent, but this example has no server-side handler for them.
  * `"book_flight"` is the action name used by the schema button and can be handled with the frontend APIs in the [Advanced — Action Handlers](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/a2ui/fixed-schema/advanced#action-handlers) guide.



### Register the tool#

src/agents/a2ui_fixed.py
    
    
    from agent_framework import Agent
    from agent_framework_ag_ui import AgentFrameworkAgent
    
    base_agent = Agent(
        client=chat_client,
        name="a2ui_fixed_agent",
        instructions="You help users find flights. Call `display_flight` with origin, destination, airline, and price.",
        tools=[display_flight],
    )
    
    agent = AgentFrameworkAgent(agent=base_agent)

### Configure the runtime (TypeScript)#

Enable A2UI in your CopilotRuntime. The middleware auto-detects A2UI operations in any tool result, so no tool injection is needed here — the agent's `display_flight` tool returns them directly.

app/api/copilotkit-a2ui-fixed-schema/route.ts
    
    
    const runtime = new CopilotRuntime({
      agents: { "a2ui-fixed-schema": fixedSchemaAgent },
      a2ui: {
        injectA2UITool: false,
      },
    });

## Action handler details#

The current Python SDK does not support the `action_handlers=` option. The button schema can still define the action context used by frontend handlers. Here's how the schema side looks:

### Button with action context#

In your `flight_schema.json`, buttons declare an `action` with data-bound context fields. When clicked, the values are resolved from that specific card's data:
    
    
    {
      "id": "book-button",
      "component": "Button",
      "child": "book-label",
      "variant": "primary",
      "action": {
        "event": {
          "name": "book_flight",
          "context": {
            "flightNumber": { "path": "flightNumber" },
            "price": { "path": "price" }
          }
        }
      }
    }

When this button is clicked on a card showing flight AA100 at $350, frontend action handling receives `context: { flightNumber: "AA100", price: "$350" }`. The Python `action_handlers=` path is not yet supported.

For custom frontend handling with `createA2UIMessageRenderer` and its `onAction` option, see the [Advanced — Action Handlers](https://docs.copilotkit.ai/ms-agent-dotnet/generative-ui/a2ui/fixed-schema/advanced#action-handlers) guide.

### On this page

How it worksImplementationCreate the A2UI schemaDefine the agent tool (Python)Register the toolConfigure the runtime (TypeScript)Action handler detailsButton with action context
