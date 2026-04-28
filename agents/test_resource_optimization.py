"""Tests for Resource Optimization Agent."""

import unittest
from resource_optimization import (
    JobMetric,
    MetricsAnalyzer,
    ResourceOptimizationReport,
)


class TestMetricsAnalyzer(unittest.TestCase):
    """Test cases for metrics analysis."""

    def setUp(self):
        self.analyzer = MetricsAnalyzer()

    def test_job_statistics_calculation(self):
        """Test calculation of job statistics."""
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success'),
            JobMetric('job-1', 'build', '2024-03-19T11:00Z', 320, 2, 55, 1100, 65, 'success'),
        ]
        self.analyzer.add_metrics(metrics)
        job_stats, _ = self.analyzer.analyze()

        self.assertIn('build', job_stats)
        self.assertEqual(job_stats['build'].run_count, 2)
        self.assertAlmostEqual(job_stats['build'].avg_duration_seconds, 310, places=0)

    def test_high_cpu_detection(self):
        """Test detection of high CPU usage."""
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success'),
            JobMetric('job-2', 'test', '2024-03-19T10:00Z', 600, 16, 30, 4096, 40, 'success'),
            JobMetric('job-3', 'deploy', '2024-03-19T10:00Z', 100, 1, 50, 512, 60, 'success'),
        ]
        self.analyzer.add_metrics(metrics)
        _, opportunities = self.analyzer.analyze()

        high_cpu_opps = [o for o in opportunities if o.issue_type == 'high_cpu']
        self.assertGreater(len(high_cpu_opps), 0)

    def test_high_memory_detection(self):
        """Test detection of high memory usage."""
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success'),
            JobMetric('job-2', 'test', '2024-03-19T10:00Z', 600, 2, 50, 8192, 40, 'success'),
            JobMetric('job-3', 'deploy', '2024-03-19T10:00Z', 100, 1, 50, 512, 60, 'success'),
        ]
        self.analyzer.add_metrics(metrics)
        _, opportunities = self.analyzer.analyze()

        high_mem_opps = [o for o in opportunities if o.issue_type == 'high_memory']
        self.assertGreater(len(high_mem_opps), 0)

    def test_long_duration_detection(self):
        """Test detection of long-running jobs."""
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success'),
            JobMetric('job-2', 'test', '2024-03-19T10:00Z', 3600, 2, 50, 1024, 60, 'success'),
            JobMetric('job-3', 'deploy', '2024-03-19T10:00Z', 100, 1, 50, 512, 60, 'success'),
        ]
        self.analyzer.add_metrics(metrics)
        _, opportunities = self.analyzer.analyze()

        long_dur_opps = [o for o in opportunities if o.issue_type == 'long_duration']
        self.assertGreater(len(long_dur_opps), 0)

    def test_low_success_rate_detection(self):
        """Test detection of low success rate."""
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success'),
            JobMetric('job-1', 'build', '2024-03-19T11:00Z', 300, 2, 50, 1024, 60, 'failed'),
            JobMetric('job-1', 'build', '2024-03-19T12:00Z', 300, 2, 50, 1024, 60, 'failed'),
        ]
        self.analyzer.add_metrics(metrics)
        _, opportunities = self.analyzer.analyze()

        low_success_opps = [o for o in opportunities if o.issue_type == 'low_success_rate']
        self.assertGreater(len(low_success_opps), 0)

    def test_low_cpu_utilization_detection(self):
        """Test detection of low CPU utilization."""
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 8, 20, 1024, 60, 'success'),
        ]
        self.analyzer.add_metrics(metrics)
        _, opportunities = self.analyzer.analyze()

        # Should detect inefficient parallelization
        inefficient_opps = [o for o in opportunities if o.issue_type == 'inefficient_parallelization']
        self.assertGreater(len(inefficient_opps), 0)

    def test_opportunity_sorting_by_impact(self):
        """Test that opportunities are sorted by impact score."""
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success'),
            JobMetric('job-2', 'test', '2024-03-19T10:00Z', 600, 8, 30, 4096, 40, 'success'),
            JobMetric('job-3', 'deploy', '2024-03-19T10:00Z', 120, 1, 80, 512, 70, 'success'),
        ]
        self.analyzer.add_metrics(metrics)
        _, opportunities = self.analyzer.analyze()

        # Opportunities should be sorted by impact score (descending)
        if len(opportunities) > 1:
            for i in range(len(opportunities) - 1):
                self.assertGreaterEqual(
                    opportunities[i].impact_score,
                    opportunities[i + 1].impact_score
                )

    def test_wasted_energy_calculation(self):
        """Test calculation of wasted energy from failed jobs."""
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success'),
            JobMetric('job-1', 'build', '2024-03-19T11:00Z', 300, 2, 50, 1024, 60, 'failed'),
        ]
        self.analyzer.add_metrics(metrics)
        job_stats, _ = self.analyzer.analyze()

        self.assertGreater(job_stats['build'].total_wasted_energy_kwh, 0)


class TestResourceOptimizationReport(unittest.TestCase):
    """Test cases for report generation."""

    def setUp(self):
        metrics = [
            JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 50, 1024, 60, 'success'),
            JobMetric('job-2', 'test', '2024-03-19T10:00Z', 600, 8, 30, 4096, 40, 'success'),
        ]
        analyzer = MetricsAnalyzer()
        analyzer.add_metrics(metrics)
        self.job_stats, self.opportunities = analyzer.analyze()
        self.report = ResourceOptimizationReport(self.job_stats, self.opportunities)

    def test_summary_generation(self):
        """Test summary report generation."""
        summary = self.report.generate_summary()

        self.assertIn('timestamp', summary)
        self.assertIn('total_jobs_analyzed', summary)
        self.assertIn('total_opportunities', summary)
        self.assertIn('energy', summary)

    def test_detailed_report_generation(self):
        """Test detailed report generation."""
        report = self.report.generate_detailed_report()

        self.assertIn('EcoGuard Resource Optimization Report', report)
        self.assertIn('Energy Impact', report)
        self.assertIn('Top Optimization Opportunities', report)

    def test_report_contains_recommendations(self):
        """Test that report contains recommendations."""
        report = self.report.generate_detailed_report()

        self.assertIn('Recommendations:', report)


if __name__ == '__main__':
    unittest.main()
