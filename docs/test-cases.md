# Test Cases & Scenario Analysis

This document outlines the testing strategy for the EcoGuard system, comparing manual test case design, AI-generated test scenarios using TestGPT, and the actual automated execution results using PyTest.

## 1. Manual Test Case Design (Excel)

We initially designed the core test cases and scenarios manually using Excel. This approach helped us establish the baseline requirements and expected behavior for each agent.

![Excel Test Cases](/Screenshot%202026-04-28%20105652.png)

**Characteristics of Manual Design:**
- **Focus:** Core functionality and happy paths (e.g., detecting inefficient loops, basic API integrations).
- **Structure:** Standard format (TC_ID, Scenario, Steps, Test Data, Expected Result).
- **Coverage:** Primary use cases for Sustainability Compliance, Carbon Footprint, and Eco-Friendly Deployment agents.

## 2. AI-Generated Test Cases (TestGPT)

To expand our test coverage and identify edge cases we might have missed, we utilized TestGPT to generate additional test scenarios.

![TestGPT Test Cases](/Screenshot%202026-04-28%20110816.png)

**Characteristics of AI Generation:**
- **Focus:** Edge cases, performance limits, and complex tradeoffs.
- **Added Scenarios:** 
  - *Compliance:* Large codebase analysis, false positive checks, minified code handling.
  - *Carbon Footprint:* Region variation, missing metrics handling, multi-cloud comparisons.
  - *Deployment:* Cost vs. carbon tradeoffs, auto-scaling optimization, low-latency constraints.
- **Value:** Significantly broadened the scope of our testing strategy with minimal manual effort.

## 3. Automated Test Execution (PyTest)

Finally, we implemented the test scenarios as automated unit and integration tests using Python's `pytest` framework. 

![PyTest Execution Results - test_compliance.py](/pytest-compliance-success.png)

**Characteristics of PyTest Execution:**
- **Execution:** Automated, fast, and repeatable.
- **Results:** Successfully ran and passed **53 automated tests** across all agent modules.
- **Feedback:** Provided immediate feedback on code health, including catching deprecation warnings (e.g., `datetime.utcnow()`) for future maintenance.

---

## Comparison: Excel vs. TestGPT vs. PyTest

| Feature / Tool | Excel (Manual) | TestGPT (AI-Generated) | PyTest (Automated Execution) |
|----------------|----------------|------------------------|------------------------------|
| **Primary Use** | Baseline planning & requirements mapping | Expanding coverage & finding edge cases | Automated verification & CI/CD integration |
| **Speed of Creation** | Slow (Manual entry) | Fast (Prompt-based) | Medium (Requires coding) |
| **Coverage Scope** | Core functionality | Edge cases, tradeoffs, limits | Code-level logic & mathematical accuracy |
| **Execution** | Manual verification required | Theoretical/Scenario generation | Fully automated pipeline execution |
| **Maintenance** | High effort to update | Easy to regenerate | Requires code maintenance, but catches regressions |
| **Strengths** | Human readability, stakeholder alignment | Creative edge-case discovery | Verifiable proof of correctness, regression testing |

### Conclusion

By combining manual test design in **Excel** for baseline requirements, **TestGPT** for expanding edge-case coverage, and **PyTest** for rigorous automated execution, EcoGuard achieves a comprehensive and robust testing strategy. This hybrid approach ensures that our sustainability agents are not only theoretically sound but also practically verified against both common and complex scenarios.
