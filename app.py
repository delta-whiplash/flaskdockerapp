import os
from flask import Flask,request,render_template,redirect
app = Flask(__name__)

def os_detector():
    if str(request.headers.get('User-Agent').find("Windows")) != -1:
        return "Windows"
    if str(request.headers.get('User-Agent').find("Android")) != -1:
        return "Android"
    if str(request.headers.get('User-Agent').find("iPhone")) != -1:
        return "iPhone"
    if str(request.headers.get('User-Agent').find("Macintosh")) != -1:
        return "Macintosh"

@app.route('/')
def mainIndex():
    return render_template("index.html")

@app.route('/services/')
def servicesIndex():
    return render_template("/services/index.html")

@app.route('/services/IAIB/')
def iaib():
    # assets_folder = os.path.join(app.root_path, 'services/IAIB/INSTALL')
    # return send_from_directory(assets_folder,"IAIB.zip")
    # assets_folder = os.path.join(app.root_path, 'static/css')
    # return send_from_directory(assets_folder,"style.css")
    return redirect("https://mega.nz/file/H5J0nJ5J#xD3AeFF2mv4twnAI6XLJeL2RrIc81ZAyBVWL1EjqvOA")


@app.route('/games/')
def gameIndex():
    return render_template("/games/index.html")

@app.route('/games/Tetris/')
def tetris():
    # assets_folder = os.path.join(app.root_path, 'games/Tetris/INSTALL')
    # return send_from_directory(assets_folder,"Tetris.zip")
    # assets_folder = os.path.join(app.root_path, 'static/css')
    # return send_from_directory(assets_folder,"style.css")
    return redirect("https://mega.nz/folder/bhxlgKBQ#dLw9Uxx2dX0KTh-mK9lvpg")


@app.errorhandler(404)
def page_404(error):
    return "êtes vous perdu?", 404


if __name__ == '__main__':
    app.secret_key = '2d9-E2.)f&é,A$p@fpa+zSU03êû9_'
    app.run(debug=True)