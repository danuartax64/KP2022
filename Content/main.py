from cctv_login import create_app
app = create_app()
import socket

hostname = socket.gethostname()
iphost = socket.gethostbyname(hostname)

#start program
if __name__ == '__main__':
    app.run(debug=True, host='10.203.1.251', port=5000)