"""Tests for Dashboard Data Agent."""

import unittest
from datetime import datetime, timedelta
from dashboard_data import (
    DailyMetrics,
    WeeklyMetrics,
    MonthlyMetrics,
    SustainabilityGoal,
    MetricsAggregator,
)


class TestMetricsAggregator(unittest.TestCase):
    """Test cases for metrics aggregation."""

    def setUp(self):
        self.aggregator = MetricsAggregator()
        self.today = datetime.utcnow()

    def test_add_daily_metrics(self):
        """Test adding daily metrics."""
        daily = DailyMetrics(
            date='2024-03-19',
            total_energy_kwh=45.2,
            total_emissions_kg_co2=18.5,
            builds_count=12,
            deployments_count=2,
            compliance_issues_opened=3,
            compliance_issues_resolved=2,
            avg_carbon_intensity_g_per_kwh=250,
            optimization_recommendations_count=5,
            failed_jobs_count=1,
            wasted_energy_kwh=2.5,
        )
        self.aggregator.add_daily_metrics(daily)

        self.assertIn('2024-03-19', self.aggregator.daily_metrics)

    def test_aggregate_weekly(self):
        """Test weekly aggregation."""
        # Add 7 days of metrics
        week_start = (self.today - timedelta(days=self.today.weekday())).strftime('%Y-%m-%d')
        for i in range(7):
            date = (self.today - timedelta(days=i)).strftime('%Y-%m-%d')
            daily = DailyMetrics(
                date=date,
                total_energy_kwh=45.0,
                total_emissions_kg_co2=18.0,
                builds_count=10,
                deployments_count=2,
                compliance_issues_opened=2,
                compliance_issues_resolved=1,
                avg_carbon_intensity_g_per_kwh=250,
                optimization_recommendations_count=4,
                failed_jobs_count=1,
                wasted_energy_kwh=2.0,
            )
            self.aggregator.add_daily_metrics(daily)

        # Aggregate week
        weekly = self.aggregator.aggregate_weekly(week_start)

        self.assertGreater(weekly.total_energy_kwh, 0)
        self.assertGreater(weekly.total_emissions_kg_co2, 0)
        self.assertEqual(weekly.builds_count, 70)  # 7 days * 10 builds

    def test_aggregate_monthly(self):
        """Test monthly aggregation."""
        # Add weekly metrics
        month = self.today.strftime('%Y-%m')
        week_start = (self.today - timedelta(days=self.today.weekday())).strftime('%Y-%m-%d')

        weekly = WeeklyMetrics(
            week_start=week_start,
            week_end=(self.today + timedelta(days=6)).strftime('%Y-%m-%d'),
            total_energy_kwh=315.0,
            total_emissions_kg_co2=126.0,
            builds_count=70,
            deployments_count=14,
            compliance_issues_opened=14,
            compliance_issues_resolved=7,
            avg_emissions_per_build_kg_co2=1.8,
            avg_emissions_per_deployment_kg_co2=9.0,
            optimization_recommendations_count=28,
            failed_jobs_count=7,
            wasted_energy_kwh=14.0,
            energy_reduction_pct=0,
        )
        self.aggregator.weekly_metrics[week_start] = weekly

        # Aggregate month
        monthly = self.aggregator.aggregate_monthly(month)

        self.assertGreater(monthly.total_energy_kwh, 0)
        self.assertGreater(monthly.total_emissions_kg_co2, 0)

    def test_sci_score_calculation(self):
        """Test SCI score calculation."""
        month = self.today.strftime('%Y-%m')
        week_start = (self.today - timedelta(days=self.today.weekday())).strftime('%Y-%m-%d')

        weekly = WeeklyMetrics(
            week_start=week_start,
            week_end=(self.today + timedelta(days=6)).strftime('%Y-%m-%d'),
            total_energy_kwh=315.0,
            total_emissions_kg_co2=126.0,
            builds_count=70,
            deployments_count=14,
            compliance_issues_opened=14,
            compliance_issues_resolved=7,
            avg_emissions_per_build_kg_co2=1.8,
            avg_emissions_per_deployment_kg_co2=9.0,
            optimization_recommendations_count=28,
            failed_jobs_count=7,
            wasted_energy_kwh=14.0,
            energy_reduction_pct=0,
        )
        self.aggregator.weekly_metrics[week_start] = weekly

        monthly = self.aggregator.aggregate_monthly(month)

        # SCI score should equal avg emissions per build
        self.assertEqual(monthly.sci_score, monthly.avg_emissions_per_build_kg_co2)

    def test_goal_tracking(self):
        """Test sustainability goal tracking."""
        goal = SustainabilityGoal(
            goal_id='goal-1',
            name='Reduce CO₂ by 20%',
            target_value=100,
            target_unit='kg_co2',
            baseline_value=125,
            deadline='2024-12-31',
            current_value=110,
            progress_percent=88,
            status='on_track',
        )
        self.aggregator.add_goal(goal)

        self.assertEqual(len(self.aggregator.goals), 1)

    def test_goal_progress_update(self):
        """Test goal progress update."""
        goal = SustainabilityGoal(
            goal_id='goal-1',
            name='Reduce CO₂ by 20%',
            target_value=100,
            target_unit='kg_co2',
            baseline_value=125,
            deadline='2024-12-31',
            current_value=110,
            progress_percent=88,
            status='on_track',
        )
        self.aggregator.add_goal(goal)

        # Update progress
        self.aggregator.update_goal_progress('goal-1', 100)

        updated_goal = self.aggregator.goals[0]
        self.assertEqual(updated_goal.current_value, 100)
        self.assertEqual(updated_goal.progress_percent, 100)
        self.assertEqual(updated_goal.status, 'achieved')

    def test_goal_status_on_track(self):
        """Test goal status determination."""
        goal = SustainabilityGoal(
            goal_id='goal-1',
            name='Test goal',
            target_value=100,
            target_unit='kg_co2',
            baseline_value=125,
            deadline='2024-12-31',
            current_value=80,
            progress_percent=80,
            status='on_track',
        )
        self.aggregator.add_goal(goal)
        self.aggregator.update_goal_progress('goal-1', 80)

        self.assertEqual(self.aggregator.goals[0].status, 'on_track')

    def test_goal_status_at_risk(self):
        """Test goal status at risk."""
        goal = SustainabilityGoal(
            goal_id='goal-1',
            name='Test goal',
            target_value=100,
            target_unit='kg_co2',
            baseline_value=125,
            deadline='2024-12-31',
            current_value=50,
            progress_percent=50,
            status='at_risk',
        )
        self.aggregator.add_goal(goal)
        self.aggregator.update_goal_progress('goal-1', 50)

        self.assertEqual(self.aggregator.goals[0].status, 'at_risk')

    def test_emissions_per_build_calculation(self):
        """Test emissions per build calculation."""
        week_start = (self.today - timedelta(days=self.today.weekday())).strftime('%Y-%m-%d')

        weekly = WeeklyMetrics(
            week_start=week_start,
            week_end=(self.today + timedelta(days=6)).strftime('%Y-%m-%d'),
            total_energy_kwh=315.0,
            total_emissions_kg_co2=126.0,
            builds_count=70,
            deployments_count=14,
            compliance_issues_opened=14,
            compliance_issues_resolved=7,
            avg_emissions_per_build_kg_co2=1.8,
            avg_emissions_per_deployment_kg_co2=9.0,
            optimization_recommendations_count=28,
            failed_jobs_count=7,
            wasted_energy_kwh=14.0,
            energy_reduction_pct=0,
        )
        self.aggregator.weekly_metrics[week_start] = weekly

        # Verify calculation
        expected_per_build = 126.0 / 70
        self.assertAlmostEqual(weekly.avg_emissions_per_build_kg_co2, expected_per_build, places=2)


if __name__ == '__main__':
    unittest.main()
