from flask import Flask, render_template, request
from persona_engine import generate_persona

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = ""
    if request.method == 'POST':
        name = request.form['name']
        hobbies = request.form['hobbies']
        tone = request.form['tone']
        style = request.form['style']  # <-- New
        result = generate_persona(name, hobbies, tone, style)
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
