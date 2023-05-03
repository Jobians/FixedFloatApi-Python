import json
import hashlib
import requests
import hmac

class FixedFloatApi:
    RESP_OK = 0
    TYPE_FIXED = 'fixed'
    TYPE_FLOAT = 'float'

    def __init__(self, key, secret):
        self.key = key
        self.secret = secret

    def sign(self, data):
        parts = []
        if isinstance(data, dict):
            for key, value in data.items():
                parts.append(f'{key}={value}')
            data = '&'.join(parts)
        return hmac.new(self.secret.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

    def req(self, method, data):
        url = f'https://ff.io/api/v2/{method}'

        req = json.dumps(data)

        headers = {
            'Content-Type': 'application/json',
            'X-API-KEY': self.key,
            'X-API-SIGN': self.sign(req)
        }

        response = requests.post(url, headers=headers, data=req, verify=True)

        try:
            result = response.json()
        except ValueError:
            raise Exception(f'Invalid JSON response: {response.content}')

        if response.status_code != 200:
            raise Exception(f'Request failed with status {response.status_code}: {result.get("msg", "")}')

        if result['code'] != self.RESP_OK:
            raise Exception(result['msg'], result['code'])

        return result['data']

    def ccies(self):
        return self.req('ccies', {})

    def price(self, data):
        return self.req('price', data)

    def create(self, data):
        return self.req('create', data)

    def order(self, data):
        return self.req('order', data)

    def emergency(self, data):
        return self.req('emergency', data)

    def setEmail(self, data):
        return self.req('setEmail', data)

    def qr(self, data):
        return self.req('qr', data)

    def custom_request(self, method, data):
        return self.req(method, data)
