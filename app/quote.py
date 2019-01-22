import requests


def get_todays_quote():
    r = requests.get('http://quotes.rest/qod.json')
    json_data = r.json()
    if r.status_code == requests.codes.ok:
        return json_data['contents']['quotes'][0]['quote']
