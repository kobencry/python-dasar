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
