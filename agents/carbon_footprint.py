"""Carbon Footprint Agent for EcoGuard.

Calculates CI/CD pipeline energy usage and CO₂ emissions.
Uses real Electricity Maps API for carbon intensity data.
"""

import os
import json
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from datetime import datetime
import requests


@dataclass
class JobMetrics:
    """Represents metrics for a single job."""
    job_id: str
    job_name: str
    duration_seconds: float
    cpu_cores: int
    memory_mb: float
    status: str  # 'success', 'failed'


@dataclass
class EnergyCalculation:
    """Represents energy calculation results."""
    cpu_energy_wh: float
    memory_energy_wh: float
    total_energy_wh: float
    total_energy_kwh: float
    carbon_intensity_g_per_kwh: float
    total_emissions_g_co2: float
    total_emissions_kg_co2: float


# Mapping from simple zone codes to Electricity Maps zone keys
ZONE_MAPPING = {
    'US-CA': 'US-CAL-CISO',
    'US-TX': 'US-TEX-ERCO',
    'US-NY': 'US-NY-NYIS',
    'DE': 'DE',
    'GB': 'GB',
    'FR': 'FR',
    'NO': 'NO-NO1',
    'AU': 'AU-NSW',
    'IN': 'IN-WE',
    'SG': 'SG',
}


