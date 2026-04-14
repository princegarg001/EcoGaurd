---
title: Use Case Diagram
---

# Use Case Diagram

<div class="ucd-hero">
  <p class="ucd-eyebrow">📐 System Modeling</p>
  <h2 class="ucd-title">EcoGuard — Use Case Analysis</h2>
  <p class="ucd-subtitle">
    A complete behavioral model of EcoGuard's actors and system interactions, structured from stakeholder goals down to technical system boundaries.
  </p>
</div>

---

## 👥 Actors

EcoGuard serves four distinct actors, each with a different level of system interaction and concern.

<div class="actor-grid">

  <div class="actor-card actor--devops">
    <div class="actor-icon">⚙️</div>
    <h3>DevOps Engineer</h3>
    <p class="actor-role">Primary User</p>
    <p>Manages CI/CD pipelines day-to-day. Monitors emissions, applies AI-generated optimizations, and reviews anomaly alerts to improve pipeline efficiency.</p>
    <ul>
      <li>Views live emission dashboards</li>
      <li>Reviews & applies optimization MRs</li>
      <li>Configures pipeline thresholds</li>
      <li>Schedules eco-friendly deployments</li>
    </ul>
  </div>

  <div class="actor-card actor--lead">
    <div class="actor-icon">🧑‍💼</div>
    <h3>Team Lead</h3>
    <p class="actor-role">Supervisor</p>
    <p>Oversees the team's collective pipeline sustainability posture. Approves AI-generated merge requests and receives escalated anomaly alerts.</p>
    <ul>
      <li>Receives threshold breach alerts</li>
      <li>Approves AI remediation MRs</li>
      <li>Reviews team-level emission trends</li>
      <li>Sets project sustainability goals</li>
    </ul>
  </div>

  <div class="actor-card actor--officer">
    <div class="actor-icon">🌿</div>
    <h3>Sustainability Officer</h3>
    <p class="actor-role">Compliance Owner</p>
    <p>Responsible for regulatory compliance reporting. Generates AI-assisted audit reports for EU CSRD, ISO 14064, and GHG Protocol requirements.</p>
    <ul>
      <li>Generates compliance reports</li>
      <li>Exports PDF / DOCX / CSV reports</li>
      <li>Tracks sustainability goal progress</li>
      <li>Submits to regulatory bodies</li>
    </ul>
  </div>

  <div class="actor-card actor--system">
    <div class="actor-icon">🤖</div>
    <h3>AI Agent System</h3>
    <p class="actor-role">Automated Actor</p>
    <p>An autonomous subsystem that continuously monitors pipeline data, detects anomalies, forecasts emissions, and generates code-level optimization patches.</p>
    <ul>
      <li>Forecasts future emissions (ML)</li>
      <li>Detects pipeline anomalies</li>
      <li>Generates remediation MRs</li>
      <li>Auto-drafts compliance reports</li>
    </ul>
  </div>

</div>

---

## 📋 Use Case Inventory

All use cases are listed below, grouped by functional domain, before being visualized in the diagrams.

