from flask import Blueprint, render_template

auth = Blueprint('auth', __name__)

@auth.route('/signup')
def signup():
    return "This page will be used to sign up users"

@auth.route('/login')
def login():
    return "This is a log in page"

@auth.route('/logout')
def logout():
    return "This is a log out page"

