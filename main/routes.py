from main import app
from flask import render_template, redirect, flash, url_for, get_flashed_messages
from main.models import User
from main.forms import RegisterForm, LoginForm
from main import db
from flask_login import login_user, logout_user, login_required

# homepage


@app.route('/')
@app.route("/product-arena/about")
def home_page():
    return render_template('home.html')


# register route
@app.route("/product-arena/register", methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        possible_user = User(username=form.username.data,
                             email_address=form.email_address.data,
                             password=form.password1.data)
        db.session.add(possible_user)
        db.session.commit()
        login_user(possible_user)
        flash(
            f"Account created successfully! You are now logged in as {possible_user.username}", category='success')
        return redirect(url_for('home_page'))
    if form.errors != {}:
        for err in form.errors.values():
            flash(f'Error while creating a user: {err}', category='danger')
    return render_template('register.html', form=form)


# login route
@app.route('/product-arena/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        aspiring_user = User.query.filter_by(
            username=form.username.data).first()
        if aspiring_user and aspiring_user.check_password(attempted_pw=form.password.data):
            login_user(aspiring_user)
            flash(
                f'Successful login! You are currently logged in as: {aspiring_user.username}', category='success')
            return redirect(url_for('home_page'))
        else:
            flash('Wrong credentials! Please try again.', category='danger')
    return render_template('login.html', form=form)


# logout route
@app.route('/product-arena/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))


# "backend" route
@app.route("/product-arena/backend-developer")
@login_required
def backend_page():
    return render_template('backend.html')


# "full stack developer" route
@app.route("/product-arena/full-stack-developer")
@login_required
def fullstack_page():
    return render_template('fullstack.html')


# "quality assurance" route
@app.route("/product-arena/quality-assurance")
@login_required
def qa_page():
    return render_template('qa.html')


# "ui/ux" route
@app.route("/product-arena/ui-ux-dizajner")
@login_required
def uiux_page():
    return render_template('uiux.html')

# "management" route


@app.route("/product-arena/menadzment-role")
@login_required
def managment_page():
    return render_template('managment.html')
