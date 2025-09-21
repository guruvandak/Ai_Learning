# AI Learning Platform

## Overview
This is an AI Learning Platform built with Flask that provides an interactive web interface for learning about artificial intelligence topics. The project was successfully imported and configured for the Replit environment.

## Project Architecture
- **Backend**: Flask web application (Python 3.11)
- **Frontend**: HTML, CSS, JavaScript
- **Port**: 5000 (configured for Replit proxy)
- **Host**: 0.0.0.0 (allows all hosts for Replit iframe integration)

## Structure
```
.
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main web interface
├── static/
│   ├── css/
│   │   └── style.css  # Styling
│   └── js/
│       └── app.js     # Frontend logic
└── replit.md          # This documentation file
```

## Features
- Interactive web interface for AI learning
- RESTful API endpoint (/api/learn) for learning content
- Responsive design with modern CSS
- Real-time content loading with JavaScript

## API Endpoints
- `GET /` - Main web interface
- `POST /api/learn` - Submit learning topic and receive content

## Recent Changes
- 2025-09-21: Initial project setup and configuration for Replit
- Configured Flask app with proper host settings for Replit proxy
- Set up workflow for automatic deployment
- Configured deployment settings for autoscale

## Deployment
- Configured for autoscale deployment target
- Production command: `python app.py`
- No build step required

## Development
The application runs in debug mode during development and is accessible through Replit's web preview.