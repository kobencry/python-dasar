# python tuple

# Tuple adalah salah satu dari 4 tipe data bawaan di Python yang digunakan untuk menyimpan kumpulan data,
# 3 lainnya adalah List , Set , dan Dictionary , semuanya dengan kualitas dan penggunaan yang berbeda.

# Tuple adalah koleksi yang dipesan dan tidak dapat diubah, artinya Anda
# tidak dapat mengubah, menambah, atau menghapus item setelah tupel dibuat.
# Tuple digunakan untuk menyimpan banyak item dalam satu variabel.
# Tuple ditulis dengan tanda kurung bulat. 

# Dari perspektif Python, tuple didefinisikan sebagai objek dengan tipe data 'tuple'.
print(type(('hello', 'world')))     # <class 'tuple'>

# membuat tuple
x = ('alice', 'carl', 'eliot', 'geral')
print(x)    # ('alice', 'carl', 'eliot', 'geral')

# membuat tuple dengan item duplikat
x = ('alice', 'carl', 'alice', 'carl')
print(x)    # ('alice', 'carl', 'alice', 'carl')

# membuat tuple dengan tipe data apapun
x = ('alice', 'carl', 'eliot')
y = (1, 2.5, 0xff, 0b11111111)
z = (True, False, None)
print(x)    # ('alice', 'carl', 'eliot')
print(y)    # (1, 2.5, 255, 255)
print(z)    # (True, False, None)

# membuat satu item tuple
x = ('hello', )
y = ('world')
print(type(x), x)   # <class 'tuple'> ('hello',)
print(type(y), y)   # <class 'str'> world

# menggunakan konstruktor tuple() saat membuat tuple
tupleku = tuple(('alice', 2.5, True, 0xff, 0b11))
print(tupleku)  # ('alice', 2.5, True, 255, 3)

# copy item tuple menggunakan konstruktor tuple()
x = ('alice', 'carl', 'eliot')
copy_x = tuple(x)
print(copy_x)       # ('alic', 'carl', 'eliot')
print(x is copy_x)  # True

# akses item tuple
# mengakses item tuple dengan mengacu pada nomor indeks, di dalam tanda kurung siku.
tupleku = ('alice', 'carl', 'eliot', 'geral')
print(tupleku[0])   # alice
print(tupleku[1])   # carl
print(tupleku[1:3]) # ('carl', 'eliot')
# menggunakan indeks negatif
print(tupleku[-1])  # geral
print(tupleku[-3])  # carl

# mengubah item tuple
# Ingat: Tuple tidak dapat diubah, artinya Anda tidak dapat mengubah,
#        menambah, atau menghapus item setelah tupel dibuat.
# "Tetapi ada beberapa solusi"

tupleku = ('hello', 'world')
print(tupleku)  # ('hello', 'world')
# ubah tuple menjadi list untuk mengubahnya
listku = list(tupleku)
listku[0] = 'war'
tupleku = tuple(listku)
print(tupleku)  # ('war', 'world')

# menambahkan item tuple
tupleku = ('alice', 'carl')
tupleku += ('eliot',)
print(tupleku)  # ('alice', 'carl', 'eliot')

# unpacking/membongkar tuple
packing_tuple = ('alice', 'carl', 'eliot')
# unpacking tuple
x, y, z = packing_tuple
print(x)    # alice
print(y)    # carl
print(z)    # eliot

# urutkan tuple secara alfanumerik (0-9A-Za-z)
# menggunakan "Fungsi-Bawaan" dengan fungsi sorted() mengembalikan daftar terurut dari objek iterable yang ditentukan.
tupleku = ('eliot', '25', 'carl', 'Alice', '1')
x = sorted(tupleku)
print(tuple(x))   # ('1', '25', 'Alice', 'carl', 'eliot')

# urutkan terbalik 
# menggunakan "Fungsi-Bawaan" dengan fungsi reversed() mengemablikan objek iterator terbalik
tupleku = ('alice', 'carl', 'eliot')
objek_iterator = reversed(tupleku)
tupleku = tuple(objek_iterator)
print(tupleku)  # ('eliot', 'carl', 'alice')

# gabungkan item tuple
tuple1 = ('alice', 'carl', 'eliot')
tuple2 = (1, 2.5, False, None)
hasil = tuple1 + tuple2
print(hasil)    # ('alice', 'carl', 'eliot', 1, 2.5, False, None)

# looping tuple
for i in ('hello', 25, False):
    print(i)
# hello
# 25
# False

# menghitung jumlah item tuple
tupleku = ('hello', 25, False, 'world', None)
print(len(tupleku)) # 5

# periksa apakah 'carl' ada didalam tuple
tupleku = ('alice', 'carl', 'eliot')
if 'carl' in tupleku:
    print("passed")

# jika anda ingin mengetahui tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
# jika anda ingin mengetahui tentang fungsi-bawaan sorted() kunjungi folder_name: "Fungsi-Bawaan/fungsi_sorted.py"
# jika anda ingin mengetahui tentang fungsi-bawaan reversed() kunjungi folder_name: "Fungsi-Bawaan/fungsi_reversed.py"
# jika anda ingin mengetahui tentang fungsi-bawaan konstruktor tuple() kunjungi folder_name: "Fungsi-Bawaan/fungsi_tuple.py"
