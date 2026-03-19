# Dashboard Data Agent

This directory contains the Dashboard Data Agent implementation.

## Files

- `dashboard_data.py` - Core aggregation engine
- `dashboard_data_gitlab.py` - GitLab API integration
- `test_dashboard_data.py` - Unit tests

## Features

### Metrics Collection

**Data Sources:**
- Prometheus metrics (CPU, memory, duration)
- GitLab API (pipelines, deployments, issues)
- Carbon intensity data (grid emissions)
- Deployment metrics (timing, regions)

**Metrics Tracked:**
- Total energy (kWh) by day/week/month
- Total CO₂ emissions (kg CO₂e) by day/week/month
- Build count and deployment count
- Compliance issues opened and resolved
- Optimization recommendations
- Failed jobs and wasted energy
- Average carbon intensity

### Aggregation Levels

**Daily Metrics:**
- Individual day metrics
- 24-hour snapshots
- Real-time tracking

**Weekly Metrics:**
- 7-day aggregation
- Week-over-week comparison
- Energy reduction percentage
- Per-build and per-deployment emissions

**Monthly Metrics:**
- 30-day aggregation
- Month-over-month comparison
- SCI score (Software Carbon Intensity)
- Trend analysis

### Sustainability Goals

**Goal Types:**
- CO₂ reduction targets
- Energy consumption targets
- Compliance issue resolution targets
- SCI score targets

**Goal Tracking:**
- Progress percentage
- Status (on_track, at_risk, achieved)
- Deadline tracking
- Baseline comparison

### Output Files

**Generated JSON Files:**
- `daily-metrics.json` - Daily metrics for all tracked days
- `weekly-metrics.json` - Weekly aggregated metrics
- `monthly-metrics.json` - Monthly aggregated metrics
- `sustainability-goals.json` - Goal definitions and progress
- `summary.json` - Latest metrics and overview

## Usage

### Standalone Aggregation

```python
from dashboard_data import (
    DashboardDataAgent,
    DailyMetrics,
    SustainabilityGoal,
)

agent = DashboardDataAgent()

# Add daily metrics
daily = DailyMetrics(
    date='2024-03-19',
    total_energy_kwh=45.2,
    total_emissions_kg_co2=18.5,
    builds_count=12,
    deployments_count=2,
    compliance_issues_opened=3,
    compliance_issues_resolved=2,
    avg_carbon_intensity_g_per_kwh=250,
    optimization_recommendations_count=5,
    failed_jobs_count=1,
    wasted_energy_kwh=2.5,
)
agent.process_daily_metrics(daily)

# Set goals
goal = SustainabilityGoal(
    goal_id='goal-1',
    name='Reduce CO₂ by 20%',
    target_value=100,
    target_unit='kg_co2',
    baseline_value=125,
    deadline='2024-12-31',
    current_value=110,
    progress_percent=88,
    status='on_track',
)
agent.set_sustainability_goals([goal])

# Aggregate and write
agent.aggregate_and_write()
```

### GitLab Integration

```python
from dashboard_data_gitlab import DashboardDataAgentGitLab

agent = DashboardDataAgentGitLab(project_id='80410036')
agent.collect_and_aggregate(days=7)
```

## Example Output

### daily-metrics.json
```json
[
  {
    "date": "2024-03-19",
    "total_energy_kwh": 45.2,
    "total_emissions_kg_co2": 18.5,
    "builds_count": 12,
    "deployments_count": 2,
    "compliance_issues_opened": 3,
    "compliance_issues_resolved": 2,
    "avg_carbon_intensity_g_per_kwh": 250,
    "optimization_recommendations_count": 5,
    "failed_jobs_count": 1,
    "wasted_energy_kwh": 2.5
  }
]
```

### weekly-metrics.json
```json
[
  {
    "week_start": "2024-03-18",
    "week_end": "2024-03-24",
    "total_energy_kwh": 312.5,
    "total_emissions_kg_co2": 128.3,
    "builds_count": 85,
    "deployments_count": 12,
    "avg_emissions_per_build_kg_co2": 1.51,
    "avg_emissions_per_deployment_kg_co2": 10.69,
    "energy_reduction_pct": 5.2
  }
]
```

### monthly-metrics.json
```json
[
  {
    "month": "2024-03",
    "total_energy_kwh": 1250.0,
    "total_emissions_kg_co2": 512.5,
    "builds_count": 340,
    "deployments_count": 48,
    "avg_emissions_per_build_kg_co2": 1.51,
    "sci_score": 1.51,
    "energy_reduction_pct": 8.5
  }
]
```

### sustainability-goals.json
```json
[
  {
    "goal_id": "goal-1",
    "name": "Reduce CO₂ by 20%",
    "target_value": 100,
    "target_unit": "kg_co2",
    "baseline_value": 125,
    "deadline": "2024-12-31",
    "current_value": 110,
    "progress_percent": 88,
    "status": "on_track"
  }
]
```

## Testing

```bash
python -m pytest test_dashboard_data.py -v
```

## Configuration

**Environment Variables:**
- `PROMETHEUS_URL` - Prometheus instance URL
- `CI_PROJECT_ID` - GitLab project ID
- `GITLAB_TOKEN` - GitLab API token
- `DASHBOARD_DATA_DIR` - Output directory for dashboard data

## Next Steps

- Integrate with Prometheus for real metrics
- Add cloud provider API support
- Implement trend analysis and forecasting
- Create dashboard visualization
- Add email report generation
