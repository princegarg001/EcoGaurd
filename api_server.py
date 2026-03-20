"""EcoGuard API Server.

Serves dashboard data from JSON files via REST endpoints.
Supports CORS for local development.
"""
from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
import json
import sys

# Load .env file
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    with open(env_path, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#') and '=' in line:
                key, value = line.split('=', 1)
                os.environ[key.strip()] = value.strip()

app = Flask(__name__)

# Enable CORS for all routes (needed for local dashboard development)
try:
    CORS(app)
except Exception:
    # If flask-cors not installed, add headers manually
    @app.after_request
    def after_request(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET')
        return response

def load_json(filename):
    path = os.path.join(os.path.dirname(__file__), 'dashboards', 'data', filename)
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return json.load(f)

@app.route('/api/daily-metrics')
def daily_metrics():
    return jsonify(load_json('daily-metrics.json'))

@app.route('/api/weekly-metrics')
def weekly_metrics():
    return jsonify(load_json('weekly-metrics.json'))

@app.route('/api/monthly-metrics')
def monthly_metrics():
    return jsonify(load_json('monthly-metrics.json'))

@app.route('/api/sustainability-goals')
def sustainability_goals():
    return jsonify(load_json('sustainability-goals.json'))

@app.route('/api/summary')
def summary():
    return jsonify(load_json('summary.json'))

@app.route('/api/status')
def status():
    """Show API configuration status."""
    return jsonify({
        'status': 'running',
        'electricity_maps_api': bool(os.getenv('ELECTRICITY_MAPS_API_KEY')),
        'gitlab_token': bool(os.getenv('GITLAB_TOKEN')),
        'project_id': os.getenv('CI_PROJECT_ID', '80410036'),
        'data_files': {
            'daily': os.path.exists(os.path.join(os.path.dirname(__file__), 'dashboards', 'data', 'daily-metrics.json')),
            'weekly': os.path.exists(os.path.join(os.path.dirname(__file__), 'dashboards', 'data', 'weekly-metrics.json')),
            'monthly': os.path.exists(os.path.join(os.path.dirname(__file__), 'dashboards', 'data', 'monthly-metrics.json')),
            'goals': os.path.exists(os.path.join(os.path.dirname(__file__), 'dashboards', 'data', 'sustainability-goals.json')),
            'summary': os.path.exists(os.path.join(os.path.dirname(__file__), 'dashboards', 'data', 'summary.json')),
        }
    })

# --- Frontend Routes ---
@app.route('/')
def index():
    """Serve the dashboard UI."""
    public_dir = os.path.join(os.path.dirname(__file__), 'public')
    # Try index.html first, fallback to dashboard.html if it exists instead
    if os.path.exists(os.path.join(public_dir, 'index.html')):
        return send_from_directory(public_dir, 'index.html')
    return send_from_directory(public_dir, 'dashboard.html')

@app.route('/<path:filename>')
def serve_static(filename):
    """Serve static files (JS, CSS, images)."""
    public_dir = os.path.join(os.path.dirname(__file__), 'public')
    return send_from_directory(public_dir, filename)

if __name__ == '__main__':
    print("\n🌍 EcoGuard API Server")
    print("=" * 40)
    print(f"  Electricity Maps API: {'✅' if os.getenv('ELECTRICITY_MAPS_API_KEY') else '❌'}")
    print(f"  GitLab Token: {'✅' if os.getenv('GITLAB_TOKEN') else '❌'}")
    print(f"  Serving on: http://localhost:5000")
    print("=" * 40 + "\n")
    app.run(host='0.0.0.0', port=5000, debug=True)