# Generator adalah suatu objek yang bisa diterima sebagai iterable (seperti list atau tuple),
# tetapi tidak seperti list atau tuple, generator tidak menyimpan semua elemen dalam memori, 
# melainkan menghasilkan satu elemen pada satu waktu ketika diterjemahkan.
# Ini bisa membantu untuk menghemat memori dan lebih efisien dalam hal waktu ketika menangani data besar.

# Generator memiliki beberapa manfaat dan kegunaan:
# 1. Mempercepat proses penyimpanan dan pemrosesan data: 
# Generators membuat objek yang mampu diproses hanya pada saat diperlukan. 
# Ini membuat penyimpanan dan pemrosesan data lebih cepat dan efisien.

# 2. Menurunkan penggunaan memori: 
# Karena generators hanya menghasilkan satu elemen pada satu waktu, 
# mereka menggunakan lebih sedikit memori dibandingkan list comprehensions.

# 3. Generator chaining: 
# Generators bisa di-chain (digabungkan) bersama untuk memproduksi output yang lebih kompleks dan besar.

# 4. Mengurangi waktu eksekusi: 
# Karena generators menghasilkan satu elemen pada satu waktu, mereka membuat proses eksekusi lebih cepat.

# 5. Interval-by-interval processing: 
# Generators membuat data dapat diproses interval-by-interval sehingga membuat aplikasi lebih responsive dan efisien.
# Interval-by-interval processing adalah metode pemrosesan data satu-persatu dengan melibatkan interval-interval tertentu.
# Dalam hal ini, data dibagi menjadi beberapa interval yang lebih kecil, lalu setiap interval diproses satu per satu.
# Interval-by-interval processing sering digunakan untuk memproses data yang sangat besar 
# sehingga memudahkan pemrosesan dan mempercepat waktu pemrosesan. 
# Keuntungan dari interval-by-interval processing adalah konsumsi memori yang lebih rendah dan lebih mudah untuk memantau progres pemrosesan data.

# Ada beberapa jenis generator pada Python, yaitu:
# 1. Built-in function/fungsi bawaan: fungsi range(), map(), filter()
# 2. Generator Function: menggunakan keyword 'yield'
# 3. Generator Expression: atau bisa disebut 'Generator comprehension'

# Untuk menampilkan objek generator pada python terdapat beberapa jenis, antara lain:
# 1. For loop: menggunakan perulangan for untuk mengiterasi objek generator.
# 2. fungsi next(): menggunakan fungsi next() untuk mengakses elemen generator satu per satu.
# 3. konversi ke list(): menggunakan fungsi list() untuk mengubah objek generator menjadi list.
# 4. Unpacking: dengan menggunakan syntax *(unpacking) untuk mengubah generator menjadi daftar elemen.

# Built-In Functions/fungsi bawaan python:
#----------------------------------------- 
# Ada beberapa built-in function yang juga mengembalikan objek generator, seperti range(), map(), dan filter().
# Jika anda ingin mengetahui tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
# Jika anda ingin mengetahui tentang fungsi-bawaan map() kunjungi folder_name: "Fungsi-Bawaan/fungsi_map.py"
# Jika anda ingin mengetahui tentang fungsi-bawaan filter() kunjungi folder_name: "Fungsi-Bawaan/fungsi_filter.py"
# Contoh kode menggunakan fungsi range():
obj_gen_range = range(5)
print(obj_gen_range) # range(0, 5)
for i in obj_gen_range:
    print(i)
# Output:
# 0
# 1
# 2
# 3
# 4

# Anda dapat menggunakan fungsi next() untuk mengakses elemen generator satu per satu.
# obj_gen_range2 = range(5)
# print(next(obj_gen_range2))
# print(next(obj_gen_range2))

# Contoh kode menggunakan fungsi map()
obj_gen_map = map(lambda i: i**2, [1, 2, 3, 4, 5])
print(obj_gen_map)  # <map object at 0x0000020F16D23310>
for i in obj_gen_map:
    print(i)
# Output:
# 1
# 4
# 9
# 16
# 25

# Anda dapat menggunakan fungsi list() untuk mengubah objek generator menjadi list, 
# seperti contoh berikut ini:
obj_gen_map2 = list(map(lambda i: i**2, [1, 2, 3, 4, 5]))
print(obj_gen_map2)
# Output:
# [1, 4, 9, 16, 25]

