---
title: Software Requirements Specification
---

# Software Requirements Specification (SRS)

<div class="srs-hero">
  <p class="srs-hero-eyebrow">📄 SRS Document</p>
  <h2 class="srs-hero-title">A comprehensive requirements specification for the EcoGuard sustainability platform</h2>
  <p class="srs-hero-subtitle">
    This document defines every layer of requirements — from high-level business goals down to interface contracts — following IEEE 830 standards and managed through <strong>OSRMT</strong> (Open-Source Requirements Management Tool).
  </p>
</div>

---

## 📐 Requirements Hierarchy

The diagram below illustrates how the five requirement types relate to each other, flowing from strategic business needs down to technical interface contracts.

```mermaid
flowchart TD
    BR["🏢 Business Requirements"]
    UR["👤 User Requirements"]
    FR["⚙️ Functional Requirements"]
    NFR["🛡️ Non-Functional Requirements"]
    IR["🔌 Interface Requirements"]

    BR --> UR
    BR --> NFR
    UR --> FR
    FR --> IR
    NFR --> IR

    style BR fill:#1e40af,stroke:#1e3a8a,color:#fff,stroke-width:2px
    style UR fill:#7c3aed,stroke:#6d28d9,color:#fff,stroke-width:2px
    style FR fill:#059669,stroke:#047857,color:#fff,stroke-width:2px
    style NFR fill:#d97706,stroke:#b45309,color:#fff,stroke-width:2px
    style IR fill:#dc2626,stroke:#b91c1c,color:#fff,stroke-width:2px
```

Each level adds specificity. Business Requirements define **why** the system exists, User Requirements define **what** users need, Functional Requirements define **how** the system behaves, Non-Functional Requirements define **how well** it performs, and Interface Requirements define **how it connects** to external systems.

---

## 🏢 1. Business Requirements

Business requirements capture the high-level objectives that justify the project's existence. They are defined by executive stakeholders and drive every downstream decision.

<div class="srs-card srs-card--business">
  <h3>BR-001: Sustainability Compliance</h3>
  <p><strong>Description:</strong> EcoGuard shall enable organizations to measure, track, and report the carbon footprint of their CI/CD pipelines in compliance with emerging EU sustainability reporting directives.</p>
  <p><strong>Priority:</strong> <span class="priority-badge priority-critical">Critical</span></p>
  <p><strong>Rationale:</strong> Regulatory bodies are increasingly requiring digital sustainability reporting. Failure to comply exposes organizations to legal and reputational risk.</p>
</div>

<div class="srs-card srs-card--business">
  <h3>BR-002: Cost Optimization</h3>
  <p><strong>Description:</strong> The platform shall identify resource inefficiencies in pipeline execution and recommend optimizations that reduce both compute costs and energy consumption by at least 15%.</p>
  <p><strong>Priority:</strong> <span class="priority-badge priority-high">High</span></p>
  <p><strong>Rationale:</strong> Cloud compute costs are a major operational expense. Aligning cost reduction with sustainability creates a dual incentive for adoption.</p>
</div>

<div class="srs-card srs-card--business">
  <h3>BR-003: Transparent Reporting</h3>
  <p><strong>Description:</strong> EcoGuard shall produce clear, auditable sustainability dashboards and reports suitable for both internal engineering teams and external stakeholders.</p>
  <p><strong>Priority:</strong> <span class="priority-badge priority-high">High</span></p>
  <p><strong>Rationale:</strong> Transparency builds trust with customers, investors, and regulatory bodies.</p>
</div>

### Business Requirements Traceability

