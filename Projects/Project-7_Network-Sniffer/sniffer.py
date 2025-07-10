from scapy.all import sniff

def packet_callback(packet):
    print(packet.summary())

print("🔍 Starting packet sniffer...")
sniff(prn=packet_callback, count=10)
