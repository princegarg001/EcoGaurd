# EcoGuard Phase 2: Testing & Validation Guide

## Complete Step-by-Step Testing Instructions

### Prerequisites

Before starting, ensure you have:
- Python 3.9+ installed
- Git installed and configured
- A modern web browser (Chrome, Firefox, Safari)
- Terminal/Command prompt access
- Project cloned locally

---

## STEP 1: Run Real Data Collection (15 minutes)

### 1.1 Navigate to Project Directory

```bash
# Open terminal/command prompt
cd /path/to/EcoGuard

# Verify you're in the right directory
pwd  # macOS/Linux
cd   # Windows
```

**Expected Output:**
```
/path/to/EcoGuard
```

### 1.2 Install Dependencies (if not already installed)

```bash
# Install Python dependencies
pip install -r requirements.txt

# Verify installation
pip list | grep pytest
```

**Expected Output:**
```
pytest (7.x.x)
pytest-cov (4.x.x)
```

### 1.3 Run Data Collection Script

```bash
# Run the real data collection
python collect_real_data.py
```

**Expected Output:**
```
============================================================
  🌍 EcoGuard Real Data Collection System
============================================================

📊 Collecting Compliance Data...
  ✓ Found 4 compliance issues
    - High: 1
    - Medium: 2
    - Low: 1

🌍 Collecting Carbon Footprint Data...
  ✓ Pipeline Analysis Complete
    - Energy: 0.0425 kWh
    - Emissions: 0.0064 kg CO₂e
    - Jobs: 5

⚙️  Collecting Optimization Data...
  ✓ Optimization Analysis Complete
    - Jobs Analyzed: 3
    - Opportunities: 5
    - High Severity: 2

🚀 Collecting Deployment Data...
  ✓ Deployment Analysis Complete
    - Optimal Time: 2024-03-19T03:00:00
    - Savings: 33.3%
    - Alternative Regions: 3

📈 Generating Daily Metrics...
  ✓ Daily Metrics Generated
    - Date: 2024-03-19
    - Energy: 0.04 kWh
    - Emissions: 0.01 kg CO₂e

💾 Updating Dashboard Data...
  ✓ Updated dashboards/data/daily-metrics.json
  ✓ Updated dashboards/data/weekly-metrics.json
  ✓ Updated dashboards/data/monthly-metrics.json

📋 Updating Summary...
  ✓ Updated dashboards/data/summary.json

============================================================
  ✅ Real Data Collection Complete!
============================================================

  Dashboard data updated successfully!
  Open dashboards/src/index.html to view real metrics.
```

### 1.4 Verify Data Files Were Created

```bash
# Check if data files exist
ls -la dashboards/data/

# Verify file sizes (should not be empty)
wc -l dashboards/data/*.json
```

**Expected Output:**
```
daily-metrics.json          (50+ lines)
weekly-metrics.json         (30+ lines)
monthly-metrics.json        (30+ lines)
sustainability-goals.json   (50+ lines)
summary.json                (40+ lines)
```

### 1.5 Verify Data Content

```bash
# View latest daily metrics
cat dashboards/data/daily-metrics.json | tail -20

# View summary
cat dashboards/data/summary.json
```

**Expected Output:**
```json
{
  "date": "2024-03-19",
  "total_energy_kwh": 45.2,
  "total_emissions_kg_co2": 18.5,
  "builds_count": 12,
  "deployments_count": 2,
  ...
}
```

✅ **Step 1 Complete:** Real data has been collected and dashboard files updated.

---

## STEP 2: Test Dashboard with Real Data (20 minutes)

### 2.1 Open Dashboard in Browser

```bash
# macOS
open dashboards/src/index.html

# Linux
firefox dashboards/src/index.html

# Windows
start dashboards/src/index.html
```

**Expected Result:**
Dashboard opens in your default browser showing the EcoGuard interface.

### 2.2 Verify Header Section

**Check these elements:**
- [ ] Green gradient header visible
- [ ] "🌍 EcoGuard Dashboard" title displayed
- [ ] Subtitle: "Real-time Sustainability Metrics & Carbon Footprint Tracking"
- [ ] 4 stat cards visible:
  - [ ] Total CO₂ Emissions (should show a number like "18.5 kg")
  - [ ] Total Energy Used (should show a number like "45.2 kWh")
  - [ ] SCI Score (should show a number like "1.39")
  - [ ] Builds This Month (should show a number like "12")

