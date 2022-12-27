from flask import Blueprint, redirect, request, session, render_template
import mysql.connector
from .auth import admin, usernamepass

db_user = Blueprint('database_user', __name__)
user=[[],[],[]]

def openDb():
   global connection, cursor
   connection = mysql.connector.connect(host='localhost',
                                         database='db-app-cctv',
                                         user='pep2',
                                         password='l0gin@kses')
   cursor = connection.cursor()

def closeDb():
   global connection, cursor
   cursor.close()
   connection.close()

def get_db_user():
    openDb()
    cursor = connection.cursor()
    cursor.execute("select * from accounts")
    # get all records
    records = cursor.fetchall()
    user[0] = []
    user[1] = []
    user[2] = []
    for row in records:
        user[0].append(row[1])
        user[1].append(row[2])
        user[2].append(row[3])
    closeDb()
get_db_user()

def add_user(nama_user, password, fullakses):
    openDb()
    cursor.execute('''INSERT INTO accounts(username,password,fullakses) VALUES(%s,%s,%s)''', (nama_user, password, fullakses))
    connection.commit()
    closeDb()

@db_user.route('/dashboardadm/list_user')
def list_user():
    if usernamepass[0] in admin and 'loggedin' in session:
        openDb()
        cursor.execute("SELECT * from accounts")
        user = cursor.fetchall()
        closeDb()
        return render_template("cruduser.html", user=user)
    else:
        return render_template('index.html', msg='Anda tidak memiliki izin')

@db_user.route('/dashboardadm/list_user/delete_user/<int:id>', methods=['GET'])
def del_user(id):
    if request.method == "GET" and usernamepass[0] in admin and 'loggedin' in session:
        openDb()
        cursor.execute("DELETE from accounts WHERE id = %s",(id,))
        connection.commit()
        closeDb()
        return redirect("/dashboardadm/list_user")

    else:
        return render_template('index.html', msg="Anda tidak memiliki izin")

@db_user.route('/dashboardadm/list_user/update_user/<int:id>', methods = ['GET', 'POST'])
def update_user(id):    #edit cctv
    if usernamepass[0] in admin and 'loggedin' in session and request.method == "GET":
        openDb()
        cursor.execute("SELECT * from accounts WHERE id = %s",(id,))
        user = cursor.fetchone()
        closeDb()
        return render_template("updateuser.html", row=user)

    elif usernamepass[0] in admin and 'loggedin' in session and request.method == "POST" :
        nama_user = request.form['nama_user']
        pass_user = request.form['pass_user']
        akses_user = request.form['fullakses']

        openDb()
        cursor.execute("UPDATE accounts SET username = %s, password = %s, fullakses = %s WHERE id = %s;", (nama_user, pass_user, akses_user, id))
        connection.commit()
        closeDb()

        return redirect('/dashboardadm/list_user')

    else:
        return render_template("index.html", msg="Anda tidak memiliki izin")

@db_user.route('/dashboardadm/list_user/add_user', methods = ['POST', 'GET'])
def add_cctv_crud():
    if usernamepass[0] in admin and 'loggedin' in session and request.method =='POST':
        
        nama_user = request.form['nama_user']
        pass_user = request.form['pass_user']
        akses_user = request.form['fullakses']

        add_user(nama_user, pass_user, akses_user)

        return redirect('/dashboardadm/list_user')

    elif usernamepass[0] in admin and 'loggedin' in session and request.method == 'GET':
        return render_template('adduser.html')

    else:
        return redirect('/dashboardadm/list_user')