<div class="uc-inventory">

  <div class="uc-group">
    <h3>📊 Monitoring & Visibility</h3>
    <div class="uc-list">
      <div class="uc-item"><span class="uc-id">UC-01</span><span class="uc-name">View Emission Trend Dashboard</span><span class="uc-actor">DevOps Engineer</span></div>
      <div class="uc-item"><span class="uc-id">UC-02</span><span class="uc-name">Filter Emissions by Project / Branch / Job</span><span class="uc-actor">DevOps Engineer</span></div>
      <div class="uc-item"><span class="uc-id">UC-03</span><span class="uc-name">View Carbon Intensity Heatmap</span><span class="uc-actor">DevOps Engineer</span></div>
      <div class="uc-item"><span class="uc-id">UC-04</span><span class="uc-name">Track Sustainability Goal Progress</span><span class="uc-actor">Team Lead · Sustainability Officer</span></div>
      <div class="uc-item"><span class="uc-id">UC-05</span><span class="uc-name">View AI Emission Forecast (7-day)</span><span class="uc-actor">DevOps Engineer · Team Lead</span></div>
    </div>
  </div>

  <div class="uc-group">
    <h3>🚨 Alerting & Anomaly Detection</h3>
    <div class="uc-list">
      <div class="uc-item"><span class="uc-id">UC-06</span><span class="uc-name">Configure Emission Threshold Alerts</span><span class="uc-actor">Team Lead</span></div>
      <div class="uc-item"><span class="uc-id">UC-07</span><span class="uc-name">Receive Threshold Breach Notification</span><span class="uc-actor">Team Lead</span></div>
      <div class="uc-item"><span class="uc-id">UC-08</span><span class="uc-name">Receive AI Anomaly Detection Alert</span><span class="uc-actor">DevOps Engineer · Team Lead</span></div>
      <div class="uc-item"><span class="uc-id">UC-09</span><span class="uc-name">View Root-Cause Job Breakdown</span><span class="uc-actor">DevOps Engineer</span></div>
    </div>
  </div>

  <div class="uc-group">
    <h3>🔧 Optimization & Remediation</h3>
    <div class="uc-list">
      <div class="uc-item"><span class="uc-id">UC-10</span><span class="uc-name">View Manual Optimization Recommendations</span><span class="uc-actor">DevOps Engineer</span></div>
      <div class="uc-item"><span class="uc-id">UC-11</span><span class="uc-name">Receive AI-Generated Remediation MR</span><span class="uc-actor">DevOps Engineer</span></div>
      <div class="uc-item"><span class="uc-id">UC-12</span><span class="uc-name">Review & Approve AI Remediation MR</span><span class="uc-actor">Team Lead</span></div>
      <div class="uc-item"><span class="uc-id">UC-13</span><span class="uc-name">Schedule Eco-Friendly Deployment Window</span><span class="uc-actor">DevOps Engineer</span></div>
      <div class="uc-item"><span class="uc-id">UC-14</span><span class="uc-name">Trigger Manual Re-optimization Scan</span><span class="uc-actor">DevOps Engineer</span></div>
    </div>
  </div>

  <div class="uc-group">
    <h3>📄 Reporting & Compliance</h3>
    <div class="uc-list">
      <div class="uc-item"><span class="uc-id">UC-15</span><span class="uc-name">Generate Monthly Compliance Report</span><span class="uc-actor">Sustainability Officer</span></div>
      <div class="uc-item"><span class="uc-id">UC-16</span><span class="uc-name">Select Regulatory Format (EU/ISO/GHG)</span><span class="uc-actor">Sustainability Officer</span></div>
      <div class="uc-item"><span class="uc-id">UC-17</span><span class="uc-name">Export Report (PDF / DOCX / CSV)</span><span class="uc-actor">Sustainability Officer</span></div>
      <div class="uc-item"><span class="uc-id">UC-18</span><span class="uc-name">AI Auto-Draft Compliance Narrative</span><span class="uc-actor">AI Agent System</span></div>
    </div>
  </div>

  <div class="uc-group">
    <h3>⚙️ System & Data Operations</h3>
    <div class="uc-list">
      <div class="uc-item"><span class="uc-id">UC-19</span><span class="uc-name">Collect Pipeline Data from GitLab API</span><span class="uc-actor">AI Agent System</span></div>
      <div class="uc-item"><span class="uc-id">UC-20</span><span class="uc-name">Fetch Carbon Intensity from Electricity Maps</span><span class="uc-actor">AI Agent System</span></div>
      <div class="uc-item"><span class="uc-id">UC-21</span><span class="uc-name">Calculate CO₂ Emissions per Job</span><span class="uc-actor">AI Agent System</span></div>
      <div class="uc-item"><span class="uc-id">UC-22</span><span class="uc-name">Retrain Anomaly Detection Model</span><span class="uc-actor">AI Agent System</span></div>
      <div class="uc-item"><span class="uc-id">UC-23</span><span class="uc-name">Retrain Emission Forecast Model</span><span class="uc-actor">AI Agent System</span></div>
      <div class="uc-item"><span class="uc-id">UC-24</span><span class="uc-name">Validate AI Output via Sandbox</span><span class="uc-actor">AI Agent System</span></div>
    </div>
  </div>

