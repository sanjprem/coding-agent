from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Coding Agent is running!"

@app.route('/api/test')
def test_api():
    return jsonify({'message': 'API is working!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

@app.route('/api/analyze', methods=['POST'])
def analyze_code():
    try:
        # Add your analysis logic here
        return jsonify({
            'status': 'success',
            'analysis': {
                'files_count': 42,
                'issues_found': 3,
                'suggestions': ['Fix imports', 'Add documentation']
            }
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

@app.route('/api/suggestions', methods=['POST'])
def get_suggestions():
    try:
        # Add AI-powered suggestions logic here
        return jsonify({
            'status': 'success',
            'suggestions': [
                'Consider using TypeScript',
                'Add error handling',
                'Optimize database queries'
            ]
        })
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500