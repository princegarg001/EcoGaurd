---
title: SDLC Models
---

# Software Development Life Cycle (SDLC) Models

This document outlines the detailed conceptual SDLC models used in software development processes.

## Waterfall Model

```mermaid
flowchart LR
    subgraph Timelines
        direction LR
        req1[Requirements] -.-> req2[Requirements]
        ana1[Analysis] -.-> ana2[Analysis]
        des1[Design] -.-> des2[Design]
        cod1[Coding] -.-> cod2[Coding]
        tes1[Testing] -.-> tes2[Testing]
        ops1[Operations] -.-> ops2[Operations]
    end

    req1 -- "Requirements Document" --> fs[Fixed Scope]
    fs --> ana2
    
    ana1 -- "Functional Specs" --> sa[System Architecture]
    sa --> des2
    
    des1 -- "Design Documents" --> lui[Logic & UI]
    lui --> cod2
    
    cod1 -- "Source Code" --> ui[Unit/Integration]
    ui --> tes2
    
    tes1 -- "Verified Product" --> dm[Deployment & Maintenance]
    dm --> ops2
```

## Spiral Model (Boehm)

```mermaid
flowchart TD
    start("Start: Initial Idea")
    
    I("[I] Set Objectives,\nAlternatives, Constraints")
    II("[II] Risk Analysis &\nPrototype Development")
    III("[III] Development &\nTesting (e.g., Waterfall)")
    IV("[IV] Plan Next Iteration")
    
    start --> I
    
    I -- "Risk Analysis" --> II
    II -- "Development" --> III
    III -- "Release" --> IV
    IV -- "Loop / Review" --> I
    
    noteI["Key Activities:\n- Determine Objectives\n- Identify Constraints\n- Evaluate Alternatives"]
    noteII["Key Activities:\n- Analyze Risks\n- Perform Feasibility\n- Build Prototypes"]
    noteIII["Key Activities:\n- Design & Coding\n- Unit & Integration Test\n- System Acceptance"]
    noteIV["Key Activities:\n- Review Results\n- Plan Next Spiral\n- Secure Commitment"]
    
    I -.- noteI
    II -.- noteII
    III -.- noteIII
    IV -.- noteIV
    
    style I fill:#f5f5f5,stroke:#333,stroke-width:1px
    style II fill:#f5f5f5,stroke:#333,stroke-width:1px
    style III fill:#f5f5f5,stroke:#333,stroke-width:1px
    style IV fill:#f5f5f5,stroke:#333,stroke-width:1px
    
    style noteI fill:#ffffe0,stroke:#d4c47d
    style noteII fill:#ffffe0,stroke:#d4c47d
    style noteIII fill:#ffffe0,stroke:#d4c47d
    style noteIV fill:#ffffe0,stroke:#d4c47d
```

## Evolutionary Development Model

```mermaid
flowchart LR
    Start((Start)) --> req["Initial\nRequirements"]
    req --> dev["Development\n(Analysis, Design, Code)"]
    dev --> test["Testing &\nEvaluation"]
    test --> feed["Customer\nFeedback"]
    
    feed -- "Release Stable Version" --> prod[("Product\n(Incremental Release)")]
    
    feed -- "Refine / Next Version" --> dev
    
    note["Each cycle results in\nan improved version\nof the software."]
    prod -.- note
```

## V-Model (Software Development Life Cycle)

```mermaid
flowchart TD
    %% Left Side
    req[Requirements] --> sys[System Design]
    sys --> arch[Architecture Design]
    arch --> mod[Module Design]
    mod --> code[Coding]
    
    %% Right Side
    code --> unit[Unit Testing]
    unit --> integ[Integration Testing]
    integ --> systest[System Testing]
    systest --> acc[Acceptance]
    
    %% Cross Links
    req -. "validates" .-> acc
    sys -. "verifies" .-> systest
    arch -. "verifies" .-> integ
    mod -. "verifies" .-> unit
```
