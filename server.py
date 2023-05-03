from flask import Flask
from flask import request
import socket

app = Flask(__name__)

cache = {}

@app.route('/', methods=['POST', 'GET'])
def seed():
    if request.method == 'POST':
        subprocess.Popen(['python', 'stress_cpu.py'])
        return str(0)
    elif request.method == 'GET':
        return str(socket.gethostname())

if __name__ == '__main__':
    app.run(host='172.31.26.178', port='5000')
