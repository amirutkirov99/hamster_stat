from flask import Flask
from threading import Thread







app = Flask(__name__)

@app.route('/')
def home():
    return "Всё работает! Я живой и готов к работе!"

def run():
    app.run(host='0.0.0.0', port=8080)



# def print_hello():
#     while True:
#         time.sleep(40)
        
def keep_alive():
    flask_thread = Thread(target=run)
    flask_thread.start()

    # Запускаем поток для print("Hello")

    # print_hello_thread = Thread(target=print_hello)
    # print_hello_thread.start()
