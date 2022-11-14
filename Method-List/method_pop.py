# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=pop#list.pop

# fungsi pop() menghapus elemen list pada posisi yang ditentukan.

# Syntax
# list.pop(posisi)

# Nilai Parameter
# Parameter                 Deskripsi
# posisi                    Opsional. Angka yang menentukan posisi elemen yang ingin Anda hapus, nilai defaultnya adalah -1, yang mengembalikan item terakhir

listku = ['alice', 'carl', 'eliot', 'geral']
print(listku)   # ['alice', 'carl', 'eliot', 'geral'] 

listku.pop()
print(listku)   # ['alice', 'carl', 'eliot']

listku.pop(1)
print(listku)   # ['alice', 'eliot']

listku.pop(0)
print(listku)   # ['eliot']

listku = ['alice', 'carl', 'eliot', 'geral']
listku.pop(len(listku) - 2)
print(listku)   # ['alice', 'carl', 'geral']

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
