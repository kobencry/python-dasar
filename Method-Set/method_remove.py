# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.remove

# fungsi remove() menghapus elemen yang ditentukan dari set.
# fungsi ini berbeda dengan fungsi discard(), karena remove() akan 
# memunculkan error jika item yang ditentukan tidak ada, dan discard() tidak.

# Syntax
# set.remove(item)

# Nilai Parameter
# Parameter                     Deskripsi
# item                          Dibutuhkan. Item yang akan dicari, dan dihapus

x = {'alice', 'carl', 'eliot'}
x.remove('carl')
print(x)    # {'alice', 'eliot'}

y = {10, 20, 30}
print(y.remove(30))

# memunculkan error KeyError
x = {'alice', 'carl', 'eliot'}
x.remove('hello')
print(x)
# Traceback (most recent call last):
#   File "method_remove.py", line 25, in <module>
#     x.remove('hello')
# KeyError: 'hello'
