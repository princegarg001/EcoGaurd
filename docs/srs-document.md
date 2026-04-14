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

## 🤖 6. AI-Assisted Requirements (Comparison)

To enhance the system's capabilities beyond manual rule-based logic, the following AI-assisted requirements are introduced to compare against traditional manual features. These features aim to reduce human bottleneck by automating complex pattern recognition and code modification.

> **AI-Assisted vs. Manual:** Each AI requirement below directly supersedes or augments a manual requirement, offering greater adaptability, speed, and scale — at the cost of added complexity, compute overhead, and governance concerns.

<div class="srs-card srs-card--functional">
  <h3>AI-FR-001: Predictive Emission Forecasting</h3>
  <p><strong>Compared to:</strong> Manual trend review (UR-001)</p>
  <p><strong>Description:</strong> Instead of relying solely on past data visualization for manual review, the system shall utilize machine learning models (e.g., LSTM time-series or Prophet) to forecast future carbon emissions up to 7 days ahead. This includes predicting energy spikes during seasonal traffic increases, large code branch merges, or scheduled release cycles.</p>
  <p><strong>Input:</strong> Historical emission time-series data per project (minimum 30 days), runner metadata, calendar events</p>
  <p><strong>Output:</strong> Probabilistic emission forecast with confidence intervals, surfaced in the dashboard and triggering pre-emptive scheduling recommendations</p>
  <p><strong>Acceptance Criteria:</strong></p>
  <ul>
    <li>Forecasts shall achieve a Mean Absolute Percentage Error (MAPE) ≤ 15% on a rolling 7-day horizon</li>
    <li>Predictions are refreshed automatically after each new pipeline run completes</li>
    <li>A confidence band (80% interval) must accompany every forecast shown in the UI</li>
    <li>If training data is insufficient (&lt; 30 data points), the system shall display a manual trend chart and suppress AI forecasts</li>
  </ul>
  <p><strong>AI Technology:</strong> Facebook Prophet / LSTM via scikit-learn or TensorFlow Lite; model artifacts versioned in the repository</p>
  <p><strong>NFR References:</strong> NFR-016 (determinism), NFR-018 (benchmarking)</p>
</div>

<div class="srs-card srs-card--functional">
  <h3>AI-FR-002: Intelligent Remediation Generation</h3>
  <p><strong>Compared to:</strong> Static Optimization Agent (FR-003)</p>
  <p><strong>Description:</strong> While the manual agent highlights issues via static rules, the AI-assisted system shall employ an LLM-based agent (e.g., GitLab Duo / OpenAI GPT-4o) to contextualize pipeline failures and inefficiencies. It must generate automated merge requests with context-aware, code-level optimizations — rewriting `.gitlab-ci.yml` and Dockerfile configurations — to directly reduce the carbon footprint without requiring a developer's initial draft.</p>
  <p><strong>Input:</strong> Raw `.gitlab-ci.yml` content, job duration logs, CPU/memory utilization metrics, identified inefficiency categories from FR-003</p>
  <p><strong>Output:</strong> A fully formed merge request containing patched CI/CD configuration files, inline comments explaining each change, and an estimated emission reduction percentage</p>
  <p><strong>Acceptance Criteria:</strong></p>
  <ul>
    <li>Generated merge requests must pass automated CI syntax validation before being opened</li>
    <li>Each MR description must include a carbon saving estimate (kg CO₂) and a confidence score</li>
    <li>Remediation suggestions must not remove any job flagged as a required status check</li>
    <li>Human approval is mandatory before any AI-generated MR is merged (human-in-the-loop gate)</li>
    <li>The system shall achieve ≥ 70% MR acceptance rate measured over a rolling 30-day window</li>
  </ul>
  <p><strong>AI Technology:</strong> LLM API (GitLab Duo / OpenAI GPT-4o) with structured output / function calling; prompt templates version-controlled</p>
  <p><strong>NFR References:</strong> NFR-017 (sandboxed fallback), NFR-018 (benchmarking)</p>
</div>

