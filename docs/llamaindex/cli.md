---
url: https://docs.copilotkit.ai/llamaindex/cli/
title: CopilotKit CLI
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:14:19.822939+00:00
---

# CopilotKit CLI

> Source: https://docs.copilotkit.ai/llamaindex/cli/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[LlamaIndex](https://docs.copilotkit.ai/llamaindex)

# CopilotKit CLI

Use the CopilotKit CLI to create apps, sign in to cloud-hosted CopilotKit Intelligence, select projects, provision runtime API keys, import historical conversations, and install agent skills.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is this?#

The CopilotKit CLI helps you create CopilotKit apps connected to CopilotKit Intelligence, whether cloud-hosted or self-hosted. It handles browser sign-in, project selection, project-scoped runtime API keys, historical thread import, and local project configuration so your app can use threads and conversation history.

Use the CLI when you want to start a new app, import historical ADK or LangGraph conversations, or install CopilotKit agent skills for your coding agent.

[Start cloud-hosted Intelligence onboardingSign up or sign in, finish organization onboarding when required, then return to the CLI to select a project and connect your app.Start cloud-hosted setup](https://intelligence.copilotkit.ai/?utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_cli_intro_signup&utm_frontend=react&utm_backend=llamaindex)

## Prerequisites#

  * Node.js 20+
  * A CopilotKit account for cloud-hosted CopilotKit Intelligence
  * An OpenAI API key or another model provider key for the starter app you choose



Team Self-hosted is a plan

Team Self-hosted is the plan for a self-hosted deployment. You choose it on the cloud-hosted account. The deployment uses your identity provider.

## Start a new app#

Creating vs. adding to an existing app

`init` (aliased as `create`) scaffolds a brand-new project in its own directory — it prompts for an app name and does not detect or bootstrap an app you already have. To add CopilotKit to an existing app, follow the manual installation in the [Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart) instead.

### Run create#

Terminal
    
    
    npx copilotkit@latest create

The CLI prompts for the app name and framework, opens browser sign-in when needed, scaffolds the starter, and connects the app to a cloud-hosted CopilotKit Intelligence project.

### Sign up or sign in#

If you are not already signed in, the CLI opens a browser login flow. A new account accepts the CopilotKit Self-Service Agreement. An account that already accepted it does not accept it again.

If the browser does not open, the CLI prints a login URL and supports a manual paste fallback.

### Select or create an organization#

Select or create an organization in the browser. A new organization chooses the Developer plan or a paid plan. Developer is the no-cost plan. Read [Plans](https://docs.copilotkit.ai/llamaindex/intelligence/plans) when you want to change that choice.

### Return to the terminal#

After organization onboarding, return to the terminal. The original CLI command resumes and prompts you to select or create a project.

### Select or create a project#

Choose an existing cloud-hosted project or create a new one. A project is where your app's threads, messages, and platform metadata are stored.

The CLI writes the selected project to `.copilotkit/project.json`:

.copilotkit/project.json
    
    
    {
      "projectId": "proj_...",
      "projectSlug": "support-assistant",
      "clerkOrgId": "org_..."
    }

### Use the generated environment#

`init` and its `create` alias write the cloud-hosted platform URLs, `SL_ENABLED`, and project-scoped runtime API key to `.env`.

.env
    
    
    INTELLIGENCE_API_URL=https://...
    INTELLIGENCE_GATEWAY_WS_URL=wss://...
    CPK_INTELLIGENCE_API_KEY=cpk-...
    CPK_TELEMETRY_ID=...
    SL_ENABLED=true

Keep `CPK_INTELLIGENCE_API_KEY` on the server side. The project key connects the Runtime to Intelligence. `CPK_TELEMETRY_ID` is an optional, non-secret analytics identity.

Cloud-hosted setup does not issue `COPILOTKIT_LICENSE_TOKEN`. That token is only for offline or self-hosted licensing and does not replace the cloud-hosted project API key.

### Start development#

Terminal
    
    
    npm run dev

The starter runs your local app and runtime while storing threads in the cloud-hosted project selected by the CLI.

## Evaluate Intelligence locally#

To try Intelligence without a cloud-hosted project, run it in Docker on your own machine. Local evaluation is a preview supported on macOS with Docker Desktop. Read [Evaluate Intelligence locally](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting-local) for the supported preview scope. From your app's folder:

Terminal
    
    
    npx copilotkit@latest local setup
    npx copilotkit@latest local connect --approve-connection

The CLI checks Docker, gets an evaluation license for your organization, installs the latest release, and connects the app to it. Read [Evaluate Intelligence locally](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting-local) for requirements, dashboard sign-in, and model setup.

Command| What it does  
---|---  
`npx copilotkit@latest local status`| Shows service health, URLs, and any failed setup step.  
`npx copilotkit@latest local start`| Starts the app's local stack.  
`npx copilotkit@latest local stop`| Stops the stack and keeps its data.  
`npx copilotkit@latest local login`| Opens the local dashboard and signs you in.  
`npx copilotkit@latest local setup`| Installs the stack, configures the Automatic Learning model, or resumes setup.  
`npx copilotkit@latest local update`| Updates the stack to the latest release and keeps its data.  
`npx copilotkit@latest local renew`| Renews the evaluation license.  
`npx copilotkit@latest local delete`| Asks, then deletes the stack and its data.  
  
## Import and synchronize historical conversations#

Use `import` from a CopilotKit app created with the CLI and CopilotKit Intelligence enabled. The importer targets the CopilotKit Intelligence project already selected for the current directory.

ADKLangGraph
    
    
    npx copilotkit@latest import --source adk --dry-run
    
    
    npx copilotkit@latest import --source langgraph --dry-run

The command runs interactively by default. Start with `--dry-run` to discover source agent keys, conversation counts, skips, and the estimated upload size without opening an import batch.

If you need to import into a different project, select it before continuing with the real import:

Terminal
    
    
    npx copilotkit@latest project select

This changes the project selected for the current directory and writes its project-scoped runtime key to the starter's generated `.env`.

Before the real import, export the destination values from that `.env`:

Terminal
    
    
    export INTELLIGENCE_API_URL="https://..."
    export CPK_INTELLIGENCE_API_KEY="cpk-..."

The importer reads `--api-url` and `--api-key` or the current process environment. It does not load `.env` or `.copilotkit/project.json` automatically. `COPILOTKIT_API_KEY` is also accepted for the key.

Project selection updates the app configuration; the importer still receives its destination through flags or exported environment variables.

For the full adoption flow, see [Add AG-UI Streams to Existing Threads](https://docs.copilotkit.ai/llamaindex/threads-import). Source-specific setup lives in [Add AG-UI streams to ADK sessions](https://docs.copilotkit.ai/google-adk/threads-import) and [Add AG-UI streams to LangGraph threads](https://docs.copilotkit.ai/langgraph-python/threads-import).

## Verify your setup#

`verify` answers the question every integration reaches: _is this actually working?_ It checks the wiring from outside the browser, so it is the proof to reach for on a surface that has no browser at all — React Native, or a runtime on a remote host.
    
    
    npx copilotkit@latest verify

It checks that a cloud-hosted project is selected, that a project API key authenticates, that the runtime responds, and that the runtime declares at least one agent — then reports the runtime version, the agent framework, gateway wiring, and license state.

Read the individual checks, not the summary

Every check reports **PASS** , **FAIL** , or **UNKNOWN**. `UNKNOWN` means the check could not run. It never means the check passed.

To prove the agent actually _runs_ rather than that it is _configured_ , add `--round-trip`. It sends one real request through the runtime and reads the answer back off the thread:
    
    
    npx copilotkit@latest verify --round-trip

What --round-trip does not prove

It sends a **fixed** prompt and records the answer's character count and any tool-call names — **never the answer's text**. It proves an answer came back; it can never tell you what the answer said, so it is no substitute for checking a response against the data your project actually holds.

It also proves an agent answered under the _declared id_ , not **which deployment** answered — a runtime pointed at another project's agent responds identically.

Because it runs the agent, it costs a model call and records a thread. That is why it is opt-in rather than the default.

Option| What it does  
---|---  
`--runtime-url <url>`| The runtime endpoint to probe. Default `http://localhost:3000/api/copilotkit` — pass this whenever your runtime is elsewhere.  
`--round-trip`| Also run the agent and read its answer back.  
`--agent <id>`| Which declared agent to run, when the runtime declares several.  
`--expect-runtime <mode>`| `intelligence` (default) or `oss`. With `oss`, cloud-hosted project and credential checks do not apply.  
`--timeout <seconds>`| How long to wait for the answer. Default `90`.  
`--header "<name>: <value>"`| Extra request header, repeatable. Use it when your `identifyUser` reads a session the CLI does not carry.  
`--json`| Emit a machine-readable payload alone on stdout.  
  
`verify` exits non-zero unless every check passed, so it works as a CI gate.

## Auth commands#

Command| What it does  
---|---  
`npx copilotkit@latest login`| Opens the browser sign-in flow and stores a local CLI session.  
`npx copilotkit@latest whoami`| Shows the signed-in user and active organization.  
`npx copilotkit@latest logout`| Clears the local CLI session.  
  
## Project commands#

Command| What it does  
---|---  
`npx copilotkit@latest project select`| Selects or creates a cloud-hosted CopilotKit Intelligence project for the current directory.  
`npx copilotkit@latest import --source adk --dry-run`| Previews historical Google ADK conversation threads before import.  
`npx copilotkit@latest import --source langgraph --dry-run`| Previews historical LangGraph conversation threads before import.  
`npx copilotkit@latest license create`| Issues a CopilotKit license token for flows that still require one.  
`npx copilotkit@latest license list`| Lists license metadata for the current user or organization.  
  
Re-running `project select` is safe when you need to move a CLI-created app to a different cloud-hosted project. The command updates `.copilotkit/project.json` and provisions a project-scoped API key for the selected project.

## Skills commands#

Command| What it does  
---|---  
`npx copilotkit@latest skills install`| Installs CopilotKit agent skills for supported coding agents.  
`npx copilotkit@latest skills onboard`| Installs skills, then starts agent-assisted onboarding for an existing app.  
  
## Next steps#

  * **Cloud-hosted platform:** [Cloud-hosted CopilotKit Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/managed-intelligence-platform) — login, projects, API keys, threads, and plans in the cloud-hosted web app
  * **Add threads:** use the [Threads Drawer](https://docs.copilotkit.ai/llamaindex/prebuilt-components/copilot-threads-drawer) for a drop-in thread switcher, or [Headless Threads](https://docs.copilotkit.ai/llamaindex/headless-threads) to build your own thread UI
  * **Add AG-UI streams to existing threads:** [Add AG-UI Streams to Existing Threads](https://docs.copilotkit.ai/llamaindex/threads-import) — connect Intelligence for ongoing delivery, then optionally import supported ADK or LangGraph history
  * **Self-hosting:** [Self-host CopilotKit Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting) — run CopilotKit Intelligence in your own Kubernetes cluster
  * **Local evaluation (preview, macOS):** [Evaluate Intelligence locally](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting-local) — run Intelligence in Docker on your own machine to try it with your app



### On this page

What is this?PrerequisitesStart a new appEvaluate Intelligence locallyImport and synchronize historical conversationsVerify your setupAuth commandsProject commandsSkills commandsNext steps