```mermaid
flowchart LR
    subgraph Business Goals
        BG1["Regulatory Compliance"]
        BG2["Cost Reduction"]
        BG3["Stakeholder Transparency"]
    end

    subgraph Success Metrics
        SM1["100% pipeline coverage"]
        SM2["15% cost reduction"]
        SM3["Monthly reports published"]
    end

    BG1 --> SM1
    BG2 --> SM2
    BG3 --> SM3

    style BG1 fill:#1e40af,stroke:#1e3a8a,color:#fff
    style BG2 fill:#1e40af,stroke:#1e3a8a,color:#fff
    style BG3 fill:#1e40af,stroke:#1e3a8a,color:#fff
    style SM1 fill:#dbeafe,stroke:#93c5fd,color:#1e3a8a
    style SM2 fill:#dbeafe,stroke:#93c5fd,color:#1e3a8a
    style SM3 fill:#dbeafe,stroke:#93c5fd,color:#1e3a8a
```

---

## 👤 2. User Requirements

User requirements describe the system from the perspective of the people who will interact with it. They define expected behaviors in natural language.

<div class="srs-card srs-card--user">
  <h3>UR-001: View Emission Trends</h3>
  <p><strong>Actor:</strong> DevOps Engineer</p>
  <p><strong>Description:</strong> As a DevOps engineer, I want to view CO₂ emission trends for my pipelines over the past 30 days so that I can identify which jobs are the biggest contributors.</p>
  <p><strong>Acceptance Criteria:</strong></p>
  <ul>
    <li>Dashboard displays a line chart of daily emissions</li>
    <li>User can filter by project, branch, or job name</li>
    <li>Data refreshes within 5 minutes of pipeline completion</li>
  </ul>
</div>

<div class="srs-card srs-card--user">
  <h3>UR-002: Receive Optimization Alerts</h3>
  <p><strong>Actor:</strong> Team Lead</p>
  <p><strong>Description:</strong> As a team lead, I want to receive alerts when a pipeline exceeds emission thresholds so that I can prioritize optimization before the next sprint.</p>
  <p><strong>Acceptance Criteria:</strong></p>
  <ul>
    <li>Configurable threshold per project (kg CO₂ per build)</li>
    <li>Alerts delivered via GitLab notification and email</li>
    <li>Alert includes specific job and recommended action</li>
  </ul>
</div>

<div class="srs-card srs-card--user">
  <h3>UR-003: Generate Compliance Reports</h3>
  <p><strong>Actor:</strong> Sustainability Officer</p>
  <p><strong>Description:</strong> As a sustainability officer, I want to generate monthly compliance reports with one click so that I can submit them to regulatory bodies without manual data aggregation.</p>
  <p><strong>Acceptance Criteria:</strong></p>
  <ul>
    <li>Report includes total emissions, energy usage, and trend analysis</li>
    <li>Exportable as PDF and CSV</li>
    <li>Signed with generation timestamp for audit trail</li>
  </ul>
</div>

### User Journey Map

```mermaid
journey
    title DevOps Engineer - Daily Sustainability Workflow
    section Morning Review
      Open EcoGuard Dashboard: 5: DevOps Engineer
      Check overnight emission trends: 4: DevOps Engineer
      Review optimization alerts: 3: DevOps Engineer
    section During Development
      Push code and trigger pipeline: 5: DevOps Engineer
      Monitor live emission tracking: 4: DevOps Engineer
      Apply recommended optimizations: 4: DevOps Engineer
    section End of Sprint
      Generate sustainability report: 5: DevOps Engineer
      Share with team lead: 4: DevOps Engineer, Team Lead
```

---

## ⚙️ 3. Functional Requirements

Functional requirements define the specific behaviors, features, and functions the system must perform.

<div class="srs-card srs-card--functional">
  <h3>FR-001: Pipeline Data Collection</h3>
  <p><strong>Traces to:</strong> UR-001, BR-001</p>
  <p><strong>Description:</strong> The system shall automatically collect job-level metadata (duration, runner type, resource usage) from GitLab CI/CD pipelines via the GitLab REST API.</p>
  <p><strong>Input:</strong> GitLab project ID, API token</p>
  <p><strong>Output:</strong> Structured JSON containing job metrics per pipeline run</p>
  <p><strong>Processing:</strong></p>
  <ol>
    <li>Query <code>/api/v4/projects/:id/pipelines</code> for recent pipelines</li>
    <li>For each pipeline, fetch individual job details</li>
    <li>Extract duration, runner tags, artifacts size, and status</li>
    <li>Store normalized data in <code>dashboards/data/</code></li>
  </ol>
