from flask import Flask, render_template, request, session, jsonify
from transformers import pipeline
import textstat
from collections import deque

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this for production

# Load BART summarizer once (abstractive summarization)
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Session-based history (max 3 entries)
if 'history' not in session:
    session['history'] = deque(maxlen=3)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        
        # Word count for original
        orig_word_count = len(text.split())
        
        # Readability score for original (Flesch Reading Ease: 0-100)
        orig_readability = textstat.flesch_reading_ease(text)
        
        # Summarize (truncate to 1024 tokens if too long)
        max_length = 130  # Summary length
        min_length = 30
        if len(text) > 1000:  # Simple truncation for long texts
            text = text[:1000]
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)[0]['summary_text']
        
        # Word count and readability for summary
        sum_word_count = len(summary.split())
        sum_readability = textstat.flesch_reading_ease(summary)
        
        # Save to history
        entry = {
            'original': text[:200] + '...' if len(text) > 200 else text,  # Truncated for display
            'summary': summary,
            'orig_wc': orig_word_count,
            'sum_wc': sum_word_count,
            'orig_read': round(orig_readability, 2),
            'sum_read': round(sum_readability, 2)
        }
        session['history'].append(entry)
        session.modified = True
        
        return render_template('index.html',
                               original=text,
                               summary=summary,
                               orig_wc=orig_word_count,
                               sum_wc=sum_word_count,
                               orig_read=round(orig_readability, 2),
                               sum_read=round(sum_readability, 2),
                               history=list(session['history']))
    
    # GET: Show form and history
    return render_template('index.html', history=list(session['history']))

if __name__ == '__main__':
    app.run(debug=True)
