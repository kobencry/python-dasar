# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.setdefault

# fungsi setdefault() mengembalikan nilai item dengan kunci yang ditentukan.
# Jika keys/kunci tidak ada, masukkan keys/kunci, dengan nilai yang ditentukan.

# Syntax
# dictionary.setdefault(namakey, value)

# Nilai Parameter
# Parameter                     Deskripsi
# namakey                       Dibutuhkan. Namakey item yang ingin Anda kembalikan nilainya.
# value                         Opsional. Jika kuncinya ada, parameter ini tidak berpengaruh.
#                               Jika nama keys/kunci tidak ada, Nilai default None/Tidak ada

# mendapatkan nilai "alamat"
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
hasil = dictku.setdefault('alamat')
print(hasil)    # jakarta

# catatan: fungsi setdefault() jika nama value/kunci tidak ada maka objek dictionary akan ditambahkan dan diperbarui.

# jika nama keys/kunci tidak ada value/nilai defaultnya None
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
dictku.setdefault('jurusan')
print(dictku)   # {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta', 'jurusan': None}

# menggunakan value/nilai sendiri
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
dictku.setdefault('jurusan', 'teknik komputer')
print(dictku)   # {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta', 'jurusan': 'teknik komputer'}
