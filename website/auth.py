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

@auth.route('/index')
def index():
   return render_template('index.html')

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
    birthDay=request.form.get('date')
    gender=request.form.get('gender')
    height=request.form.get('height')
    weight=request.form.get('weight')



  return render_template('signUp.html')
@auth.route('/enter-info', methods=['GET', 'POST'])
def enter_info():
 if request.method=="POST":
  d=request.form.get('date')
  print(d)
  print(type(d))
 return render_template ("enterInfo.html")
