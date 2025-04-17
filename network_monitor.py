from scapy.all import sniff, IP
from datetime import datetime

TRUSTED_DEVICES = {"192.168.1.101", "192.168.1.102"}  # Your known devices
SUSPICIOUS_HOURS = range(0, 6)  # Midnight to 6 AM

def is_suspicious(packet):
    if not packet.haslayer(IP):
        return False

    src_ip = packet[IP].src
    dst_ip = packet[IP].dst
    hour = datetime.now().hour

    return (
        src_ip not in TRUSTED_DEVICES and
        dst_ip not in TRUSTED_DEVICES and
        hour in SUSPICIOUS_HOURS
    )

def extract_packet_info(packet):
    return {
        "src_ip": packet[IP].src,
        "dst_ip": packet[IP].dst,
        "timestamp": datetime.now().isoformat()
    }

def start_sniffing(callback):
    def process_packet(packet):
        if is_suspicious(packet):
            info = extract_packet_info(packet)
            callback(info)

    sniff(prn=process_packet, store=False)