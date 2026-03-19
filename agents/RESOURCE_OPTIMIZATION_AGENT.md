# Resource Optimization Agent

This directory contains the Resource Optimization Agent implementation.

## Files

- `resource_optimization.py` - Core analysis engine
- `resource_optimization_gitlab.py` - GitLab API integration
- `test_resource_optimization.py` - Unit tests

## Features

### Analysis Capabilities

**Metrics Collection:**
- Job duration (min, max, average)
- CPU cores and utilization percentage
- Memory usage and utilization percentage
- Success/failure rates
- Historical trends over 7 days

**Outlier Detection:**
- High CPU usage (>2x average)
- High memory usage (>2x average)
- Long-running jobs (>2x average duration)
- Low success rates (<95%)
- Low CPU utilization (<50%)
- Low memory utilization (<60%)

**Impact Scoring:**
- Combines frequency and resource usage
- Prioritizes high-impact opportunities
- Estimates energy savings in kWh and percentage

### Optimization Opportunities

1. **High CPU Usage**
   - Review CPU allocation
   - Split into parallel subtasks
   - Enable caching
   - Profile for bottlenecks

2. **High Memory Usage**
   - Implement streaming/chunking
   - Use memory-efficient data structures
   - Enable garbage collection
   - Break into smaller jobs

3. **Long Duration**
   - Enable parallelization
   - Implement caching
   - Optimize algorithms
   - Use incremental builds

4. **Low Success Rate**
   - Investigate failures
   - Add error handling
   - Implement retry logic
   - Review resource allocation

5. **Low CPU Utilization**
   - Reduce allocated cores
   - Enable multi-threading
   - Profile for bottlenecks
   - Use async operations

6. **Low Memory Utilization**
   - Reduce allocated memory
   - Implement batch processing
   - Review allocation strategy
   - Profile usage patterns

## Usage

### Standalone Analysis

```python
from resource_optimization import (
    JobMetric,
    MetricsAnalyzer,
    ResourceOptimizationReport,
)

metrics = [
    JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 45, 1024, 50, 'success'),
    JobMetric('job-2', 'test', '2024-03-19T10:00Z', 600, 8, 25, 4096, 40, 'success'),
]

analyzer = MetricsAnalyzer()
analyzer.add_metrics(metrics)
job_stats, opportunities = analyzer.analyze()

report = ResourceOptimizationReport(job_stats, opportunities)
print(report.generate_detailed_report())
```

### GitLab Integration

```python
from resource_optimization_gitlab import ResourceOptimizationAgent

agent = ResourceOptimizationAgent(project_id='80410036')
agent.analyze_and_report(metrics)
```

## Example Output

```
## 📊 EcoGuard Resource Optimization Report

Analysis Period: Last 7 days

### Summary

- Jobs Analyzed: 3
- Optimization Opportunities: 5
  - 🔴 High Severity: 2
  - 🟡 Medium Severity: 2
  - 🟢 Low Severity: 1

### Energy Impact

| Metric | Value |
|--------|-------|
| Total Energy Used | 0.0425 kWh |
| Wasted Energy | 0.0042 kWh |
| Potential Savings | 0.0125 kWh (29.4%) |

### Top Optimization Opportunities

#### 1. 🔴 test - High CPU

Description: Job uses 8.0 CPU cores on average, 6.0 more than baseline

Recommendations:
- Review CPU allocation - may be over-provisioned
- Consider splitting into parallel subtasks
- Enable job caching to reduce re-computation
- Profile the job to identify CPU bottlenecks
- Use resource limits to prevent over-allocation

Estimated Savings: 0.0075 kWh (17.6%)
Impact Score: 85.0/100
```

## Testing

```bash
python -m pytest test_resource_optimization.py -v
```

## Configuration

**Environment Variables:**
- `PROMETHEUS_URL` - Prometheus instance URL
- `CI_PROJECT_ID` - GitLab project ID
- `GITLAB_TOKEN` - GitLab API token

## Next Steps

- Integrate with Prometheus for real metrics collection
- Add machine learning for anomaly detection
- Implement trend analysis and forecasting
- Create dashboard integration
- Add support for custom thresholds
