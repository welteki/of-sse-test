import time
import os

import requests


if __name__ == '__main__':
    ping_url = os.environ.get('PING_URL', 'http://localhost:8080/ping')

    while True:
        requests.get(ping_url)
        time.sleep(1)
