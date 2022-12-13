#this is main file
from flask import Flask, render_template, Response
import cv2
import time

app = Flask(__name__)

camera = cv2.VideoCapture(0)
#camera = cv2.VideoCapture('rtsp://service:Az123456b$@10.203.2.64/?2h6x=4')  # use 0 for web camera
#camera2 = cv2.VideoCapture('rtsp://admin:admin123@10.203.21.20:554/Streaming/Channels/1/')
#  for cctv camera use rtsp://username:password@ip_address:554/user=username_password='password'_channel=channel_number_stream=0.sdp' instead of camera

def gen_frames():  # generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            #time.sleep(0.041)
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result
            


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/')
def index():
    """Video streaming home page."""
    return render_template('main.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1')
