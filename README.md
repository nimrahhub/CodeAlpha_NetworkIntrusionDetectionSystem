# 🛡️ Network Intrusion Detection System (NIDS)

A real-time Network Intrusion Detection System built using **Suricata (Kali Linux)**, **Python (Dash + Plotly)**, and **iptables response automation**.
This project was developed as part of my **CodeAlpha Internship**.

---

## 🚀 Project Overview

This system monitors live network traffic, detects suspicious activity, visualizes attacks in real time, and automatically responds by blocking malicious IPs.

It demonstrates how a basic Security Operations Center (SOC) pipeline works:

**Detect → Monitor → Visualize → Respond**

---

## 🎯 Objectives

✔ Set up a network-based intrusion detection system (Suricata)
✔ Configure rules to detect suspicious activity
✔ Continuously monitor network traffic
✔ Implement automatic response mechanisms
✔ Visualize detected attacks using a live dashboard

---

## 🧰 Tools & Technologies

* 🐧 Kali Linux
* 🛡️ Suricata IDS
* 🐍 Python 3
* 📊 Dash (Plotly)
* 🔥 iptables (Firewall Response)
* 📄 JSON logs (eve.json)

---

## ⚙️ System Workflow

### 1️⃣ Input (Traffic Generation)

Commands used:

```bash
ping 8.8.8.8
nmap -sS <target-ip>
curl http://testphp.vulnweb.com
```

---

### 2️⃣ Detection (Suricata IDS)

Suricata monitors network interface (`eth0`) and detects suspicious activity using rules.

Command:

```bash
sudo suricata -i eth0 -c /etc/suricata/suricata.yaml
```

---

### 3️⃣ Output (Alerts)

Alerts are generated in:

📂 `/var/log/suricata/fast.log`
📂 `/var/log/suricata/eve.json`

Example alert:

```
ICMP Ping Detected [10.0.2.15 → 8.8.8.8]
```

---

### 4️⃣ Visualization (Dashboard)

A Python Dash application reads `eve.json` and displays:

📊 Attack timeline
📍 Source IP distribution
🚨 Alert frequency

Run:

```bash
python suricata_dash.py
```

Open:

```
http://127.0.0.1:8050
```

---

### 5️⃣ Response Mechanism

If malicious activity is detected, the system automatically blocks the attacker IP using:

```bash
sudo iptables -A INPUT -s <attacker-ip> -j DROP
```

---

## 📸 Screenshots (Add Yours Here)

* Dashboard UI
* Suricata alerts in terminal
* Active IP blocking response

---

## 🎥 Video Demo

👉 LinkedIn Video Explanation:
https://www.linkedin.com/posts/nimrah-shafiq-b965342b2_cybersecurity-networksecurity-kalilinux-ugcPost-7471510783147925504-qJGm/?utm_source=share&utm_medium=member_desktop&rcm=ACoAAEsvcKIBehepy2P3eckC3gNupmiAcVjVRLw

---

## 💡 Key Features

✔ Real-time network traffic monitoring
✔ IDS-based attack detection
✔ Live visualization dashboard
✔ Automated IP blocking response
✔ SOC-style architecture

---

## 📚 Learning Outcomes

* Network security fundamentals
* IDS/IPS systems (Suricata)
* Log analysis (JSON processing)
* Python data visualization
* Basic firewall automation

---

## 🔮 Future Improvements

* GeoIP attack mapping 🌍
* Email/SMS alerts 📩
* Machine learning-based detection 🤖
* Web-based SOC panel upgrade

---

## 🙌 Acknowledgment

This project was completed as part of the **CodeAlpha Internship Program**.

---

## 📌 Repository Info

**Project Name:** CodeAlpha_NetworkIntrusionDetectionSystem
**Category:** Cybersecurity / Network Security
**Status:** Completed ✔
