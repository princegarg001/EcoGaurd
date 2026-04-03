---
title: Testing
---

# Testing

Run tests before merging changes to agents, flows, or the dashboard.

## Local test commands

```bash
cd agents
python -m pytest test_*.py -v
```

## Specific test files

```bash
python -m pytest test_carbon_footprint.py -v
python -m pytest test_compliance.py -v
python -m pytest test_dashboard_data.py -v
python -m pytest test_eco_friendly_deployment.py -v
python -m pytest test_resource_optimization.py -v
```

## Recommended order

1. Run the full agent suite.
2. Run one focused test for the changed area.
3. Run flow validation if YAML changed.
4. Review pipeline logs for warnings.
