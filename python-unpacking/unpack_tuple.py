# unpacking/membongkar Tuple
# Saat membuat tuple, kami biasanya memberikan nilai padanya, ini disebut "packing/mengemas" tuple.
packing_tuple = ('alice', 'carl', 'eliot')
# unpacking tuple
x, y, z = packing_tuple
print(x)    # alice
print(y)    # carl
print(z)    # eliot

# Catatan: Jumlah variabel harus sesuai dengan jumlah nilai dalam tuple,
# jika tidak, Anda harus menggunakan tanda bintang (*) untuk mengumpulkan
# nilai yang tersisa sebagai list.

# unpacking menggunakan tanda bintang *
packing_tuple = ('alice', 'carl', 'eliot', 'geral')
x, y, *z = packing_tuple
print(x)    # alice
print(y)    # carl
print(z)    # ['eliot', 'geral']

# Jika tanda bintang ditambahkan ke nama variabel lain selain yang terakhir,
# Python akan memberikan nilai ke variabel sampai jumlah nilai yang tersisa 
# sesuai dengan jumlah variabel yang tersisa.

packing_tuple = ('alice', 'carl', 'eliot', 'geral')
x, *y, z = packing_tuple
print(x)    # alice
print(y)    # ['carl', 'eliot']
print(z)    # geral

packing_tuple = ('alice', 'carl', 'eliot', 'geral')
*x, y, z = packing_tuple
print(x)    # ['alice', 'carl']
print(y)    # eliot
print(z)    # geral

# untuk membuat objek tuple, kita tidak perlu menggunakan sepasang tanda kurung () sebagai pembatas.
# ini juga berfungsi untuk membongkar tuple, jadi sintaks berikut ini setara dengan tuple
x, y, z = 'alice', 23, 'jakarta'
print(x)    # alice
print(y)    # 23
print(z)    # jakarta

# mengembalikan tuple dalam fungsi
# fungsi Python dapat mengembalikan beberapa nilai yang dipisahkan dengan koma.
# karena kita dapat mendefinisikan objek tupel tanpa menggunakan tanda kurung,
# operasi semacam ini dapat diartikan sebagai mengembalikan nilai tupel.
# Jika kita membuat kode fungsi yang mengembalikan banyak nilai, 
# maka kita dapat melakukan operasi pengepakan dan pembongkaran yang dapat 
# diulang dengan nilai yang dikembalikan.

def fungsi(angka):
    return angka, angka ** 2, angka ** 3
print(fungsi(2))    # (2, 4, 8)

x, y, z = fungsi(2)
print(x)    # 2
print(y)    # 4
print(z)    # 8
