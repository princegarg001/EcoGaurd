# EcoGuard Setup Guide

This guide walks you through setting up EcoGuard in your GitLab project.

## Prerequisites

- GitLab 15.0+ with GitLab Duo enabled
- Access to GitLab Duo Agent Platform
- (Optional) Prometheus instance for metrics collection
- (Optional) API keys for external services:
  - Electricity Maps API key (for carbon intensity data)
  - Google Cloud credentials (for cloud metrics)

## Step 1: Clone EcoGuard

```bash
git clone https://gitlab.com/princegarg001-group/EcoGuard.git
cd EcoGuard
```

## Step 2: Configure External APIs

### Electricity Maps API

1. Sign up at [Electricity Maps](https://www.electricitymap.org/)
2. Get your API key from the dashboard
3. In your GitLab project, go to **Settings > CI/CD > Variables**
4. Add variable: `ELECTRICITY_MAPS_API_KEY` = your API key

### Google Cloud (Optional)

1. Set up a Google Cloud project with BigQuery enabled
2. Create a service account and download credentials
3. Add variable: `GOOGLE_CLOUD_TOKEN` = your OAuth2 token
4. Add variable: `GOOGLE_CLOUD_PROJECT` = your project ID

## Step 3: Enable GitLab Duo Agents

1. Go to **Automate > Agents** in your GitLab project
2. Click **New agent**
3. Name it `ecoguard`
4. Copy the registration token
5. In your local clone, create `.gitlab/agents/ecoguard/config.yaml`:

```yaml
gilab_duo:
  enabled: true
  agents:
    - name: sustainability-compliance
      enabled: true
    - name: carbon-footprint
      enabled: true
    - name: resource-optimization
      enabled: true
    - name: eco-friendly-deployment
      enabled: true
```

## Step 4: Configure Flows

1. Copy flow files from `/flows/` to `.gitlab/workflows/`
2. Update flow configurations with your project details
3. Go to **Automate > Triggers** and create triggers for each flow
4. Test triggers with sample commits/MRs

## Step 5: Set Up Prometheus (Optional)

If you want to collect detailed metrics:

1. Deploy Prometheus to monitor GitLab Runner
2. Configure GitLab Runner to expose metrics:

```toml
[[runners]]
  [runners.machine]
    prometheus_listen_address = "0.0.0.0:9252"
```

3. Add Prometheus URL to project variables: `PROMETHEUS_URL`

## Step 6: Initialize Dashboard

1. Create `/dashboards/data/` directory
2. Initialize baseline metrics:

```bash
mkdir -p dashboards/data
echo '[]' > dashboards/data/daily-metrics.json
echo '[]' > dashboards/data/compliance-issues.json
```

3. Deploy dashboard (see [Dashboard Guide](DASHBOARD.md))

## Step 7: Test EcoGuard

1. Create a test branch with sample code
2. Open a merge request
3. Comment: `@ecoguard-compliance analyze this code`
4. Verify the agent responds with feedback
5. Run a pipeline and check for carbon footprint comment

## Troubleshooting

### Agents not responding

- Check that GitLab Duo is enabled in your workspace
- Verify agent configuration in `.gitlab/duo/AGENTS.md`
- Check project variables are set correctly

### API calls failing

- Verify API keys are correct and have appropriate permissions
- Check network connectivity to external services
- Review agent logs in **Automate > Agent Logs**

### Metrics not collecting

- Ensure Prometheus is running and accessible
- Verify `PROMETHEUS_URL` variable is set
- Check GitLab Runner is configured to expose metrics

## Next Steps

- Read [Agent Definitions](.gitlab/duo/AGENTS.md) to understand each agent
- Review [Flow Configuration](FLOWS.md) to customize workflows
- Set up the [Dashboard](DASHBOARD.md) for visualization
- Check [Chat Rules](.gitlab/duo/chat-rules.md) for available commands
