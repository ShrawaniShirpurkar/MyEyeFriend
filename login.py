from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user data for demonstration
USER_DATA = {
    'username': 'Shrawani',
    'password': 'Shrawani'
}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username == USER_DATA['username'] and password == USER_DATA['password']:
        return redirect(url_for('success'))
    else:
        return "Invalid credentials, please try again.", 401

@app.route('/success')
def success():
    return "Login successful!"

if __name__ == '__main__':
    app.run(debug=True)