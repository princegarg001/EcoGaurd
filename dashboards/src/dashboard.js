// EcoGuard Dashboard JavaScript

let charts = {};
let currentTab = 'overview';

// Initialize Dashboard
document.addEventListener('DOMContentLoaded', function() {
    loadDashboardData();
    updateLastUpdate();
    setInterval(updateLastUpdate, 60000); // Update every minute
});

// Load Dashboard Data
async function loadDashboardData() {
    try {
        // Load data from API endpoints
        const [dailyData, weeklyData, monthlyData, goalsData] = await Promise.all([
            fetch('http://localhost:5000/api/daily-metrics').then(r => r.json()).catch(() => []),
            fetch('http://localhost:5000/api/weekly-metrics').then(r => r.json()).catch(() => []),
            fetch('http://localhost:5000/api/monthly-metrics').then(r => r.json()).catch(() => []),
            fetch('http://localhost:5000/api/sustainability-goals').then(r => r.json()).catch(() => [])
        ]);

        // Update header stats
        updateHeaderStats(dailyData, monthlyData);

        // Initialize charts
        initializeCharts(dailyData, weeklyData, monthlyData);

        // Update metrics
        updateMetrics(dailyData, weeklyData, monthlyData);

        // Update goals
        updateGoals(goalsData);

        // Update issues and recommendations
        updateIssuesAndRecommendations();
    } catch (error) {
        console.error('Error loading dashboard data:', error);
    }
}

// Update Header Stats
function updateHeaderStats(dailyData, monthlyData) {
    if (dailyData.length > 0) {
        const latest = dailyData[dailyData.length - 1];
        document.getElementById('totalEmissions').textContent = 
            (latest.total_emissions_kg_co2 || 0).toFixed(2) + ' kg';
        document.getElementById('totalEnergy').textContent = 
            (latest.total_energy_kwh || 0).toFixed(2) + ' kWh';
        document.getElementById('buildCount').textContent = latest.builds_count || 0;
    }

    if (monthlyData.length > 0) {
        const latest = monthlyData[monthlyData.length - 1];
        document.getElementById('sciScore').textContent = 
            (latest.sci_score || 0).toFixed(2);
    }
}