class CarbonIntensityProvider:
    """Fetches carbon intensity data from Electricity Maps API."""

    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv('ELECTRICITY_MAPS_API_KEY')
        self.base_url = 'https://api.electricitymap.org/v3'
        self.cache = {}  # Simple cache for zone data

    def _resolve_zone(self, zone: str) -> str:
        """Resolve a simple zone code to an Electricity Maps zone key."""
        return ZONE_MAPPING.get(zone, zone)

    def get_carbon_intensity(self, zone: str = 'US-CA') -> float:
        """Get current carbon intensity for a region in gCO₂/kWh.
        
        Args:
            zone: Region code (e.g., 'US-CA', 'DE', 'GB')
            
        Returns:
            Carbon intensity in gCO₂/kWh
        """
        resolved_zone = self._resolve_zone(zone)

        # Check cache first
        if resolved_zone in self.cache:
            return self.cache[resolved_zone]

        # Default values if API unavailable
        default_intensities = {
            'US-CAL-CISO': 150,
            'US-TEX-ERCO': 400,
            'US-NY-NYIS': 200,
            'DE': 380,
            'GB': 250,
            'FR': 50,
            'NO-NO1': 20,
            'AU-NSW': 600,
            'IN-WE': 700,
            'SG': 450,
        }

        if not self.api_key:
            # Return default if no API key
            print(f"  ⚠️  No ELECTRICITY_MAPS_API_KEY set, using default for {zone}")
            return default_intensities.get(resolved_zone, 300)

        try:
            response = requests.get(
                f'{self.base_url}/carbon-intensity/latest',
                params={'zone': resolved_zone},
                headers={'auth-token': self.api_key},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                intensity = data.get('carbonIntensity', 300)
                self.cache[resolved_zone] = intensity
                print(f"  ✅ Real carbon intensity for {zone} ({resolved_zone}): {intensity} gCO₂/kWh")
                return intensity
            else:
                print(f"  ⚠️  Electricity Maps API returned {response.status_code} for zone {resolved_zone}: {response.text[:200]}")
                return default_intensities.get(resolved_zone, 300)
                
        except Exception as e:
            print(f"  ⚠️  Error fetching carbon intensity: {e}")
            return default_intensities.get(resolved_zone, 300)

    def get_forecast(self, zone: str = 'US-CA') -> List[Dict[str, Any]]:
        """Get carbon intensity forecast.
        
        Returns:
            List of hourly forecasts with timestamp and intensity
        """
        resolved_zone = self._resolve_zone(zone)
        
        if not self.api_key:
            return self._mock_forecast()

        try:
            response = requests.get(
                f'{self.base_url}/carbon-intensity/forecast',
                params={'zone': resolved_zone},
                headers={'auth-token': self.api_key},
                timeout=10
            )
            
            if response.status_code == 200:
                data = response.json()
                forecast_data = data.get('forecast', [])
                print(f"  ✅ Got {len(forecast_data)} forecast entries for {zone}")
                return [
                    {
                        'timestamp': entry.get('datetime', ''),
                        'intensity': entry.get('carbonIntensity', 300)
                    }
                    for entry in forecast_data[:24]  # First 24 hours
                ]
            else:
                print(f"  ⚠️  Forecast API returned {response.status_code}")
                return self._mock_forecast()
                
        except Exception as e:
            print(f"  ⚠️  Error fetching forecast: {e}")
            return self._mock_forecast()

    def _mock_forecast(self) -> List[Dict[str, Any]]:
        """Fallback mock forecast data."""
        return [
            {'timestamp': '2024-03-19T12:00Z', 'intensity': 150},
            {'timestamp': '2024-03-19T13:00Z', 'intensity': 145},
            {'timestamp': '2024-03-19T14:00Z', 'intensity': 140},
        ]

    def get_multiple_zones(self, zones: List[str]) -> Dict[str, float]:
        """Get carbon intensity for multiple zones at once."""
        results = {}
        for zone in zones:
            results[zone] = self.get_carbon_intensity(zone)
        return results


class EnergyCalculator:
    """Calculates energy consumption and CO₂ emissions."""

    # Default power consumption values
    CPU_WATTS_PER_CORE = 30  # Watts per CPU core
    MEMORY_WATTS_PER_GB = 0.5  # Watts per GB of RAM

    def __init__(self, carbon_provider: Optional[CarbonIntensityProvider] = None):
        self.carbon_provider = carbon_provider or CarbonIntensityProvider()

    def calculate_job_energy(self, job: JobMetrics, zone: str = 'US-CA') -> EnergyCalculation:
        """Calculate energy and emissions for a single job.
        
        Args:
            job: Job metrics
            zone: Region for carbon intensity lookup
            
        Returns:
            EnergyCalculation with detailed breakdown
        """
        # Convert duration to hours
        duration_hours = job.duration_seconds / 3600

        # Calculate CPU energy (Wh)
        cpu_energy_wh = job.cpu_cores * self.CPU_WATTS_PER_CORE * duration_hours

        # Calculate memory energy (Wh)
        memory_gb = job.memory_mb / 1024
        memory_energy_wh = memory_gb * self.MEMORY_WATTS_PER_GB * duration_hours

        # Total energy
        total_energy_wh = cpu_energy_wh + memory_energy_wh
        total_energy_kwh = total_energy_wh / 1000

        # Get carbon intensity
        carbon_intensity = self.carbon_provider.get_carbon_intensity(zone)

        # Calculate CO₂ emissions
        total_emissions_g_co2 = total_energy_kwh * carbon_intensity
        total_emissions_kg_co2 = total_emissions_g_co2 / 1000

        return EnergyCalculation(
            cpu_energy_wh=cpu_energy_wh,
            memory_energy_wh=memory_energy_wh,
            total_energy_wh=total_energy_wh,
            total_energy_kwh=total_energy_kwh,
            carbon_intensity_g_per_kwh=carbon_intensity,
            total_emissions_g_co2=total_emissions_g_co2,
            total_emissions_kg_co2=total_emissions_kg_co2
        )

    def calculate_pipeline_energy(self, jobs: List[JobMetrics], 
                                 zone: str = 'US-CA') -> Tuple[EnergyCalculation, Dict[str, EnergyCalculation]]:
        """Calculate total energy and emissions for a pipeline.
        
        Args:
            jobs: List of job metrics
            zone: Region for carbon intensity lookup
            
        Returns:
            Tuple of (total calculation, per-job calculations)
        """
        job_calculations = {}
        total_energy_wh = 0
        total_emissions_g = 0

        for job in jobs:
            calc = self.calculate_job_energy(job, zone)
            job_calculations[job.job_id] = calc
            total_energy_wh += calc.total_energy_wh
            total_emissions_g += calc.total_emissions_g_co2

        total_energy_kwh = total_energy_wh / 1000
        total_emissions_kg = total_emissions_g / 1000
        carbon_intensity = self.carbon_provider.get_carbon_intensity(zone)

        total_calc = EnergyCalculation(
            cpu_energy_wh=sum(c.cpu_energy_wh for c in job_calculations.values()),
            memory_energy_wh=sum(c.memory_energy_wh for c in job_calculations.values()),
            total_energy_wh=total_energy_wh,
            total_energy_kwh=total_energy_kwh,
            carbon_intensity_g_per_kwh=carbon_intensity,
            total_emissions_g_co2=total_emissions_g,
            total_emissions_kg_co2=total_emissions_kg
        )

        return total_calc, job_calculations


class CarbonFootprintAnalyzer:
    """Analyzes pipeline carbon footprint and provides recommendations."""

    def __init__(self, carbon_provider: Optional[CarbonIntensityProvider] = None):
        self.calculator = EnergyCalculator(carbon_provider)
        self.baseline_kwh = 5.0  # Default baseline for comparison
        self.baseline_kg_co2 = 2.0

    def set_baseline(self, kwh: float, kg_co2: float) -> None:
        """Set baseline for comparison."""
        self.baseline_kwh = kwh
        self.baseline_kg_co2 = kg_co2

    def analyze_pipeline(self, jobs: List[JobMetrics], 
                        zone: str = 'US-CA') -> Dict[str, Any]:
        """Analyze pipeline and generate report.
        
        Args:
            jobs: List of job metrics
            zone: Region for carbon intensity lookup
            
        Returns:
            Analysis report with metrics and recommendations
        """
        total_calc, job_calcs = self.calculator.calculate_pipeline_energy(jobs, zone)

        # Calculate comparison to baseline
        energy_diff = total_calc.total_energy_kwh - self.baseline_kwh
        energy_diff_pct = (energy_diff / self.baseline_kwh * 100) if self.baseline_kwh > 0 else 0
        emissions_diff = total_calc.total_emissions_kg_co2 - self.baseline_kg_co2
        emissions_diff_pct = (emissions_diff / self.baseline_kg_co2 * 100) if self.baseline_kg_co2 > 0 else 0

        # Generate recommendations
        recommendations = self._generate_recommendations(jobs, job_calcs, total_calc)

        # Find heaviest jobs
        heaviest_jobs = sorted(
            job_calcs.items(),
            key=lambda x: x[1].total_energy_kwh,
            reverse=True
        )[:3]

        return {
            'timestamp': datetime.utcnow().isoformat(),
            'total_jobs': len(jobs),
            'successful_jobs': len([j for j in jobs if j.status == 'success']),
            'failed_jobs': len([j for j in jobs if j.status == 'failed']),
            'energy': {
                'total_kwh': round(total_calc.total_energy_kwh, 4),
                'cpu_kwh': round(total_calc.cpu_energy_wh / 1000, 4),
                'memory_kwh': round(total_calc.memory_energy_wh / 1000, 4),
                'baseline_kwh': self.baseline_kwh,
                'difference_kwh': round(energy_diff, 4),
                'difference_pct': round(energy_diff_pct, 2),
            },
            'emissions': {
                'total_kg_co2': round(total_calc.total_emissions_kg_co2, 4),
                'total_g_co2': round(total_calc.total_emissions_g_co2, 2),
                'baseline_kg_co2': self.baseline_kg_co2,
                'difference_kg_co2': round(emissions_diff, 4),
                'difference_pct': round(emissions_diff_pct, 2),
            },
            'carbon_intensity': {
                'zone': zone,
                'g_per_kwh': total_calc.carbon_intensity_g_per_kwh,
            },
            'heaviest_jobs': [
                {
                    'job_id': job_id,
                    'energy_kwh': round(calc.total_energy_kwh, 4),
                    'emissions_kg_co2': round(calc.total_emissions_kg_co2, 4),
                }
                for job_id, calc in heaviest_jobs
            ],
            'recommendations': recommendations,
        }

    def _generate_recommendations(self, jobs: List[JobMetrics],
                                 job_calcs: Dict[str, EnergyCalculation],
                                 total_calc: EnergyCalculation) -> List[str]:
        """Generate optimization recommendations."""
        recommendations = []

        # Check if energy is above baseline
        if total_calc.total_energy_kwh > self.baseline_kwh * 1.2:
            recommendations.append(
                f"⚠️ Pipeline energy ({total_calc.total_energy_kwh:.2f} kWh) is 20% above baseline. "
                "Consider optimizing job parallelization or resource allocation."
            )

        # Check for long-running jobs
        long_jobs = [j for j in jobs if j.duration_seconds > 600]  # > 10 minutes
        if long_jobs:
            recommendations.append(
                f"⏱️ Found {len(long_jobs)} job(s) running longer than 10 minutes. "
                "Consider splitting into smaller tasks or enabling caching."
            )

        # Check memory usage
        high_memory_jobs = [j for j in jobs if j.memory_mb > 2048]  # > 2GB
        if high_memory_jobs:
            recommendations.append(
                f"💾 Found {len(high_memory_jobs)} job(s) using >2GB memory. "
                "Review memory allocation and consider optimization."
            )

        # Check CPU cores
        high_cpu_jobs = [j for j in jobs if j.cpu_cores > 4]
        if high_cpu_jobs:
            recommendations.append(
                f"⚙️ Found {len(high_cpu_jobs)} job(s) using >4 CPU cores. "
                "Verify parallelization is necessary and efficient."
            )

        # Check for failed jobs
        failed_jobs = [j for j in jobs if j.status == 'failed']
        if failed_jobs:
            recommendations.append(
                f"❌ {len(failed_jobs)} job(s) failed, wasting {sum(job_calcs[j.job_id].total_energy_kwh for j in failed_jobs):.2f} kWh. "
                "Fix failures to reduce wasted energy."
            )

        # Positive feedback
        if not recommendations:
            recommendations.append(
                "✅ Pipeline is running efficiently! Keep up the good work."
            )

        return recommendations


def format_report(analysis: Dict[str, Any]) -> str:
    """Format analysis report for display."""
    report = f"""
## 🌍 EcoGuard Carbon Footprint Report

**Pipeline Summary**
- Total Jobs: {analysis['total_jobs']}
- Successful: {analysis['successful_jobs']}
- Failed: {analysis['failed_jobs']}

### ⚡ Energy Consumption

| Metric | Value |
|--------|-------|
| **Total Energy** | {analysis['energy']['total_kwh']} kWh |
| CPU Energy | {analysis['energy']['cpu_kwh']} kWh |
| Memory Energy | {analysis['energy']['memory_kwh']} kWh |
| Baseline | {analysis['energy']['baseline_kwh']} kWh |
| Difference | {analysis['energy']['difference_kwh']} kWh ({analysis['energy']['difference_pct']:+.1f}%) |

### 🌱 CO₂ Emissions

| Metric | Value |
|--------|-------|
| **Total Emissions** | {analysis['emissions']['total_kg_co2']} kg CO₂e |
| Baseline | {analysis['emissions']['baseline_kg_co2']} kg CO₂e |
| Difference | {analysis['emissions']['difference_kg_co2']} kg CO₂e ({analysis['emissions']['difference_pct']:+.1f}%) |

### 📊 Carbon Intensity

- **Region**: {analysis['carbon_intensity']['zone']}
- **Intensity**: {analysis['carbon_intensity']['g_per_kwh']} gCO₂/kWh

### 🔥 Heaviest Jobs

"""

    for job in analysis['heaviest_jobs']:
        report += f"- **{job['job_id']}**: {job['energy_kwh']} kWh ({job['emissions_kg_co2']} kg CO₂e)\n"

    report += "\n### 💡 Recommendations\n\n"
    for rec in analysis['recommendations']:
        report += f"- {rec}\n"

    report += "\n---\n"
    report += "*Report generated by EcoGuard Carbon Footprint Agent*\n"

    return report


if __name__ == '__main__':
    # Example usage
    jobs = [
        JobMetrics('job-1', 'build', 300, 2, 1024, 'success'),
        JobMetrics('job-2', 'test', 600, 4, 2048, 'success'),
        JobMetrics('job-3', 'deploy', 120, 1, 512, 'success'),
    ]

    analyzer = CarbonFootprintAnalyzer()
    analysis = analyzer.analyze_pipeline(jobs, zone='US-CA')

    print(json.dumps(analysis, indent=2))
    print(format_report(analysis))