</div>

---

## 🗺️ Use Case Diagram — Overview

The master diagram below shows all actors and their relationships to the EcoGuard system boundary.

```mermaid
graph LR
  %% ── Actors ──────────────────────────────
  DevOps(["⚙️ DevOps\nEngineer"])
  Lead(["🧑‍💼 Team\nLead"])
  Officer(["🌿 Sustainability\nOfficer"])
  AI(["🤖 AI Agent\nSystem"])

  %% ── System Boundary ─────────────────────
  subgraph EcoGuard ["🌍  EcoGuard System"]

    subgraph MON ["📊 Monitoring & Visibility"]
      UC01["UC-01 View Emission Trends"]
      UC02["UC-02 Filter by Project/Branch/Job"]
      UC03["UC-03 Carbon Intensity Heatmap"]
      UC04["UC-04 Track Goal Progress"]
      UC05["UC-05 View AI Forecast (7-day)"]
    end

    subgraph ALERT ["🚨 Alerting & Anomaly Detection"]
      UC06["UC-06 Configure Threshold Alerts"]
      UC07["UC-07 Receive Threshold Alert"]
      UC08["UC-08 Receive AI Anomaly Alert"]
      UC09["UC-09 View Root-Cause Breakdown"]
    end

    subgraph OPT ["🔧 Optimization & Remediation"]
      UC10["UC-10 Manual Recommendations"]
      UC11["UC-11 Receive AI Remediation MR"]
      UC12["UC-12 Approve AI Remediation MR"]
      UC13["UC-13 Schedule Eco Deployment"]
      UC14["UC-14 Trigger Re-optimization Scan"]
    end

    subgraph RPT ["📄 Reporting & Compliance"]
      UC15["UC-15 Generate Compliance Report"]
      UC16["UC-16 Select Regulatory Format"]
      UC17["UC-17 Export Report"]
      UC18["UC-18 AI Auto-Draft Narrative"]
    end

    subgraph SYS ["⚙️ System Operations"]
      UC19["UC-19 Collect GitLab Pipeline Data"]
      UC20["UC-20 Fetch Carbon Intensity"]
      UC21["UC-21 Calculate CO₂ per Job"]
      UC22["UC-22 Retrain Anomaly Model"]
      UC23["UC-23 Retrain Forecast Model"]
      UC24["UC-24 Validate AI Output (Sandbox)"]
    end

  end

  %% ── DevOps Associations ──────────────────
  DevOps --> UC01
  DevOps --> UC02
  DevOps --> UC03
  DevOps --> UC05
  DevOps --> UC08
  DevOps --> UC09
  DevOps --> UC10
  DevOps --> UC11
  DevOps --> UC13
  DevOps --> UC14

  %% ── Team Lead Associations ───────────────
  Lead --> UC04
  Lead --> UC05
  Lead --> UC06
  Lead --> UC07
  Lead --> UC08
  Lead --> UC12

  %% ── Sustainability Officer Associations ──
  Officer --> UC04
  Officer --> UC15
  Officer --> UC16
  Officer --> UC17

  %% ── AI Agent Associations ────────────────
  AI --> UC05
  AI --> UC08
  AI --> UC11
  AI --> UC18
  AI --> UC19
  AI --> UC20
  AI --> UC21
  AI --> UC22
  AI --> UC23
  AI --> UC24

  %% ── Styling ──────────────────────────────
  style EcoGuard fill:#0f172a,stroke:#334155,stroke-width:2px,color:#f1f5f9
  style MON fill:#0c2340,stroke:#2563eb,stroke-width:1.5px,color:#93c5fd
  style ALERT fill:#1c1008,stroke:#d97706,stroke-width:1.5px,color:#fde68a
  style OPT fill:#071a12,stroke:#16a34a,stroke-width:1.5px,color:#86efac
  style RPT fill:#160b24,stroke:#7c3aed,stroke-width:1.5px,color:#c4b5fd
  style SYS fill:#1a0e0e,stroke:#dc2626,stroke-width:1.5px,color:#fca5a5
```

