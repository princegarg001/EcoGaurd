"""Dashboard Data Agent for EcoGuard.

Aggregates metrics and updates sustainability dashboard.
"""

import os
import json
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, asdict
from datetime import datetime, timedelta
from collections import defaultdict
import statistics


@dataclass
class DailyMetrics:
    """Daily sustainability metrics."""
    date: str
    total_energy_kwh: float
    total_emissions_kg_co2: float
    builds_count: int
    deployments_count: int
    compliance_issues_opened: int
    compliance_issues_resolved: int
    avg_carbon_intensity_g_per_kwh: float
    optimization_recommendations_count: int
    failed_jobs_count: int
    wasted_energy_kwh: float


@dataclass
class WeeklyMetrics:
    """Weekly aggregated metrics."""
    week_start: str
    week_end: str
    total_energy_kwh: float
    total_emissions_kg_co2: float
    builds_count: int
    deployments_count: int
    compliance_issues_opened: int
    compliance_issues_resolved: int
    avg_emissions_per_build_kg_co2: float
    avg_emissions_per_deployment_kg_co2: float
    optimization_recommendations_count: int
    failed_jobs_count: int
    wasted_energy_kwh: float
    energy_reduction_pct: float  # vs previous week


@dataclass
class MonthlyMetrics:
    """Monthly aggregated metrics."""
    month: str
    total_energy_kwh: float
    total_emissions_kg_co2: float
    builds_count: int
    deployments_count: int
    compliance_issues_opened: int
    compliance_issues_resolved: int
    avg_emissions_per_build_kg_co2: float
    avg_emissions_per_deployment_kg_co2: float
    optimization_recommendations_count: int
    failed_jobs_count: int
    wasted_energy_kwh: float
    energy_reduction_pct: float  # vs previous month
    sci_score: float  # Software Carbon Intensity


@dataclass
class SustainabilityGoal:
    """Sustainability goal tracking."""
    goal_id: str
    name: str
    target_value: float
    target_unit: str  # 'kg_co2', 'kwh', 'percent'
    baseline_value: float
    deadline: str
    current_value: float
    progress_percent: float
    status: str  # 'on_track', 'at_risk', 'achieved'


