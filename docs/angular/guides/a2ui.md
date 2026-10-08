---
url: https://docs.copilotkit.ai/angular/guides/a2ui/
title: A2UI schemas, styling, and recovery
method: scrapling+scrapegraph
fetched_at: 2026-10-08T08:49:22.339697+00:00
---

# A2UI schemas, styling, and recovery

> Source: https://docs.copilotkit.ai/angular/guides/a2ui/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendAngularAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/angular)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

Basics

Generative UI

Interactivity

[WebMCP](https://docs.copilotkit.ai/angular/webmcp)

Agent capabilities

Built-in Agent

[Sub-agents](https://docs.copilotkit.ai/angular/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/angular/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/angular/learning)

[User Memories](https://docs.copilotkit.ai/angular/intelligence/memories)[Standalone collector](https://docs.copilotkit.ai/angular/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/angular/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/angular/intelligence/analytics)[Channels](https://docs.copilotkit.ai/angular/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

Concepts

Angular guides

[Using the Angular docs](https://docs.copilotkit.ai/angular/using-these-docs)[Feature examples](https://docs.copilotkit.ai/angular/features)[Angular API reference](https://docs.copilotkit.ai/reference/angular)[Chat UI and customization](https://docs.copilotkit.ai/angular/guides/chat-ui)[Frontend tools and generative UI](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)[A2UI schemas, styling, and recovery](https://docs.copilotkit.ai/angular/guides/a2ui)[Voice and multimodal input](https://docs.copilotkit.ai/angular/guides/voice-multimodal)[Human-in-the-loop and interrupts](https://docs.copilotkit.ai/angular/guides/human-in-the-loop)[Shared state and agent context](https://docs.copilotkit.ai/angular/guides/shared-state)[Threads, memory, attachments, and headless UI](https://docs.copilotkit.ai/angular/guides/threads-memory-attachments-headless)[Troubleshooting Angular apps](https://docs.copilotkit.ai/angular/guides/troubleshooting)[Build with agents](https://docs.copilotkit.ai/angular/build-with-agents)[Intelligence](https://docs.copilotkit.ai/angular/intelligence/overview)

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/angular/telemetry)[Community frameworks](https://docs.copilotkit.ai/angular/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

A2UI schemas, styling, and recovery

LearnAngular guides

# A2UI schemas, styling, and recovery

Configure typed A2UI catalogs, Angular-owned styles, and incomplete-stream recovery.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

A2UI renders declarative interface operations and snapshots inside Angular chat. Configure it with a catalog of allowed components; the renderer creates only components that the catalog defines.

## What is A2UI?#

A2UI is CopilotKit's declarative generative UI path for Angular. Instead of asking an agent to emit arbitrary component code, you give it a typed catalog and render only the operations that match that catalog.

## Choose a schema strategy#

Catalog component definitions use Zod schemas for their props. A broad catalog lets the agent compose several application primitives. A fixed catalog narrows the generated interface to a specific domain and set of shapes.

The flight example keeps its component vocabulary deliberately small:

a2ui-definitions.ts
    
    
    export const fixedDefinitions = {  Card: { props: z.object({ child: z.string() }) },  Title: { props: z.object({ text: dynamicString }) },  Airport: { props: z.object({ code: dynamicString }) },  Arrow: { props: z.object({}) },  AirlineBadge: { props: z.object({ name: dynamicString }) },  PriceTag: { props: z.object({ amount: dynamicString }) },  Button: {    props: z.object({      child: z.string(),      variant: z.enum(["primary", "secondary", "ghost"]).optional(),      action: z.unknown().optional(),    }),  },} satisfies A2UICatalogDefinitions;

Give each catalog a stable `catalogId`, then select it in the `a2ui` option passed to `provideCopilotKit`. The Showcase chooses a general catalog, a fixed flight catalog, or the recovery variant from the active feature:

a2ui-catalogs.ts
    
    
    export function a2uiConfigForFeature(feature: string): A2UIConfig | undefined {  switch (feature) {    case "beautiful-chat":      return { catalog: beautifulCatalog };    case "declarative-gen-ui":      return { catalog: declarativeCatalog };    case "a2ui-recovery":      return {        catalog: declarativeCatalog,        recovery: { showAfterMs: 2_000, showAfterAttempts: 2 },      };    case "a2ui-fixed-schema":      return { catalog: fixedCatalog };    default:      return undefined;  }}

In an application config, pass the chosen catalog and lifecycle policy through the Angular provider:

src/app/app.config.ts
    
    
    provideCopilotKit({
      runtimeUrl: "/api/copilotkit",
      a2ui: {
        catalog: productCatalog,
        recovery: { showAfterMs: 2_000, showAfterAttempts: 2 },
      },
    });

A catalog is required: without one, A2UI stays off even when the runtime enables it, and CopilotKit logs a warning.

### Use existing web components#

A catalog entry can also be a Custom Element, such as a component from an existing design system. Pass `{ tagName, element }` instead of an Angular component, and mix both kinds freely:

src/app/a2ui-catalog.ts
    
    
    const catalog = createAngularCatalog(
      {
        Badge: { props: z.object({ label: z.string() }) },
        Panel: { props: z.object({ children: ChildListSchema }) },
      },
      {
        Badge: { tagName: "acme-badge", element: AcmeBadge },
        Panel: PanelComponent,
      },
      { includeBasicCatalog: true },
    );

CopilotKit registers the element, renders it in place of the node, and assigns the node's A2UI `ComponentContext` to its `context` property on every update. The element reads its props and writes to the data model through that context, for example with web_core's `GenericBinder`. Elements render in the browser only, not during server rendering.

By default, CopilotKit includes the catalog schema in agent context. Set `includeSchema: false` only when the server already supplies equivalent schema and generation instructions. Otherwise the agent cannot reliably know which components and props are valid.

## Style rendered components#

Catalog components are Angular components with application-owned class names. Style those classes in the global stylesheet so generated surfaces and their nested elements receive the same rules:

styles.css
    
    
    .a2ui-row {  display: flex;  flex-wrap: wrap;  align-items: stretch;  width: 100%;}.a2ui-column {  display: flex;  flex-direction: column;  width: 100%;}[data-testid="declarative-card"],.a2ui-chart-card,.a2ui-flight-card {  display: block;  padding: 1rem;  border: 1px solid var(--line);  border-radius: 0.9rem;  background: white;  box-shadow: 0 8px 22px -18px rgb(15 23 42 / 0.4);}.a2ui-metric {  display: grid;  min-width: 8rem;  gap: 0.25rem;}.a2ui-metric > span,.a2ui-metric > small {  color: var(--muted);  font-size: 0.75rem;}.a2ui-metric > strong {  font-size: 1.4rem;}.a2ui-status,.a2ui-airline {  display: inline-flex;  width: fit-content;  padding: 0.25rem 0.55rem;  border-radius: 999px;  background: #eef2ff;  font-size: 0.75rem;  font-weight: 700;}.a2ui-status-success {  background: #dcfce7;  color: #166534;}.a2ui-status-warning {  background: #fef3c7;  color: #92400e;}.a2ui-status-error {  background: #fee2e2;  color: #991b1b;}

Keep semantic state in explicit classes such as `a2ui-status-success` rather than asking the model to invent colors. You can also pass an A2UI `theme` through `provideCopilotKit` for renderer-level theme values; catalog CSS remains the right place for product-specific layout and visual states.

## Recover incomplete streams#

An interrupted stream can leave an A2UI surface without a terminal lifecycle event. Configure `recovery.showAfterMs` to avoid flashing recovery UI during a normal pause and `recovery.showAfterAttempts` to wait through transient retry attempts. The Showcase uses two seconds and two attempts, as shown in the catalog-selection snippet above.

Use `recovery.debugExposure` only when users should see protocol diagnostics. Keep it hidden in consumer-facing chat, or choose a collapsed or verbose mode for internal debugging. Recovery thresholds affect client display; the server still owns activity lifecycle status and retry behavior.

## Angular support boundaries#

  * **Hashbrown is unsupported.** The stable Hashbrown Angular package does not support the Angular 22 policy. Do not add it to an Angular integration; use A2UI with a typed catalog instead.
  * **JSON Renderer is not applicable.** JSON Renderer does not provide an Angular renderer; use A2UI for declarative Angular interfaces.



These are authoritative framework support states, not missing examples.

## Next steps#

  * [Dynamic catalog](https://docs.copilotkit.ai/angular/features#declarative-gen-ui)
  * [Fixed schema](https://docs.copilotkit.ai/angular/features#a2ui-fixed-schema)
  * [Recovery behavior](https://docs.copilotkit.ai/angular/features#a2ui-recovery)
  * [Other generative UI paths](https://docs.copilotkit.ai/angular/guides/frontend-tools-generative-ui)



### On this page

What is A2UI?Choose a schema strategyUse existing web componentsStyle rendered componentsRecover incomplete streamsAngular support boundariesNext steps
