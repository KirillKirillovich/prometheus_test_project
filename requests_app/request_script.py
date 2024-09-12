import requests
import random
import time

endpoints = [
    '/main',
    '/2x-code',
    '/4x-code',
    '/5x-code'
]

base_url = 'http://web_app:5000' 
error_endpoint = '/4x-code'

def make_request():
    endpoint = random.choice(endpoints)
    url = f'{base_url}{endpoint}'
    try:
        response = requests.get(url)
        print(f'Request to {url} - Status Code: {response.status_code}')
    except requests.RequestException as e:
        print(f'Error making request to {url}: {e}')

def make_errors():
    endpoint = error_endpoint
    url = f'{base_url}{endpoint}'
    try:
        response = requests.get(url)
        print(f'Request to {url} - Status Code: {response.status_code}')
    except requests.RequestException as e:
        print(f'Error making request to {url}: {e}')


if __name__ == '__main__':
    for _ in range(10):
        make_errors()
        time.sleep(5)

    for _ in range(10):
        make_request()
        time.sleep(10)
        make_request()
        time.sleep(10)