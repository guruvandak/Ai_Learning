# AI Learning Platform

## Overview
This is a comprehensive online AI Learning Platform built with Flask that provides structured courses, interactive lessons, quizzes, and progress tracking. The platform offers a complete learning experience for students interested in artificial intelligence topics.

## Project Architecture
- **Backend**: Flask web application (Python 3.11)
- **Frontend**: HTML, CSS, JavaScript with responsive design
- **Data Storage**: JSON-based persistent storage for user progress
- **Security**: Environment-based secret key management
- **Port**: 5000 (configured for Replit proxy)
- **Host**: 0.0.0.0 (allows all hosts for Replit iframe integration)

## Project Structure
```
.
├── app.py                 # Main Flask application with all routes
├── courses_data.py        # Course content and progress management
├── user_progress.json     # Persistent user progress storage
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html        # Landing page with navigation options
│   ├── courses.html      # Course catalog page
│   ├── course_detail.html # Individual course overview
│   ├── lesson.html       # Lesson content with quizzes
│   └── dashboard.html    # User progress dashboard
├── static/
│   ├── css/
│   │   └── style.css     # Complete styling for all pages
│   └── js/
│       └── app.js        # Frontend logic for interactive features
└── replit.md             # This documentation file
```

## Features
### Course Management
- **3 Complete Courses**: Introduction to AI, Machine Learning, Neural Networks
- **Structured Learning**: Organized into modules and lessons
- **Difficulty Levels**: Beginner, Intermediate, and Advanced courses
- **Rich Content**: Comprehensive lesson content with real information

### Interactive Learning
- **Quiz System**: Knowledge checks with immediate feedback
- **Progress Tracking**: Persistent progress across sessions
- **Session Management**: Automatic user session creation and management
- **Responsive Design**: Works on desktop and mobile devices

### User Experience
- **Intuitive Navigation**: Clean navigation between courses and lessons
- **Progress Visualization**: Visual indicators for completed lessons
- **Personal Dashboard**: Overview of learning progress and achievements
- **Quick Learning**: Instant AI topic exploration feature

## API Endpoints
- `GET /` - Landing page with learning options
- `GET /courses` - Course catalog
- `GET /course/<course_id>` - Individual course details
- `GET /lesson/<course_id>/<module_id>/<lesson_id>` - Lesson content
- `GET /dashboard` - User progress dashboard
- `POST /api/learn` - Quick learning topic exploration
- `POST /api/quiz-answer` - Submit quiz answers
- `POST /api/complete-lesson` - Mark lessons as complete

## Course Content
### Available Courses:
1. **Introduction to AI** (Beginner, 4 weeks)
   - History and types of AI
   - AI applications in various industries

2. **Machine Learning Fundamentals** (Intermediate, 6 weeks)
   - ML basics and concepts
   - Supervised vs unsupervised learning

3. **Neural Networks and Deep Learning** (Advanced, 8 weeks)
   - Neural network fundamentals
   - Deep learning architectures

## Recent Changes
- 2025-09-27: Complete platform overhaul with comprehensive features
- Added structured course system with modules and lessons
- Implemented interactive quiz functionality with immediate feedback
- Created user progress tracking with persistent JSON storage
- Added comprehensive dashboard for learning progress
- Implemented secure session management
- Enhanced UI/UX with modern responsive design
- Fixed security issues with environment-based secret key
- Added persistent data storage to prevent progress loss

## Security & Data Management
- **Environment Variables**: Secret key managed via environment variables
- **Session Security**: Secure session management with unique user IDs
- **Data Persistence**: User progress saved to JSON files, survives restarts
- **Error Handling**: Graceful handling of missing courses/lessons

## Deployment
- **Target**: Autoscale deployment for stateless web application
- **Command**: `python app.py`
- **Environment**: Requires `SECRET_KEY` environment variable for production
- **Dependencies**: All listed in requirements.txt

## Development
- **Debug Mode**: Enabled for development with hot reloading
- **Testing**: All APIs tested and working correctly
- **Progress Tracking**: Persistent across development sessions
- **Mobile Ready**: Responsive design works on all devices