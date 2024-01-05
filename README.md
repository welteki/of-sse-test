## OpenFaaS Flask SSE test

Deploy the `flask-sse` function:

```sh
faas-cli deploy
```

In the first terminal, create a virtual environment, activate it, and install the necessary requirements.

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
```

Next, listen for updates

```sh
export LISTEN_URL="https://gw.example.com/function/flask-sse/listen"
python3 listen.py
```

In the second terminal, send a ping to the function to start sending events.

```bash
curl -i https://gw.example.com/function/flask-sse/ping
```

This will start sending 500 events. You should see a new `pong` message being displayed every 0.01 second or so.
