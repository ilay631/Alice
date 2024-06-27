from flask import Flask, request, jsonify
from wakeonlan import send_magic_packet


app = Flask(__name__)


# Пример приветствия
def welcome():
    return {
        "response": {
            "text": "Привет! Я готова помочь вам Илья Батькович! Hui Pizda",
            "end_session": False
        },
        "version": "1.0"
    }


# Обработчик запросов от Яндекс Алисы
@app.route('/')
def alice_request():
    send_magic_packet("D8:43:AE:21:83:87")
    return jsonify(welcome())

@app.route('/hello')
def hello():
    return "HELLO WORLD IlyA Bat'kovich"


if __name__ == '__main__':
    context = ("server.crt", "server.key")
    app.run(host='0.0.0.0', ssl_context=context)
