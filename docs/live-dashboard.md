---
title: Live Dashboard
description: Embedded real-time EcoGuard dashboard powered by live pipeline and carbon data.
---

# Live Dashboard

This page embeds the actual EcoGuard dashboard that fetches real data from the JSON metrics published during the GitHub Pages build.

<div class="dashboard-intro">
  <p>
    The dashboard below loads the same data pipeline used by <code>public/dashboard.html</code>.
    It reads from the generated <code>api/*.json</code> files and updates charts from live metrics.
  </p>
</div>

<div id="data-health-panel" class="data-health-panel">
  <div class="data-health-header">
    <h2>Live Data Health</h2>
    <p>Instant status from published dashboard data files.</p>
  </div>
  <div class="data-health-grid">
    <div class="data-health-item">
      <span class="data-health-label">Pipeline Status</span>
      <span id="health-status" class="health-pill health-pill--checking">Checking</span>
    </div>
    <div class="data-health-item">
      <span class="data-health-label">Last Data Update</span>
      <span id="health-updated-at" class="data-health-value">Checking</span>
    </div>
    <div class="data-health-item">
      <span class="data-health-label">Data Source</span>
      <span id="health-source" class="data-health-value">Checking</span>
    </div>
    <div class="data-health-item">
      <span class="data-health-label">Daily Records</span>
      <span id="health-records" class="data-health-value">Checking</span>
    </div>
    <div class="data-health-item">
      <span class="data-health-label">Carbon API</span>
      <span id="health-carbon-source" class="data-health-value">Checking</span>
    </div>
    <div class="data-health-item">
      <span class="data-health-label">GitLab Source</span>
      <span id="health-gitlab-source" class="data-health-value">Checking</span>
    </div>
  </div>
  <p id="health-hint" class="data-health-hint">Fetching live status from api/summary.json and api/daily-metrics.json</p>
</div>

<div class="dashboard-shell">
  <iframe class="dashboard-frame" src="./dashboard.html" title="EcoGuard live dashboard" loading="lazy"></iframe>
</div>

## What this dashboard shows

- Real pipeline emissions and energy usage
- Sustainability score and build totals
- Daily, weekly, and monthly trends
- Resource and region breakdowns
- Goals and recommendation panels

## Direct file

- [Open dashboard.html](./dashboard.html)
