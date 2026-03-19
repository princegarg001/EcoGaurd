# EcoGuard CI/CD Pipeline Documentation

## Overview

The EcoGuard CI/CD pipeline automates testing, building, and deployment of all components:

- **5 Agents** - Sustainability analysis tools
- **8 Workflows** - Automated processes
- **Dashboard** - Web interface
- **Documentation** - Setup and usage guides

## Pipeline Stages

### 1. Test Stage

Runs comprehensive tests for all agents:

```
test:agents:compliance      → Sustainability Compliance Agent tests
test:agents:carbon          → Carbon Footprint Agent tests
test:agents:optimization    → Resource Optimization Agent tests
test:agents:deployment      → Eco-Friendly Deployment Agent tests
test:agents:dashboard       → Dashboard Data Agent tests
test:agents:all             → All tests with coverage report
test:code:quality           → Code quality checks (flake8, pylint)
test:flows:validation       → YAML flow validation
test:documentation          → Documentation completeness check
```

**Duration:** ~5-10 minutes

### 2. Build Stage

Packages all components:

```
build:dashboard:package     → Dashboard HTML/JS/CSS
build:agents:package        → Agent Python modules
build:flows:package         → Flow YAML definitions
build:docs:package          → Documentation files
build:complete              → Build completion summary
```

**Duration:** ~2-3 minutes

### 3. Deploy Stage

Deploys to production:

```
pages                       → Deploy dashboard to GitLab Pages
deploy:documentation       → Deploy docs to GitLab Pages
success:summary             → Success notification
failure:summary             → Failure notification
```

**Duration:** ~2-3 minutes

## Total Pipeline Time

**~10-15 minutes** from commit to production

## Artifacts

Each stage produces artifacts:

- **Test Stage**
  - JUnit test reports
  - Coverage reports (HTML)
  - Test results

- **Build Stage**
  - Packaged agents
  - Packaged flows
  - Packaged documentation

- **Deploy Stage**
  - Dashboard (GitLab Pages)
  - Documentation (GitLab Pages)
  - Public artifacts

## Environment Variables

Required for pipeline execution:

```yaml
ELECTRICITY_MAPS_API_KEY    # Electricity Maps API key
GOOGLE_CLOUD_TOKEN          # Google Cloud credentials
GITLAB_TOKEN                # GitLab personal access token
PROMETHEUS_URL              # Prometheus instance URL
CI_PROJECT_ID               # GitLab project ID
RUNNER_REGION               # Default region (e.g., US-CA)
DASHBOARD_DATA_DIR          # Dashboard data directory
```

## Running Locally

### Run All Tests

```bash
cd agents
python -m pytest test_*.py -v
```

### Run Specific Test

```bash
cd agents
python -m pytest test_compliance.py -v
```

### Run with Coverage

```bash
cd agents
python -m pytest test_*.py --cov=. --cov-report=html
open htmlcov/index.html
```

### Validate Flows

```bash
yamllint -d relaxed flows/*.yml
```

### Build Dashboard

```bash
cd dashboards
npm install
npm run build
```

## Troubleshooting

### Test Failures

1. Check test output for specific errors
2. Review agent implementation
3. Verify test data is correct
4. Run tests locally to reproduce

### Build Failures

1. Check artifact paths
2. Verify file permissions
3. Review build script output
4. Check disk space

### Deploy Failures

1. Check GitLab Pages settings
2. Verify artifacts are created
3. Review deployment logs
4. Check environment variables

## Monitoring

### Pipeline Status

1. Go to **CI/CD > Pipelines**
2. View pipeline status
3. Click on failed jobs for details

### Test Coverage

1. View coverage reports in artifacts
2. Track coverage trends
3. Set coverage thresholds

### Deployment Status

1. Check GitLab Pages deployment
2. Verify dashboard is accessible
3. Monitor page load times

## Best Practices

1. **Run tests locally before pushing**
   ```bash
   cd agents && python -m pytest test_*.py -v
   ```

2. **Validate YAML before committing**
   ```bash
   yamllint -d relaxed flows/*.yml
   ```

3. **Check documentation completeness**
   - Ensure all files exist
   - Verify links are correct
   - Update version numbers

4. **Monitor pipeline performance**
   - Track pipeline duration
   - Identify slow jobs
   - Optimize as needed

## Next Steps

1. **Enable CI/CD**
   - Push `.gitlab-ci.yml` to repository
   - Verify pipeline runs
   - Check all stages pass

2. **Configure Notifications**
   - Set up Slack integration
   - Configure email alerts
   - Add status badges

3. **Monitor Deployments**
   - Check dashboard accessibility
   - Verify data loading
   - Test all features

4. **Optimize Pipeline**
   - Reduce test duration
   - Parallelize jobs
   - Cache dependencies

## Support

For pipeline issues:
1. Check [CI/CD documentation](https://docs.gitlab.com/ee/ci/)
2. Review pipeline logs
3. Open an issue on GitLab
4. Contact the team
