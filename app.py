from flask import Flask,request
app = Flask(__name__)#base de l'application
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')#lien de base
def index():
    return "Hello !"
if __name__ == '__main__':
    app.run(host= '0.0.0.0') 
    #app.run(debug=True)#lien sert a detecter les erreur dans le code