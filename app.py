from flask import Flask, request, abort
import requests

app = Flask(__name__)

def test_webhook(webhook_url):
    data = {
        "content": "working!"
    }

    try:
        response = requests.post(webhook_url, json=data)

        if response.status_code == 200:
            print("Success: Webhook sent correctly!")
        else:
            print(f"Failed: Status code {response.status_code}")
            print(response.text)

    except Exception as e:
        print(f"failed: {e}")

# Put your webhook URL here
webhook = "https://discord.com/api/webhooks/1485337144787599612/CXt6sVk5fxhYo9LNn2VAX14Tf8_Y8IsGRz1mmKstfzb0X0FaubeAW5lvDVrskFSGp7LS"

test_webhook(webhook)

# Replace with your allowed IP(s)
WHITELIST = ["192.168.0.62", "192.168.0.53"]

@app.before_request
def limit_remote_addr():
    user_ip = request.remote_addr
    if user_ip not in WHITELIST:
        abort(403)  # Forbidden

@app.route("/")
def home():
    return "Access granted!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9495)