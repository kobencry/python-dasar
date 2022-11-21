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
