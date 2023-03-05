from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
  data=request.form
  return render_template('login.html')


@auth.route('/logout')
def logout():
  return "<p>logout</p>"


@auth.route('/sign-up')
def sign_up():
  
  return render_template('signUp.html')
