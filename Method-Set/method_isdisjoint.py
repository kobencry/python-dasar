# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.isdisjoint

# fungsi isdisjoint() mengembalikan nilai boolean True jika di kedua set tidak memiliki item yang sama,
# jika tidak maka mengembalikan nilai boolean False.

# Syntax
# set.isdisjoint(set)

# Nilai Parameter
# Parameter                 Deskripsi
# set                       Dibutuhkan. Set untuk mencari item yang sama

# mengembalikan True jika tidak ada item dalam set x yang ada di set y
x = {'alice', 'carl', 'eliot'}
y = {'a', 'b', 'c'}
hasil = x.isdisjoint(y)
print(hasil)    # True

x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'carl'}
hasil = x.isdisjoint(y)
print(hasil)    # False

x = {1, 2, 3, 4}
y = {5, 6, 7, 8}
hasil = x.isdisjoint(y)
print(hasil)    # True
