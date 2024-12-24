# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, url_for
import serial.tools.list_ports

# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.
@app.route('/')
# ‘/’ URL is bound with index() function.
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

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()