**Screenshot Check:**
Take a screenshot of the header. It should look professional with:
- Green color scheme
- Clear typography
- Proper spacing

### 2.3 Test Overview Tab

**Click on "📊 Overview" tab**

**Verify these charts load:**
- [ ] Daily Emissions Trend (line chart with data points)
- [ ] Energy Consumption (bar chart with bars)
- [ ] Emissions by Source (doughnut chart with colored segments)
- [ ] Carbon Intensity by Region (horizontal bar chart)

**Check chart details:**
```
For each chart:
- [ ] Title is visible
- [ ] Data is displayed (not empty)
- [ ] Legend is shown
- [ ] Axes are labeled
- [ ] Colors are appropriate
```

### 2.4 Test Metrics Tab

**Click on "📈 Metrics" tab**

**Verify metric cards:**
- [ ] Daily Average card shows CO₂ value
- [ ] Weekly Total card shows CO₂ value
- [ ] Monthly Total card shows CO₂ value
- [ ] CO₂ per Build card shows SCI score

**Verify trend indicators:**
- [ ] Each card shows trend (↓ or ↑)
- [ ] Percentage change is displayed
- [ ] Color coding is correct (green for positive, red for negative)

**Verify comparison charts:**
- [ ] Weekly Comparison chart displays data
- [ ] Monthly Trend chart displays data
- [ ] Both charts have proper legends

### 2.5 Test Goals Tab

**Click on "🎯 Goals" tab**

**Verify goal items:**
- [ ] "Reduce CO₂ emissions by 20%" goal visible
- [ ] "Reduce energy consumption by 15%" goal visible
- [ ] "Resolve 80% of compliance issues" goal visible
- [ ] "Reduce SCI score to 0.5 kg CO₂/build" goal visible

**Verify goal details:**
For each goal:
- [ ] Goal name is displayed
- [ ] Status badge shows ("on_track", "at_risk", or "achieved")
- [ ] Progress bar is visible and filled
- [ ] Progress percentage is shown
- [ ] Deadline date is displayed

**Check progress bar colors:**
- [ ] Progress bars are green (indicating on-track)
- [ ] Status badges have appropriate colors

### 2.6 Test Issues Tab

**Click on "⚠️ Issues" tab**

**Verify high priority issues:**
- [ ] "High Pipeline Emissions" issue visible
- [ ] "Inefficient Loop Detected" issue visible
- [ ] Each issue shows severity badge (RED for HIGH)
- [ ] Estimated savings are displayed

**Verify recent issues:**
- [ ] "Unused Variable" issue visible
- [ ] "String Concatenation in Loop" issue visible
- [ ] Severity levels are correct
- [ ] Savings estimates are shown

### 2.7 Test Recommendations Tab

**Click on "💡 Recommendations" tab**

**Verify recommendations:**
- [ ] "Optimize Test Suite" recommendation visible
- [ ] "Enable Caching" recommendation visible
- [ ] "Deploy During Low-Carbon Hours" recommendation visible
- [ ] Each recommendation shows estimated savings

**Check recommendation styling:**
- [ ] Left border is green
- [ ] Title is bold
- [ ] Description is clear
- [ ] Savings are highlighted

### 2.8 Test Responsive Design

**Resize browser window:**

```
1. Full width (1920px)
   - [ ] All elements visible
   - [ ] Charts display properly
   - [ ] No horizontal scrolling

2. Tablet width (768px)
   - [ ] Layout adjusts
   - [ ] Single column for cards
   - [ ] Charts still readable

3. Mobile width (375px)
   - [ ] Fully responsive
   - [ ] Touch-friendly buttons
   - [ ] No overflow
   - [ ] Text is readable
```

### 2.9 Test Tab Navigation

**Click through all tabs:**

