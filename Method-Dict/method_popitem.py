# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.popitem

# fungsi popitem() menghapus item yang terakhir dimasukkan ke dalam dictionary.
# Item yang dihapus adalah nilai kembalian dari fungsi popitem(), sebagai tupel.

# Syntax
# dictionary.popitem()

# Nilai Parameter
# tidak ada nilai parameter

dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
dictku.popitem()
print(dictku)   # {'nama': 'alice', 'usia': 23}

# mengembalikan item yang dihapus sebagai tuple
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
hasil = dictku.popitem()
print(hasil)    # ('alamat', 'jakarta')
