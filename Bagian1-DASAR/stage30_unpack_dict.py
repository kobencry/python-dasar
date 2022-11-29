# unpacking/membongkar Dictionary 
# Saat membuat dict, kami biasanya memberikan keys/kunci dan value/nilai padanya, ini disebut "packing/mengemas" dictionary.
packing_dict = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
# unpack dict
x, y, z = packing_dict
# akan mengembalikan/menampilkan nama keys/kunci dict
print(x, y, z)  # nama usia alamat
# mengembalikan key dan value
print(packing_dict[x])  # alice
print(packing_dict[y])  # 23
print(packing_dict[z])  # jakarta

# Catatan: Jumlah variabel harus sesuai dengan jumlah item dalam dictionary,
# jika tidak, Anda harus menggunakan tanda bintang (*) untuk mengumpulkan
# nilai yang tersisa sebagai tipe data list.

# unpcaking menggunakan tanda bintang *
packing_dict = {'nama':'carl', 'usia':23, 'alamat':'jakarta', 'email':'carl@gmail.com', 'jurusan':'teknik komputer'}
x, y, *z = packing_dict
print(x, y, z)  # nama usia ['alamat', 'email', 'jurusan']

# Jika tanda bintang ditambahkan ke nama variabel lain selain yang terakhir,
# Python akan memberikan nilai ke variabel sampai jumlah nilai yang tersisa 
# sesuai dengan jumlah variabel yang tersisa.

x, *y, z = packing_dict
print(x, y, z)  # nama ['usia', 'alamat', 'email'] jurusan

*x, y, z = packing_dict
print(x, y, z)  # ['nama', 'usia', 'alamat'] email jurusan

# unpacking menggunakan tanda bintang dua kali **
dict1 = {'nama':'carl', 'usia':23, 'alamat':'jakarta'}
dict2 = {'email':'carl@gmail.com', 'jurusan':'teknik komputer'}
x = {**dict1, **dict2}
print(x)    # {'nama': 'carl', 'usia': 23, 'alamat': 'jakarta', 'email': 'carl@gmail.com', 'jurusan': 'teknik komputer'}
