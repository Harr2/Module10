from pprint import pprint
import requests

url = "http://icanhazdadjoke.com/"

payload = {}
headers = {
    'Accept' : 'application/json'
}

response = requests.request('GET', url, headers=headers, data=payload)
pprint(response.text)
