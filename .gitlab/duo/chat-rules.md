# EcoGuard Chat Trigger Rules

This file defines how to trigger EcoGuard agents through GitLab chat and comments.

## Mention-Based Triggers

### Sustainability Compliance Check

**Trigger**: Mention `@ecoguard-compliance` in an MR comment

```
@ecoguard-compliance analyze this code for efficiency issues
```

**Agent**: Sustainability Compliance Agent  
**Action**: Analyzes the MR diff and posts feedback with optimization suggestions

### Carbon Footprint Analysis

**Trigger**: Mention `@ecoguard-carbon` in a pipeline comment or issue

```
@ecoguard-carbon calculate emissions for this pipeline
```

**Agent**: Carbon Footprint Agent  
**Action**: Fetches pipeline metrics and posts CO₂ calculation with breakdown

### Resource Optimization Report

**Trigger**: Mention `@ecoguard-optimize` in an issue

```
@ecoguard-optimize generate weekly optimization report
```

**Agent**: Resource Optimization Agent  
**Action**: Analyzes recent jobs and creates a detailed optimization report

### Deployment Optimization

**Trigger**: Mention `@ecoguard-deploy` in a deployment issue/MR

```
@ecoguard-deploy suggest optimal deployment time
```

**Agent**: Eco-Friendly Deployment Agent  
**Action**: Analyzes grid carbon intensity and recommends deployment timing

## Automatic Triggers

### On Merge Request Creation

- **Trigger**: New MR opened
- **Agent**: Sustainability Compliance Agent
- **Action**: Automatically analyzes code changes and posts initial feedback

### On Pipeline Completion

- **Trigger**: Pipeline succeeds or fails
- **Agent**: Carbon Footprint Agent
- **Action**: Automatically calculates and posts pipeline emissions

### Daily Scheduled

- **Trigger**: 00:00 UTC daily
- **Agent**: Resource Optimization Agent + Dashboard Data Agent
- **Action**: Generates weekly reports and updates dashboard data

## Chat Commands

In the EcoGuard chat sidebar:

```
/analyze-file <file-path>          # Analyze specific file for efficiency
/carbon-report <pipeline-id>       # Get detailed carbon report
/optimization-tips                 # Get general optimization suggestions
/dashboard-status                  # Show current sustainability metrics
/set-goal <target> <date>         # Set sustainability goal (e.g., "reduce CO₂ by 20% by 2024-12-31")
```

## Configuration

To enable these triggers in your GitLab project:

1. Go to **Automate > Triggers**
2. Create triggers for each agent with appropriate events
3. Link triggers to corresponding flows in `/flows/`
4. Test with sample commits/MRs

See [Flow Configuration](../docs/FLOWS.md) for detailed setup instructions.