// Initialize Charts
function initializeCharts(dailyData, weeklyData, monthlyData) {
    // Emissions Chart
    if (dailyData.length > 0) {
        const ctx = document.getElementById('emissionsChart')?.getContext('2d');
        if (ctx) {
            charts.emissions = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: dailyData.map(d => new Date(d.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })),
                    datasets: [{
                        label: 'CO₂ Emissions (kg)',
                        data: dailyData.map(d => d.total_emissions_kg_co2),
                        borderColor: '#10b981',
                        backgroundColor: 'rgba(16, 185, 129, 0.1)',
                        borderWidth: 2,
                        fill: true,
                        tension: 0.4,
                        pointRadius: 4,
                        pointBackgroundColor: '#10b981',
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: {
                            display: true,
                            labels: { usePointStyle: true }
                        }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: { color: '#6b7280' },
                            grid: { color: '#e5e7eb' }
                        },
                        x: {
                            ticks: { color: '#6b7280' },
                            grid: { color: '#e5e7eb' }
                        }
                    }
                }
            });
        }
    }

    // Energy Chart
    if (dailyData.length > 0) {
        const ctx = document.getElementById('energyChart')?.getContext('2d');
        if (ctx) {
            charts.energy = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: dailyData.map(d => new Date(d.date).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })),
                    datasets: [{
                        label: 'Energy (kWh)',
                        data: dailyData.map(d => d.total_energy_kwh),
                        backgroundColor: '#3b82f6',
                        borderRadius: 6,
                        borderSkipped: false
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: true }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: { color: '#6b7280' },
                            grid: { color: '#e5e7eb' }
                        },
                        x: {
                            ticks: { color: '#6b7280' },
                            grid: { color: '#e5e7eb' }
                        }
                    }
                }
            });
        }
    }

    // Source Chart (Pie)
    const sourceCtx = document.getElementById('sourceChart')?.getContext('2d');
    if (sourceCtx) {
        charts.source = new Chart(sourceCtx, {
            type: 'doughnut',
            data: {
                labels: ['CI/CD Pipelines', 'Deployments', 'Cloud Services', 'Other'],
                datasets: [{
                    data: [45, 25, 20, 10],
                    backgroundColor: [
                        '#10b981',
                        '#3b82f6',
                        '#f59e0b',
                        '#ef4444'
                    ],
                    borderColor: '#fff',
                    borderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        position: 'bottom',
                        labels: { usePointStyle: true, padding: 15 }
                    }
                }
            }
        });
    }

    // Region Chart (Bar)
    const regionCtx = document.getElementById('regionChart')?.getContext('2d');
    if (regionCtx) {
        charts.region = new Chart(regionCtx, {
            type: 'bar',
            data: {
                labels: ['US-CA', 'EU-FR', 'EU-NO', 'US-TX', 'APAC-AU'],
                datasets: [{
                    label: 'Carbon Intensity (gCO₂/kWh)',
                    data: [150, 50, 20, 400, 600],
                    backgroundColor: [
                        '#10b981',
                        '#3b82f6',
                        '#059669',
                        '#f59e0b',
                        '#ef4444'
                    ],
                    borderRadius: 6,
                    borderSkipped: false
                }]
            },
            options: {
                indexAxis: 'y',
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false }
                },
                scales: {
                    x: {
                        beginAtZero: true,
                        ticks: { color: '#6b7280' },
                        grid: { color: '#e5e7eb' }
                    },
                    y: {
                        ticks: { color: '#6b7280' },
                        grid: { color: '#e5e7eb' }
                    }
                }
            }
        });
    }

    // Weekly Comparison Chart
    if (weeklyData.length > 0) {
        const ctx = document.getElementById('weeklyComparisonChart')?.getContext('2d');
        if (ctx) {
            charts.weeklyComparison = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: weeklyData.map(w => `Week of ${new Date(w.week_start).toLocaleDateString('en-US', { month: 'short', day: 'numeric' })}`),
                    datasets: [
                        {
                            label: 'Energy (kWh)',
                            data: weeklyData.map(w => w.total_energy_kwh),
                            backgroundColor: '#3b82f6',
                            borderRadius: 6,
                            borderSkipped: false
                        },
                        {
                            label: 'CO₂ (kg)',
                            data: weeklyData.map(w => w.total_emissions_kg_co2),
                            backgroundColor: '#ef4444',
                            borderRadius: 6,
                            borderSkipped: false
                        }
                    ]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: true }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: { color: '#6b7280' },
                            grid: { color: '#e5e7eb' }
                        },
                        x: {
                            ticks: { color: '#6b7280' },
                            grid: { color: '#e5e7eb' }
                        }
                    }
                }
            });
        }
    }

    // Monthly Trend Chart
    if (monthlyData.length > 0) {
        const ctx = document.getElementById('monthlyTrendChart')?.getContext('2d');
        if (ctx) {
            charts.monthlyTrend = new Chart(ctx, {
                type: 'line',
                data: {
                    labels: monthlyData.map(m => new Date(m.month + '-01').toLocaleDateString('en-US', { month: 'short', year: '2-digit' })),
                    datasets: [{
                        label: 'Monthly CO₂ (kg)',
                        data: monthlyData.map(m => m.total_emissions_kg_co2),
                        borderColor: '#10b981',
                        backgroundColor: 'rgba(16, 185, 129, 0.1)',
                        borderWidth: 3,
                        fill: true,
                        tension: 0.4,
                        pointRadius: 5,
                        pointBackgroundColor: '#10b981',
                        pointBorderColor: '#fff',
                        pointBorderWidth: 2
                    }]
                },
                options: {
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: {
                        legend: { display: true }
                    },
                    scales: {
                        y: {
                            beginAtZero: true,
                            ticks: { color: '#6b7280' },
                            grid: { color: '#e5e7eb' }
                        },
                        x: {
                            ticks: { color: '#6b7280' },
                            grid: { color: '#e5e7eb' }
                        }
                    }
                }
            });
        }
    }
}

// Update Metrics
function updateMetrics(dailyData, weeklyData, monthlyData) {
    if (dailyData.length > 0) {
        const latest = dailyData[dailyData.length - 1];
        document.getElementById('dailyAvg').textContent = latest.total_emissions_kg_co2.toFixed(2);
    }

    if (weeklyData.length > 0) {
        const latest = weeklyData[weeklyData.length - 1];
        document.getElementById('weeklyTotal').textContent = latest.total_emissions_kg_co2.toFixed(2);
        document.getElementById('co2PerBuild').textContent = latest.avg_emissions_per_build_kg_co2.toFixed(3);
    }

    if (monthlyData.length > 0) {
        const latest = monthlyData[monthlyData.length - 1];
        document.getElementById('monthlyTotal').textContent = latest.total_emissions_kg_co2.toFixed(2);
    }
}

