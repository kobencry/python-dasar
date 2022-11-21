# memodifikasi list python
# python memiliki seperangkat method/method/fungsi bawaan yang dapat digunakan pada list.

# ubah nilai item list
listku = ['alice', 'carl', 'eliot', 'geral']
print(listku)   # sebelum ['alice', 'carl', 'eliot', 'geral']
listku[1] = 'bert'
print(listku)   # sesudah ['alice', 'bert', 'eliot', 'geral']

# ubah rentang nilai item list
# untuk mengubah nilai item dalam rentang tertentu, tentukan list dengan nilai
# baru, dan rujuk ke rentang nomor indeks ketempat anda ingin menyisipkan nilai baru
listku = ['alice', 'carl', 'eliot', 'geral']
print(listku)   # sebelum ['alice', 'carl', 'eliot', 'geral'] 
listku[1:2] = ['bert']
print(listku)   # sesudah ['alice', 'bert', 'eliot', 'geral']

listku = ['alice', 'carl', 'eliot', 'geral']
print(listku)   # sebelum ['alice', 'carl', 'eliot', 'geral']
listku[1:3] = ['bert', 'corie']
print(listku)   # sesudah ['alice', 'bert', 'corie', 'geral']

# Jika anda memasukkan lebih banyak item list daripada yang anda ganti,
# item baru akan dimasukkan di tempat yang anda tentukan,
# dan item yang tersisa akan bergerak menyesuaikan
listku = ['alice', 'carl', 'eliot']
print(listku)   # sebelum ['alice', 'carl', 'eliot']
listku[1:2] = ['bert', 'corie', 'dely']
print(listku)   # sesudah ['alice', 'bert', 'corie', 'dely', 'eliot']

# Catatan: Panjang list akan berubah bila jumlah item list yang dimasukkan tidak sesuai dengan jumlah item list yang diganti.
 
listku = ['hello', 'world']
print(listku)   # sebelum ['hello', 'world']
listku[1:3] = ['alice', 'carl', 'eliot', 'geral']
print(listku)   # sesudah ['hello', 'alice', 'carl', 'eliot', 'geral']

# mengubah item list kedua dan ketiga dengan menggunakan satu nilai item list
listku = ['hello', 'alice', 'carl']
print(listku)   # sebelum ['hello', 'alice', 'carl']
listku[1:3] = ['world']
print(listku)   # sesudah ['hello', 'world']

# tambahkan item list menggunakan Method-List insert()
# fungsi insert() menyisipkan item list pada indeks yang ditentukan.
listku = ['hello', 'world']
print(listku)   # sebelum ['hello', 'world']
listku.insert(1, 'alice')
print(listku)   # sesudah ['hello', 'alice', 'world']

# tambahkan item list menggunakan operator (+)
x = ['hello']
y = ['world']
z = x + y
print(z)    # ['hello', 'world']

# list comprehension
listku = ['alice', False, 'carl', 2.5, 'eliot', 0xff, 'geral', None]
list_nama = [i for i in listku if type(i) == type(str())]
print(list_nama)    # ['alice', 'carl', 'eliot', 'geral']

# jika ingin mempelajari lebih lanjut tentang Method-List insert() kunjungi folder_name: "Method-List/method_insert.py"
# jika ingin mempelajari lebih lanjut tentang jenis2 Method-List python kunjungi folder_name: "Method-List"
# jika ingin mempelajari lebih lanjut tentang comprehension kunjungi folder_name: "python-comprehension"
