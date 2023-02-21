# -- python exception --

# raise adalah sebuah keyword dalam bahasa pemrograman Python
# yang digunakan untuk melemparkan exception atau kesalahan secara manual. 
# Dalam Python, kita dapat menggunakan keyword raise untuk memicu exception tertentu
# pada kondisi-kondisi tertentu yang tidak diinginkan.

# Kita dapat menentukan jenis exception yang ingin diangkat bersamaan dengan pesan atau argumen lain
# yang mungkin diperlukan, untuk memberikan informasi tambahan tentang kesalahan tersebut. 
# Dalam hal ini, pesan yang dimasukkan akan ditampilkan bersamaan dengan jenis exception saat dijalankan.

try:
    x = 10
    if x > 5:
        raise ValueError("x harus lebih kecil dari 5")
except ValueError as err:
    print(err)
# Output:
# x harus lebih kecil dari 5

# fungsi ini memvalidasi panjang password
def protec_password(password):
    if len(str(password)) <= 8:
        raise Exception(f"(!) password '{password}' kurang panjang coba lagi.")
    else:
        print("passed")
try:
    protec_password("abc123")
except Exception as err:
    print(err)
# Output:
# (!) password 'abc123' kurang panjang coba lagi