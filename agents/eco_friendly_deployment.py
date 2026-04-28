"""Eco-Friendly Deployment Agent for EcoGuard.

Optimizes deployments for minimal environmental impact.
"""

import os
import json
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
import statistics


@dataclass
class CarbonIntensityForecast:
    """Represents carbon intensity forecast data."""
    timestamp: str
    carbon_intensity_g_per_kwh: float
    is_renewable_heavy: bool
    confidence: float  # 0-1, confidence in forecast


@dataclass
class RegionData:
    """Represents data for a deployment region."""
    region_code: str
    region_name: str
    current_intensity_g_per_kwh: float
    avg_intensity_g_per_kwh: float
    forecast_24h: List[CarbonIntensityForecast]
    auto_scaling_enabled: bool
    current_load_percent: float
    estimated_deployment_energy_kwh: float


@dataclass
class DeploymentConfig:
    """Represents deployment configuration."""
    deployment_id: str
    target_region: str
    deployment_size_mb: float
    estimated_duration_minutes: int
    requires_downtime: bool
    auto_scaling_enabled: bool
    resource_requirements: Dict[str, float]  # cpu_cores, memory_gb, etc.


@dataclass
class DeploymentRecommendation:
    """Represents a deployment recommendation."""
    region: str
    recommended_time: str
    carbon_intensity_g_per_kwh: float
    estimated_emissions_kg_co2: float
    estimated_savings_kg_co2: float
    savings_percentage: float
    confidence: float
    reason: str
    alternative_regions: List[Dict[str, Any]] = field(default_factory=list)
    auto_scaling_recommendations: List[str] = field(default_factory=list)
    resource_cleanup_recommendations: List[str] = field(default_factory=list)


class CarbonIntensityProvider:
    """Provides carbon intensity data and forecasts."""

    # Default carbon intensity values for regions (gCO₂/kWh)
    DEFAULT_INTENSITIES = {
        'US-CA': {'current': 150, 'avg': 180, 'renewable_heavy': True},
        'US-TX': {'current': 400, 'avg': 420, 'renewable_heavy': False},
        'US-NY': {'current': 200, 'avg': 220, 'renewable_heavy': True},
        'US-VA': {'current': 350, 'avg': 370, 'renewable_heavy': False},
        'EU-DE': {'current': 380, 'avg': 400, 'renewable_heavy': True},
        'EU-GB': {'current': 250, 'avg': 280, 'renewable_heavy': True},
        'EU-FR': {'current': 50, 'avg': 60, 'renewable_heavy': True},
        'EU-NO': {'current': 20, 'avg': 25, 'renewable_heavy': True},
        'IN': {'current': 700, 'avg': 720, 'renewable_heavy': False},
        'APAC-SG': {'current': 450, 'avg': 480, 'renewable_heavy': False},
        'APAC-AU': {'current': 600, 'avg': 620, 'renewable_heavy': False},
    }

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('ELECTRICITY_MAPS_API_KEY')

    def get_region_data(self, region_code: str) -> RegionData:
        """Get current and forecast data for a region.
        
        Args:
            region_code: Region code (e.g., 'US-CA', 'EU-DE')
            
        Returns:
            RegionData with current and forecast information
        """
        intensity_data = self.DEFAULT_INTENSITIES.get(
            region_code,
            {'current': 300, 'avg': 320, 'renewable_heavy': False}
        )

        # Generate 24-hour forecast
        forecast = self._generate_forecast(region_code, intensity_data)

        region_name = self._get_region_name(region_code)

        return RegionData(
            region_code=region_code,
            region_name=region_name,
            current_intensity_g_per_kwh=intensity_data['current'],
            avg_intensity_g_per_kwh=intensity_data['avg'],
            forecast_24h=forecast,
            auto_scaling_enabled=True,
            current_load_percent=45.0,  # Mock value
            estimated_deployment_energy_kwh=0.0,  # Will be calculated
        )

    def _generate_forecast(self, region_code: str, 
                          intensity_data: Dict[str, Any]) -> List[CarbonIntensityForecast]:
        """Generate 24-hour carbon intensity forecast."""
        forecast = []
        base_intensity = intensity_data['current']
        is_renewable = intensity_data['renewable_heavy']

        # Simulate hourly forecast with variations
        for hour in range(24):
            # Renewable-heavy regions have lower intensity at night (less solar)
            # Coal-heavy regions have lower intensity at night (less demand)
            if is_renewable:
                # Solar generation peaks at noon, drops at night
                if 6 <= hour <= 18:
                    variation = 1.0 + (0.3 * ((hour - 12) ** 2 / 36))  # Peak at noon
                else:
                    variation = 1.2  # Higher at night (less solar)
            else:
                # Demand-based variation
                if 9 <= hour <= 17:
                    variation = 1.1  # Higher during day
                else:
                    variation = 0.9  # Lower at night

            intensity = base_intensity * variation
            timestamp = (datetime.utcnow() + timedelta(hours=hour)).isoformat()

            forecast.append(CarbonIntensityForecast(
                timestamp=timestamp,
                carbon_intensity_g_per_kwh=intensity,
                is_renewable_heavy=is_renewable,
                confidence=0.95 - (hour * 0.01),  # Confidence decreases over time
            ))

        return forecast

    def _get_region_name(self, region_code: str) -> str:
        """Get human-readable region name."""
        names = {
            'US-CA': 'US - California',
            'US-TX': 'US - Texas',
            'US-NY': 'US - New York',
            'US-VA': 'US - Virginia',
            'EU-DE': 'Europe - Germany',
            'EU-GB': 'Europe - UK',
            'EU-FR': 'Europe - France',
            'EU-NO': 'Europe - Norway',
            'APAC-SG': 'Asia Pacific - Singapore',
            'APAC-AU': 'Asia Pacific - Australia',
        }
        return names.get(region_code, region_code)


