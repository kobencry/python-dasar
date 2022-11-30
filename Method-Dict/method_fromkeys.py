# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.fromkeys

# fungsi fromkeys() mengembalikan dictionary dengan keys/kunci yang ditentukan dan value/nilai yang ditentukan.

# Syntax
# dict.fromkeys(keys, value)

# Nilai Parameter
# Parameter                 Deskripsi
# keys                      Dibutuhkan. Iterable yang menentukan keys/kunci dictionary baru
# value                     Opsional. Nilai untuk semua keys/kunci. Nilai defaultnya adalah None/Tidak Ada.

# menggunakan parameter keys
key = ('nama', 'usia', 'alamat')
dictku = dict.fromkeys(key)
print(dictku)   # {'nama': None, 'usia': None, 'alamat': None}

# menggunakan parameter keys dan value
key = ('nama', 'usia', 'alamat')
val = 'xxxxx'
dictku = dict.fromkeys(key, val)
print(dictku)   # {'nama': 'xxxxx', 'usia': 'xxxxx', 'alamat': 'xxxxx'}

key = "python" 
val = [i for i in range(1,3)]
dictku = dict.fromkeys(key, val)
print(dictku)   # {'p': [1, 2], 'y': [1, 2], 't': [1, 2], 'h': [1, 2], 'o': [1, 2], 'n': [1, 2]}
