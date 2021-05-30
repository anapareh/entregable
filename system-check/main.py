from flask import Flask, render_template
import platform, os, socket, subprocess
app = Flask(__name__)
mensaje=[]

@app.route("/")
def index():
    return render_template('index.html', mensaje=['System-Check', ''])

@app.route("/<parametro>")
def mostrar(parametro):
        if parametro=="nombre":
            return render_template('index.html', mensaje=['Nombre:', socket.gethostname()])
        elif parametro=="ip":
            return render_template('index.html', mensaje=['IP:',  get_ip()])
        elif parametro=="reinicio":
            try:
                return render_template('index.html', mensaje=['Reiniciando...', subprocess.run("shutdown -r now", shell=True)])
            except FileNotFoundError:
                return render_template('index.html', mensaje=['Archivo o ruta inválidos'])
        else:
            return render_template('index.html',mensaje=['Parámetro no válido :( prueba de nuevo'])
def get_ip():
    s= socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255',1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
if __name__ == "__main__":
            app.run(host="127.0.0.1", port=8080, debug=True)