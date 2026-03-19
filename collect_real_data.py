#!/usr/bin/env python3
"""Script to collect real data from agents and populate dashboard.

Usage:
    python collect_real_data.py

This script:
1. Runs all agents with sample data
2. Collects real metrics from agent outputs
3. Generates daily/weekly/monthly aggregates
4. Updates dashboard data files
5. Populates summary.json for dashboard display
"""

import sys
import os

# Add agents directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'agents'))

from agents.collect_real_data import RealDataCollector


def main():
    """Main entry point."""
    collector = RealDataCollector()
    collector.collect_all()


if __name__ == '__main__':
    main()
