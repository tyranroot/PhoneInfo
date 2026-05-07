#!/usr/bin/env python3

import sys
import os
import re
import requests
import phonenumbers
from phonenumbers import carrier, geocoder
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

# Colors
R = Fore.RED
G = Fore.GREEN
Y = Fore.YELLOW
C = Fore.CYAN
W = Fore.WHITE
BOLD = Style.BRIGHT
RESET = Style.RESET_ALL

# ==================== API KEY ====================
GEOAPIFY_KEY = "2cee691ee998470895c0b83bfca5cae6"
# =================================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def banner():
    clear()
    print(f"""{C}{BOLD}
          
██████╗ ██╗  ██╗ ██████╗ ███╗   ██╗███████╗██╗███╗   ██╗███████╗ ██████╗ 
██╔══██╗██║  ██║██╔═══██╗████╗  ██║██╔════╝██║████╗  ██║██╔════╝██╔═══██╗
██████╔╝███████║██║   ██║██╔██╗ ██║█████╗  ██║██╔██╗ ██║█████╗  ██║   ██║
██╔═══╝ ██╔══██║██║   ██║██║╚██╗██║██╔══╝  ██║██║╚██╗██║██╔══╝  ██║   ██║
██║     ██║  ██║╚██████╔╝██║ ╚████║███████╗██║██║ ╚████║██║     ╚██████╔╝
╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝               
                     ⚡ P H O N E I N F O   v 1 . 0 ⚡                                         
                            Coded by: TyraxZero                                      
                                                                                
{RESET}""")
    print(f"{Y}{BOLD}[!] Use only on YOUR OWN number or with PERMISSION!{RESET}\n")

