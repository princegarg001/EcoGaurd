---
title: CI/CD
---

# CI/CD

EcoGuard currently has both GitHub Actions and GitLab CI/CD definitions.

## GitHub Actions

- File: [.github/workflows/main.yml](../.github/workflows/main.yml)
- Trigger: push and pull request on `main`
- Runs tests, data collection, dashboard build, and Pages deployment

## GitLab CI/CD

- File: [.gitlab-ci.yml](../.gitlab-ci.yml)
- Trigger: push to `main`
- Runs build, test, and deploy stages, then publishes Pages

## What the GitLab pipeline does

1. Builds real data and package artifacts.
2. Runs agent tests and code quality checks.
3. Validates flow YAML and docs.
4. Publishes the dashboard to GitLab Pages.

## What to watch

- Make sure the branch is `main` for Pages deployment.
- Verify the `public` artifact contains the dashboard files.
- Check pipeline logs if the dashboard looks stale.
