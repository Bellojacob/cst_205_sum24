"""
NAME: Jacob Bello
DATE: 7/10/2024
CLASS: CST 205
COMMENTS:
I didn't get to the end of the lab because I was having problems
with my api. I was able to figure out the api but it took me
about 1 1/2 hours of debugging and using postman.
"""

import requests, json
from pprint import pprint
#   https://www.frankfurter.app/docs/
#   Currency converter

# payload = {
#     'from' : 'USD'
# }
endpoint = 'https://api.frankfurter.app/latest?from=USD'

try:
    r = requests.get(endpoint)
    data = r.json()
    pprint(data)
except:
    print('Please try again')