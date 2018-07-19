from flask import render_template,redirect,request,url_for,flash
from . import auth 
from flask_login import login_required,login_user,logout_user,current_user
from .forms import LoginForm
from ..models import User

@auth.route('/login',methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.rember_me.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        flash('Invalid username or password.') 
    return render_template('auth/login.html',form=form,title="Login")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@auth.route("/secret")
@login_required
def secret():
    print(current_user.is_authenticated,1)
    return 'Only authenticated users are allowed!'
@auth.route("/aa")
@login_required
def aa():
    print(current_user.is_authenticated,1)
    return 'ok'