<div class="srs-card srs-card--functional">
  <h3>AI-FR-003: Dynamic Anomaly Detection</h3>
  <p><strong>Compared to:</strong> Static Threshold Alerts (UR-002)</p>
  <p><strong>Description:</strong> Rather than relying on rigid, pre-configured high-emission thresholds, the system shall train an unsupervised anomaly detection model (e.g., Isolation Forest or DBSCAN) on the historical baseline behaviour of each specific CI/CD pipeline. Alerts are raised automatically for statistically anomalous deviations, adapting to evolving pipeline structures without manual threshold updates.</p>
  <p><strong>Input:</strong> Per-job emission time-series, pipeline structural metadata (job count, parallelism), runner utilization rates</p>
  <p><strong>Output:</strong> Anomaly score per pipeline run (0–1), binary alert flag, and a human-readable root-cause hypothesis surfaced to the team lead</p>
  <p><strong>Acceptance Criteria:</strong></p>
  <ul>
    <li>Model retrains automatically every 7 days or after 500 new pipeline runs, whichever comes first</li>
    <li>False-positive rate shall remain below 10% measured against a manually labelled validation set</li>
    <li>Anomaly alerts must fire within 5 minutes of pipeline completion (same as UR-001 data freshness SLA)</li>
    <li>The system must surface the top-3 contributing jobs to each anomaly in the alert payload</li>
    <li>Baseline model bootstrapping requires a minimum of 50 pipeline runs; system falls back to static thresholds during the cold-start period</li>
  </ul>
  <p><strong>AI Technology:</strong> scikit-learn Isolation Forest; model serialized with joblib and stored in <code>models/</code></p>
  <p><strong>NFR References:</strong> NFR-016 (determinism), NFR-017 (fallback), NFR-018 (benchmarking)</p>
</div>

<div class="srs-card srs-card--functional">
  <h3>AI-FR-004: Context-Aware Documentation & Compliance</h3>
  <p><strong>Compared to:</strong> Manual Report Generation (UR-003)</p>
  <p><strong>Description:</strong> The system shall auto-generate detailed, narrative-driven compliance reports formatted specifically for varying regulatory bodies (EU CSRD, ISO 14064, GHG Protocol). An LLM layer translates raw emission metrics into structured audit narratives, shifting the manual burden of compiling different data sets for different audits entirely to AI.</p>
  <p><strong>Input:</strong> Aggregated monthly emission metrics, sustainability goals progress data, regulatory body selector (EU / ISO / GHG), organization profile</p>
  <p><strong>Output:</strong> A formatted PDF/DOCX report with executive summary, data tables, trend narrative, methodology disclosure, and digital audit signature</p>
  <p><strong>Acceptance Criteria:</strong></p>
  <ul>
    <li>Report must be generated and available for download within 60 seconds of user request</li>
    <li>All numerical data in the narrative must be validated against the source JSON with a ±0.01 kg CO₂ tolerance — no AI hallucination of figures permitted</li>
    <li>Every report shall include a machine-readable JSON-LD metadata block for automated regulatory ingestion</li>
    <li>The system shall support at minimum three output formats: PDF, DOCX, and CSV</li>
    <li>Narrative text quality shall be reviewed via automated Flesch-Kincaid readability scoring (target grade level ≤ 12)</li>
  </ul>
  <p><strong>AI Technology:</strong> LLM with retrieval-augmented generation (RAG) over the organization's emission data; output grounded and fact-checked before rendering</p>
  <p><strong>NFR References:</strong> NFR-016 (determinism), NFR-017 (sandboxed fallback)</p>
</div>

### AI Requirements Lifecycle Flow

