"""GitLab integration for Eco-Friendly Deployment Agent.

Handles interaction with GitLab API for deployment recommendations.
"""

import os
import json
from typing import List, Dict, Any, Optional
from eco_friendly_deployment import (
    DeploymentOptimizer,
    DeploymentConfig,
    CarbonIntensityProvider,
    format_recommendation,
)


class GitLabDeploymentAPI:
    """Handles GitLab API interactions for deployments."""

    def __init__(self, project_id: str, token: Optional[str] = None):
        self.project_id = project_id
        self.token = token or os.getenv('GITLAB_TOKEN')
        self.api_url = os.getenv('CI_API_V4_URL', 'https://gitlab.com/api/v4')

    def post_deployment_comment(self, deployment_id: str, comment: str) -> bool:
        """Post a comment on a deployment.
        
        In production, would call:
        POST /projects/{id}/deployments/{deployment_id}/notes
        """
        print(f"[Deployment {deployment_id}] Comment: {comment}")
        return True

    def create_issue(self, title: str, description: str, labels: List[str]) -> bool:
        """Create a new issue in the project."""
        print(f"[Issue] {title}")
        print(f"Description: {description}")
        print(f"Labels: {labels}")
        return True

    def update_deployment_status(self, deployment_id: str, status: str) -> bool:
        """Update deployment status.
        
        In production, would call:
        PUT /projects/{id}/deployments/{deployment_id}
        """
        print(f"[Deployment {deployment_id}] Status: {status}")
        return True


class EcoFriendlyDeploymentAgent:
    """Main agent for eco-friendly deployment optimization."""

    def __init__(self, project_id: str):
        self.project_id = project_id
        self.gitlab_api = GitLabDeploymentAPI(project_id)
        self.optimizer = DeploymentOptimizer(CarbonIntensityProvider())

    def analyze_deployment(self, deployment: DeploymentConfig) -> None:
        """Analyze deployment and provide recommendations.
        
        Args:
            deployment: Deployment configuration
        """
        # Analyze deployment
        recommendation = self.optimizer.analyze_deployment(deployment)

        # Generate formatted report
        report = format_recommendation(recommendation)

        # Post comment to deployment
        self.gitlab_api.post_deployment_comment(deployment.deployment_id, report)

        # Create issue if significant savings possible
        if recommendation.savings_percentage > 30:
            self._create_optimization_issue(deployment, recommendation)

        # Log metrics for dashboard
        self._log_metrics(deployment, recommendation)

    def _create_optimization_issue(self, deployment: DeploymentConfig,
                                  recommendation) -> None:
        """Create issue for significant optimization opportunity."""
        title = f"🌱 Deployment Optimization: {recommendation.savings_percentage:.0f}% CO₂ Savings Possible"
        description = f"""
## Deployment Optimization Opportunity

**Deployment ID:** {deployment.deployment_id}
**Target Region:** {deployment.target_region}

### Recommendation

**Optimal Time:** {recommendation.recommended_time}
**Estimated Savings:** {recommendation.estimated_savings_kg_co2:.4f} kg CO₂e ({recommendation.savings_percentage:.1f}%)

### Details

{recommendation.reason}

### Alternative Regions

"""
        for alt in recommendation.alternative_regions:
            description += f"- **{alt['region_name']}**: {alt['estimated_savings_kg_co2']:.4f} kg CO₂e savings\n"

        description += "\n### Next Steps\n\n"
        description += "1. Review the recommended deployment time\n"
        description += "2. Consider alternative regions if applicable\n"
        description += "3. Implement auto-scaling recommendations\n"
        description += "4. Schedule deployment at optimal time\n"

        labels = ['deployment', 'optimization', 'eco-friendly']
        self.gitlab_api.create_issue(title, description, labels)

    def _log_metrics(self, deployment: DeploymentConfig, recommendation) -> None:
        """Log metrics for dashboard aggregation.
        
        In production, would write to a metrics file or database.
        """
        metrics_entry = {
            'deployment_id': deployment.deployment_id,
            'timestamp': recommendation.recommended_time,
            'region': deployment.target_region,
            'estimated_emissions_kg_co2': recommendation.estimated_emissions_kg_co2,
            'estimated_savings_kg_co2': recommendation.estimated_savings_kg_co2,
            'savings_percentage': recommendation.savings_percentage,
            'carbon_intensity': recommendation.carbon_intensity_g_per_kwh,
        }
        print(f"[Metrics] {json.dumps(metrics_entry)}")


def main():
    """Main entry point for the agent."""
    # Get environment variables
    project_id = os.getenv('CI_PROJECT_ID', '80410036')
    deployment_id = os.getenv('CI_DEPLOYMENT_ID', 'deploy-123')
    target_region = os.getenv('DEPLOYMENT_REGION', 'US-CA')

    # Create deployment config
    deployment = DeploymentConfig(
        deployment_id=deployment_id,
        target_region=target_region,
        deployment_size_mb=500,
        estimated_duration_minutes=15,
        requires_downtime=False,
        auto_scaling_enabled=True,
        resource_requirements={'cpu_cores': 4, 'memory_gb': 8},
    )

    agent = EcoFriendlyDeploymentAgent(project_id)
    agent.analyze_deployment(deployment)


if __name__ == '__main__':
    main()
