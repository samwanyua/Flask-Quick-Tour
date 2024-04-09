from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def home():
    return "Hello world"

@main.route('/profile')
def profile():
    return "Your profile"