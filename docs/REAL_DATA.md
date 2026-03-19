# Real Data Collection Guide

## Overview

The real data collection system automatically gathers metrics from all EcoGuard agents and populates the dashboard with actual data.

## How It Works

### 1. Data Collection

The system collects data from:

- **Sustainability Compliance Agent** - Code analysis results
- **Carbon Footprint Agent** - Pipeline energy and emissions
- **Resource Optimization Agent** - Job metrics and opportunities
- **Eco-Friendly Deployment Agent** - Deployment analysis
- **Dashboard Data Agent** - Aggregation and storage

### 2. Data Processing

Collected data is:

1. Aggregated into daily metrics
2. Rolled up into weekly summaries
3. Rolled up into monthly summaries
4. Stored in JSON files for dashboard

### 3. Dashboard Update

Dashboard automatically loads:

- `dashboards/data/daily-metrics.json` - Daily data
- `dashboards/data/weekly-metrics.json` - Weekly data
- `dashboards/data/monthly-metrics.json` - Monthly data
- `dashboards/data/summary.json` - Latest summary

## Running Data Collection

### Manual Collection

```bash
# Collect real data from agents
python collect_real_data.py
```

Output:
```
============================================================
  🌍 EcoGuard Real Data Collection System
============================================================

📊 Collecting Compliance Data...
  ✓ Found 4 compliance issues
    - High: 1
    - Medium: 2
    - Low: 1

🌍 Collecting Carbon Footprint Data...
  ✓ Pipeline Analysis Complete
    - Energy: 0.0425 kWh
    - Emissions: 0.0064 kg CO₂e
    - Jobs: 5

⚙️  Collecting Optimization Data...
  ✓ Optimization Analysis Complete
    - Jobs Analyzed: 3
    - Opportunities: 5
    - High Severity: 2

🚀 Collecting Deployment Data...
  ✓ Deployment Analysis Complete
    - Optimal Time: 2024-03-19T03:00:00
    - Savings: 33.3%
    - Alternative Regions: 3

📈 Generating Daily Metrics...
  ✓ Daily Metrics Generated
    - Date: 2024-03-19
    - Energy: 0.04 kWh
    - Emissions: 0.01 kg CO₂e

💾 Updating Dashboard Data...
  ✓ Updated dashboards/data/daily-metrics.json
  ✓ Updated dashboards/data/weekly-metrics.json
  ✓ Updated dashboards/data/monthly-metrics.json

📋 Updating Summary...
  ✓ Updated dashboards/data/summary.json

============================================================
  ✅ Real Data Collection Complete!
============================================================

  Dashboard data updated successfully!
  Open dashboards/src/index.html to view real metrics.
```

### Automated Collection (CI/CD)

Add to `.gitlab-ci.yml`:

```yaml
collect:real:data:
  stage: build
  script:
    - echo "Collecting real data from agents..."
    - python collect_real_data.py
  artifacts:
    paths:
      - dashboards/data/
    expire_in: 30 days
  only:
    - main
```

## Data Files

### daily-metrics.json

Daily metrics for each day:

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

Weekly aggregated metrics:

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

Monthly aggregated metrics:

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
    "energy_reduction_pct": 12.0
  }
]
```

### summary.json

Latest summary for dashboard header:

```json
{
  "timestamp": "2024-03-19T14:30:00Z",
  "latest_daily": { ... },
  "latest_weekly": { ... },
  "latest_monthly": { ... },
  "total_days_tracked": 38,
  "total_weeks_tracked": 5,
  "total_months_tracked": 2,
  "goals": [ ... ]
}
```

## Integration with Agents

### Real Pipeline Data

To use real pipeline data instead of sample data:

1. **Modify collect_real_data.py** to fetch actual metrics:

```python
def collect_carbon_data(self) -> Dict[str, Any]:
    """Collect real pipeline metrics."""
    # Fetch from Prometheus
    jobs = self.fetch_from_prometheus()
    
    # Analyze with agent
    analyzer = CarbonFootprintAnalyzer()
    return analyzer.analyze_pipeline(jobs)
```

2. **Connect to Prometheus** for real metrics
3. **Connect to GitLab API** for pipeline data
4. **Connect to Electricity Maps** for carbon intensity

## Scheduling

### Daily Collection

Add to `.gitlab-ci.yml`:

```yaml
schedule:collect:data:
  stage: build
  script:
    - python collect_real_data.py
  only:
    - schedules
  variables:
    SCHEDULE_TYPE: daily
```

Then create a scheduled pipeline:
1. Go to **CI/CD > Schedules**
2. Click **New schedule**
3. Set cron: `0 1 * * *` (Daily at 01:00 UTC)
4. Select branch: `main`

## Troubleshooting

### Data Not Updating

1. Check if `collect_real_data.py` runs without errors
2. Verify data files are created in `dashboards/data/`
3. Check file permissions
4. Review agent outputs

### Dashboard Not Showing Data

1. Verify data files exist
2. Check browser console for errors
3. Clear browser cache
4. Verify JSON format is correct

### Agent Errors

1. Run agents individually to test
2. Check agent logs
3. Verify sample data is valid
4. Review agent implementations

## Next Steps

1. **Run data collection**
   ```bash
   python collect_real_data.py
   ```

2. **View dashboard**
   ```bash
   open dashboards/src/index.html
   ```

3. **Verify data**
   - Check daily metrics tab
   - Verify charts display data
   - Check goals progress

4. **Schedule automated collection**
   - Add to CI/CD pipeline
   - Set up daily schedule
   - Monitor execution

## Support

For issues:
1. Check agent logs
2. Review data files
3. Test agents individually
4. Check documentation
