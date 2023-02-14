# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html#dict

# fungsi dict() membuat dictionary/kamus.
# Objek dictionary adalah koleksi yang tidak terurut, dapat diubah, dan diindeks.

# Syntax
# dict(keyword=argumen)

# Nilai Parameter
# Parameter                 Deskripsi
# keyword=argumen           Opsional. Sebanyak argumen kata kunci yang Anda suka, 
#                           dipisahkan dengan koma: key=value, key = value 
#                           atau menggunakan list dan tuple: [(key=value), (key=value)]

# membuat dictionary dengan konstruktor dict()
dictku = dict(nama='alice', usia=23, alamat='jakarta')
print(dictku)
# Output:
# {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta'}

dictku = dict([('nama', 'carl'), ('usia', 20), ('alamat', 'bandung')])
print(dictku)
# Output:
# {'nama': 'carl', 'usia': 20, 'alamat': 'bandung'} 

# membuat dictionary dengan bracket {} kurawal
dictku = {'nama':'eliot', 'usia':25, 'alamat':'surabaya'}
print(dictku)
# Output:
# {'nama': 'eliot', 'usia': 25, 'alamat': 'surabaya'}

# menggunakan dict comprehension
dictku = dict((key, val) for key, val in enumerate(['alice', 'carl', 'eliot'], start=1))
print(dictku)
# Output:
# {1: 'alice', 2: 'carl', 3: 'eliot'}

# jika ingin mempelajari lebih lanjut tentang koleksi-dictionary  kunjungi folder_name: "Method-Dict"
# jika ingin mempelajari lebih lanjut tentang comprehension  kunjungi folder_name: "python-comprehension"