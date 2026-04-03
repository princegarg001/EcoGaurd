---
title: Real Data Collection
---

# Real Data Collection

EcoGuard can run against live GitLab and carbon-intensity data instead of static examples.

## Collection pipeline

1. Read the current GitLab project and pipeline history.
2. Pull current carbon intensity from Electricity Maps.
3. Estimate energy usage from job duration and stage profile.
4. Compute emissions and summary scores.
5. Write dashboard JSON files.

## Main entry point

- [collect_real_data.py](../collect_real_data.py)

## Output locations

- [dashboards/data](../dashboards/data)
- [public/api](../public/api) when deployed through Pages

## Refresh expectations

- Scheduled jobs update the data automatically.
- Manual runs are useful for testing changes locally.
- The dashboard should always read the newest JSON files.
