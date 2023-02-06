# Comprehension adalah fitur ekspresif pada bahasa pemrograman Python yang memungkinkan Anda 
# untuk membuat objek seperti list, tuple, set, atau dictionary dengan cara yang sederhana dan efisien. 
# Comprehension memungkinkan Anda untuk membuat koleksi baru dengan looping melalui koleksi lain
# dan melakukan manipulasi pada setiap elemen selama proses pembuatan. 
# Ini sangat berguna ketika Anda ingin membuat sebuah list hasil dari operasi 
# yang dilakukan pada setiap elemen dalam sebuah koleksi.

# List Comprehension adalah jenis comprehension paling sering digunakan dalam Python. 
# List Comprehension membuat sebuah list baru dari suatu iterasi. 
# Misalnya, kita memiliki sebuah list angka dan ingin mencari angka yang lebih besar dari 10.
# Kita dapat menggunakan List Comprehension untuk mencapai hal tersebut dengan mudah seperti kode berikut ini:

# Syntax
# new_list = [expression for item in iterable]
# atau dengan menambahkan kondisional di akhir ekspresi
# new_list = [expression for item in iterable (if conditional)]

hasil = [i for i in range(1, 11) if i > 5]
print(hasil)
# Output:
# [6, 7, 8, 9, 10]
# yaitu sebuah list baru yang berisi angka yang lebih besar dari 10.

# kode ini setara dengan yang diatas
hasil = []
for i in range(1, 11): # dimulai dari 1 sampai 10
    if i > 5:
        hasil.append(i)
print(hasil)
# Output:
# [6, 7, 8, 9, 10]

#==================================================================================

# Set Comprehension adalah jenis comprehension yang digunakan untuk membuat sebuah set.
# Set Comprehension membuat sebuah set baru dari suatu iterasi.
# Misalnya, kita memiliki sebuah list angka dan ingin membuat set dari angka-angka tersebut.
# Kita dapat menggunakan Set Comprehension untuk mencapai hal tersebut seperti kode berikut ini:

# Syntax
# new_set = {expression for item in iterable}
# atau dengan menambahkan kondisional di akhir ekspresi
# new_set = {expression for item in iterable (if conditional)}

setku = {i for i in range(1, 6)}
print(setku)
# Output:
# {1, 2, 3, 4, 5}
# yaitu sebuah set baru dari angka-angka tersebut.

#==================================================================================

# Dictionary Comprehension adalah jenis comprehension yang digunakan untuk membuat sebuah dictionary. 
# Dictionary Comprehension membuat sebuah dictionary baru dari suatu iterasi.
# Misalnya, kita memiliki sebuah list nama dan ingin membuat dictionary dari angka dan nama
# tersebut dengan key adalah angka dan value adalah nama.
# Kita dapat menggunakan Dictionary Comprehension untuk mencapai hal tersebut seperti kode berikut ini:

# Syntax
# new_dict = {key_expression: value_expression for key, val in iterable}
# atau dengan menambahkan kondisional di akhir ekspresi
# new_dict = {key_expression: value_expression for key, val in iterable (if conditional)}

listku = ['alice', 'carl', 'eliot', 'geral']
dictku = {i:nama for i, nama in enumerate(listku)}
print(dictku)
# Output:
# {0: 'alice', 1: 'carl', 2: 'eliot', 3: 'geral'}
# yaitu sebuah dictionary baru dari angka dan nama.

# mengubah nilai IPK setiap mahasiswa dalam dictionary ipk_lama menjadi nilai yang lebih tinggi sebesar 0.2.
# Nilai IPK baru ditemukan dengan menambahkan 0.2 pada setiap nilai IPK lama. 
# Hasilnya akan ditempatkan dalam dictionary baru bernama ipk_baru. 
ipk_lama = {'alice':3.5, 'carl': 2.9, 'eliot':3.3}

ipk_baru = {nama:ipk+0.2 for nama, ipk in ipk_lama.items()}
print(ipk_baru)
# Output:
# {'alice': 3.7, 'carl': 3.1, 'eliot': 3.5}

lulus = {nama:ipk for nama, ipk in ipk_baru.items() if ipk >= 3.5}
print(lulus)
# Output:
# {'alice': 3.7, 'eliot': 3.5}

# Syntax
# new_dict = {key_expression: value_expression(if conditional) for key, val in iterable}
dictku = {'alice':23, 'carl':30, 'eliot':24, 'guido':60, 'steve': 70}
hasil = {key:('junior' if val < 40 else 'senior') for key, val in dictku.items()}
print(hasil)
# Output:
# {'alice': 'junior', 'carl': 'junior', 'eliot': 'junior', 'guido': 'senior', 'steve': 'senior'}

#==================================================================================

# Tuple Comprehension tidak ada di Python. 
# Jika Anda ingin membuat tuple yang mirip dengan comprehension, 
# cara terbaik adalah dengan melakukan list comprehension terlebih dahulu, 
# lalu mengubah list menjadi tuple. 
# Ini memberikan hasil yang paling cepat dibandingkan dengan menggunakan tuple comprehensions secara langsung.

listku = [1, 2, 3, 4, 5]
hasil = [x**2 for x in listku]
tupleku = tuple(hasil)
print(tupleku)
# Output:
# (1, 4, 9, 16, 25)

# (!) peringatan: tidak direkomendasikan dengan cara ini untuk tuple comprehension.
hasil = tuple(i**2 for i in listku)
print(hasil)
# Output:
# (1, 4, 9, 16, 25)

# =================================================================================

# Generator comprehension adalah bentuk singkat dari generator expression, 
# yang digunakan untuk membuat generator baru dalam satu baris kode. 
# Ini bekerja dengan cara yang sama seperti list comprehension atau dictionary comprehension, 
# dengan perbedaan bahwa hasil akhir adalah generator, bukan list atau dictionary. 
# Generator comprehension memproses satu elemen pada satu waktu, 
# sehingga lebih efisien dalam hal memori dan lebih cocok untuk menangani data besar.

# Syntax
# (expression for item in iterable (if conditional))

angka = [1, 2, 3, 4, 5]
generators = (i**2 for i in angka)
print(generators)
# Output:
# <generator object <genexpr> at 0x000001C47A281F90>

# menggunakan forloop untuk menampilkan objek generator 
for i in generators:
    print(i)
# Output:
# 1
# 4
# 9
# 16
# 25
# jika anda ingin mengetahui tentang generator expresi python kunjungi folder_name: "python-generator"