from flask import Flask, render_template
from config import Config
from extensions import db, login_manager
from controllers.auth_controller import auth
from flask_login import login_required
from models.user import User

app = Flask(__name__, template_folder='views/templates')
app.config.from_object(Config)

# Init extensions
db.init_app(app)
login_manager.init_app(app)

# Register blueprints
app.register_blueprint(auth)


@app.route('/')
@login_required
def home():
    users = User.query.all()  # Just to ensure the user is loaded and session is active
    return render_template('home.html', users=users)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)