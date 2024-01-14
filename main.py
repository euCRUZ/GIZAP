# pip install python-socketio flask-socketio  simple-websocket
# https://cdnjs.com/
# importei jquery e socket
# ambiente virtual -> criar um novo tda vez para novos (.venv)
# local no pc para todas as instalações EXCLUSIVAS desse site

# http://localhost:5000pip install python-socketio

from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
# permitir qualquer origem de msg
socketio = SocketIO(app, cors_allowerd_origins="*")  # túnel


# funcionalidade de enviar msg
@socketio.on("message")  
def gerenciar_mensagem(mensagem):
    send(mensagem, broadcast=True)

# criar a nossa 1ª página = 1ª rota (td o que vem depois da "/")
# decorator --> atribuí uma funcionalidade para o que está abaixo dele

@app.route("/")
def homepage():
    # criar uma pasta "templates" e dentro dela abrir algo ".html"
    return render_template("index.html")


# rodar o app
socketio.run(app, host="")  # to put your local ip: ipconfig --> IPv4
