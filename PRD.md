# Aegentis
## Product Requirements Document (PRD)

**Version:** 1.0
**Status:** Proposed — Ready for architecture and MVP planning
**Date:** October 11, 2026
**Product category:** AI SRE, Autonomous Cloud Operations, Incident Remediation
**Initial deployment target:** Kubernetes and Azure-based environments
**Primary tagline:** Detect. Resolve. Prove.

---

## 1. Executive Summary

Aegentis is an AI-powered Site Reliability Engineering (SRE) platform that automates the incident lifecycle, from detection through verified recovery.

Modern engineering teams operate complex infrastructure across Kubernetes, cloud services, CI/CD pipelines, infrastructure-as-code, observability systems, and distributed applications. When an incident occurs, engineers must correlate alerts, logs, deployment changes, resource metrics, and configuration differences before identifying and implementing a fix.

Existing monitoring tools detect symptoms. AI assistants explain possible causes. Automation platforms execute predefined workflows. Aegentis connects these capabilities into a controlled, evidence-driven incident response system.

Aegentis will:

1. Detect or receive infrastructure and application incidents.
2. Collect relevant telemetry, resource state, and recent changes.
3. Correlate evidence and generate ranked root-cause hypotheses.
4. Produce a remediation plan with risk classification and expected outcomes.
5. Request approval when required by policy.
6. Execute approved actions using authorized integrations.
7. Verify service recovery against explicit health criteria.
8. Stop, retry within defined limits, or roll back when recovery fails.
9. Maintain a complete audit trail of evidence, decisions, approvals, and actions.

### Product vision

Build a trusted operational control plane that enables engineering teams to resolve routine infrastructure incidents autonomously while keeping humans in control of high-impact decisions.

### Core differentiator

**Aegentis closes the loop between diagnosis, execution, and verification.**

A successful tool invocation is not considered a successful remediation. An incident is resolved only when the relevant recovery criteria have been satisfied.

---

## 2. Problem Statement

### 2.1 Current operational challenges

Engineering teams face several recurring problems.

**Fragmented investigation**

Incident information is distributed across monitoring dashboards, Kubernetes events, cloud logs, deployment pipelines, Git repositories, and infrastructure configuration.

**Slow root-cause identification**

Engineers manually compare timestamps, recent changes, error messages, resource utilization, and dependency failures.

**Manual remediation**

Common fixes, such as restarting unhealthy workloads or reverting a problematic deployment, require human investigation and execution.

**Unsafe automation**

Traditional scripts can execute predefined actions but often lack contextual reasoning, dynamic risk evaluation, and robust post-action verification.

**Unverified recovery**

A deployment command may return successfully even though the application remains unhealthy, requests continue failing, or dependent services are unavailable.

**Insufficient operational traceability**

Incident timelines, diagnostic evidence, approvals, executed commands, and remediation results may be scattered across several systems.

### 2.2 Problem statement

Engineering organizations need a system that can investigate incidents using multiple sources of evidence, choose appropriate remediation from a controlled action set, execute it within defined permissions, and verify recovery without sacrificing security, reliability, or operational accountability.

### 2.3 Product hypothesis

If Aegentis correlates operational telemetry with deployment and configuration history, then executes policy-approved remediation with explicit verification, teams can reduce manual investigation effort and incident recovery time for supported incident classes.

This hypothesis must be validated through a controlled pilot. No reduction in MTTR or autonomous resolution rate is assumed in advance.

---

## 3. Product Goals and Non-Goals

### 3.1 Goals

1. Reduce manual investigation effort for supported incidents.
2. Shorten mean time to recovery (MTTR).
3. Provide evidence-backed root-cause hypotheses.
4. Automate a bounded set of repeatable remediation workflows.
5. Prevent unauthorized or high-risk infrastructure modifications.
6. Verify service health after every remediation.
7. Support human approval, cancellation, and intervention.
8. Integrate with existing engineering tools instead of replacing them.
9. Provide complete auditability for enterprise operations.
10. Support incremental expansion from Kubernetes to broader cloud operations.

### 3.2 Non-goals for the initial release

- Replacing Prometheus, Grafana, Azure Monitor, or other observability systems.
- Replacing Azure DevOps or other CI/CD platforms.
- Replacing Terraform or other infrastructure-as-code engines.
- Providing unrestricted, general-purpose shell access to an AI agent.
- Automatically applying arbitrary LLM-generated scripts to production.
- Guaranteeing that every incident can be resolved autonomously.
- Building a general-purpose chatbot unrelated to operational workflows.
- Replacing human incident commanders for critical production incidents.
- Supporting every cloud provider and monitoring platform in the MVP.
- Training a proprietary foundation model.

### 3.3 Product principles

- **Evidence before action:** Every proposed remediation must reference supporting evidence.
- **Least privilege:** Integrations receive only the permissions they require.
- **Policy before autonomy:** The platform cannot override organizational execution policies.
- **Verification before closure:** Recovery requires measurable health criteria.
- **Reversibility where possible:** Prefer actions that can be undone or safely repeated.
- **Explainability:** Engineers can inspect the reasoning inputs, evidence, and action sequence.
- **Human control:** Authorized users can approve, reject, cancel, or take over.
- **Fail safely:** Uncertainty or verification failure must not trigger unlimited automated actions.

---

## 4. Target Users and Personas

### 4.1 Primary personas

**Persona A: Site Reliability Engineer**

Responsibilities:
- Maintain service availability and reliability.
- Investigate incidents and reduce MTTR.
- Develop and maintain remediation runbooks.
- Improve alert quality and operational readiness.

Needs:
- Rapid correlation of logs, metrics, events, and changes.
- Evidence-backed diagnosis.
- Safe remediation and verification.
- Incident timelines and operational analytics.

**Persona B: Platform Engineer**

Responsibilities:
- Manage Kubernetes platforms and shared infrastructure.
- Maintain reusable infrastructure and deployment patterns.
- Enforce platform guardrails.
- Provide self-service operational capabilities.

