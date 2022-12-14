# Fungsi annotations adalah informasi tambahan yang dapat ditambahkan ke fungsi dalam Python 
# untuk menyediakan informasi tambahan tentang tipe data yang diharapkan dari fungsi tersebut. 
# Annotations dapat memberikan informasi yang berguna bagi pengembang untuk memastikan 
# bahwa fungsi tersebut dipanggil dengan argumen yang benar.

# Contoh kode yang menggunakan fungsi annotations dapat seperti ini:
def tambah(x: int, y: int) -> int:
    return x + y
# Di sini, annotations int yang ditambahkan setelah nama variabel x dan y memberikan
# informasi bahwa fungsi add mengharapkan argumen x dan y berupa tipe data integer.
# Annotation -> int setelah deklarasi fungsi menunjukkan bahwa fungsi tambah 
# akan mengembalikan nilai berupa tipe data integer.
print(tambah.__annotations__)
# {'x': <class 'int'>, 'y': <class 'int'>, 'return': <class 'int'>}

print(tambah(2, 3))
# 5

# menambahkan data mahasiswa
def tambah_data(nama:str, usia:int, ipk:float) -> str:
    print(f"{nama} {usia} {ipk}")
print(tambah_data.__annotations__)
# {'nama': <class 'str'>, 'usia': <class 'int'>, 'ipk': <class 'float'>, 'return': <class 'str'>}

tambah_data('alice', 23, 2.5)
# alice 23 2.5

# Anda dapat menggunakan annotations pada fungsi untuk memberikan informasi lebih 
# lanjut tentang tipe data yang diharapkan oleh fungsi tersebut, sehingga memudahkan
# pengembangan aplikasi dan memastikan bahwa fungsi tersebut dipanggil dengan benar.


# contoh tidak variabel annotations tidak menggunakan tipe data
def main(x:'hello', y:'world') -> "Fungsi Main":
    print(x, y)
print(main.__annotations__)
# {'x': 'hello', 'y': 'world', 'return': 'Fungsi Main'}

main(2, 3)
# 2 3

# jika anda ingin mengetahui tentang annotations kunjungi folder_name: "python-annotations"
