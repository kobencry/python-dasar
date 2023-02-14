# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html#tuple

# fungsi tuple() membuat objek tuple.
# Objek tuple adalah koleksi yang tidak dapat diubah atau dihapus.

# Syntax
# tuple(iterable)

# Nilai Parameter
# Parameter                 Deskripsi
# iterable                  Opsional. Urutan, koleksi, atau objek iterator

# membuat tuple dengan konstruktor tuple()
listku = ['alice', 'carl', 'eliot']
tupleku = tuple(listku)
print(tupleku)
# Output:
# ('alice', 'carl', 'eliot')

# membuat tuple dengan bracket () "bulat" atau "parentheses" dan simbol koma ","
x = ('alice', 'carl', 'eliot')
y = ('python', )
z = 'hello', 'world'
print(x)    # ('alice', 'carl', 'eliot')
print(y)    # ('python',)
print(z)    # ('hello', 'world')

# jika ingin mempelajari lebih lanjut tentang koleksi-tuple  kunjungi folder_name: "Method-Tuple"