Needs:
- Consistent remediation across clusters and environments.
- Centralized policies and reusable workflows.
- Integration with Helm, Terraform, and CI/CD.
- Multi-team isolation and auditable access.

**Persona C: DevOps Engineer**

Responsibilities:
- Maintain build and release pipelines.
- Troubleshoot failed deployments.
- Manage environment configuration and deployment automation.

Needs:
- Correlation between pipeline failures and infrastructure symptoms.
- Identification of problematic releases.
- Safe deployment rollback and post-deployment validation.

**Persona D: Engineering Manager / Incident Commander**

Responsibilities:
- Coordinate incident response.
- Monitor service reliability and operational performance.
- Review incident outcomes and recurring failure patterns.

Needs:
- Incident overview, severity, ownership, and timeline.
- Approval workflows and escalation.
- MTTR and remediation effectiveness metrics.
- Audit and post-incident reporting.

**Persona E: Security / Cloud Governance Administrator**

Responsibilities:
- Define infrastructure access and execution policies.
- Manage approval requirements and compliance controls.
- Review privileged operations.

Needs:
- Explicit permissions and action boundaries.
- Immutable or tamper-evident audit records.
- Separation of duties and tenant isolation.
- Emergency stop and policy enforcement.

### 4.2 Roles and permissions

| Role | Primary permissions |
|---|---|
| Organization Owner | Organization configuration, membership, tenant settings |
| Platform Administrator | Integrations, environments, execution policies |
| SRE / Operator | Investigate incidents, initiate permitted actions |
| Approver | Approve or reject gated remediation plans |
| Viewer | Read incidents, evidence, reports, and audit history |
| Auditor | Read audit records and compliance evidence |

Role permissions must be configurable and enforceable on the backend. UI visibility alone is not an authorization mechanism.

---

## 5. Product Scope

### 5.1 Initial integration scope

**Core runtime**
- Kubernetes API.
- Helm release and deployment metadata.
- Prometheus-compatible metrics.
- Kubernetes events, workload status, and container logs.

**Azure and delivery systems**
- Azure Monitor and Azure Log Analytics.
- Azure Kubernetes Service (AKS).
- Azure DevOps pipelines and deployment metadata.
- Azure Resource Manager for selected read-only resource information.

**Infrastructure-as-code**
- Terraform plan artifacts and execution results.
- Git repository changes associated with deployments.
- Approved Terraform execution workflows, initially through external CI/CD rather than direct arbitrary execution.

**Notification and incident systems**
- Microsoft Teams and/or Slack notifications.
- Webhooks for incident ingestion.
- Jira or another ticketing system in a subsequent integration phase.

Integration priorities may be adjusted after discovery with pilot users.

### 5.2 Integration principles

- Prefer supported APIs over browser automation.
- Support both polling and event-driven ingestion where practical.
- Store integration credentials in a secrets manager.
- Make integrations independently configurable and testable.
- Allow read-only integration mode.
- Record source timestamps and ingestion timestamps.
- Handle rate limits, pagination, retries, and partial failures.
- Prevent one integration failure from disabling the entire platform.

---

## 6. Functional Requirements

Priority definitions:

- **P0:** Required for the MVP.
- **P1:** Required for a production pilot or early expansion.
- **P2:** Future enhancement.

### 6.1 Identity and access management

**FR-001 — Organization management (P0)**

The platform shall support organization-scoped workspaces and user membership.

**FR-002 — Authentication (P0)**

The platform shall support secure authentication, with OIDC/OAuth 2.0 integration. Enterprise SSO and identity-provider integration must be supported before broad enterprise rollout.

**FR-003 — Role-based access control (P0)**

The platform shall enforce role and resource permissions on every protected API and action.

**FR-004 — Environment scoping (P0)**

Users and service identities shall be restricted to authorized organizations, clusters, subscriptions, and environments.

**FR-005 — Service identities (P0)**

Integration credentials shall be separated from user credentials and scoped to required permissions.

### 6.2 Incident ingestion and detection

**FR-010 — Incident ingestion (P0)**

The platform shall ingest incidents through:
- Webhooks.
- Prometheus Alertmanager-compatible webhooks.
- Kubernetes event and workload monitoring.
- Manual incident creation.

**FR-011 — Incident normalization (P0)**

Incoming incidents shall be converted into a common schema containing source, timestamp, affected resource, severity, environment, description, and source identifiers where available.

**FR-012 — Deduplication (P0)**

The platform shall identify duplicate or repeated alerts using configurable fingerprints, time windows, and resource identifiers.

**FR-013 — Incident correlation (P1)**

The platform shall correlate related alerts into a shared incident when supported by temporal, resource, or dependency evidence.

**FR-014 — Severity classification (P0)**

Incidents shall support configurable severity levels, such as SEV-1 through SEV-4, with organization-defined mapping rules.

**FR-015 — Manual incident initiation (P0)**

Authorized users shall be able to initiate an investigation without waiting for an alert.

### 6.3 Context collection and diagnosis

**FR-020 — Evidence collection (P0)**

The platform shall collect relevant context from authorized sources, including:
- Resource status and configuration.
- Kubernetes events and logs.
- Metric values and recent trends.
- Recent deployments and release metadata.
- Related infrastructure or configuration changes.
- Dependency health where available.

**FR-021 — Time-bounded investigation (P0)**

Each investigation shall use configurable lookback windows, collection timeouts, and maximum evidence limits.

**FR-022 — Evidence provenance (P0)**

Every evidence item shall include its source, timestamp, resource association, and retrieval status.

**FR-023 — Root-cause hypotheses (P0)**

The diagnostic engine shall produce one or more ranked hypotheses, each with:
- Description.
- Supporting evidence.
- Contradictory or missing evidence.
- Confidence estimate or qualitative confidence level.
- Recommended validation steps.
- Potential remediation options.

**FR-024 — Uncertainty handling (P0)**

When evidence is insufficient or contradictory, the system shall identify uncertainty and request more evidence or human investigation instead of fabricating a definitive cause.

