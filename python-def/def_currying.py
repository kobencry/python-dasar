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
# fungsi currying
def masukan_nama(nama):
    def masukan_usia(usia):
        def masukan_alamat(alamat):
            return [nama, usia, alamat]
        return masukan_alamat
    return masukan_usia

print(main('alice', 23, 'jakarta'))  # ['alice', 23, 'jakarta']
print(main('eliot', 23, 'surabaya')) # ['eliot', 23, 'surabaya']

# contoh menggunakan fungsi "normal" dengan argumen yang berisi sebuah fungsi
def main(arg_fungsi:'argumen yang menerima sebagai fungsi'):
    def curried(x: int):
        def apply(y: int):
            return arg_fungsi(x, y)
        return apply
    return curried
# contoh penggunaan
fungsi_tambah = main(lambda p, q: p + q) # argumen yang berisi fungsi penjumlahan p + q
fungsi_tambah_2 = fungsi_tambah(20)
print(fungsi_tambah_2(30))  # 50
print(fungsi_tambah_2(40))  # 60

# Fungsi 'main()' menerima sebuah argumen, dan kemudian mengembalikan sebuah fungsi 'curried()'
# yang menerima sebuah operand pertama. 
# Fungsi 'curried()' yang telah dikembalikan kemudian mengembalikan sebuah fungsi
# yang menerima operand kedua dan menggunakan 'arg_fungsi' untuk menghitung hasilnya.
# Contoh di atas menunjukkan penggunaan 'main()' untuk mengubah fungsi penjumlahan menjadi
# sebuah fungsi 'curried()' yang menerima operand pertama, dan kemudian mengembalikan sebuah 
# fungsi yang menerima operand kedua dan mengembalikan hasil penjumlahan.

# contoh menggunakan fungsi lambda dengan currying
fungsiku = lambda x: lambda y: lambda z: x + y + z
print(fungsiku(100)(200)(300))    # 600

# jika anda ingin mengetahui tentang fungsi lambda python kunjungi folder_name: "python-def/def_lambda.py"
