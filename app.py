from flask import Flask, request, render_template, redirect, url_for, session
from werkzeug.utils import secure_filename
import os
from pdfminer.high_level import extract_text
import docx

app = Flask(__name__)
app.secret_key = 'supersecretkey'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

def extract_text_from_resume(filepath):
    if filepath.endswith('.pdf'):
        return extract_text(filepath)
    elif filepath.endswith('.docx'):
        doc = docx.Document(filepath)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    skills = request.form.get('skills').lower()
    interests = request.form.get('interests').lower()
    location = request.form.get('location').lower()

    # Process uploaded resume
    resume_text = ""
    resume_file = request.files.get('resume')
    if resume_file and resume_file.filename != '':
        filename = secure_filename(resume_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(filepath)
        resume_text = extract_text_from_resume(filepath).lower()

    combined_skills = f"{skills} {resume_text} {interests}"

    # Opportunities data
    all_opportunities = [
        {"title": "Python Developer - TCS", "location": "hyderabad", "tags": ["python", "backend"]},
        {"title": "Frontend Intern - Infosys", "location": "hyderabad", "tags": ["html", "css", "javascript", "web development"]},
        {"title": "AI Research Assistant - IIIT", "location": "hyderabad", "tags": ["machine learning", "ai", "python"]},
        {"title": "Java Backend Developer - Wipro", "location": "hyderabad", "tags": ["java", "spring", "backend"]},
        {"title": "Cloud Engineer - Amazon AWS", "location": "hyderabad", "tags": ["aws", "cloud", "linux"]},
        {"title": "Data Analyst - Deloitte", "location": "bangalore", "tags": ["data", "excel", "python"]},
        {"title": "Remote Web Dev Intern - StartupX", "location": "remote", "tags": ["web development", "javascript", "html", "css", "react"]},
        {"title": "ML Engineer - Google AI", "location": "bangalore", "tags": ["machine learning", "python", "tensorflow"]},
    ]

    def match(opp):
        return (location in opp['location']) and any(tag in combined_skills for tag in opp['tags'])

    recommended = [opp['title'] for opp in all_opportunities if match(opp)]
    if not recommended:
        recommended.append("No specific opportunities found for your resume and preferences.")

    session['name'] = name
    session['recommendations'] = recommended

    return redirect(url_for('results'))

@app.route('/results')
def results():
    name = session.get('name')
    recommendations = session.get('recommendations', [])
    return render_template('results.html', name=name, recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)



