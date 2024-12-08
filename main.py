from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1> <a  href="/Miruta" >next route</a> </h1>'
@app.route("/Miruta")
def Mostrandoinfo():
    return '<h1> <a href= "/Sopadetomatetactica">eeeeee pappapapapapa </a> </h1>'
@app.route("/Sopadetomatetactica")
def sopadetomatetactica():
    return '<h1> caldo de cebolla </h1>'

app.run(debug=True)
