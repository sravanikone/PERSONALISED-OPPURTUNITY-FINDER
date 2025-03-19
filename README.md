
This project is a Flask-based web application designed to collect user profile data and provide personalized opportunity suggestions based on their skills, interests, and location.

## 🚀 Features
- User-friendly HTML form for data collection
- Data validation for required fields
- JSON response displaying submitted data
- Easy integration with databases for future improvements

## 📂 Project Structure
```
/project-root
│
├── /templates
│   └── index.html          # HTML form for user input
│
├── /static                 # For CSS/JS (Optional)
│   ├── styles.css
│   └── script.js
│
├── app.py                  # Flask backend logic
│
├── requirements.txt        # Flask dependencies
│
└── README.md
```

## 🛠️ Setup Instructions
### 1. Install Dependencies
Create and activate a virtual environment:
```
python -m venv venv
venv\Scripts\activate      # For Windows
source venv/bin/activate   # For Mac/Linux
```

Install Flask using:
```
pip install -r requirements.txt
```

### 2. Run the Application
In the terminal, run:
```
python app.py
```
✅ The app will run on **http://localhost:5000**

### 3. Test the Application
- Open your browser and visit **http://localhost:5000**
- Fill out the form and submit.
- You should receive a JSON response displaying the submitted data.

### 4. Sample JSON Response
```json
{
    "message": "User profile submitted successfully!",
    "data": {
        "name": "John Doe",
        "skills": "Python, Flask",
        "interests": "Web Development, AI",
        "location": "India"
    }
}
```

## 🔍 Debugging Tips
- **`ModuleNotFoundError: No module named 'flask'`** → Ensure Flask is installed and your virtual environment is active.
- **`jinja2.exceptions.TemplateNotFound: index.html`** → Ensure `index.html` is inside the `/templates` folder.
- **Port Issues (`OSError: [Errno 48] Address already in use`)** → Use `python app.py --port=5001`

## 📧 Contact
If you face any issues, feel free to reach out!

