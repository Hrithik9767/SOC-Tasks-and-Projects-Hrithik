# 📡 Project 7 – Network Packet Sniffer with Alerts

This project simulates a basic SOC (Security Operations Center) tool that captures real-time network traffic, detects suspicious activity (like packet flooding), and logs alerts into a local SQLite database for analysis.

---

## 🎯 Objective

To build a Python-based network sniffer that:
- Monitors incoming/outgoing packets using Scapy
- Triggers an alert when any IP sends excessive packets (>15)
- Logs alert details into a local `SQLite3` database
- Helps understand how packet inspection tools work in a SOC

---

## 🛠 Tools & Technologies Used

- **Kali Linux (VM)**
- **Python 3**
- **Scapy** for sniffing packets
- **SQLite3** for storing alert logs
- **ICMP (ping)** for testing traffic

---

## ⚙️ How It Works

### 📦 Files:
| File | Purpose |
|------|---------|
| `sniffer.py` | Basic real-time packet sniffer (Day 1) |
| `sniffer_alert.py` | Sniffer with alert system + database logging (Day 2) |
| `alerts.db` | SQLite3 DB that stores alerts triggered |
| `screenshots/` | Proof of work for each step |

### 🚨 Alert Rule:
> If more than **15 packets** are received from the same source IP during the scan session → an alert is triggered and stored in the database.

---

## 🧪 Test Performed

- Ran `sniffer_alert.py` script
- Generated traffic using:
  ```bash
  ping google.com -c 50


##📸 Screenshots
Located in the /screenshots/ folder:
| Screenshot             | Description                         |
| ---------------------- | ----------------------------------- |
| `sniffer_running.png`  | Live packet capture in terminal     |
| `ip_address.png`       | Output of `ip a` (local IP check)   |
| `ping_test.png`        | Ping test to generate traffic       |
| `alert_triggered.png`  | Alerts triggered after packet flood |
| `sqlite_alerts.png`    | Output of `SELECT * FROM alerts;`   |
| `alerts_db_exists.png` | Project folder showing DB exists    |

##📁 Folder Structure

Project-7_Network-Sniffer/
├── sniffer.py
├── sniffer_alert.py
├── alerts.db
├── README.md
└── screenshots/
    ├── sniffer_running.png
    ├── ip_address.png
    ├── ping_test.png
    ├── alert_triggered.png
    ├── sqlite_alerts.png
    └── alerts_db_exists.png

## ✅ Status

 Packet capture working

 Alert logic working

 Database logging

 Project completed and documented

👤 Author
Hrithik – Cybersecurity Intern @ Elevate Labs
GitHub: Hrithik9767