---

## 🎯 Detailed Use Case Views

### 1️⃣ DevOps Engineer — Daily Workflow

```mermaid
graph TD
  DevOps(["⚙️ DevOps Engineer"])

  subgraph EcoGuard ["EcoGuard System"]
    direction TB

    A1["UC-01\nView Emission Trend Dashboard"]
    A2["UC-02\nFilter by Project / Branch / Job"]
    A3["UC-03\nView Carbon Intensity Heatmap"]
    A5["UC-05\nView AI Emission Forecast"]
    A8["UC-08\nReceive AI Anomaly Alert"]
    A9["UC-09\nView Root-Cause Job Breakdown"]
    A10["UC-10\nView Manual Recommendations"]
    A11["UC-11\nReceive AI Remediation MR"]
    A13["UC-13\nSchedule Eco-Friendly Deployment"]
    A14["UC-14\nTrigger Re-optimization Scan"]

    A1 -->|"«include»"| A2
    A8 -->|"«include»"| A9
    A10 -->|"«extend»"| A11
    A13 -->|"«extend»"| A3
  end

  DevOps --> A1
  DevOps --> A3
  DevOps --> A5
  DevOps --> A8
  DevOps --> A10
  DevOps --> A11
  DevOps --> A13
  DevOps --> A14

  style EcoGuard fill:#071a12,stroke:#16a34a,stroke-width:2px,color:#86efac
  style DevOps fill:#16a34a,stroke:#15803d,color:#fff
```

### 2️⃣ Team Lead — Oversight & Approval Workflow

```mermaid
graph TD
  Lead(["🧑‍💼 Team Lead"])

  subgraph EcoGuard ["EcoGuard System"]
    direction TB

    B4["UC-04\nTrack Sustainability Goal Progress"]
    B5["UC-05\nView AI Emission Forecast"]
    B6["UC-06\nConfigure Threshold Alerts"]
    B7["UC-07\nReceive Threshold Breach Alert"]
    B8["UC-08\nReceive AI Anomaly Alert"]
    B12["UC-12\nReview & Approve AI Remediation MR"]

    B6 -->|"«include»"| B7
    B8 -->|"«extend»"| B12
  end

  Lead --> B4
  Lead --> B5
  Lead --> B6
  Lead --> B7
  Lead --> B8
  Lead --> B12

  style EcoGuard fill:#0c2340,stroke:#2563eb,stroke-width:2px,color:#93c5fd
  style Lead fill:#2563eb,stroke:#1d4ed8,color:#fff
```

### 3️⃣ Sustainability Officer — Compliance Workflow

```mermaid
graph TD
  Officer(["🌿 Sustainability Officer"])

  subgraph EcoGuard ["EcoGuard System"]
    direction TB

    C4["UC-04\nTrack Sustainability Goal Progress"]
    C15["UC-15\nGenerate Monthly Compliance Report"]
    C16["UC-16\nSelect Regulatory Format\n(EU CSRD / ISO 14064 / GHG Protocol)"]
    C17["UC-17\nExport Report (PDF / DOCX / CSV)"]
    C18["UC-18\nAI Auto-Draft Compliance Narrative"]

    C15 -->|"«include»"| C16
    C15 -->|"«include»"| C18
    C15 -->|"«extend»"| C17
  end

  Officer --> C4
  Officer --> C15
  Officer --> C16
  Officer --> C17

  style EcoGuard fill:#160b24,stroke:#7c3aed,stroke-width:2px,color:#c4b5fd
  style Officer fill:#7c3aed,stroke:#6d28d9,color:#fff
```

