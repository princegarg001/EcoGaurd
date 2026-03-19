# Contributing to EcoGuard

We welcome contributions to EcoGuard! This document provides guidelines for contributing.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://gitlab.com/your-username/EcoGuard.git`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Make your changes
5. Commit with clear messages: `git commit -m "Add feature: description"`
6. Push to your fork: `git push origin feature/your-feature`
7. Create a merge request

## Code Style

- Follow existing code patterns
- Use clear, descriptive variable names
- Add comments for complex logic
- Keep functions focused and modular

## Agent Development

When adding new agents:

1. Add agent definition to `.gitlab/duo/AGENTS.md`
2. Include system prompt and available tools
3. Create corresponding flow in `/flows/`
4. Add documentation in `/docs/`
5. Test with sample data

## Flow Development

When creating new flows:

1. Create YAML file in `/flows/`
2. Define clear trigger conditions
3. Document workflow steps
4. Test with sample events
5. Update `docs/FLOWS.md`

## Testing

- Test agents with sample code and metrics
- Verify flows execute correctly
- Check dashboard data updates
- Test external API integrations

## Documentation

- Update relevant docs when making changes
- Include examples and use cases
- Keep README.md current
- Document new features in appropriate guides

## Reporting Issues

When reporting bugs:

1. Describe the issue clearly
2. Include steps to reproduce
3. Provide relevant logs or screenshots
4. Suggest a fix if possible

## Feature Requests

When suggesting features:

1. Explain the use case
2. Describe expected behavior
3. Suggest implementation approach
4. Consider sustainability impact

## Code Review

All contributions require review before merging:

- Reviewers will check code quality and alignment with goals
- Address feedback constructively
- Update code based on review comments
- Ensure tests pass before merge

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Questions?

Open an issue or discussion in the project for questions about contributing.
