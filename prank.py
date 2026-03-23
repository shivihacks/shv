import time
import sys
import random
import os

# Colors for terminal
GREEN = "\033[1;32m"
RED = "\033[1;31m"
BLUE = "\033[1;34m"
WHITE = "\033[1;37m"
YELLOW = "\033[1;33m"
RESET = "\033[0m"

def typing_effect(text, color=GREEN, speed=0.04):
    sys.stdout.write(color)
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print(RESET)

def fake_hacking():
    os.system('clear' if os.name == 'posix' else 'cls')
    
    # Header
    print(f"{RED}###############################################")
    print(f"##          SHV CYBER-ATTACK SYSTEM          ##")
    print(f"###############################################{RESET}\n")
    
    time.sleep(1)
    typing_effect("[*] Initializing Bruteforce Attack on Mainframe...", BLUE)
    typing_effect("[*] Connecting to Proxy: 192.168.1.105...", BLUE)
    typing_effect("[*] Bypassing SSL Encryption...", BLUE)
    
    # Fake scrolling data
    for _ in range(30):
        hex_data = "".join(random.choices("0123456789ABCDEF", k=16))
        print(f"{GREEN}[DATA_STREAM] {hex_data} | STATUS: INJECTING...{RESET}")
        time.sleep(0.05)

    print(f"\n{YELLOW}[!] FIREWALL DETECTED! Attempting Manual Bypass...{RESET}")
    time.sleep(1.5)

    # Fake loading bar
    for i in range(101):
        sys.stdout.write(f"\r{WHITE}Decrypting Passwords: [{GREEN}{'#' * (i // 5)}{' ' * (20 - (i // 5))}{WHITE}] {i}%")
        sys.stdout.flush()
        time.sleep(0.03)
    
    print("\n")
    typing_effect("[+] Password Found: admin_shiva_99", GREEN)
    typing_effect("[+] Accessing Database: 'User_Records'...", GREEN)
    
    time.sleep(1)
    
    # Final Message
    print(f"\n{RED}***********************************************")
    print(f"** SYSTEM HACKED SUCCESSFULLY       **")
    print(f"***********************************************{RESET}")
    
    input(f"\n{WHITE}Press Enter to exit the terminal...{RESET}")

if __name__ == "__main__":
    try:
        fake_hacking()
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Attack Aborted by User.{RESET}")
