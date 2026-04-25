from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Simple in-memory storage (for learning only)
profileList = []

@app.route('/')
def home():
    return render_template('home.html', title='Home Page')


@app.route('/about')
def about():
    return render_template('about.html', title='About Page')


@app.route('/contact')
def contact():
    return render_template('contact.html', title='Contact Page')


# 🔹 LOGIN
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # Check user
        for user in profileList:
            if user['username'] == username and user['password'] == password:
                return render_template('login.html', title='Login Page', welcome=f"Welcome {user['name']}")

        return render_template('login.html', title='Login Page', welcome="Invalid username or password")

    return render_template('login.html', title='Login Page', welcome=None)


# 🔹 REGISTER
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        # Save user as dictionary
        user = {
            'name': name,
            'username': username,
            'password': password
        }

        profileList.append(user)

    return render_template('register.html', title='Register Page', profileList=profileList)


if __name__ == '__main__':
    app.run(debug=True)