```
1. Click "📊 Overview"
   - [ ] Charts load
   - [ ] No errors in console

2. Click "📈 Metrics"
   - [ ] Cards display
   - [ ] Charts resize properly

3. Click "🎯 Goals"
   - [ ] Goals load
   - [ ] Progress bars animate

4. Click "⚠️ Issues"
   - [ ] Issues display
   - [ ] Severity colors correct

5. Click "💡 Recommendations"
   - [ ] Recommendations load
   - [ ] Styling is correct
```

### 2.10 Check Browser Console

**Open Developer Tools:**
```
Chrome/Firefox: Press F12 or Cmd+Option+I (Mac)
Safari: Cmd+Option+I
```

**Check Console tab:**
- [ ] No red error messages
- [ ] No warnings about missing files
- [ ] Data loading messages are present

**Check Network tab:**
- [ ] All JSON files load successfully (200 status)
- [ ] No 404 errors
- [ ] Load time is < 2 seconds

✅ **Step 2 Complete:** Dashboard displays real data correctly.

---

## STEP 3: Run CI/CD Pipeline (30 minutes)

### 3.1 Commit and Push Changes

```bash
# Check git status
git status

# Add all changes
git add .

# Commit changes
git commit -m "Phase 2: Real data collection and testing"

# Push to remote
git push origin duo-edit-20260319-144302
```

**Expected Output:**
```
Enumerating objects: 15, done.
Counting objects: 100% (15/15), done.
Delta compression using up to 8 threads
Compressing objects: 100% (10/10), done.
Writing objects: 100% (10/10), 5.23 KiB | 5.23 MiB/s, done.
Total 10 (delta 5), reused 0 (delta 0), reused pack 0
remote: Resolving deltas: 100% (5/5), done.
remote: 
remote: To create a merge request for duo-edit-20260319-144302, visit:
remote:   https://gitlab.com/princegarg001-group/EcoGuard/-/merge_requests/new?merge_request%5Bsource_branch%5D=duo-edit-20260319-144302
```

### 3.2 Monitor Pipeline Execution

**Go to GitLab project:**
```
https://gitlab.com/princegarg001-group/EcoGuard
```

**Navigate to CI/CD > Pipelines:**
- [ ] New pipeline appears at top
- [ ] Pipeline status shows "running" (blue spinner)

### 3.3 Wait for Test Stage

**Monitor test jobs:**

```
Expected jobs to run:
- test:agents:compliance
- test:agents:carbon
- test:agents:optimization
- test:agents:deployment
- test:agents:dashboard
- test:agents:all
- test:code:quality
- test:flows:validation
- test:documentation
```

**For each job:**
- [ ] Click on job name
- [ ] Watch logs scroll
- [ ] Look for "✓" checkmarks
- [ ] Verify no red error messages

**Expected test output:**
```
test:agents:compliance
  ✓ test_add_daily_metrics
  ✓ test_aggregate_weekly
  ✓ test_aggregate_monthly
  ✓ test_sci_score_calculation
  ✓ test_goal_tracking
  ✓ test_goal_progress_update
  ✓ test_goal_status_on_track
  ✓ test_goal_status_at_risk
  ✓ test_emissions_per_build_calculation

9 passed in 2.34s
```

### 3.4 Wait for Build Stage

**Monitor build jobs:**

```
Expected jobs:
- build:dashboard
- build:agents:package
- build:flows:package
- build:docs:package
- build:complete
```

**For each job:**
- [ ] Job completes successfully
- [ ] No errors in logs
- [ ] Artifacts are created

### 3.5 Wait for Deploy Stage

**Monitor deploy jobs:**

```
Expected jobs:
- pages
- deploy:documentation
- success:summary
```

**For pages job:**
- [ ] Job completes
- [ ] Look for deployment URL in logs
- [ ] Should show: "https://princegarg001.gitlab.io/EcoGuard"

### 3.6 Verify Pipeline Success

**Check pipeline status:**
- [ ] All jobs show green checkmarks
- [ ] Pipeline status shows "passed"
- [ ] No failed jobs

