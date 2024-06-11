from flask import Flask, request, jsonify

app = Flask(__name__)


# Пример приветствия
def welcome():
    return {
        "response": {
            "text": "Привет! Я готова помочь вам Илья Батькович!.",
            "end_session": False
        },
        "version": "1.0"
    }


# Обработчик запросов от Яндекс Алисы
@app.route('/')
def alice_request():
    return jsonify(welcome())

if __name__ == '__main__':
    app.run(debug=True)
