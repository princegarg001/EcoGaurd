# EcoGuard Agents

This directory contains agent implementations and supporting scripts.

## Agent Files

- `sustainability-compliance.py` - Code analysis for green patterns
- `carbon-footprint.py` - Energy and emissions calculation
- `resource-optimization.py` - Job performance analysis
- `eco-friendly-deployment.py` - Deployment optimization
- `dashboard-data.py` - Metrics aggregation

## Utilities

- `metrics_collector.py` - Prometheus metrics collection
- `carbon_calculator.py` - Energy to CO₂ conversion
- `api_client.py` - External API integration

## Development

Each agent is implemented as a Python module that:

1. Receives input from GitLab Duo platform
2. Processes data using available tools
3. Generates output (comments, issues, data)
4. Logs execution for debugging

See `.gitlab/duo/AGENTS.md` for agent specifications.
