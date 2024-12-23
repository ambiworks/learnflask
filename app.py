from flask import Flask, url_for
import serial.tools.list_ports

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return f'{username}\'s profile'

@app.route('/port_select')
def port_select():
    ports = serial.tools.list_ports.comports()
    devices = ''
    for port, description, hardware_id in ports:
        devices += f"Port: {port}, Description: {description}\n"
    return f'{devices}'