class MetricsAggregator:
    """Aggregates sustainability metrics from various sources."""

    def __init__(self):
        self.daily_metrics: Dict[str, DailyMetrics] = {}
        self.weekly_metrics: Dict[str, WeeklyMetrics] = {}
        self.monthly_metrics: Dict[str, MonthlyMetrics] = {}
        self.goals: List[SustainabilityGoal] = []

    def add_daily_metrics(self, metrics: DailyMetrics) -> None:
        """Add daily metrics."""
        self.daily_metrics[metrics.date] = metrics

    def aggregate_weekly(self, week_start: str) -> WeeklyMetrics:
        """Aggregate metrics for a week.
        
        Args:
            week_start: Start date of week (YYYY-MM-DD)
            
        Returns:
            WeeklyMetrics with aggregated data
        """
        start_dt = datetime.fromisoformat(week_start)
        end_dt = start_dt + timedelta(days=6)
        week_end = end_dt.strftime('%Y-%m-%d')

        # Collect metrics for the week
        week_daily_metrics = []
        for i in range(7):
            date = (start_dt + timedelta(days=i)).strftime('%Y-%m-%d')
            if date in self.daily_metrics:
                week_daily_metrics.append(self.daily_metrics[date])

        if not week_daily_metrics:
            # Return empty metrics if no data
            return WeeklyMetrics(
                week_start=week_start,
                week_end=week_end,
                total_energy_kwh=0,
                total_emissions_kg_co2=0,
                builds_count=0,
                deployments_count=0,
                compliance_issues_opened=0,
                compliance_issues_resolved=0,
                avg_emissions_per_build_kg_co2=0,
                avg_emissions_per_deployment_kg_co2=0,
                optimization_recommendations_count=0,
                failed_jobs_count=0,
                wasted_energy_kwh=0,
                energy_reduction_pct=0,
            )

        # Aggregate
        total_energy = sum(m.total_energy_kwh for m in week_daily_metrics)
        total_emissions = sum(m.total_emissions_kg_co2 for m in week_daily_metrics)
        total_builds = sum(m.builds_count for m in week_daily_metrics)
        total_deployments = sum(m.deployments_count for m in week_daily_metrics)
        total_issues_opened = sum(m.compliance_issues_opened for m in week_daily_metrics)
        total_issues_resolved = sum(m.compliance_issues_resolved for m in week_daily_metrics)
        total_recommendations = sum(m.optimization_recommendations_count for m in week_daily_metrics)
        total_failed_jobs = sum(m.failed_jobs_count for m in week_daily_metrics)
        total_wasted_energy = sum(m.wasted_energy_kwh for m in week_daily_metrics)

        # Calculate per-build and per-deployment emissions
        avg_per_build = (total_emissions / total_builds) if total_builds > 0 else 0
        avg_per_deployment = (total_emissions / total_deployments) if total_deployments > 0 else 0

        # Calculate energy reduction vs previous week
        energy_reduction_pct = self._calculate_energy_reduction(week_start)

        # Calculate average carbon intensity
        avg_intensity = statistics.mean(
            [m.avg_carbon_intensity_g_per_kwh for m in week_daily_metrics]
        ) if week_daily_metrics else 0

        weekly = WeeklyMetrics(
            week_start=week_start,
            week_end=week_end,
            total_energy_kwh=total_energy,
            total_emissions_kg_co2=total_emissions,
            builds_count=total_builds,
            deployments_count=total_deployments,
            compliance_issues_opened=total_issues_opened,
            compliance_issues_resolved=total_issues_resolved,
            avg_emissions_per_build_kg_co2=avg_per_build,
            avg_emissions_per_deployment_kg_co2=avg_per_deployment,
            optimization_recommendations_count=total_recommendations,
            failed_jobs_count=total_failed_jobs,
            wasted_energy_kwh=total_wasted_energy,
            energy_reduction_pct=energy_reduction_pct,
        )

        self.weekly_metrics[week_start] = weekly
        return weekly

    def aggregate_monthly(self, month: str) -> MonthlyMetrics:
        """Aggregate metrics for a month.
        
        Args:
            month: Month in format YYYY-MM
            
        Returns:
            MonthlyMetrics with aggregated data
        """
        # Parse month
        year, month_num = month.split('-')
        start_dt = datetime(int(year), int(month_num), 1)

        # Find all weeks in month
        month_weekly_metrics = []
        current_dt = start_dt
        while current_dt.month == start_dt.month:
            week_start = current_dt.strftime('%Y-%m-%d')
            if week_start in self.weekly_metrics:
                month_weekly_metrics.append(self.weekly_metrics[week_start])
            current_dt += timedelta(days=7)

        if not month_weekly_metrics:
            # Return empty metrics if no data
            return MonthlyMetrics(
                month=month,
                total_energy_kwh=0,
                total_emissions_kg_co2=0,
                builds_count=0,
                deployments_count=0,
                compliance_issues_opened=0,
                compliance_issues_resolved=0,
                avg_emissions_per_build_kg_co2=0,
                avg_emissions_per_deployment_kg_co2=0,
                optimization_recommendations_count=0,
                failed_jobs_count=0,
                wasted_energy_kwh=0,
                energy_reduction_pct=0,
                sci_score=0,
            )

        # Aggregate
        total_energy = sum(m.total_energy_kwh for m in month_weekly_metrics)
        total_emissions = sum(m.total_emissions_kg_co2 for m in month_weekly_metrics)
        total_builds = sum(m.builds_count for m in month_weekly_metrics)
        total_deployments = sum(m.deployments_count for m in month_weekly_metrics)
        total_issues_opened = sum(m.compliance_issues_opened for m in month_weekly_metrics)
        total_issues_resolved = sum(m.compliance_issues_resolved for m in month_weekly_metrics)
        total_recommendations = sum(m.optimization_recommendations_count for m in month_weekly_metrics)
        total_failed_jobs = sum(m.failed_jobs_count for m in month_weekly_metrics)
        total_wasted_energy = sum(m.wasted_energy_kwh for m in month_weekly_metrics)

        # Calculate per-build and per-deployment emissions
        avg_per_build = (total_emissions / total_builds) if total_builds > 0 else 0
        avg_per_deployment = (total_emissions / total_deployments) if total_deployments > 0 else 0

        # Calculate energy reduction vs previous month
        energy_reduction_pct = self._calculate_monthly_energy_reduction(month)

        # Calculate SCI score (CO2 per build)
        sci_score = avg_per_build

        monthly = MonthlyMetrics(
            month=month,
            total_energy_kwh=total_energy,
            total_emissions_kg_co2=total_emissions,
            builds_count=total_builds,
            deployments_count=total_deployments,
            compliance_issues_opened=total_issues_opened,
            compliance_issues_resolved=total_issues_resolved,
            avg_emissions_per_build_kg_co2=avg_per_build,
            avg_emissions_per_deployment_kg_co2=avg_per_deployment,
            optimization_recommendations_count=total_recommendations,
            failed_jobs_count=total_failed_jobs,
            wasted_energy_kwh=total_wasted_energy,
            energy_reduction_pct=energy_reduction_pct,
            sci_score=sci_score,
        )

        self.monthly_metrics[month] = monthly
        return monthly

    def _calculate_energy_reduction(self, week_start: str) -> float:
        """Calculate energy reduction vs previous week."""
        start_dt = datetime.fromisoformat(week_start)
        prev_week_start = (start_dt - timedelta(days=7)).strftime('%Y-%m-%d')

        if prev_week_start not in self.weekly_metrics:
            return 0

        current_week = self.weekly_metrics[week_start]
        prev_week = self.weekly_metrics[prev_week_start]

        if prev_week.total_energy_kwh == 0:
            return 0

        reduction = (prev_week.total_energy_kwh - current_week.total_energy_kwh) / prev_week.total_energy_kwh * 100
        return max(-100, min(100, reduction))  # Clamp to -100 to 100

    def _calculate_monthly_energy_reduction(self, month: str) -> float:
        """Calculate energy reduction vs previous month."""
        year, month_num = month.split('-')
        current_month_dt = datetime(int(year), int(month_num), 1)
        prev_month_dt = current_month_dt - timedelta(days=1)
        prev_month = prev_month_dt.strftime('%Y-%m')

        if prev_month not in self.monthly_metrics:
            return 0

        current = self.monthly_metrics[month]
        previous = self.monthly_metrics[prev_month]

        if previous.total_energy_kwh == 0:
            return 0

        reduction = (previous.total_energy_kwh - current.total_energy_kwh) / previous.total_energy_kwh * 100
        return max(-100, min(100, reduction))  # Clamp to -100 to 100

    def add_goal(self, goal: SustainabilityGoal) -> None:
        """Add sustainability goal."""
        self.goals.append(goal)

    def update_goal_progress(self, goal_id: str, current_value: float) -> None:
        """Update goal progress."""
        for goal in self.goals:
            if goal.goal_id == goal_id:
                goal.current_value = current_value
                goal.progress_percent = (current_value / goal.target_value * 100) if goal.target_value > 0 else 0

                # Determine status
                if goal.progress_percent >= 100:
                    goal.status = 'achieved'
                elif goal.progress_percent >= 75:
                    goal.status = 'on_track'
                else:
                    goal.status = 'at_risk'
                break


