from flask import Flask, g, render_template, flash, redirect, url_for, abort, Markup
from flask.ext.bcrypt import check_password_hash
from flask.ext.login import LoginManager, login_user, logout_user, login_required, current_user

import forms
import models

DEBUG = True

app = Flask(__name__)
app.secret_key = '7sdf5g6sdf7&dgy7zf&TGf78gsfgnjHDfjg^3dfas7^433Hgfdsta!@11'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(userid):
    try:
        return models.User.get(models.User.id == userid)
    except models.DoesNotExist:
        return None

@app.before_request
def before_request():
    """Connect to the database before each request."""
    g.db = models.DATABASE
    g.db.connect()
    g.user = current_user

@app.after_request
def after_request(response):
    """Close the database connection after each request."""
    g.db.close()
    return response

@app.route('/register', methods=('GET', 'POST'))
def register():
    form = forms.RegisterForm()
    if form.validate_on_submit():
        flash(Markup('Nice! You registered! Now <a href="/login" >login</a>.'), "alert alert-success")
        models.User.create_user(
            username=form.username.data,
            email=form.email.data,
            password=form.password.data
        )
        return redirect(url_for('index'))
    return render_template('register.html', form=form)

@app.route('/login', methods=('GET', 'POST'))
def login():
    form = forms.LoginForm()
    if form.validate_on_submit():
        try:
            user = models.User.get(models.User.email == form.email.data)
        except models.DoesNotExist:
            flash("Your email or password doesn't match. Try again.", "alert alert-danger")
        else:
            if check_password_hash(user.password, form.password.data):
                login_user(user)
                flash("You're logged in!", "alert alert-success")
                return redirect(url_for('index'))
            else:
                flash("Your email or password doesn't match. Try again.", "alert alert-danger")
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You're logged out! Come back soon!", "alert alert-success")
    return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html')

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

if __name__ == '__main__':
    models.initialize()
    try:
        models.User.create_user(
            username='admin',
            email='admin@email.com',
            password='password',
            admin=True
        )
    except ValueError:
        pass
    app.run(debug=DEBUG)
