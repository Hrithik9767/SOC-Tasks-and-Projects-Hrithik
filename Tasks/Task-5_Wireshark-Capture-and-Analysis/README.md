# Task 5 – Network Traffic Capture & Analysis with Wireshark

## Objective
Capture live network traffic using Wireshark and analyze at least three different protocols.

## Tools Used
- Wireshark v4.x
- Browser and Terminal

## Steps Performed
1. Opened Wireshark and started capture on the active network interface.
2. Visited `https://example.com` in the browser.
3. Ran `ping google.com` in the terminal to generate traffic.
4. Stopped capture after about 1 minute.
5. Filtered traffic using:
   - `dns` for DNS queries
   - `tcp` for TCP connections
   - `icmpv6` for ping packets

## Protocols Identified

### 1. DNS
- Queries to resolve domain names like `google.com`
- Protocol: `DNS`
- Example: Standard query sent to 8.8.8.8

### 2. TCP
- TCP handshake (SYN, SYN-ACK, ACK)
- Protocol: `TCP`
- Example: Connection setup between local machine and web server

### 3. ICMPv6
- Ping echo request and replies
- Protocol: `ICMPv6`
- Example: Echo request to `google.com` seen in capture

## Files Included
- `task5_capture.pcap`: Packet capture file
- `screenshots/`: Folder with relevant screenshots

## Key Concepts
- Packet capture and analysis
- Protocol-level inspection
- Basic network troubleshooting skills



