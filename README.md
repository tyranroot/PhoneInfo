```bash 
         ██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
         ██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
         ██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║█████╗  ██║   ██║
         ██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██╔══╝  ██║   ██║
         ██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║██║     ╚██████╔╝
         ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
```             

</div>

---

## 📌 **Overview**

**PhoneInfo ** is a professional-grade OSINT (Open Source Intelligence) tool that extracts comprehensive information from a phone number including:
- 📱 **Number validation & format check**
- 🌍 **Country, region, and timezone information**
- 📡 **Carrier/operator details & line type**
- 📍 **Approximate IP-based geolocation**
- 💬 **Social media presence detection (WhatsApp, Telegram)**
- 🔓 **Breach database references**

> ⚠️ **IMPORTANT**: This tool is for **EDUCATIONAL PURPOSES** only. Use only on numbers you OWN or have WRITTEN PERMISSION to investigate.

---

## ✨ **Features**

<div align="center">

| Category | Features |
|:--------:|:---------|
| 🔍 **Number Intelligence** | Validation, country code, region detection |
| 📡 **Carrier Information** | Operator name, line type (Mobile/Fixed/VoIP) |
| 📍 **Geolocation** | City, state, country, timezone (IP-based) |
| 💬 **Social Media** | WhatsApp presence, Telegram account detection |
| 🔓 **Breach Data** | DeHashed & LeakCheck references |
| 📊 **Reporting** | Professional HTML report with clickable links |
| 🎨 **UI** | Matrix-style terminal with formatted output |

</div>

---

## 📊 **Live Scan Statistics**

```bash
============================================================
              📞 PHONE NUMBER INTELLIGENCE REPORT
============================================================

┌──────────────────────────────────────────────────────────┐
│ 📱 BASIC INFORMATION
├──────────────────────────────────────────────────────────┤
│ Phone Number     : +880********
│ Valid Format     : ✅ YES
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ 🌍 COUNTRY & REGION
├──────────────────────────────────────────────────────────┤
│ Country Code     : +880
│ Country Name     : 
│ Region           : 
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ 📡 CARRIER & NETWORK
├──────────────────────────────────────────────────────────┤
│ Operator         : 
│ Line Type        : 
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ 📍 IP LOCATION (Approximate)
├──────────────────────────────────────────────────────────┤
│ City             : 
│ State/Region     :
│ Country          : 
│ Timezone         : Unknown
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ 💬 SOCIAL MEDIA PRESENCE
├──────────────────────────────────────────────────────────┤
│ WhatsApp         : ✅ ACCOUNT FOUND
│ Telegram         : ❌ Not found
└──────────────────────────────────────────────────────────┘

┌──────────────────────────────────────────────────────────┐
│ 🔓 BREACH DATABASE
├──────────────────────────────────────────────────────────┤
│ DeHashed         : 🔗 https://dehashed.com
│ LeakCheck        : 🔗 https://leakcheck.io
└──────────────────────────────────────────────────────────┘

============================================================
[✓] Scan completed at  00/00/0000
============================================================
```
---
---

###   **Installation**
###  **Termux / Android**
```bash
pkg update -y
pkg install python git -y
git clone https://github.com/tyranroot/PhoneInfo.git
cd PhoneInfo
pip install phonenumbers requests colorama
python PhoneInfo.py
```

###  **Kali and Others distribution**
```bash
sudo apt update -y
sudo apt install python python3 git -y
git clone https://github.com/tyranroot/PhoneInfo.git
cd PhoneInfo
python3 -m venv venv
source venv/bin/activate
pip3 install phonenumbers requests colorama
python3 PhoneInfo.py
```
###  **Overview**
```bash

          
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║█████╗  ██║   ██║
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██╔══╝  ██║   ██║
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║██║     ╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝               
                     ⚡ P H O N E I N F O   v 1 . 0 ⚡                                         
                            Coded by: TyraxZero                                      
                                                                                

[!] Use only on YOUR OWN number or with PERMISSION!

  [>] Phone number (with country code): ***************
```

---
---
###  **Accuracy**

```bash
Type	Information	Accuracy
📱 Number	Validation, formatting	100%
🌍 Country	Code, name, region	99%
📡 Carrier	Operator name	         95%
📞 Line Type	Mobile/Fixed/VoIP	         90%
📍 Location	City, state (IP-based)	85%
⏰ Timezone	Timezone detection	90%
💬 WhatsApp	Account existence	         95%
✈️ Telegram	Account existence	         80%
```