**View pipeline summary:**
```
Expected output:
============================================================
  🌍 EcoGuard CI/CD Pipeline - SUCCESS
============================================================

✓ All Tests Passed
  - Sustainability Compliance Agent
  - Carbon Footprint Agent
  - Resource Optimization Agent
  - Eco-Friendly Deployment Agent
  - Dashboard Data Agent

✓ Build Complete
  - Dashboard built and ready
  - Agents packaged
  - Flows validated
  - Documentation prepared

✓ Deployment Complete
  - Dashboard: https://princegarg001.gitlab.io/EcoGuard
  - Documentation: https://princegarg001.gitlab.io/EcoGuard/docs
```

### 3.7 Access Deployed Dashboard

**Visit GitLab Pages URL:**
```
https://princegarg001.gitlab.io/EcoGuard
```

**Verify:**
- [ ] Dashboard loads from GitLab Pages
- [ ] Real data is displayed
- [ ] All charts are visible
- [ ] No console errors

✅ **Step 3 Complete:** CI/CD pipeline executed successfully.

---

## STEP 4: Verify All Components (25 minutes)

### 4.1 Test Each Agent Individually

**Test Compliance Agent:**

```bash
cd agents
python -c "from sustainability_compliance import analyze_code; result = analyze_code('for i in range(100):\n    x = 5 * 10'); print(f'Issues found: {result[\"total_issues\"]}')"
```

**Expected Output:**
```
Issues found: 2
```

**Test Carbon Footprint Agent:**

```bash
python -c "from carbon_footprint import CarbonFootprintAnalyzer, JobMetrics; jobs = [JobMetrics('j1', 'build', 300, 2, 1024, 'success')]; analyzer = CarbonFootprintAnalyzer(); result = analyzer.analyze_pipeline(jobs); print(f'Energy: {result[\"energy\"][\"total_kwh\"]:.4f} kWh')"
```

**Expected Output:**
```
Energy: 0.0104 kWh
```

**Test Resource Optimization Agent:**

```bash
python -c "from resource_optimization import MetricsAnalyzer, JobMetric; metrics = [JobMetric('j1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success')]; analyzer = MetricsAnalyzer(); analyzer.add_metrics(metrics); stats, opps = analyzer.analyze(); print(f'Jobs analyzed: {len(stats)}')"
```

**Expected Output:**
```
Jobs analyzed: 1
```

**Test Deployment Agent:**

```bash
python -c "from eco_friendly_deployment import DeploymentOptimizer, DeploymentConfig; config = DeploymentConfig('d1', 'US-CA', 500, 15, False, True, {'cpu_cores': 4, 'memory_gb': 8}); optimizer = DeploymentOptimizer(); rec = optimizer.analyze_deployment(config); print(f'Savings: {rec.savings_percentage:.1f}%')"
```

**Expected Output:**
```
Savings: 33.3%
```

**Test Dashboard Agent:**

```bash
python -c "from dashboard_data import DashboardDataAgent, DailyMetrics; agent = DashboardDataAgent(); daily = DailyMetrics('2024-03-19', 45.2, 18.5, 12, 2, 3, 2, 250, 5, 1, 2.5); agent.process_daily_metrics(daily); print('Daily metrics processed')"
```

**Expected Output:**
```
Daily metrics processed
```

### 4.2 Validate Flow YAML Files

```bash
# Install yamllint if not already installed
pip install yamllint

# Validate all flow files
cd ..
yamllint -d relaxed flows/*.yml
```

**Expected Output:**
```
flows/eco-check.yml
flows/carbon-track.yml
flows/eco-deploy.yml
flows/weekly-optimization.yml
flows/dashboard-update.yml
flows/compliance-check.yml
flows/carbon-report.yml
flows/optimization-report.yml

✓ All flow files are valid YAML
```

### 4.3 Check Documentation Completeness

```bash
# Check if all required files exist
test -f README.md && echo "✓ README.md exists"
test -f INSTALLATION.md && echo "✓ INSTALLATION.md exists"
test -f QUICKSTART.md && echo "✓ QUICKSTART.md exists"
test -f .gitlab-ci.yml && echo "✓ .gitlab-ci.yml exists"
test -f requirements.txt && echo "✓ requirements.txt exists"
test -f docs/CI_CD.md && echo "✓ docs/CI_CD.md exists"
test -f docs/REAL_DATA.md && echo "✓ docs/REAL_DATA.md exists"
test -f LICENSE && echo "✓ LICENSE exists"
test -f CONTRIBUTING.md && echo "✓ CONTRIBUTING.md exists"
```

