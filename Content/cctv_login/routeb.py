from flask import Blueprint, render_template, session, redirect
from cctv_login.auth import bolehmasuk
router = Blueprint('route', __name__)

@router.route('/dashboard')
def indexcam():
    if 'loggedin' in session:
        return render_template('indexcam.html', username=session['username'])
    else:
        return redirect('/')