```mermaid
flowchart TD
    subgraph Data Ingestion
        D1["Pipeline Metrics\n(FR-001)"]
        D2["Carbon Intensity\n(IR-002)"]
        D3["Historical Baseline\n(12-month store)"]
    end

    subgraph AI Processing Layer
        AI1["AI-FR-001\nPredictive Forecasting\n(Prophet / LSTM)"]
        AI2["AI-FR-002\nRemediation Generation\n(LLM Agent)"]
        AI3["AI-FR-003\nAnomaly Detection\n(Isolation Forest)"]
        AI4["AI-FR-004\nCompliance Docs\n(LLM + RAG)"]
    end

    subgraph Validation Gate
        V1["Sandbox Validator\n(NFR-017)"]
        V2["Consistency Monitor\n(NFR-018)"]
    end

    subgraph Output
        O1["Dashboard Forecast\nChart"]
        O2["Auto MR /\nCode Patch"]
        O3["Anomaly Alert\n+ Root Cause"]
        O4["Regulatory PDF\nReport"]
    end

    D1 --> AI1 & AI2 & AI3
    D2 --> AI1
    D3 --> AI1 & AI3
    D1 --> AI4

    AI1 --> V2 --> O1
    AI2 --> V1 --> O2
    AI3 --> V2 --> O3
    AI4 --> V1 --> O4

    style AI1 fill:#7c3aed,stroke:#6d28d9,color:#fff
    style AI2 fill:#7c3aed,stroke:#6d28d9,color:#fff
    style AI3 fill:#7c3aed,stroke:#6d28d9,color:#fff
    style AI4 fill:#7c3aed,stroke:#6d28d9,color:#fff
    style V1 fill:#d97706,stroke:#b45309,color:#fff
    style V2 fill:#d97706,stroke:#b45309,color:#fff
    style O1 fill:#059669,stroke:#047857,color:#fff
    style O2 fill:#059669,stroke:#047857,color:#fff
    style O3 fill:#059669,stroke:#047857,color:#fff
    style O4 fill:#059669,stroke:#047857,color:#fff
```

---

## ⚖️ 7. Conclusion: Manual vs. AI-Assisted Execution

When evaluating the platform's execution, there are distinct trade-offs between manual (rule-based) approaches and AI-assisted workflows. A successful implementation requires balancing the precision of manual rules with the adaptability of AI. The conclusions drawn below are informed by the four paired requirement comparisons documented in Section 6.

<div class="osrmt-benefits">
  <div class="srs-card">
    <h3>📉 Limitations of Manual Execution</h3>
    <ul>
      <li><strong>Scalability lag:</strong> Manual review of pipeline emissions becomes unmanageable across hundreds of repositories. Team leads simply cannot review every job log.</li>
      <li><strong>Cognitive Overload:</strong> Engineers are forced to interpret raw data and manually translate insights into code changes — a high-effort, low-leverage activity.</li>
      <li><strong>Static Rules:</strong> Heuristics for optimization cannot adapt to unique pipeline structures without constant, labor-intensive human updates.</li>
      <li><strong>Delayed Action:</strong> Reporting and remediation completely depend on human time availability, drastically delaying potential energy savings.</li>
      <li><strong>Threshold Drift:</strong> Manually configured emission thresholds become stale as pipelines evolve, leading to alert fatigue from false positives or missed anomalies.</li>
      <li><strong>Inconsistent Reporting Quality:</strong> Human-compiled compliance documents vary in structure, depth, and language across reporters, creating audit trail inconsistencies.</li>
    </ul>
  </div>
  <div class="srs-card">
    <h3>⚠️ Limitations of AI-Assisted Execution</h3>
    <ul>
      <li><strong>Consistency lag:</strong> AI models exhibit non-deterministic behavior, proposing completely different code optimizations for the exact same pipeline data over time.</li>
      <li><strong>Compute Overhead:</strong> Running LLMs for code optimization generates its own severe carbon footprint, which can ironically outweigh the pipeline energy savings if not metered carefully.</li>
      <li><strong>Hallucinations:</strong> The AI may confidently suggest invalid configuration changes that structurally break CI/CD pipelines or fabricate emission figures in reports.</li>
      <li><strong>Data Privacy:</strong> Sending proprietary CI/CD logs and internal code to external LLM providers introduces significant data governance and IP risks.</li>
      <li><strong>Cold-Start Problem:</strong> AI models for anomaly detection and forecasting require substantial historical data (30–50+ pipeline runs) before producing reliable outputs.</li>
      <li><strong>Model Drift:</strong> Without continuous retraining, AI models degrade in accuracy as pipeline structures and team workflows evolve, requiring ongoing MLOps investment.</li>
    </ul>
  </div>
