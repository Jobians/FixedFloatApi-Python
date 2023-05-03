## Installation

```bash
pip install FixedFloatApi
```

## Usage

```python
from fixedfloatapi import FixedFloatApi

# create a new API client
api = FixedFloatApi(key='YOUR_API_KEY', secret='YOUR_API_SECRET')

# Get a list of supported currencies
ccies = api.ccies()
print(ccies)

# Get the current price for an exchange
price = api.price({
    'fromCcy': 'BTC',
    'toCcy': 'ETH',
    'amount': 1.0,
    'direction': 'from',
    'type': 'fixed' # or 'float'
})
print(price)

# Create a new exchange order
order = api.create({
    'fromCcy': 'BTC',
    'toCcy': 'ETH',
    'amount': 1.0,
    'direction': 'from',
    'type': 'fixed', # or 'float'
    'toAddress': '0x123...'
})
print(order)

# Place an order for an existing exchange
order_status = api.order({
    'id': '12345',
    'token': 'TESTTOKENvRB90NOtr397kHY3PJ1VRy2p29HHaN7'
})
print(order_status)

# Request emergency assistance for an exchange
emergency = api.emergency({
    'id': '12345',
    'token': 'TESTTOKENvRB90NOtr397kHY3PJ1VRy2p29HHaN7',
    'choice': 'EXCHANGE'
})
print(emergency)

# set email address for order notifications
set_email = api.setEmail({
    'id': 'TESTID',
    'token': 'TESTTOKENvRB90NOtr397kHY3PJ1VRy2p29HHaN7',
    'email': 'notifyme@gmail.com',
})
print(set_email)

# get a QR code for a trade
qr_code = api.qr({
    'id': 'TESTID',
    'token': 'TESTTOKENvRB90NOtr397kHY3PJ1VRy2p29HHaN7',
})
print(qr_code)

# Make a custom API request
method = 'some_method'
data = {'param1': 'value1', 'param2': 'value2'}
response = api.custom_request(method, data)
print(response)
```

For more information, see the [API documentation](https://fixedfloat.com/api)


## Support

If you find my work helpful, you can support me by donating:

[![Donate](https://img.shields.io/badge/Donate-Crypto-0070BA.svg)](https://cwallet.com/t/TE6A6KMV)
