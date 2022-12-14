# statement return
# Dalam bahasa pemrograman Python, fungsi 'return' adalah perintah yang digunakan
# untuk mengembalikan nilai dari suatu fungsi. 
# Fungsi 'return' biasanya digunakan dalam sebuah fungsi untuk menghentikan eksekusi
# fungsi dan memberikan nilai kembali ke bagian kode program yang memanggil fungsi tersebut.

# contoh Anda dapat menggunakan fungsi return untuk mengembalikan hasil 
# perhitungan tersebut ke bagian kode program yang memanggil fungsi tersebut.
def tambah(x, y):
    return x + y

def kurang(x, y):
    hasil = x - y
    return hasil

# memanggil fungsi tambah
tambah(1, 2)

# karna return hanya mengembalikan nilainya, 
# untuk mencetak nilainya gunakan fungsi print()
print(tambah(1, 2))
# 3

# bisa juga seperti ini
x = kurang(5, 2)
print(x)
# 3

# 

# contoh 'return' tidak mengembalikan tipe data apapun atau nilai kosong
def fungsiku(x):
    # jika nilai x kurang dari 0
    if x < 0:
        return
        # return f"nilai x adalah bilangan negatif"
    # jika nilai x lebih besar dari 100
    if x > 10:
        return
        # return f"nilai x terlalu besar"
    # jika kondisi atas tidak terpenuhi cetak nilai x
    print(x)

fungsiku(-2)
fungsiku(20)
fungsiku(5)
# 5

# menggunakan fungsi tanpa argumen 
def listku():
    return ['alice', 'carl', 'eliot']

for f in tupleku():
    print(f)

print(listku()[0])
# alice

for f in listku():
    print(f)
    # alice
    # carl
    # eliot

# Suatu fungsi dapat mengembalikan semua jenis objek. 
# Dalam Python, itu berarti hampir semua hal.
# pemanggilan fungsi dapat digunakan secara sintaksis dengan cara apa pun yang masuk
# akal untuk jenis objek yang dikembalikan fungsi.
# Misalnya, dalam kode diatas, listku() mengembalikan tipe data list. 
# Di pemanggilan fungsi, ekspresi listku() mewakili list, dan listku()[0] adalah referensi ke elemen alice.
