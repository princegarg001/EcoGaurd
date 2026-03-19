# EcoGuard Quick Start Guide

Get EcoGuard up and running in 10 minutes!

## 🚀 5-Minute Setup

### 1. Clone & Install

```bash
git clone https://gitlab.com/princegarg001-group/EcoGuard.git
cd EcoGuard
pip install -r requirements.txt
```

### 2. Set Environment Variables

```bash
export ELECTRICITY_MAPS_API_KEY="your_key"
export GITLAB_TOKEN="your_token"
export CI_PROJECT_ID="80410036"
```

### 3. Run Tests

```bash
cd agents
python -m pytest test_*.py -v
```

### 4. View Dashboard

```bash
open dashboards/src/index.html
```

## 📊 Using EcoGuard

### Automatic Analysis (No Action Needed)

EcoGuard automatically analyzes your project:

- **On Merge Request** → Code efficiency analysis
- **On Pipeline** → Energy & CO₂ calculation
- **On Deployment** → Optimal timing recommendation
- **Daily at 00:00 UTC** → Resource optimization report
- **Daily at 01:00 UTC** → Dashboard metrics update

### Manual Analysis (On Demand)

Trigger analysis by mentioning agents in comments:

```
@ecoguard-compliance analyze this code
@ecoguard-carbon calculate emissions
@ecoguard-optimize generate report
```

## 📈 Dashboard Features

### Overview Tab
- Daily emissions trend
- Energy consumption
- Emissions by source
- Carbon intensity by region

### Metrics Tab
- Daily/weekly/monthly totals
- CO₂ per build (SCI score)
- Trend comparisons
- Energy reduction %

### Goals Tab
- Track sustainability targets
- Progress indicators
- Status tracking
- Deadline monitoring

### Issues Tab
- High priority problems
- Severity levels
- Estimated savings

### Recommendations Tab
- Optimization suggestions
- Impact quantification
- Priority ranking

## 🔧 Configuration

### API Keys

Get free API keys:

1. **Electricity Maps** - https://www.electricitymap.org/
   - Sign up for free tier
   - Get API key from dashboard

2. **GitLab Token** - https://gitlab.com/-/profile/personal_access_tokens
   - Create token with `api` scope
   - Keep it secret!

### Environment Variables

Set in GitLab project settings:

```
Settings > CI/CD > Variables
```

Required variables:
- `ELECTRICITY_MAPS_API_KEY`
- `GITLAB_TOKEN`
- `CI_PROJECT_ID`

Optional variables:
- `PROMETHEUS_URL` - For metrics collection
- `GOOGLE_CLOUD_TOKEN` - For cloud metrics
- `SLACK_WEBHOOK_URL` - For Slack notifications

## 📝 Common Tasks

### View Dashboard

```bash
open dashboards/src/index.html
```

### Run Agent Tests

```bash
cd agents
python -m pytest test_compliance.py -v
python -m pytest test_carbon_footprint.py -v
python -m pytest test_resource_optimization.py -v
python -m pytest test_eco_friendly_deployment.py -v
python -m pytest test_dashboard_data.py -v
```

### Test Individual Agent

```bash
cd agents
python sustainability_compliance.py
python carbon_footprint.py
python resource_optimization.py
python eco_friendly_deployment.py
python dashboard_data.py
```

### Check Flow Status

1. Go to **Automate > Flow Runs**
2. View execution history
3. Check logs for errors

### View Metrics

1. Open dashboard: `dashboards/src/index.html`
2. Click on **Metrics** tab
3. View daily/weekly/monthly data

## 🎯 First Steps

1. **Create a test branch**
   ```bash
   git checkout -b test/ecoguard
   ```

2. **Make a code change**
   ```bash
   echo "# Test" >> README.md
   git add README.md
   git commit -m "Test commit"
   ```

3. **Create a merge request**
   - Push branch
   - Create MR
   - Watch for eco-check analysis

4. **Run a pipeline**
   - Commit triggers pipeline
   - Watch for carbon-track analysis
   - Check dashboard for metrics

5. **View results**
   - Check MR comments
   - View pipeline comments
   - Open dashboard

## 📚 Learn More

- [Full Installation Guide](INSTALLATION.md)
- [Agent Documentation](agents/)
- [Flow Configuration](docs/FLOWS.md)
- [Dashboard Guide](docs/DASHBOARD.md)
- [Contributing Guidelines](CONTRIBUTING.md)

## ❓ Troubleshooting

### Dashboard not loading?
- Check browser console for errors
- Verify data files exist in `dashboards/data/`
- Clear browser cache

### Agents not responding?
- Check GitLab Duo is enabled
- Verify API keys are set
- Check agent logs

### Flows not executing?
- Verify triggers are configured
- Check flow YAML syntax
- Review execution logs

## 🎉 You're Ready!

EcoGuard is now monitoring your project's sustainability. Check the dashboard regularly to:

- Track CO₂ emissions
- Monitor energy usage
- Implement recommendations
- Achieve sustainability goals

**Happy coding! 🌍**
