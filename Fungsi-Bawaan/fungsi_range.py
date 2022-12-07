# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html?#func-range
# https://docs.python.org/3/library/stdtypes.html?#range

# fungsi range() mengembalikan urutan angka, mulai dari 0 secara default, dan bertambah 1 (secara default), dan berhenti sebelum angka yang ditentukan. 

# Syntax
# range(start, stop, step)

# Nilai Parameter
# Parameter                 Deskripsi
# start                     Opsional. Angka bilangan bulat yang menentukan di mana posisi untuk memulai. Standarnya/default adalah 0
# stop                      Dibutuhkan. Angka bilangan bulat yang menentukan posisi berhenti (tidak disertakan).
# step                      Opsional. Angka bilangan bulat yang menentukan penambahan. Standarnya/default adalah 1

# contoh menggunakan parameter start
for i in range(5):  # mencetak dari 0 - 4
    print(i)
# 0
# 1
# 2
# 3
# 4

# contoh menggunakan parameter start, stop
for i in range(1, 5):   # mencetak dari 1 - 4
    print(i)
# 1
# 2
# 3
# 4

# contoh menggunakan parameter start, stop, step
for i in range(1, 5, 2):
    print(i)
# 1
# 3

# kita bisa memulainya dari angka yang terbersar
# jika ingin hasilnya dari 0 gunakan for i in range(5, -1, -1)
for i in range(5, 0, -1):
    print(i)
# 5
# 4
# 3
# 2
# 1

# contoh menggunakan tipe data string
s = "hello world"
for i in range(len(s)):
    print(i)
# 0
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# unpacking dari nilai dari hasil range()
x, y, z = range(3)
print(x)    # 0
print(y)    # 1
print(z)    # 2

# Catatan: Jumlah variabel harus sesuai dengan jumlah nilai dalam range(),
# jika tidak, Anda harus menggunakan tanda bintang (*) untuk mengumpulkan
# nilai yang tersisa sebagai list.

*x, = range(5)
print(x)    # [0, 1, 2, 3, 4]

x, *y, z = range(5)
print(x)    # 0
print(y)    # [1, 2, 3]
print(z)    # 4
