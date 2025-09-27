import os
import json
import uuid
from flask import Flask, render_template, request, jsonify, session
from courses_data import get_all_courses, get_course, get_lesson, update_user_progress, get_user_progress

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/courses')
def courses():
    all_courses = get_all_courses()
    return render_template('courses.html', courses=all_courses)

@app.route('/course/<course_id>')
def course_detail(course_id):
    course = get_course(course_id)
    if not course:
        return "Course not found", 404
    
    # Get or create user session
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    
    user_progress = get_user_progress(session['user_id'])
    course_progress = user_progress.get(course_id, {})
    
    return render_template('course_detail.html', course=course, progress=course_progress)

@app.route('/lesson/<course_id>/<module_id>/<lesson_id>')
def lesson_view(course_id, module_id, lesson_id):
    lesson = get_lesson(course_id, module_id, lesson_id)
    course = get_course(course_id)
    
    if not lesson or not course:
        return "Lesson not found", 404
    
    # Get or create user session
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    
    return render_template('lesson.html', lesson=lesson, course=course, 
                         module_id=module_id, course_id=course_id)

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    
    user_progress = get_user_progress(session['user_id'])
    all_courses = get_all_courses()
    
    return render_template('dashboard.html', progress=user_progress, courses=all_courses)

@app.route('/api/complete-lesson', methods=['POST'])
def complete_lesson():
    data = request.get_json()
    course_id = data.get('course_id')
    module_id = data.get('module_id')  
    lesson_id = data.get('lesson_id')
    
    if 'user_id' not in session:
        session['user_id'] = str(uuid.uuid4())
    
    update_user_progress(session['user_id'], course_id, module_id, lesson_id, True)
    
    return jsonify({'status': 'success', 'message': 'Lesson completed!'})

@app.route('/api/quiz-answer', methods=['POST'])
def quiz_answer():
    data = request.get_json()
    course_id = data.get('course_id')
    module_id = data.get('module_id')
    lesson_id = data.get('lesson_id')
    answer = data.get('answer')
    
    lesson = get_lesson(course_id, module_id, lesson_id)
    if not lesson or 'quiz' not in lesson:
        return jsonify({'error': 'Quiz not found'}), 404
    
    correct = lesson['quiz']['correct'] == answer
    
    if correct and 'user_id' in session:
        update_user_progress(session['user_id'], course_id, module_id, lesson_id, True)
    
    return jsonify({
        'correct': correct,
        'message': 'Correct! Well done!' if correct else 'Incorrect. Try again!',
        'correct_answer': lesson['quiz']['options'][lesson['quiz']['correct']]
    })

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