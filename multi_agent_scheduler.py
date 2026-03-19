import schedule
import time
import subprocess

# List of agent scripts to run
AGENTS = [
    'carbon_footprint.py',
    'sustainability_compliance.py',
    'dashboard_data.py',
    'eco_friendly_deployment.py',
    'resource_optimization.py'
]

AGENTS_DIR = 'agents'

# Function to run all agents
def run_agents():
    print('Running all agents...')
    for agent in AGENTS:
        agent_path = f'{AGENTS_DIR}/{agent}'
        try:
            subprocess.run(['python', agent_path], check=True)
            print(f'{agent} completed.')
        except Exception as e:
            print(f'Error running {agent}:', e)
    print('All agents finished.')

# Schedule agents to run every hour
schedule.every(1).hours.do(run_agents)

if __name__ == '__main__':
    print('Multi-agent scheduler started.')
    run_agents()  # Initial run
    while True:
        schedule.run_pending()
        time.sleep(60)
