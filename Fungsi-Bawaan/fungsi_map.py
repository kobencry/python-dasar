# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html#map

# fungsi map() adalah sebuah fungsi-bawaan dalam bahasa pemrograman Python yang memungkinkan 
# kita untuk menerapkan suatu fungsi ke setiap elemen dalam sebuah iterable, seperti list, tuple, atau set.
# Fungsi ini akan menghasilkan sebuah objek baru yang berisi hasil dari menerapkan fungsi tersebut 
# pada setiap elemen dalam iterable tersebut.

# Syntax
# map(function, iterable_1, iterable_2, ...dst)

# Nilai Parameter
# Parameter                 Deskripsi
# function                  Dibutuhkan. Fungsi untuk mengeksekusi untuk setiap item
# iterable                  Diperlukan. Urutan, koleksi, atau objek iterator. Anda dapat mengirim iterable sebanyak yang Anda suka, 
#                           pastikan fungsinya memiliki satu parameter untuk setiap iterable.

# menghitung panjang setiap kata dalam list
hasil = map(lambda kata: len(kata), ['alice', 'carl', 'eliot'])
print(hasil)
# Output:
# <map object at 0x0000027ED6083310>

# mengubah map menjadi list, agar mudah dibaca
print(list(hasil))
# Output:
# [5, 4, 5]

# jika anda tidak terbiasa dengan fungsi lambda(anonymous function)
# kode ini setara dengan diatas
def fungsiku(kata):
    return len(kata)
hasil = list(map(fungsiku, ['alice', 'carl', 'eliot']))
print(hasil)
# Output:
# [5, 4, 5]

# atau bisa seperti ini menggunakan fungsi len()
hasil = list(map(len, ['alice', 'carl', 'eliot']))
print(hasil)
# [5, 4, 5]

# memangkatkan dua dari masing-masing elemen dalam list angka.
hasil = list(map(lambda angka: angka**2, [1, 2, 3, 4, 5]))
print(hasil)
# Output:
# [1, 4, 9, 16, 25]

# mengubah string huruf kecil menjadi huruf besar
s = list(map(str.upper, ['alice', 'carl', 'eliot']))
print(s)
# Output:
# ['ALICE', 'CARL', 'ELIOT']

# menghitung jumlah nama elemen yang sama
from collections import Counter

listku = ['foo', 'bar', 'foo', 'baz', 'bar', 'foo', 'baz', 'foo', 'bar']
dictku = Counter(listku)

hasil = dict(map(lambda x: (x[0], x[1]), dictku.items()))
print(hasil)
# Output:
# {'foo': 4, 'bar': 3, 'baz': 2}

# fungsi map() setara dengan menulis ekspresi generator
def fungsi_map(function, iterable):
    return (function(i) for i in iterable)

hasil = list(fungsi_map(str.lower, ['ALICE', 'CARL', 'ELIOT']))
print(hasil)
# Output:
# ['alice', 'carl', 'eliot']

# menerima inputan dari user
uint = list(map(int, input("masukan angka: ").split()))
print(uint)

# jika ingin mempelajari lebih lanjut tentang modul-collection Counter() kunjungi folder_name: "modul-collections/collections-Counter"
# jika ingin mempelajari lebih lanjut tentang fungsi lambda(anonymous functions) kunjungi folder_name: "python-def/def_lambda.py"