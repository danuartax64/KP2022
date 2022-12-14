from flask import Blueprint,render_template
from flask.wrappers import Response
import cv2
from time import sleep

auth2 = Blueprint('auth2',__name__)

camera = cv2.VideoCapture('rtsp://service:Az123456b$@10.203.2.64/?2h6x=4')
def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            pass
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            sleep(0.041)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

@auth2.route('/login')

def login():
    return render_template("index.html")

@auth2.route('/logout')

def logout():
    return "<p>Logout</p>"

@auth2.route('/sign-up')

def sign_up():
    return "<p>signUP</p>"

@auth2.route('/view')

def view():
    return render_template('indexcam.html')



@auth2.route('/video_feed1')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





