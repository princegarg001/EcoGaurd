"""Resource Optimization Agent for EcoGuard.

Analyzes historical job metrics and identifies optimization opportunities.
"""

import os
import json
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from collections import defaultdict
import statistics


@dataclass
class JobMetric:
    """Represents a single job metric record."""
    job_id: str
    job_name: str
    timestamp: str
    duration_seconds: float
    cpu_cores: int
    cpu_usage_percent: float
    memory_mb: float
    memory_usage_percent: float
    status: str  # 'success', 'failed'
    run_count: int = 1  # How many times this job has run


@dataclass
class JobStatistics:
    """Statistics for a job type."""
    job_name: str
    run_count: int
    avg_duration_seconds: float
    min_duration_seconds: float
    max_duration_seconds: float
    avg_cpu_cores: float
    avg_cpu_usage_percent: float
    avg_memory_mb: float
    avg_memory_usage_percent: float
    success_rate: float
    total_energy_kwh: float = 0.0
    total_wasted_energy_kwh: float = 0.0  # Energy from failed runs


@dataclass
class OptimizationOpportunity:
    """Represents an optimization opportunity."""
    job_name: str
    issue_type: str  # 'high_cpu', 'high_memory', 'long_duration', 'low_success_rate', 'inefficient_parallelization'
    severity: str  # 'high', 'medium', 'low'
    description: str
    current_metric: float
    baseline_metric: float
    recommendations: List[str]
    estimated_savings_kwh: float
    estimated_savings_pct: float
    impact_score: float  # 0-100, based on frequency and resource usage


