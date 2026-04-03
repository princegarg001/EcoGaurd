---
title: Flows
---

# Flows

Flows define when EcoGuard agents run and what each workflow publishes.

## Core workflows

### Eco Check

- Trigger: merge request opened or updated
- Purpose: analyze code for sustainability issues
- Result: comments, suggestions, and possible issue creation

### Carbon Track

- Trigger: pipeline success or failure
- Purpose: calculate pipeline emissions and publish a report
- Result: comments and dashboard updates

### Weekly Optimization

- Trigger: scheduled daily run or periodic review window
- Purpose: analyze the previous 7 days for heavy jobs
- Result: optimization report and actionable recommendations

### Eco Deploy

- Trigger: deployment initiated
- Purpose: choose a lower-carbon deployment time
- Result: timing recommendation and optional deferral

## Files to review

- [flows/README.md](../flows/README.md)
- [flows/eco-check.yml](../flows/eco-check.yml)
- [flows/carbon-track.yml](../flows/carbon-track.yml)
- [flows/weekly-optimization.yml](../flows/weekly-optimization.yml)
- [flows/eco-deploy.yml](../flows/eco-deploy.yml)
# EcoGuard Flow Configuration

This document describes the YAML workflows that orchestrate EcoGuard agents.

## Flow: Eco Check (On Merge Request)

**File**: `flows/eco-check.yml`  
**Trigger**: Merge request opened or updated  
**Purpose**: Analyze code for sustainability issues

### Workflow

1. **Sustainability Compliance Agent** analyzes code diff
2. Posts feedback with optimization suggestions
3. Creates issues for significant inefficiencies
4. Updates MR with sustainability score

### Configuration

```yaml
name: Eco Check
trigger:
  type: merge_request
  events:
    - opened
    - updated

steps:
  - name: Analyze Code
    agent: sustainability-compliance
    inputs:
      - mr_diff
      - file_paths
    outputs:
      - issues_found
      - suggestions
  
  - name: Post Feedback
    type: comment
    inputs:
      - suggestions
    target: merge_request
  
  - name: Create Issues
    type: issue_creation
    inputs:
      - issues_found
    condition: "issues_found.count > 0"
```

## Flow: Carbon Track (On Pipeline Completion)

**File**: `flows/carbon-track.yml`  
**Trigger**: Pipeline succeeds or fails  
**Purpose**: Calculate and report pipeline emissions

### Workflow

1. **Carbon Footprint Agent** collects pipeline metrics
2. Fetches current grid carbon intensity
3. Calculates energy and CO₂
4. Posts detailed report as pipeline comment
5. Updates dashboard data

### Configuration

```yaml
name: Carbon Track
trigger:
  type: pipeline
  events:
    - success
    - failure

steps:
  - name: Collect Metrics
    agent: carbon-footprint
    inputs:
      - pipeline_id
      - job_metrics
    outputs:
      - energy_kwh
      - emissions_kg_co2
      - breakdown
  
  - name: Post Report
    type: comment
    inputs:
      - energy_kwh
      - emissions_kg_co2
      - breakdown
    target: pipeline
  
  - name: Update Dashboard
    agent: dashboard-data
    inputs:
      - energy_kwh
      - emissions_kg_co2
      - timestamp
```

## Flow: Weekly Optimization (Scheduled)

**File**: `flows/weekly-optimization.yml`  
**Trigger**: Daily at 00:00 UTC  
**Purpose**: Analyze resource usage and recommend optimizations

### Workflow

1. **Resource Optimization Agent** analyzes past 7 days of metrics
2. Identifies heavy jobs and inefficiencies
3. Creates weekly optimization report issue
4. Suggests specific improvements

### Configuration

```yaml
name: Weekly Optimization
trigger:
  type: schedule
  cron: "0 0 * * *"  # Daily at 00:00 UTC

steps:
  - name: Analyze Resources
    agent: resource-optimization
    inputs:
      - time_range: "7d"
      - metrics_query: "prometheus"
    outputs:
      - heavy_jobs
      - optimization_suggestions
  
  - name: Create Report
    type: issue_creation
    inputs:
      - heavy_jobs
      - optimization_suggestions
    title: "Weekly Optimization Report"
    labels:
      - optimization
      - weekly
```

## Flow: Eco Deploy (On Deployment)

**File**: `flows/eco-deploy.yml`  
**Trigger**: Deployment initiated  
**Purpose**: Recommend optimal deployment timing

### Workflow

1. **Eco-Friendly Deployment Agent** analyzes deployment parameters
2. Fetches carbon intensity forecast
3. Recommends optimal deployment time
4. Suggests alternative regions if beneficial
5. Posts recommendations as comment

### Configuration

```yaml
name: Eco Deploy
trigger:
  type: deployment
  events:
    - initiated

steps:
  - name: Analyze Deployment
    agent: eco-friendly-deployment
    inputs:
      - target_region
      - deployment_size
      - current_time
    outputs:
      - optimal_time
      - carbon_savings
      - alternative_regions
  
  - name: Post Recommendations
    type: comment
    inputs:
      - optimal_time
      - carbon_savings
      - alternative_regions
    target: deployment_issue
```

## Flow: Dashboard Update (Daily)

**File**: `flows/dashboard-update.yml`  
**Trigger**: Daily at 01:00 UTC  
**Purpose**: Aggregate metrics and update dashboard

### Workflow

1. **Dashboard Data Agent** aggregates daily metrics
2. Calculates weekly and monthly totals
3. Computes SCI scores
4. Updates dashboard data files
5. Generates summary report

### Configuration

```yaml
name: Dashboard Update
trigger:
  type: schedule
  cron: "0 1 * * *"  # Daily at 01:00 UTC

steps:
  - name: Aggregate Metrics
    agent: dashboard-data
    inputs:
      - time_range: "24h"
    outputs:
      - daily_metrics
      - weekly_totals
      - monthly_totals
      - sci_scores
  
  - name: Update Dashboard Data
    type: file_update
    inputs:
      - daily_metrics
      - weekly_totals
      - monthly_totals
    files:
      - dashboards/data/daily-metrics.json
      - dashboards/data/weekly-totals.json
      - dashboards/data/monthly-totals.json
```

## Enabling Flows

1. Copy flow files to `.gitlab/workflows/` in your project
2. Go to **Automate > Triggers**
3. Create a trigger for each flow:
   - Select the flow file
   - Configure trigger conditions
   - Set any required variables
4. Test the flow with sample events

## Customizing Flows

To customize a flow:

1. Edit the YAML file in `.gitlab/workflows/`
2. Modify trigger conditions, steps, or outputs
3. Commit and push changes
4. Flows update automatically

## Monitoring Flow Execution

1. Go to **Automate > Flow Runs**
2. View execution history and logs
3. Check for errors or failures
4. Review agent outputs and decisions

## Next Steps

- Review [Agent Definitions](.gitlab/duo/AGENTS.md) for agent capabilities
- Check [Chat Rules](.gitlab/duo/chat-rules.md) for manual triggers
- Set up the [Dashboard](DASHBOARD.md) to visualize results
