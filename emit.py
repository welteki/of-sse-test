import time
import os

import requests


if __name__ == '__main__':
    ping_url = os.environ.get('PING_URL', 'http://localhost:8080/ping')

    ping_count = 1
    while True:
        requests.get('{}?id={}'.format(ping_url, ping_count))

        print('ping {}'.format(ping_count))
        ping_count += 1
        time.sleep(1)