obj_gen_map3 = map(lambda i: i**2, [1, 2, 3, 4, 5])
print(list(obj_gen_map3))
# Output:
# [1, 4, 9, 16, 25]

# Anda dapat menggunakan fungsi next() untuk mengakses elemen generator satu per satu.
obj_gen_map4 = map(lambda i: i**2, [1, 2, 3, 4, 5])
print(next(obj_gen_map4))   # 1
print(next(obj_gen_map4))   # 4
print(next(obj_gen_map4))   # 9
print(next(obj_gen_map4))   # 16
print(next(obj_gen_map4))   # 25
# jika anda meneruskan fungsi next() anda akan mendapatkan pesan StopIteration
# Traceback (most recent call last):
#   File ".\generators.py", line 83, in <module>
#     print(next(obj_gen_map4))
# StopIteration

# Contoh kode menggunakan fungsi filter()
obj_gen_filter = filter(lambda i: i % 2==0, [1, 2, 3, 4, 5])
print(obj_gen_filter)   # <filter object at 0x000001869E0433A0>
for i in obj_gen_filter:
    print(i)
# Output:
# 2
# 4

# Anda dapat menggunakan fungsi list() untuk mengubah objek generator menjadi list, 
# seperti contoh berikut ini:
obj_gen_filter2 = list(filter(lambda i: i % 2==0, [1, 2, 3, 4, 5]))
print(obj_gen_filter2)
# Output:
# [2, 4]

obj_gen_filter3 = filter(lambda i: i % 2==0, [1, 2, 3, 4, 5])
print(list(obj_gen_filter3))
# Output:
# [2, 4]

# Generator Functions:
#---------------------
# Fungsi generator adalah fungsi yang mengembalikan objek generator. 
# Sebuah fungsi generator dapat didefinisikan dengan menggunakan keyword "yield" dalam kode program.
# Contoh kode:
def func_gen(angka):
    for i in range(angka):
        yield i

for i in func_gen(5):
    print(i)

# Generator Expressions atau Generator Comprehension:
#----------------------------------------------------
# Ekspresi generator adalah bentuk singkat dari list comprehensions yang digunakan untuk membuat generator.

# Syntax
# gen_exp = (expression for var in iterable (if conditional))

# <expression> adalah ekspresi yang akan menentukan apa yang akan dikembalikan oleh generator comprehension.
# <var> adalah variabel yang digunakan untuk mengulangi setiap elemen dalam <iterable>.
# <iterable> adalah objek yang bisa diterima oleh generator comprehension, seperti list, tuple, string, dll.
# (if <conditional>) adalah bagian opsional dari syntax generator comprehension. Jika digunakan, 
# <conditional> adalah kondisi yang harus dipenuhi sebelum <expression> diterima. 
# Jika kondisi tidak terpenuhi, elemen tersebut tidak akan termasuk dalam generator yang dikembalikan.
# Generator comprehension berguna untuk membuat generator baru yang dapat digunakan seperti iterable lainnya, 
# dengan menggunakan syntax yang ringkas dan mudah dipahami python.

# menggunakan Generator expression:
# Contoh kode ini mirip seperti fungsi map()
obj_gen = (i**2 for i in range(1,6))
print(obj_gen)  # <generator object <genexpr> at 0x000001F64B6E1F90>

for i in obj_gen:
    print(i)
# Output:
# 1
# 4
# 9
# 16
# 25

# Anda dapat menggunakan fungsi list() untuk mengubah objek generator menjadi list, 
# seperti contoh berikut ini:.
obj_gen = (i**2 for i in range(1,6))
print(list(obj_gen))
# Output:
# [1, 4, 9, 16, 25]

# menggunakan Generator expression dengan (if conditional): 
# Contoh kode ini mirip seperti fungsi filter()
obj_gen2 = (i for i in range(1, 6) if i % 2==0)
print(obj_gen2) # <generator object <genexpr> at 0x00000218DB321F20>

for i in obj_gen2:
    print(i)
# Output:
# 2
# 4

# Anda dapat menggunakan fungsi list() untuk mengubah objek generator menjadi list, 
# seperti contoh berikut ini:
obj_gen2 = (i for i in range(1, 6)  if i % 2==0)
print(list(obj_gen2))
# Output:
# [2, 4]

# kompleksitas waktu
# python -m timeit 'listku = [i ** 2 for i in range(1_000_000)]'
# python -m timeit 'tupleku = (i ** 2 for i in range(1_000_000))'