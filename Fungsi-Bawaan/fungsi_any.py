# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-any#any

# fungsi any() mengembalikan nilai boolean True jika ada item dalam iterable yang True/benar,
# jika tidak maka akan mengembalikan nilai boolean False.

# Jika objek iterable kosong, fungsi any() akan mengembalikan False.

# Syntax
# any(iterable)

# Nilai Parameter
# Parameter             Deskripsi
# iterable              Objek yang dapat diubah (list, tupel, dict)

list_x = [1, 2, 3]
list_y = [0, 2, 3]
x = any(list_x)
y = any(list_y)
print(x)    # True
print(y)    # True
print(any([0, False, None]))    # False

tuple_x = ("hello", "world")
tuple_y = (0.0, 0.5, 1)
x = any(tuple_x)
y = any(tuple_y)
print(x)    # True
print(y)    # True

tuple_x = ("")
tuple_y = (0.0, False, 0x00)
tuple_z = ("", "hello", 1)
print(any(tuple_x))     # False
print(any(tuple_y))     # False
print(any(tuple_z))     # True

# Catatan: Saat digunakan pada dict, fungsi any() memeriksa apakah ada key=kunci yang True/benar, bukan pada valuesnilainya.
dict_x = {"nama":"alice", "usia":23}
dict_y = {0x00:0, 0xff:255}
print(any(dict_x))  # True
print(any(dict_y))  # True

dict_x = {0:"hello", False:"world", 0x00:"x"}
print(any(dict_x))  # False

# Ingat: Jika objek iterable kosong, fungsi any() akan mengembalikan False.
print(any([]))  # False
print(any(()))  # False
print(any({}))  # False
