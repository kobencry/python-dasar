# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-bool#bool

# fungsi bool() mengembalikan nilai boolean True, False dari objek tertentu

# Syntax
# bool(objek)

# Nilai Parameter
# Parameter             Deskripsi
# objek                 Objek apa pun, seperti String, List, Angka, dll.

# tipe data koleksi
list_kosong = []
tupl_kosong = ()
sets_kosong = {}
print(bool(list_kosong))    # False
print(bool(tupl_kosong))    # False
print(bool(sets_kosong))    # False

# string
print(bool("hello world"))  # True
print(bool("")) # False

# int
print(bool(1))  # True
print(bool(0))  # False

print(bool(0.1))    # True
print(bool(0.0))    # False

# hexa
print(bool(0xff))   # True
print(bool(0x00))   # False

# biner
print(bool(0b1))    # True
print(bool(0b0))    # False

# false true none
print(bool(True))   # True
print(bool(False))  # False
print(bool(None))   # False
