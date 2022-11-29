# memodifikasi dictionary python
# dict dapat diubah, artinya kita dapat mengubah, menambah atau menghapus item setelah kamus dibuat.

# mengubah item dict dengan nama keys/kunci
dictku = {'nama':'alice', 'usia':23}
dictku['nama'] = 'carl'
print(dictku)   # {'nama': 'carl', 'usia': 23}

# mengubah item dict dengan "Method-Dict" update()
dictku.update({'usia':29})
print(dictku)   # {'nama': 'carl', 'usia': 29}

# menambahkan item dict dengan nama keys/kunci, 
# jika item dict tidak ada maka akan ditambahkan
dictku = {'nama':'alice', 'usia':25}
dictku['alamat'] = 'jakarta'
print(dictku)   # {'nama': 'alice', 'usia': 25, 'alamat': 'jakarta'}
dictku['email'] = 'alice@gmail.com'
dictku['noid'] = 12345
print(dictku)   # {'nama': 'alice', 'usia': 25, 'alamat': 'jakarta', 'email': 'alice@gmail.com', 'noid': 12345}

# menambahkan item dict dengan "Method-Dict" update(), 
# jika item dict tidak ada maka akan ditambahkan
dictku = {'nama': 'carl', 'usia':25}
dictku.update({'alamat':'bandung'})
# menggunakan konstruktor dict()
dictku.update(dict(email='carl@gmail.com'))
print(dictku)   # {'nama': 'carl', 'usia': 25, 'alamat': 'bandung', 'email': 'carl@gmail.com'}

# menambahkan atau menggabungkan item dengan operator **
data_nama = {'nama':'alcie'}
data_usia = {'usia':23}
x = {**data_nama, **data_usia}
print(x)    # {'nama': 'alcie', 'usia': 23}

# menghapus item dict dengan "Method-Dict" pop()
dictku = {'nama':'alice', 'usia':23}
dictku.pop('usia')
print(dictku)   # {'nama': 'alice'}

# menghapus item dict menggunakan keyword "del" dengan nama key/kunci
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarta', 'email':'alice@gmail.com'}
del dictku['alamat']
print(dictku)   # {'nama': 'alice', 'usia': 23, 'email': 'alice@gmail.com'}

# menghapus semua/seluruh item dict dangan "Method-Dict" clear()
dictku = {'nama':'alice', 'usia':23}
dictku.clear()
print(dictku)   # {}

# anda juga bisa menghapus semua/seluruh item dict dengan keyword "del"
# Peringatan: akan memunculkan pesan error NameError
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarta', 'email':'alice@gmail.com'}
del dictku
print(dictku)
# Traceback (most recent call last):
#   File "stage29_modify_dict.py", line 48, in <module>
#     print(dictku)
# NameError: name 'dictku' is not defined

# jenis-jenis keyword python kunjungi file_name: "stage01_helloworld.py"
# jika anda ingin mengetahui tentang jenis-jenis Method-Dict kunjungi folder_name: "Method-Dict"
