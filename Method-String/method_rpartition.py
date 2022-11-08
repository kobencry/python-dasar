# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=rpartition#str.rpartition

# Catatan:
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi repartition() mencari kemunculan terakhir dari string yang ditentukan, 
# dan membagi string menjadi tuple yang berisi tiga elemen.
# Elemen pertama berisi bagian sebelum string yang ditentukan.
# Elemen kedua berisi string yang ditentukan.
# Elemen ketiga berisi bagian setelah string.

# Syntax
# string.rpartition(value)

# Nilai Parameter
# Parameter              Deskripsi
# value                  Dibutuhkan. String untuk mencari

text = "hello alice carl eliot"
x = text.rpartition('alice')
y = text.rpartition('carl')

print(x)    # ('hello ', 'alice', ' carl eliot')
print(y)    # ('hello alice ', 'carl', ' eliot')

text = "hello alice carl eliot alice"
x = text.rpartition('alice')
y = text.rpartition('python')

print(x)    # ('hello alice carl eliot ', 'alice', '')
print(y)    # ('', '', 'hello alice carl eliot alice')
# jika ingin mempelajari lebih lanjut tentang Method-Tuple kunjungi folder_name: "Method-Tuple"
