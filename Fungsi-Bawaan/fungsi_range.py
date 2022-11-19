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
for i in range(5):
    print(i)
# 0
# 1
# 2
# 3
# 4

# contoh menggunakan parameter start, stop
for i in range(1, 5):
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
