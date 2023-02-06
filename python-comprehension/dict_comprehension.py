# Dictionary Comprehension adalah jenis comprehension yang digunakan untuk membuat sebuah dictionary. 
# Dictionary Comprehension membuat sebuah dictionary baru dari suatu iterasi.
# Misalnya, kita memiliki sebuah list nama dan ingin membuat dictionary dari angka dan nama
# tersebut dengan key adalah angka dan value adalah nama.
# Kita dapat menggunakan Dictionary Comprehension untuk mencapai hal tersebut seperti kode berikut ini:

# Syntax
# new_dict = {key_expression: value_expression for key, val in iterable}
dictku = {key:val for key, val in enumerate(['alice', 'carl', 'eliot'], start=1)}
print(dictku)
# Output:
# {1: 'alice', 2: 'carl', 3: 'eliot'}

# kode ini setara dengan diatas
dictku = {}
for key, val in enumerate(['alice', 'carl', 'eliot'], start=1): # nomor indeks dimulai dari 1
    dictku[key] = val
print(dictku)
# Output:
# {1: 'alice', 2: 'carl', 3: 'eliot'}

# atau dengan menambahkan kondisional di akhir ekspresi
# new_dict = {key_expression: value_expression for key, val in iterable (if conditional)}