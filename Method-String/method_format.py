# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi format() memformat nilai yang ditentukan dan memasukkannya ke dalam placeholder string.
# placeholder didefinisikan menggunakan tanda kurung kurawal: {}. 
# fungsi format() mengembalikan string yang diformat

# Syntax
# string.format(value1, value2...dst)

# Nilai Parameter
# parameter             Deskripsi
# val1, val2..dst       Dibutuhkan. Satu atau lebih nilai yang harus diformat dan dimasukkan ke dalam string.
#                       nilainya berupa list, nilai yang dipisahkan dengan koma, key=val, atau kombinasi keduanya.
#                       nilai dapat berupa tipe data apa pun.

data1 = "nama: {x} usia: {y}".format(x="alice", y=23)
data2 = "nama: {0} usia: {1}".format("carl", 23)
data3 = "nama: {} usia: {}".format("eliot", 23)

print(data1)    # nama: alice usia: 23
print(data2)    # nama: carl usia: 23
print(data3)    # nama: eliot usia: 23
# Pelajari lebih lanjut tentang formatting python di folder_name: "python-formatting"
