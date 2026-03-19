"""GitLab integration for Dashboard Data Agent.

Handles interaction with GitLab API for metrics collection and reporting.
"""

import os
import json
from typing import List, Dict, Any, Optional
from datetime import datetime, timedelta
from dashboard_data import (
    DashboardDataAgent,
    DailyMetrics,
    SustainabilityGoal,
)


class PrometheusMetricsCollector:
    """Collects metrics from Prometheus for dashboard."""

    def __init__(self, prometheus_url: Optional[str] = None):
        self.prometheus_url = prometheus_url or os.getenv(
            'PROMETHEUS_URL',
            'http://prometheus:9090'
        )

    def get_daily_metrics(self, date: str) -> Optional[DailyMetrics]:
        """Get daily metrics from Prometheus.
        
        In production, would query Prometheus with PromQL:
        - sum(gitlab_runner_job_duration_seconds)
        - sum(gitlab_runner_job_cpu_seconds_total)
        - count(gitlab_runner_job_status{status="success"})
        - count(gitlab_runner_job_status{status="failed"})
        """
        # Mock implementation for MVP
        return None


class GitLabMetricsCollector:
    """Collects metrics from GitLab API."""

    def __init__(self, project_id: str, token: Optional[str] = None):
        self.project_id = project_id
        self.token = token or os.getenv('GITLAB_TOKEN')
        self.api_url = os.getenv('CI_API_V4_URL', 'https://gitlab.com/api/v4')

    def get_compliance_issues(self, date: str) -> Dict[str, int]:
        """Get compliance issues opened/resolved on a date.
        
        In production, would call:
        GET /projects/{id}/issues?created_after={date}&labels=sustainability
        """
        # Mock implementation for MVP
        return {'opened': 0, 'resolved': 0}

    def get_pipeline_count(self, date: str) -> int:
        """Get number of pipelines on a date.
        
        In production, would call:
        GET /projects/{id}/pipelines?updated_after={date}
        """
        # Mock implementation for MVP
        return 0

    def get_deployment_count(self, date: str) -> int:
        """Get number of deployments on a date.
        
        In production, would call:
        GET /projects/{id}/deployments?updated_after={date}
        """
        # Mock implementation for MVP
        return 0


class DashboardDataAgentGitLab:
    """Main agent for dashboard data aggregation with GitLab integration."""

    def __init__(self, project_id: str, data_dir: str = 'dashboards/data'):
        self.project_id = project_id
        self.agent = DashboardDataAgent(data_dir)
        self.prometheus_collector = PrometheusMetricsCollector()
        self.gitlab_collector = GitLabMetricsCollector(project_id)

    def collect_and_aggregate(self, days: int = 7) -> None:
        """Collect metrics for the last N days and aggregate.
        
        Args:
            days: Number of days to collect metrics for
        """
        # Collect metrics for each day
        for i in range(days):
            date = (datetime.utcnow() - timedelta(days=i)).strftime('%Y-%m-%d')

            # Get metrics from various sources
            prometheus_metrics = self.prometheus_collector.get_daily_metrics(date)
            compliance_issues = self.gitlab_collector.get_compliance_issues(date)
            pipeline_count = self.gitlab_collector.get_pipeline_count(date)
            deployment_count = self.gitlab_collector.get_deployment_count(date)

            # Create daily metrics (use mock data if no real data)
            daily = self._create_daily_metrics(
                date,
                prometheus_metrics,
                compliance_issues,
                pipeline_count,
                deployment_count,
            )

            self.agent.process_daily_metrics(daily)

        # Set default sustainability goals
        self._set_default_goals()

        # Aggregate and write
        self.agent.aggregate_and_write()

    def _create_daily_metrics(self, date: str, prometheus_metrics: Optional[DailyMetrics],
                             compliance_issues: Dict[str, int], pipeline_count: int,
                             deployment_count: int) -> DailyMetrics:
        """Create daily metrics from collected data."""
        if prometheus_metrics:
            # Use real metrics if available
            daily = prometheus_metrics
            daily.compliance_issues_opened = compliance_issues.get('opened', 0)
            daily.compliance_issues_resolved = compliance_issues.get('resolved', 0)
            daily.builds_count = pipeline_count
            daily.deployments_count = deployment_count
            return daily
        else:
            # Use mock data for MVP
            import random
            return DailyMetrics(
                date=date,
                total_energy_kwh=40 + random.uniform(-10, 10),
                total_emissions_kg_co2=16 + random.uniform(-4, 4),
                builds_count=10 + random.randint(-2, 5),
                deployments_count=random.randint(1, 3),
                compliance_issues_opened=random.randint(0, 3),
                compliance_issues_resolved=random.randint(0, 2),
                avg_carbon_intensity_g_per_kwh=250 + random.uniform(-50, 50),
                optimization_recommendations_count=random.randint(2, 6),
                failed_jobs_count=random.randint(0, 2),
                wasted_energy_kwh=2 + random.uniform(-1, 2),
            )

    def _set_default_goals(self) -> None:
        """Set default sustainability goals."""
        goals = [
            SustainabilityGoal(
                goal_id='goal-co2-reduction',
                name='Reduce CO₂ emissions by 20%',
                target_value=100,
                target_unit='kg_co2',
                baseline_value=125,
                deadline='2024-12-31',
                current_value=110,
                progress_percent=88,
                status='on_track',
            ),
            SustainabilityGoal(
                goal_id='goal-energy-reduction',
                name='Reduce energy consumption by 15%',
                target_value=300,
                target_unit='kwh',
                baseline_value=350,
                deadline='2024-12-31',
                current_value=320,
                progress_percent=91,
                status='on_track',
            ),
            SustainabilityGoal(
                goal_id='goal-compliance-issues',
                name='Resolve 80% of compliance issues',
                target_value=80,
                target_unit='percent',
                baseline_value=0,
                deadline='2024-12-31',
                current_value=75,
                progress_percent=94,
                status='on_track',
            ),
            SustainabilityGoal(
                goal_id='goal-sci-score',
                name='Reduce SCI score to 0.5 kg CO₂/build',
                target_value=0.5,
                target_unit='kg_co2',
                baseline_value=0.8,
                deadline='2024-12-31',
                current_value=0.55,
                progress_percent=91,
                status='on_track',
            ),
        ]
        self.agent.set_sustainability_goals(goals)


def main():
    """Main entry point for the agent."""
    # Get environment variables
    project_id = os.getenv('CI_PROJECT_ID', '80410036')
    data_dir = os.getenv('DASHBOARD_DATA_DIR', 'dashboards/data')

    # Create agent
    agent = DashboardDataAgentGitLab(project_id, data_dir)

    # Collect and aggregate metrics
    print("Collecting and aggregating metrics...")
    agent.collect_and_aggregate(days=7)

    print(f"Dashboard data updated in {data_dir}")


if __name__ == '__main__':
    main()