**Expected Output:**
```
✓ README.md exists
✓ INSTALLATION.md exists
✓ QUICKSTART.md exists
✓ .gitlab-ci.yml exists
✓ requirements.txt exists
✓ docs/CI_CD.md exists
✓ docs/REAL_DATA.md exists
✓ LICENSE exists
✓ CONTRIBUTING.md exists
```

### 4.4 Verify API Integrations

**Check environment variables:**

```bash
# Create .env file for testing
cat > .env << EOF
ELECTRICITY_MAPS_API_KEY=test_key
GITLAB_TOKEN=test_token
CI_PROJECT_ID=80410036
PROMETHEUS_URL=http://prometheus:9090
RUNNER_REGION=US-CA
EOF

# Verify .env file
cat .env
```

**Expected Output:**
```
ELECTRICITY_MAPS_API_KEY=test_key
GITLAB_TOKEN=test_token
CI_PROJECT_ID=80410036
PROMETHEUS_URL=http://prometheus:9090
RUNNER_REGION=US-CA
```

### 4.5 Run Full Test Suite

```bash
cd agents
python -m pytest test_*.py -v --tb=short
```

**Expected Output:**
```
test_compliance.py::TestMetricsAggregator::test_add_daily_metrics PASSED
test_compliance.py::TestMetricsAggregator::test_aggregate_weekly PASSED
test_compliance.py::TestMetricsAggregator::test_aggregate_monthly PASSED
...
test_dashboard_data.py::TestResourceOptimizationReport::test_report_contains_recommendations PASSED

======================== 45 passed in 12.34s ========================
```

✅ **Step 4 Complete:** All components verified successfully.

---

## FINAL VERIFICATION CHECKLIST

### Data Collection ✅
- [ ] `python collect_real_data.py` runs without errors
- [ ] All 5 agents execute successfully
- [ ] Data files are created in `dashboards/data/`
- [ ] JSON files contain valid data

### Dashboard Testing ✅
- [ ] Dashboard opens in browser
- [ ] All 5 tabs load correctly
- [ ] Charts display real data
- [ ] Goals show progress
- [ ] Issues display with severity
- [ ] Recommendations show savings
- [ ] Responsive design works
- [ ] No console errors

### CI/CD Pipeline ✅
- [ ] All test jobs pass
- [ ] All build jobs complete
- [ ] Deployment succeeds
- [ ] GitLab Pages accessible
- [ ] Dashboard loads from Pages URL

### Component Verification ✅
- [ ] All 5 agents work individually
- [ ] All 8 flow files are valid YAML
- [ ] All documentation files exist
- [ ] Full test suite passes (45+ tests)
- [ ] Environment variables configured

---

## 🎉 Phase 2 Complete!

If all checks pass, you have successfully:
1. ✅ Collected real data from all agents
2. ✅ Tested dashboard with real metrics
3. ✅ Executed CI/CD pipeline successfully
4. ✅ Verified all components

**Next Phase:** Demo & Submission (Phase 3)

---

## Troubleshooting

### If data collection fails:
```bash
# Check Python version
python --version  # Should be 3.9+

# Check dependencies
pip list | grep -E "pytest|requests"

# Run with verbose output
python collect_real_data.py -v
```

### If dashboard doesn't load:
```bash
# Check file exists
ls -la dashboards/src/index.html

# Check data files
ls -la dashboards/data/

# Open browser console (F12) and check for errors
```

### If pipeline fails:
```bash
# Check git status
git status

# View pipeline logs
# Go to: https://gitlab.com/princegarg001-group/EcoGuard/-/pipelines

# Check specific job logs
# Click on failed job to see detailed logs
```

### If tests fail:
```bash
# Run tests with verbose output
cd agents
python -m pytest test_*.py -vv

# Run specific test
python -m pytest test_compliance.py::TestMetricsAggregator::test_add_daily_metrics -v
```

---

## Support

For issues:
1. Check the troubleshooting section above
2. Review agent logs
3. Check browser console (F12)
4. Review pipeline logs on GitLab
5. Check documentation in `docs/` folder