### 4️⃣ AI Agent System — Autonomous Operations

```mermaid
graph TD
  AI(["🤖 AI Agent System"])

  subgraph EcoGuard ["EcoGuard System"]
    direction TB

    D19["UC-19\nCollect Pipeline Data\nfrom GitLab API"]
    D20["UC-20\nFetch Carbon Intensity\nfrom Electricity Maps"]
    D21["UC-21\nCalculate CO₂\nEmissions per Job"]
    D22["UC-22\nRetrain Anomaly\nDetection Model"]
    D23["UC-23\nRetrain Emission\nForecast Model"]
    D24["UC-24\nValidate AI Output\nvia Sandbox"]
    D05["UC-05\nGenerate 7-Day\nEmission Forecast"]
    D08["UC-08\nTrigger Anomaly\nAlert"]
    D11["UC-11\nGenerate Remediation MR"]
    D18["UC-18\nAuto-Draft Compliance\nNarrative (RAG)"]

    D19 -->|"«include»"| D21
    D20 -->|"«include»"| D21
    D21 -->|"«include»"| D05
    D21 -->|"«include»"| D08
    D11 -->|"«include»"| D24
    D18 -->|"«include»"| D24
    D22 -.->|"«extend»"| D08
    D23 -.->|"«extend»"| D05
  end

  AI --> D19
  AI --> D20
  AI --> D22
  AI --> D23
  AI --> D11
  AI --> D18

  style EcoGuard fill:#1a0e0e,stroke:#dc2626,stroke-width:2px,color:#fca5a5
  style AI fill:#dc2626,stroke:#b91c1c,color:#fff
```

---

## 🔗 Use Case Relationships Summary

| Relationship | From | To | Type |
|---|---|---|---|
| UC-01 → UC-02 | View Dashboard | Filter by Criteria | `«include»` |
| UC-06 → UC-07 | Configure Alert | Receive Alert | `«include»` |
| UC-08 → UC-12 | AI Anomaly Alert | Approve Remediation MR | `«extend»` |
| UC-10 → UC-11 | Manual Recs | AI Remediation MR | `«extend»` |
| UC-13 → UC-03 | Eco Scheduling | Carbon Intensity Heatmap | `«extend»` |
| UC-15 → UC-16 | Generate Report | Select Format | `«include»` |
| UC-15 → UC-18 | Generate Report | AI Auto-Draft Narrative | `«include»` |
| UC-15 → UC-17 | Generate Report | Export Report | `«extend»` |
| UC-19 → UC-21 | Collect Data | Calculate Emissions | `«include»` |
| UC-20 → UC-21 | Fetch Carbon Intensity | Calculate Emissions | `«include»` |
| UC-21 → UC-05 | Calculate Emissions | AI Forecast | `«include»` |
| UC-21 → UC-08 | Calculate Emissions | Anomaly Alert | `«include»` |
| UC-11 → UC-24 | Generate MR | Sandbox Validation | `«include»` |
| UC-18 → UC-24 | Auto-Draft Report | Sandbox Validation | `«include»` |

---

## 📊 Actor Coverage Matrix