</div>

<div class="srs-card srs-card--functional">
  <h3>FR-002: Carbon Emission Calculation</h3>
  <p><strong>Traces to:</strong> UR-001, BR-001</p>
  <p><strong>Description:</strong> The system shall calculate CO₂ emissions for each pipeline job using the formula:</p>
  <div class="formula-box">
    CO₂ (kg) = Energy (kWh) × Carbon Intensity (gCO₂/kWh) ÷ 1000
  </div>
  <p>Where Energy = Duration (hours) × Power Draw (kW) and Carbon Intensity is fetched from the Electricity Maps API for the runner's region.</p>
</div>

<div class="srs-card srs-card--functional">
  <h3>FR-003: Optimization Agent</h3>
  <p><strong>Traces to:</strong> UR-002, BR-002</p>
  <p><strong>Description:</strong> The system shall analyze pipeline efficiency and generate actionable recommendations including:</p>
  <ul>
    <li>Parallelization opportunities for sequential jobs</li>
    <li>Cache optimization for repeated dependency installations</li>
    <li>Runner right-sizing based on actual CPU/memory utilization</li>
    <li>Scheduling non-urgent jobs during low carbon intensity windows</li>
  </ul>
</div>

<div class="srs-card srs-card--functional">
  <h3>FR-004: Dashboard Visualization</h3>
  <p><strong>Traces to:</strong> UR-001, UR-003, BR-003</p>
  <p><strong>Description:</strong> The system shall render interactive dashboards with the following views:</p>
  <ul>
    <li>Daily/weekly/monthly emission trend charts</li>
    <li>Per-project and per-job breakdowns</li>
    <li>Sustainability goal progress indicators</li>
    <li>Carbon intensity heatmap by time of day</li>
  </ul>
</div>

<div class="srs-card srs-card--functional">
  <h3>FR-005: Eco-Friendly Deployment Scheduling</h3>
  <p><strong>Traces to:</strong> BR-001, BR-002</p>
  <p><strong>Description:</strong> The system shall recommend optimal deployment windows based on forecasted grid carbon intensity. When carbon intensity exceeds a configurable threshold, the system shall suggest delaying non-critical deployments.</p>
</div>

### Functional Decomposition

```mermaid
flowchart TD
    subgraph Data Layer
        F1["FR-001: Pipeline Data Collection"]
        F6["FR-006: Carbon Intensity Fetch"]
    end

    subgraph Processing Layer
        F2["FR-002: Emission Calculation"]
        F3["FR-003: Optimization Agent"]
        F5["FR-005: Deployment Scheduling"]
    end

    subgraph Presentation Layer
        F4["FR-004: Dashboard Visualization"]
        F7["FR-007: Report Generation"]
    end

    F1 --> F2
    F6 --> F2
    F2 --> F3
    F2 --> F4
    F2 --> F5
    F3 --> F4
    F5 --> F4
    F4 --> F7

    style F1 fill:#059669,stroke:#047857,color:#fff
    style F2 fill:#059669,stroke:#047857,color:#fff
    style F3 fill:#059669,stroke:#047857,color:#fff
    style F4 fill:#059669,stroke:#047857,color:#fff
    style F5 fill:#059669,stroke:#047857,color:#fff
    style F6 fill:#059669,stroke:#047857,color:#fff
    style F7 fill:#059669,stroke:#047857,color:#fff
```

---

## 🛡️ 4. Non-Functional Requirements (NFRs)

Non-functional requirements define the quality attributes and constraints that the system must satisfy.

