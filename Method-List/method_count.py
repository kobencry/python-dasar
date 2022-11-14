# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=count#list.count

# fungsi count() mengembalikan jumlah elemen dengan nilai yang ditentukan.

# Syntax
# list.count(value)

# Nilai Parameter
# Parameter                 Deskripsi
# value                     Dibutuhkan. Jenis apa pun (string, angka, list, tupel, dll.). Nilai yang akan dicari.

# mencari nilai False
listku = ['hello', False, 2.5, False, True, 'world', False]
x = listku.count(False)
print(x)    # 3

# mencari nilai 6.5
listku = ['p', 'x', [6.5, 'y'], 6.5, ['x', 6.5]]
x = listku.count(6.5)
print(x)    # 1

# catatan: fungsi count() tidak mencari elemen list secara mendalam

# mencari nilai x
listku = [False, 'x', ['x', 'x'], True, 'x', ['x', ['x', 'x']]]
print(listku.count('x'))    # 2
