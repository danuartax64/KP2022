from flask import Blueprint, render_template, request, session, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors
from cctv_login import app
from datetime import timedelta
from cctv_login.database_cctv import active_camera, get_db_camera, active_camera_client, get_db_camera_client

akses = Blueprint('auth',__name__)
admin=[None]
usernamepass=[None]
user=[None]

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'pep2'
app.config['MYSQL_PASSWORD'] = 'l0gin@kses'
app.config['MYSQL_DB'] = 'db-app-cctv'

# Intialize MySQL
mysql = MySQL(app)
@akses.route('/', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        global username
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Buat sesi dan verifikasi db
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Buat sesi expired ketika browser ditutup
            session.permanent = False
            # Buat sesi expired ketika lewat dari 9 jam
            app.permanent_session_lifetime = timedelta(hours=1)

            if account['lokasi'] == "ADMIN":
                admin.append(username)
                usernamepass[0]=session['username']

                return redirect("/dashboardadm")
            else:
                user[0]= account['lokasi']
                return redirect('/dashboard')
        else:
            # Gagal login
            msg = 'Incorrect username/password!'
    #mental ke halaman login dengan peringatan
    return render_template('index.html', msg=msg)

@akses.route('/dashboard')
def indexcam():
    if 'loggedin' in session:
        get_db_camera_client(user[0])
        print(active_camera_client[0])
        return render_template('indexcam.html', username=session['username'], list_cctv = active_camera_client, test1=active_camera_client[2][0], test2=active_camera_client[2][1], test3=active_camera_client[2][2], test4=active_camera_client[2][3],limit=len(active_camera_client[0]))
    else:
        msg = 'Login Terlebih Dahulu!!!'
        return render_template('index.html', msg=msg)

@akses.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    usernamepass[0]="None"
    try:
        admin[0]="Gatek"
        user[0]="None"
        active_camera[3] = [r'cctv_login\templates\no-signal.mp4',r'cctv_login\templates\no-signal.mp4',r'cctv_login\templates\no-signal.mp4',r'cctv_login\templates\no-signal.mp4']
        print(active_camera_client[3])
    except IndexError:
        pass
    # Redirect to login page
    return redirect('/')   

@akses.route('/dashboardadm')
def dashboard_admin():
    if 'loggedin' in session and session['username'] in admin:
        get_db_camera()
        return render_template('dashboardadm.html', username=session['username'], list_cctv = active_camera, test1=active_camera[2][0], test2=active_camera[2][1], test3=active_camera[2][2], test4=active_camera[2][3], limit = len(active_camera[0]))
    else:
        msg = 'Anda tidak memiliki izin'
        return render_template('index.html', msg=msg)

@akses.route('/cruduser')
def user_manage():
    if session['username'] in admin:
        return render_template('cruduser.html')
    else:
        msg="Anda tidak memiliki izin"
        return render_template('index.html', msg=msg)

@akses.route('/crudcctv')
def cctv_manage():
    return render_template('crudcctv.html')