<div class="nfr-grid">
  <div class="srs-card srs-card--nfr">
    <h3>⚡ Performance</h3>
    <table>
      <tr><td><strong>NFR-001</strong></td><td>Dashboard shall load within 3 seconds on a standard broadband connection</td></tr>
      <tr><td><strong>NFR-002</strong></td><td>Data collection for 100 pipelines shall complete within 60 seconds</td></tr>
      <tr><td><strong>NFR-003</strong></td><td>Emission calculations shall process within 500ms per job</td></tr>
    </table>
  </div>

  <div class="srs-card srs-card--nfr">
    <h3>🔒 Security</h3>
    <table>
      <tr><td><strong>NFR-004</strong></td><td>GitLab API tokens shall be stored as environment variables, never in source code</td></tr>
      <tr><td><strong>NFR-005</strong></td><td>All external API calls shall use HTTPS/TLS 1.2+</td></tr>
      <tr><td><strong>NFR-006</strong></td><td>Dashboard access shall respect GitLab project-level permissions</td></tr>
    </table>
  </div>

  <div class="srs-card srs-card--nfr">
    <h3>📈 Scalability</h3>
    <table>
      <tr><td><strong>NFR-007</strong></td><td>System shall handle data from up to 50 concurrent GitLab projects</td></tr>
      <tr><td><strong>NFR-008</strong></td><td>Historical data storage shall support at least 12 months of metrics</td></tr>
    </table>
  </div>

  <div class="srs-card srs-card--nfr">
    <h3>🔧 Maintainability</h3>
    <table>
      <tr><td><strong>NFR-009</strong></td><td>Codebase shall maintain a minimum of 80% test coverage</td></tr>
      <tr><td><strong>NFR-010</strong></td><td>All Python modules shall follow PEP 8 style guidelines</td></tr>
      <tr><td><strong>NFR-011</strong></td><td>Documentation shall be updated alongside every feature change</td></tr>
    </table>
  </div>

  <div class="srs-card srs-card--nfr">
    <h3>♿ Usability</h3>
    <table>
      <tr><td><strong>NFR-012</strong></td><td>Dashboard shall be responsive and usable on screens from 375px to 2560px</td></tr>
      <tr><td><strong>NFR-013</strong></td><td>Color palette shall meet WCAG 2.1 AA contrast standards</td></tr>
    </table>
  </div>

  <div class="srs-card srs-card--nfr">
    <h3>🔄 Reliability</h3>
    <table>
      <tr><td><strong>NFR-014</strong></td><td>System shall gracefully degrade if external APIs are unavailable</td></tr>
      <tr><td><strong>NFR-015</strong></td><td>Failed data collection jobs shall retry up to 3 times with exponential backoff</td></tr>
    </table>
  </div>
</div>

### NFR Quality Model

```mermaid
mindmap
  root((EcoGuard Quality))
    Performance
      Load time under 3s
      Processing under 500ms
      100 pipelines in 60s
    Security
      TLS 1.2+
      No hardcoded secrets
      Role-based access
    Scalability
      50 projects
      12 months history
    Maintainability
      80% test coverage
      PEP 8 compliance
      Living documentation
    Usability
      Responsive design
      WCAG 2.1 AA
    Reliability
      Graceful degradation
      Auto-retry with backoff
```

---

## 🔌 5. Interface Requirements

Interface requirements define how EcoGuard connects to external systems, APIs, and user-facing surfaces.

### 5.1 External API Interfaces

<div class="srs-card srs-card--interface">
  <h3>IR-001: GitLab REST API</h3>
  <p><strong>Direction:</strong> EcoGuard → GitLab</p>
  <p><strong>Protocol:</strong> HTTPS REST (JSON)</p>
  <p><strong>Authentication:</strong> Personal Access Token (PAT) via <code>GITLAB_TOKEN</code> environment variable</p>
  <p><strong>Endpoints Used:</strong></p>
  <ul>
    <li><code>GET /api/v4/projects/:id/pipelines</code> — List pipeline runs</li>
    <li><code>GET /api/v4/projects/:id/pipelines/:pipeline_id/jobs</code> — Job details</li>
    <li><code>GET /api/v4/projects/:id/issues</code> — Compliance issue tracking</li>
    <li><code>POST /api/v4/projects/:id/issues</code> — Create optimization recommendations</li>
  </ul>
  <p><strong>Rate Limits:</strong> Respects GitLab rate limit headers; implements retry with <code>Retry-After</code> header.</p>
