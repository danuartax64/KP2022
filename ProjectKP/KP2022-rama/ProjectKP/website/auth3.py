from flask import Blueprint,render_template
from flask.wrappers import Response
import cv2
from time import sleep

auth3 = Blueprint('auth3',__name__)

camera = cv2.VideoCapture(0)
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

@auth3.route('/login')

def login():
    return render_template("index.html")

@auth3.route('/logout')

def logout():
    return "<p>Logout</p>"

@auth3.route('/sign-up')

def sign_up():
    return "<p>signUP</p>"

@auth3.route('/view')

def view():
    return render_template('indexcam.html')



@auth3.route('/video_feed2')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





