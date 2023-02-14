# -- Fungsi bawaan python --

# fungsi list() membuat objek list.
# Objek list adalah koleksi yang dipesan dan dapat diubah.

# Syntax
# list(iterable)

# Nilai Parameter
# Parameter             Deskripsi
# iterable              Opsional. Urutan, koleksi, atau objek iterator

# menggunakan tipe data string
listku = list('hello world')
print(listku)
# Output:
# ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# menggunakan tipe data list
listku = list(['alice', 'carl', 'eliot'])
print(listku)
# Output:
# ['alice', 'carl', 'eliot']

# menggunakan tipe data tuple
listku = list(('alice', 'carl', 'eliot'))
print(listku)
# Output:
# ['alice', 'carl', 'eliot']

# menggunakan tipe data set
listku = list({'alice', 'carl', 'eliot'})
# Output:
# ['alice', 'carl', 'eliot']

# menggunakan fungsi range()
listku = list(range(1, 6))
print(listku)
# Output:
# [1, 2, 3, 4, 5]

# menggunakan list comprehension
listku = list(i for i in range(1, 11) if i %2==0)
print(listku)
# Output:
# [2, 4, 6, 8, 10]

# menggunakan generator fungsi map()
angka = list(range(1, 6))
listku = list(map(lambda x: x**2, angka))
print(listku)
# Output:
# [1, 4, 9, 16, 25]

# jika ingin mempelajari lebih lanjut tentang koleksi-list  kunjungi folder_name: "Method-List"
# jika ingin mempelajari lebih lanjut tentang comprehension  kunjungi folder_name: "python-comprehension"
# jika ingin mempelajari lebih lanjut tentang generators  kunjungi folder_name: "python-generator"