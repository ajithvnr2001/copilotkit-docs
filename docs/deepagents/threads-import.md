---
url: https://docs.copilotkit.ai/deepagents/threads-import/
title: Add AG-UI Streams to Existing Threads
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:01:01.074194+00:00
---

# Add AG-UI Streams to Existing Threads

> Source: https://docs.copilotkit.ai/deepagents/threads-import/

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

[Overview](https://docs.copilotkit.ai/deepagents/threads)[Bring your own thread system](https://docs.copilotkit.ai/deepagents/intelligence/bring-your-own-thread-system)[Add to Existing Threads](https://docs.copilotkit.ai/deepagents/threads-import)[Thread & History Lifecycle](https://docs.copilotkit.ai/deepagents/threads-lifecycle)[Streams & Framework Threads](https://docs.copilotkit.ai/deepagents/intelligence/threads-explained)

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

Add to Existing Threads

IntelligenceFeaturesAG-UI Streams

# Add AG-UI Streams to Existing Threads

Add Intelligence’s AG-UI streams to your existing agent conversations, with optional historical import for supported stores.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Add Intelligence to your existing app#

Add reconnection, catch-up, and delivery across devices to the conversations your agent already manages. Follow the [Intelligence quickstart](https://docs.copilotkit.ai/deepagents/intelligence/quickstart) to connect your existing CopilotKit app and Runtime, then verify that a new conversation is saved. That setup enables AG-UI streams for runs through CopilotKit; importing old conversations is not required.

Your framework continues managing agent context and execution state. Keep your durable LangGraph checkpointer or durable ADK session service configured and keep the mapping between CopilotKit `threadId` values and native framework conversation identifiers stable. See [AG-UI Streams & Framework Threads](https://docs.copilotkit.ai/deepagents/intelligence/threads-explained#how-threads-work-with-framework-storage) for the responsibilities of each layer.

For a concrete example without historical import, see [keep an existing LangGraph conversation](https://docs.copilotkit.ai/deepagents/intelligence/bring-your-own-thread-system#example-keep-an-existing-langgraph-conversation).

## Include earlier conversations (optional)#

If you also want users to reopen history recorded before Intelligence was connected, copy supported history into Intelligence using the steps below. This guide covers Google ADK, LangGraph, and Mastra stores. It copies historical content; it does not enable live delivery, recover past execution, or establish ongoing database replication.

Use Threads Drawer or `useThreads` to select a conversation, and pass its `threadId` to your chat. Imported and new conversations then use the same UI. Importing cannot recover content the source no longer exposes.

## Supported sources#

Source| Import guide| Supported history  
---|---|---  
Google ADK| [Add AG-UI streams to ADK sessions](https://docs.copilotkit.ai/google-adk/threads-import)| Persisted ADK sessions from a database session service or Vertex/Agent Engine session service.  
LangGraph| [Add AG-UI streams to LangGraph threads](https://docs.copilotkit.ai/langgraph-python/threads-import)| LangGraph Server, LangGraph Platform, or LangSmith Deployment threads exposed through the LangGraph SDK thread/run APIs.  
Mastra| [Add AG-UI streams to Mastra conversations](https://docs.copilotkit.ai/mastra/threads-import)| Saved conversations from a local LibSQL database or a Mastra server.  
  
## What gets imported?#

The importer preserves conversation content that can render in the CopilotKit chat UI or help downstream learning systems:

  * user, assistant, tool, system, and developer messages
  * tool calls and tool results
  * reasoning traces when the source exposes them
  * media that can be resolved during extraction
  * saved agent state when supported by the source
  * original timestamps
  * import provenance and per-conversation import outcomes



It does not import framework transport noise, LangSmith traces, or unsupported source stores. What is available depends on what your source saved; see your framework’s import guide for details.

## Import flow#

### Confirm the target project#

Choose the Intelligence project that will receive the history. Its app-api URL and project-scoped runtime key select the destination. You will export those values before importing.

For a CLI-created app, you can select a cloud-hosted project:

Terminal
    
    
    npx copilotkit@latest project select

The command updates the project selected for the current directory and writes its project-scoped runtime key to the app's generated `.env`.

### Run a dry run#

A dry run reads the source, discovers source agent keys, counts conversations, reports skips, and estimates upload size without opening an import batch. It does not need a CopilotKit Intelligence URL or API key.

ADKLangGraphMastra

[Configure the ADK source](https://docs.copilotkit.ai/google-adk/threads-import#configure-the-source), then run:
    
    
    npx copilotkit@latest import --source adk --dry-run

[Configure the LangGraph source](https://docs.copilotkit.ai/langgraph-python/threads-import#configure-the-source) and its user IDs, then run:
    
    
    npx copilotkit@latest import --source langgraph --user-source metadata.user_id --dry-run

Configure your source using the [Mastra import guide](https://docs.copilotkit.ai/mastra/threads-import#configure-the-source), then run:
    
    
    npx copilotkit@latest import --source mastra --dry-run

### Map source agents#

The importer maps each source agent key to the `agentId` your live CopilotKit runtime uses. Use the same agent ID for import and later runs. The imported application user ID must also match the ID returned by your runtime's `identifyUser`.

For scripted imports, put the mapping in a JSON file:

agent-map.json
    
    
    {
      "support-agent": "support-agent",
      "sales-agent": "sales-agent"
    }

### Prepare the CopilotKit Intelligence destination#

A real import needs the destination app-api URL and project-scoped runtime key. A CLI-created starter writes them to `.env`, but the importer reads the current process environment and does not load `.env` or `.copilotkit/project.json` automatically.

Copy the generated values into your shell before importing:

Terminal
    
    
    export INTELLIGENCE_API_URL="https://..."
    export CPK_INTELLIGENCE_API_KEY="cpk-..."

`COPILOTKIT_API_KEY` is also accepted for the key. You can pass the same values directly with `--api-url` and `--api-key` instead.

### Run the import#

Run the source-specific import after the dry run looks right:

  * [Add AG-UI streams to ADK sessions](https://docs.copilotkit.ai/google-adk/threads-import)
  * [Add AG-UI streams to LangGraph threads](https://docs.copilotkit.ai/langgraph-python/threads-import)
  * [Add AG-UI streams to Mastra conversations](https://docs.copilotkit.ai/mastra/threads-import)



Already-imported threads are skipped by default. Use `--replace` to refresh them; running or continued threads are left unchanged.

### Verify the imported conversations#

Sign in as the application user assigned to the imported conversation. Open it from the Threads Drawer and make sure that its history appears. Send a message and make sure that your native framework continues the same conversation.

### Continue using your framework's persistence#

Your app sends future conversations that run through CopilotKit to CopilotKit Intelligence. Keep your durable LangGraph or ADK persistence configured so those runs continue using both persistence layers. Reopen a conversation with the same CopilotKit `threadId` and a stable mapping to its native thread or session so its history stays continuous.

Importing copies supported history; it does not establish ongoing database replication. Intelligence rename, archive, and delete operations affect only Intelligence records.

  * **Threads Drawer:** already included in CLI-created starters. Use the [Threads Drawer guide](https://docs.copilotkit.ai/deepagents/prebuilt-components/copilot-threads-drawer) to customize its ready-made thread UI.
  * **Headless Threads:** use the [Headless Threads guide](https://docs.copilotkit.ai/deepagents/headless-threads) only when you need a custom UI. Select a thread with `useThreads`, store its `thread.id`, and pass that value to your chat component as `threadId`.



Use the imported `thread.id` returned by the Drawer or `useThreads` when you reopen the conversation. Keep any mapping to the native ID unchanged.

For the underlying persistence and replay model, see [AG-UI Streams & Framework Threads](https://docs.copilotkit.ai/deepagents/intelligence/threads-explained).

## Deployment notes#

  * **Cloud-hosted CopilotKit Intelligence:** export the destination values generated in the CLI-created app's `.env`, or pass them with `--api-url` and `--api-key`. `project select` can rewrite the app's generated values, but the importer still reads only flags or the current process environment. See [Cloud-hosted CopilotKit Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/managed-intelligence-platform).
  * **Self-hosted CopilotKit Intelligence:** pass the deployment's app-api URL with `--api-url` and a project-scoped `cpk` runtime key with `--api-key`. See [Self-host CopilotKit Intelligence](https://docs.copilotkit.ai/deepagents/intelligence/self-hosting).



### On this page

Add Intelligence to your existing appInclude earlier conversations (optional)Supported sourcesWhat gets imported?Import flowDeployment notes
