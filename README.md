# Companion mvp
We need to work on each module as we go. Two-week implementation plan included.

A minimalist AI-powered personal assistant built to help busy individuals manage their day-to-day responsibilities through voice and text commands. This project represents a Minimum Viable Product (MVP) designed to be implemented within a 2-week timeframe.

## Project Overview

This assistant should be able to:
- Process both voice and text commands
- Post to social media platforms (Twitter, LinkedIn)
- Schedule reminders and tasks
- Provide feedback on command execution
  
## Implementation Plan

### Week 1: Core Framework & Basic Functionality

**Days 1-2: Setup & User Interface**
- Create Python Flask application with simple UI
- Implement speech-to-text using Web Speech API and SpeechRecognition

**Days 3-4: Command Processing**
- Build NLP pipeline with spaCy or NLTK
- Create command classifier and intent recognition
- Design action mapping framework

**Days 5-7: API Integration**
- Implement Twitter API connection
- Add LinkedIn basic posting capability
- Create abstract API handler

### Week 2: Completion & Testing

**Days 8-9: Scheduler Implementation**
- Build basic scheduler using APScheduler
- Implement reminder functionality
- Create persistence layer for scheduled tasks

**Days 10-11: Feedback & Error Handling**
- Design user feedback system
- Implement robust error handling
- Add notification capabilities

**Days 12-14: Testing, Fixes & Documentation**
- Conduct integration testing
- Fix critical issues
- Document usage and architecture

## Architecture

The system follows a modular design with these components:

![PHOTO-2025-04-11-20-23-58](https://github.com/user-attachments/assets/9737fecb-d4f0-4c9f-b505-567401741e1d)


1. **User Interface** - Text/voice input collection
2. **Speech-to-Text** - Voice input processing
3. **Command Processing** - NLP and intent recognition
4. **Social Media APIs** - Integration with Twitter and LinkedIn
5. **Scheduler** - Task and reminder management
6. **API Response Handling** - Managing API interactions
7. **User Feedback** - Success/error notifications

## Setup Instructions

1. Clone this repository
2. Install requirements:
   ```
   pip install -r requirements.txt
   ```
3. Download spaCy English model:
   ```
   python -m spacy download en_core_web_sm
   ```
4. Configure API keys in `config.py` (see `config.example.py`)
5. Run the application:
   ```
   python app.py
   ```

## Usage

After starting the application, open your browser to `http://localhost:5000` and:

1. Type a command or click the microphone button to use voice
2. Example commands:
   - "Post Hello world on Twitter"
   - "Remind me to call John at 5 PM"
   - "Schedule a meeting with the team tomorrow at 10 AM"

## Future Development

This MVP is intentionally limited in scope to demonstrate core functionality. Future enhancements could include:

- Additional social platforms (Instagram, Facebook)
- Calendar integration (Google Calendar, Outlook)
- Email composition and sending
- Weather updates and news briefings
- Expanded NLP capabilities for more natural conversations

## Requirements

- Python 3.8+
- Flask
- spaCy
- tweepy
- linkedin-api
- apscheduler
- SpeechRecognition

## Disclaimer

This is a starter module intended as a foundation for further development. API functionality requires valid developer credentials for each platform.
