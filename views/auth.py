from flask import abort, Blueprint, flash, render_template, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.security import check_password_hash
from blog.models import forms
from blog.models.dao import user

bp = Blueprint("auth", __name__)

@bp.route("/flask-signin", methods=['GET','POST'])
def signin():
    if current_user.is_authenticated:
        flash('You are already signed in.')
        return redirect(url_for('show.index'))

    f = forms.SignInForm()
    if f.validate_on_submit():
        u = user.load_user(f.email.data)
        if u and check_password_hash(u.password, f.password.data):
            login_user(u)
            flash('You have successfully signed in.')
            return redirect(url_for('show.index'))

        flash('The combination of user name and password is different.')
        return redirect(url_for('auth.signin'))
        
    return render_template('signin.html', form=f)

@bp.route('/flask-signout')
@login_required
def signout():
    logout_user()
    flash('You have successfully signed out.')
    return redirect(url_for('show.index'))