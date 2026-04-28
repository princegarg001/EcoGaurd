"""Tests for Eco-Friendly Deployment Agent."""

import unittest
from datetime import datetime, timedelta
from eco_friendly_deployment import (
    DeploymentConfig,
    CarbonIntensityProvider,
    DeploymentOptimizer,
)


class TestCarbonIntensityProvider(unittest.TestCase):
    """Test cases for carbon intensity provider."""

    def setUp(self):
        self.provider = CarbonIntensityProvider()

    def test_get_region_data(self):
        """Test getting region data."""
        region_data = self.provider.get_region_data('US-CA')

        self.assertEqual(region_data.region_code, 'US-CA')
        self.assertGreater(region_data.current_intensity_g_per_kwh, 0)
        self.assertGreater(len(region_data.forecast_24h), 0)

    def test_forecast_generation(self):
        """Test 24-hour forecast generation."""
        region_data = self.provider.get_region_data('US-CA')

        self.assertEqual(len(region_data.forecast_24h), 24)
        for forecast in region_data.forecast_24h:
            self.assertGreater(forecast.carbon_intensity_g_per_kwh, 0)
            self.assertGreaterEqual(forecast.confidence, 0)
            self.assertLessEqual(forecast.confidence, 1)

    def test_renewable_heavy_region(self):
        """Test renewable-heavy region has lower night intensity."""
        region_data = self.provider.get_region_data('EU-FR')  # Nuclear heavy

        # Find day and night intensities
        day_intensities = [f.carbon_intensity_g_per_kwh for f in region_data.forecast_24h[9:17]]
        night_intensities = [f.carbon_intensity_g_per_kwh for f in region_data.forecast_24h[0:6]]

        # For nuclear/renewable heavy, should be relatively stable
        self.assertLess(max(day_intensities) - min(day_intensities), 100)

    def test_coal_heavy_region(self):
        """Test coal-heavy region has higher day intensity."""
        region_data = self.provider.get_region_data('APAC-AU')  # Coal heavy

        # Find day and night intensities
        day_intensities = [f.carbon_intensity_g_per_kwh for f in region_data.forecast_24h[9:17]]
        night_intensities = [f.carbon_intensity_g_per_kwh for f in region_data.forecast_24h[0:6]]

        # For coal heavy, day should be higher than night
        self.assertGreater(sum(day_intensities), sum(night_intensities))

    def test_region_name_mapping(self):
        """Test region name mapping."""
        region_data = self.provider.get_region_data('US-CA')
        self.assertIn('California', region_data.region_name)


class TestDeploymentOptimizer(unittest.TestCase):
    """Test cases for deployment optimizer."""

    def setUp(self):
        self.optimizer = DeploymentOptimizer()
        self.deployment = DeploymentConfig(
            deployment_id='deploy-123',
            target_region='US-CA',
            deployment_size_mb=500,
            estimated_duration_minutes=15,
            requires_downtime=False,
            auto_scaling_enabled=True,
            resource_requirements={'cpu_cores': 4, 'memory_gb': 8},
        )

    def test_deployment_energy_calculation(self):
        """Test deployment energy calculation."""
        energy = self.optimizer._calculate_deployment_energy(self.deployment)
        self.assertGreater(energy, 0)

    def test_analyze_deployment(self):
        """Test deployment analysis."""
        recommendation = self.optimizer.analyze_deployment(self.deployment)

        self.assertEqual(recommendation.region, 'US-CA')
        self.assertGreater(recommendation.carbon_intensity_g_per_kwh, 0)
        self.assertGreater(recommendation.estimated_emissions_kg_co2, 0)
        self.assertGreaterEqual(recommendation.confidence, 0)
        self.assertLessEqual(recommendation.confidence, 1)

    def test_optimal_time_selection(self):
        """Test optimal time selection."""
        recommendation = self.optimizer.analyze_deployment(self.deployment)

        # Recommended time should be in the future
        recommended_dt = datetime.fromisoformat(recommendation.recommended_time)
        self.assertGreater(recommended_dt, datetime.utcnow())

    def test_savings_calculation(self):
        """Test savings calculation."""
        recommendation = self.optimizer.analyze_deployment(self.deployment)

        # Savings should be non-negative
        self.assertGreaterEqual(recommendation.estimated_savings_kg_co2, 0)
        self.assertGreaterEqual(recommendation.savings_percentage, 0)

    def test_alternative_regions(self):
        """Test alternative region suggestions."""
        recommendation = self.optimizer.analyze_deployment(self.deployment)

        # Should have alternative regions
        self.assertGreater(len(recommendation.alternative_regions), 0)

        # All alternatives should have lower intensity than current
        for alt in recommendation.alternative_regions:
            self.assertLess(
                alt['current_intensity'],
                recommendation.carbon_intensity_g_per_kwh
            )

    def test_auto_scaling_recommendations(self):
        """Test auto-scaling recommendations."""
        deployment_no_scaling = DeploymentConfig(
            deployment_id='deploy-124',
            target_region='US-CA',
            deployment_size_mb=500,
            estimated_duration_minutes=15,
            requires_downtime=False,
            auto_scaling_enabled=False,
            resource_requirements={'cpu_cores': 4, 'memory_gb': 8},
        )
        recommendation = self.optimizer.analyze_deployment(deployment_no_scaling)

        # Should have recommendations
        self.assertGreater(len(recommendation.auto_scaling_recommendations), 0)

    def test_cleanup_recommendations(self):
        """Test resource cleanup recommendations."""
        recommendation = self.optimizer.analyze_deployment(self.deployment)

        # Should have cleanup recommendations
        self.assertGreater(len(recommendation.resource_cleanup_recommendations), 0)

    def test_different_regions_different_recommendations(self):
        """Test that different regions get different recommendations."""
        # Test with low-carbon region
        deployment_fr = DeploymentConfig(
            deployment_id='deploy-fr',
            target_region='EU-FR',
            deployment_size_mb=500,
            estimated_duration_minutes=15,
            requires_downtime=False,
            auto_scaling_enabled=True,
            resource_requirements={'cpu_cores': 4, 'memory_gb': 8},
        )

        rec_ca = self.optimizer.analyze_deployment(self.deployment)
        rec_fr = self.optimizer.analyze_deployment(deployment_fr)

        # France should have lower emissions
        self.assertLess(
            rec_fr.estimated_emissions_kg_co2,
            rec_ca.estimated_emissions_kg_co2
        )

    def test_downtime_affects_recommendations(self):
        """Test that downtime requirement affects recommendations."""
        deployment_downtime = DeploymentConfig(
            deployment_id='deploy-downtime',
            target_region='US-CA',
            deployment_size_mb=500,
            estimated_duration_minutes=15,
            requires_downtime=True,  # Requires downtime
            auto_scaling_enabled=True,
            resource_requirements={'cpu_cores': 4, 'memory_gb': 8},
        )

        recommendation = self.optimizer.analyze_deployment(deployment_downtime)

        # Should have downtime-related recommendations
        downtime_recs = [r for r in recommendation.auto_scaling_recommendations 
                        if 'low-traffic' in r.lower()]
        self.assertGreater(len(downtime_recs), 0)


if __name__ == '__main__':
    unittest.main()
