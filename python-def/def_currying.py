# Currying adalah teknik pemrograman yang memungkinkan Anda mengubah fungsi yang menerima 
# beberapa argumen menjadi sekumpulan fungsi yang masing-masing menerima satu argumen.
# Fungsi yang dihasilkan dari proses currying disebut sebagai fungsi curried.

# Contoh sederhananya, jika Anda memiliki sebuah fungsi yang menerima tiga argumen seperti berikut:
def tambah(x, y, z):
    return x + y + z
print(tambah(1, 2, 3))  # 6

# Anda dapat menerapkan currying pada fungsi tersebut sehingga menjadi seperti ini:
def tambah(x):
    def tambah_2(y):
        def tambah_3(z):
            return x + y + z
        return tambah_3
    return tambah_2

# memanggil fungsi tambah()
print(tambah(1)(2)(3))  # 6


# anda dapat memanggilnya dengan fungsi "normal" dan nilai argumen diteruskan ke fungsi curry
def main(nama, usia, alamat):
    return masukan_nama(nama)(usia)(alamat)

def masukan_nama(nama):
    def masukan_usia(usia):
        def masukan_alamat(alamat):
            return [nama, usia, alamat]
        return masukan_alamat
    return masukan_usia

print(main('alice', 23, 'jakarta'))  # ['alice', 23, 'jakarta']
print(main('eliot', 23, 'surabaya')) # ['eliot', 23, 'surabaya']

# contoh menggunakan fungsi lambda 
fungsiku = lambda x: lambda y: lambda z: x + y + z
print(fungsiku(1)(2)(3))    # 6

# jika anda ingin mengetahui tentang fungsi lambda python kunjungi folder_name: "python-def/def_lambda.py"
