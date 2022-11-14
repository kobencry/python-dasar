# -- Method List --

# https://docs.python.org/3/tutorial/datastructures.html?highlight=extend#list.extend

# fungsi extend() menambahkan elemen list yang ditentukan (atau dapat diubah apa pun) ke akhir list.

# Syntax
# list.extend(iterabel)

# Nilai Parameter
# Parameter                 Deskripsi
# iterabel                  Dibutuhkan. Setiap iterable (list, set, Tuple, dll.)

listku = ['hello']
print(listku)   # sebelum ['hello']
x = ['world', False, 2.5, ]
listku.extend(x)
print(listku)   # sesudah ['hello', 'world', False, 2.5]

# menggunakan iterable tuple
listku.extend((True, 3.5, 'tuple'))
print(listku)   # ['hello', 'world', False, 2.5, True, 3.5, 'tuple']

# menggunakan iterable set
listku.extend({None, 4.5, 'set'})
print(listku)   # ['hello', 'world', False, 2.5, True, 3.5, 'tuple', 4.5, 'set', None]

# menggunakan iterable dict
listku.extend({'nama':'alice', 'usia':23})
print(listku)   # ['hello', 'world', False, 2.5, True, 3.5, 'tuple', 4.5, 'set', None, 'nama', 'usia']
# jika ingin menghasilkan value gunakan fungsi values() di method dict
listku.extend({'nama':'alice', 'usia':23}.values())
print(listku)   # 'hello', 'world', False, 2.5, True, 3.5, 'tuple', 'set', 4.5, None, 'nama', 'usia', 'alice', 23]

# menggunakan iterable berjumlah 1 elemen
listku = ['hello']
listku.extend(['world'])
print(listku)   # ['hello', 'world']
