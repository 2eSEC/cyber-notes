# Sample Python Script: Nmap Automation

import subprocess

target = "192.168.1.1"
command = f"nmap -sV {target}"

output = subprocess.getoutput(command)
print(output)
