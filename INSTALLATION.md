# EcoGuard Installation & Setup Guide

## Prerequisites

- GitLab 15.0+ with GitLab Duo enabled
- Python 3.9+
- Node.js 16+ (for dashboard)
- Git

## Quick Start (5 minutes)

### 1. Clone the Repository

```bash
git clone https://gitlab.com/princegarg001-group/EcoGuard.git
cd EcoGuard
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root:

```bash
# API Keys
ELECTRICITY_MAPS_API_KEY=your_api_key_here
GOOGLE_CLOUD_TOKEN=your_token_here
GITLAB_TOKEN=your_gitlab_token

# URLs
PROMETHEUS_URL=http://prometheus:9090
CI_API_V4_URL=https://gitlab.com/api/v4

# Configuration
CI_PROJECT_ID=80410036
RUNNER_REGION=US-CA
DASHBOARD_DATA_DIR=dashboards/data
```

### 3. Install Dependencies

```bash
# Install Python dependencies
pip install -r requirements.txt

# Install Node dependencies (for dashboard)
cd dashboards
npm install
cd ..
```

### 4. Run Tests

```bash
# Run all agent tests
cd agents
python -m pytest test_*.py -v
cd ..
```

### 5. Start Dashboard

```bash
# Open dashboard in browser
open dashboards/src/index.html
# or
firefox dashboards/src/index.html
```

## Full Setup (15 minutes)

### Step 1: Configure GitLab Project

1. Go to your GitLab project
2. Navigate to **Settings > CI/CD > Variables**
3. Add the following variables:
   - `ELECTRICITY_MAPS_API_KEY` - Your Electricity Maps API key
   - `GOOGLE_CLOUD_TOKEN` - Your Google Cloud token
   - `GITLAB_TOKEN` - Your GitLab personal access token
   - `PROMETHEUS_URL` - Your Prometheus instance URL

### Step 2: Enable GitLab Duo Agents

1. Go to **Automate > Agents**
2. Click **New agent**
3. Name it `ecoguard`
4. Copy the registration token
5. Create `.gitlab/agents/ecoguard/config.yaml`:

```yaml
gitlab_duo:
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
    - name: dashboard-data
      enabled: true
```

### Step 3: Configure Flows

1. Go to **Automate > Triggers**
2. Create triggers for each flow:
   - `eco-check.yml` - On MR opened/updated
   - `carbon-track.yml` - On pipeline success/failure
   - `eco-deploy.yml` - On deployment
   - `weekly-optimization.yml` - Daily at 00:00 UTC
   - `dashboard-update.yml` - Daily at 01:00 UTC

### Step 4: Set Up Notifications

#### Slack Integration

1. Create a Slack webhook URL
2. Add to GitLab project variables: `SLACK_WEBHOOK_URL`
3. Configure in flow files

#### Email Integration

1. Configure SMTP settings in GitLab
2. Set email recipients in flow files

### Step 5: Deploy Dashboard

1. Push to `main` branch
2. CI/CD pipeline automatically deploys to GitLab Pages
3. Access at: `https://your-namespace.gitlab.io/EcoGuard`

## Verify Installation

### Check Agents

```bash
# Test Sustainability Compliance Agent
python agents/sustainability_compliance.py

# Test Carbon Footprint Agent
python agents/carbon_footprint.py

# Test Resource Optimization Agent
python agents/resource_optimization.py

# Test Eco-Friendly Deployment Agent
python agents/eco_friendly_deployment.py

# Test Dashboard Data Agent
python agents/dashboard_data.py
```

### Check Dashboard

1. Open `dashboards/src/index.html` in browser
2. Verify all tabs load correctly
3. Check that data files are accessible

### Check Flows

1. Go to **Automate > Flow Runs**
2. Verify flows are executing
3. Check logs for any errors

## Troubleshooting

### Agents Not Responding

- Check GitLab Duo is enabled
- Verify agent configuration in `.gitlab/duo/AGENTS.md`
- Check project variables are set correctly
- Review agent logs in **Automate > Agent Logs**

### API Calls Failing

- Verify API keys are correct
- Check network connectivity
- Review error messages in logs
- Test API endpoints manually

### Dashboard Not Loading

- Check browser console for errors
- Verify data files are accessible
- Check CORS settings
- Clear browser cache

### Flows Not Executing

- Verify triggers are configured
- Check flow YAML syntax
- Review flow execution logs
- Test with manual trigger

## Configuration Files

### `.gitlab-ci.yml`

CI/CD pipeline configuration:
- Test stage: Runs all unit tests
- Build stage: Packages agents and dashboard
- Deploy stage: Deploys to GitLab Pages

### `.gitlab/duo/AGENTS.md`

Agent definitions and system prompts

### `.gitlab/duo/mcp.json`

MCP configuration for external APIs

### `.gitlab/duo/chat-rules.md`

Chat trigger rules for manual invocation

## Next Steps

1. **Test with Real Data**
   - Create a test branch
   - Commit code changes
   - Run a pipeline
   - Check dashboard for metrics

2. **Customize Thresholds**
   - Edit agent configurations
   - Adjust notification settings
   - Set sustainability goals

3. **Integrate with Team**
   - Share dashboard URL
   - Configure team notifications
   - Set up regular reviews

4. **Monitor & Optimize**
   - Track metrics over time
   - Implement recommendations
   - Measure impact

## Support

For issues or questions:
1. Check the [documentation](docs/)
2. Review [troubleshooting guide](docs/SETUP.md#troubleshooting)
3. Open an issue on GitLab
4. Check [contributing guidelines](CONTRIBUTING.md)

## License

MIT License - See [LICENSE](LICENSE) file