</div>

<div class="srs-card srs-card--interface">
  <h3>IR-002: Electricity Maps API</h3>
  <p><strong>Direction:</strong> EcoGuard → Electricity Maps</p>
  <p><strong>Protocol:</strong> HTTPS REST (JSON)</p>
  <p><strong>Authentication:</strong> API key via <code>ELECTRICITY_MAPS_API_KEY</code> environment variable</p>
  <p><strong>Endpoints Used:</strong></p>
  <ul>
    <li><code>GET /v3/carbon-intensity/latest</code> — Current carbon intensity by zone</li>
    <li><code>GET /v3/carbon-intensity/forecast</code> — 72-hour forecast for deployment scheduling</li>
  </ul>
  <p><strong>Fallback:</strong> If the API is unavailable, use a default carbon intensity of 475 gCO₂/kWh (global average).</p>
</div>

### 5.2 Internal Interfaces

<div class="srs-card srs-card--interface">
  <h3>IR-003: Flask API Server</h3>
  <p><strong>Direction:</strong> Dashboard ↔ Backend</p>
  <p><strong>Protocol:</strong> HTTP REST (JSON)</p>
  <p><strong>Endpoints:</strong></p>
  <ul>
    <li><code>GET /api/metrics/daily</code> — Daily metrics summary</li>
    <li><code>GET /api/metrics/weekly</code> — Weekly metrics summary</li>
    <li><code>GET /api/metrics/monthly</code> — Monthly metrics summary</li>
    <li><code>GET /api/summary</code> — Overall project summary</li>
    <li><code>GET /api/goals</code> — Sustainability goal progress</li>
  </ul>
</div>

### 5.3 User Interface

<div class="srs-card srs-card--interface">
  <h3>IR-004: Web Dashboard</h3>
  <p><strong>Technology:</strong> HTML5, CSS3, JavaScript with Chart.js / D3.js</p>
  <p><strong>Supported Browsers:</strong> Chrome 90+, Firefox 88+, Safari 14+, Edge 90+</p>
  <p><strong>Responsive Breakpoints:</strong></p>
  <ul>
    <li>Mobile: 375px – 768px</li>
    <li>Tablet: 769px – 1024px</li>
    <li>Desktop: 1025px+</li>
  </ul>
</div>

### Interface Architecture

```mermaid
flowchart LR
    subgraph External
        GL["GitLab API"]
        EM["Electricity Maps API"]
    end

    subgraph EcoGuard
        DC["Data Collector"]
        AG["Agent Engine"]
        API["Flask API"]
        DB["JSON Storage"]
    end

    subgraph Presentation
        DASH["Web Dashboard"]
        DOCS["VitePress Docs"]
    end

    GL -->|REST/JSON| DC
    EM -->|REST/JSON| DC
    DC --> DB
    DB --> AG
    AG --> DB
    DB --> API
    API -->|REST/JSON| DASH
    DB --> DOCS

    style GL fill:#fc6d26,stroke:#e24329,color:#fff
    style EM fill:#16a34a,stroke:#15803d,color:#fff
    style DC fill:#2563eb,stroke:#1d4ed8,color:#fff
    style AG fill:#2563eb,stroke:#1d4ed8,color:#fff
    style API fill:#2563eb,stroke:#1d4ed8,color:#fff
    style DB fill:#2563eb,stroke:#1d4ed8,color:#fff
    style DASH fill:#7c3aed,stroke:#6d28d9,color:#fff
    style DOCS fill:#7c3aed,stroke:#6d28d9,color:#fff
```

---

## 🔧 Requirements Management with OSRMT

**OSRMT (Open-Source Requirements Management Tool)** is used to gather, organize, trace, and validate all requirements throughout the project lifecycle.