<div class="matrix-wrapper">
  <div class="matrix-table">
    <div class="matrix-header">
      <div class="matrix-cell matrix-dim">Use Case</div>
      <div class="matrix-cell matrix-devops">⚙️ DevOps</div>
      <div class="matrix-cell matrix-lead">🧑‍💼 Lead</div>
      <div class="matrix-cell matrix-officer">🌿 Officer</div>
      <div class="matrix-cell matrix-ai">🤖 AI Agent</div>
    </div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-01 View Emission Trends</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-02 Filter Emissions</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-03 Carbon Intensity Heatmap</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-04 Track Goal Progress</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-05 AI Emission Forecast</div><div class="matrix-cell">✅</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-06 Configure Alerts</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-07 Threshold Alert</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-08 AI Anomaly Alert</div><div class="matrix-cell">✅</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-09 Root-Cause Breakdown</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-10 Manual Recommendations</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-11 AI Remediation MR</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-12 Approve Remediation MR</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-13 Eco Deployment Schedule</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-14 Re-optimization Scan</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-15 Generate Compliance Report</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-16 Select Regulatory Format</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-17 Export Report</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div><div class="matrix-cell">—</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-18 AI Auto-Draft Narrative</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-19 Collect GitLab Data</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-20 Fetch Carbon Intensity</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-21 Calculate CO₂ per Job</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-22 Retrain Anomaly Model</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row"><div class="matrix-cell matrix-dim">UC-23 Retrain Forecast Model</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-row matrix-alt"><div class="matrix-cell matrix-dim">UC-24 Validate via Sandbox</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">—</div><div class="matrix-cell">✅</div></div>
    <div class="matrix-footer">
      <div class="matrix-cell matrix-dim"><strong>Total Use Cases</strong></div>
      <div class="matrix-cell score-devops"><strong>10</strong></div>
      <div class="matrix-cell score-lead"><strong>6</strong></div>
      <div class="matrix-cell score-officer"><strong>5</strong></div>
      <div class="matrix-cell score-ai"><strong>10</strong></div>
    </div>
  </div>
</div>

<style>
/* ── Hero ──────────────────────────────────────────── */
.ucd-hero {
  text-align: center;
  padding: 2.5rem 1.5rem;
  margin: 1.5rem 0 2rem;
  background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(37,99,235,0.08) 60%, transparent);
  border-radius: 20px;
  border: 1px solid var(--vp-c-divider);
}
.ucd-eyebrow {
  font-size: 0.82rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #10b981;
  font-weight: 700;
  margin-bottom: 0.7rem;
}
.ucd-title {
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
  letter-spacing: -0.03em;
  margin: 0 auto 0.8rem;
  max-width: 600px;
  line-height: 1.2;
}
.ucd-subtitle {
  color: var(--vp-c-text-2);
  max-width: 620px;
  margin: 0 auto;
  line-height: 1.65;
}