</div>

### Consistency Assurance Requirements

To heavily mitigate the consistency and reliability lags identified in AI-assisted execution, the following hard safeguards are implemented:

<div class="srs-card srs-card--nfr">
  <h3>NFR-016: AI Output Consistency & Determinism</h3>
  <p><strong>Description:</strong> The system shall enforce deterministic parameter settings (e.g., Temperature = 0.0, strict seed values) for all analytical LLM requests. This ensures maximum determination, yielding highly consistent optimization recommendations for identical inputs every time.</p>
</div>

<div class="srs-card srs-card--nfr">
  <h3>NFR-017: Fallback to Manual Heuristics (Sandboxing)</h3>
  <p><strong>Description:</strong> The system shall securely evaluate all AI-generated code optimizations using an isolated sandboxed validation test. If the AI output fails automated syntax and logic validation, the system must instantly override the AI and transparently fall back to the manual rule-based logic (FR-003).</p>
</div>

<div class="srs-card srs-card--nfr">
  <h3>NFR-018: Continuous LLM Benchmarking</h3>
  <p><strong>Description:</strong> The system shall automatically log and test the acceptance rate and output variance of the LLM responses over time, establishing an internal confidence score. If the score drops below 85% consistency, AI capabilities for that module will automatically disable.</p>
</div>

### Strategic Recommendations

Based on the comparative analysis above, the following strategies are recommended to harness AI benefits while preserving the reliability of manual baselines:

<div class="strategy-grid">
  <div class="srs-card srs-card--business">
    <h3>🔬 Hybrid Execution Model</h3>
    <p>Deploy AI and manual systems in parallel rather than replacing one with the other. AI handles high-volume pattern recognition tasks; manual rules serve as the authoritative fallback and override mechanism. Neither system is exclusively trusted.</p>
  </div>
  <div class="srs-card srs-card--business">
    <h3>🧑‍⚖️ Human-in-the-Loop Gates</h3>
    <p>All AI-generated merge requests, anomaly alerts above severity level 2, and compliance reports must receive explicit human approval before being acted upon. This prevents automated changes from propagating through production pipelines unchecked.</p>
  </div>
  <div class="srs-card srs-card--business">
    <h3>🌍 On-Premise / Local LLM Priority</h3>
    <p>To mitigate data privacy concerns, the architecture shall prefer self-hosted or on-premise LLM deployments (e.g., Ollama + Llama 3) for tasks involving proprietary pipeline code. External API calls are reserved for non-sensitive analytical tasks only.</p>
  </div>
  <div class="srs-card srs-card--business">
    <h3>📏 AI Carbon Accounting</h3>
    <p>The platform shall measure and report the AI subsystem's own energy consumption as a separate dashboard metric. This ensures that AI-driven optimizations deliver a net-positive carbon outcome — the AI must save more emissions than it consumes.</p>
  </div>
</div>

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
    <span class="summary-count">9+</span>
    <span class="summary-label">Functional Requirements</span>
  </div>
  <div class="summary-item summary-item--nfr">
    <span class="summary-count">18</span>
    <span class="summary-label">Non-Functional Requirements</span>
  </div>
  <div class="summary-item summary-item--interface">
    <span class="summary-count">4</span>
    <span class="summary-label">Interface Requirements</span>
  </div>
</div>

---

## 📋 8. Manual vs. AI-Assisted: Comparison Table

The table below provides a definitive, side-by-side evaluation of all four paired requirements across six evaluation dimensions.

