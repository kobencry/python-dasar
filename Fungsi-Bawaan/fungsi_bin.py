# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-bin#bin

# fungsi bin() mengembalikan versi biner dari bilangan bulat yang ditentukan.
# Hasilnya akan selalu dimulai dengan awalan 0b.

# Syntax
# bin(n)

# Nilai Parameter
# Parameter                 Deskripsi
# n                         Dibutuhkan. Sebuah bilangan bulat

x = 10
print(bin(x))   # 0b1010

# int
print(bin(255)) # 0b11111111
print(bin(192)) # 0b11000000
print(bin(168)) # 0b10101000
print(bin(43))  # 0b101011

# hexa
print(bin(0xff)) # 0b11111111
print(bin(0xc0)) # 0b11000000
print(bin(0xA8)) # 0b10101000
