# ⚙️ Project Setup & Execution Guide

Network Intrusion Detection System (NIDS)

---

## 🧰 1. System Setup (Kali Linux)

Update system:

```bash
sudo apt update && sudo apt upgrade -y
```

Install Suricata:

```bash
sudo apt install suricata -y
```

---

## 🌐 2. Network Interface Check

Find active interface:

```bash
ip a
```

Example used:

```
eth0 → 10.0.2.15
```

---

## ⚙️ 3. Configure Suricata

Edit configuration file:

```bash
sudo nano /etc/suricata/suricata.yaml
```

Set HOME_NET:

```yaml
HOME_NET: "[10.0.2.0/24]"
EXTERNAL_NET: "!$HOME_NET"
```

Enable logs:

```yaml
eve-log:
  enabled: yes
  filetype: regular
  filename: eve.json
```

---

## 🚀 4. Start Suricata (Detection Engine)

Run Suricata on interface:

```bash
sudo suricata -i eth0 -c /etc/suricata/suricata.yaml
```

Or test configuration:

```bash
sudo suricata -T -c /etc/suricata/suricata.yaml
```

---

## 📡 5. Generate Network Traffic (Testing)

Use commands:

```bash
ping 8.8.8.8
ping 1.1.1.1
nmap -sS 10.0.2.15
```

---

## 📄 6. View Logs (Detection Output)

Fast alerts:

```bash
tail -f /var/log/suricata/fast.log
```

JSON logs:

```bash
tail -f /var/log/suricata/eve.json
```

---

## 📊 7. Run Dashboard (Visualization)

Start Python dashboard:

```bash
python3 suricata_dash.py
```

Open browser:

```
http://127.0.0.1:8050
```

---

## 🚨 8. Response Mechanism (Optional)

Run auto-blocking system:

```bash
sudo python3 response_engine.py
```

Blocks malicious IP using firewall:

```bash
iptables -A INPUT -s <ip> -j DROP
```

---

## 🎯 Final Output Flow

Traffic → Suricata → Logs → Dashboard → Response System

---

## 📌 Notes

* `eve.json` is required for dashboard visualization
* Suricata must be running before dashboard
* Use sudo for all network monitoring tasks
