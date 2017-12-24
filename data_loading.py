import json
import requests

def get_data_json(url):
    raw_data=json.loads(requests.get(url).text)
    return raw_data
