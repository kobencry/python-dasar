# -- Method Tuple --

# fungsi index() menemukan kejadian pertama dari nilai yang ditentukan.
# jika nilainya tidak ditemukan, akan menampilkan error runtime ValueError.

# Syntax
# tuple.index(nilai)

# Nilai Parameter
# Parameter                 Deskripsi
# nilai                     Dibutuhkan. Item yang akan dicari

tupleku = (10, 8, 20, 30, 8)
print(tupleku.index(8)) # 1

tupleku = ('hello', 'alice', 'world', 'alice')
print(tupleku.index('alice'))   # 1

# nilai tidak ditemukan Error runtime ValueError
#x = (False, False, True, 'hello')
#print(x.index('world'))
