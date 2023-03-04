from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login')
def login():
  return "<p>Login</p>"


@auth.route('/logout')
def logout():
  return "<p>logout</p>"


@auth.route('/sign-up')
def sign_up():
  
  return "<p>sign up</p>"