class DeploymentOptimizer:
    """Optimizes deployment timing and configuration."""

    # Energy consumption model (simplified)
    ENERGY_PER_MB = 0.0001  # kWh per MB deployed
    ENERGY_PER_MINUTE = 0.01  # kWh per minute of deployment

    def __init__(self, carbon_provider: Optional[CarbonIntensityProvider] = None):
        self.carbon_provider = carbon_provider or CarbonIntensityProvider()

    def analyze_deployment(self, deployment: DeploymentConfig) -> DeploymentRecommendation:
        """Analyze deployment and provide recommendations.
        
        Args:
            deployment: Deployment configuration
            
        Returns:
            DeploymentRecommendation with optimal timing and alternatives
        """
        # Get data for target region
        target_region_data = self.carbon_provider.get_region_data(deployment.target_region)

        # Calculate deployment energy
        deployment_energy_kwh = self._calculate_deployment_energy(deployment)
        target_region_data.estimated_deployment_energy_kwh = deployment_energy_kwh

        # Find optimal deployment time in target region
        optimal_time, optimal_intensity = self._find_optimal_time(
            target_region_data.forecast_24h
        )

        # Calculate emissions for optimal time
        optimal_emissions = deployment_energy_kwh * optimal_intensity / 1000

        # Calculate emissions for current time
        current_emissions = deployment_energy_kwh * target_region_data.current_intensity_g_per_kwh / 1000

        # Calculate savings
        savings_kg_co2 = current_emissions - optimal_emissions
        savings_pct = (savings_kg_co2 / current_emissions * 100) if current_emissions > 0 else 0

        # Find alternative regions
        alternative_regions = self._find_alternative_regions(
            deployment.target_region,
            deployment_energy_kwh
        )

        # Generate auto-scaling recommendations
        auto_scaling_recs = self._generate_auto_scaling_recommendations(
            target_region_data,
            deployment
        )

        # Generate resource cleanup recommendations
        cleanup_recs = self._generate_cleanup_recommendations(deployment)

        # Determine confidence based on forecast
        confidence = statistics.mean([f.confidence for f in target_region_data.forecast_24h[:6]])

        return DeploymentRecommendation(
            region=deployment.target_region,
            recommended_time=optimal_time,
            carbon_intensity_g_per_kwh=optimal_intensity,
            estimated_emissions_kg_co2=optimal_emissions,
            estimated_savings_kg_co2=savings_kg_co2,
            savings_percentage=savings_pct,
            confidence=confidence,
            reason=self._generate_reason(deployment, optimal_time, savings_pct),
            alternative_regions=alternative_regions,
            auto_scaling_recommendations=auto_scaling_recs,
            resource_cleanup_recommendations=cleanup_recs,
        )

    def _calculate_deployment_energy(self, deployment: DeploymentConfig) -> float:
        """Calculate estimated energy for deployment."""
        # Energy from data transfer
        transfer_energy = deployment.deployment_size_mb * self.ENERGY_PER_MB

        # Energy from deployment process
        process_energy = deployment.estimated_duration_minutes * self.ENERGY_PER_MINUTE

        # Add resource-specific energy
        resource_energy = sum(deployment.resource_requirements.values()) * 0.001

        return transfer_energy + process_energy + resource_energy

    def _find_optimal_time(self, forecast: List[CarbonIntensityForecast]) -> Tuple[str, float]:
        """Find optimal deployment time with lowest carbon intensity."""
        if not forecast:
            return datetime.utcnow().isoformat(), 300.0

        # Find hour with lowest intensity
        optimal = min(forecast, key=lambda f: f.carbon_intensity_g_per_kwh)
        return optimal.timestamp, optimal.carbon_intensity_g_per_kwh

    def _find_alternative_regions(self, current_region: str,
                                 deployment_energy_kwh: float) -> List[Dict[str, Any]]:
        """Find alternative regions with lower carbon intensity."""
        alternatives = []
        current_data = self.carbon_provider.get_region_data(current_region)
        current_intensity = current_data.current_intensity_g_per_kwh

        # Check all regions
        for region_code in self.carbon_provider.DEFAULT_INTENSITIES.keys():
            if region_code == current_region:
                continue

            region_data = self.carbon_provider.get_region_data(region_code)
            region_intensity = region_data.current_intensity_g_per_kwh

            # Only suggest regions with lower intensity
            if region_intensity < current_intensity:
                emissions_current = deployment_energy_kwh * current_intensity / 1000
                emissions_alternative = deployment_energy_kwh * region_intensity / 1000
                savings = emissions_current - emissions_alternative
                savings_pct = (savings / emissions_current * 100) if emissions_current > 0 else 0

                alternatives.append({
                    'region': region_code,
                    'region_name': region_data.region_name,
                    'current_intensity': region_intensity,
                    'estimated_emissions_kg_co2': emissions_alternative,
                    'estimated_savings_kg_co2': savings,
                    'savings_percentage': savings_pct,
                })

        # Sort by savings and return top 3
        alternatives.sort(key=lambda x: x['estimated_savings_kg_co2'], reverse=True)
        return alternatives[:3]

    def _generate_auto_scaling_recommendations(self, region_data: RegionData,
                                              deployment: DeploymentConfig) -> List[str]:
        """Generate auto-scaling recommendations."""
        recommendations = []

        if not deployment.auto_scaling_enabled:
            recommendations.append(
                '✅ Enable auto-scaling to reduce idle resource consumption'
            )

        if region_data.current_load_percent > 80:
            recommendations.append(
                f'⚠️ Current load is {region_data.current_load_percent:.0f}%. '
                'Consider scaling up before deployment to avoid overload'
            )
        elif region_data.current_load_percent < 20:
            recommendations.append(
                f'💡 Current load is only {region_data.current_load_percent:.0f}%. '
                'Consider scaling down idle resources after deployment'
            )

        if deployment.requires_downtime:
            recommendations.append(
                '🔄 Schedule deployment during low-traffic hours to minimize impact'
            )

        return recommendations

    def _generate_cleanup_recommendations(self, deployment: DeploymentConfig) -> List[str]:
        """Generate resource cleanup recommendations."""
        recommendations = []

        recommendations.append(
            '🧹 Remove old container images and unused dependencies after deployment'
        )
        recommendations.append(
            '📦 Clean up temporary files and build artifacts'
        )
        recommendations.append(
            '🗑️ Terminate unused instances and scale down over-provisioned resources'
        )
        recommendations.append(
            '💾 Archive old logs and database backups to cold storage'
        )

        return recommendations

    def _generate_reason(self, deployment: DeploymentConfig, optimal_time: str,
                        savings_pct: float) -> str:
        """Generate human-readable reason for recommendation."""
        if savings_pct > 50:
            return f'Deploying at {optimal_time} will reduce emissions by {savings_pct:.1f}% compared to now'
        elif savings_pct > 20:
            return f'Optimal time {optimal_time} offers {savings_pct:.1f}% lower carbon intensity'
        elif savings_pct > 0:
            return f'Slight improvement ({savings_pct:.1f}%) by deploying at {optimal_time}'
        else:
            return 'Current time is optimal for deployment'