class MetricsAnalyzer:
    """Analyzes job metrics to identify patterns and opportunities."""

    # Thresholds for outlier detection
    CPU_OUTLIER_THRESHOLD = 2.0  # 2x average
    MEMORY_OUTLIER_THRESHOLD = 2.0  # 2x average
    DURATION_OUTLIER_THRESHOLD = 2.0  # 2x average
    MIN_SUCCESS_RATE = 0.95  # 95% success rate is acceptable
    MIN_CPU_UTILIZATION = 0.5  # 50% CPU utilization is acceptable
    MIN_MEMORY_UTILIZATION = 0.6  # 60% memory utilization is acceptable

    def __init__(self):
        self.metrics: List[JobMetric] = []
        self.job_stats: Dict[str, JobStatistics] = {}

    def add_metrics(self, metrics: List[JobMetric]) -> None:
        """Add metrics for analysis."""
        self.metrics.extend(metrics)

    def analyze(self) -> Tuple[Dict[str, JobStatistics], List[OptimizationOpportunity]]:
        """Analyze metrics and identify optimization opportunities.
        
        Returns:
            Tuple of (job statistics, optimization opportunities)
        """
        # Calculate statistics for each job
        self._calculate_job_statistics()

        # Identify optimization opportunities
        opportunities = self._identify_opportunities()

        # Sort by impact score
        opportunities.sort(key=lambda x: x.impact_score, reverse=True)

        return self.job_stats, opportunities

    def _calculate_job_statistics(self) -> None:
        """Calculate statistics for each job type."""
        job_metrics = defaultdict(list)

        # Group metrics by job name
        for metric in self.metrics:
            job_metrics[metric.job_name].append(metric)

        # Calculate statistics
        for job_name, metrics in job_metrics.items():
            durations = [m.duration_seconds for m in metrics]
            cpu_cores = [m.cpu_cores for m in metrics]
            cpu_usage = [m.cpu_usage_percent for m in metrics]
            memory_mb = [m.memory_mb for m in metrics]
            memory_usage = [m.memory_usage_percent for m in metrics]
            success_count = len([m for m in metrics if m.status == 'success'])

            # Calculate energy (simplified: 30W per core, 0.5W per GB)
            total_energy_kwh = sum(
                (m.cpu_cores * 30 + m.memory_mb / 1024 * 0.5) * (m.duration_seconds / 3600) / 1000
                for m in metrics
            )

            # Calculate wasted energy from failed runs
            failed_metrics = [m for m in metrics if m.status == 'failed']
            wasted_energy_kwh = sum(
                (m.cpu_cores * 30 + m.memory_mb / 1024 * 0.5) * (m.duration_seconds / 3600) / 1000
                for m in failed_metrics
            )

            self.job_stats[job_name] = JobStatistics(
                job_name=job_name,
                run_count=len(metrics),
                avg_duration_seconds=statistics.mean(durations),
                min_duration_seconds=min(durations),
                max_duration_seconds=max(durations),
                avg_cpu_cores=statistics.mean(cpu_cores),
                avg_cpu_usage_percent=statistics.mean(cpu_usage),
                avg_memory_mb=statistics.mean(memory_mb),
                avg_memory_usage_percent=statistics.mean(memory_usage),
                success_rate=success_count / len(metrics),
                total_energy_kwh=total_energy_kwh,
                total_wasted_energy_kwh=wasted_energy_kwh,
            )

    def _identify_opportunities(self) -> List[OptimizationOpportunity]:
        """Identify optimization opportunities based on statistics."""
        opportunities = []

        # Calculate global averages for comparison
        avg_duration = statistics.mean(
            [s.avg_duration_seconds for s in self.job_stats.values()]
        ) if self.job_stats else 0
        avg_cpu = statistics.mean(
            [s.avg_cpu_cores for s in self.job_stats.values()]
        ) if self.job_stats else 0
        avg_memory = statistics.mean(
            [s.avg_memory_mb for s in self.job_stats.values()]
        ) if self.job_stats else 0

        for job_name, stats in self.job_stats.items():
            # Check for high CPU usage
            if stats.avg_cpu_cores > avg_cpu * self.CPU_OUTLIER_THRESHOLD:
                opportunity = self._create_high_cpu_opportunity(job_name, stats, avg_cpu)
                opportunities.append(opportunity)

            # Check for high memory usage
            if stats.avg_memory_mb > avg_memory * self.MEMORY_OUTLIER_THRESHOLD:
                opportunity = self._create_high_memory_opportunity(job_name, stats, avg_memory)
                opportunities.append(opportunity)

            # Check for long duration
            if stats.avg_duration_seconds > avg_duration * self.DURATION_OUTLIER_THRESHOLD:
                opportunity = self._create_long_duration_opportunity(job_name, stats, avg_duration)
                opportunities.append(opportunity)

            # Check for low success rate
            if stats.success_rate < self.MIN_SUCCESS_RATE:
                opportunity = self._create_low_success_opportunity(job_name, stats)
                opportunities.append(opportunity)

            # Check for low CPU utilization
            if stats.avg_cpu_usage_percent < self.MIN_CPU_UTILIZATION * 100:
                opportunity = self._create_low_cpu_utilization_opportunity(job_name, stats)
                opportunities.append(opportunity)

            # Check for low memory utilization
            if stats.avg_memory_usage_percent < self.MIN_MEMORY_UTILIZATION * 100:
                opportunity = self._create_low_memory_utilization_opportunity(job_name, stats)
                opportunities.append(opportunity)

        return opportunities

    def _create_high_cpu_opportunity(self, job_name: str, stats: JobStatistics, 
                                    avg_cpu: float) -> OptimizationOpportunity:
        """Create optimization opportunity for high CPU usage."""
        excess_cores = stats.avg_cpu_cores - avg_cpu
        estimated_savings = excess_cores * 30 * (stats.avg_duration_seconds / 3600) / 1000 * stats.run_count
        savings_pct = (estimated_savings / stats.total_energy_kwh * 100) if stats.total_energy_kwh > 0 else 0

        return OptimizationOpportunity(
            job_name=job_name,
            issue_type='high_cpu',
            severity='high' if excess_cores > avg_cpu else 'medium',
            description=f'Job uses {stats.avg_cpu_cores:.1f} CPU cores on average, {excess_cores:.1f} more than baseline',
            current_metric=stats.avg_cpu_cores,
            baseline_metric=avg_cpu,
            recommendations=[
                'Review CPU allocation - may be over-provisioned',
                'Consider splitting into parallel subtasks',
                'Enable job caching to reduce re-computation',
                'Profile the job to identify CPU bottlenecks',
                'Use resource limits to prevent over-allocation',
            ],
            estimated_savings_kwh=estimated_savings,
            estimated_savings_pct=savings_pct,
            impact_score=min(100, (excess_cores / avg_cpu * 100) * (stats.run_count / 10)),
        )

    def _create_high_memory_opportunity(self, job_name: str, stats: JobStatistics,
                                       avg_memory: float) -> OptimizationOpportunity:
        """Create optimization opportunity for high memory usage."""
        excess_memory = stats.avg_memory_mb - avg_memory
        estimated_savings = (excess_memory / 1024) * 0.5 * (stats.avg_duration_seconds / 3600) / 1000 * stats.run_count
        savings_pct = (estimated_savings / stats.total_energy_kwh * 100) if stats.total_energy_kwh > 0 else 0

        return OptimizationOpportunity(
            job_name=job_name,
            issue_type='high_memory',
            severity='high' if excess_memory > avg_memory else 'medium',
            description=f'Job uses {stats.avg_memory_mb:.0f} MB on average, {excess_memory:.0f} MB more than baseline',
            current_metric=stats.avg_memory_mb,
            baseline_metric=avg_memory,
            recommendations=[
                'Review memory allocation - may be over-provisioned',
                'Implement streaming/chunking for large data processing',
                'Use memory-efficient data structures',
                'Enable garbage collection optimization',
                'Consider breaking into smaller jobs with less memory',
            ],
            estimated_savings_kwh=estimated_savings,
            estimated_savings_pct=savings_pct,
            impact_score=min(100, (excess_memory / avg_memory * 100) * (stats.run_count / 10)),
        )

    def _create_long_duration_opportunity(self, job_name: str, stats: JobStatistics,
                                         avg_duration: float) -> OptimizationOpportunity:
        """Create optimization opportunity for long-running jobs."""
        excess_duration = stats.avg_duration_seconds - avg_duration
        estimated_savings = (stats.avg_cpu_cores * 30 + stats.avg_memory_mb / 1024 * 0.5) * (excess_duration / 3600) / 1000 * stats.run_count
        savings_pct = (estimated_savings / stats.total_energy_kwh * 100) if stats.total_energy_kwh > 0 else 0

        return OptimizationOpportunity(
            job_name=job_name,
            issue_type='long_duration',
            severity='high' if excess_duration > avg_duration else 'medium',
            description=f'Job runs for {stats.avg_duration_seconds:.0f}s on average, {excess_duration:.0f}s longer than baseline',
            current_metric=stats.avg_duration_seconds,
            baseline_metric=avg_duration,
            recommendations=[
                'Enable parallel execution of independent tasks',
                'Implement caching for expensive operations',
                'Optimize algorithms for better time complexity',
                'Use incremental builds/tests instead of full runs',
                'Consider splitting into multiple smaller jobs',
            ],
            estimated_savings_kwh=estimated_savings,
            estimated_savings_pct=savings_pct,
            impact_score=min(100, (excess_duration / avg_duration * 100) * (stats.run_count / 10)),
        )

    def _create_low_success_opportunity(self, job_name: str, stats: JobStatistics) -> OptimizationOpportunity:
        """Create optimization opportunity for low success rate."""
        return OptimizationOpportunity(
            job_name=job_name,
            issue_type='low_success_rate',
            severity='high',
            description=f'Job has {stats.success_rate*100:.1f}% success rate, wasting {stats.total_wasted_energy_kwh:.4f} kWh on failures',
            current_metric=stats.success_rate * 100,
            baseline_metric=self.MIN_SUCCESS_RATE * 100,
            recommendations=[
                'Investigate root causes of failures',
                'Add better error handling and logging',
                'Implement retry logic with exponential backoff',
                'Review resource allocation for stability',
                'Add health checks before running expensive operations',
            ],
            estimated_savings_kwh=stats.total_wasted_energy_kwh,
            estimated_savings_pct=(stats.total_wasted_energy_kwh / stats.total_energy_kwh * 100) if stats.total_energy_kwh > 0 else 0,
            impact_score=min(100, (1 - stats.success_rate) * 100 * (stats.run_count / 10)),
        )

    def _create_low_cpu_utilization_opportunity(self, job_name: str, stats: JobStatistics) -> OptimizationOpportunity:
        """Create optimization opportunity for low CPU utilization."""
        return OptimizationOpportunity(
            job_name=job_name,
            issue_type='inefficient_parallelization',
            severity='medium',
            description=f'Job uses only {stats.avg_cpu_usage_percent:.1f}% of allocated CPU cores',
            current_metric=stats.avg_cpu_usage_percent,
            baseline_metric=self.MIN_CPU_UTILIZATION * 100,
            recommendations=[
                'Reduce allocated CPU cores to match actual usage',
                'Enable multi-threading/parallelization',
                'Profile to identify CPU bottlenecks',
                'Consider using async operations',
                'Optimize code for better CPU efficiency',
            ],
            estimated_savings_kwh=stats.total_energy_kwh * 0.2,  # Estimate 20% savings
            estimated_savings_pct=20.0,
            impact_score=min(100, (1 - stats.avg_cpu_usage_percent / 100) * 50 * (stats.run_count / 10)),
        )

    def _create_low_memory_utilization_opportunity(self, job_name: str, stats: JobStatistics) -> OptimizationOpportunity:
        """Create optimization opportunity for low memory utilization."""
        return OptimizationOpportunity(
            job_name=job_name,
            issue_type='inefficient_parallelization',
            severity='low',
            description=f'Job uses only {stats.avg_memory_usage_percent:.1f}% of allocated memory',
            current_metric=stats.avg_memory_usage_percent,
            baseline_metric=self.MIN_MEMORY_UTILIZATION * 100,
            recommendations=[
                'Reduce allocated memory to match actual usage',
                'Consider batch processing to use memory more efficiently',
                'Review memory allocation strategy',
                'Profile to identify memory usage patterns',
            ],
            estimated_savings_kwh=stats.total_energy_kwh * 0.1,  # Estimate 10% savings
            estimated_savings_pct=10.0,
            impact_score=min(100, (1 - stats.avg_memory_usage_percent / 100) * 30 * (stats.run_count / 10)),
        )


