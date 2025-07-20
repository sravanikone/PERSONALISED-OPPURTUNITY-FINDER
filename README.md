# Personalized Opportunity Finder

This is a Flask-based web application that allows users to submit their profile information and resume, then receive personalized job opportunity recommendations based on their skills, interests, location, and resume content.

---

## 🚀 Features

- Collect user input (name, skills, interests, experience, location)
- Upload and parse resumes (PDF or DOCX)
- Match opportunities using form data + resume keywords
- Display recommended jobs on a separate results page
- Frontend styled with HTML + CSS

---

## 📁 Project Structure

```
project/
│
├── app.py                  # Main Flask application
├── uploads/                # Folder where uploaded resumes are stored
├── templates/
│   ├── index.html          # Form page
│   └── results.html        # Results page with recommendations
├── static/
│   ├── styles.css          # CSS for styling
│   └── script.js           # JS for client-side validation
└── README.md               # You're reading it!
```

---

## ⚙️ Setup Instructions

### 1. Clone the Project

```bash
git clone <your-repo-url>
cd project
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install flask pdfminer.six python-docx
```

### 4. Run the Application

```bash
python app.py
```

### 5. Visit in Browser

Open: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📎 Supported Resume Formats

- .pdf
- .docx

> The resume content is parsed to extract keywords which improve the accuracy of job matching.

---

## 📌 Example Opportunities

Some mocked job examples include:

- Python Developer - TCS (Hyderabad)
- Frontend Intern - Infosys (Hyderabad)
- AI Research Assistant - IIIT
- Remote Web Dev Intern - StartupX
- ML Engineer - Google AI

---

## 🛡️ Security Note

This app uses Flask's `session` and requires a secret key. For production usage:
- Use a more secure secret key
- Implement file type and size validation
- Sanitize user input

---

## 📬 Future Improvements

- Real-time job fetching from external APIs
- Resume scoring / highlighting
- Save user profiles in a database (SQLite, Firebase, etc.)
- Email results to the user

---

## 👩‍💻 Author

Built with ❤️ by your AI assistant and you!
