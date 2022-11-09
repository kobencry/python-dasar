# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=split#str.split

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi split() membagi string menjadi tipe data list.

# Syntax
# string.split(separator, maxsplit)

# Nilai Parameter
# Parameter             Deskripsi
# separator             Opsional. Menentukan pemisah yang akan digunakan saat memisahkan string. Secara default/standarnya setiap spasi adalah pemisah
# maxsplit              Opsional. Menentukan berapa banyak split yang harus dilakukan. Nilai default adalah -1, yang merupakan "semua kejadian"

x = "Hello World"
print(x.split())    # ['Hello', 'World']

x = "alice#carl#eliot"
print(x.split('#')) # ['alice', 'carl', 'eliot']

x = "alice#carl#eliot"
print(x.split('#', 1))  # ['alice', 'carl#eliot']

# jika ingin mempelajari lebih lanjut tentang Method-List kunjungi folder_name: "Method-List"
