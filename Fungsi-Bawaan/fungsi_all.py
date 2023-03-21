# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-all#all

# fungsi all() mengembalikan nilai boolean True jika semua item dalam iterable, 
# bernilai boolean True, jika tidak maka akan mengembalikan nilai boolean False.
# Jika objek yang dapat diubah kosong, fungsi all() juga mengembalikan True.

# Syntax
# all(iterable)

# Nilai Parameter
# Parameter                 Deskripsi
# iterable                  Objek yang dapat diubah (list, tuple, dict)

list_x = [1, 2, 3]
x = all(list_x)
print(x)    
# Output:
# True

list_y = [0, 1, 5]
y = all(list_y)
print(y)    
# Output:
# False

tuple_x = ("hello", "world")
tuple_y = (0.5, 1.5, 2)
x = all(tuple_x)
y = all(tuple_y)
print(x)    # True
print(y)    # True

tuple_x = ("")
tuple_y = (0.0, 0.1)
tuple_z = ("", "hello", "world")
print(all(tuple_x))     # True
print(all(tuple_y))     # False
print(all(tuple_z))     # False

# Catatan: Saat menggunakan dict pada, fungsi all() memeriksa key=kunci apakah semua Benar/True, bukan value=nilainya.

dict_x = {1:'hello', 2:'world'}
dict_y = {0:'hello', 1:'world'}
print(all(dict_x)) # True
print(all(dict_y)) # False

# Ingat: Jika objek yang dapat diubah kosong, fungsi all() juga mengembalikan True.

print(all([]))  # True
print(all({}))  # True
print(all(()))  # True
