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

# Catatan: fungsi pop()mengembalikan nilai yang dihapus.

listku = ['alce', 'carl', 'eliot']
x = []
while len(listku):
    i = listku.pop()
    print(i)
    x.append(i)
print(x)    # ['eliot', 'carl', 'alce']


# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
