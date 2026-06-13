import json
import os

LOG_FILE = "/var/log/suricata/eve.json"

blocked_ips = set()

def block_ip(ip):
if ip in blocked_ips:
return

```
print(f"[ALERT] Blocking malicious IP: {ip}")

# Block IP using firewall
os.system(f"sudo iptables -A INPUT -s {ip} -j DROP")

blocked_ips.add(ip)

with open("blocked_ips.log", "a") as f:
    f.write(ip + "\n")
```

def monitor_logs():
print("Starting response engine...")

```
try:
    with open(LOG_FILE, "r") as f:
        f.seek(0, 2)

        while True:
            line = f.readline()

            if not line:
                continue

            try:
                data = json.loads(line)

                if data.get("event_type") == "alert":
                    src_ip = data.get("src_ip")

                    if src_ip:
                        block_ip(src_ip)

            except:
                continue

except FileNotFoundError:
    print("Log file not found!")
```

if **name** == "**main**":
monitor_logs()