def format_recommendation(rec: DeploymentRecommendation) -> str:
    """Format recommendation for display."""
    report = f"""
## 🌍 EcoGuard Eco-Friendly Deployment Recommendation

### Recommended Deployment Time

**Time:** {rec.recommended_time}
**Region:** {rec.region}
**Carbon Intensity:** {rec.carbon_intensity_g_per_kwh:.0f} gCO₂/kWh

### Environmental Impact

| Metric | Value |
|--------|-------|
| **Estimated Emissions** | {rec.estimated_emissions_kg_co2:.4f} kg CO₂e |
| **Estimated Savings** | {rec.estimated_savings_kg_co2:.4f} kg CO₂e ({rec.savings_percentage:.1f}%) |
| **Forecast Confidence** | {rec.confidence*100:.0f}% |

### Reason

{rec.reason}

"""

    if rec.alternative_regions:
        report += "### Alternative Regions\n\n"
        for alt in rec.alternative_regions:
            report += f"- **{alt['region_name']}** ({alt['region']}): "
            report += f"{alt['estimated_savings_kg_co2']:.4f} kg CO₂e savings ({alt['savings_percentage']:.1f}%)\n"
        report += "\n"

    if rec.auto_scaling_recommendations:
        report += "### Auto-Scaling Recommendations\n\n"
        for rec_item in rec.auto_scaling_recommendations:
            report += f"- {rec_item}\n"
        report += "\n"

    if rec.resource_cleanup_recommendations:
        report += "### Resource Cleanup\n\n"
        for rec_item in rec.resource_cleanup_recommendations:
            report += f"- {rec_item}\n"
        report += "\n"

    report += "---\n"
    report += "*Recommendation generated by EcoGuard Eco-Friendly Deployment Agent*\n"

    return report


if __name__ == '__main__':
    # Example usage
    deployment = DeploymentConfig(
        deployment_id='deploy-123',
        target_region='US-CA',
        deployment_size_mb=500,
        estimated_duration_minutes=15,
        requires_downtime=False,
        auto_scaling_enabled=True,
        resource_requirements={'cpu_cores': 4, 'memory_gb': 8},
    )

    optimizer = DeploymentOptimizer()
    recommendation = optimizer.analyze_deployment(deployment)

    print(json.dumps({
        'region': recommendation.region,
        'recommended_time': recommendation.recommended_time,
        'carbon_intensity': recommendation.carbon_intensity_g_per_kwh,
        'estimated_emissions_kg_co2': recommendation.estimated_emissions_kg_co2,
        'estimated_savings_kg_co2': recommendation.estimated_savings_kg_co2,
        'savings_percentage': recommendation.savings_percentage,
        'confidence': recommendation.confidence,
    }, indent=2))
    print(format_recommendation(recommendation))