**FR-025 — Investigation replay (P1)**

Authorized users shall be able to inspect the evidence and decision history associated with a completed investigation.

### 6.4 Remediation planning

**FR-030 — Remediation catalog (P0)**

The platform shall maintain a catalog of versioned remediation actions with documented parameters, prerequisites, permissions, risks, and verification procedures.

**FR-031 — Plan generation (P0)**

The system shall generate a structured remediation plan containing:
- Incident and hypothesis references.
- Intended outcome.
- Proposed actions and ordering.
- Target resources.
- Preconditions.
- Expected impact.
- Risk classification.
- Required permissions.
- Approval requirements.
- Verification criteria.
- Failure and rollback strategy.

**FR-032 — Deterministic validation (P0)**

Plans shall be validated against a deterministic policy engine before execution. The LLM shall not be the final authority on whether an action is permitted.

**FR-033 — Dry-run mode (P0)**

The platform shall support plan previews without performing infrastructure mutations.

**FR-034 — Human review (P0)**

Authorized users shall be able to approve, reject, or request changes to plans requiring review.

**FR-035 — Plan versioning (P1)**

Approved plans shall be bound to a specific version and target scope. Material changes invalidate prior approval.

### 6.5 Execution engine

**FR-040 — Controlled action execution (P0)**

The execution engine shall execute only registered, validated actions through approved integrations.

**FR-041 — Least-privilege execution (P0)**

Actions shall use credentials with only the required permissions and resource scope.

**FR-042 — Execution state machine (P0)**

Actions shall have explicit states, such as:
- Pending.
- Validating.
- Awaiting approval.
- Approved.
- Running.
- Succeeded.
- Failed.
- Cancelled.
- Timed out.
- Verification failed.
- Rolled back.

**FR-043 — Idempotency (P0)**

Where possible, actions shall be idempotent. Non-idempotent actions must use safeguards against duplicate execution.

**FR-044 — Concurrency controls (P0)**

The platform shall prevent conflicting actions against the same resource and enforce configurable concurrency limits.

**FR-045 — Execution timeout (P0)**

Every action shall have a bounded timeout, cancellation behavior, and defined handling for ambiguous execution results.

**FR-046 — Retry policy (P0)**

Retries shall be limited, policy-controlled, and restricted to actions that are safe to retry.

**FR-047 — Execution evidence (P0)**

The platform shall retain structured execution results, timestamps, target references, status, and redacted output.

**FR-048 — Emergency stop (P0)**

Authorized operators shall be able to stop new executions and cancel cancellable running workflows.

**FR-049 — Approval binding (P0)**

Approvals shall be tied to the exact action plan, target scope, and applicable policy version.

### 6.6 Recovery verification

**FR-050 — Verification policy (P0)**

Every mutating remediation action shall have a verification procedure. The procedure may contain multiple checks and observation windows.

**FR-051 — Health criteria (P0)**

Verification may include:
- Kubernetes workload readiness.
- Pod restart and crash-loop behavior.
- Application health endpoints.
- Error rate and latency.
- Prometheus alert state.
- Azure Monitor metrics.
- Deployment status.
- Business or synthetic checks when available.

**FR-052 — Recovery determination (P0)**

The system shall distinguish between:
- Action succeeded.
- Recovery verified.
- Recovery partially verified.
- Recovery failed.
- Verification unavailable.

**FR-053 — Rollback orchestration (P0)**

When a defined recovery policy allows rollback, the system shall execute only a previously validated rollback procedure. Otherwise, it shall stop and escalate.

**FR-054 — Incident closure (P0)**

An incident shall not be marked automatically as resolved merely because an execution action succeeded. Closure requires the configured recovery criteria or an authorized human decision.

**FR-055 — Stability window (P1)**

The system shall support a post-recovery observation period to detect immediate recurrence.

### 6.7 Incident management

**FR-060 — Incident workspace (P0)**

Each incident shall have a central view showing:
- Summary and severity.
- Affected resources.
- Timeline.
- Evidence.
- Root-cause hypotheses.
- Remediation plan.
- Approval history.
- Execution status.
- Verification results.
- Audit history.

**FR-061 — Incident lifecycle (P0)**

The incident lifecycle shall support New, Investigating, Awaiting Approval, Remediating, Verifying, Resolved, Escalated, and Closed states, with explicit transition rules.

**FR-062 — Manual takeover (P0)**

Authorized users shall be able to pause an automation workflow and assume responsibility for investigation or remediation.

**FR-063 — Notifications (P1)**

The platform shall notify relevant users when incidents are created, approvals are needed, execution fails, recovery is verified, or escalation is required.

**FR-064 — Incident export (P1)**

The platform shall export incident timelines and post-incident reports in a structured format.

### 6.8 Policy and governance

**FR-070 — Policy engine (P0)**

The platform shall evaluate actions against centrally managed policies before execution.

**FR-071 — Risk classification (P0)**

Actions shall be classified according to impact, scope, reversibility, environment, privilege level, and potential service disruption.

**FR-072 — Environment-specific policies (P0)**

Policies shall support different restrictions for development, test, staging, and production environments.

**FR-073 — Deny-by-default mutations (P0)**

Unregistered actions, unknown targets, and unapproved execution paths shall be denied.

**FR-074 — Separation of duties (P1)**

Organizations shall be able to require an approver other than the plan creator for selected operations.

**FR-075 — Audit retention (P0)**

Audit records shall be protected against unauthorized modification and retained according to configurable organizational policies.

### 6.9 Analytics and reporting

**FR-080 — Operational metrics (P0)**

The platform shall calculate:
- Time to acknowledge.
- Time to diagnose.
- Time awaiting approval.
- Time to execute remediation.
- Time to verified recovery.
- Successful remediation rate.
- Verification failure rate.
- Human intervention rate.
- Incident recurrence rate.

**FR-081 — Outcome classification (P0)**

