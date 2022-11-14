# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=append#list.append

# fungsi append() menambahkan elemen list ke akhir list.

# Syntax
# list.append(elemen)

# Nilai Parameter
# Parameter             Deskripsi
# elemen                Dibutuhkan. Elemen jenis apa pun (string, angka, objek, dll.)

# list kosong
listku = []
print(listku)   # sebelum []
listku.append('alice')
listku.append(False)
print(listku)   # ['alice', False]
listku.append(2.5)
print(listku)   # ['alice', False, 2.5]

# menggunakan looping 
listku = ['hello']
for i in ['alice', True, 2.5, ('world', None)]:
    listku.append(i)
print(listku)   # ['hello', 'alice', True, 2.5, ('world', None)]

# menggunakan tipe data list, tuple dan dict
listku = ['hello']
# tipe data list
listku.append(['alice', 'carl', 'eliot'])
print(listku)   # ['hello', ['alice', 'carl', 'eliot']]

# tipe data tuple
listku.append((False, 2.5))
print(listku)   # ['hello', ['alice', 'carl', 'eliot'], (False, 2.5)]

# tipe data dict
listku.append({'id':555444})
print(listku)   # ['hello', ['alice', 'carl', 'eliot'], (False, 2.5), {'id': 555444}]

# menggunakan elemen yang berisi fungsi, dan operator perbandingan
def fungsi():
   print("hello world") 
#print(type(fungsi)) # <class 'function'>

listku = ['hello']
listku.append(3>2)
listku.append(2==3)
listku.append([fungsi, fungsi()])
print(listku)   # ['hello', True, False, [<function fungsi at 0x000001C21AF53E20>, None]]

# jika ingin mempelajari lebih lanjut tentang operator kunjungi folder_name: "python-operator" 
