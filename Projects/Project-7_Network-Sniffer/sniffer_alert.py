from scapy.all import sniff, IP
import sqlite3
from datetime import datetime

# === SETUP DATABASE ===
conn = sqlite3.connect("alerts.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    src_ip TEXT,
    dst_ip TEXT,
    protocol TEXT,
    timestamp TEXT,
    reason TEXT
)
''')

conn.commit()

# === PACKET HANDLER FUNCTION ===
ip_counter = {}

def packet_callback(packet):
    if IP in packet:
        src = packet[IP].src
        dst = packet[IP].dst
        proto = packet.proto
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Count traffic from each source
        ip_counter[src] = ip_counter.get(src, 0) + 1

        # === Simple Alert Rule ===
        if ip_counter[src] > 15:
            print(f"[⚠️ ALERT] High traffic from {src} → {dst} (Packets: {ip_counter[src]})")

            cursor.execute('''
            INSERT INTO alerts (src_ip, dst_ip, protocol, timestamp, reason)
            VALUES (?, ?, ?, ?, ?)
            ''', (src, dst, str(proto), time, "High packet volume"))

            conn.commit()

# === START SNIFFING ===
print("🚨 Packet Sniffer with Alert System started...")
sniff(prn=packet_callback, count=50)

conn.close()