// Update Goals
function updateGoals(goalsData) {
    const goalsList = document.getElementById('goalsList');
    if (!goalsList) return;

    if (goalsData.length === 0) {
        goalsList.innerHTML = '<p style="color: #6b7280;">No goals set yet.</p>';
        return;
    }

    goalsList.innerHTML = goalsData.map(goal => `
        <div class="goal-item">
            <div class="goal-header">
                <div class="goal-name">${goal.name}</div>
                <span class="goal-status ${goal.status}">${goal.status.replace('_', ' ').toUpperCase()}</span>
            </div>
            <div class="progress-bar">
                <div class="progress-fill" style="width: ${Math.min(goal.progress_percent, 100)}%"></div>
            </div>
            <div class="goal-details">
                <span>${goal.current_value.toFixed(2)} / ${goal.target_value.toFixed(2)} ${goal.target_unit}</span>
                <span>${goal.progress_percent.toFixed(1)}% Complete</span>
            </div>
            <div style="font-size: 0.85em; color: #6b7280; margin-top: 8px;">
                Deadline: ${new Date(goal.deadline).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' })}
            </div>
        </div>
    `).join('');
}

// Update Issues and Recommendations
function updateIssuesAndRecommendations() {
    // Mock data for demonstration
    const highIssues = [
        {
            title: 'High Pipeline Emissions',
            description: 'Pipeline #1234 used 0.08 kg CO₂e',
            severity: 'high',
            savings: '15% reduction possible'
        },
        {
            title: 'Inefficient Loop Detected',
            description: 'Constant computation inside loop in processor.py',
            severity: 'high',
            savings: '5-10% energy savings'
        }
    ];

    const recentIssues = [
        {
            title: 'Unused Variable',
            description: 'Variable "temp_data" assigned but never used',
            severity: 'low',
            savings: '1-2% memory reduction'
        },
        {
            title: 'String Concatenation in Loop',
            description: 'Using += operator for string concatenation',
            severity: 'medium',
            savings: '20-30% energy reduction'
        }
    ];

    const recommendations = [
        {
            title: 'Optimize Test Suite',
            description: 'Test job uses 8 CPU cores but only 25% utilization',
            savings: '17.6% energy savings'
        },
        {
            title: 'Enable Caching',
            description: 'Build job recomputes dependencies on every run',
            savings: '25-35% time reduction'
        },
        {
            title: 'Deploy During Low-Carbon Hours',
            description: 'Schedule deployments at 03:00 UTC for 40% lower emissions',
            savings: '40% CO₂ reduction'
        }
    ];

    // Update high issues
    const highIssuesList = document.getElementById('highIssuesList');
    if (highIssuesList) {
        highIssuesList.innerHTML = highIssues.map(issue => `
            <div class="issue-item">
                <div class="issue-icon">🔴</div>
                <div class="issue-content">
                    <div class="issue-title">${issue.title}</div>
                    <div class="issue-description">${issue.description}</div>
                    <div class="issue-meta">
                        <span class="issue-severity high">HIGH</span>
                        <span>${issue.savings}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    // Update recent issues
    const recentIssuesList = document.getElementById('recentIssuesList');
    if (recentIssuesList) {
        recentIssuesList.innerHTML = recentIssues.map(issue => `
            <div class="issue-item">
                <div class="issue-icon">${issue.severity === 'high' ? '🔴' : issue.severity === 'medium' ? '🟡' : '🔵'}</div>
                <div class="issue-content">
                    <div class="issue-title">${issue.title}</div>
                    <div class="issue-description">${issue.description}</div>
                    <div class="issue-meta">
                        <span class="issue-severity ${issue.severity}">${issue.severity.toUpperCase()}</span>
                        <span>${issue.savings}</span>
                    </div>
                </div>
            </div>
        `).join('');
    }

    // Update recommendations
    const recommendationsList = document.getElementById('recommendationsList');
    if (recommendationsList) {
        recommendationsList.innerHTML = recommendations.map(rec => `
            <div class="recommendation-item">
                <div class="recommendation-title">💡 ${rec.title}</div>
                <div class="recommendation-description">${rec.description}</div>
                <div class="recommendation-savings">Estimated Savings: ${rec.savings}</div>
            </div>
        `).join('');
    }
}

// Tab Switching
function switchTab(tabName) {
    // Hide all tabs
    document.querySelectorAll('.tab-content').forEach(tab => {
        tab.classList.add('hidden');
    });

    // Remove active class from all tabs
    document.querySelectorAll('.nav-tab').forEach(tab => {
        tab.classList.remove('active');
    });

    // Show selected tab
    const selectedTab = document.getElementById(tabName);
    if (selectedTab) {
        selectedTab.classList.remove('hidden');
    }

    // Add active class to clicked tab
    event.target.classList.add('active');

    // Trigger chart resize
    setTimeout(() => {
        Object.values(charts).forEach(chart => {
            if (chart) chart.resize();
        });
    }, 100);
}

// Update Last Update Time
function updateLastUpdate() {
    const now = new Date();
    const timeString = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' });
    document.getElementById('lastUpdate').textContent = timeString;
}
