# EcoGuard Test Cases

This document provides a comprehensive overview of the test cases used to validate the core functionality of the EcoGuard system. The tests are broken down by their respective agents, with execution evidence and a final comparison table detailing their scope.

## 1. Carbon Footprint Agent

The Carbon Footprint Agent tests verify that our CI/CD pipeline correctly calculates energy usage and carbon emissions using realistic region-specific carbon intensities.

![Carbon Footprint Tests](/Screenshot%202026-04-07%20115646.png)

**Key Test Validations:**
- **Energy Accuracy:** Ensures `JobMetrics` conversions logic (cores & duration to kWh) is mathematically correct.
- **Pipeline Aggregation:** Validates that multi-job pipelines accurately sum energy consumption.
- **Zone Variances:** Confirms emissions calculations adapt to differing regional carbon intensities (e.g., US-CA vs AU).

## 2. Sustainability Compliance Agent

The Sustainability Compliance tests evaluate the static analysis logic, ensuring energy-inefficient coding patterns are accurately flagged without raising false positives on clean code.

![Compliance Agent Tests](/Screenshot%202026-04-07%20115658.png)

**Key Test Validations:**
- **Inefficient Loops:** Detects constant computations inside loops.
- **Unused Variables:** Validates AST (Abstract Syntax Tree) traversal to find allocated but unused variables.
- **Issue Assertions:** Checks that every flagged issue possesses an actionable suggestion and estimated energy savings.

## 3. Eco-Friendly Deployment Agent

The Eco-Friendly Deployment tests ensure that our optimizer correctly suggests the greenest deployment windows and regions based on projected carbon intensities.

![Deployment Agent Tests](/Screenshot%202026-04-07%20115715.png)

**Key Test Validations:**
- **Optimal Time Selection:** Asserts the recommended deployment time aligns with the lowest predicted intensity.
- **Alternative Regions:** Checks if the agent suggests geographically diverse alternatives with lower carbon intensity.
- **Auto-Scaling Recommendations:** Confirms specific guidance is provided based on the target region's current load and configuration.

## 4. Resource Optimization Agent

The Resource Optimization tests confirm our system can successfully identify historically underutilized or overallocated CI/CD resources to prevent wasted energy.

![Optimization Agent Tests](/Screenshot%202026-04-07%20115729.png)

**Key Test Validations:**
- **High CPU/Memory Detection:** Validates the statistical outlier thresholds that identify bloated workloads.
- **Wasted Energy Calculation:** Aggregates total energy squandered by failed pipeline runs.
- **Opportunity Sorting:** Ensures optimization opportunities are properly sorted by their potential impact score.

---

## Agent Test Suites Comparison

| Agent Test Suite | Focus Area | Key Validation | Execution Focus |
|------------------|------------|----------------|-----------------|
| **Carbon Footprint** | Mathematical accuracy of emissions | Multi-job kWh & CO₂ aggregation | Region-based intensity math |
| **Sustainability Compliance** | Static code analysis | Pattern matching via Regex/AST | False positive prevention |
| **Eco-Friendly Deployment** | Workload scheduling | Lowest-carbon region discovery | Constraint-based optimization |
| **Resource Optimization** | Historical utilization analysis | Outlier & wasted energy detection | Impact-based prioritization |

### Summary Description

The EcoGuard system relies on these diverse test suites to ensure reliable and eco-conscious decision-making. The tests validate everything from micro-level code inefficiencies (Compliance Agent) to macro-level deployment scheduling (Deployment Agent). By running robust, mathematically sound tests with mocked variations in grid carbon intensities, EcoGuard ensures that the insights and optimization recommendations presented to users are highly accurate, strictly tested, and consistently lead to a verifiable reduction in overall software carbon footprint.
