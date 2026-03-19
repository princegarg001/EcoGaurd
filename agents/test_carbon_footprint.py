"""Tests for Carbon Footprint Agent."""

import unittest
from carbon_footprint import (
    JobMetrics,
    EnergyCalculator,
    CarbonIntensityProvider,
    CarbonFootprintAnalyzer,
)


class TestEnergyCalculator(unittest.TestCase):
    """Test cases for energy calculations."""

    def setUp(self):
        self.provider = CarbonIntensityProvider()
        self.calculator = EnergyCalculator(self.provider)

    def test_single_job_energy_calculation(self):
        """Test energy calculation for a single job."""
        job = JobMetrics('job-1', 'build', 3600, 2, 1024, 'success')
        calc = self.calculator.calculate_job_energy(job)

        # 2 cores * 30W * 1 hour = 60 Wh
        self.assertAlmostEqual(calc.cpu_energy_wh, 60, places=1)

        # 1 GB * 0.5W * 1 hour = 0.5 Wh
        self.assertAlmostEqual(calc.memory_energy_wh, 0.5, places=1)

        # Total should be sum
        self.assertAlmostEqual(calc.total_energy_wh, 60.5, places=1)

    def test_energy_in_kwh(self):
        """Test energy conversion to kWh."""
        job = JobMetrics('job-1', 'build', 3600, 2, 1024, 'success')
        calc = self.calculator.calculate_job_energy(job)

        # 60.5 Wh = 0.0605 kWh
        self.assertAlmostEqual(calc.total_energy_kwh, 0.0605, places=4)

    def test_co2_calculation(self):
        """Test CO₂ emissions calculation."""
        job = JobMetrics('job-1', 'build', 3600, 2, 1024, 'success')
        calc = self.calculator.calculate_job_energy(job, zone='US-CA')

        # Should have non-zero emissions
        self.assertGreater(calc.total_emissions_kg_co2, 0)
        self.assertGreater(calc.total_emissions_g_co2, 0)

    def test_pipeline_energy_calculation(self):
        """Test energy calculation for multiple jobs."""
        jobs = [
            JobMetrics('job-1', 'build', 300, 2, 1024, 'success'),
            JobMetrics('job-2', 'test', 600, 4, 2048, 'success'),
            JobMetrics('job-3', 'deploy', 120, 1, 512, 'success'),
        ]

        total_calc, job_calcs = self.calculator.calculate_pipeline_energy(jobs)

        # Should have calculations for all jobs
        self.assertEqual(len(job_calcs), 3)

        # Total should be sum of individual jobs
        sum_energy = sum(c.total_energy_kwh for c in job_calcs.values())
        self.assertAlmostEqual(total_calc.total_energy_kwh, sum_energy, places=4)

    def test_different_zones_different_emissions(self):
        """Test that different zones produce different emissions."""
        job = JobMetrics('job-1', 'build', 3600, 2, 1024, 'success')

        calc_ca = self.calculator.calculate_job_energy(job, zone='US-CA')
        calc_au = self.calculator.calculate_job_energy(job, zone='AU')

        # Australia has higher carbon intensity, so more emissions
        self.assertGreater(
            calc_au.total_emissions_kg_co2,
            calc_ca.total_emissions_kg_co2
        )


class TestCarbonFootprintAnalyzer(unittest.TestCase):
    """Test cases for carbon footprint analysis."""

    def setUp(self):
        self.analyzer = CarbonFootprintAnalyzer()
        self.analyzer.set_baseline(5.0, 2.0)

    def test_pipeline_analysis(self):
        """Test complete pipeline analysis."""
        jobs = [
            JobMetrics('job-1', 'build', 300, 2, 1024, 'success'),
            JobMetrics('job-2', 'test', 600, 4, 2048, 'success'),
        ]

        analysis = self.analyzer.analyze_pipeline(jobs)

        # Check required fields
        self.assertIn('total_jobs', analysis)
        self.assertIn('energy', analysis)
        self.assertIn('emissions', analysis)
        self.assertIn('recommendations', analysis)
        self.assertIn('heaviest_jobs', analysis)

    def test_baseline_comparison(self):
        """Test baseline comparison calculation."""
        jobs = [
            JobMetrics('job-1', 'build', 3600, 2, 1024, 'success'),
        ]

        analysis = self.analyzer.analyze_pipeline(jobs)

        # Should have difference from baseline
        self.assertIn('difference_kwh', analysis['energy'])
        self.assertIn('difference_pct', analysis['energy'])

    def test_recommendations_generated(self):
        """Test that recommendations are generated."""
        jobs = [
            JobMetrics('job-1', 'build', 3600, 2, 1024, 'success'),
        ]

        analysis = self.analyzer.analyze_pipeline(jobs)

        # Should have at least one recommendation
        self.assertGreater(len(analysis['recommendations']), 0)

    def test_failed_job_detection(self):
        """Test detection of failed jobs in recommendations."""
        jobs = [
            JobMetrics('job-1', 'build', 300, 2, 1024, 'success'),
            JobMetrics('job-2', 'test', 600, 4, 2048, 'failed'),
        ]

        analysis = self.analyzer.analyze_pipeline(jobs)

        # Should have recommendation about failed job
        failed_recs = [r for r in analysis['recommendations'] if 'failed' in r.lower()]
        self.assertGreater(len(failed_recs), 0)

    def test_heaviest_jobs_identified(self):
        """Test identification of heaviest jobs."""
        jobs = [
            JobMetrics('job-1', 'build', 100, 1, 512, 'success'),
            JobMetrics('job-2', 'test', 1000, 8, 4096, 'success'),
            JobMetrics('job-3', 'deploy', 50, 1, 256, 'success'),
        ]

        analysis = self.analyzer.analyze_pipeline(jobs)

        # job-2 should be heaviest
        self.assertEqual(analysis['heaviest_jobs'][0]['job_id'], 'job-2')

    def test_job_count_accuracy(self):
        """Test accurate job counting."""
        jobs = [
            JobMetrics('job-1', 'build', 300, 2, 1024, 'success'),
            JobMetrics('job-2', 'test', 600, 4, 2048, 'success'),
            JobMetrics('job-3', 'deploy', 120, 1, 512, 'failed'),
        ]

        analysis = self.analyzer.analyze_pipeline(jobs)

        self.assertEqual(analysis['total_jobs'], 3)
        self.assertEqual(analysis['successful_jobs'], 2)
        self.assertEqual(analysis['failed_jobs'], 1)


if __name__ == '__main__':
    unittest.main()
