---
title: Dashboard
---

# Dashboard

The dashboard turns EcoGuard metrics into a readable sustainability view.

## What it shows

- CO₂ emissions over time
- Energy usage by day and week
- Compliance issues and recommendations
- Grid carbon intensity and deployment windows
- Sustainability goal progress

## Data files

- [dashboards/data/daily-metrics.json](../dashboards/data/daily-metrics.json)
- [dashboards/data/weekly-metrics.json](../dashboards/data/weekly-metrics.json)
- [dashboards/data/monthly-metrics.json](../dashboards/data/monthly-metrics.json)
- [dashboards/data/summary.json](../dashboards/data/summary.json)
- [dashboards/data/sustainability-goals.json](../dashboards/data/sustainability-goals.json)

## Frontend files

- [public/index.html](../public/index.html)
- [public/dashboard.html](../public/dashboard.html)
- [public/dashboard.js](../public/dashboard.js)

## How it stays fresh

1. The collector writes new metrics into JSON.
2. The API or static files serve those metrics.
3. The dashboard fetches the JSON and redraws charts.
# EcoGuard Dashboard Guide

The EcoGuard Dashboard visualizes sustainability metrics and tracks progress toward green goals.

## Dashboard Features

### Metrics Displayed

1. **CO₂ Emissions Over Time**
   - Daily, weekly, and monthly totals
   - Trend line showing progress
   - Comparison to baseline

2. **Energy Usage**
   - kWh per build
   - kWh per deployment
   - Total project energy consumption

3. **Compliance Issues**
   - Number of issues opened
   - Issues resolved
   - Trend in code efficiency

4. **Resource Utilization**
   - CPU and memory usage patterns
   - Heavy job identification
   - Optimization recommendations

5. **Grid Carbon Intensity**
   - Current intensity by region
   - 72-hour forecast
   - Optimal deployment windows

6. **Sustainability Goals**
   - Progress toward targets
   - Estimated completion date
   - Impact visualization

## Data Structure

Dashboard data is stored in JSON format in `/dashboards/data/`:

### daily-metrics.json

```json
[
  {
    "date": "2024-03-19",
    "total_energy_kwh": 45.2,
    "total_emissions_kg_co2": 18.5,
    "builds_count": 12,
    "deployments_count": 2,
    "compliance_issues": 3,
    "avg_carbon_intensity": 250
  }
]
```

### weekly-totals.json

```json
[
  {
    "week": "2024-03-11",
    "total_energy_kwh": 312.5,
    "total_emissions_kg_co2": 128.3,
    "builds_count": 85,
    "deployments_count": 12,
    "avg_emissions_per_build": 1.51,
    "optimization_suggestions": 5
  }
]
```

### compliance-issues.json

```json
[
  {
    "date": "2024-03-19",
    "issue_id": 42,
    "title": "Inefficient loop in data processor",
    "severity": "medium",
    "estimated_savings_kwh": 2.5,
    "status": "open"
  }
]
```

## Deployment Options

### Option 1: Static HTML Dashboard

Use the included HTML template with D3.js for visualization:

```bash
cd dashboards
npm install
npm run build
```

Deploy to GitLab Pages:

```yaml
# .gitlab-ci.yml
pages:
  stage: deploy
  script:
    - cd dashboards && npm run build
  artifacts:
    paths:
      - public
  only:
    - main
```

### Option 2: GitLab Wiki

Embed dashboard as a wiki page:

1. Create `docs/wiki/dashboard.md`
2. Include charts using embedded HTML/JavaScript
3. Link from project wiki

### Option 3: Grafana Integration

For advanced monitoring:

1. Set up Grafana instance
2. Connect to Prometheus data source
3. Import EcoGuard dashboard template
4. Link from GitLab project

## Customizing the Dashboard

### Adding New Metrics

1. Update Dashboard Data Agent in `.gitlab/duo/AGENTS.md`
2. Add metric calculation logic
3. Update data JSON schema
4. Add chart to dashboard template

### Changing Chart Types

Edit `/dashboards/src/charts.js`:

```javascript
// Example: Change to bar chart
const emissionsChart = new Chart(ctx, {
  type: 'bar',  // or 'line', 'pie', etc.
  data: {
    labels: dates,
    datasets: [{
      label: 'CO₂ Emissions (kg)',
      data: emissions,
      backgroundColor: '#10b981'
    }]
  }
});
```

### Setting Sustainability Goals

1. Edit `/dashboards/config.json`:

```json
{
  "goals": [
    {
      "name": "Reduce CO₂ by 20%",
      "target": 100,
      "baseline": 125,
      "deadline": "2024-12-31",
      "metric": "monthly_emissions_kg_co2"
    }
  ]
}
```

2. Dashboard automatically tracks progress

## Sharing the Dashboard

### Public Access

1. Deploy to GitLab Pages (see Option 1)
2. Share public URL with stakeholders
3. Dashboard updates automatically daily

### Embedded in GitLab

1. Create wiki page with embedded dashboard
2. Link from project README
3. Accessible to all project members

### Email Reports

Configure automated email reports:

1. Create flow in `.gitlab/workflows/email-report.yml`
2. Trigger weekly or monthly
3. Attach dashboard snapshot and metrics

## Interpreting Dashboard Data

### Green Indicators

- **Downward trend** in CO₂ and energy usage
- **Increasing** compliance issue resolution rate
- **Decreasing** average emissions per build
- **More deployments** during low-carbon windows

### Areas for Improvement

- **Spikes** in energy usage (investigate heavy jobs)
- **Unresolved** compliance issues (prioritize fixes)
- **High** emissions per build (optimize resource usage)
- **Missed** low-carbon deployment windows

## Troubleshooting

### Dashboard not updating

- Check Dashboard Data Agent logs
- Verify data files are being written to `/dashboards/data/`
- Ensure flow is scheduled correctly

### Charts not displaying

- Check browser console for JavaScript errors
- Verify data JSON format is correct
- Clear browser cache and reload

### Missing metrics

- Verify agents are collecting data
- Check Prometheus connectivity
- Review agent logs for errors

## Next Steps

- Review [Agent Definitions](.gitlab/duo/AGENTS.md)
- Check [Flow Configuration](FLOWS.md)
- Set up [Chat Rules](.gitlab/duo/chat-rules.md)
