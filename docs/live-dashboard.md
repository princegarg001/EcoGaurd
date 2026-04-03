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
