# -- Method Dictionary --

# fungsi pop() menghapus item yang ditentukan dari dictionary.
# Nilai item yang dihapus adalah nilai kembalian dari fungsi pop().

# Syntax
# dictionary.pop(namakey, defaultvalue)

# Nilai Parameter
# Parameter                 Deskripsi
# namakey                   Dibutuhkan. Nama keys/kunci item yang ingin Anda hapus.
# defaultvalue              Opsional. Nilai untuk dikembalikan jika nama kunci yang ditentukan tidak ada.
#                           Jika parameter ini tidak ditentukan, dan item dengan kunci yang ditentukan tidak ditemukan, 
#                           pesan kesalahan akan muncul.

# menghapus "alamat" dari dictionary
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarata'}
dictku.pop('alamat')
print(dictku)   # {'nama': 'alice', 'usia': 23}

# mengembalikan nilai yang dihapus
dictku = {'nama':'carl', 'usia':26, 'alamat':'bandung'}
hasil = dictku.pop('alamat')
print(hasil)    # bandung

# jika nama kunci tidak ada, akan menampilkan pesan kesalahan KeyError
dictku = {'nama':'eliot', 'usia':22, 'alamat':'surabaya'}
dictku.pop('jurusan')
print(dictku)
# Traceback (most recent call last):
#   File "method_pop.py", line 28, in <module>
#     dictku.pop('jurusan')
# KeyError: 'jurusan'
