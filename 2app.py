import os
from flask import Flask,request,render_template,redirect
app = Flask(__name__)


@app.route('/')
def mainIndex():
    return render_template("index.html")


@app.errorhandler(404)
def page_404(error):
    return "êtes vous perdu?", 404


if __name__ == '__main__':
    app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'
    app.run(debug=False, host='0.0.0.0')