<div class="comparison-wrapper">
  <div class="comparison-header">
    <div class="comparison-header-cell comparison-header-dim">Dimension</div>
    <div class="comparison-header-cell comparison-header-manual">🔧 Manual Approach</div>
    <div class="comparison-header-cell comparison-header-ai">🤖 AI-Assisted Approach</div>
    <div class="comparison-header-cell comparison-header-verdict">Verdict</div>
  </div>

  <div class="comparison-section-label">📈 Emission Forecasting (UR-001 vs AI-FR-001)</div>
  <div class="comparison-row">
    <div class="comparison-cell comparison-dim">Accuracy</div>
    <div class="comparison-cell comparison-manual">Retroactive only — shows past trends with no predictive capability</div>
    <div class="comparison-cell comparison-ai">MAPE ≤ 15% on 7-day horizon with probabilistic confidence bands</div>
    <div class="comparison-cell comparison-verdict verdict-ai">✅ AI Wins</div>
  </div>
  <div class="comparison-row comparison-row-alt">
    <div class="comparison-cell comparison-dim">Response Time</div>
    <div class="comparison-cell comparison-manual">Immediate (static chart render)</div>
    <div class="comparison-cell comparison-ai">Model inference adds 2–5 seconds per prediction</div>
    <div class="comparison-cell comparison-verdict verdict-manual">✅ Manual Wins</div>
  </div>
  <div class="comparison-row">
    <div class="comparison-cell comparison-dim">Adaptability</div>
    <div class="comparison-cell comparison-manual">None — historical aggregation only</div>
    <div class="comparison-cell comparison-ai">Retrains on new data automatically every 7 days</div>
    <div class="comparison-cell comparison-verdict verdict-ai">✅ AI Wins</div>
  </div>
  <div class="comparison-row comparison-row-alt">
    <div class="comparison-cell comparison-dim">Data Requirement</div>
    <div class="comparison-cell comparison-manual">Works from day 1 with any data volume</div>
    <div class="comparison-cell comparison-ai">Requires ≥ 30 pipeline runs to bootstrap; cold-start gap</div>
    <div class="comparison-cell comparison-verdict verdict-manual">✅ Manual Wins</div>
  </div>

  <div class="comparison-section-label">🔧 Pipeline Optimization (FR-003 vs AI-FR-002)</div>
  <div class="comparison-row">
    <div class="comparison-cell comparison-dim">Automation Depth</div>
    <div class="comparison-cell comparison-manual">Identifies issues; developer must manually implement fixes</div>
    <div class="comparison-cell comparison-ai">Auto-generates merge requests with ready-to-merge code patches</div>
    <div class="comparison-cell comparison-verdict verdict-ai">✅ AI Wins</div>
  </div>
  <div class="comparison-row comparison-row-alt">
    <div class="comparison-cell comparison-dim">Reliability</div>
    <div class="comparison-cell comparison-manual">Deterministic — same input always yields same recommendation</div>
    <div class="comparison-cell comparison-ai">Non-deterministic — Temperature = 0.0 mitigates but cannot eliminate variance</div>
    <div class="comparison-cell comparison-verdict verdict-manual">✅ Manual Wins</div>
  </div>
  <div class="comparison-row">
    <div class="comparison-cell comparison-dim">Scalability</div>
    <div class="comparison-cell comparison-manual">Linear human cost per additional repository</div>
    <div class="comparison-cell comparison-ai">Near-constant LLM cost; handles hundreds of repos concurrently</div>
    <div class="comparison-cell comparison-verdict verdict-ai">✅ AI Wins</div>
  </div>
  <div class="comparison-row comparison-row-alt">
    <div class="comparison-cell comparison-dim">Risk of Error</div>
    <div class="comparison-cell comparison-manual">Low — recommendations are audited heuristics</div>
    <div class="comparison-cell comparison-ai">High — LLM hallucinations may break pipelines; sandbox gate required</div>
    <div class="comparison-cell comparison-verdict verdict-manual">✅ Manual Wins</div>
  </div>

  <div class="comparison-section-label">🚨 Anomaly Detection (UR-002 vs AI-FR-003)</div>
  <div class="comparison-row">
    <div class="comparison-cell comparison-dim">Alert Precision</div>
    <div class="comparison-cell comparison-manual">Fixed thresholds cause alert fatigue as pipelines drift</div>
    <div class="comparison-cell comparison-ai">Adaptive baseline; false-positive rate &lt; 10%</div>
    <div class="comparison-cell comparison-verdict verdict-ai">✅ AI Wins</div>
  </div>
  <div class="comparison-row comparison-row-alt">
    <div class="comparison-cell comparison-dim">Setup Complexity</div>
    <div class="comparison-cell comparison-manual">Simple — configure one threshold per project</div>
    <div class="comparison-cell comparison-ai">Requires model training pipeline, MLOps tooling, and retraining schedule</div>
    <div class="comparison-cell comparison-verdict verdict-manual">✅ Manual Wins</div>
  </div>
  <div class="comparison-row">
    <div class="comparison-cell comparison-dim">Root-Cause Insight</div>
    <div class="comparison-cell comparison-manual">Alert only — no attribution to specific contributing jobs</div>
    <div class="comparison-cell comparison-ai">Surfaces top-3 contributing jobs with anomaly scores in alert payload</div>
    <div class="comparison-cell comparison-verdict verdict-ai">✅ AI Wins</div>
  </div>
  <div class="comparison-row comparison-row-alt">
    <div class="comparison-cell comparison-dim">Compute Cost</div>
    <div class="comparison-cell comparison-manual">Near-zero — threshold comparison only</div>
    <div class="comparison-cell comparison-ai">Model inference per pipeline run; retraining every 7 days adds overhead</div>
    <div class="comparison-cell comparison-verdict verdict-manual">✅ Manual Wins</div>
  </div>

  <div class="comparison-section-label">📄 Compliance Reporting (UR-003 vs AI-FR-004)</div>
  <div class="comparison-row">
    <div class="comparison-cell comparison-dim">Effort Required</div>
    <div class="comparison-cell comparison-manual">Hours of manual data compilation and narrative writing per report</div>
    <div class="comparison-cell comparison-ai">Generated in ≤ 60 seconds from a single user click</div>
    <div class="comparison-cell comparison-verdict verdict-ai">✅ AI Wins</div>
  </div>
  <div class="comparison-row comparison-row-alt">
    <div class="comparison-cell comparison-dim">Regulatory Adaptability</div>
    <div class="comparison-cell comparison-manual">Static template — one format for all auditors</div>
    <div class="comparison-cell comparison-ai">Dynamic templates per regulatory body (EU CSRD, ISO 14064, GHG Protocol)</div>
    <div class="comparison-cell comparison-verdict verdict-ai">✅ AI Wins</div>
  </div>
  <div class="comparison-row">
    <div class="comparison-cell comparison-dim">Data Accuracy</div>
    <div class="comparison-cell comparison-manual">Human-verified figures; low hallucination risk</div>
    <div class="comparison-cell comparison-ai">RAG-grounded; figures validated ±0.01 kg CO₂ — hallucination remains a residual risk</div>
    <div class="comparison-cell comparison-verdict verdict-manual">✅ Manual Wins</div>
  </div>
  <div class="comparison-row comparison-row-alt">
    <div class="comparison-cell comparison-dim">Data Privacy</div>
    <div class="comparison-cell comparison-manual">Data stays entirely on-premise</div>
    <div class="comparison-cell comparison-ai">External LLM API calls risk exposing proprietary metrics unless on-premise LLM is used</div>
    <div class="comparison-cell comparison-verdict verdict-manual">✅ Manual Wins</div>
  </div>

  <div class="comparison-section-label">🏆 Overall Scorecard</div>
  <div class="comparison-row comparison-row-score">
    <div class="comparison-cell comparison-dim"><strong>Dimensions Won</strong></div>
    <div class="comparison-cell comparison-manual score-manual"><strong>8 / 16</strong></div>
    <div class="comparison-cell comparison-ai score-ai"><strong>8 / 16</strong></div>
    <div class="comparison-cell comparison-verdict verdict-tie">🤝 Tied</div>
  </div>
  <div class="comparison-row comparison-row-alt comparison-row-score">
    <div class="comparison-cell comparison-dim"><strong>Best Use Case</strong></div>
    <div class="comparison-cell comparison-manual">Deterministic tasks, low-data environments, high-security contexts</div>
    <div class="comparison-cell comparison-ai">High-volume analysis, adaptive alerting, multi-format reporting</div>
    <div class="comparison-cell comparison-verdict verdict-hybrid">🔀 Hybrid</div>
  </div>
  <div class="comparison-row comparison-row-score">
    <div class="comparison-cell comparison-dim"><strong>Recommended Strategy</strong></div>
    <div class="comparison-cell" style="grid-column: span 2; text-align:center; color: var(--vp-c-text-1); font-weight: 600;">Deploy both in parallel — AI handles volume & adaptability, Manual rules serve as the authoritative safety net and audit baseline.</div>
    <div class="comparison-cell comparison-verdict verdict-hybrid">🔀 Hybrid</div>
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

