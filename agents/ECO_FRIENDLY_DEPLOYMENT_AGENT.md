# Eco-Friendly Deployment Agent

This directory contains the Eco-Friendly Deployment Agent implementation.

## Files

- `eco_friendly_deployment.py` - Core optimization engine
- `eco_friendly_deployment_gitlab.py` - GitLab API integration
- `test_eco_friendly_deployment.py` - Unit tests

## Features

### Deployment Analysis

**Carbon Intensity Data:**
- Real-time grid carbon intensity for 10+ regions
- 24-hour forecast with hourly granularity
- Confidence scores for forecast accuracy
- Region-specific patterns (renewable vs coal-heavy)

**Deployment Optimization:**
- Calculates deployment energy consumption
- Finds optimal deployment time (lowest carbon intensity)
- Estimates CO₂ emissions and savings
- Compares against current time deployment

**Regional Recommendations:**
- Identifies alternative regions with cleaner grids
- Calculates savings for each alternative
- Ranks by environmental impact
- Provides top 3 alternatives

### Smart Recommendations

**Auto-Scaling:**
- Enable auto-scaling to reduce idle resources
- Scale up before deployment if load is high
- Scale down after deployment if load is low
- Schedule during low-traffic hours if downtime required

**Resource Cleanup:**
- Remove old container images
- Clean up temporary files and build artifacts
- Terminate unused instances
- Archive old logs to cold storage

### Supported Regions

**North America:**
- US-CA (California) - 150 gCO₂/kWh
- US-TX (Texas) - 400 gCO₂/kWh
- US-NY (New York) - 200 gCO₂/kWh
- US-VA (Virginia) - 350 gCO₂/kWh

**Europe:**
- EU-DE (Germany) - 380 gCO₂/kWh
- EU-GB (UK) - 250 gCO₂/kWh
- EU-FR (France) - 50 gCO₂/kWh (Nuclear)
- EU-NO (Norway) - 20 gCO₂/kWh (Hydro)

**Asia Pacific:**
- APAC-SG (Singapore) - 450 gCO₂/kWh
- APAC-AU (Australia) - 600 gCO₂/kWh

## Usage

### Standalone Analysis

```python
from eco_friendly_deployment import (
    DeploymentConfig,
    DeploymentOptimizer,
    format_recommendation,
)

deployment = DeploymentConfig(
    deployment_id='deploy-123',
    target_region='US-CA',
    deployment_size_mb=500,
    estimated_duration_minutes=15,
    requires_downtime=False,
    auto_scaling_enabled=True,
    resource_requirements={'cpu_cores': 4, 'memory_gb': 8},
)

optimizer = DeploymentOptimizer()
recommendation = optimizer.analyze_deployment(deployment)
print(format_recommendation(recommendation))
```

### GitLab Integration

```python
from eco_friendly_deployment_gitlab import EcoFriendlyDeploymentAgent

agent = EcoFriendlyDeploymentAgent(project_id='80410036')
agent.analyze_deployment(deployment)
```

## Example Output

```
## 🌍 EcoGuard Eco-Friendly Deployment Recommendation

### Recommended Deployment Time

**Time:** 2024-03-19T03:00:00
**Region:** US-CA
**Carbon Intensity:** 120 gCO₂/kWh

### Environmental Impact

| Metric | Value |
|--------|-------|
| Estimated Emissions | 0.0012 kg CO₂e |
| Estimated Savings | 0.0004 kg CO₂e (33.3%) |
| Forecast Confidence | 95% |

### Reason

Deploying at 2024-03-19T03:00:00 will reduce emissions by 33.3% compared to now

### Alternative Regions

- **Europe - France** (EU-FR): 0.0010 kg CO₂e savings (83.3%)
- **Europe - Norway** (EU-NO): 0.0011 kg CO₂e savings (91.7%)

### Auto-Scaling Recommendations

- ✅ Enable auto-scaling to reduce idle resource consumption
- 💡 Current load is only 45%. Consider scaling down idle resources after deployment

### Resource Cleanup

- 🧹 Remove old container images and unused dependencies after deployment
- 📦 Clean up temporary files and build artifacts
- 🗑️ Terminate unused instances and scale down over-provisioned resources
- 💾 Archive old logs and database backups to cold storage
```

## Testing

```bash
python -m pytest test_eco_friendly_deployment.py -v
```

## Configuration

**Environment Variables:**
- `ELECTRICITY_MAPS_API_KEY` - Carbon intensity API key
- `CI_PROJECT_ID` - GitLab project ID
- `CI_DEPLOYMENT_ID` - Deployment ID
- `DEPLOYMENT_REGION` - Target deployment region
- `GITLAB_TOKEN` - GitLab API token

## Next Steps

- Integrate with Electricity Maps API for real-time data
- Add support for multi-region deployments
- Implement deployment scheduling automation
- Create dashboard integration
- Add cost optimization alongside carbon optimization
