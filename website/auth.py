from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():
  data=request.form
  print(data)
  return render_template('login.html')


@auth.route('/logout')
def logout():
  return "<p>logout</p>"


@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
  data=request.form
  print(data)
  if request.method=='POST':
    email=request.form.get('email')
    password1=request.form.get('password1')
    password2=request.form.get('password2')
    firstName=request.form.get('firstName')
    lastName=request.form.get('lastName')
    birthMonth=request.form.get('m')
    birthDay=request.form.get('day')
    birthYear=request.form.get('year')
    gender=request.form.get('gender')
    height=request.form.get('height')
    weight=request.form.get('weight')
    


  return render_template('signUp.html')
