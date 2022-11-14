# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=insert#list.insert

# fungsi insert() menyisipkan nilai yang ditentukan pada posisi yang ditentukan.

# Syntax
# list.insert(posisi, elemen)

# Nilai Parameter
# Parameter                 Deskripsi
# posisi                    Dibutuhkan. Angka yang menentukan di posisi mana untuk memasukkan nilai
# elemen                    Dibutuhkan. Elemen jenis apa pun (string, angka, objek, dll.)

listku = ['hello', 'world']
print(listku)   # sebelum ['hello', 'world'] 

listku.insert(1, False)
print(listku)   # sesudah ['hello', False, 'world']

listku.insert(0, 'alice')
print(listku)   # ['alice', 'hello', False, 'world']

listku.insert(10, True)
print(listku)   # ['alice', 'hello', False, 'world', True]

listku.insert(6, 'carl')
print(listku)   # ['alice', 'hello', False, 'world', True, 'carl']

listku.insert(len(listku), None)
print(listku)   # ['alice', 'hello', False, 'world', True, 'carl', None]

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
