from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    server_id = os.environ.get('SERVER_ID', 'Unknown')
    return f'<h1>Hello from Web Server {server_id}!</h1>'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80) 