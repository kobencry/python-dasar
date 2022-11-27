# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.pop

# fungsi pop() menghapus item acak dari set.
# Metode ini mengembalikan item yang dihapus.

# Syntax
# set.pop()

# Nilai Parameter
# tidak ada nilai parameter

x = {'alice', 'carl', 'eliot'}
x.pop()
print(x)    # {'eliot', 'alice'}

# Catatan: fungsi pop() mengembalikan nilai yang dihapus.
x = {'alice', 'carl', 'eliot'}
hasil = x.pop()
print(hasil)    # carl 
print(x.pop())  # eliot

# karna menghapus secara acak mungkin anda hasilnya berbeda dengan output contoh yang diatas.
