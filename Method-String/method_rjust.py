# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=rjust#str.rjust

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi rjust() akan menyelaraskan/menyesuaikan/menggeser string ke kanan, menggunakan karakter tertentu (default/standarnya adalah spasi) sebagai karakter pengisi.

# Syntax
# string.rjust(panjang, karakter)

# Nilai Parameter
# Parameter             Deskripsi
# panjang               Dibutuhkan. Panjang string yang dikembalikan
# karakter              Opsional. Sebuah karakter untuk mengisi spasi yang hilang (di sebelah kiri string). Standarnya/default adalah " " (spasi).

x = "hello"
y = "hello"
print(x.rjust(20))        #                hello
print(y.rjust(20, '+'))   # +++++++++++++++hello

# contoh dengan daftar judul buku
print("1.", 'python3'.rjust(20, '.'))
print("2.", 'python-oop'.rjust(20, '.'))
print("3.", 'python-expert'.rjust(20, '.'))
# 1. .............python3
# 2. ..........python-oop
# 3. .......python-expert

print("123".rjust(5, '0'))  # 00123