The platform shall distinguish fully automated, human-approved, manually resolved, failed, and inconclusive incidents.

**FR-082 — Reporting (P1)**

Authorized users shall be able to review incident trends, remediation effectiveness, and recurring failure classes over a selected period.

**FR-083 — Baseline comparison (P1)**

The platform shall support comparing pilot performance against a documented pre-deployment baseline.

---

## 7. Autonomous Operation Modes

Aegentis shall support explicit operating modes at the organization, environment, and action level.

### Mode 1: Observe

- Ingest alerts and collect evidence.
- Generate diagnostic hypotheses.
- Recommend remediation.
- Never execute infrastructure mutations.

### Mode 2: Assist

- Perform investigation and planning.
- Require human approval before every mutating action.
- Verify recovery after approved execution.

### Mode 3: Guarded Autonomy

- Execute preapproved, allowlisted actions when all policy conditions are satisfied.
- Require approval for actions outside the autonomous policy.
- Stop when evidence, permissions, or verification is insufficient.

### Mode 4: Restricted Emergency Automation

An optional future capability for explicitly defined incident classes, subject to stricter organizational policies.

This mode must not provide unrestricted authority over production infrastructure.

**MVP requirement:** Observe and Assist are mandatory. Guarded Autonomy is supported for a small allowlisted action set in non-production environments before any production enablement.

---

## 8. Initial Remediation Catalog

The first release should support a deliberately small set of operational workflows.

| Incident | Candidate remediation | Initial execution policy |
|---|---|---|
| Deployment rollout stalled | Inspect rollout and restart or roll back through an approved deployment mechanism | Approval required |
| Pod repeatedly crashing | Collect logs, events, probes, and resource status; recommend a targeted fix | Diagnosis first |
| Replica count below target | Restore configured replica count when drift is confirmed | Guarded automation in test |
| Failed Helm release | Inspect release history and values; propose rollback | Approval required |
| Failed CI/CD deployment | Correlate pipeline logs and resource changes; propose redeployment or rollback | Approval required |
| High CPU or memory usage | Identify affected workloads and capacity signals; recommend scaling or resource changes | Approval required |
| Node pressure | Collect node and workload evidence; recommend safe remediation | Human-led initially |
| Application health check failing | Correlate deployment history and application health signals | Diagnosis first |

Actions must not be treated as universally safe. Restarting a workload, scaling a service, or rolling back a release can worsen an incident if the diagnosis is incorrect.

### Initial exclusions

The MVP shall not autonomously:
- Delete persistent volumes or databases.
- Modify network security rules without explicit authorization.
- Rotate production credentials without an approved workflow.
- Execute arbitrary shell commands generated by an LLM.
- Apply unreviewed Terraform changes to production.
- Delete cloud resources.
- Perform cluster-wide destructive operations.

---

## 9. User Experience Requirements

### 9.1 Primary navigation

The application shall provide:

1. Overview.
2. Incidents.
3. Investigations.
4. Remediation Plans.
5. Approvals.
6. Environments.
7. Integrations.
8. Policies.
9. Audit Logs.
10. Analytics.
11. Settings.

### 9.2 Overview dashboard

The dashboard shall show:
- Active incidents by severity.
- Incidents awaiting approval.
- Running remediation workflows.
- Incidents with failed verification.
- Recent verified recoveries.
- Integration health.
- Recent high-risk actions.
- Key operational performance indicators.

### 9.3 Incident detail page

The incident detail page is the primary working interface.

It shall contain:
- Incident summary and current state.
- Affected resources and environment.
- Evidence collected from integrations.
- Root-cause hypotheses and confidence.
- A chronological event timeline.
- Proposed remediation plan.
- Risk and approval status.
- Execution progress and outputs.
- Verification results.
- Escalation and manual takeover controls.

### 9.4 Remediation approval interface

Before approval, the user shall see:
- Why the action is recommended.
- Evidence supporting the diagnosis.
- Exact target resources.
- Exact action parameters.
- Expected impact and risks.
- Whether the action is reversible.
- Preconditions and verification criteria.
- Rollback behavior.
- Required permissions.

Approval must be an explicit action. Opening a plan or viewing a notification must not imply consent.

### 9.5 User experience principles

- Clearly distinguish facts, hypotheses, and recommendations.
- Show the source and freshness of evidence.
- Make action state visible in real time.
- Explain why an action is blocked.
- Make cancellation and escalation discoverable.
- Avoid claiming recovery when verification is incomplete.
- Provide useful error messages when integrations fail.

---

## 10. High-Level Technical Architecture

### 10.1 Logical components

**A. Web Console**

A responsive interface for incidents, investigations, plans, approvals, environments, policies, and analytics.

**B. API Gateway and Identity Layer**

Authenticates requests, enforces tenant boundaries, validates authorization, and exposes versioned APIs.

**C. Incident Ingestion Service**

Receives alerts and webhooks, normalizes events, deduplicates incidents, and publishes work items.

**D. Context Collection Service**

Retrieves Kubernetes, cloud, monitoring, Git, and CI/CD evidence through controlled connectors.

**E. Diagnostic Orchestrator**

Coordinates investigation steps, invokes approved diagnostic tools, and requests structured analysis from an LLM.

**F. Remediation Planner**

Converts validated diagnostic findings into structured remediation plans using registered action definitions.

**G. Policy Engine**

Deterministically evaluates identity, environment, action scope, risk, approval, and organizational policy.

**H. Workflow and Execution Engine**

Executes durable workflows with retries, timeouts, concurrency control, cancellation, and explicit action state transitions.

**I. Integration and Connector Layer**

Provides provider-specific adapters and standardized interfaces for Kubernetes, Prometheus, Azure, Terraform, and CI/CD systems.

**J. Verification Engine**

Runs configured recovery checks, evaluates outcomes, and determines whether an incident can be resolved.

**K. Audit and Analytics Service**

Stores operational events, action results, approvals, policy decisions, and performance metrics.

### 10.2 Architecture principles

