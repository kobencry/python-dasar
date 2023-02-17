# Keyword yield adalah sebuah kata kunci dalam bahasa pemrograman Python yang digunakan 
# untuk menghasilkan nilai pada fungsi yang didefinisikan dengan menggunakan generator.
# Dalam hal ini, fungsi generator mengembalikan iterator yang menghasilkan nilai berulang kali
# pada setiap iterasi hingga mencapai akhir dari generator.

# Saat memanggil fungsi generator dengan kata kunci yield, 
# Python akan mengevaluasi nilai yang dihasilkan dan kemudian menghentikan eksekusi fungsi, 
# sementara nilai-nilai tersebut dapat diakses secara berurutan oleh pengguna melalui iterator yang dihasilkan.

def fungsiku():
    nilai = 1
    print("baris pertama")
    yield nilai

    nilai += 1
    print("baris kedua")
    yield nilai

    nilai += 2
    print("baris ketiga")
    yield nilai

# untuk menampilkan hasilnya anda bisa menggunakan forloop atau method next()
print(next(fungsiku()))
# Output:
# baris pertama
# 1

for i in fungsiku():
    print(i)
# Output:
# baris pertama
# 1
# baris kedua
# 2
# baris ketiga
# 4

def generator(iterable):
    panjang = len(iterable)
    for i in range(panjang):
        yield iterable[i]

for i in generator(['alice', 'carl', 'eliot']):
    print(i)
# Output:
# alice
# carl
# eliot

for i in generator("hello world"):
    print(i)
# Output:
# h
# e
# l
# l
# o

# w
# o
# r
# l
# d