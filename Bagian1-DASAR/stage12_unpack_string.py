# unpacking/membongkar String
# Saat membuat string, kami biasanya memberikan nilai padanya, ini disebut "packing/mengemas" string.
packing_string = "hai"
# unpacking string
x, y, z = packing_string
print(x)    # h
print(y)    # a
print(z)    # i

# Catatan: Jumlah variabel harus sesuai dengan jumlah nilai dalam string,
# jika tidak, Anda harus menggunakan tanda bintang (*) untuk mengumpulkan
# nilai yang tersisa sebagai list.

# unpacking menggunakan tanda bintang *
packing_string = "hello world"
x, y, *z = packing_string
print(x)    # h
print(y)    # e
print(z)    # ['l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# Jika tanda bintang ditambahkan ke nama variabel lain selain yang terakhir,
# Python akan memberikan nilai ke variabel sampai jumlah nilai yang tersisa 
# sesuai dengan jumlah variabel yang tersisa.

packing_string = "hello world"
x, *y, z = packing_string
print(x)    # h
print(y)    # ['e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l']
print(z)    # d

packing_string = "alice"
x, *y, z = packing_string
# print(type(y))  # <class 'list'>
print("".join(y) + z + x)   # licea

# jika ingin mempelajari lebih lanjut tentang method/metode/fungsi-string folder_name: "Method-String"
# jika ingin mempelajari lebih lanjut tentang Method-String join() kunjung folder_name: "Method-String/method_join.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan type() kunjung folder_name: "Fungsi-Bawaan/fungsi_type.py"
