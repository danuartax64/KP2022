from flask import Blueprint, render_template

views = Blueprint('view', __name__)

@views.route('/home')

def home():
    return render_template("indexcam.html")