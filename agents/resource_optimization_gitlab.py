"""GitLab integration for Resource Optimization Agent.

Handles interaction with GitLab API for reporting and issue creation.
"""

import os
import json
from typing import List, Dict, Any, Optional
from resource_optimization import (
    MetricsAnalyzer,
    JobMetric,
    ResourceOptimizationReport,
)


class PrometheusMetricsCollector:
    """Collects historical metrics from Prometheus."""

    def __init__(self, prometheus_url: Optional[str] = None):
        self.prometheus_url = prometheus_url or os.getenv(
            'PROMETHEUS_URL',
            'http://prometheus:9090'
        )

    def get_job_metrics_last_7_days(self) -> List[JobMetric]:
        """Get job metrics for the last 7 days from Prometheus.
        
        In production, would query Prometheus with PromQL:
        - gitlab_runner_job_duration_seconds
        - gitlab_runner_job_cpu_seconds_total
        - gitlab_runner_job_memory_bytes
        - gitlab_runner_job_status
        """
        # Mock implementation for MVP
        # In production, would use requests to query Prometheus
        return []

    def get_job_metrics_by_name(self, job_name: str, days: int = 7) -> List[JobMetric]:
        """Get metrics for a specific job over the last N days."""
        # Mock implementation for MVP
        return []


class GitLabIssueAPI:
    """Handles GitLab API interactions for issue creation."""

    def __init__(self, project_id: str, token: Optional[str] = None):
        self.project_id = project_id
        self.token = token or os.getenv('GITLAB_TOKEN')
        self.api_url = os.getenv('CI_API_V4_URL', 'https://gitlab.com/api/v4')

    def create_issue(self, title: str, description: str, labels: List[str]) -> bool:
        """Create a new issue in the project.
        
        In production, would call:
        POST /projects/{id}/issues
        """
        print(f"[Issue] {title}")
        print(f"Description: {description}")
        print(f"Labels: {labels}")
        return True

    def create_merge_request(self, title: str, description: str, 
                            source_branch: str, target_branch: str) -> bool:
        """Create a merge request with optimization suggestions.
        
        In production, would call:
        POST /projects/{id}/merge_requests
        """
        print(f"[MR] {title}")
        print(f"Source: {source_branch} -> Target: {target_branch}")
        print(f"Description: {description}")
        return True


class ResourceOptimizationAgent:
    """Main agent for resource optimization analysis."""

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.gitlab_api = GitLabIssueAPI(project_id)
        self.metrics_collector = PrometheusMetricsCollector()

    def analyze_and_report(self, metrics: List[JobMetric]) -> None:
        """Analyze metrics and create optimization report.
        
        Args:
            metrics: List of job metrics to analyze
        """
        if not metrics:
            print("No metrics to analyze")
            return

        # Analyze metrics
        analyzer = MetricsAnalyzer()
        analyzer.add_metrics(metrics)
        job_stats, opportunities = analyzer.analyze()

        # Generate report
        report_gen = ResourceOptimizationReport(job_stats, opportunities)
        summary = report_gen.generate_summary()
        detailed_report = report_gen.generate_detailed_report()

        # Create weekly optimization issue
        self._create_optimization_issue(summary, detailed_report)

        # Create high-priority issues for critical opportunities
        for opp in opportunities:
            if opp.severity == 'high':
                self._create_opportunity_issue(opp)

        # Log metrics for dashboard
        self._log_metrics(summary)

    def _create_optimization_issue(self, summary: Dict[str, Any], 
                                  detailed_report: str) -> None:
        """Create weekly optimization report issue."""
        title = f"📊 Weekly Resource Optimization Report - {summary['total_opportunities']} Opportunities"
        description = detailed_report
        labels = ['optimization', 'weekly-report', 'resource-analysis']

        self.gitlab_api.create_issue(title, description, labels)

    def _create_opportunity_issue(self, opportunity) -> None:
        """Create issue for a specific optimization opportunity."""
        title = f"🔴 [HIGH] {opportunity.job_name}: {opportunity.issue_type.replace('_', ' ').title()}"
        description = f"""
## Optimization Opportunity

**Job:** {opportunity.job_name}
**Issue Type:** {opportunity.issue_type.replace('_', ' ').title()}
**Severity:** {opportunity.severity.upper()}

### Description

{opportunity.description}

### Current vs Baseline

- **Current:** {opportunity.current_metric:.2f}
- **Baseline:** {opportunity.baseline_metric:.2f}

### Recommendations

"""
        for rec in opportunity.recommendations:
            description += f"- {rec}\n"

        description += f"""
### Impact

- **Estimated Savings:** {opportunity.estimated_savings_kwh:.4f} kWh ({opportunity.estimated_savings_pct:.2f}%)
- **Impact Score:** {opportunity.impact_score:.1f}/100

### Next Steps

1. Review the recommendations above
2. Implement the suggested optimizations
3. Monitor metrics to verify improvements
4. Close this issue once optimizations are complete
"""
        labels = ['optimization', 'high-priority', opportunity.issue_type]
        self.gitlab_api.create_issue(title, description, labels)

    def _log_metrics(self, summary: Dict[str, Any]) -> None:
        """Log metrics for dashboard aggregation.
        
        In production, would write to a metrics file or database.
        """
        metrics_entry = {
            'timestamp': summary['timestamp'],
            'jobs_analyzed': summary['total_jobs_analyzed'],
            'opportunities_found': summary['total_opportunities'],
            'high_severity': summary['high_severity'],
            'potential_savings_kwh': summary['energy']['potential_savings_kwh'],
            'potential_savings_pct': summary['energy']['potential_savings_pct'],
        }
        print(f"[Metrics] {json.dumps(metrics_entry)}")


def main():
    """Main entry point for the agent."""
    # Get environment variables
    project_id = os.getenv('CI_PROJECT_ID', '80410036')

    # Sample metrics for testing
    sample_metrics = [
        JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 45, 1024, 50, 'success'),
        JobMetric('job-1', 'build', '2024-03-19T11:00Z', 320, 2, 48, 1100, 52, 'success'),
        JobMetric('job-2', 'test', '2024-03-19T10:00Z', 600, 8, 25, 4096, 40, 'success'),
        JobMetric('job-2', 'test', '2024-03-19T11:00Z', 620, 8, 28, 4200, 42, 'failed'),
        JobMetric('job-3', 'deploy', '2024-03-19T10:00Z', 120, 1, 80, 512, 70, 'success'),
        JobMetric('job-3', 'deploy', '2024-03-19T11:00Z', 110, 1, 85, 480, 75, 'success'),
    ]

    agent = ResourceOptimizationAgent(project_id)
    agent.analyze_and_report(sample_metrics)


if __name__ == '__main__':
    main()
