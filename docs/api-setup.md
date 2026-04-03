---
title: API Setup
---

# API Setup

EcoGuard depends on external APIs for carbon and pipeline data.

## Required APIs

### Electricity Maps

- Required for live carbon intensity
- Add `ELECTRICITY_MAPS_API_KEY`
- Test with the latest carbon intensity endpoint

### GitLab API

- Required for pipelines, jobs, and project metadata
- Add `GITLAB_TOKEN`
- Set `CI_PROJECT_ID`

## Optional APIs

- Prometheus for runner metrics
- Google Cloud for cloud carbon data

## Environment variables

```bash
ELECTRICITY_MAPS_API_KEY=your-api-key
GITLAB_TOKEN=your-personal-access-token
CI_PROJECT_ID=80410036
PROMETHEUS_URL=http://prometheus:9090
GOOGLE_CLOUD_TOKEN=your-oauth2-token
RUNNER_REGION=US-CA
```

## Verification commands

```bash
curl --header "PRIVATE-TOKEN: %GITLAB_TOKEN%" "https://gitlab.com/api/v4/user"
curl -H "auth-token: %ELECTRICITY_MAPS_API_KEY%" "https://api.electricitymap.org/v3/carbon-intensity/latest?zone=US-CA"
```
