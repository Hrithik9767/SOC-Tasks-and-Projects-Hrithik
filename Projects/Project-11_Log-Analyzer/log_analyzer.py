import re
from collections import defaultdict

# Open log file
with open("sample.log", "r") as file:
    logs = file.readlines()

# Store failed login info
failed_logins = defaultdict(list)

# Regex to find IP and timestamp
pattern = r"^(.*?sshd.*?)Failed password.*from (\d+\.\d+\.\d+\.\d+)"

# Process each line
for line in logs:
    match = re.search(pattern, line)
    if match:
        timestamp = match.group(1).strip()
        ip = match.group(2)
        failed_logins[ip].append(timestamp)

# Function to determine alert level
def get_alert_level(count):
    if count >= 6:
        return "🔴 Critical"
    elif count >= 4:
        return "🟠 High"
    elif count >= 3:
        return "🟡 Medium"
    else:
        return "🟢 Low"

# Show suspicious activity
print("\n🔐 Suspicious IPs Detected:\n---------------------------")

for ip, attempts in failed_logins.items():
    count = len(attempts)
    if count >= 3:
        level = get_alert_level(count)
        print(f"{level} → {ip} → {count} failed attempts")
        for time in attempts:
            print(f"   • {time}")

# Save to report file
with open("report.txt", "w") as report:
    report.write("Suspicious IPs Report\n----------------------\n")
    for ip, attempts in failed_logins.items():
        count = len(attempts)
        if count >= 3:
            level = get_alert_level(count)
            report.write(f"{level} → {ip} → {count} failed logins\n")
            for time in attempts:
                report.write(f"   • {time}\n")
            report.write("\n")

print("\n✅ Report saved as report.txt")

