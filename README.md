# AI-Writer-with-text-Summarization
Objective: Generate summaries from large articles using NLP. Tools: Python, Hugging Face Transformers, Flask.1.Use BART or T5 summarization model 2.Build text input interface 3.Process long articles 4.Run model and return summary 5.Add word count and readability score 6.Optional: Save history of summaries 7.Deploy using Flask Deliverables

# AI Writer: Text Summarization Web App

[![Python 3.8+](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)

A Flask web app using Hugging Face's BART for abstractive summarization of articles. Includes metrics (word count, Flesch readability) and session history.

## Features
- AI summaries via BART-large-CNN.
- Handles long texts with truncation.
- Original/summary metrics.
- Last 3 summaries saved in session.
- Simple UI for input/output.

## Setup and Installation
### Prerequisites
- Python 3.8+.
- Git.

### Local Development
1. Clone: `git clone https://github.com/yourusername/ai-writer.git`
2. Navigate: `cd ai-writer`
3. Virtual env: `python -m venv venv` (activate: `source venv/bin/activate` on Unix, `venv\Scripts\activate` on Windows)
4. Install: `pip install -r requirements.txt`
5. Run: `python app.py`
6. Access: `http://127.0.0.1:5000/`

First run downloads BART model (~1.6GB).

## Quick Start
Paste article text, click "Summarize". View metrics and history below.

## Deployment
- **Heroku**: Use `Procfile`; `git push heroku main`.
- **Vercel**: Via CLI for serverless.

## Usage
Paste article text, click "Summarize". View metrics and history below.

## Dependencies
Flask, Transformers, Torch, Textstat, Gunicorn.
