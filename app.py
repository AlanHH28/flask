from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('/index.html')

@app.route('/process', methods=['POST'])
def process():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Process form data (e.g., save to database, send email)
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Message: {message}")

    return render_template('mensaje.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
