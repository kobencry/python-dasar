# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=remove#list.remove

# fungsi remove() menghapus kejadian pertama dari elemen list dengan nilai yang ditentukan.

# Syntax
# list.remove(elemen)

# Nilai Parameter
# Parameter                 Deskripsi
# elemen                    Dibutuhkan. Jenis apa pun (string, angka, list, dll.) Elemen yang ingin Anda hapus.

listku = ["hello", False, 2.5, "alice", None, 20, 'carl', True]

listku.remove('alice')
print(listku)   # ['hello', False, 2.5, None, 20, 'carl', True]

listku.remove(listku[1])
print(listku)   # ['hello', 2.5, None, 20, 'carl', True]

listku.remove(listku[len(listku) - 1])
print(listku)   # ['hello', 2.5, None, 20, 'carl']

listku.remove(listku[-3])
print(listku)   # ['hello', 2.5, 20, 'carl']

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
