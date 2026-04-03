---
title: Getting Started
---

# Getting Started

Follow this sequence to get EcoGuard running locally and connected to GitLab.

## 1. Clone the repository

```bash
git clone https://gitlab.com/princegarg001-group/EcoGuard.git
cd EcoGuard
```

## 2. Install the base dependencies

```bash
pip install -r requirements.txt
```

## 3. Set the required environment variables

```bash
set GITLAB_TOKEN=your_gitlab_token
set ELECTRICITY_MAPS_API_KEY=your_electricity_maps_key
set CI_PROJECT_ID=80410036
```

## 4. Run the data collector

```bash
python collect_real_data.py
```

## 5. Open the dashboard

```bash
start public\dashboard.html
```

## 6. Run the tests

```bash
cd agents
python -m pytest test_*.py -v
```

## 7. Review the result

- Check the JSON files in [dashboards/data](../dashboards/data) for fresh metrics.
- Start the API server with `python api_server.py` if you want a live backend.
- Use the GitLab pipeline page to confirm the latest run.
