# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=clear#list.clear

# fungsi clear() menghapus semua elemen dari list

# Syntax
# list.clear()

# Nilai Parameter
# tidak ada nilai parameter

listku = ['hello', 'world']
print(listku)   # sebelum ['hello', 'world']
listku.clear()
print(listku)   # sesudah []

# periksa apakah ada elemen list, jika ada maka hapus elemen tersebut
listku = ['hello', False, 2.5, None, True]
print(listku)   # ['hello', False, 2.5, None, True]
if bool(listku):
    listku.clear()
    print('elemen list telah dihapus')
print(listku)

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan bool() kunjungi folder_name: "Fungsi-Bawaan/fungsi_bool.py"
