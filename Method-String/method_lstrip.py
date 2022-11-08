# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=lstrip#str.lstrip

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi lstrip() menghapus semua karakter tertentu atau utama (karakter diawal/dikiri string).
# (defaultnya/standarnya adalah karakter spasi yang akan dihapus)

# Syntax
# string.lstrip(karakter)

# Nilai Parameter
# Parameter             Deskripsi
# karakter              Opsional. Satu set karakter untuk dihapus sebagai karakter utama

x = "   Hello World"
y = "https://www.google.com"
print(x.lstrip()) # Hello World
print(y.lstrip('htps:/'))   # www.google.com


x = "   hello world    "
y = "..,,,Hello, world!"
print(x.lstrip())   # hello world  "ini sebenernya ada karakter (spasi)"
print(x.lstrip(), '<-spasi')  # hello world      <-spasi
print(x.lstrip() + '<-spasi') # hello world     <-spasi
print(y.lstrip('.,')) # Hello, world!
