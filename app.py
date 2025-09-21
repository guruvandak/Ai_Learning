from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/api/learn', methods=['POST'])
def learn():
    data = request.get_json()
    topic = data.get('topic', 'general AI')
    
    # Simple learning response
    learning_content = {
        'topic': topic,
        'content': f'Learning about {topic}...',
        'tips': [
            'Start with basic concepts',
            'Practice regularly',
            'Apply what you learn'
        ]
    }
    
    return jsonify(learning_content)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)