---
url: https://docs.copilotkit.ai/contributing/code-contributions/
title: Code Contributions
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:55:50.387308+00:00
---

# Code Contributions

> Source: https://docs.copilotkit.ai/contributing/code-contributions/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/)[Quickstart](https://docs.copilotkit.ai/quickstart)[Build with agents](https://docs.copilotkit.ai/build-with-agents)[Intelligence](https://docs.copilotkit.ai/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/learning)

[User Memories](https://docs.copilotkit.ai/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/intelligence/analytics)[Channels](https://docs.copilotkit.ai/intelligence/channels)

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

[Code Contributions](https://docs.copilotkit.ai/contributing/code-contributions)[Documentation Contributions](https://docs.copilotkit.ai/contributing/docs-contributions)

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/telemetry)[Community frameworks](https://docs.copilotkit.ai/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Code Contributions

OtherContributing

# Code Contributions

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

We are grateful for your interest in contributing to CopilotKit. We welcome new contributors and appreciate your help in making CopilotKit better.

This guide will help you get started as smoothly as possible.

## Step 1: Install Prerequisites#

  * [Node.js](https://nodejs.org/en/) 20.x or later
  * [pnpm](https://pnpm.io/) v10.x installed globally (`npm i -g pnpm@^10`)



## Step 2: Repository Setup#

### Fork The Repository#

First, head over to the [CopilotKit repository](https://github.com/CopilotKit/CopilotKit) and create a fork.

Then, clone your fork to your local machine:
    
    
    git clone https://github.com/<your-username>/CopilotKit
    cd CopilotKit

### Install Dependencies#

The CopilotKit repository is a monorepo using a [pnpm](https://pnpm.io/) workspace. Tasks across packages are orchestrated with [Nx](https://nx.dev/).

Install the dependencies using pnpm:
    
    
    pnpm install

### Build Packages#

To make sure everything works, let's build all packages once:
    
    
    pnpm run build

## Step 3: Development Mode#

Now that everything is set up and works as expected, you can get started developing:
    
    
    # Start all packages in development mode
    pnpm run dev
    
    # Start a specific package in development mode
    pnpm exec nx watch --projects=packages/package-name -- pnpm run build

Now you can start making changes to the code.

You can find all `@copilotkit/*` packages under the `packages` folder of the monorepo.

## Step 4: Test Changes in Real-Time#

In most cases, you want to seamlessly be able to test your changes in real-time as you develop.

We have an `examples` folder in the monorepo with a few different examples using CopilotKit. You can run these examples to test your changes, as they are linked to the `@copilotkit/*` packages in the monorepo.

For this tutorial, we'll use the `next-openai` example, specifically the Presentation Demo (`/presentation`).

In a separate terminal, run the following command to start the example:
    
    
    cd examples/v1/next-openai
    export OPENAI_API_KEY=<your-openai-api-key>
    pnpm run example-dev

We use the `pnpm run example-dev` command to run examples, which is different from the `pnpm run dev` command we use to work on the individual packages.

Now navigate to <http://localhost:3000/presentation> and you should see the example running. Any changes you make to the CopilotKit packages will immediately be reflected here.

## Step 5: Formatting and Linting#

Before committing your changes, ensure your files are formatted properly by running the following at the root of the monorepo:
    
    
    pnpm run format

Additionally, ensure you have no linting errors:
    
    
    pnpm run lint

## Step 6: Submit a Pull Request#

Now that you've made your changes, commit and push them. Then, simply head over to the [Pull Requests page](https://github.com/CopilotKit/CopilotKit/pulls) and create a pull request. Well done!

## Starting a dev environment with hot reload#

CopilotKit contains a ready-made script for starting a development environment based on one of the CoAgent examples. It lets you work on CopilotKit internals in the core Typescript and Python code while seeing your changes applied to the chosen example.

As a prerequisite, make sure you have GNU parallel and langgraph CLI installed.

Next, go to the `CopilotKit/` directory and run the `example.sh` script for the example you want to work on:
    
    
    ./scripts/develop/example.sh coagents-starter

This will start a development environment with hot reload.

You can optionally run the same example on LangGraph platform by running:
    
    
    ./scripts/develop/example.sh coagents-starter langgraph-platform

## Debugging#

Every time you run CopilotKit on localhost, you will be able to see the **CopilotKit Dev Console** in the chat window. The Dev Console provides you with useful functionality to debug your copilot (e.g. see what state the copilot is aware of, actions it can perform, etc).

![](https://cdn.copilotkit.ai/docs/copilotkit/images/contributing/copilotkit-dev-console.png)

If you'd like to disable the Dev Console locally, simply set `showDevConsole` to `false` in your `<CopilotKit />` provider.

## (Advanced) Package Linking#

In some cases, you want to test your CopilotKit changes in your own project. For example, you tried to integrate CopilotKit into your own codebase and encountered a bug you want to fix.

Conveniently, you can link your local CopilotKit packages to your own project to test your changes.

Check out the [Advanced: Package Linking](https://docs.copilotkit.ai/contributing/code-contributions/package-linking) guide to learn how to do that.

## Need help?#

If you need help with anything, please don't hesitate to reach out to us on [Discord](https://discord.gg/6dffbvGU3D). We have a dedicated [#contributing](https://discord.com/channels/1122926057641742418/1183863183149117561) channel.

### On this page

Step 1: Install PrerequisitesStep 2: Repository SetupStep 3: Development ModeStep 4: Test Changes in Real-TimeStep 5: Formatting and LintingStep 6: Submit a Pull RequestStarting a dev environment with hot reloadDebugging(Advanced) Package LinkingNeed help?
