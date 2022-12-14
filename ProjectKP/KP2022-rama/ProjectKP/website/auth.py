from flask import Blueprint,render_template
from flask.wrappers import Response
import cv2
from time import sleep

auth = Blueprint('auth',__name__)

camera = cv2.VideoCapture('rtsp://admin:admin123@10.203.21.20:554/Streaming/Channels/1/')
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

@auth.route('/login')

def login():
    return render_template("index.html")

@auth.route('/logout')

def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up')

def sign_up():
    return "<p>signUP</p>"

@auth.route('/view')

def view():
    return render_template('indexcam.html')



@auth.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')





