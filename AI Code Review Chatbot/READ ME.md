# AI Code Review Agent

[Badges]

## Overview

AI Code Review Agent is a web application that uses FastAPI and Anthropic Claude to review source code and return structured findings such as bugs, security vulnerabilities, and style improvements.

## Features

- AI-powered code review
- Bug detection
- Security vulnerability analysis
- Code style suggestions
- Severity levels
- REST API
- Health endpoint
- JSON responses
- Responsive frontend
- Docker support

## Demo

(Add screenshots or GIF here)

## Architecture

Frontend
    │
    ▼
FastAPI Backend
    │
    ▼
Anthropic Claude API
    │
    ▼
Structured JSON Findings

## Project Structure

backend/
frontend/
docs/
tests/
.github/

## Installation

1. Clone repository
2. Create virtual environment
3. Install requirements
4. Configure API key
5. Run server

## Environment Variables

ANTHROPIC_API_KEY=your_api_key

## API

GET /api/health

POST /api/review

Request:
{
  "code": "...",
  "filename": "main.py",
  "language": "python"
}

Response:
{
  "summary": "...",
  "findings": [...]
}

## Technologies

- Python
- FastAPI
- Anthropic Claude
- Pydantic
- HTML
- CSS
- JavaScript

## Future Improvements

- GitHub repository analysis
- ZIP project upload
- Authentication
- PDF reports
- Review history

## License

MIT