class DashboardDataWriter:
    """Writes aggregated metrics to dashboard data files."""

    def __init__(self, data_dir: str = 'dashboards/data'):
        self.data_dir = data_dir
        os.makedirs(data_dir, exist_ok=True)

    def write_daily_metrics(self, daily_metrics: Dict[str, DailyMetrics]) -> None:
        """Write daily metrics to JSON file."""
        data = [
            asdict(m) for m in sorted(daily_metrics.values(), key=lambda x: x.date)
        ]
        self._write_json('daily-metrics.json', data)

    def write_weekly_metrics(self, weekly_metrics: Dict[str, WeeklyMetrics]) -> None:
        """Write weekly metrics to JSON file."""
        data = [
            asdict(m) for m in sorted(weekly_metrics.values(), key=lambda x: x.week_start)
        ]
        self._write_json('weekly-metrics.json', data)

    def write_monthly_metrics(self, monthly_metrics: Dict[str, MonthlyMetrics]) -> None:
        """Write monthly metrics to JSON file."""
        data = [
            asdict(m) for m in sorted(monthly_metrics.values(), key=lambda x: x.month)
        ]
        self._write_json('monthly-metrics.json', data)

    def write_goals(self, goals: List[SustainabilityGoal]) -> None:
        """Write sustainability goals to JSON file."""
        data = [asdict(g) for g in goals]
        self._write_json('sustainability-goals.json', data)

    def write_summary(self, aggregator: MetricsAggregator) -> None:
        """Write summary dashboard data."""
        # Get latest metrics
        latest_daily = None
        latest_weekly = None
        latest_monthly = None

        if aggregator.daily_metrics:
            latest_daily = max(aggregator.daily_metrics.values(), key=lambda x: x.date)
        if aggregator.weekly_metrics:
            latest_weekly = max(aggregator.weekly_metrics.values(), key=lambda x: x.week_start)
        if aggregator.monthly_metrics:
            latest_monthly = max(aggregator.monthly_metrics.values(), key=lambda x: x.month)

        summary = {
            'timestamp': datetime.utcnow().isoformat(),
            'latest_daily': asdict(latest_daily) if latest_daily else None,
            'latest_weekly': asdict(latest_weekly) if latest_weekly else None,
            'latest_monthly': asdict(latest_monthly) if latest_monthly else None,
            'total_days_tracked': len(aggregator.daily_metrics),
            'total_weeks_tracked': len(aggregator.weekly_metrics),
            'total_months_tracked': len(aggregator.monthly_metrics),
            'goals': [asdict(g) for g in aggregator.goals],
        }
        self._write_json('summary.json', summary)

    def _write_json(self, filename: str, data: Any) -> None:
        """Write data to JSON file."""
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"Wrote {filepath}")


