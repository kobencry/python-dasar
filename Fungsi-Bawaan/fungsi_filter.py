# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html#filter

# fungsi filter() memungkinkan Anda memilih atau memfilter item dari 
# iterable berdasarkan evaluasi fungsi yang diberikan.

# Syntax
# filter(function, iterable)

# Nilai Parameter
# Parameter                 Deskripsi
# function                  Fungsi yang akan dijalankan untuk setiap item di iterable.
# iterable                  Iterable untuk difilter.

# mencari nilai bilangan genap
listku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bilangan_genap = filter(lambda x: x %2==0, listku)
print(bilangan_genap)
# Output:
# <filter object at 0x000001BC22EE3250>

# mengubah filter menjadi list, agar mudah dibaca
print(list(bilangan_genap))
# Output:
# [2, 4, 6, 8, 10]

# jika anda tidak terbiasa dengan fungsi lambda(annonymous functions)
# kode ini setara degan diatas
def fungsiku(x):
    return x %2==0
bilangan_genap = list(filter(fungsiku, listku))
print(bilangan_genap)
# Output:
# [2, 4, 6, 8, 10]

# mencari nilai bilangan ganjil
listku = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
bilangan_ganjil = list(filter(lambda x: x %2!=0, listku))
print(bilangan_ganjil)
# Output:
# [1, 3, 5, 7, 9]

# mencari nama yang memiliki panjang lebi dari 4 karakter
nama_list = ['alice', 'bob', 'carl', 'done', 'eliot', 'for', 'gerald']
hasil = list(filter(lambda x: len(x) > 4, nama_list))
print(hasil)
# Output:
# ['alice', 'eliot', 'gerald']

# mencari nilai diatas rata-rata
listku = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
rata_rata = sum(listku) / len(listku)
hasil = list(filter(lambda x: x > rata_rata, listku))
print(hasil) 
# Output:
# [60, 70, 80, 90, 100]

# mencari nama yang memiliki huruf 'a'
nama_list = ['alice', 'carl', 'eliot', 'gerald']
hasil = list(filter(lambda x: 'a' in x, nama_list))
print(hasil)
# Output:
# ['alice', 'carl', 'gerald']

# fungsi filter() setara dengan menulis ekspresi generator
def fungsi_filter(function, iterable):
    return (i for i in iterable if function(i))

# mencari tipe data integer
listku = [10.5, 'foo', 10, 'bar', 25, '100', 25.0, True, 50]
hasil = list(fungsi_filter(lambda x: type(x) == int, listku))
print(hasil)
# Output:
# [10, 25, 50]

# mencari mahasiswa dengan nilai IPK di atas 3.0
mahasiswa = [
    {'nama':'alice', 'nim':1111, 'ipk':3.2},
    {'nama':'carl', 'nim':2222, 'ipk':2.8},
    {'nama':'eliot', 'nim':3333, 'ipk':3.5},
    {'nama':'gerald', 'nim':4444, 'ipk':3.0}
]
hasil = list(filter(lambda x: x['ipk'] >= 3.0, mahasiswa))
print(hasil)
# Output:
# [{'nama': 'alice', 'nim': 1111, 'ipk': 3.2}, {'nama': 'eliot', 'nim': 3333, 'ipk': 3.5}, {'nama': 'gerald', 'nim': 4444, 'ipk': 3.0}]
for dictku in hasil:
    print(dictku)
# Output:
# {'nama': 'alice', 'nim': 1111, 'ipk': 3.2}
# {'nama': 'eliot', 'nim': 3333, 'ipk': 3.5}
# {'nama': 'gerald', 'nim': 4444, 'ipk': 3.0}