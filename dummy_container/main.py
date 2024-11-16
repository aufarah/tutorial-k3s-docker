from flask import Flask
import socket
import random 

var = int(random.random()*100)

app = Flask(__name__)

@app.route('/')
def hello_geek():
    nama_host = socket.gethostname()
    return f'<h1>Hello from Flask, I\'m {nama_host} - {var}</h2>'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5001', debug=False) #port default ke 5000