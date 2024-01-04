import os

import sseclient


if __name__ == '__main__':
    listen_url = os.environ.get('LISTEN_URL', 'http://localhost:8080/listen')

    messages = sseclient.SSEClient(listen_url)

    for msg in messages:
        print(msg)  # call print(dir(msg)) to see the available attributes
