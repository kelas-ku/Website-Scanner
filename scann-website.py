import socket
import os

# Warna terminal
hijau = '\033[1;32m'
kuning = '\033[1;33m'
merah = '\033[1;31m'
magenta = '\033[1;37m'
reset = '\033[1;0m'

# Banner ASCII Art
print(rf"""{kuning}
 __      _____ ___ ___ ___ _____ ___   ___  ___   _   _  _ _  _ ___ _  _  ___ 
 \ \    / / __| _ ) __|_ _|_   _| __| / __|/ __| /_\ | \| | \| |_ _| \| |/ __|
  \ \/\/ /| _|| _ \__ \| |  | | | _|  \__ \ (__ / _ \| .` | .` || || .` | (_ |
   \_/\_/ |___|___/___/___| |_| |___| |___/\___/_/ \_\_|\_|_|\_|___|_|\_|\___|
   
{hijau}Author: {magenta}Zayad K.{reset}
{hijau}Github: {magenta}https://github.com/kelas-ku{reset}
{hijau}Instagram: {magenta}https://www.instagram.com/zayad_kanani/{reset}
""")

# Menu pilihan
print(f"{hijau}Pilih menu scanning:{reset}")
print("1. DNS Lookup (IP dari domain)")
print("2. Reverse DNS (Domain dari IP)")
print("3. Port Scanner (cek port terbuka)")
print("4. Ping Test (cek host aktif)")
print("0. Keluar")

pilihan = input(f"{kuning}Masukkan nomor menu: {reset}")

# Menu 1: DNS Lookup
if pilihan == "1":
    website = input(f"{hijau}Masukkan domain target: {reset}")
    try:
        ip_addres = socket.gethostbyname_ex(website)[2]
        for ip in ip_addres:
            print(f"{hijau}Alamat IP dari {kuning}{website}{hijau} adalah: {ip}{reset}")
    except socket.gaierror:
        print(f"{merah}Domain {website} tidak valid!{reset}")

# Menu 2: Reverse DNS
elif pilihan == "2":
    ip = input(f"{hijau}Masukkan alamat IP target: {reset}")
    try:
        host = socket.gethostbyaddr(ip)
        print(f"{hijau}Nama domain dari IP {kuning}{ip}{hijau} adalah: {host[0]}{reset}")
    except socket.herror:
        print(f"{merah}Tidak ditemukan domain untuk IP {ip}{reset}")

# Menu 3: Port Scanner
elif pilihan == "3":
    target = input(f"{hijau}Masukkan domain/IP target: {reset}")
    ports = [21, 22, 80, 443]  # daftar port umum
    print(f"{kuning}Scanning port pada {target}...{reset}")
    for port in ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((target, port))
        if result == 0:
            print(f"{hijau}Port {port} terbuka{reset}")
        else:
            print(f"{merah}Port {port} tertutup{reset}")
        sock.close()

# Menu 4: Ping Test
elif pilihan == "4":
    target = input(f"{hijau}Masukkan domain/IP target: {reset}")
    print(f"{kuning}Melakukan ping ke {target}...{reset}")
    # Perintah ping berbeda di Windows/Linux
    if os.name == "nt":  # Windows
        os.system(f"ping {target}")
    else:  # Linux/Mac
        os.system(f"ping -c 4 {target}")

# Menu 0: Keluar
elif pilihan == "0":
    print(f"{hijau}Program selesai!{reset}")

# Input salah
else:
    print(f"{merah}Pilihan menu tidak valid!{reset}")
