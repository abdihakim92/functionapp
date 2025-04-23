
# Task Implementation Summary

## Overview
This repository contains the deployment setup for a Python-based Azure Function App using Terraform and GitHub Actions. The CI workflow is designed to provision infrastructure and deploy application code based on commit messages.

## Key Features

- **Self-Hosted GitHub Actions Runner**
  - Ubuntu VM provisioned in Azure.
  - Runner activated via `run.sh` during terminal sessions for secure, session-based execution.
  - Authentication handled using provided user credentials (email & password) with Contributor access.

- **Infrastructure as Code (IaC)**
  - Azure resources (Function App, App Service Plan, Storage Account, Application Insights) provisioned using Terraform.

- **Conditional CI Workflow**
  - Single pipeline with two stages:
    - **[infra]**: Runs infrastructure provisioning.
    - **[app]**: Deploys Function App code.
    - **[all]**: Executes both stages and performs post-deployment testing.
  - Note: Deployment stage runs even if infrastructure stage fails.

- **Repository Enhancements**
  - Workflow status badge included in `README.md`.

## Pipeline Logic
- Commit message triggers:
  - `[infra]` → Runs infrastructure stage.
  - `[app]` → Runs deployment stage.
  - `[all]` → Runs both stages + test.

## Known Limitations
- The pipeline does not prevent the deployment stage from running if the infrastructure stage fails.
- The self-hosted runner is manually activated and is not a persistent background service.

## Blockers Resolved
1. **Application Insights Workspace Migration**
   - Manually referenced `workspace_id` in Terraform.

2. **Pipeline Execution Flow**
   - Accepted current conditional setup; improvement needed for better failure handling.

3. **Runner Configuration**
   - Manual session-based runner setup due to lack of Service Principal.

## Outcome
- Automated infrastructure provisioning and app deployment.
- Conditional CI workflow for efficient execution.
- Deployment verified through live testing.
- Status badge reflects real-time pipeline health.
