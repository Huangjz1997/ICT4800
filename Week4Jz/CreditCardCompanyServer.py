from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/authorize', methods=['POST'])
def authorize():
    data = request.json
    if data['amount'] <= data['credit_limit']:
        auth_code = 'AUTH' + str(len(data['card_number']))
        return jsonify({
            'status': 'OK',
            'authorization_code': auth_code
        })
    else:
        return jsonify({
            'status': 'ERROR',
            'message': 'Credit limit exceeded!'
        })

@app.route('/capture', methods=['POST'])
def capture():
    responses = [{'authorization_code': payment['authorization_code'], 'status': 'CAPTURED'} for payment in request.json['payments']]
    return jsonify(responses)

@app.route('/get_data', methods=['GET'])
def get_data():
    return jsonify({
        "example_key": "example_value"
    })

if __name__ == '__main__':
    app.run(port=6000, ssl_context=('cert.pem', 'key.pem'))
