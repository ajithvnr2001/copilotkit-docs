---
url: https://docs.copilotkit.ai/crewai-crews/cookbook/oracle-agent-spec-memory/
title: Oracle Agent Memory
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:56:37.875975+00:00
---

# Oracle Agent Memory

> Source: https://docs.copilotkit.ai/crewai-crews/cookbook/oracle-agent-spec-memory/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCrewAI Flows

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/crewai-crews)[Quickstart](https://docs.copilotkit.ai/crewai-crews/quickstart)[Build with agents](https://docs.copilotkit.ai/crewai-crews/build-with-agents)[Intelligence](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/crewai-crews/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/crewai-crews/webmcp)

Agent capabilities

CrewAI Flows

[Sub-agents](https://docs.copilotkit.ai/crewai-crews/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/crewai-crews/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/crewai-crews/learning)

[User Memories](https://docs.copilotkit.ai/crewai-crews/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/crewai-crews/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/crewai-crews/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/crewai-crews/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/crewai-crews/intelligence/analytics)[Channels](https://docs.copilotkit.ai/crewai-crews/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/crewai-crews/telemetry)[Community frameworks](https://docs.copilotkit.ai/crewai-crews/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[CrewAI Flows](https://docs.copilotkit.ai/crewai-crews)[Cookbook](https://docs.copilotkit.ai/crewai-crews/cookbook)

# Oracle Agent Memory

Define an agent once in Oracle Agent Spec, run it on LangGraph over AG-UI, give it long-term memory on Oracle AI Database, and render it in CopilotKit with human-in-the-loop.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

[Oracle Agent Spec](https://github.com/oracle/agent-spec) is an open, framework-agnostic way to describe an agent as portable JSON — define it once, run it on any supported runtime. This recipe wires three things together: an Agent Spec agent running on **LangGraph** , served over the open [AG-UI](https://docs.ag-ui.com/) protocol, rendered in a [CopilotKit](https://www.copilotkit.ai/) chat, with **long-term memory** on Oracle AI Database so it remembers you across sessions.

The example is a personal **travel concierge** : it remembers your preferences across sessions, searches flights, and books them with a **human-in-the-loop** confirmation card rendered by CopilotKit's generative UI.

## How it works#

  * The agent is defined declaratively with `pyagentspec` and serialized to Agent Spec JSON.
  * The [`ag_ui_agentspec`](https://github.com/ag-ui-protocol/ag-ui) adapter loads that JSON and serves it as a FastAPI AG-UI endpoint on the LangGraph runtime.
  * CopilotKit consumes the AG-UI endpoint with an `HttpAgent` — the same protocol as any AG-UI agent.
  * Memory is the glue: a `recall_memory` tool reads durable preferences from Oracle Agent Memory, and each turn is persisted after the response streams — then a small reconcile pass supersedes outdated facts so an updated preference wins next time.


    
    
    CopilotKit (Next.js, V2) ──/api/copilotkit──▶ CopilotRuntime (HttpAgent)
                                                        │  AG-UI (SSE)
                                                        ▼
                                      Agent Spec JSON → ag_ui_agentspec (LangGraph)
                                         recall_memory · search_flights · book_flight (HITL ClientTool)
                                                        │  recall + persist
                                                        ▼
                                            oracleagentmemory → Oracle AI Database

## Memory: what's CopilotKit, what's Oracle#

![Memory ownership across the stack: CopilotKit owns the chat UI and threads, the AG-UI transport, and the generative UI; your agent code is the seam — Agent Spec on LangGraph, the recall_memory tool, and persist + reconcile; Oracle Agent Memory owns the Oracle AI Database, fact extraction, and vector recall.](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iNzIwIiBoZWlnaHQ9IjM2MCIgdmlld0JveD0iMCAwIDcyMCAzNjAiIHJvbGU9ImltZyIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8dGl0bGU+V2hhdCBDb3BpbG90S2l0IG93bnMgdmVyc3VzIHdoYXQgT3JhY2xlIG93bnMgaW4gdGhlIG1lbW9yeSBmZWF0dXJlPC90aXRsZT4KICA8ZGVzYz5UaHJlZSBjb2x1bW5zLiBDb3BpbG90S2l0IG93bnMgdGhlIGNoYXQgVUkgYW5kIHRocmVhZHMsIHRoZSBBRy1VSSB0cmFuc3BvcnQsIGFuZCB0aGUgZ2VuZXJhdGl2ZSBVSS4gWW91ciBhZ2VudCBjb2RlIGlzIHRoZSBzZWFtOiBBZ2VudCBTcGVjIG9uIExhbmdHcmFwaCwgdGhlIHJlY2FsbF9tZW1vcnkgdG9vbCwgYW5kIHBlcnNpc3QgcGx1cyByZWNvbmNpbGUuIE9yYWNsZSBBZ2VudCBNZW1vcnkgb3ducyB0aGUgT3JhY2xlIEFJIERhdGFiYXNlIHN0b3JhZ2UsIGZhY3QgZXh0cmFjdGlvbiwgYW5kIHZlY3RvciByZWNhbGwuIEEgdHVybiBmbG93cyBsZWZ0IHRvIHJpZ2h0IHRvIHJlY2FsbCwgdGhlbiB0aGUgYWdlbnQgcGVyc2lzdHMgYmFjayB0byBPcmFjbGUgYWZ0ZXIgdGhlIHR1cm4uPC9kZXNjPgogIDxzdHlsZT4KICAgIHRleHQgeyBmb250LWZhbWlseTogLWFwcGxlLXN5c3RlbSwgQmxpbmtNYWNTeXN0ZW1Gb250LCAiU2Vnb2UgVUkiLCBSb2JvdG8sIEhlbHZldGljYSwgQXJpYWwsIHNhbnMtc2VyaWY7IH0KICAgIC5oIHsgZm9udC1zaXplOiAxNHB4OyBmb250LXdlaWdodDogNTAwOyB9CiAgICAudCB7IGZvbnQtc2l6ZTogMTRweDsgZm9udC13ZWlnaHQ6IDUwMDsgfQogICAgLnMgeyBmb250LXNpemU6IDEycHg7IGZvbnQtd2VpZ2h0OiA0MDA7IH0KICAgIC5jYXAgeyBmb250LXNpemU6IDEyLjVweDsgZmlsbDogIzQ3NTU2OTsgfQogICAgLmNhcHRpdGxlIHsgZm9udC1zaXplOiAxM3B4OyBmb250LXdlaWdodDogNTAwOyBmaWxsOiAjMGYxNzJhOyB9CiAgICAuYXJyIHsgZm9udC1zaXplOiAxNnB4OyBmaWxsOiAjOTRhM2I4OyB9CiAgPC9zdHlsZT4KCiAgPHJlY3QgeD0iMC41IiB5PSIwLjUiIHdpZHRoPSI3MTkiIGhlaWdodD0iMzU5IiByeD0iMTQiIGZpbGw9IiNmZmZmZmYiIHN0cm9rZT0iI2U1ZTdlYiIvPgoKICA8IS0tIENvcGlsb3RLaXQgKGJsdWUpIC0tPgogIDxyZWN0IHg9IjI0IiB5PSIzNiIgd2lkdGg9IjIxMiIgaGVpZ2h0PSIzMCIgcng9IjgiIGZpbGw9IiNkYmVhZmUiIHN0cm9rZT0iIzNiODJmNiIvPgogIDx0ZXh0IGNsYXNzPSJoIiB4PSIxMzAiIHk9IjU2IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMWUzYThhIj5Db3BpbG90S2l0PC90ZXh0PgogIDxyZWN0IHg9IjI0IiB5PSI4MCIgd2lkdGg9IjIxMiIgaGVpZ2h0PSI0NiIgcng9IjgiIGZpbGw9IiNlZmY2ZmYiIHN0cm9rZT0iIzNiODJmNiIvPgogIDx0ZXh0IGNsYXNzPSJ0IiB4PSIxMzAiIHk9IjEwMSIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzFlM2E4YSI+Q2hhdCBVSSAmYW1wOyB0aHJlYWRzPC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJzIiB4PSIxMzAiIHk9IjExNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzFkNGVkOCI+dGhlIGNvbnZlcnNhdGlvbiBzdXJmYWNlPC90ZXh0PgogIDxyZWN0IHg9IjI0IiB5PSIxMzgiIHdpZHRoPSIyMTIiIGhlaWdodD0iNDYiIHJ4PSI4IiBmaWxsPSIjZWZmNmZmIiBzdHJva2U9IiMzYjgyZjYiLz4KICA8dGV4dCBjbGFzcz0idCIgeD0iMTMwIiB5PSIxNTkiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMxZTNhOGEiPkFHLVVJIHRyYW5zcG9ydDwvdGV4dD4KICA8dGV4dCBjbGFzcz0icyIgeD0iMTMwIiB5PSIxNzUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMxZDRlZDgiPnN0cmVhbXMgb3ZlciBTU0U8L3RleHQ+CiAgPHJlY3QgeD0iMjQiIHk9IjE5NiIgd2lkdGg9IjIxMiIgaGVpZ2h0PSI0NiIgcng9IjgiIGZpbGw9IiNlZmY2ZmYiIHN0cm9rZT0iIzNiODJmNiIvPgogIDx0ZXh0IGNsYXNzPSJ0IiB4PSIxMzAiIHk9IjIxNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzFlM2E4YSI+R2VuZXJhdGl2ZSBVSTwvdGV4dD4KICA8dGV4dCBjbGFzcz0icyIgeD0iMTMwIiB5PSIyMzMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMxZDRlZDgiPmNoaXAsIGNhcmRzLCBISVRMPC90ZXh0PgoKICA8dGV4dCBjbGFzcz0iYXJyIiB4PSIyNDUiIHk9IjU3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIj4mIzg1OTQ7PC90ZXh0PgoKICA8IS0tIFlvdXIgYWdlbnQgY29kZSAoc2xhdGUpIC0tPgogIDxyZWN0IHg9IjI1NCIgeT0iMzYiIHdpZHRoPSIyMTIiIGhlaWdodD0iMzAiIHJ4PSI4IiBmaWxsPSIjZTJlOGYwIiBzdHJva2U9IiM5NGEzYjgiLz4KICA8dGV4dCBjbGFzcz0iaCIgeD0iMzYwIiB5PSI1NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzBmMTcyYSI+WW91ciBhZ2VudCBjb2RlPC90ZXh0PgogIDxyZWN0IHg9IjI1NCIgeT0iODAiIHdpZHRoPSIyMTIiIGhlaWdodD0iNDYiIHJ4PSI4IiBmaWxsPSIjZjFmNWY5IiBzdHJva2U9IiM5NGEzYjgiLz4KICA8dGV4dCBjbGFzcz0idCIgeD0iMzYwIiB5PSIxMDEiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiMwZjE3MmEiPkFnZW50IFNwZWMgKyBMYW5nR3JhcGg8L3RleHQ+CiAgPHRleHQgY2xhc3M9InMiIHg9IjM2MCIgeT0iMTE3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjNDc1NTY5Ij5kZWNpZGVzIHdoZW4gdG8gcmVjYWxsPC90ZXh0PgogIDxyZWN0IHg9IjI1NCIgeT0iMTM4IiB3aWR0aD0iMjEyIiBoZWlnaHQ9IjQ2IiByeD0iOCIgZmlsbD0iI2YxZjVmOSIgc3Ryb2tlPSIjOTRhM2I4Ii8+CiAgPHRleHQgY2xhc3M9InQiIHg9IjM2MCIgeT0iMTU5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjMGYxNzJhIj5yZWNhbGxfbWVtb3J5IHRvb2w8L3RleHQ+CiAgPHRleHQgY2xhc3M9InMiIHg9IjM2MCIgeT0iMTc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjNDc1NTY5Ij5xdWVyaWVzIE9yYWNsZSwgZmlsdGVyczwvdGV4dD4KICA8cmVjdCB4PSIyNTQiIHk9IjE5NiIgd2lkdGg9IjIxMiIgaGVpZ2h0PSI0NiIgcng9IjgiIGZpbGw9IiNmMWY1ZjkiIHN0cm9rZT0iIzk0YTNiOCIvPgogIDx0ZXh0IGNsYXNzPSJ0IiB4PSIzNjAiIHk9IjIxNyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzBmMTcyYSI+UGVyc2lzdCArIHJlY29uY2lsZTwvdGV4dD4KICA8dGV4dCBjbGFzcz0icyIgeD0iMzYwIiB5PSIyMzMiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZpbGw9IiM0NzU1NjkiPnNhdmVzICZhbXA7IHN1cGVyc2VkZXMgZmFjdHM8L3RleHQ+CgogIDx0ZXh0IGNsYXNzPSJhcnIiIHg9IjQ3NSIgeT0iNTciIHRleHQtYW5jaG9yPSJtaWRkbGUiPiYjODU5NDs8L3RleHQ+CgogIDwhLS0gT3JhY2xlIEFnZW50IE1lbW9yeSAoY29yYWwpIC0tPgogIDxyZWN0IHg9IjQ4NCIgeT0iMzYiIHdpZHRoPSIyMTIiIGhlaWdodD0iMzAiIHJ4PSI4IiBmaWxsPSIjZmZlNGU2IiBzdHJva2U9IiNmYjcxODUiLz4KICA8dGV4dCBjbGFzcz0iaCIgeD0iNTkwIiB5PSI1NiIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iIzlmMTIzOSI+T3JhY2xlIEFnZW50IE1lbW9yeTwvdGV4dD4KICA8cmVjdCB4PSI0ODQiIHk9IjgwIiB3aWR0aD0iMjEyIiBoZWlnaHQ9IjQ2IiByeD0iOCIgZmlsbD0iI2ZmZjFmMiIgc3Ryb2tlPSIjZmI3MTg1Ii8+CiAgPHRleHQgY2xhc3M9InQiIHg9IjU5MCIgeT0iMTAxIiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjOWYxMjM5Ij5PcmFjbGUgQUkgRGF0YWJhc2U8L3RleHQ+CiAgPHRleHQgY2xhc3M9InMiIHg9IjU5MCIgeT0iMTE3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjYmUxMjNjIj5zdG9yZXMgZXZlcnkgcmVjb3JkPC90ZXh0PgogIDxyZWN0IHg9IjQ4NCIgeT0iMTM4IiB3aWR0aD0iMjEyIiBoZWlnaHQ9IjQ2IiByeD0iOCIgZmlsbD0iI2ZmZjFmMiIgc3Ryb2tlPSIjZmI3MTg1Ii8+CiAgPHRleHQgY2xhc3M9InQiIHg9IjU5MCIgeT0iMTU5IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjOWYxMjM5Ij5GYWN0IGV4dHJhY3Rpb248L3RleHQ+CiAgPHRleHQgY2xhc3M9InMiIHg9IjU5MCIgeT0iMTc1IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjYmUxMjNjIj5kaXN0aWxscyBkdXJhYmxlIGZhY3RzPC90ZXh0PgogIDxyZWN0IHg9IjQ4NCIgeT0iMTk2IiB3aWR0aD0iMjEyIiBoZWlnaHQ9IjQ2IiByeD0iOCIgZmlsbD0iI2ZmZjFmMiIgc3Ryb2tlPSIjZmI3MTg1Ii8+CiAgPHRleHQgY2xhc3M9InQiIHg9IjU5MCIgeT0iMjE3IiB0ZXh0LWFuY2hvcj0ibWlkZGxlIiBmaWxsPSIjOWYxMjM5Ij5WZWN0b3IgcmVjYWxsPC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJzIiB4PSI1OTAiIHk9IjIzMyIgdGV4dC1hbmNob3I9Im1pZGRsZSIgZmlsbD0iI2JlMTIzYyI+c2VtYW50aWMgc2VhcmNoPC90ZXh0PgoKICA8bGluZSB4MT0iMjQiIHkxPSIyNjIiIHgyPSI2OTYiIHkyPSIyNjIiIHN0cm9rZT0iI2U1ZTdlYiIvPgogIDx0ZXh0IGNsYXNzPSJjYXB0aXRsZSIgeD0iMjQiIHk9IjI4NSIgdGV4dC1hbmNob3I9InN0YXJ0Ij5Ib3cgb25lIHR1cm4gZmxvd3M8L3RleHQ+CiAgPHRleHQgY2xhc3M9ImNhcCIgeD0iMjQiIHk9IjMwNyIgdGV4dC1hbmNob3I9InN0YXJ0Ij4mIzkzMTI7IHJlY2FsbCAmIzgyMTI7IENvcGlsb3RLaXQgJiM4NTk0OyBhZ2VudCAmIzg1OTQ7IE9yYWNsZSwgdGhlbiBnZW5lcmF0aXZlIFVJIHN0cmVhbXMgYmFjayB0byBjaGF0PC90ZXh0PgogIDx0ZXh0IGNsYXNzPSJjYXAiIHg9IjI0IiB5PSIzMjkiIHRleHQtYW5jaG9yPSJzdGFydCI+JiM5MzEzOyBwZXJzaXN0ICYjODIxMjsgYWZ0ZXIgdGhlIHR1cm4sIHRoZSBhZ2VudCBzYXZlcyBpdDsgT3JhY2xlIGV4dHJhY3RzIGFuZCBzdXBlcnNlZGVzIGZhY3RzPC90ZXh0Pgo8L3N2Zz4K)

Oracle does the remembering, CopilotKit does the conversing, and your agent code is the seam between them. CopilotKit never touches the database — to it, `recall_memory` is just a tool that returns text — and Oracle never sees the chat protocol. Swap Oracle for another store and the frontend doesn't change a line.

## Try it live#

Talk to the concierge below. Tell it a travel preference, then open a **new thread** with **"+ New thread"** and ask about your preferences again — it recalls what you told it from memory persisted in Oracle AI Database, not from the current conversation.

## Prerequisites#

  * **Python 3.12** (required — `oracleagentmemory` ships a cp312 wheel), [`uv`](https://docs.astral.sh/uv/), Node.js 20+
  * Docker (for the local Oracle AI Database) or your own Oracle AI Database
  * `OPENAI_API_KEY` (defaults use OpenAI via litellm)



Pre-release dependencies

This frontend uses CopilotKit **V2** pre-release builds so Agent Spec's human-in-the-loop renders, and the `ag_ui_agentspec` adapter is installed from the `ag-ui` repo (not PyPI). Both are pinned in the manifests.

## Start the database and run the agent#
    
    
    git clone https://github.com/CopilotKit/CopilotKit.git
    cd CopilotKit/examples/showcases/oracle-agent-memory
    
    docker compose up -d                 # wait for "DATABASE IS READY TO USE"
    ./db/setup-db.sh                     # create the cookbook DB user (idempotent)
    
    cd agent
    cp .env.example .env                 # add your OPENAI_API_KEY
    uv sync
    uv run uvicorn concierge.server:app --reload --port 8000

## Run the frontend#
    
    
    cd frontend
    cp .env.local.example .env.local     # optional; defaults to localhost:8000/run
    npm install
    npm run dev

Open `http://localhost:3000`.

## Try it#

**Frontend at a glance:** the left panel lists your conversation threads with a **"+ New thread"** button. `search_flights` renders interactive flight-option cards with a **"Select this flight"** button, `recall_memory` shows a **"🧠 Remembered your preferences"** chip you can click to expand and see exactly which preferences it pulled, and booking surfaces a **"Confirm your booking"** card (Confirm / Cancel) that stamps into a **boarding-pass ticket** once confirmed.

  1. Tell it: _"I'm vegetarian, I fly from SFO, and I prefer an aisle seat."_
  2. Click **"+ New thread"** in the sidebar (instead of reloading), then ask: _"Find me a flight to Amsterdam."_
  3. It recalls your preferences from Oracle — home airport SFO, aisle seat, vegetarian meal — and surfaces flights like **AMS-001 (KLM KL606, nonstop, $740)** personalized to what it remembered, not what you said in this thread.



**Book it:** select a flight from the cards (or ask _"Book me flight AMS-001 to Amsterdam"_), then click **Confirm & book** on the confirmation card to receive the boarding pass. `book_flight` is implemented as a CopilotKit **ClientTool** (`useHumanInTheLoop`) executed on the frontend, so the confirm→book step resolves within a single agent run. Follow-up messages in the same thread work too — search, pick, confirm, and keep chatting (see the note below).

Recall is eventually consistent

Memory is written and indexed asynchronously, so a fact you just taught becomes recallable after a brief delay (typically seconds). In a normal "come back later" session that delay is invisible; only a teach-then-ask within the same few seconds can outrun indexing.

Multi-turn works via a server-side workaround

Follow-ups after a server-tool call would otherwise hit an upstream Agent Spec × AG-UI adapter bug (`tool_call_id` correlation) that corrupts the replayed history and 400s on the next turn. The cookbook works around it in `agent/concierge/server.py` by replacing the adapter's incremental message merge with a full-history _replace_ each turn, so multi-turn conversations — and the confirm→book human-in-the-loop — work end to end. The **"+ New thread"** step above proves cross-session recall (memory is user-scoped, so a fresh thread still remembers you) — not a workaround for broken follow-ups. Details + the upstream fix we're tracking: [`agentspec-multiturn-toolcall-correlation`](https://github.com/CopilotKit/CopilotKit/blob/main/examples/showcases/oracle-agent-memory/docs/known-issues/agentspec-multiturn-toolcall-correlation.md).

## The key pieces, in code#

Memory recall is exposed as an Agent Spec `ServerTool`, so the portable spec itself declares the capability; `book_flight` is a CopilotKit **ClientTool** so the confirmation card is rendered on the frontend via `useHumanInTheLoop` and the entire flow completes in a single agent run:

agent/concierge/tools.py
    
    
    book_flight_tool = ClientTool(
        name="book_flight",
        description="Book the chosen flight by its id. The traveler confirms in the UI before it is finalized.",
        inputs=[_str_prop("flight_id", "The id of the flight to book, e.g. 'AMS-001'.")],
        outputs=[_str_prop("confirmation", "Human-readable booking confirmation.")],
    )

The agent is defined once and serialized to portable JSON:

agent/concierge/agent.py
    
    
    return Agent(
        name="travel_concierge",
        llm_config=llm,
        system_prompt=SYSTEM_PROMPT,
        tools=TOOLS,
        human_in_the_loop=True,
    )

The adapter has no post-run hook, so the server persists each turn to Oracle Agent Memory after the AG-UI stream drains (see `agent/concierge/server.py`).

## Going further#

  * **Per-user memory** — the cookbook defaults to a single `demo-user`. The stock adapter does not forward `forwarded_props`, so scope `user_id` via a FastAPI dependency / ContextVar (see `agent/concierge/tools.py`).
  * **Swap the runtime** — Agent Spec's adapter also supports Oracle's WayFlow runtime; the same spec runs on either.
  * **Memory reconciliation** — after each turn a small LLM pass (`reconcile_durable_memories` in `agent/concierge/reconcile.py`) prunes outdated or duplicate durable facts so an updated preference supersedes the old one on recall. Swap in your own policy (e.g. keep history, or reconcile on a schedule).



## Get started with a coding agent#

Want to build this yourself? Paste this into your coding agent (Claude Code, Cursor, …):
    
    
    Build a CopilotKit chat backed by a portable Oracle Agent Spec agent with
    long-term memory on Oracle AI Database. Requirements:
    
    - A Python FastAPI agent that defines an Oracle Agent Spec `Agent` (via
      `pyagentspec`) with three tools: `recall_memory` (reads durable preferences from
      Oracle Agent Memory via `oracleagentmemory`), `search_flights` (a mock flight
      search returning cards like AMS-001 KLM KL606 $740 nonstop), and `book_flight`
      (a CopilotKit `ClientTool` — Agent Spec `ClientTool` — gated in the UI via
      `useHumanInTheLoop` for human-in-the-loop in a single agent run).
    - Serialize the agent to Agent Spec JSON and serve it over AG-UI on the LangGraph
      runtime with the `ag_ui_agentspec` adapter (`add_agentspec_fastapi_endpoint`).
      The adapter has no post-run hook, so persist each turn to Oracle Agent Memory
      after the AG-UI stream drains.
    - A Next.js CopilotKit frontend that proxies to the agent over AG-UI with
      `HttpAgent`, so the agent owns the LLM call (use CopilotKit's empty runtime
      adapter). The frontend renders generative UI: `search_flights` → flight-option
      cards, `recall_memory` → a "🧠 Remembered your preferences" chip, and
      `book_flight` → a confirmation card that stamps into a boarding-pass ticket. A
      collapsible left sidebar lists conversation threads with a "+ New thread" button.
    - Use Oracle AI Database (Docker image `container-registry.oracle.com/database/free`)
      as the memory store; connect with `oracledb` and litellm embeddings.
    
    Walk me through it step by step, starting with the agent.

## Get the code#

Full source: [`examples/showcases/oracle-agent-memory`](https://github.com/CopilotKit/CopilotKit/tree/main/examples/showcases/oracle-agent-memory) — `agent/` (the Agent Spec agent) and `frontend/` (the CopilotKit V2 chat).

### On this page

How it worksMemory: what's CopilotKit, what's OracleTry it livePrerequisitesStart the database and run the agentRun the frontendTry itThe key pieces, in codeGoing furtherGet started with a coding agentGet the code
