from network_monitor import start_sniffing
from telegram_alerts import send_alert
from event_logger import log_event

def handle_suspicious_packet(packet_info):
    log_event(packet_info)
    message = f"⚠️ Suspicious traffic detected:\nFrom {packet_info['src_ip']} to {packet_info['dst_ip']} at {packet_info['timestamp']}"
    send_alert(message)

if __name__ == "__main__":
    print("[*] Starting PetCam Defender...")
    start_sniffing(callback=handle_suspicious_packet)