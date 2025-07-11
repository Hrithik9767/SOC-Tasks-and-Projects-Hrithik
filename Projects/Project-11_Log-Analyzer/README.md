# 📘 Project 11 – Log File Analyzer for Intrusion Detection

This project simulates a SOC (Security Operations Center) log monitoring tool that reads server logs (like SSH auth logs), detects suspicious login attempts, and generates alerts based on severity.

---

## 🎯 Objective

To analyze system logs and detect potential intrusions based on repeated failed login attempts. This helps mimic how real-world SIEM tools work inside a SOC team.

---

## 🛠 Tools Used

- Python 3
- Regex for log parsing
- `sample.log` (test SSH log)
- Alert levels & timestamp tracking

---

## 🔍 Features

- Parses log entries and detects failed SSH logins
- Tracks number of failed attempts per IP
- Adds alert level based on frequency:
  - 🟢 Low (1–2 attempts)
  - 🟡 Medium (3 attempts)
  - 🟠 High (4–5 attempts)
  - 🔴 Critical (6+ attempts)
- Collects timestamps of each incident
- Saves a clean summary to `report.txt`

---

## 📁 Folder Structure

Project-11_Log-Analyzer/
├── sample.log ← Sample SSH log file
├── log_analyzer.py ← Python script
├── report.txt ← Generated report (after running script)
└── README.md


---

## 📸 Screenshots

| Screenshot              | Description                                      |
|-------------------------|--------------------------------------------------|
| `log_analysis_output.png` | Terminal output showing alert levels and timestamps |
| `report_file.png`        | The contents of `report.txt` using `cat`        |

---

## ✅ Status

- [x] Log file created and analyzed
- [x] Script generates alert levels + timestamps
- [x] Report saved to file
- [x] Ready for GitHub upload

