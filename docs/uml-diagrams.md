---
title: UML Diagrams
---

# UML Diagrams

<div class="uml-hero">
  <p class="uml-eyebrow">📐 System Architecture</p>
  <h2 class="uml-title">EcoGuard — UML Diagrams</h2>
  <p class="uml-subtitle">
    Detailed structural and behavioral models representing the EcoGuard system.
  </p>
</div>

---

## 🏗️ System Diagrams

These diagrams provide a visual representation of how different components interact and function within the system.

<div class="uml-grid">

  <div class="uml-card">
    <h3>Activity Diagram</h3>
    <img src="/images/activity-diagram.png" alt="Activity Diagram" />
    <p>Visualizes the step-by-step workflow of the EcoGuard system, from code push to generating sustainability reports and updating the dashboard.</p>
  </div>

  <div class="uml-card">
    <h3>Sequence Diagram</h3>
    <img src="/images/sequence-diagram.png" alt="Sequence Diagram" />
    <p>Illustrates the sequence of interactions between the developer, GitLab CI/CD, the EcoGuard orchestrator, and various agents over time.</p>
  </div>

  <div class="uml-card">
    <h3>Collaboration Diagram</h3>
    <img src="/images/collaboration-diagram.png" alt="Collaboration Diagram" />
    <p>Shows the structural relationships and message flow between system components, emphasizing how they collaborate to achieve optimization goals.</p>
  </div>

  <div class="uml-card">
    <h3>Class Diagram</h3>
    <img src="/images/class-diagram.png" alt="Class Diagram" />
    <p>Defines the static structure of the EcoGuard system, detailing the classes, their attributes, methods, and relationships.</p>
  </div>

</div>

<style>
/* ── Hero ──────────────────────────────────────────── */
.uml-hero {
  text-align: center;
  padding: 2.5rem 1.5rem;
  margin: 1.5rem 0 2rem;
  background: linear-gradient(135deg, rgba(16,185,129,0.12), rgba(37,99,235,0.08) 60%, transparent);
  border-radius: 20px;
  border: 1px solid var(--vp-c-divider);
}
.uml-eyebrow {
  font-size: 0.82rem;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: #10b981;
  font-weight: 700;
  margin-bottom: 0.7rem;
}
.uml-title {
  font-size: 1.7rem;
  font-weight: 800;
  color: var(--vp-c-text-1);
  letter-spacing: -0.03em;
  margin: 0 auto 0.8rem;
  max-width: 600px;
  line-height: 1.2;
}
.uml-subtitle {
  color: var(--vp-c-text-2);
  max-width: 620px;
  margin: 0 auto;
  line-height: 1.65;
}

/* ── UML Grid ──────────────────────────────────────── */
.uml-grid {
  display: flex;
  flex-direction: column;
  gap: 2.5rem;
  margin: 2rem 0;
}
.uml-card {
  background: var(--vp-c-bg-soft);
  border: 1px solid var(--vp-c-divider);
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 4px 12px rgba(0,0,0,0.05);
  text-align: center;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}
.uml-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 16px 40px rgba(0,0,0,0.1);
}
.uml-card h3 {
  margin-top: 0;
  margin-bottom: 1.5rem;
  font-size: 1.5rem;
  font-weight: 700;
  color: var(--vp-c-text-1);
  border-bottom: 2px solid var(--vp-c-divider);
  display: inline-block;
  padding-bottom: 0.5rem;
}
.uml-card img {
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  border: 1px solid var(--vp-c-divider);
  box-shadow: 0 4px 16px rgba(0,0,0,0.1);
  margin-bottom: 1.5rem;
}
.uml-card p {
  color: var(--vp-c-text-2);
  font-size: 0.95rem;
  line-height: 1.6;
  margin: 0 auto;
  max-width: 80%;
}

@media (max-width: 768px) {
  .uml-card p {
    max-width: 100%;
  }
}
</style>