class PhoneInfoPro:
    def __init__(self, number):
        self.raw_number = number
        self.parsed_number = None
        self.results = {
            'number': number,
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'valid': False,
            'country': {},
            'carrier': {},
            'location': {},
            'whatsapp': False,
            'telegram': False
        }
    
    def log(self, msg, typ="info"):
        """Log function for displaying messages"""
        ts = datetime.now().strftime("%H:%M:%S")
        if typ == "info":
            print(f"{C}[{ts}]{RESET} {msg}")
        elif typ == "success":
            print(f"{G}[{ts}] ✓{RESET} {msg}")
        elif typ == "warning":
            print(f"{Y}[{ts}] ⚠{RESET} {msg}")
        elif typ == "error":
            print(f"{R}[{ts}] ✗{RESET} {msg}")
    
    def validate_format(self):
        try:
            number = phonenumbers.parse(self.raw_number, None)
            if phonenumbers.is_valid_number(number):
                self.parsed_number = number
                self.results['valid'] = True
                self.log("Number is VALID", "success")
                return True
            else:
                self.log("Number is INVALID", "error")
                return False
        except:
            self.log("Could not parse number", "error")
            return False
    
    def get_country_info(self):
        if not self.parsed_number:
            return
        country_code = self.parsed_number.country_code
        country_name = geocoder.country_name_for_number(self.parsed_number, "en")
        self.results['country'] = {
            'code': f"+{country_code}",
            'name': country_name,
            'region': geocoder.description_for_number(self.parsed_number, "en")
        }
        self.log(f"Country: {country_name} (+{country_code})", "success")
    
    def get_carrier_info(self):
        if not self.parsed_number:
            return
        try:
            carrier_name = carrier.name_for_number(self.parsed_number, "en")
            self.results['carrier'] = {
                'name': carrier_name if carrier_name else 'Unknown',
                'type': self.get_line_type()
            }
            self.log(f"Carrier: {carrier_name if carrier_name else 'Unknown'}", "success")
        except:
            self.results['carrier'] = {'name': 'Unknown', 'type': 'Unknown'}
            self.log("Could not determine carrier", "warning")
    
    def get_line_type(self):
        if not self.parsed_number:
            return "Unknown"
        number_type = phonenumbers.number_type(self.parsed_number)
        types = {0: 'Fixed Line', 1: 'Mobile', 2: 'Mobile/Fixed', 3: 'Toll Free',
                 4: 'Premium Rate', 5: 'Shared Cost', 6: 'VoIP', 7: 'Personal Number'}
        return types.get(number_type, 'Unknown')
    
    def get_location_approx(self):
        """Get approximate location from Geoapify API"""
        try:
            url = f"https://api.geoapify.com/v1/ipinfo?apiKey={GEOAPIFY_KEY}"
            response = requests.get(url, timeout=10)
            data = response.json()
            
            if 'location' in data:
                self.results['location'] = {
                    'city': data.get('city', {}).get('name', 'Unknown'),
                    'region': data.get('state', {}).get('name', 'Unknown'),
                    'country': data.get('country', {}).get('name', 'Unknown'),
                    'timezone': data.get('location', {}).get('timezone', {}).get('name', 'Unknown')
                }
                self.log(f"Location: {self.results['location']['city']}, {self.results['location']['country']}", "success")
            else:
                self._fallback_location()
                
        except Exception as e:
            self.log(f"Geoapify error: {str(e)[:50]}", "warning")
            self._fallback_location()
    
    def _fallback_location(self):
        """Fallback location API"""
        try:
            response = requests.get('http://ip-api.com/json/', timeout=10)
            data = response.json()
            if data.get('status') == 'success':
                self.results['location'] = {
                    'city': data.get('city', 'Unknown'),
                    'region': data.get('regionName', 'Unknown'),
                    'country': data.get('country', 'Unknown'),
                    'timezone': data.get('timezone', 'Unknown')
                }
                self.log(f"Location (fallback): {data.get('city', 'Unknown')}", "success")
            else:
                self.results['location'] = {'message': 'Could not determine location'}
                self.log("Could not determine location", "warning")
        except:
            self.results['location'] = {'message': 'Could not determine location'}
            self.log("Location detection failed", "warning")
    
    def check_whatsapp(self):
        self.log("Checking WhatsApp...", "info")
        try:
            clean_number = re.sub(r'[^0-9]', '', self.raw_number)
            if not clean_number.startswith('0') and len(clean_number) > 10:
                clean_number = '+' + clean_number
            response = requests.get(f'https://api.whatsapp.com/send/?phone={clean_number}', timeout=10, allow_redirects=True)
            self.results['whatsapp'] = 'WhatsApp' in response.text or 'wa.me' in response.text
            if self.results['whatsapp']:
                self.log("WhatsApp account found!", "success")
            else:
                self.log("No WhatsApp account found", "info")
        except:
            self.results['whatsapp'] = False
            self.log("Could not check WhatsApp", "warning")
    
    def check_telegram(self):
        self.log("Checking Telegram...", "info")
        try:
            clean_number = re.sub(r'[^0-9]', '', self.raw_number)
            if clean_number.startswith('0'):
                clean_number = clean_number[1:]
            response = requests.get(f'https://t.me/{clean_number}', timeout=10)
            self.results['telegram'] = 'If you have Telegram' in response.text and 'username' not in response.text
            if self.results['telegram']:
                self.log("Telegram account found!", "success")
            else:
                self.log("No Telegram account found", "info")
        except:
            self.results['telegram'] = False
            self.log("Could not check Telegram", "warning")
    
    def print_output(self):
        print()
        print(f"{C}{BOLD}{'='*60}{RESET}")
        print(f"{C}{BOLD}              📞 PHONE NUMBER INTELLIGENCE REPORT{RESET}")
        print(f"{C}{BOLD}{'='*60}{RESET}")
        print()
        
        print(f"{Y}{BOLD}┌──────────────────────────────────────────────────────────┐{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}📱 BASIC INFORMATION{RESET}")
        print(f"{Y}{BOLD}├──────────────────────────────────────────────────────────┤{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Phone Number     : {W}{self.raw_number}{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Valid Format     : {W}{'✅ YES' if self.results['valid'] else '❌ NO'}{RESET}")
        print(f"{Y}{BOLD}└──────────────────────────────────────────────────────────┘{RESET}")
        print()
        
        print(f"{Y}{BOLD}┌──────────────────────────────────────────────────────────┐{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}🌍 COUNTRY & REGION{RESET}")
        print(f"{Y}{BOLD}├──────────────────────────────────────────────────────────┤{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Country Code     : {W}{self.results['country'].get('code', 'N/A')}{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Country Name     : {W}{self.results['country'].get('name', 'N/A')}{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Region           : {W}{self.results['country'].get('region', 'N/A')[:40]}{RESET}")
        print(f"{Y}{BOLD}└──────────────────────────────────────────────────────────┘{RESET}")
        print()
        
        print(f"{Y}{BOLD}┌──────────────────────────────────────────────────────────┐{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}📡 CARRIER & NETWORK{RESET}")
        print(f"{Y}{BOLD}├──────────────────────────────────────────────────────────┤{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Operator         : {W}{self.results['carrier'].get('name', 'N/A')}{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Line Type        : {W}{self.results['carrier'].get('type', 'N/A')}{RESET}")
        print(f"{Y}{BOLD}└──────────────────────────────────────────────────────────┘{RESET}")
        print()
        
        print(f"{Y}{BOLD}┌──────────────────────────────────────────────────────────┐{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}📍 IP LOCATION (Approximate){RESET}")
        print(f"{Y}{BOLD}├──────────────────────────────────────────────────────────┤{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}City             : {W}{self.results['location'].get('city', 'N/A')}{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}State/Region     : {W}{self.results['location'].get('region', 'N/A')}{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Country          : {W}{self.results['location'].get('country', 'N/A')}{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Timezone         : {W}{self.results['location'].get('timezone', 'N/A')}{RESET}")
        print(f"{Y}{BOLD}└──────────────────────────────────────────────────────────┘{RESET}")
        print()
        
        print(f"{Y}{BOLD}┌──────────────────────────────────────────────────────────┐{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}💬 SOCIAL MEDIA PRESENCE{RESET}")
        print(f"{Y}{BOLD}├──────────────────────────────────────────────────────────┤{RESET}")
        wa_status = "✅ ACCOUNT FOUND" if self.results['whatsapp'] else "❌ Not found"
        tg_status = "✅ ACCOUNT FOUND" if self.results['telegram'] else "❌ Not found"
        print(f"{Y}{BOLD}│{RESET} {C}WhatsApp         : {W}{wa_status}{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}Telegram         : {W}{tg_status}{RESET}")
        print(f"{Y}{BOLD}└──────────────────────────────────────────────────────────┘{RESET}")
        print()
        
        print(f"{Y}{BOLD}┌──────────────────────────────────────────────────────────┐{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}🔓 BREACH DATABASE{RESET}")
        print(f"{Y}{BOLD}├──────────────────────────────────────────────────────────┤{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}DeHashed         : {W}🔗 https://dehashed.com{RESET}")
        print(f"{Y}{BOLD}│{RESET} {C}LeakCheck        : {W}🔗 https://leakcheck.io{RESET}")
        print(f"{Y}{BOLD}└──────────────────────────────────────────────────────────┘{RESET}")
        
        print()
        print(f"{C}{BOLD}{'='*60}{RESET}")
        print(f"{G}{BOLD}[✓] Scan completed at {self.results['timestamp']}{RESET}")
        print(f"{C}{BOLD}{'='*60}{RESET}\n")
    
    def generate_html_report(self):
        filename = f"phone_report_{self.raw_number.replace('+', '')}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.html"
        html_content = f"""<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>PhoneInfo  - Report</title>
<style>
body {{ background: #0a0a0a; font-family: monospace; color: #00ff88; padding: 30px; }}
.container {{ max-width: 1000px; margin: 0 auto; }}
h1 {{ color: #00ff88; border-bottom: 2px solid #00ff88; }}
h2 {{ color: #00cfff; margin-top: 30px; border-left: 3px solid #00cfff; padding-left: 15px; }}
.card {{ background: #0a1520; border: 1px solid #00ff88; border-radius: 10px; padding: 20px; margin-bottom: 20px; }}
.info-row {{ display: flex; padding: 8px 0; border-bottom: 1px solid #2a5a4a; }}
.info-label {{ width: 150px; color: #4acfff; }}
.info-value {{ color: #00ff88; }}
.found {{ color: #00ff88; }}
.not-found {{ color: #ff6a6a; }}
.footer {{ text-align: center; margin-top: 40px; color: #4a7a99; }}
</style>
</head>
<body>
<div class="container">
<h1>📞 PhoneInfo Pro - Report</h1>
<div class="card">
<h2>🎯 Target</h2>
<div class="info-row"><div class="info-label">Phone Number:</div><div class="info-value">{self.raw_number}</div></div>
<div class="info-row"><div class="info-label">Valid Format:</div><div class="info-value">{'✓ Yes' if self.results['valid'] else '✗ No'}</div></div>
<div class="info-row"><div class="info-label">Scan Date:</div><div class="info-value">{self.results['timestamp']}</div></div>
</div>
<div class="card">
<h2>🌍 Country</h2>
<div class="info-row"><div class="info-label">Country Code:</div><div class="info-value">{self.results['country'].get('code', 'N/A')}</div></div>
<div class="info-row"><div class="info-label">Country Name:</div><div class="info-value">{self.results['country'].get('name', 'N/A')}</div></div>
<div class="info-row"><div class="info-label">Region:</div><div class="info-value">{self.results['country'].get('region', 'N/A')}</div></div>
</div>
<div class="card">
<h2>📡 Carrier</h2>
<div class="info-row"><div class="info-label">Operator:</div><div class="info-value">{self.results['carrier'].get('name', 'N/A')}</div></div>
<div class="info-row"><div class="info-label">Line Type:</div><div class="info-value">{self.results['carrier'].get('type', 'N/A')}</div></div>
</div>
<div class="card">
<h2>📍 IP Location</h2>
<div class="info-row"><div class="info-label">City:</div><div class="info-value">{self.results['location'].get('city', 'N/A')}</div></div>
<div class="info-row"><div class="info-label">State/Region:</div><div class="info-value">{self.results['location'].get('region', 'N/A')}</div></div>
<div class="info-row"><div class="info-label">Country:</div><div class="info-value">{self.results['location'].get('country', 'N/A')}</div></div>
<div class="info-row"><div class="info-label">Timezone:</div><div class="info-value">{self.results['location'].get('timezone', 'N/A')}</div></div>
</div>
<div class="card">
<h2>💬 Social Media</h2>
<div class="info-row"><div class="info-label">WhatsApp:</div><div class="info-value">{'✓ Found' if self.results['whatsapp'] else '✗ Not found'}</div></div>
<div class="info-row"><div class="info-label">Telegram:</div><div class="info-value">{'✓ Found' if self.results['telegram'] else '✗ Not found'}</div></div>
</div>
<div class="footer">Report by PhoneInfo Pro | TyraxZero</div>
</div>
</body>
</html>"""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        return filename
    
    def run(self):
        if not self.validate_format():
            return
        self.get_country_info()
        self.get_carrier_info()
        self.get_location_approx()
        self.check_whatsapp()
        self.check_telegram()
        self.print_output()
        report = self.generate_html_report()
        print(f"{G}[✓] HTML Report saved: {report}{RESET}\n")

def main():
    banner()
    phone = input(f"  {C}{BOLD}[>]{RESET} Phone number (with country code): {W}").strip()
    if not phone:
        print(f"\n{R}[!] Invalid number!{RESET}")
        return
    scanner = PhoneInfoPro(phone)
    scanner.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{Y}[!] Stopped by user{RESET}")
