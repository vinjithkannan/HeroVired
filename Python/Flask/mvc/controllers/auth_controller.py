from flask import Blueprint, render_template, request, redirect, url_for
from extensions import db, login_manager
from models.user import User
from flask_login import login_user, logout_user, login_required

auth = Blueprint('auth', __name__)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))

        return render_template('login.html', title='Login Page', welcome="Invalid username or password")

    return render_template('login.html', title='Login Page', welcome=None)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        username = request.form.get('username')
        password = request.form.get('password')

        if User.query.filter_by(username=username).first():
            return render_template('register.html', title='Register Page', welcome=None, message="Username already exists")

        user = User(name=name, username=username)
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('auth.login'))

    return render_template('register.html', title='Register Page', welcome=None, message=None)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))