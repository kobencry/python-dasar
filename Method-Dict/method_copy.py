# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.copy

# Syntax
# dictionary.copy()

# Nilai Parameter
# tidak ada nilai parameter

# menyalin dictionary data mahasiswa
mahasiswa = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
data_copy = mahasiswa.copy()
print(mahasiswa)    # {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta'}
print(data_copy)    # {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta'}

print(mahasiswa == data_copy)   # True