class DashboardDataAgent:
    """Main agent for dashboard data aggregation."""

    def __init__(self, data_dir: str = 'dashboards/data'):
        self.aggregator = MetricsAggregator()
        self.writer = DashboardDataWriter(data_dir)

    def process_daily_metrics(self, daily_metrics: DailyMetrics) -> None:
        """Process and store daily metrics."""
        self.aggregator.add_daily_metrics(daily_metrics)

    def aggregate_and_write(self) -> None:
        """Aggregate metrics and write to dashboard files."""
        # Aggregate weekly metrics
        today = datetime.utcnow()
        week_start = (today - timedelta(days=today.weekday())).strftime('%Y-%m-%d')
        self.aggregator.aggregate_weekly(week_start)

        # Aggregate monthly metrics
        month = today.strftime('%Y-%m')
        self.aggregator.aggregate_monthly(month)

        # Write all metrics
        self.writer.write_daily_metrics(self.aggregator.daily_metrics)
        self.writer.write_weekly_metrics(self.aggregator.weekly_metrics)
        self.writer.write_monthly_metrics(self.aggregator.monthly_metrics)
        self.writer.write_goals(self.aggregator.goals)
        self.writer.write_summary(self.aggregator)

    def set_sustainability_goals(self, goals: List[SustainabilityGoal]) -> None:
        """Set sustainability goals."""
        for goal in goals:
            self.aggregator.add_goal(goal)

    def update_goal_progress(self, goal_id: str, current_value: float) -> None:
        """Update goal progress."""
        self.aggregator.update_goal_progress(goal_id, current_value)


if __name__ == '__main__':
    # Example usage
    agent = DashboardDataAgent()

    # Add sample daily metrics
    today = datetime.utcnow()
    for i in range(7):
        date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
        daily = DailyMetrics(
            date=date,
            total_energy_kwh=45.2 + i * 2,
            total_emissions_kg_co2=18.5 + i * 0.8,
            builds_count=12 + i,
            deployments_count=2,
            compliance_issues_opened=3 - i,
            compliance_issues_resolved=2,
            avg_carbon_intensity_g_per_kwh=250,
            optimization_recommendations_count=5,
            failed_jobs_count=1,
            wasted_energy_kwh=2.5,
        )
        agent.process_daily_metrics(daily)

    # Set sustainability goals
    goals = [
        SustainabilityGoal(
            goal_id='goal-1',
            name='Reduce CO₂ by 20%',
            target_value=100,
            target_unit='kg_co2',
            baseline_value=125,
            deadline='2024-12-31',
            current_value=110,
            progress_percent=88,
            status='on_track',
        ),
        SustainabilityGoal(
            goal_id='goal-2',
            name='Reduce energy by 15%',
            target_value=300,
            target_unit='kwh',
            baseline_value=350,
            deadline='2024-12-31',
            current_value=320,
            progress_percent=91,
            status='on_track',
        ),
    ]
    agent.set_sustainability_goals(goals)

    # Aggregate and write
    agent.aggregate_and_write()

    print("Dashboard data aggregation complete!")