- Separate planning from execution.
- Keep authorization and policy evaluation outside the LLM.
- Use a durable workflow engine for long-running operations.
- Treat infrastructure tools as privileged external systems.
- Use asynchronous processing for investigations and remediation.
- Make all actions traceable to a user, policy, incident, and plan.
- Isolate provider-specific implementations behind connector interfaces.
- Keep the MVP modular without requiring a large microservices deployment on day one.

### 10.3 Suggested initial technology stack

| Layer | Proposed technology |
|---|---|
| Frontend | React, Vite, TypeScript, Tailwind CSS |
| Backend API | Go or Python with FastAPI |
| API contract | OpenAPI |
| Primary database | PostgreSQL |
| Job and event processing | Redis-backed queue or a durable workflow engine |
| Workflow orchestration | Temporal or an equivalent durable workflow solution |
| Observability | OpenTelemetry, Prometheus, Grafana |
| Kubernetes integration | Kubernetes client libraries |
| Azure integration | Azure SDKs and supported REST APIs |
| LLM abstraction | Provider-independent model gateway |
| Secrets | Azure Key Vault or another supported secrets manager |
| Authentication | OIDC-compatible identity provider |
| Deployment | Docker and Helm on Kubernetes |
| Infrastructure provisioning | Terraform |

These are proposed choices, not mandatory dependencies. The implementation should select the smallest reliable stack that meets the durability, security, and deployment requirements.

### 10.4 Model usage boundaries

The LLM may:
- Summarize evidence.
- Generate root-cause hypotheses.
- Recommend diagnostic queries from approved templates.
- Propose actions from the registered remediation catalog.
- Explain outcomes and produce incident reports.

The LLM may not independently:
- Grant itself permissions.
- Modify policy rules.
- Bypass approvals.
- Execute arbitrary infrastructure commands.
- Mark an incident resolved without verification.
- Override execution limits or organizational guardrails.

---

## 11. Core Data Model

### 11.1 Organization

Fields:
- `id`
- `name`
- `status`
- `settings`
- `created_at`

### 11.2 Environment

Fields:
- `id`
- `organization_id`
- `name`
- `environment_type`
- `provider`
- `resource_scope`
- `execution_mode`
- `policy_set_id`

### 11.3 Integration

Fields:
- `id`
- `organization_id`
- `environment_id`
- `integration_type`
- `configuration`
- `credential_reference`
- `health_status`
- `last_successful_sync`

Credentials must not be stored as plaintext configuration fields.

### 11.4 Incident

Fields:
- `id`
- `organization_id`
- `environment_id`
- `source`
- `source_event_id`
- `fingerprint`
- `title`
- `description`
- `severity`
- `status`
- `affected_resources`
- `opened_at`
- `resolved_at`
- `correlation_id`

### 11.5 Evidence

Fields:
- `id`
- `incident_id`
- `source_integration_id`
- `evidence_type`
- `resource_reference`
- `observed_at`
- `collected_at`
- `content_reference`
- `content_hash`
- `redaction_status`

### 11.6 Diagnosis

Fields:
- `id`
- `incident_id`
- `model_reference`
- `hypotheses`
- `supporting_evidence_ids`
- `contradictory_evidence_ids`
- `uncertainties`
- `created_at`

### 11.7 Remediation Plan

Fields:
- `id`
- `incident_id`
- `version`
- `diagnosis_id`
- `actions`
- `risk_level`
- `preconditions`
- `verification_policy`
- `rollback_plan`
- `approval_state`
- `created_by`
- `created_at`

### 11.8 Execution

Fields:
- `id`
- `plan_id`
- `plan_version`
- `action_id`
- `target_reference`
- `execution_state`
- `started_at`
- `completed_at`
- `result_reference`
- `idempotency_key`

### 11.9 Approval

Fields:
- `id`
- `plan_id`
- `plan_version`
- `approver_id`
- `decision`
- `decision_reason`
- `policy_version`
- `created_at`

### 11.10 Verification

Fields:
- `id`
- `incident_id`
- `execution_id`
- `verification_policy_id`
- `check_results`
- `overall_result`
- `observed_at`
- `stability_window_completed`

### 11.11 Audit Event

Fields:
- `id`
- `organization_id`
- `actor_type`
- `actor_id`
- `incident_id`
- `plan_id`
- `action`
- `target_reference`
- `decision`
- `timestamp`
- `correlation_id`
- `previous_event_hash`

The audit implementation should use access controls, append-only application behavior, and an independently protected storage destination. Hash chaining alone does not guarantee immutability.

---

## 12. API Requirements

The initial API shall be versioned under `/api/v1`.

### 12.1 Incidents

- `POST /api/v1/incidents` — Create an incident.
- `GET /api/v1/incidents` — List and filter incidents.
- `GET /api/v1/incidents/{id}` — Retrieve incident details.
- `POST /api/v1/incidents/{id}/investigations` — Start an investigation.
- `GET /api/v1/incidents/{id}/timeline` — Retrieve the incident timeline.

### 12.2 Remediation plans

- `GET /api/v1/incidents/{id}/plans` — List remediation plans.
- `POST /api/v1/incidents/{id}/plans` — Generate a plan.
- `GET /api/v1/plans/{id}` — Retrieve a plan.
- `POST /api/v1/plans/{id}/validate` — Validate a plan against policy.
- `POST /api/v1/plans/{id}/approve` — Approve a plan.
- `POST /api/v1/plans/{id}/reject` — Reject a plan.

### 12.3 Execution and verification

- `POST /api/v1/plans/{id}/execute` — Request execution.
- `GET /api/v1/executions/{id}` — Retrieve execution state.
- `POST /api/v1/executions/{id}/cancel` — Request cancellation.
- `POST /api/v1/incidents/{id}/verify` — Run configured verification.
- `POST /api/v1/incidents/{id}/escalate` — Escalate to a human operator.

### 12.4 Configuration and audit

