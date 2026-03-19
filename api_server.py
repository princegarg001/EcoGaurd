from flask import Flask, jsonify
import os
import json

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)