### Why OSRMT?

<div class="osrmt-benefits">
  <div class="srs-card">
    <h3>📋 Structured Capture</h3>
    <p>OSRMT provides a tree-based hierarchy to organize requirements into categories (Business, User, Functional, NFR, Interface) with unique identifiers for traceability.</p>
  </div>
  <div class="srs-card">
    <h3>🔗 Traceability Matrix</h3>
    <p>Every requirement is linked to its parent (upstream traceability) and its implementation artifacts like test cases and code modules (downstream traceability).</p>
  </div>
  <div class="srs-card">
    <h3>📊 Change Tracking</h3>
    <p>OSRMT logs every modification with timestamps, authors, and justifications — creating a complete audit trail for compliance and review.</p>
  </div>
  <div class="srs-card">
    <h3>✅ Validation & Verification</h3>
    <p>Requirements are tagged with validation status (Draft → Reviewed → Approved → Implemented → Verified) to track progress through the lifecycle.</p>
  </div>
</div>

### OSRMT Workflow for EcoGuard

```mermaid
flowchart TD
    A["1. Import Requirements"] --> B["2. Categorize by Type"]
    B --> C["3. Assign Priority & Owner"]
    C --> D["4. Create Traceability Links"]
    D --> E["5. Review & Approve"]
    E --> F["6. Track Implementation"]
    F --> G["7. Verify & Validate"]
    G --> H["8. Generate Reports"]

    style A fill:#2563eb,stroke:#1d4ed8,color:#fff
    style B fill:#2563eb,stroke:#1d4ed8,color:#fff
    style C fill:#7c3aed,stroke:#6d28d9,color:#fff
    style D fill:#7c3aed,stroke:#6d28d9,color:#fff
    style E fill:#059669,stroke:#047857,color:#fff
    style F fill:#059669,stroke:#047857,color:#fff
    style G fill:#d97706,stroke:#b45309,color:#fff
    style H fill:#d97706,stroke:#b45309,color:#fff
```

### Full Traceability Matrix

| Req ID | Type | Traces To | Status | Owner |
|---|---|---|---|---|
| BR-001 | Business | UR-001, UR-003 | Approved | Product Owner |
| BR-002 | Business | UR-002 | Approved | Product Owner |
| BR-003 | Business | UR-003 | Approved | Product Owner |
| UR-001 | User | FR-001, FR-002, FR-004 | Approved | DevOps Lead |
| UR-002 | User | FR-003 | Approved | DevOps Lead |
| UR-003 | User | FR-004, FR-007 | Approved | Sustainability Officer |
| FR-001 | Functional | IR-001 | Implemented | Backend Dev |
| FR-002 | Functional | IR-001, IR-002 | Implemented | Backend Dev |
| FR-003 | Functional | — | Implemented | Backend Dev |
| FR-004 | Functional | IR-003, IR-004 | Implemented | Frontend Dev |
| FR-005 | Functional | IR-002 | Implemented | Backend Dev |
| NFR-001 | Non-Functional | FR-004 | Verified | QA Lead |
| NFR-004 | Non-Functional | IR-001, IR-002 | Verified | Security Lead |
| IR-001 | Interface | FR-001, FR-002 | Verified | Backend Dev |
| IR-002 | Interface | FR-002, FR-005 | Verified | Backend Dev |

---

## 📊 Requirements Summary

<div class="summary-grid">
  <div class="summary-item summary-item--business">
    <span class="summary-count">3</span>
    <span class="summary-label">Business Requirements</span>
  </div>
  <div class="summary-item summary-item--user">
    <span class="summary-count">3</span>
    <span class="summary-label">User Requirements</span>
  </div>
  <div class="summary-item summary-item--functional">
    <span class="summary-count">5+</span>
    <span class="summary-label">Functional Requirements</span>
  </div>
  <div class="summary-item summary-item--nfr">
    <span class="summary-count">15</span>
    <span class="summary-label">Non-Functional Requirements</span>
  </div>
  <div class="summary-item summary-item--interface">
    <span class="summary-count">4</span>
    <span class="summary-label">Interface Requirements</span>
  </div>
