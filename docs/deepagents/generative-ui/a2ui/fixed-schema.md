---
url: https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/fixed-schema/
title: Fixed Schema A2UI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:59:59.288790+00:00
---

# Fixed Schema A2UI

> Source: https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/fixed-schema/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendDeep Agents

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/deepagents)[Quickstart](https://docs.copilotkit.ai/deepagents/quickstart)[Build with agents](https://docs.copilotkit.ai/deepagents/build-with-agents)[Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/deepagents/frontend-tools)

Generative UI

Controlled

Declarative

[A2UI](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui)

[Dynamic Schema A2UI](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/dynamic-schema)[Fixed Schema A2UI](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/fixed-schema)

[JSON Render](https://docs.copilotkit.ai/deepagents/generative-ui/json-render)[Hashbrown](https://docs.copilotkit.ai/deepagents/generative-ui/hashbrown)

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/deepagents/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/deepagents/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/deepagents/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/deepagents/learning)

[User Memories](https://docs.copilotkit.ai/deepagents/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/deepagents/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/deepagents/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/deepagents/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/deepagents/intelligence/analytics)[Channels](https://docs.copilotkit.ai/deepagents/intelligence/channels)

Hosting

Backend

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

[Open-source telemetry](https://docs.copilotkit.ai/deepagents/telemetry)[Community frameworks](https://docs.copilotkit.ai/deepagents/community-frameworks)

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
  3. Tool returns `a2ui.render()` with createSurface + updateComponents + updateDataModel
  4. The A2UI middleware intercepts the tool result and renders the surface



## Implementation#

### Create the A2UI schema#

Design your schema using the [A2UI Composer](https://a2ui-composer.ag-ui.com/) or write it by hand. Save it as a JSON file:
    
    
    apps/agent/src/a2ui/schemas/flight_schema.json

### Define the agent tool (Python)#

apps/agent/src/a2ui_fixed_schema.py
    
    
    from copilotkit import a2ui
    from langchain.tools import tool
    from pathlib import Path
    from typing import TypedDict
    
    class Flight(TypedDict):
        id: str
        airline: str
        airlineLogo: str
        flightNumber: str
        origin: str
        destination: str
        date: str
        departureTime: str
        arrivalTime: str
        duration: str
        status: str
        statusIcon: str
        price: str
    
    SURFACE_ID = "flight-search-results"
    FLIGHT_SCHEMA = a2ui.load_schema(
        Path(__file__).parent / "a2ui" / "schemas" / "flight_schema.json"
    )
    
    
    @tool
    def search_flights(flights: list[Flight]) -> str:
        """Search for flights and display results as rich cards."""
        return a2ui.render(
            operations=[
                a2ui.create_surface(SURFACE_ID),
                a2ui.update_components(SURFACE_ID, FLIGHT_SCHEMA),
                a2ui.update_data_model(SURFACE_ID, {"flights": flights}),
            ],
        )

Key points:

  * The `Flight` TypedDict is essential — LangChain serializes it into the tool's JSON schema, which is what the LLM sees when deciding what data to generate.
  * The Python SDK's `a2ui.render` does not yet support the `action_handlers=` keyword, so the example keeps the button schema but does not declare server-side handlers. Button clicks are forwarded to the agent, but this example has no server-side handler for them.
  * `"book_flight"` is the action name used by the schema button and can be handled with the frontend APIs in the [Advanced — Action Handlers](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/fixed-schema/advanced#action-handlers) guide.



### Register the tool#

apps/agent/main.py
    
    
    from deepagents import create_deep_agent
    from src.a2ui_fixed_schema import search_flights
    
    agent = create_deep_agent(
        tools=[search_flights, ...],
        ...
    )

### Configure the runtime (TypeScript)#

Enable A2UI in your CopilotRuntime:

app/api/copilotkit/route.ts
    
    
    const runtime = new CopilotRuntime({
      agents: { default: myAgent },
      a2ui: {
        injectA2UITool: true,
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

For custom frontend handling with `createA2UIMessageRenderer` and its `onAction` option, see the [Advanced — Action Handlers](https://docs.copilotkit.ai/deepagents/generative-ui/a2ui/fixed-schema/advanced#action-handlers) guide.

### On this page

How it worksImplementationCreate the A2UI schemaDefine the agent tool (Python)Register the toolConfigure the runtime (TypeScript)Action handler detailsButton with action context