/* ── Actor Cards ───────────────────────────────────── */
.actor-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1.1rem;
  margin: 1.2rem 0;
}
.actor-card {
  padding: 1.4rem 1.3rem;
  border-radius: 16px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
  position: relative;
  overflow: hidden;
}
.actor-card::before {
  content: '';
  position: absolute;
  top: 0; left: 0; right: 0;
  height: 3px;
}
.actor-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 16px 40px rgba(0,0,0,0.1);
}
.actor--devops::before { background: linear-gradient(90deg, #16a34a, #059669); }
.actor--lead::before   { background: linear-gradient(90deg, #2563eb, #3b82f6); }
.actor--officer::before { background: linear-gradient(90deg, #7c3aed, #a78bfa); }
.actor--system::before { background: linear-gradient(90deg, #dc2626, #f87171); }

.actor-icon {
  font-size: 2rem;
  margin-bottom: 0.5rem;
}
.actor-card h3 {
  margin: 0 0 0.2rem;
  font-size: 1.05rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
}
.actor-role {
  font-size: 0.75rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  font-weight: 600;
  margin: 0 0 0.7rem;
  color: var(--vp-c-text-3);
}
.actor-card p:not(.actor-role) {
  font-size: 0.87rem;
  color: var(--vp-c-text-2);
  line-height: 1.55;
  margin-bottom: 0.8rem;
}
.actor-card ul {
  font-size: 0.83rem;
  color: var(--vp-c-text-2);
  padding-left: 1.1rem;
  margin: 0;
  line-height: 1.7;
}

/* ── Use Case Inventory ────────────────────────────── */
.uc-inventory {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 1rem;
  margin: 1.2rem 0;
}
.uc-group {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 14px;
  padding: 1.1rem 1.2rem;
}
.uc-group h3 {
  margin: 0 0 0.8rem;
  font-size: 0.95rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  border-bottom: 1px solid var(--vp-c-divider);
  padding-bottom: 0.5rem;
}
.uc-list {
  display: flex;
  flex-direction: column;
  gap: 0.45rem;
}
.uc-item {
  display: flex;
  align-items: baseline;
  gap: 0.6rem;
  font-size: 0.83rem;
  line-height: 1.4;
}
.uc-id {
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.72rem;
  font-weight: 700;
  color: #10b981;
  background: rgba(16,185,129,0.1);
  border-radius: 6px;
  padding: 1px 6px;
  white-space: nowrap;
  flex-shrink: 0;
}
.uc-name {
  color: var(--vp-c-text-1);
  font-weight: 500;
  flex: 1;
}
.uc-actor {
  font-size: 0.72rem;
  color: var(--vp-c-text-3);
  white-space: nowrap;
  font-style: italic;
}

/* ── Matrix ────────────────────────────────────────── */
.matrix-wrapper {
  margin: 1.2rem 0;
  border-radius: 14px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  box-shadow: 0 6px 24px rgba(0,0,0,0.06);
}
.matrix-table {
  width: 100%;
  display: flex;
  flex-direction: column;
}
.matrix-header {
  display: grid;
  grid-template-columns: 1fr 90px 90px 90px 90px;
  background: linear-gradient(135deg, #0f172a, #1e293b);
  padding: 0;
}
.matrix-row {
  display: grid;
  grid-template-columns: 1fr 90px 90px 90px 90px;
  border-top: 1px solid var(--vp-c-divider);
  transition: background 0.15s;
}
.matrix-row:hover { background: var(--vp-c-bg-soft); }
.matrix-alt { background: rgba(0,0,0,0.02); }
.matrix-footer {
  display: grid;
  grid-template-columns: 1fr 90px 90px 90px 90px;
  border-top: 2px solid var(--vp-c-divider);
  background: var(--vp-c-bg-soft);
}
.matrix-cell {
  padding: 0.5rem 0.8rem;
  font-size: 0.82rem;
  color: var(--vp-c-text-2);
  border-right: 1px solid var(--vp-c-divider);
  display: flex;
  align-items: center;
  justify-content: center;
}
.matrix-cell:first-child { justify-content: flex-start; }
.matrix-cell:last-child { border-right: none; }
.matrix-dim {
  color: var(--vp-c-text-1);
  font-weight: 600;
  font-size: 0.8rem;
  justify-content: flex-start;
}
.matrix-devops { color: #34d399; font-weight: 700; font-size: 0.78rem; }
.matrix-lead   { color: #60a5fa; font-weight: 700; font-size: 0.78rem; }
.matrix-officer { color: #c4b5fd; font-weight: 700; font-size: 0.78rem; }
.matrix-ai     { color: #f87171; font-weight: 700; font-size: 0.78rem; }

.score-devops { color: #10b981; font-size: 1.05rem; font-weight: 800; }
.score-lead   { color: #3b82f6; font-size: 1.05rem; font-weight: 800; }
.score-officer { color: #8b5cf6; font-size: 1.05rem; font-weight: 800; }
.score-ai     { color: #ef4444; font-size: 1.05rem; font-weight: 800; }

@media (max-width: 768px) {
  .actor-grid, .uc-inventory { grid-template-columns: 1fr; }
  .matrix-header, .matrix-row, .matrix-footer {
    grid-template-columns: 1fr 60px 60px 60px 60px;
  }
  .matrix-cell { padding: 0.4rem 0.4rem; font-size: 0.72rem; }
}
</style>
