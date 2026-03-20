#!/usr/bin/env python3
"""Script to collect real data from agents and populate dashboard.

Usage:
    python collect_real_data.py

This script:
1. Loads environment variables from .env file
2. Fetches real pipeline data from GitLab API
3. Gets real carbon intensity from Electricity Maps API
4. Calculates energy and emissions from actual job durations
5. Updates dashboard data files with real metrics
"""

import sys
import os

# Load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        load_dotenv(env_path)
        print(f"✅ Loaded environment from .env")
    else:
        print(f"⚠️  No .env file found at {env_path}")
except ImportError:
    # Fallback: manually load .env
    env_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_path):
        with open(env_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#') and '=' in line:
                    key, value = line.split('=', 1)
                    os.environ[key.strip()] = value.strip()
        print(f"✅ Loaded environment from .env (manual)")

# Add agents directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'agents'))

from agents.collect_real_data import RealDataCollector


def main():
    """Main entry point."""
    collector = RealDataCollector()
    collector.collect_all()


if __name__ == '__main__':
    main()
