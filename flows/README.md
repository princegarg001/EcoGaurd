# EcoGuard Flows

This directory contains YAML workflow definitions for GitLab Duo.

## Available Flows

- `eco-check.yml` - Analyze code on MR (Sustainability Compliance Agent)
- `carbon-track.yml` - Calculate emissions on pipeline completion (Carbon Footprint Agent)
- `weekly-optimization.yml` - Weekly resource analysis (Resource Optimization Agent)
- `eco-deploy.yml` - Optimize deployment timing (Eco-Friendly Deployment Agent)
- `dashboard-update.yml` - Daily metrics aggregation (Dashboard Data Agent)

## Flow Structure

Each flow defines:

- **Trigger**: When the flow runs (event, schedule, manual)
- **Steps**: Sequential or parallel agent invocations
- **Inputs**: Data passed to agents
- **Outputs**: Results and actions (comments, issues, files)

## Enabling Flows

1. Copy flow files to `.gitlab/workflows/` in your project
2. Go to **Automate > Triggers** in GitLab
3. Create triggers for each flow
4. Test with sample events

See `docs/FLOWS.md` for detailed configuration.
