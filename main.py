from flask import Flask, request, jsonify
from wol_test import wol_pc


app = Flask(__name__)


# Пример приветствия
def welcome():
    return {
        "response": {
            "text": "Привет! Я готова помочь вам Илья Батькович! Hui Pizda Blyat'",
            "end_session": False
        },
        "version": "1.0"
    }


# Обработчик запросов от Яндекс Алисы
@app.route('/', methods=['GET', 'POST'])
def alice_request():
    wol_pc()
    return jsonify(welcome())

@app.route('/hello')
def hello():
    return "HELLO WORLD IlyA Bat'kovich"


if __name__ == '__main__':
    app.run()
