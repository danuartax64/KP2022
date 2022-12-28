from flask import Blueprint, redirect, request, session, render_template
import mysql.connector

database = Blueprint('database_cctv', __name__)

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

#array load nama dan link camera dari databae
#index array ke 2-3 merupakan nama dan link dari kamera yang akan diplay pada browser
active_camera = [[],[],['WinCam1', 'WinCam2', 'WinCam3', 'WinCam4'],[r'C:\Users\user\Downloads\KP2022-Clean\KP2022-Clean\Content\cctv_login\no-signal.mp4',r'C:\Users\user\Downloads\KP2022-Clean\KP2022-Clean\Content\cctv_login\no-signal.mp4',r'C:\Users\user\Downloads\KP2022-Clean\KP2022-Clean\Content\cctv_login\no-signal.mp4',r'C:\Users\user\Downloads\KP2022-Clean\KP2022-Clean\Content\cctv_login\no-signal.mp4']]

def get_db_camera():
    openDb()
    sql_select_Query = "select * from list_cctv"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    active_camera[0] = []
    active_camera[1] = []
    for row in records:
        active_camera[0].append(row[0])
        active_camera[1].append(row[1])
    closeDb()

get_db_camera()

def add_cctv(nama_cctv, link_cctv):
    openDb()
    cursor.execute('''INSERT INTO `list_cctv`(`nama_cctv`, `link`) VALUES(%s,%s)''', (nama_cctv,link_cctv))
    connection.commit()
    closeDb()

@database.route('/dashboard',methods=['GET', 'POST'])
def update_active_wincam():
    if request.method == 'POST':
        wincam1 = request.form.get('wincam1')
        wincam2 = request.form.get('wincam2')
        wincam3= request.form.get('wincam3')
        wincam4 = request.form.get('wincam4')

        active_camera[3][0]=wincam1
        active_camera[3][1]=wincam2
        active_camera[3][2]=wincam3
        active_camera[3][3]=wincam4

        return redirect('/dashboard')
    return redirect('/')

@database.route('/dashboardadm',methods=['GET', 'POST'])
def update_active_wincam_admin():
    if request.method == 'POST':
        wincam1 = request.form.get('wincam1')
        wincam2 = request.form.get('wincam2')
        wincam3= request.form.get('wincam3')
        wincam4 = request.form.get('wincam4')

        active_camera[3][0]=wincam1
        active_camera[3][1]=wincam2
        active_camera[3][2]=wincam3
        active_camera[3][3]=wincam4
        get_db_camera()

        return redirect('/dashboardadm')



@database.route('/dashboardadm/add_cctv', methods=['GET', 'POST'])
def add_cctv_dashboardadm():
    if request.method =='POST':
        nama_cctv = request.form['nama_cctv']
        link_cctv = request.form['link_cctv']
        add_cctv(nama_cctv, link_cctv)

        return redirect('/dashboardadm')
    else:
        return redirect('/dashboardadm')

### CRUD CCTV ###


@database.route('/dashboardadm/list_cctv')
def list_cctv():
    if 'loggedin' in session:
        openDb()
        cursor.execute("SELECT * from list_cctv")
        cctv = cursor.fetchall()
        closeDb()
        return render_template("crudcctv.html", cctv=cctv)
    else:
        return render_template('index.html', msg='Anda tidak memiliki izin')

@database.route('/dashboardadm/list_cctv/delete_cctv/<int:id>', methods=['GET'])
def del_cctv(id):
    if 'loggedin' in session and request.method == "GET":
        openDb()
        cursor.execute("DELETE from list_cctv WHERE id = %s",(id,))
        connection.commit()
        closeDb()
        return redirect("/dashboardadm/list_cctv")
    else:
        return render_template('index.html', msg="Anda tidak memiliki izin")

@database.route('/dashboardadm/list_cctv/update_cctv/<int:id>', methods = ['GET', 'POST'])
def update_cctv(id):    #edit cctv
    if 'loggedin' in session and request.method == "GET":
        openDb()
        cursor.execute("SELECT * from list_cctv WHERE id = %s",(id,))
        cctv = cursor.fetchone()
        closeDb()
        return render_template("updatecctv.html", row=cctv)
    elif 'loggedin' in session and request.method == "POST":
        nama_cctv = request.form['nama_cctv']
        link_cctv = request.form['link_cctv']
        openDb()
        cursor.execute("UPDATE list_cctv SET nama_cctv = %s, link = %s WHERE id = %s;", (nama_cctv, link_cctv, id))
        connection.commit()
        closeDb()

        return redirect('/dashboardadm/list_cctv')

@database.route('/dashboardadm/list_cctv/add_cctv', methods = ['POST', 'GET'])
def add_cctv_crud():
    if request.method =='POST':
        nama_cctv = request.form['nama_cctv']
        link_cctv = request.form['link_cctv']
        add_cctv(nama_cctv, link_cctv)
        return redirect('/dashboardadm/list_cctv')

    elif request.method == 'GET':
        return render_template('addcctv.html')

    else:
        return redirect('/dashboardadm/list_cctv')