class ResourceOptimizationReport:
    """Generates optimization reports."""

    def __init__(self, job_stats: Dict[str, JobStatistics], 
                 opportunities: List[OptimizationOpportunity]):
        self.job_stats = job_stats
        self.opportunities = opportunities

    def generate_summary(self) -> Dict[str, Any]:
        """Generate summary report."""
        total_energy = sum(s.total_energy_kwh for s in self.job_stats.values())
        total_wasted = sum(s.total_wasted_energy_kwh for s in self.job_stats.values())
        total_potential_savings = sum(o.estimated_savings_kwh for o in self.opportunities)

        return {
            'timestamp': datetime.utcnow().isoformat(),
            'total_jobs_analyzed': len(self.job_stats),
            'total_opportunities': len(self.opportunities),
            'high_severity': len([o for o in self.opportunities if o.severity == 'high']),
            'medium_severity': len([o for o in self.opportunities if o.severity == 'medium']),
            'low_severity': len([o for o in self.opportunities if o.severity == 'low']),
            'energy': {
                'total_kwh': round(total_energy, 4),
                'wasted_kwh': round(total_wasted, 4),
                'potential_savings_kwh': round(total_potential_savings, 4),
                'potential_savings_pct': round((total_potential_savings / total_energy * 100) if total_energy > 0 else 0, 2),
            },
            'top_opportunities': [
                {
                    'job_name': o.job_name,
                    'issue_type': o.issue_type,
                    'severity': o.severity,
                    'estimated_savings_kwh': round(o.estimated_savings_kwh, 4),
                    'estimated_savings_pct': round(o.estimated_savings_pct, 2),
                    'impact_score': round(o.impact_score, 2),
                }
                for o in self.opportunities[:5]
            ],
        }

    def generate_detailed_report(self) -> str:
        """Generate detailed markdown report."""
        summary = self.generate_summary()

        report = f"""
## 📊 EcoGuard Resource Optimization Report

**Analysis Period:** Last 7 days
**Generated:** {summary['timestamp']}

### Summary

- **Jobs Analyzed:** {summary['total_jobs_analyzed']}
- **Optimization Opportunities:** {summary['total_opportunities']}
  - 🔴 High Severity: {summary['high_severity']}
  - 🟡 Medium Severity: {summary['medium_severity']}
  - 🟢 Low Severity: {summary['low_severity']}

### Energy Impact

| Metric | Value |
|--------|-------|
| **Total Energy Used** | {summary['energy']['total_kwh']} kWh |
| **Wasted Energy** | {summary['energy']['wasted_kwh']} kWh |
| **Potential Savings** | {summary['energy']['potential_savings_kwh']} kWh ({summary['energy']['potential_savings_pct']}%) |

### Top Optimization Opportunities

"""

        for i, opp in enumerate(self.opportunities[:10], 1):
            severity_emoji = {'high': '🔴', 'medium': '🟡', 'low': '🟢'}[opp.severity]
            report += f"""
#### {i}. {severity_emoji} {opp.job_name} - {opp.issue_type.replace('_', ' ').title()}

**Description:** {opp.description}

**Current:** {opp.current_metric:.2f} | **Baseline:** {opp.baseline_metric:.2f}

**Recommendations:**
"""
            for rec in opp.recommendations:
                report += f"- {rec}\n"

            report += f"""
**Estimated Savings:** {opp.estimated_savings_kwh:.4f} kWh ({opp.estimated_savings_pct:.2f}%)

**Impact Score:** {opp.impact_score:.1f}/100

"""

        report += "\n---\n"
        report += "*Report generated by EcoGuard Resource Optimization Agent*\n"

        return report


if __name__ == '__main__':
    # Example usage
    sample_metrics = [
        JobMetric('job-1', 'build', '2024-03-19T10:00Z', 300, 2, 45, 1024, 50, 'success'),
        JobMetric('job-1', 'build', '2024-03-19T11:00Z', 320, 2, 48, 1100, 52, 'success'),
        JobMetric('job-2', 'test', '2024-03-19T10:00Z', 600, 8, 25, 4096, 40, 'success'),
        JobMetric('job-2', 'test', '2024-03-19T11:00Z', 620, 8, 28, 4200, 42, 'failed'),
        JobMetric('job-3', 'deploy', '2024-03-19T10:00Z', 120, 1, 80, 512, 70, 'success'),
        JobMetric('job-3', 'deploy', '2024-03-19T11:00Z', 110, 1, 85, 480, 75, 'success'),
    ]

    analyzer = MetricsAnalyzer()
    analyzer.add_metrics(sample_metrics)
    job_stats, opportunities = analyzer.analyze()

    report_gen = ResourceOptimizationReport(job_stats, opportunities)
    summary = report_gen.generate_summary()

    print(json.dumps(summary, indent=2))
    print(report_gen.generate_detailed_report())
