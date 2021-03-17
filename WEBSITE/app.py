import os
from flask import Flask,request,render_template,redirect
app = Flask(__name__)

@app.route('/')
def mainIndex():
    return "Hello World"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')