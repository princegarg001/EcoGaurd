# EcoGuard API Requirements & Configuration

## Overview

EcoGuard integrates with multiple external APIs to collect real-time sustainability metrics. This guide covers all required and optional APIs.

---

## 🔑 Required APIs

### 1. **Electricity Maps API** (REQUIRED)

**Purpose:** Get real-time and forecast carbon intensity data for different regions

**Website:** https://www.electricitymap.org/

**Setup:**
1. Go to https://www.electricitymap.org/
2. Sign up for free account
3. Get API key from dashboard
4. Set environment variable:
   ```bash
   export ELECTRICITY_MAPS_API_KEY="your-api-key-here"
   ```

**Endpoints Used:**
- `GET /v3/carbon-intensity/latest` - Current carbon intensity
- `GET /v3/carbon-intensity/forecast` - 72-hour forecast

**Example Usage:**
```bash
curl -H "auth-token: YOUR_API_KEY" \
  "https://api.electricitymap.org/v3/carbon-intensity/latest?zone=US-CA"
```

**Response:**
```json
{
  "zone": "US-CA",
  "carbonIntensity": 150,
  "datetime": "2024-03-19T16:40:00Z",
  "updatedAt": "2024-03-19T16:35:00Z"
}
```

**Pricing:** Free tier available (100 requests/day)

---

### 2. **GitLab API** (REQUIRED)

**Purpose:** Access pipeline metrics, job data, and project information

**Setup:**
1. Go to https://gitlab.com/-/profile/personal_access_tokens
2. Create token with `api` scope
3. Set environment variable:
   ```bash
   export GITLAB_TOKEN="your-token-here"
   ```

**Endpoints Used:**
- `GET /api/v4/projects/{id}/pipelines` - List pipelines
- `GET /api/v4/projects/{id}/pipelines/{pipeline_id}/jobs` - Get job metrics
- `GET /api/v4/projects/{id}/deployments` - Get deployments
- `GET /api/v4/projects/{id}/issues` - Get compliance issues

**Example Usage:**
```bash
curl --header "PRIVATE-TOKEN: YOUR_TOKEN" \
  "https://gitlab.com/api/v4/projects/80410036/pipelines"
```

**Pricing:** Free (included with GitLab)

---

## 📊 Optional APIs

### 3. **Prometheus API** (OPTIONAL)

**Purpose:** Collect detailed metrics from GitLab Runners

**Setup:**
1. Deploy Prometheus instance
2. Configure GitLab Runner to expose metrics
3. Set environment variable:
   ```bash
   export PROMETHEUS_URL="http://prometheus:9090"
   ```

**Endpoints Used:**
- `GET /api/v1/query` - Query metrics
- `GET /api/v1/query_range` - Query metrics over time range

**Example Usage:**
```bash
curl "http://prometheus:9090/api/v1/query?query=up"
```

**Metrics Collected:**
- `gitlab_runner_job_duration_seconds` - Job duration
- `gitlab_runner_job_cpu_seconds_total` - CPU usage
- `gitlab_runner_job_memory_bytes` - Memory usage

**Pricing:** Free (open source)

---

### 4. **Google Cloud API** (OPTIONAL)

**Purpose:** Get carbon footprint data from Google Cloud infrastructure

**Setup:**
1. Create Google Cloud project
2. Enable BigQuery API
3. Set up OAuth2 credentials
4. Set environment variable:
   ```bash
   export GOOGLE_CLOUD_TOKEN="your-token-here"
   ```

**Endpoints Used:**
- `GET /bigquery/v2/projects/{project}/datasets/carbon_footprint` - Carbon data

**Pricing:** Free tier available (1TB/month)

---

## 🔧 Environment Variables

### Required
```bash
# Electricity Maps API
ELECTRICITY_MAPS_API_KEY=your-api-key

# GitLab API
GITLAB_TOKEN=your-personal-access-token
CI_PROJECT_ID=80410036

# Prometheus (if using)
PROMETHEUS_URL=http://prometheus:9090
```

### Optional
```bash
# Google Cloud
GOOGLE_CLOUD_TOKEN=your-oauth2-token

# Configuration
RUNNER_REGION=US-CA
DASHBOARD_DATA_DIR=dashboards/data
```

---

## ✅ Setup Checklist

### Minimum Setup (For MVP)
- [ ] Create Electricity Maps account
- [ ] Get Electricity Maps API key
- [ ] Create GitLab personal access token
- [ ] Set environment variables
- [ ] Test API connections

### Full Setup (For Production)
- [ ] Complete minimum setup
- [ ] Deploy Prometheus instance
- [ ] Configure GitLab Runner metrics
- [ ] Set up Google Cloud (optional)
- [ ] Configure Slack/email notifications
- [ ] Set up scheduled data collection

---

## 🧪 Testing API Connections

### Test Electricity Maps API
```bash
curl -H "auth-token: $ELECTRICITY_MAPS_API_KEY" \
  "https://api.electricitymap.org/v3/carbon-intensity/latest?zone=US-CA"
```

### Test GitLab API
```bash
curl --header "PRIVATE-TOKEN: $GITLAB_TOKEN" \
  "https://gitlab.com/api/v4/user"
```

### Test Prometheus API
```bash
curl "$PROMETHEUS_URL/api/v1/query?query=up"
```

---

## 🔄 Integration Points

### Carbon Footprint Agent
- Uses: Electricity Maps API, Prometheus
- Collects: Energy usage, carbon intensity, emissions

### Resource Optimization Agent
- Uses: Prometheus, GitLab API
- Collects: Job metrics, resource usage, performance data

### Eco-Friendly Deployment Agent
- Uses: Electricity Maps API
- Collects: Carbon intensity forecasts, optimal deployment times

### Dashboard Data Agent
- Uses: All APIs
- Aggregates: All metrics into dashboard data files

---

## 📈 Data Flow

```
External APIs
    |
    v
Agents (collect data)
    |
    v
Dashboard Data Agent (aggregate)
    |
    v
JSON Files (dashboards/data/)
    |
    v
Dashboard UI (display)
```

---

## 🔐 Security Best Practices

1. **Never commit API keys** to repository
2. **Use environment variables** for all secrets
3. **Rotate tokens regularly** (every 90 days)
4. **Use minimal scopes** for API tokens
5. **Monitor API usage** for unusual activity
6. **Use HTTPS** for all API calls

---

## 📞 Support

### Electricity Maps
- Website: https://www.electricitymap.org/
- Docs: https://api.electricitymap.org/
- Support: support@electricitymap.org

### GitLab API
- Docs: https://docs.gitlab.com/ee/api/
- Support: https://gitlab.com/support

### Prometheus
- Docs: https://prometheus.io/docs/
- Community: https://prometheus.io/community/

### Google Cloud
- Docs: https://cloud.google.com/docs
- Support: https://cloud.google.com/support

---

## 🚀 Next Steps

1. **Get Electricity Maps API key** (5 minutes)
2. **Create GitLab token** (2 minutes)
3. **Set environment variables** (2 minutes)
4. **Test connections** (5 minutes)
5. **Run data collection** (5 minutes)
6. **View dashboard** (2 minutes)

**Total: ~20 minutes to get started!**
