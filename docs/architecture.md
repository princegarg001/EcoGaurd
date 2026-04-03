---
title: Architecture
---

# Architecture

EcoGuard is built as a pipeline of data collection, analysis, storage, and presentation.

## System layers

1. External data sources
   - GitLab API for pipeline and job metadata
   - Electricity Maps for live carbon intensity
2. Processing layer
   - `collect_real_data.py`
   - agent modules in [agents](../agents)
3. Storage and serving
   - JSON metrics in [dashboards/data](../dashboards/data)
   - Flask API in [api_server.py](../api_server.py)
4. Presentation layer
   - static dashboard files in [public](../public)
5. Automation layer
   - GitHub Actions and GitLab CI/CD workflows

## Main data flow

1. A commit, merge request, or scheduled job starts the pipeline.
2. The collector fetches GitLab job data and external carbon intensity data.
3. The agents convert runtime into energy and CO₂ estimates.
4. The dashboard data agent writes JSON summaries.
5. The backend or static site reads those JSON files.
6. The dashboard displays trends, recommendations, and goals.

## Important files

- [collect_real_data.py](../collect_real_data.py)
- [api_server.py](../api_server.py)
- [agents/carbon_footprint.py](../agents/carbon_footprint.py)
- [agents/resource_optimization.py](../agents/resource_optimization.py)
- [agents/eco_friendly_deployment.py](../agents/eco_friendly_deployment.py)
- [agents/dashboard_data.py](../agents/dashboard_data.py)