.strategy-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 1rem;
  margin: 1rem 0;
}

/* ── Comparison Table ── */
.comparison-wrapper {
  margin: 1.5rem 0;
  border-radius: 16px;
  overflow: hidden;
  border: 1px solid var(--vp-c-divider);
  box-shadow: 0 8px 32px rgba(0,0,0,0.07);
}

.comparison-header {
  display: grid;
  grid-template-columns: 180px 1fr 1fr 120px;
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%);
  padding: 0;
}
.comparison-header-cell {
  padding: 1rem 1.2rem;
  font-size: 0.8rem;
  font-weight: 700;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: #94a3b8;
}
.comparison-header-manual { color: #60a5fa; }
.comparison-header-ai { color: #a78bfa; }
.comparison-header-verdict { color: #34d399; text-align: center; }

.comparison-section-label {
  grid-column: 1 / -1;
  padding: 0.6rem 1.2rem;
  background: linear-gradient(90deg, rgba(37,99,235,0.1), rgba(124,58,237,0.08));
  border-top: 1px solid var(--vp-c-divider);
  border-bottom: 1px solid var(--vp-c-divider);
  font-size: 0.85rem;
  font-weight: 700;
  color: var(--vp-c-text-2);
  letter-spacing: 0.04em;
}

.comparison-row {
  display: grid;
  grid-template-columns: 180px 1fr 1fr 120px;
  border-top: 1px solid var(--vp-c-divider);
  transition: background 0.15s ease;
}
.comparison-row:hover { background: var(--vp-c-bg-soft); }
.comparison-row-alt { background: rgba(0,0,0,0.02); }
.comparison-row-alt:hover { background: var(--vp-c-bg-soft); }
.comparison-row-score { background: rgba(37,99,235,0.04); }

.comparison-cell {
  padding: 0.75rem 1.2rem;
  font-size: 0.88rem;
  line-height: 1.5;
  color: var(--vp-c-text-2);
  border-right: 1px solid var(--vp-c-divider);
}
.comparison-cell:last-child { border-right: none; }

.comparison-dim {
  font-weight: 700;
  font-size: 0.82rem;
  color: var(--vp-c-text-1);
  display: flex;
  align-items: center;
}
.comparison-manual {
  border-left: 3px solid #3b82f6;
}
.comparison-ai {
  border-left: 3px solid #8b5cf6;
}
.comparison-verdict {
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 0.78rem;
  font-weight: 700;
  text-align: center;
}
.verdict-ai { color: #7c3aed; }
.verdict-manual { color: #2563eb; }
.verdict-tie { color: #059669; }
.verdict-hybrid { color: #d97706; }

.score-manual {
  color: #2563eb;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}
.score-ai {
  color: #7c3aed;
  font-size: 1.1rem;
  display: flex;
  align-items: center;
  justify-content: center;
}

@media (max-width: 768px) {
  .nfr-grid, .osrmt-benefits, .strategy-grid { grid-template-columns: 1fr; }
  .summary-grid { grid-template-columns: repeat(2, 1fr); }
  .comparison-header,
  .comparison-row {
    grid-template-columns: 1fr;
  }
  .comparison-header-cell,
  .comparison-cell { border-right: none; border-bottom: 1px solid var(--vp-c-divider); }
  .comparison-dim { font-weight: 800; background: var(--vp-c-bg-soft); }
}
</style>
