# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=partition#str.partition

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi partition() mencari string yang ditentukan, dan membagi string menjadi tuple yang berisi tiga elemen.
# Elemen pertama berisi bagian sebelum string yang ditentukan.
# Elemen kedua berisi string yang ditentukan.
# Elemen ketiga berisi bagian setelah string.
# Catatan: fungsi partition() ini mencari kemunculan pertama dari string yang ditentukan.

# Syntax
# string.partition(value)

# Nilai Parameter
# Parameter             Deskripsi
# value                 Dibutuhkan. String untuk mencari.

text = "hello alice carl eliot"
x = text.partition('alice')
y = text.partition('carl')

print(x)    # ('hello ', 'alice', ' carl eliot')
print(y)    # ('hello alice ', 'carl', ' eliot')

text = "hello alice carl eliot alice"
x = text.partition('alice')
y = text.partition('python')

print(x)    # ('hello ', 'alice', ' carl eliot alice')
print(y)    # ('hello alice carl eliot alice', '', '')

print("hello world".partition('war'))   # ('hello world', '', '')
# jika ingin mempelajari lebih lanjut tentang Method-Tuple kunjungi folder_name: "Method-Tuple"