</div>

<style>
.srs-hero {
  text-align: center;
  padding: 2.5rem 1.5rem;
  margin: 1.5rem 0 2rem;
  background: linear-gradient(135deg, var(--vp-c-brand-soft), transparent 60%);
  border-radius: 20px;
  border: 1px solid var(--vp-c-divider);
}
.srs-hero-eyebrow {
  font-size: 0.85rem;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--vp-c-brand-1);
  margin-bottom: 0.8rem;
  font-weight: 600;
}
.srs-hero-title {
  font-size: 1.55rem;
  line-height: 1.25;
  color: var(--vp-c-text-1);
  margin: 0 auto 1rem;
  max-width: 720px;
  letter-spacing: -0.03em;
}
.srs-hero-subtitle {
  color: var(--vp-c-text-2);
  max-width: 640px;
  margin: 0 auto;
  line-height: 1.6;
}

.srs-card {
  padding: 1.25rem 1.5rem;
  margin: 1rem 0;
  border-radius: 14px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.srs-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 32px rgba(0,0,0,0.08);
}
.srs-card h3 { margin-top: 0; margin-bottom: 0.6rem; font-size: 1.1rem; }
.srs-card p { margin: 0.4rem 0; line-height: 1.6; }
.srs-card ul, .srs-card ol { margin: 0.5rem 0; padding-left: 1.2rem; }
.srs-card table { width: 100%; margin: 0.5rem 0; }
.srs-card table td { padding: 0.4rem 0.6rem; border-bottom: 1px solid var(--vp-c-divider); }
.srs-card table td:first-child { font-weight: 600; white-space: nowrap; width: 100px; }

.srs-card--business { border-left: 4px solid #1e40af; }
.srs-card--user { border-left: 4px solid #7c3aed; }
.srs-card--functional { border-left: 4px solid #059669; }
.srs-card--nfr { border-left: 4px solid #d97706; }
.srs-card--interface { border-left: 4px solid #dc2626; }

.priority-badge {
  display: inline-block;
  padding: 2px 10px;
  border-radius: 999px;
  font-size: 0.8rem;
  font-weight: 700;
}
.priority-critical { background: rgba(220,38,38,0.12); color: #b91c1c; }
.priority-high { background: rgba(217,119,6,0.12); color: #b45309; }

.nfr-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(340px, 1fr));
  gap: 1rem;
}

.formula-box {
  padding: 1rem 1.5rem;
  margin: 0.8rem 0;
  border-radius: 10px;
  background: rgba(37,99,235,0.06);
  border: 1px solid rgba(37,99,235,0.15);
  font-family: 'IBM Plex Mono', monospace;
  font-size: 0.95rem;
  text-align: center;
  font-weight: 600;
  color: var(--vp-c-text-1);
}

.osrmt-benefits {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1rem;
}

.summary-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 1rem;
  margin: 1.5rem 0;
}
.summary-item {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.4rem;
  padding: 1.5rem 1rem;
  border-radius: 16px;
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  transition: transform 0.2s ease;
}
.summary-item:hover { transform: translateY(-3px); }
.summary-count { font-size: 2.2rem; font-weight: 800; letter-spacing: -0.04em; }
.summary-label { font-size: 0.82rem; text-transform: uppercase; letter-spacing: 0.06em; color: var(--vp-c-text-3); text-align: center; }

.summary-item--business .summary-count { color: #1e40af; }
.summary-item--user .summary-count { color: #7c3aed; }
.summary-item--functional .summary-count { color: #059669; }
.summary-item--nfr .summary-count { color: #d97706; }
.summary-item--interface .summary-count { color: #dc2626; }

@media (max-width: 768px) {
  .nfr-grid, .osrmt-benefits { grid-template-columns: 1fr; }
  .summary-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>
