# Fungsi adalah blok kode yang hanya berjalan saat dipanggil.
# Anda dapat meneruskan data, yang dikenal sebagai parameter, ke dalam suatu fungsi.
# Suatu fungsi dapat mengembalikan data sebagai hasilnya.

# Hampir semua bahasa pemrograman yang digunakan saat ini mendukung bentuk 
# fungsi yang ditentukan pengguna, meskipun tidak selalu disebut fungsi.
# Dalam bahasa lain, Anda mungkin melihatnya disebut sebagai salah satu dari berikut ini:
# Subroutines/Subrutin
# Procedures/Prosedur
# Methods/Metode
# Subprograms/Subprogram

# Untuk membuat fungsi di Python, Anda dapat menggunakan keyword 'def',
# diikuti dengan nama fungsi dan parameter yang diperlukan. Contoh:

# Syntax
# def <nama_fungsi>(parameter):
#     <statement>

# <nama_fungsi>(argument)

# def          Kata kunci yang menginformasikan Python bahwa suatu fungsi sedang didefinisikan
# nama_fungsi  Pengidentifikasi Python yang valid yang menamai fungsi.
# parameter    Daftar parameter opsional yang dipisahkan koma yang dapat diteruskan ke fungsi
# statement    Blok pernyataan python yang valid
# arguments    adalah nilai yang diteruskan ke fungsi. 

# membuat fungsi tanpa parameter
def hello():
    # isi fungsi disini 
    x = 10
    print(x)
    print('ini adalah fungsi hello')

# memanggil fungsi
# untuk menjalankan fungsi, anda dapat memanggil fungsi dengan menuliskan nama fungsi diikuti dengan tanda kurung ().
hello()
# output:
# 10
# ini adalah fungsi hello

# membuat fungsi menggunakan satu parameter atau argumen
def word(parameter):
    # isi fungsi disini
    print(parameter)
    print("ini adalah fungsi word")

# memanggil fungsi
# anda harus mengisi nilai parameter atau argumen dari fungsi word(argumen|parameter)
word('hello world')
# output:
# hello world
# ini adalah fungsi word

# Parameter atau Argumen?
# Istilah parameter dan argumen dapat digunakan untuk hal yang sama: 
# "informasi yang diteruskan ke suatu fungsi"
# Argumen sering disingkat menjadi args dalam dokumentasi Python.

# Jumlah Argumen
# Secara default, sebuah fungsi harus dipanggil dengan jumlah argumen yang benar.
# Artinya jika fungsi Anda mengharapkan 2 argumen, Anda harus memanggil fungsi 
# tersebut dengan 2 argumen, tidak lebih, dan tidak kurang.
def fungsiku(nama, usia):
    print(f"nama: {nama} usia: {usia}")

# memanggil fungsi
fungsiku('alice', 23)
# output:
# nama: alice usia: 23

# Jika Anda mencoba memanggil fungsi dengan 1 atau 3 argumen, Anda akan mendapatkan error:
# fungsiku('alice') error
# fungsiku('alice', 23, 'hello') error

# fungsi juga dapat mengembalikan nilai dengan keyword 'return' 
def fungsiku(nama, usia):
    return f"nama: {nama} usia: {usia}"
# untuk menampilkan hasilnya gunakan fungsi print(nama_fungsi)
print(fungsiku('alice', 23))
# nama: alice usia: 23

x = fungsiku('alice', 23)
print(x)
# nama: alice usia: 23

# Argumen Kata Kunci
# Anda juga dapat mengirim argumen dengan sintaks kunci = nilai .
# Dengan cara ini urutan argumen tidak menjadi masalah.
def fungsiku(nama, usia, alamat):
    return f"nama: {nama} usia: {usia} alamat: {alamat}"
x = fungsiku(nama='alice', usia=23, alamat='jakarta')
# memasukan argumen tidak dalam urutan
y = fungsiku(alamat='bandung', nama='carl', usia=25)
print(x)    # nama: alice usia: 23 alamat: jakarta
print(y)    # nama: carl usia: 25 alamat: bandung

# jenis-jenis keyword python kunjungi file_name: "stage01_helloworld.py"
# jika anda ingin mengetahui tentang jenis-jenis argumen/parameter pada fungsi python kunjungi folder_name: "python-def"
