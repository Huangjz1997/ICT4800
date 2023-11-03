import requests
def fetch_data():
    url = "https://localhost:6000/get_data"
    response = requests.get(url, verify=False)
    data = response.json()
    print(data)

def authorize_payment(card_number, card_expiry, amount, credit_limit):
    url = "https://localhost:5000/authorize"
    data = {
        'card_number': card_number,
        'card_expiry': card_expiry,
        'amount': amount,
        'credit_limit': credit_limit
    }
    response = requests.post(url, json=data, verify=False)
    return response.json()

def capture_payments(payments):
    url = "https://localhost:5000/capture"
    response = requests.post(url, json={'payments': payments}, verify=False)
    return response.json()

if __name__ == '__main__':
    fetch_data()
    auth_response = authorize_payment('1234-5678-9012-3456', '12/25', 500, 1000)
    if auth_response['status'] == 'OK':
        print(f"Payment authorized! Authorization Code: {auth_response['authorization_code']}")
        capture_response = capture_payments([{'authorization_code': auth_response['authorization_code']}])
        for resp in capture_response:
            if resp['status'] == 'CAPTURED':
                print(f"Payment captured successfully for Authorization Code: {resp['authorization_code']}")
            else:
                print(f"Failed to capture payment for Authorization Code: {resp['authorization_code']}")
    else:
        print(f"Authorization failed! Reason: {auth_response['message']}")
