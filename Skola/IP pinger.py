# 4. Ip pinger
#  Lägg till IP-adresser i en text fil (en ip-adress per rad).
#  Öppna filen och pinga varje ip-adress. Skriv ut resultatet till terminalen och till en fil.
#  Använd följande i toppen av ditt skript:
#  import os
#  Os-funktion för att pinga en adress (en funktion för win och en för linux):
#  os.system(f"ping-c 1 {ip_address} > /dev/null 2>&1") # Linux
#  os.popen(f"ping-n 1 {ip_address}").read() # Window

import os

ip_list = []

with open("IP_addresses.txt", "r") as file:
    for line in file:
        ip_adresses = line.strip()
        ip_list.append(ip_adresses)

for ip in ip_list:
    output = os.popen(f"ping {ip}").read()
    print(f"Pinging {ip}: {output}")
    with open("IP_pinger.txt", "a") as file:
        file.write(output + "\n")

print("Ping output was added to textfile IP_pinger.txt")