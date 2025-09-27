# AI Learning Platform - Course Data Structure

COURSES = {
    "intro-to-ai": {
        "id": "intro-to-ai",
        "title": "Introduction to Artificial Intelligence",
        "description": "Learn the fundamentals of AI, its history, and basic concepts.",
        "difficulty": "Beginner",
        "duration": "4 weeks",
        "modules": [
            {
                "id": "module-1",
                "title": "What is AI?",
                "lessons": [
                    {
                        "id": "lesson-1-1",
                        "title": "History of AI",
                        "content": "Artificial Intelligence has a rich history dating back to the 1950s...",
                        "type": "text",
                        "quiz": {
                            "question": "When was the term 'Artificial Intelligence' first coined?",
                            "options": ["1950", "1956", "1960", "1965"],
                            "correct": 1
                        }
                    },
                    {
                        "id": "lesson-1-2", 
                        "title": "Types of AI",
                        "content": "There are several types of AI systems: Narrow AI, General AI, and Super AI...",
                        "type": "text",
                        "quiz": {
                            "question": "Which type of AI exists today?",
                            "options": ["General AI", "Narrow AI", "Super AI", "All of the above"],
                            "correct": 1
                        }
                    }
                ]
            },
            {
                "id": "module-2",
                "title": "AI Applications",
                "lessons": [
                    {
                        "id": "lesson-2-1",
                        "title": "AI in Healthcare",
                        "content": "AI is revolutionizing healthcare through diagnostic tools, drug discovery...",
                        "type": "text",
                        "quiz": {
                            "question": "What is one major application of AI in healthcare?",
                            "options": ["Gaming", "Medical diagnosis", "Social media", "Music"],
                            "correct": 1
                        }
                    },
                    {
                        "id": "lesson-2-2",
                        "title": "AI in Business",
                        "content": "Businesses use AI for automation, customer service, analytics...",
                        "type": "text",
                        "quiz": {
                            "question": "How do businesses primarily use AI?",
                            "options": ["Entertainment", "Automation and analytics", "Decoration", "None of the above"],
                            "correct": 1
                        }
                    }
                ]
            }
        ]
    },
    "machine-learning": {
        "id": "machine-learning",
        "title": "Machine Learning Fundamentals",
        "description": "Dive deep into machine learning algorithms and techniques.",
        "difficulty": "Intermediate",
        "duration": "6 weeks",
        "modules": [
            {
                "id": "module-1",
                "title": "ML Basics",
                "lessons": [
                    {
                        "id": "lesson-1-1",
                        "title": "What is Machine Learning?",
                        "content": "Machine Learning is a subset of AI that enables systems to learn and improve from experience...",
                        "type": "text",
                        "quiz": {
                            "question": "What is machine learning?",
                            "options": ["A type of computer", "A subset of AI", "A programming language", "A database"],
                            "correct": 1
                        }
                    },
                    {
                        "id": "lesson-1-2",
                        "title": "Supervised vs Unsupervised Learning",
                        "content": "Supervised learning uses labeled data, while unsupervised learning finds patterns in unlabeled data...",
                        "type": "text",
                        "quiz": {
                            "question": "What does supervised learning require?",
                            "options": ["Unlabeled data", "Labeled data", "No data", "Random data"],
                            "correct": 1
                        }
                    }
                ]
            }
        ]
    },
    "neural-networks": {
        "id": "neural-networks",
        "title": "Neural Networks and Deep Learning",
        "description": "Understand neural networks and deep learning architectures.",
        "difficulty": "Advanced",
        "duration": "8 weeks",
        "modules": [
            {
                "id": "module-1",
                "title": "Neural Network Basics",
                "lessons": [
                    {
                        "id": "lesson-1-1",
                        "title": "Introduction to Neural Networks",
                        "content": "Neural networks are inspired by the human brain and consist of interconnected nodes...",
                        "type": "text",
                        "quiz": {
                            "question": "What are neural networks inspired by?",
                            "options": ["Computers", "The human brain", "Mathematics", "Physics"],
                            "correct": 1
                        }
                    }
                ]
            }
        ]
    }
}

# User progress tracking with persistent storage
import json
import os
from datetime import datetime

PROGRESS_FILE = 'user_progress.json'

def load_user_progress():
    if os.path.exists(PROGRESS_FILE):
        try:
            with open(PROGRESS_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return {}
    return {}

def save_user_progress(progress_data):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(progress_data, f, indent=2)

def get_all_courses():
    return COURSES

def get_course(course_id):
    return COURSES.get(course_id)

def get_lesson(course_id, module_id, lesson_id):
    course = get_course(course_id)
    if course:
        for module in course['modules']:
            if module['id'] == module_id:
                for lesson in module['lessons']:
                    if lesson['id'] == lesson_id:
                        return lesson
    return None

def update_user_progress(user_id, course_id, module_id, lesson_id, completed=True):
    user_progress = load_user_progress()
    
    if user_id not in user_progress:
        user_progress[user_id] = {}
    
    if course_id not in user_progress[user_id]:
        user_progress[user_id][course_id] = {}
    
    if module_id not in user_progress[user_id][course_id]:
        user_progress[user_id][course_id][module_id] = {}
    
    user_progress[user_id][course_id][module_id][lesson_id] = {
        'completed': completed,
        'completed_at': datetime.now().isoformat() if completed else None
    }
    
    save_user_progress(user_progress)

def get_user_progress(user_id):
    user_progress = load_user_progress()
    return user_progress.get(user_id, {})