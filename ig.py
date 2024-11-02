import requests
from colorama import Fore, Style

def cek_akun_instagram(username):
    url = f"https://www.instagram.com/{username}/"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            return f"{username} {Fore.GREEN}active{Style.RESET_ALL}"
        elif response.status_code == 404:
            return f"{username} {Fore.RED}not active{Style.RESET_ALL}"
        else:
            return f"{username} status unknown (code: {response.status_code})"
    except requests.exceptions.RequestException as e:
        return f"{username} error: {e}"

def main():
    usernames = input("Masukkan username Instagram (pisahkan dengan koma): ").split(',')
    active_count = 0
    inactive_count = 0

    print("\n======== SEARCH RESULTS ========")
    for username in usernames:
        username = username.strip()  # Menghapus spasi
        result = cek_akun_instagram(username)
        print(result)
        
        if "active" in result:
            active_count += 1
        elif "not active" in result:
            inactive_count += 1

    print("\nJumlah akun aktif:", active_count)
    print("Jumlah akun tidak aktif:", inactive_count)

if __name__ == "__main__":
    main()
