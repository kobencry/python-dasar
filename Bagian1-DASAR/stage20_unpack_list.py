# unpacking/membongkar List
# Saat membuat list, kami biasanya memberikan nilai padanya, ini disebut "packing/mengemas" list.
packing_list = ['alice', 'carl', 'eliot']
# unpacking list
x, y, z = packing_list
print(x)    # alice 
print(y)    # carl
print(z)    # eliot

# Catatan: Jumlah variabel harus sesuai dengan jumlah nilai dalam list,
# jika tidak, Anda harus menggunakan tanda bintang (*) untuk mengumpulkan
# nilai yang tersisa sebagai list.

# unpacking menggunakan tanda bintang *
packing_list = ['alice', 'carl', 'eliot', 'geral']
x, y, *z = packing_list
print(x)    # alice
print(y)    # carl
print(z)    # ['eliot', 'geral']

# Jika tanda bintang ditambahkan ke nama variabel lain selain yang terakhir,
# Python akan memberikan nilai ke variabel sampai jumlah nilai yang tersisa 
# sesuai dengan jumlah variabel yang tersisa.

packing_list = ['alice', 'carl', 'eliot', 'geral']
x, *y, z = packing_list
print(x)    # alice
print(y)    # ['carl', 'eliot']
print(z)    # geral

*x, y, z = packing_list
print(x)    # ['alice', 'carl']
print(y)    # eliot
print(z)    # geral