- `GET /api/v1/environments`
- `POST /api/v1/integrations`
- `GET /api/v1/integrations`
- `GET /api/v1/policies`
- `POST /api/v1/policies`
- `GET /api/v1/audit-events`

### 12.5 API security requirements

All protected endpoints must enforce:
- Authentication.
- Organization and environment authorization.
- Input schema validation.
- Rate limiting.
- Audit logging for sensitive operations.
- Idempotency for execution requests.
- Consistent error responses.
- Pagination for list operations.

Webhook endpoints must authenticate incoming requests and defend against replay attacks where the source supports appropriate signatures or timestamps.

---

## 13. Security and Safety Requirements

Security is a core product requirement, not a later enhancement.

### 13.1 Credential security

- Store credentials in an approved secrets manager.
- Use workload identity or short-lived credentials where supported.
- Never expose secrets to the LLM unless a specific, justified requirement exists.
- Redact tokens, credentials, and sensitive values from logs.
- Rotate credentials according to organizational policy.

### 13.2 Authorization

- Enforce least privilege at both the Aegentis and target-system layers.
- Scope permissions by organization, environment, cluster, and resource.
- Revalidate authorization at execution time.
- Do not rely on permissions checked only when a plan was created.
- Require explicit policies for production mutation.

### 13.3 Prompt injection and untrusted evidence

Logs, annotations, Git content, issue descriptions, and other retrieved data must be treated as untrusted input.

Aegentis must:
- Separate retrieved evidence from trusted system instructions.
- Prevent evidence content from directly changing tool permissions.
- Validate all tool arguments against strict schemas.
- Use deterministic policy checks before execution.
- Restrict the action surface to registered tools.
- Avoid passing unnecessary secrets or sensitive data to models.

### 13.4 Production safety

- Default to read-only behavior.
- Require explicit production enablement.
- Use allowlists for autonomous actions.
- Enforce action-specific timeouts and concurrency limits.
- Prevent conflicting execution.
- Support emergency suspension of new automation.
- Record every approval and execution decision.
- Escalate on ambiguous execution results or failed verification.

### 13.5 Multi-tenancy

- Enforce organization-level authorization on every data query.
- Isolate credentials and environment configuration.
- Prevent cross-tenant retrieval through logs, caches, vector stores, and background jobs.
- Test tenant isolation as part of automated security testing.

### 13.6 Data protection

- Encrypt data in transit and at rest.
- Apply configurable retention and deletion policies.
- Redact sensitive logs before model submission.
- Provide audit access controls.
- Document what data is sent to external model providers.

---

## 14. Non-Functional Requirements

Initial targets below are proposed engineering objectives to validate during implementation.

| Category | Requirement |
|---|---|
| Availability | Target 99.9% monthly availability for the production control plane, excluding documented maintenance and external dependency failures |
| API latency | P95 below 500 ms for ordinary database-backed reads under the agreed test load |
| Incident ingestion | P95 below 10 seconds from accepted webhook receipt to persisted incident, under the agreed test load |
| Investigation | Asynchronous, with configurable timeouts and visible progress |
| Execution reliability | Durable action state and recovery after worker restart |
| Security | No unauthorized action execution; enforce tenant isolation |
| Auditability | All privileged actions, policy decisions, and approvals traceable |
| Scalability | Horizontal scaling of stateless API and worker components |
| Observability | Structured logs, metrics, traces, and actionable alerts |
| Portability | Core architecture should not depend on a single LLM provider |
| Accessibility | Core workflows operable using keyboard navigation and accessible labels |
| Maintainability | Versioned APIs, automated tests, documented connector contracts |
| Recovery | Documented backup, restore, and disaster recovery procedures before production rollout |

Latency and availability targets must be measured against defined infrastructure, load, and failure assumptions. External monitoring systems, cloud APIs, and LLM providers can affect end-to-end investigation time.

---

## 15. Key User Workflows

### Workflow A: Automatic incident investigation

1. A monitoring system reports a deployment health alert.
2. Aegentis authenticates and normalizes the incoming event.
3. The incident is deduplicated or associated with an existing incident.
4. Relevant Kubernetes events, logs, metrics, and deployment history are collected.
5. The diagnostic engine creates ranked hypotheses with evidence references.
6. Aegentis records the investigation results.
7. The incident dashboard presents the diagnosis and available remediation options.

**Success condition:** The investigation completes or reports a clear partial-failure state, with evidence provenance and no unauthorized mutation.

### Workflow B: Human-approved remediation

1. Aegentis identifies a likely faulty release.
2. The planner proposes a rollback using a registered action.
3. The policy engine validates scope, permissions, prerequisites, and risk.
4. The UI presents the exact action and its expected impact.
5. An authorized user approves the specific plan version.
6. The execution engine revalidates policy and executes the action.
7. The verification engine evaluates deployment and application health.
8. The incident is marked recovered only when its recovery policy passes.
9. The timeline records all actions and results.

**Success condition:** The approved action executes within scope, recovery is verified, and the audit trail is complete.

### Workflow C: Failed remediation

1. A remediation action executes.
2. Verification shows the service remains unhealthy.
3. The workflow marks recovery as failed.
4. Aegentis evaluates whether an explicitly authorized rollback procedure is safe and applicable.
5. If permitted, the workflow attempts the bounded rollback.
6. If rollback is unavailable or fails, the workflow stops further mutation and escalates.
7. The incident remains open until recovery is verified or a human closes it with an explicit outcome.

**Success condition:** The system avoids uncontrolled retry loops and provides a clear failure report.

### Workflow D: Insufficient evidence

1. An alert is received.
2. Required telemetry is unavailable or contradictory.
3. Aegentis identifies missing evidence.
4. The diagnostic engine refrains from presenting a definitive root cause.
5. The incident is escalated or requests additional diagnostic access.

**Success condition:** Uncertainty is made explicit and no unsupported remediation is executed.

---

## 16. MVP Definition

The MVP should prove that Aegentis can complete a real incident workflow safely, rather than attempting broad integration coverage.

### 16.1 MVP scope

