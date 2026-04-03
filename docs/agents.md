---
title: Agents
---

# Agents

EcoGuard uses five focused agents. Each one handles a specific sustainability job.

## Agent map

### Sustainability Compliance Agent

- Detects inefficient patterns in code and workflows
- Useful during merge request review
- References: [agents/sustainability_compliance.py](../agents/sustainability_compliance.py)

### Carbon Footprint Agent

- Estimates energy use and emissions from pipeline execution
- Uses job runtime and carbon intensity inputs
- References: [agents/carbon_footprint.py](../agents/carbon_footprint.py)

### Resource Optimization Agent

- Finds heavy jobs and likely bottlenecks
- Recommends caching, parallelism, and runtime reduction
- References: [agents/resource_optimization.py](../agents/resource_optimization.py)

### Eco-Friendly Deployment Agent

- Suggests lower-carbon deployment windows
- Compares timing against grid carbon intensity
- References: [agents/eco_friendly_deployment.py](../agents/eco_friendly_deployment.py)

### Dashboard Data Agent

- Aggregates metrics into dashboard-ready JSON
- Keeps daily, weekly, and summary views aligned
- References: [agents/dashboard_data.py](../agents/dashboard_data.py)
