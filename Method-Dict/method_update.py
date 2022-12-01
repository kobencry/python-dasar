# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.update

# fungsi update() memasukan item yang ditentukan ke kamus.
# Item yang ditentukan dapat berupa dict, atau objek yang dapat diubah dengan pasangan kunci dan nilai.

# Syntax
# dictionary.update(iterable)

# Nilai Parameter
# Parameter                 Deskripsi
# iterable                  Dictionary atau objek yang dapat diubah dengan pasangan kunci dan nilai, yang akan dimasukkan ke dictionary.

# memasukan item ke dictionary
dictku = {'nama':'alice', 'usia':23}
dictku.update({'alamat':'jakarta'})
print(dictku)   # {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta'}

x = {'jurusan':'teknik komputer', 'email':'alice@gmail.com'}
dictku.update(x)
print(dictku)   # {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta', 'jurusan': 'teknik komputer', 'email': 'alice@gmail.com'}

# mengubah item "nama"
dictku.update({'nama':'carl'})
print(dictku)   # {'nama': 'carl', 'usia': 23, 'alamat': 'jakarta', 'jurusan': 'teknik komputer', 'email': 'alice@gmail.com'}
