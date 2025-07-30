import os
import subprocess
from pyfiglet import figlet_format
from termcolor import cprint, colored

# Banner ASCII
def banner():
    os.system("clear")  # Atau "cls" kalau di Windows
    cprint(figlet_format("JIZJAZ", font="slant"), "cyan")
    cprint("=== CYBER AUTORECON TOOL ===", "green", attrs=["bold"])
    cprint("created by jizjaz the cat", "red")

# Fungsi Nmap
def nmap_scan(target):
    cprint(f"[+] Scanning {target} with Nmap...", "yellow")
    output_file = f"results/{target.replace('.', '_')}_nmap.txt"
    os.makedirs("results", exist_ok=True)
    with open(output_file, "w") as f:
        subprocess.call(["nmap", "-sV", "-Pn", target], stdout=f)
    cprint(f"[✓] Nmap result saved: {output_file}", "green")

# Fungsi Nikto
def nikto_scan(target):
    cprint(f"[+] Scanning {target} with Nikto...", "yellow")
    output_file = f"results/{target.replace('.', '_')}_nikto.txt"
    os.makedirs("results", exist_ok=True)
    with open(output_file, "w") as f:
        subprocess.call(["nikto", "-h", target], stdout=f)
    cprint(f"[✓] Nikto result saved: {output_file}", "green")

# Fungsi WHOIS
def whois_lookup(target):
    cprint(f"[+] Performing WHOIS lookup on {target}...", "yellow")
    output_file = f"results/{target.replace('.', '_')}_whois.txt"
    os.makedirs("results", exist_ok=True)
    with open(output_file, "w") as f:
        subprocess.call(["whois", target], stdout=f)
    cprint(f"[✓] WHOIS result saved: {output_file}", "green")

# Menu utama
def menu():
    banner()
    target = input(colored("Enter IP or Domain: ", "cyan"))
    while True:
        cprint("""
=== AutoRecon Menu ===
[1] Nmap Scan
[2] Nikto Scan
[3] WHOIS Lookup
[0] Exit
""", "blue", attrs=["bold"])
        choice = input(colored("Select option: ", "yellow"))
        if choice == "1":
            nmap_scan(target)
        elif choice == "2":
            nikto_scan(target)
        elif choice == "3":
            whois_lookup(target)
        elif choice == "0":
            cprint("[*] Exiting JIZJAZ AutoRecon. Goodbye!", "red")
            break
        else:
            cprint("[!] Invalid choice. Try again.", "red")

# Jalankan program
if __name__ == "__main__":
    menu()

