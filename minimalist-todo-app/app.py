from flask import Flask, render_template, jsonify, request
import json
import os
from datetime import datetime

app = Flask(__name__)

DATA_FILE = 'tasks.json'

def load_data():
    """Load game state from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'tasks': [],
        'current_level': 0,
        'skips_used': 0,
        'completed_tasks': [],
        'game_started': False
    }

def save_data(data):
    """Save game state to JSON file"""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    """Setup screen - add tasks before starting"""
    data = load_data()
    if data['game_started'] and data['current_level'] < len(data['tasks']):
        return render_template('game.html')
    return render_template('index.html')

@app.route('/api/setup', methods=['POST'])
def setup_game():
    """Initialize game with tasks"""
    tasks = request.json.get('tasks', [])
    if not tasks:
        return jsonify({'error': 'No tasks provided'}), 400

    data = {
        'tasks': tasks,
        'current_level': 0,
        'skips_used': 0,
        'completed_tasks': [],
        'game_started': True,
        'start_time': datetime.now().isoformat()
    }
    save_data(data)
    return jsonify({'success': True})

@app.route('/api/game-state')
def get_game_state():
    """Get current game state"""
    data = load_data()
    if not data['game_started']:
        return jsonify({'error': 'Game not started'}), 400

    current_level = data['current_level']
    total_levels = len(data['tasks'])

    if current_level >= total_levels:
        return jsonify({
            'game_over': True,
            'completed': len(data['completed_tasks']),
            'total': total_levels,
            'skipped': total_levels - len(data['completed_tasks'])
        })

    return jsonify({
        'current_task': data['tasks'][current_level],
        'level': current_level + 1,
        'total_levels': total_levels,
        'skips_remaining': 2 - data['skips_used'],
        'game_over': False
    })

@app.route('/api/complete', methods=['POST'])
def complete_task():
    """Mark current task as complete and move to next level"""
    data = load_data()

    if data['current_level'] >= len(data['tasks']):
        return jsonify({'error': 'No more tasks'}), 400

    # Mark task as completed
    completed_task = data['tasks'][data['current_level']]
    data['completed_tasks'].append(completed_task)
    data['current_level'] += 1

    save_data(data)
    return jsonify({'success': True, 'next_level': data['current_level'] + 1})

@app.route('/api/skip', methods=['POST'])
def skip_task():
    """Skip current task (max 2 skips allowed)"""
    data = load_data()

    if data['skips_used'] >= 2:
        return jsonify({'error': 'Maximum skips reached'}), 400

    if data['current_level'] >= len(data['tasks']):
        return jsonify({'error': 'No more tasks'}), 400

    # Skip task
    data['skips_used'] += 1
    data['current_level'] += 1

    save_data(data)
    return jsonify({'success': True, 'skips_remaining': 2 - data['skips_used']})

@app.route('/api/reset', methods=['POST'])
def reset_game():
    """Reset the game"""
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
