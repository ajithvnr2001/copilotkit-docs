---
url: https://docs.copilotkit.ai/strands/intelligence/self-hosting-ecs/
title: Self-host Intelligence on AWS ECS/Fargate
method: scrapling+scrapegraph
fetched_at: 2026-10-08T09:31:40.990877+00:00
---

# Self-host Intelligence on AWS ECS/Fargate

> Source: https://docs.copilotkit.ai/strands/intelligence/self-hosting-ecs/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands)[Quickstart](https://docs.copilotkit.ai/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](https://docs.copilotkit.ai/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands/learning)

[User Memories](https://docs.copilotkit.ai/strands/intelligence/memories)[Capture interactions](https://docs.copilotkit.ai/strands/intelligence/capture-interactions)[Standalone collector](https://docs.copilotkit.ai/strands/intelligence/standalone-collector)[Captured data](https://docs.copilotkit.ai/strands/intelligence/captured-data)[Product Analytics](https://docs.copilotkit.ai/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands/intelligence/channels)

Hosting

[Cloud-hosted](https://docs.copilotkit.ai/strands/intelligence/managed-intelligence-platform)[Self-hosted](https://docs.copilotkit.ai/strands/intelligence/self-hosting)[AWS ECS/Fargate](https://docs.copilotkit.ai/strands/intelligence/self-hosting-ecs)[Local evaluation](https://docs.copilotkit.ai/strands/intelligence/self-hosting-local)

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

[Open-source telemetry](https://docs.copilotkit.ai/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

AWS ECS/Fargate

IntelligenceHosting

# Self-host Intelligence on AWS ECS/Fargate

Deploy the versioned CopilotKit Intelligence ECS bundle with CloudFormation, your own AWS services, and OIDC. Configure, deploy, verify, upgrade, and roll back.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

Deploy CopilotKit Intelligence in your AWS account with the versioned ECS/Fargate bundle and its `cpki-ecs` command. You start with your own network, databases, secrets, and OIDC provider. You finish with the Intelligence dashboard behind HTTPS, an authenticated session, and a runtime connected to your deployment.

Choose your deployment path

This page covers ECS/Fargate. For a Kubernetes deployment, use the [Helm guide](https://docs.copilotkit.ai/strands/intelligence/self-hosting). To evaluate ECS before preparing production resources, use the reference environment.

## What the bundle deploys#

The bundle uses the same released Intelligence service images as the Helm chart. It pins each first-party task image to a digest from `release-manifest.json`.

Stack| Resources  
---|---  
`<deploymentName>-foundation`| ECS cluster, HTTPS Application Load Balancer, security groups, private Cloud Map discovery, KMS-encrypted CloudWatch log groups, IAM roles, and scheduler dead-letter queue.  
`<deploymentName>-release`| Task definitions for app API, frontend, realtime gateway, embeddings, migrations, bootstrap, and thread culling.  
`<deploymentName>-services`| Four running services, ALB routing, CPU autoscaling, and a disabled thread-culler schedule.  
Service| Container port| Public route  
---|---|---  
`app-api`| 4201| `/api`, `/api/*`, `/auth`, and `/auth/*` on the UI host.  
`app-frontend`| 8080| Remaining paths on the UI host, including `/healthz`.  
`realtime-gateway`| 4401| All paths on the realtime host, including WebSocket routes and `/health`.  
`embeddings`| 8080| Private Cloud Map endpoint; no public route.  
  
All four services run in private subnets with public IP assignment disabled. The embeddings service runs even when the deployment has no Memory entitlement; app API requires its provider configuration at startup. The composite image is not an ECS task in this bundle.

The three stacks do not create your VPC, PostgreSQL, Redis, OIDC provider, certificate, KMS keys, secret values, or application DNS records.

## Before you start#

### Release access and tools#

Obtain `copilot-intelligence-ecs-<version>.tar.gz` and `release-manifest.json` from the **same release**. The [Intelligence GitHub releases](https://github.com/CopilotKit/Intelligence/releases) require repository access. If you do not have access, [contact your CopilotKit account team](https://copilotkit.ai/talk-to-an-engineer) for the release bundle.

Install AWS CLI v2, Bash, `jq`, `curl`, `tar`, and Python 3 on the deployment machine. Use AWS credentials that can create CloudFormation stacks and their IAM roles, pass the generated task roles, and add ingress rules to the database and Redis security groups. Configuration validation uses read-only AWS APIs; deployment requires write access.

### AWS resources#

Resource| Required configuration  
---|---  
Network| One VPC with at least two public subnets and two private subnets. Each subnet set must span at least two Availability Zones. Public subnets need an active `0.0.0.0/0` route to an internet gateway; private subnets need an active `0.0.0.0/0` route to a NAT gateway. The configurator rejects endpoint-only private networking.  
Databases| PostgreSQL with pgvector, reachable on port 5432, and Redis on port 6379. Supply their security group IDs and the PostgreSQL server's actual connection limit. The foundation stack adds ingress from its runtime security group.  
HTTPS and DNS| An issued ACM certificate covering both `uiHostName` and `realtimeHostName`. After deployment, point both names at the foundation ALB.  
Identity| An HTTPS OIDC issuer and client. Register `https://<uiHostName>/auth/callback/<authProviderId>` as the callback. The default provider ID is `enterprise-sso`.  
Encryption| Two distinct, enabled, customer-managed symmetric KMS keys in the deployment account and region: `kmsKeyArn` for logs and `secretKmsKeyArn` for secrets. Supply full key ARNs, not aliases.  
  
The log key policy must allow the regional CloudWatch Logs service (`logs.<region>.amazonaws.com`) to use `kms:Encrypt`, `kms:Decrypt`, `kms:ReEncrypt*`, `kms:GenerateDataKey*`, and `kms:Describe*`, scoped to the encryption context for `/ecs/<deploymentName>/*`. The secret key policy must allow account IAM permissions so the task execution roles' `kms:Decrypt` grants take effect. The reference environment's `substrate.yaml` contains both policies.

The configurator calls `sts:GetCallerIdentity`, EC2 describe APIs for the supplied VPC, subnets, routes, and security groups, `acm:DescribeCertificate`, `kms:DescribeKey`, and `secretsmanager:DescribeSecret`. If you configure object storage, it also needs `s3:GetBucketLocation`. It checks the OIDC discovery document over HTTPS. It does not read secret values or test database credentials.

### Secrets#

Create a separate Secrets Manager secret for each required field below. Encrypt every secret with the exact `secretKmsKeyArn` you will supply to the configurator. Configuration files contain ARNs; the tasks receive the secret values when they start.

Configuration field| Secret value  
---|---  
`databaseUrlSecretArn`| PostgreSQL connection URL (`DATABASE_URL`).  
`redisUrlSecretArn`| Redis connection URL (`REDIS_URL`).  
`authSecretArn`| Session secret (`AUTH_SECRET`), at least 32 characters.  
`authClientIdSecretArn`| OIDC client ID (`AUTH_CLIENT_ID`).  
`authClientSecretSecretArn`| OIDC client secret (`AUTH_CLIENT_SECRET`).  
`runnerAuthSecretArn`| Realtime runner authentication secret (`RUNNER_AUTH_SECRET`).  
`secretKeyBaseSecretArn`| Phoenix secret key base (`SECRET_KEY_BASE`).  
`releaseCookieSecretArn`| Shared realtime cluster cookie (`RELEASE_COOKIE`).  
`providerCredentialEncryptionKeySecretArn`| 64-character hex AES-256 key (`APP_HOSTED_BOTS_CREDENTIAL_ENCRYPTION_KEY`).  
  
For RDS, the service images include the CA bundle at `/etc/cpki/rds-ca/global-bundle.pem`. The bundle README documents `sslmode=verify-full` with that CA path. Match the Redis URL's TLS settings to your Redis service.

Optional field| When to supply it  
---|---  
`licenseTokenSecretArn`| Your signed deployment license (`COPILOTKIT_LICENSE_TOKEN`) for licensed capabilities. A project API key is a separate runtime credential.  
`bootstrapConfigSecretArn`| Base64-encoded bootstrap JSON (`BOOTSTRAP_CONFIG_B64`). Supply this on a first install to create organization access mappings. Existing deployments can keep their mappings.  
`timescaleUrlSecretArn`| Restricted runtime TimescaleDB URL for analytics.  
`timescaleMigratorUrlSecretArn`| Schema-owner TimescaleDB URL for analytics migrations.  
  
Analytics defaults to disabled. To enable it, set `analyticsEnabled` to `true` and supply **both** Timescale secret ARNs. The migration task receives the owner URL and the runtime URL; app API and realtime receive only the runtime URL. Both runtime services and the migration task must reach TimescaleDB.

### First-install organization access#

An OIDC login does not grant organization access. Prepare a bootstrap file using the bundle's `config/bootstrap.example.json`. The following example creates one organization and grants membership to users whose OIDC `groups` claim contains the exact, case-sensitive value `intelligence-users`:

bootstrap.json
    
    
    {
      "organizations": [
        {
          "slug": "my-organization",
          "name": "My Organization",
          "mappings": [
            {
              "role": "org_member",
              "claimName": "groups",
              "claimValue": "intelligence-users"
            }
          ]
        }
      ],
      "platformAdminMappings": [],
      "emergencyPlatformAdminGrants": []
    }

Replace the organization and claim values with yours. Your IdP must emit the matching claim. The supported claim names are `groups`, `roles`, `department`, and `entitlements`; an email domain does not grant membership. Use the example file's `platformAdminMappings` shape if you also need to grant platform administration to a specific IdP group.

Base64-encode your file and store the resulting text as a Secrets Manager secret under the same secret KMS key:

Terminal
    
    
    base64 < bootstrap.json | tr -d '\n' > bootstrap.b64

Supply that secret's ARN as `bootstrapConfigSecretArn`. Deployment runs bootstrap after migrations. If no organization or access mapping exists, the UI reports that the deployment has not been bootstrapped. If the signed-in user matches no mapping, it reports that the user is not assigned to an organization.

## Deploy and verify#

Run the following commands in Bash. Keep the same shell open so the paths set in the first step remain available.

### Unpack one release#

Put the two release assets in an empty working directory. Set `CPKI_VERSION` to the version you obtained; `0.12.9` is an example published release.

Terminal
    
    
    export CPKI_VERSION=0.12.9
    export CPKI_DEPLOY_DIR="$PWD"
    
    tar -xzf "copilot-intelligence-ecs-${CPKI_VERSION}.tar.gz"
    cd "copilot-intelligence-ecs-${CPKI_VERSION}"
    export CPKI_CONFIG="$CPKI_DEPLOY_DIR/parameters.json"
    export CPKI_MANIFEST="$CPKI_DEPLOY_DIR/release-manifest.json"
    
    cmp ./release-manifest.json "$CPKI_MANIFEST"
    ./bin/cpki-ecs validate --offline

`cmp` must report no difference between the bundled manifest and the downloaded manifest. Offline validation checks required bundle files and the manifest contract. It does not contact AWS or validate your account resources.

### Generate your configuration#

Run the guided configurator with the IDs, ARNs, host names, and issuer prepared above:

Terminal
    
    
    ./bin/cpki-ecs configure --interactive --output "$CPKI_CONFIG"

The command asks one question at a time, checks local constraints and AWS metadata, and writes the file only after validation passes. It creates no AWS resources. Existing output is not overwritten unless you pass `--force`.

If you use a named AWS profile, select it for the entire shell with `AWS_PROFILE` before configuring or deploying. The configurator's `--profile` option applies only to that invocation and is not saved in the file.

For a prepared JSON file, copy the supplied example outside the bundle, replace its placeholders, and validate it:

Alternative: prepared JSON
    
    
    cp ./config/example.parameters.json "$CPKI_DEPLOY_DIR/draft.parameters.json"
    # Edit draft.parameters.json with your resource IDs, ARNs, and settings.
    ./bin/cpki-ecs configure \
      --from-json "$CPKI_DEPLOY_DIR/draft.parameters.json" \
      --output "$CPKI_CONFIG"

Choose either the guided or JSON path. For automation, `./bin/cpki-ecs configure --help` lists every flag for `--non-interactive` mode.

Before deploying, check these settings:

Setting| Contract  
---|---  
App API and frontend counts| Desired, minimum, and maximum counts must be at least 2. Realtime desired/minimum can be 1; its maximum must be at least 2.  
Database pools| The configurator budgets the maximum API and realtime counts at 200% rollout capacity. Their combined pools must fit within 70% of `databaseMaxConnections`.  
Embeddings| Keep the supplied digest-pinned `embeddingsImage` and `embeddingsModel` unless you have selected another compatible provider image and model.  
Optional S3| Set `objectStorageBucket` and its actual `objectStorageRegion` for channel files and realtime archives. The templates grant scoped task-role access.  
Thread culling| Keep `threadCullerState` set to `DISABLED`. This task deletes data.  
  
With the example's API and realtime maximum counts of 10 and pool sizes of 10, the rollout budget is `20 × 10 + 20 × 10 = 400` connections. Set `databaseMaxConnections` to your server's limit; adjust counts and pools if 400 exceeds 70% of that limit.

### Deploy the stacks and migrations#

Terminal
    
    
    ./bin/cpki-ecs deploy \
      --config "$CPKI_CONFIG" \
      --manifest "$CPKI_MANIFEST"

The command applies foundation and release, runs product migrations, runs analytics migrations when enabled, and runs bootstrap when configured. Each one-shot task must exit with code zero before services update. The command then verifies the deployed services against the requested release.

A failed migration or bootstrap stops the deployment before the service update. Read the task diagnostics and the component's CloudWatch logs before trying again.

### Set DNS and check health#

Read the foundation outputs:

Terminal
    
    
    export AWS_REGION="$(jq -r '.region' "$CPKI_CONFIG")"
    export CPKI_DEPLOYMENT_NAME="$(jq -r '.deploymentName' "$CPKI_CONFIG")"
    export CPKI_UI_HOST="$(jq -r '.uiHostName' "$CPKI_CONFIG")"
    export CPKI_REALTIME_HOST="$(jq -r '.realtimeHostName' "$CPKI_CONFIG")"
    
    aws cloudformation describe-stacks \
      --region "$AWS_REGION" \
      --stack-name "${CPKI_DEPLOYMENT_NAME}-foundation" \
      --query 'Stacks[0].Outputs' --output table

Create DNS records for both hosts using `LoadBalancerDnsName` and, for Route53 aliases, `LoadBalancerCanonicalHostedZoneId`. The source release's `deploy/ecs/examples/reference-environment/app-dns.yaml` provides a Route53 example; see how to obtain the reference templates.

Once both names resolve to the ALB, verify the release and health routes:

Terminal
    
    
    ./bin/cpki-ecs verify \
      --config "$CPKI_CONFIG" \
      --manifest "$CPKI_MANIFEST"
    
    curl --fail "https://${CPKI_UI_HOST}/healthz"
    curl --fail "https://${CPKI_UI_HOST}/api/health"
    curl --fail "https://${CPKI_REALTIME_HOST}/health"

`verify` checks stack state, stable service counts, completed rollouts, and the requested task definitions and image digests. It does not perform an OIDC login or prove that a browser can open a WebSocket.

### Sign in and connect your runtime#

Open the UI host in a browser and sign in through your OIDC provider with a user who matches your bootstrap access mapping. Select the organization, select or create a project, and create a project API key in that deployment.

Follow [Connect your runtime](https://docs.copilotkit.ai/strands/intelligence/quickstart#self-hosted-deployments), using both of your deployment's base URLs:

Intelligence client in your server-side runtime
    
    
    import { CopilotKitIntelligence } from "@copilotkit/runtime/v2";
    
    const intelligence = new CopilotKitIntelligence({
      apiUrl: "https://intelligence.example.com",
      wsUrl: "wss://realtime.intelligence.example.com",
      apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
    });

Replace the hosts with `uiHostName` and `realtimeHostName`, and set the server-side key to the project key you just created. Pass `intelligence` to your existing `CopilotRuntime` as shown in the runtime guide. Do not append `/api`, `/runner`, or `/client` to these base URLs; the client adds the paths.

Check your application's browser origin

The `0.12.9` release template sets realtime `CHECK_ORIGIN` to `https://<uiHostName>`. The configurator has no additional browser-origin field. If your app runs on another origin, review the gateway origin configuration with your deployment team before testing its browser connection; changing the runtime's URLs alone does not change that setting.

Send a message from your app. Confirm the realtime connection upgrades to a WebSocket, the response streams, and the thread appears in your self-hosted project. Reload the app and reopen that thread to check persistence. These checks exercise the user path beyond the three HTTP health probes.

## Evaluate with the reference environment#

The Intelligence source repository provides an AWS evaluation environment under `deploy/ecs/examples/reference-environment/`. The bundle root's `README.md` contains the full **Quickstart: reference environment** commands, including output-to-parameter wiring.

Obtain the reference templates separately

The published `0.12.9` ECS archive does not contain `examples/reference-environment/`, even though its README refers to that directory. Obtain it from the matching source release or your CopilotKit account team before following the quickstart. The three production templates are already in the ECS archive.

After the unpack step above, you can retrieve the source with the GitHub CLI authenticated to an account that has Intelligence repository access:

Terminal
    
    
    gh release download "v${CPKI_VERSION}" \
      --repo CopilotKit/Intelligence \
      --archive tar.gz \
      --output "$CPKI_DEPLOY_DIR/intelligence-source.tar.gz"
    
    mkdir "$CPKI_DEPLOY_DIR/reference-source"
    tar -xzf "$CPKI_DEPLOY_DIR/intelligence-source.tar.gz" \
      --strip-components=1 -C "$CPKI_DEPLOY_DIR/reference-source"
    
    cd "$CPKI_DEPLOY_DIR/copilot-intelligence-ecs-${CPKI_VERSION}"
    cp -R "$CPKI_DEPLOY_DIR/reference-source/deploy/ecs/examples" ./examples

Now follow **Quickstart: reference environment** in `README.md` from the extracted ECS bundle directory. Use your downloaded release manifest; you do not need to construct one from image tags.

Order| Template or command| Purpose  
---|---|---  
1| `substrate.yaml`| VPC, public/private subnets, NAT, RDS PostgreSQL, ElastiCache Redis, KMS keys, ACM certificate, and database password secret.  
2| `secrets.yaml`| Runtime secrets and connection URLs derived from the substrate outputs.  
3| `keycloak.yaml` with `realm-cpki.json`| Evaluation OIDC issuer, application client, and demo user.  
4| `cpki-ecs configure`, then `cpki-ecs deploy`| The same three Intelligence stacks used in production.  
5| `app-dns.yaml`, then health/login checks| UI and realtime Route53 aliases, followed by verification.  
  
Use your own domain and evaluation-only credentials

Supply your own Route53 hosted zone and host names. Override the substrate's `WildcardDomain` parameter: its default is a CopilotKit domain. The certificate must cover the UI, realtime, and Keycloak hosts. The imported realm includes `demo` / `Passw0rd!`; use the reference environment for evaluation only. Production uses your own identity provider and managed resources.

The reference environment does not add a TimescaleDB instance. Leave analytics disabled unless you supply one and both analytics secret ARNs.

The reference realm also does not define organization claim mappings. Its demo login can verify OIDC, but project access still needs a supported claim from the IdP and the bootstrap mapping above.

## Operate the deployment#

### Upgrade or roll back#

Keep the previous bundle, manifest, and configuration. Back up the database under your recovery policy and check migration compatibility before upgrading. Obtain the new bundle and matching manifest, unpack them in a new directory, and run its `deploy` command with your configuration. Repeat the health, sign-in, and runtime checks above.

To roll application tasks back, run from the retained prior bundle with its manifest:

Terminal
    
    
    ./bin/cpki-ecs rollback \
      --config "$CPKI_CONFIG" \
      --manifest ./release-manifest.json

Rollback registers the prior task definitions, updates services, and verifies their release. **It does not reverse database migrations.** The ECS deployment circuit breaker also rolls back failed service deployments; it does not reverse migrations or foundation changes.

### Rotate secrets or change capacity#

After changing a secret value, start a new deployment for every service that consumes it. For example, after rotating an app API secret:

Terminal
    
    
    aws ecs update-service \
      --region "$AWS_REGION" \
      --cluster "$CPKI_DEPLOYMENT_NAME" \
      --service "${CPKI_DEPLOYMENT_NAME}-app-api" \
      --force-new-deployment

Running tasks do not receive new environment-secret values until they restart. To change service counts, validate an updated configuration and run `deploy` with the same manifest. API, frontend, and realtime use CPU target tracking through `targetCpuUtilization`.

### Inspect a failed rollout#

Use ECS service events, stopped-task reasons, and `/ecs/<deploymentName>/...` CloudWatch log groups. Container Insights defaults to enabled. Set `otlpEndpoint` to the base URL of your OTLP collector to receive traces. The bundle does not install an observability backend. See [Monitor with OpenTelemetry](https://docs.copilotkit.ai/strands/intelligence/self-hosting-observability).

Failure| Check  
---|---  
Configuration is rejected| The named resource, account/region, NAT route, certificate host coverage, exact secret KMS key, and OIDC discovery response.  
Migration or bootstrap fails| The stopped task and its component log group. Services do not update until each required task exits zero.  
ALB health fails| `/api/health`, `/healthz`, or `/health` on the correct host; task access to PostgreSQL and Redis.  
OIDC redirect is rejected| The exact `https://<uiHostName>/auth/callback/<authProviderId>` registered at your IdP.  
Realtime discovery fails| Cloud Map records and runtime security-group rules for EPMD 4369 and BEAM distribution 9000–9010.  
  
### Remove the deployment#

Remove application DNS records first. From the bundle directory, delete the three Intelligence stacks:

Terminal — removes the deployment
    
    
    ./bin/cpki-ecs teardown \
      --config "$CPKI_CONFIG" \
      --confirm "$CPKI_DEPLOYMENT_NAME"

The confirmation must exactly match `deploymentName`. This disables ALB deletion protection and deletes services, release, and foundation in that order. CloudWatch log groups remain. Customer-managed databases, Redis, VPC, IdP, secrets, certificate, and KMS keys remain.

For the reference environment, follow the bundle README's full teardown order: application DNS, bundle stacks, Keycloak, secrets, then substrate. `cpki-ecs teardown` alone does not remove those additional stacks.

## Implementation references#

The release bundle's `README.md`, `config/example.parameters.json`, and `bin/cpki-ecs configure --help` travel with the version you deploy. For source review, the [CLI and configuration validators](https://github.com/CopilotKit/Intelligence/tree/main/deploy/ecs/bin) and [CloudFormation templates](https://github.com/CopilotKit/Intelligence/tree/main/deploy/ecs/cloudformation) require Intelligence repository access.

### On this page

OverviewWhat the bundle deploysBefore you startRelease access and toolsAWS resourcesSecretsFirst-install organization accessDeploy and verifyEvaluate with the reference environmentOperate the deploymentUpgrade or roll backRotate secrets or change capacityInspect a failed rolloutRemove the deploymentImplementation references
