import requests
import json
import time
import os
from alive import server_on

# ใส่ User Token ที่ได้จาก DevTools
TOKEN = os.getenv("YOUR DISCORD TOKEN")
SWITCH_INTERVAL = 5  # 5 วินาทีแล้วเปลี่ยน

# กิลด์ที่มี Server Tag
GUILDS = [
    {"name": "meow", "id": "427067963137589258"},
    {"name": "cute", "id": "294005213763993601"},
    {"name": "dev", "id": "547906569489350657"},
    {"name": "ios", "id": "349243932447604736"},
    {"name": "cybr", "id": "543652415870730240"},
    {"name": "star", "id": "1044698006395555960"},
    {"name": "vip", "id": "710871326557995079"},
    {"name": "owo", "id": "267735321695748096"},
    {"name": "bruh", "id": "844285068275875890"},
    {"name": "ez", "id": "986691543102529546"},
    {"name": "tit", "id": "247434867527122945"},
    {"name": "emh", "id": "897153084478865438"},
    {"name": "dual", "id": "476454574715174912"},
    {"name": "gca", "id": "223070469148901376"},
    {"name": "valc", "id": "1350807682520711199"},
    {"name": "soul", "id": "786437953299021844"}
]

HEADERS = {
    "Authorization": TOKEN,
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def switch_identity(guild):
    url = "https://discord.com/api/v9/users/@me/clan"
    payload = {
        "identity_guild_id": guild["id"],
        "identity_enabled": True
    }
    res = requests.put(url, headers=HEADERS, data=json.dumps(payload))
    if res.status_code == 200:
        print(f"🔁 เปลี่ยนเป็น: {guild['name']} ({guild['id']})")
    else:
        print(f"❌ เปลี่ยน tag ล้มเหลว ({res.status_code}) → {res.text}")

def loop_switch():
    idx = 0
    while True:
        switch_identity(GUILDS[idx])
        idx = (idx + 1) % len(GUILDS)
        time.sleep(SWITCH_INTERVAL)

def main():
    print(f"🌀 เริ่มสลับ Server Tag ทุก {SWITCH_INTERVAL} วินาที")
    loop_switch()

if __name__ == "__main__":
    server_on()
    main()


