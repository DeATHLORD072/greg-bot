import os, requests

TOKEN = os.environ CHAT_ID = os.environ def send(text):
    requests.post(f"https://api.telegram.org/bot{TOKEN}/sendMessage",
                  json={"chat_id": CHAT_ID, "text": text})

send("Good morning. Greg here. Today's digest: (nothing yet)")
