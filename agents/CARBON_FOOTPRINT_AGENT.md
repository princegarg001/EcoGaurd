# Carbon Footprint Agent

This directory contains the Carbon Footprint Agent implementation.

## Files

- `carbon_footprint.py` - Core analysis engine
- `carbon_footprint_gitlab.py` - GitLab API integration
- `test_carbon_footprint.py` - Unit tests

## Features

### Energy Calculation

**Methodology:**
- CPU energy: CPU-cores × 30W × duration-hours
- Memory energy: Memory-GB × 0.5W × duration-hours
- Total energy: (CPU energy + Memory energy) / 1000 = kWh

**Carbon Intensity:**
- Fetches real-time grid carbon intensity from Electricity Maps API
- Default values for common regions (US-CA, DE, GB, FR, etc.)
- Supports custom zones

**CO₂ Calculation:**
- CO₂ = kWh × carbon-intensity (gCO₂/kWh)
- Converts to kg CO₂e for reporting

### Analysis Features

1. **Pipeline Summary**
   - Total jobs, successful, failed
   - Total energy and emissions
   - Comparison to baseline

2. **Breakdown by Job**
   - Individual job energy and emissions
   - Identification of heaviest jobs
   - Per-job recommendations

3. **Recommendations**
   - Long-running jobs (>10 min)
   - High memory usage (>2GB)
   - High CPU usage (>4 cores)
   - Failed jobs (wasted energy)
   - Parallelization opportunities

4. **Carbon Intensity**
   - Region-specific grid data
   - 72-hour forecast support
   - Optimal deployment timing suggestions

## Usage

### Standalone Analysis

```python
from carbon_footprint import (
    JobMetrics,
    CarbonFootprintAnalyzer,
    format_report
)

jobs = [
    JobMetrics('job-1', 'build', 300, 2, 1024, 'success'),
    JobMetrics('job-2', 'test', 600, 4, 2048, 'success'),
]

analyzer = CarbonFootprintAnalyzer()
analysis = analyzer.analyze_pipeline(jobs, zone='US-CA')
print(format_report(analysis))
```

### GitLab Integration

```python
from carbon_footprint_gitlab import CarbonFootprintAgent

agent = CarbonFootprintAgent(project_id='80410036', zone='US-CA')
agent.analyze_pipeline(pipeline_id=123, jobs=jobs)
```

## Example Output

```
## 🌍 EcoGuard Carbon Footprint Report

Pipeline Summary
- Total Jobs: 3
- Successful: 3
- Failed: 0

⚡ Energy Consumption
| Metric | Value |
|--------|-------|
| Total Energy | 0.0425 kWh |
| CPU Energy | 0.0417 kWh |
| Memory Energy | 0.0008 kWh |
| Baseline | 5.0 kWh |
| Difference | -4.9575 kWh (-99.1%) |

🌱 CO₂ Emissions
| Metric | Value |
|--------|-------|
| Total Emissions | 0.0064 kg CO₂e |
| Baseline | 2.0 kg CO₂e |
| Difference | -1.9936 kg CO₂e (-99.7%) |

📊 Carbon Intensity
- Region: US-CA
- Intensity: 150 gCO₂/kWh

🔥 Heaviest Jobs
- job-2: 0.0208 kWh (0.0031 kg CO₂e)
- job-1: 0.0104 kWh (0.0016 kg CO₂e)
- job-3: 0.0042 kWh (0.0006 kg CO₂e)

💡 Recommendations
- ✅ Pipeline is running efficiently! Keep up the good work.
```

## Testing

```bash
python -m pytest test_carbon_footprint.py -v
```

## Configuration

**Environment Variables:**
- `ELECTRICITY_MAPS_API_KEY` - API key for carbon intensity data
- `PROMETHEUS_URL` - Prometheus instance URL
- `RUNNER_REGION` - Default region for carbon intensity (default: US-CA)
- `CI_PROJECT_ID` - GitLab project ID
- `CI_PIPELINE_ID` - GitLab pipeline ID

## Next Steps

- Integrate with Prometheus for real metrics collection
- Add support for cloud provider APIs (AWS, GCP, Azure)
- Implement caching for carbon intensity data
- Add historical trend analysis
- Create dashboard integration