**Must have**
- Authentication and basic role-based access control.
- Organization and environment configuration.
- Kubernetes integration.
- Prometheus Alertmanager-compatible webhook ingestion.
- Manual incident creation.
- Incident normalization and deduplication.
- Evidence collection from Kubernetes and Prometheus.
- LLM-assisted root-cause hypotheses.
- Structured remediation plans.
- Deterministic policy validation.
- Dry-run mode.
- Human approval workflow.
- A small registry of approved remediation actions.
- Durable execution tracking.
- Health-check verification.
- Incident timeline and audit events.
- Basic dashboard and incident detail page.
- Read-only default and safe handling of execution failures.

**Should have**
- Azure Monitor integration.
- Azure DevOps deployment metadata.
- Helm release inspection.
- Notification integration.
- Configurable environment-specific policies.
- Incident export.

**Later**
- Multi-cloud remediation.
- Advanced incident correlation.
- Automated Terraform change execution.
- Multi-agent collaboration.
- Predictive incident detection.
- Cross-incident learning and remediation optimization.
- Advanced SLO and error-budget automation.

### 16.2 MVP acceptance criteria

The MVP is considered functionally complete when:

1. A test alert creates or updates the correct incident.
2. Duplicate alerts are handled according to the configured deduplication policy.
3. Kubernetes and Prometheus evidence is collected and attributed to its source.
4. The diagnostic response references real collected evidence.
5. Insufficient evidence produces an explicit inconclusive result.
6. An unregistered action is rejected by the policy engine.
7. A plan requiring approval cannot execute before approval.
8. Approval for a changed plan cannot authorize the changed version.
9. A registered remediation executes only against its authorized target.
10. Duplicate execution requests do not produce unsafe repeated actions.
11. Recovery is evaluated independently from command success.
12. Failed verification prevents automatic incident closure.
13. Cancellation and timeout states are visible and handled safely.
14. All privileged actions and approval decisions are auditable.
15. A user from one organization cannot access another organization's incidents or credentials.
16. The full workflow can be demonstrated in a disposable or non-production test environment.

---

## 17. Success Metrics and Evaluation

### 17.1 Primary metrics

**Mean time to recovery (MTTR)**

Measure elapsed time from incident start to verified recovery. Compare supported incident classes against a pre-deployment baseline.

**Time to diagnosis**

Measure elapsed time from incident creation to an accepted diagnosis or explicit inconclusive result.

**Remediation success rate**

Number of attempted remediation workflows meeting their predefined recovery criteria divided by total attempted workflows, with failed and inconclusive outcomes reported separately.

**Autonomous resolution rate**

Percentage of eligible incidents resolved without manual execution or intervention, reported separately from human-approved automation.

**Verification accuracy**

Measure false recovery declarations and missed recoveries using independent health signals and test scenarios.

**Human intervention rate**

Percentage of incidents requiring an operator to investigate further, modify a plan, execute manually, or recover from failed automation.

### 17.2 Guardrail metrics

- Unauthorized action execution: target zero.
- Cross-tenant data exposure: target zero.
- False recovery declarations: target zero in the acceptance test suite.
- Actions executed against the wrong resource: target zero.
- Unbounded retries: target zero.
- Policy bypasses: target zero.
- Audit records missing for privileged actions: target zero.

Any violation of a critical safety guardrail blocks production rollout regardless of improvements in MTTR.

### 17.3 Evaluation methodology

Before broad adoption:
1. Establish a baseline for selected incident classes.
2. Replay historical incidents where adequate evidence is available.
3. Run controlled fault-injection tests in a test environment.
4. Compare diagnoses against engineer-reviewed findings.
5. Validate remediation and rollback outcomes.
6. Track false positives, false recovery declarations, and unnecessary actions.
7. Enable autonomous actions only after the corresponding action class passes its safety tests.

---

## 18. Delivery Roadmap

### Phase 0 — Discovery and design

**Deliverables**
- Confirm pilot use cases.
- Define supported environments and action catalog.
- Document security and execution policies.
- Select architecture and integration contracts.
- Define incident and remediation schemas.
- Prepare threat model and test strategy.

**Exit criteria:** A documented MVP scope, architecture, risk register, and testable acceptance criteria.

### Phase 1 — Read-only intelligence

**Deliverables**
- Authentication and environment configuration.
- Kubernetes and Prometheus connectors.
- Incident ingestion and deduplication.
- Context collection and diagnosis.
- Incident workspace and timeline.
- Basic audit trail.

**Exit criteria:** Incidents can be investigated without infrastructure mutations, and evidence is traceable.

### Phase 2 — Controlled remediation

**Deliverables**
- Remediation catalog.
- Structured plan generation.
- Policy engine.
- Approval interface.
- Execution workflow and action-state tracking.
- Verification engine.
- Emergency stop and failure handling.

**Exit criteria:** Approved actions can be executed and recovery verified in a test environment.

### Phase 3 — Pilot and enterprise hardening

**Deliverables**
- Azure Monitor and Azure DevOps integrations.
- Notifications and reporting.
- Stronger RBAC and approval controls.
- Tenant isolation tests.
- Resilience, load, and security testing.
- Deployment, backup, and recovery documentation.

**Exit criteria:** Pilot acceptance criteria pass, safety guardrails are met, and operational ownership is established.

### Phase 4 — Guarded autonomy

**Deliverables**
- Allowlisted autonomous action policies.
- Environment-specific autonomy settings.
- Post-recovery stability windows.
- Recurrence analysis.
- Expanded integration and action catalogs.

**Exit criteria:** Each enabled action class has demonstrated acceptable reliability and safety through documented testing.

### Phase 5 — Advanced capabilities

Potential future work:
- Cross-service incident correlation.
- SLO-aware remediation.
- Change-impact analysis.
- Multi-cloud orchestration.
- Cost-aware scaling recommendations.
- Remediation effectiveness optimization.
- Advanced dependency mapping.

These capabilities are not prerequisites for the initial MVP.

---

## 19. Risks and Mitigations

