import requests
from bs4 import BeautifulSoup

# Kode warna ANSI
GREEN = '\033[92m'  # Hijau terang
RED = '\033[91m'    # Merah terang
RESET = '\033[0m'   # Reset warna

# Membaca username dari file usernames.txt
with open('name.txt', 'r') as file:
    username_list = [line.strip() for line in file]

# Inisialisasi penghitung
active_count = 0
not_active_count = 0

# Melakukan iterasi untuk setiap username dalam file
for username in username_list:
    url = f"https://www.instagram.com/{username}/"
    response = requests.get(url)
    
    # Cek apakah permintaan berhasil
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Mengambil nama lengkap pengguna sebagai indikator apakah profil ada
        full_name_meta = soup.find('meta', property="og:title")
        
        if full_name_meta and 'content' in full_name_meta.attrs:
            print(f"{username}: {GREEN}active{RESET}")
            active_count += 1
        else:
            print(f"{username}: {RED}not active{RESET}")
            not_active_count += 1
    else:
        print(f"{username}: {RED}not active{RESET}")
        not_active_count += 1

# Menampilkan jumlah akun aktif dan tidak aktif
print(f"\nJumlah akun aktif: {active_count}")
print(f"Jumlah akun tidak aktif: {not_active_count}")
