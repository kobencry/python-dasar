# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.clear

# fungsi clear() menghapus semua elemen dari dictionary.

# Syntax
# dictionary.clear()

# Nilai Parameter
# tidak ada nilai parameter

# menghapus semua dictionary data mahasiswa
mahasiswa = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
print(mahasiswa)    # {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta'}
mahasiswa.clear()
print(mahasiswa)    # {}
