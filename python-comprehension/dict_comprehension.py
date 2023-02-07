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

# menambahkan kondisional di akhir ekspresi
# new_dict = {key_expression: value_expression for key, val in iterable (if conditional)}
ipk_mahasiswa = {'alice':3.2, 'carl':2.7, 'eliot':3.4}
lulus = {nama:ipk for nama, ipk in ipk_mahasiswa.items() if ipk >= 3.0}
print(lulus)
# Output:
# {'alice': 3.2, 'eliot': 3.4}

# kode ini setara dengan diatas
lulus = {}
for nama, ipk in ipk_mahasiswa.items():
    if ipk >= 3.0:
        lulus[nama] = ipk
print(lulus)
# Output:
# {'alice': 3.2, 'eliot': 3.4}

# menambahkan kondisional di awal ekspresi
# new_dict = {key_expression: val_expression(if conditional) for key, val in iterable}
karyawan = {'alice':23, 'carl':30, 'eliot':24, 'guido':60, 'steve': 70}
dictku = {nama:('junior' if usia <= 40 else 'senior') for nama, usia in karyawan.items()}
print(dictku)
# Output:
# {'alice': 'junior', 'carl': 'junior', 'eliot': 'junior', 'guido': 'senior', 'steve': 'senior'}

# kode ini setara dengan diatas
dictku = {}
for nama, usia in karyawan.items():
    if usia <= 40:
        dictku[nama] = 'junior'
    else:
        dictku[nama] = 'senior'
print(dictku)
# Output:
# {'alice': 'junior', 'carl': 'junior', 'eliot': 'junior', 'guido': 'senior', 'steve': 'senior'}