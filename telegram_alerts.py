import requests

BOT_TOKEN = "YOUR_BOT_TOKEN"  # Replace with your bot token
CHAT_ID = "YOUR_CHAT_ID"      # Replace with your chat ID

def send_alert(message):
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message}
    try:
        requests.post(url, data=payload, timeout=5)
    except requests.exceptions.RequestException as e:
        print(f"[!] Failed to send Telegram alert: {e}")