| Risk | Impact | Mitigation |
|---|---|---|
| Incorrect root-cause diagnosis | Harmful remediation | Evidence requirements, validation checks, approval gates |
| Prompt injection through logs or metadata | Unauthorized or unsafe actions | Treat retrieved content as untrusted; deterministic policy enforcement |
| Excessive privileges | Large blast radius | Least-privilege identities and target-scoped permissions |
| Incorrect recovery determination | False incident closure | Independent health checks and explicit verification criteria |
| Repeated execution | Service disruption | Idempotency, concurrency controls, bounded retries |
| Rollback causes further failure | Prolonged outage | Prevalidated rollback plans and explicit stop conditions |
| Cloud API outage | Incomplete diagnosis or execution | Timeouts, circuit breakers, partial-failure handling |
| LLM outage or latency | Delayed investigation | Bounded timeouts and graceful degradation |
| Model cost escalation | Higher operating cost | Evidence limits, caching where appropriate, model routing and usage budgets |
| Tenant data leakage | Security incident | Backend authorization, isolated credentials, tenant-isolation testing |
| Integration complexity | Delivery delays | Start with Kubernetes and Prometheus; use connector contracts |
| False confidence in automation | Operational risk | Transparent confidence, explicit uncertainty, conservative autonomy defaults |

---

## 20. Dependencies and Assumptions

### Dependencies

- Access to a non-production Kubernetes environment.
- A supported metrics source, initially Prometheus.
- A usable LLM endpoint or local model service.
- Secure identity and credential management.
- A durable database and background execution mechanism.
- Defined recovery checks for each supported remediation.
- Engineering ownership for connector maintenance and production operations.

### Assumptions

- The pilot team has authority to integrate with its target environment.
- Monitoring alerts and telemetry contain enough information to support useful investigations.
- The target system exposes reliable health indicators for supported workflows.
- Organizations can define which actions are safe to automate.
- Infrastructure permissions can be scoped to appropriate resources.
- Pilot success will be evaluated using measured outcomes, not unvalidated marketing claims.

---

## 21. Product Positioning and Differentiation

### Positioning statement

Aegentis is an autonomous SRE platform that turns operational signals into controlled remediation and verified recovery.

### Core differentiators

1. **Closed-loop remediation:** Diagnosis, execution, and verification form one workflow.
2. **Evidence-backed reasoning:** Recommendations are linked to collected operational evidence.
3. **Policy-enforced autonomy:** A deterministic control layer governs what the AI may execute.
4. **Recovery-oriented outcomes:** Incident resolution depends on health criteria, not command status.
5. **Infrastructure-aware operations:** Kubernetes, cloud telemetry, and deployment history can be correlated.
6. **Enterprise accountability:** Approvals, actions, decisions, and outcomes are recorded.

### Relationship to existing engineering tools

Aegentis should integrate with existing tools rather than recreate their entire functionality.

- Monitoring platforms remain responsible for metrics and alert generation.
- CI/CD platforms remain responsible for pipeline execution.
- Terraform remains responsible for infrastructure-as-code planning and application.
- Kubernetes and cloud APIs remain the systems of record for infrastructure state.
- Aegentis coordinates investigation, policy-controlled remediation, and recovery verification across these systems.

### Relationship to existing projects

The implementation can reuse capabilities from existing engineering work where appropriate:

- **k8s-helm-mcp:** A potential source of Kubernetes and Helm diagnostic tools through a controlled integration boundary.
- **PipelineIQ:** A potential source of pipeline-incident enrichment, diagnosis, and reporting concepts.
- **GitMagician:** A potential source of repository analysis and change-context capabilities.

These are integration opportunities, not assumed completed integrations. Each connector must be evaluated for its permissions, reliability, auditability, and execution contract before production use.

---

## 22. Open Product Decisions

The following decisions should be resolved during Phase 0:

1. Will the first deployment be self-hosted, managed, or support both?
2. Which identity provider will be used for authentication and enterprise SSO?
3. Which backend language best fits the implementation team and existing components?
4. Will Temporal or another durable workflow engine be adopted?
5. Which LLM providers and deployment modes are required?
6. What evidence may be sent to external model providers?
7. Which Kubernetes remediation actions are approved for the initial catalog?
8. Which incident sources are mandatory for the pilot?
9. What is the required audit retention period?
10. Which user roles may approve production remediation?
11. What is the maximum acceptable execution blast radius?
12. Which recovery criteria must pass before an incident is considered resolved?

These decisions should be captured in architecture decision records rather than left implicit in implementation.

---

## 23. Definition of Done

Aegentis MVP is ready for a controlled pilot when:

- Core incident workflows are implemented and tested.
- Required integrations operate reliably in the target test environment.
- Read-only investigation works without mutation privileges.
- Registered remediation actions have explicit preconditions and verification procedures.
- Approval and policy enforcement are tested at the backend.
- Failed verification, timeouts, retries, and cancellation are handled safely.
- Privileged operations are auditable.
- Authentication, authorization, and tenant-isolation tests pass.
- Secrets are managed securely and sensitive output is redacted.
- Dashboards expose actual workflow state and measured operational outcomes.
- Deployment and recovery procedures are documented.
- Pilot users can complete the incident lifecycle without relying on undocumented manual steps.
- Critical security and safety guardrails pass their acceptance tests.

---

## 24. Final Product Summary

**Aegentis — Detect. Resolve. Prove.**

Aegentis is designed to move SRE operations from reactive investigation toward controlled, evidence-driven autonomy.

Its first release should concentrate on a narrow but complete workflow: ingest an incident, collect evidence, generate a diagnosis, propose an approved remediation, execute it safely, verify recovery, and retain an auditable record.

The MVP should prioritize correctness, operational safety, and transparent outcomes over the number of integrations or autonomous actions supported.

The long-term objective is to establish Aegentis as a trusted operational control plane for cloud-native engineering teams, with autonomy earned incrementally through measurable reliability and explicit policy enforcement.
