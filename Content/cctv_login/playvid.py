from flask import Blueprint, Response
import cv2
from cctv_login.database_cctv import active_camera
import random
import string

# nosignalpath = "no-signal.mp4"

def get_random_string(length):
    # choose from all lowercase letter
    letters = string.hexdigits
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def gen_frames(cam):  # generate frame by frame from camera
    camera = cv2.VideoCapture(cam)
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            pass
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result

playvid = Blueprint('playvid',__name__)
@playvid.route(f'/{get_random_string(16)}')
def video_feed():
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(active_camera[3][0]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid.route(f'/{get_random_string(16)}')
def video_feed2():
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(active_camera[3][1]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid.route(f'/{get_random_string(16)}')
# @playvid.route(f'/video_feed3')
def video_feed3():
    
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(active_camera[3][2]),
            mimetype='multipart/x-mixed-replace; boundary=frame')

@playvid.route(f'/{get_random_string(16)}')
def video_feed4():
        """Video streaming route. Put this in the src attribute of an img tag."""
        return Response(gen_frames(active_camera[3][3]),
            mimetype='multipart/x-mixed-replace; boundary=frame')