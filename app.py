from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Flask automatically detects /templates folder

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    skills = request.form.get('skills')
    interests = request.form.get('interests')
    location = request.form.get('location')

    # Return confirmation message
    return jsonify({
        "message": "User profile submitted successfully!",
        "data": {
            "name": name,
            "skills": skills,
            "interests": interests,
            "location": location
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
