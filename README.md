# EcoGuard: AI-Powered Sustainability for GitLab

EcoGuard is a GitLab Duo-powered multi-agent platform that automates sustainability analysis, carbon footprint tracking, and green code optimization for software projects.

## Features

- **Sustainability Compliance Agent**: Analyzes code for inefficient patterns and suggests green optimizations
- **Carbon Footprint Agent**: Calculates CI/CD pipeline emissions and provides real-time CO₂ metrics
- **Resource Optimization Agent**: Identifies heavy jobs and recommends efficiency improvements
- **Eco-Friendly Deployment Agent**: Suggests optimal deployment times based on grid carbon intensity
- **Interactive Dashboard**: Visualizes sustainability metrics and tracks progress over time

## Quick Start

1. Clone this repository
2. Enable EcoGuard agents in your GitLab project
3. Configure MCP for external API access (Electricity Maps, Google Cloud)
4. Trigger flows on commits, MRs, or pipeline events
5. View sustainability insights in the dashboard

## Project Structure

```
.
├── agents/              # Agent implementations and prompts
├── flows/               # YAML workflow definitions
├── dashboards/          # Dashboard visualization code
├── docs/                # Documentation and guides
├── .gitlab/duo/         # GitLab Duo configuration
│   ├── AGENTS.md        # Agent definitions and prompts
│   ├── chat-rules.md    # Chat trigger rules
│   └── mcp.json         # MCP configuration
└── README.md            # This file
```

## Documentation

- [VitePress Docs Home](docs/index.md)
- [Getting Started](docs/getting-started.md)
- [Architecture](docs/architecture.md)
- [Agents](docs/agents.md)
- [Flows](docs/flows.md)
- [Dashboard](docs/dashboard.md)
- [CI/CD](docs/ci-cd.md)
- [Testing](docs/testing.md)
- [Troubleshooting](docs/troubleshooting.md)
- [Agent Definitions](.gitlab/duo/AGENTS.md)

## Standards & References

EcoGuard aligns with:
- Green Software Foundation's Software Carbon Intensity (SCI) specification
- GitLab Duo Agent Platform capabilities
- Industry best practices from Google Cloud, Microsoft, and Electricity Maps

## License

MIT License - See LICENSE file for details

## Contributing

Contributions are welcome! Please see CONTRIBUTING.md for guidelines.
