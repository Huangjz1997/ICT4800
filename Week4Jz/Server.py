from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/authorize', methods=['POST'])
def authorize():
    response = requests.post("https://localhost:6000/authorize", json=request.json, verify=False)
    return jsonify(response.json())

@app.route('/capture', methods=['POST'])
def capture():
    response = requests.post("https://localhost:6000/capture", json=request.json, verify=False)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000, ssl_context=('cert.pem', 'key.pem'))
