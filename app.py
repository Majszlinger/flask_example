from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# Enable CORS for all routes (allowing any origin)
CORS(app)

@app.route('/')
def hello_world():
    return "Hello, World! Welcome to Dockerized Flask App."

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
