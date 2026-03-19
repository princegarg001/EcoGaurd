# EcoGuard Flows

This directory contains YAML workflow definitions for GitLab Duo that orchestrate EcoGuard agents.

## Available Flows

### Automatic Flows (Triggered by Events)

1. **eco-check.yml** - Analyze code on MR
   - Trigger: Merge request opened/updated
   - Agent: Sustainability Compliance Agent
   - Communication: MR comments, issues for high-severity items
   - Timing: Immediate (on MR event)

2. **carbon-track.yml** - Calculate emissions on pipeline
   - Trigger: Pipeline success/failure
   - Agent: Carbon Footprint Agent
   - Communication: Pipeline comments, issues for high emissions
   - Timing: Immediate (on pipeline completion)

3. **eco-deploy.yml** - Optimize deployment timing
   - Trigger: Deployment initiated
   - Agent: Eco-Friendly Deployment Agent
   - Communication: Deployment comments, optimization issues
   - Timing: Immediate (on deployment event)

### Scheduled Flows (Triggered by Time)

4. **weekly-optimization.yml** - Weekly resource analysis
   - Trigger: Daily at 00:00 UTC
   - Agent: Resource Optimization Agent
   - Communication: Weekly report on Mondays, daily logs
   - Timing: Daily analysis, weekly detailed reports

5. **dashboard-update.yml** - Daily metrics aggregation
   - Trigger: Daily at 01:00 UTC
   - Agent: Dashboard Data Agent
   - Communication: Slack notifications, email reports, monthly/weekly issues
   - Timing: Daily updates, weekly summaries, monthly reports

### On-Demand Flows (Triggered by Manual Request)

6. **compliance-check.yml** - Manual compliance analysis
   - Trigger: Comment mention `@ecoguard-compliance`
   - Agent: Sustainability Compliance Agent
   - Communication: Comment reply with results
   - Timing: Immediate (on request)

7. **carbon-report.yml** - Manual carbon analysis
   - Trigger: Comment mention `@ecoguard-carbon`
   - Agent: Carbon Footprint Agent
   - Communication: Comment reply with detailed report
   - Timing: Immediate (on request)

8. **optimization-report.yml** - Manual optimization analysis
   - Trigger: Comment mention `@ecoguard-optimize`
   - Agent: Resource Optimization Agent
   - Communication: Comment reply with analysis
   - Timing: Immediate (on request)

## Communication Strategy

### Right Time, Right Channel

**Immediate Feedback (Real-time)**
- MR comments for code issues (eco-check)
- Pipeline comments for emissions (carbon-track)
- Deployment comments for timing optimization (eco-deploy)
- Comment replies for manual requests

**Daily Updates (01:00 UTC)**
- Dashboard data files updated
- Slack notifications to #sustainability
- Email reports to team

**Weekly Reports (Mondays)**
- Detailed optimization report issue
- High-priority optimization issues created
- Weekly summary email

**Monthly Reports (1st of month)**
- Comprehensive sustainability report
- Goal progress tracking
- Trend analysis

### Notification Channels

1. **GitLab Comments** - For immediate, contextual feedback
   - MR comments for code issues
   - Pipeline comments for emissions
   - Deployment comments for timing
   - Issue comments for reports

2. **GitLab Issues** - For tracking and action items
   - High-severity compliance issues
   - High-emissions alerts
   - Optimization opportunities
   - Goal progress alerts

3. **Slack** - For team awareness
   - Daily metrics summary
   - Weekly optimization highlights
   - Goal alerts
   - Deployment optimization tips

4. **Email** - For detailed reports
   - Daily sustainability report
   - Weekly optimization report
   - Monthly comprehensive report
   - Goal progress updates

## Flow Execution Order

```
Daily Schedule:
00:00 UTC - weekly-optimization.yml (daily analysis, weekly report on Monday)
01:00 UTC - dashboard-update.yml (aggregate metrics, update dashboard)

Event-Driven:
Immediate - eco-check.yml (on MR)
Immediate - carbon-track.yml (on pipeline)
Immediate - eco-deploy.yml (on deployment)
Immediate - compliance-check.yml (on @mention)
Immediate - carbon-report.yml (on @mention)
Immediate - optimization-report.yml (on @mention)
```

## Configuration

To enable flows in your GitLab project:

1. Go to **Automate > Triggers**
2. Create triggers for each flow:
   - Select the flow file
   - Configure trigger conditions
   - Set any required variables
3. Test with sample events

## Customization

To customize flow behavior:

1. Edit the YAML file
2. Modify trigger conditions, steps, or outputs
3. Commit and push changes
4. Flows update automatically

## Monitoring

To monitor flow execution:

1. Go to **Automate > Flow Runs**
2. View execution history and logs
3. Check for errors or failures
4. Review agent outputs and decisions

## Flow Details

### eco-check.yml
Analyzes code changes in merge requests for sustainability issues. Posts immediate feedback as MR comments and creates high-severity issues for tracking.

**Trigger:** MR opened/updated
**Agents:** Sustainability Compliance Agent
**Output:** MR comments, GitHub issues
**Timing:** Immediate

### carbon-track.yml
Calculates pipeline energy consumption and CO₂ emissions. Posts results as pipeline comments and creates issues for high-emission pipelines.

**Trigger:** Pipeline success/failure
**Agents:** Carbon Footprint Agent, Dashboard Data Agent
**Output:** Pipeline comments, GitHub issues
**Timing:** Immediate

### eco-deploy.yml
Optimizes deployment timing based on grid carbon intensity. Recommends optimal deployment times and alternative regions.

**Trigger:** Deployment initiated
**Agents:** Eco-Friendly Deployment Agent, Dashboard Data Agent
**Output:** Deployment comments, GitHub issues
**Timing:** Immediate

### weekly-optimization.yml
Analyzes historical metrics to identify resource optimization opportunities. Creates detailed reports on Mondays and high-priority issues throughout the week.

**Trigger:** Daily at 00:00 UTC
**Agents:** Resource Optimization Agent, Dashboard Data Agent
**Output:** GitHub issues, Slack notifications
**Timing:** Daily analysis, weekly detailed reports

### dashboard-update.yml
Aggregates daily metrics and updates the sustainability dashboard. Sends notifications and creates monthly/weekly summary reports.

**Trigger:** Daily at 01:00 UTC
**Agents:** Dashboard Data Agent
**Output:** JSON data files, GitHub issues, Slack/email notifications
**Timing:** Daily updates, weekly summaries, monthly reports

### compliance-check.yml
On-demand code compliance analysis triggered by @mention in comments.

**Trigger:** Comment mention `@ecoguard-compliance`
**Agents:** Sustainability Compliance Agent
**Output:** Comment reply
**Timing:** Immediate

### carbon-report.yml
On-demand carbon footprint analysis triggered by @mention in comments.

**Trigger:** Comment mention `@ecoguard-carbon`
**Agents:** Carbon Footprint Agent
**Output:** Comment reply
**Timing:** Immediate

### optimization-report.yml
On-demand resource optimization analysis triggered by @mention in comments.

**Trigger:** Comment mention `@ecoguard-optimize`
**Agents:** Resource Optimization Agent
**Output:** Comment reply
**Timing:** Immediate

## Next Steps

- Review individual flow files for detailed configuration
- Customize notification channels and templates
- Set up Slack/email integration
- Test flows with sample data
- Monitor and iterate based on feedback
