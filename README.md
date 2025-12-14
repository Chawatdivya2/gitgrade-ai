GitGrade AI

GitGrade AI is an AI-assisted web application that evaluates GitHub repositories and provides a structured quality score, skill-level classification, and a personalized improvement roadmap.
The system is designed to help students, developers, and recruiters quickly understand the quality and maturity of a GitHub project.

Table of Contents

Overview

Key Features

How It Works

Technology Stack

Project Structure

Installation & Local Setup

Deployment

Usage

Future Enhancements

Overview

GitGrade AI analyzes a given GitHub repository by examining its structure, activity, and best practices using GitHub APIs and AI-inspired evaluation logic.
Instead of relying only on popularity metrics, the system focuses on actionable insights and constructive feedback.

Key Features

Repository Quality Scoring
Generates a score (0–100) based on repository structure, activity, and practices.

Skill Level Classification
Categorizes repositories into:

Beginner (Bronze)

Intermediate (Silver)

Advanced (Gold)

AI-Inspired Analysis
Evaluates repository attributes dynamically and generates human-like feedback.

Personalized Improvement Roadmap
Provides clear, actionable steps to improve code quality and project maturity.

Clean & Minimal User Interface
A distraction-free UI that presents insights clearly and professionally.

Frontend–Backend Separation
Modular architecture suitable for real-world deployment.

How It Works

The user enters a GitHub repository URL.

The frontend sends the request to the backend API.

The backend fetches repository data using the GitHub API.

The evaluation engine analyzes:

Repository structure

Commit activity

Documentation presence

Testing practices

Overall organization

The system generates:

Score

Skill level

Summary

Improvement roadmap

Results are displayed in a clean UI.

Technology Stack
Frontend

HTML5

CSS3

JavaScript

Backend

Python

Flask

Flask-CORS

APIs & Tools

GitHub REST API

Requests (Python)

Hosting

Frontend: GitHub Pages

Backend: Render

Project Structure
gitgrade-ai/
│
├── backend/
│   ├── app.py
│   ├── ai_analyzer.py
│   ├── requirements.txt
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
├── .gitignore
└── README.md

Installation & Local Setup
Prerequisites

Python 3.9+

Git

Internet connection

Steps
git clone https://github.com/<username>/gitgrade-ai.git
cd gitgrade-ai/backend
pip install -r requirements.txt
python app.py


Open frontend/index.html in a browser.

Deployment
Backend Deployment (Render)

Push project to GitHub.

Create a new Web Service on Render.

Set:

Root directory: backend

Build command: pip install -r requirements.txt

Start command: python app.py

Deploy and copy the backend URL.

Frontend Deployment (GitHub Pages)

Go to repository → Settings → Pages.

Select branch main and folder /frontend.

Save and use the generated GitHub Pages URL.

Usage

Open the live frontend URL.

Paste a GitHub repository URL.

Click Analyze Repository.

View the score, level, summary, and improvement roadmap.

Future Enhancements

Code complexity and quality analysis

Language-specific recommendations

Visual analytics (charts & badges)

PDF report generation

Authentication and user dashboards

Purpose

GitGrade AI is built for hackathons, academic projects, and early-career developers to understand repository quality from a practical, industry-oriented perspective.

License

This project is open-source and intended for educational and hackathon use.
