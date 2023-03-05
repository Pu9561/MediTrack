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
    m=request.form.get('m')
    day=request.form.get('day')
    year=request.form.get('year')
    gender=request.form.get('gender')
    height=request.form.get('height')
    weight=request.form.get('weight')


    months = ["01", "02", "03", "04", "05", "06" ,"07" ,"08" ,"09" ,"10" ,"11" ,"12"]
    days = []
    for i in range(1,32):
      stri = str(i)
      if len(stri)<2:
        stri = "0"+stri
      
      days.append(stri)
    
      

    if len(email) < 4:
      flash('Email must be greater than 4 characters.', category = 'error')
    elif password1 != password2:
      flash('Passwords do not match.', category = 'error')
    elif len(password1)< 7:
      flash('Password must be greater than 7 characters.', category = 'error')
    elif len(firstName) < 2:
      flash('Firstname must be greater than 2 characters.', category = 'error')
    elif len(lastName) < 2:
      flash('Lastname must be greater than 2 characters.', category = 'error')
    elif m not in months:
      flash('Invalid month, if month is single digit it must have a 0 before it.', category = 'error')
    elif day not in days:
      flash('Invalid day, if day is single digit it must have a 0 before it.', category = 'error')
    elif len(year)!=4:
      flash('Year must be 4 digits long.', category = 'error')
    elif len(gender)>10:
      flash('Gender must be less than 10 characters.', category = 'error')
    elif height<0:
      flash('Invalid height, height must be greater than 0.', category = 'error')
    elif weight<0:
      flash('Invalid height, height must be greater than 0.', category = 'error')
    else:
      flash('Account Created!', category = 'success')
    


  return render_template('signUp.html')
