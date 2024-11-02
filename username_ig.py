import re

# Nama file input yang berisi username dan email
input_filename = 'input_text.txt'
# Nama file output untuk menyimpan username
output_filename = 'usernames.txt'

# Fungsi untuk mengekstrak username dari teks
def extract_usernames(text):
    # Menggunakan regex untuk mencocokkan username di awal baris yang diikuti oleh email
    # Regex ini menganggap username adalah kata pertama sebelum spasi dan '@' muncul dalam teks
    usernames = re.findall(r'\b[a-zA-Z0-9._-]+(?=\s+[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', text)
    return usernames

# Membaca teks dari file input
with open(input_filename, 'r') as file:
    text = file.read()

# Mengekstrak username dari teks
usernames = extract_usernames(text)

# Menyimpan username ke dalam file output
with open(output_filename, 'w') as file:
    for username in usernames:
        file.write(username + '\n')

print(f"Username telah disimpan dalam '{output_filename}'.")
