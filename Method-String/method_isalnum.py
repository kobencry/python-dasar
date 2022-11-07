# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isalnum#str.isalnum

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isalnum() mengembalikan nilai boolean True jika semua karakter
# huruf alfabet (a-z) dan angka (0-9) 
# contoh karakter yang bukan alfanumerik (spasi)!@#$%^_{}? dll.
# jika tidak, maka akan mengembalikan nilai boolean False

# Syntax
# string.isalnum()

# Nilai Parameter
# tidak ada nilai parameter

s = "hello"
print(s.isalnum())

s = "hello123"
print(s.isalnum())

s = "hello world"
print(s.isalnum())

s = "hello!"
print(s.isalnum())

username = input("masukan alphanumerik: ")
# pelajari lebih lanjut tentang fungsi-bawaan input() folder_name: "Fungsi-Bawaan/fungsi_input.py"
# jika username adalah alpahnumerik (a-z0-9)
if username.isalnum(): # statement if jika nilai boolean True jalankan dibawah ini
    print("passed") # tampilkan "passed" jika nilai boolean True
else:
    # jika statement if nilai boolean False jalankan dibawah ini
    print("failed") # tampilkan "failed" jika statemen if nilai boolean False
