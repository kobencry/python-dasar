# definisi looping/perulangan
# Secara umum, looping atau perulangan pada Python adalah instruksi kode program 
# yang dieksekusi berulang kali. 
# Fungsinya untuk memerintah komputer melakukan sesuatu secara berulang-ulang 
# dengan jumlah tertentu selama sebuah kondisi yang telah ditentukan masih terpenuhi.

# for loop adalah perulangan yang digunakan untuk (list, tuple, dict, set, atau string)
# Dengan perulangan for kita dapat menjalankan serangkaian pernyataan, satu kali untuk setiap item dalam daftar, tuple, set, dll.

# Syntax
# for <variabel> in <iterable>:
#     <statemen>

# <variabel> mengambil nilai elemen berikutnya di <iterable> setiap kali melalui loop.  
# <iterable> adalah kumpulan objek misalnya list, tupel, dict, set, atau string.
# <statemen> seperti semua struktur kontrol Python, dan dieksekusi sekali untuk setiap item di <iterable>.

# menggunakan tipe data string
for s in "hello world":
    print(s)
# h
# e
# l
# l ...dst('dan seterusnya')

# menggunakan tipe data list
listku = ['alice', 'carl', 'eliot']
for var in listku:
    print(var)
# alice
# carl
# eliot

# menggunakan tipe data tuple
x = 0
for i in ('alice', 'carl', 'eliot'):
    # x = x + 1
    # kode ini seterara dengan diatas
    x += 1
    print(f"{x}. {i}")
# 1. alice
# 2. carl
# 3. eliot

# menggunakan tipe data dict
for key, val in {'nama':'alice', 'usia':23, 'alamat':'jakarta'}.items():
    print(key, val)
# nama alice
# usia 23
# alamat jakarta

# menggunakan for loop bersarang ("for loop didalam for loop")
# Catatan: for loop yang ada didalam akan dieksekusi satu kali  untuk iterasi dari for loop yang ada diluar.
noid = [100, 200, 300]
nama = ['alice', 'carl', 'eliot']
for i in noid:
    for j in nama:
        print(i, j)
# 100 alice
# 100 carl
# 100 eliot
# 200 alice
# 200 carl
# 200 eliot
# 300 alice
# 300 carl
# 300 eliot

# menggunakan fungsi bawaan python zip()
nama = ('alice', 'carl', 'eliot')
usia = (23, 22, 20)
for nama, usia in zip(nama, usia):
    print(nama, usia)
# alice 23
# carl 22
# eliot 20

# menggunakan fungsi bawaan python range()
for i in range(3):
    print(i)
# 0
# 1
# 2

# mengabaikan nilai dengan garis bawah _
for _ in range(3):
    print("hello world")
# hello world
# hello world
# hello world

# membuat program bilangan ganjil genap
for i in range(1, 10):
    if i %2==0:
        print(f"{i} bilangan genap")
    else:
        print(f"{i} bilangan ganjil")

# jika anda ingin mengetahui tentang for loop dengan berbagai statement kunjungi folder_name: "python-looping"
# jika anda ingin mengetahui tentang fungsi-bawaan zip() kunjungi folder_name: "Fungsi-Bawaan/fungsi_zip.py"
# jika anda ingin mengetahui tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
