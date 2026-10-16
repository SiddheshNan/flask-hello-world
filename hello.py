from flask import Flask
import os

app = Flask(__name__)
app_port = os.getenv("PORT", "5000")

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(app_port))

