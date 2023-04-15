import os

from flask import Flask

app = Flask(__name__)



@app.route("/")
def index():
    return "Привет от приложения от Админ компьютера"


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    print("hello")
    app.run(host='0.0.0.0', port=port)