import requests

def cek_akun_instagram(username):
    # URL profil Instagram
    url = f"https://www.instagram.com/{username}/"
    
    try:
        # Mengirim permintaan GET
        response = requests.get(url)
        
        # Memeriksa status kode respons
        if response.status_code == 200:
            return f"Akun Instagram '{username}' ada."
        elif response.status_code == 404:
            return f"Akun Instagram '{username}' tidak ditemukan."
        else:
            return f"Terjadi kesalahan saat memeriksa akun '{username}'. Status kode: {response.status_code}"
    except requests.exceptions.RequestException as e:
        return f"Kesalahan dalam permintaan: {e}"

# Contoh penggunaan
username = "dctype_45"
hasil = cek_akun_instagram(username)
print(hasil)