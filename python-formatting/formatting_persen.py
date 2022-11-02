# persen % adalah format python  sejak awal. 
# anda dapat membaca lebih lanjut di dokumen Python. 
# Perlu diingat bahwa % - formatting tidak direkomendasikan oleh dokumen, 
# yang berisi catatan berikut:

# "Operasi pemformatan yang dijelaskan di sini menunjukkan berbagai kebiasaan
# yang menyebabkan sejumlah kesalahan umum 
# (seperti gagal menampilkan tupel dan kamus dengan benar).

# menggunakan literal string yang diformat lebih baru menggunakan 
# fungsi str.format() atau f-string, antarmuka membantu menghindari kesalahan ini.
# Alternatif ini juga menyediakan pendekatan yang lebih kuat, fleksibel, dan 
# dapat diperluas untuk memformat teks.
# Sumber https://docs.python.org/3/library/stdtypes.html#printf-style-string-formatting

# cara menggunakan % - formatting
# objek String memiliki operasi bawaan menggunakan operator %,
# yang dapat Anda gunakan untuk memformat string.
# inilah yang terlihat seperti dalam tutorial

x = "alice"
print("hello %s" % x)   # hello world

# untuk memasukkan lebih dari satu variabel, 
# Anda harus menggunakan tupel atau dictionary dari variabel tersebut.
# menggunakan tuple
x = "alice"
y = 23
print("nama: %s usia: %s" % (x, y)) # nama: alice usia: 23

# menggunakan dictionary
print("nama: %(nama)s usia: %(usia)s" % {'nama':'alice', 'usia':23})
# nama: alice usia: 23

# mengapa % - formatting tidak bagus
# contoh kode yang baru saja anda lihat di atas cukup mudah dibaca. 
# namun, begitu anda mulai menggunakan beberapa parameter dan string yang 
# lebih panjang, kode Anda akan terlihat sedikit berantakan.
nama = "alice"
usia = 23
noid = 444555
email = "alice@gmail.com"
jurusan = "teknik jaringan"
print("nama: %s usia: %s noid: %s email: %s jurusan: %s " % (nama, usia, noid, email, jurusan))
print("nama: %(nama)s usia: %(usia)s noid: %(noid)s email: %(email)s" % {'nama':'carl', 'usia':23, 'noid':222444, 'email':'carl@gmail.com'})

# Jenis pemformatan menggunakan persen %
# di sebelah kanan tanda % anda dapat menambahkan tipe pemformatan untuk memformat hasil

#=========================================

# opsi s
# format string
print("nama: %s usia: %s" % ('alice', 23))  # nama: alice usia: 23 

#=========================================

# opsi d 
# format integer decimal
print("nilai x: %d nilai y: %d total: %d" % (3, 7, 10)) # nilai x: 3 nilai y: 7 total: 10
# jika tipe angka adalah string maka akan menampilkan kesalahan runtime
# print("nilai string %d" % '5')

#=========================================

# opsi i
# format integer decimal
print("nama: %s usia: %i " % ('alice', 23)) # nama: alice usia: 23
# jika tipe angka adalah string maka akan menampilkan kesalahan runtime
# print("nilai string %d" % '5')

#=========================================

# opsi o
# format oktal
x = 255
print("angka %d dari oktal adalah %o" % (x, x)) # angka 255 dari oktal adalah 377

#=========================================

# opsi u
# format integer decimal
# opsi ini mewakili bilangan bulat desimal yang tidak ditandatangani
x = 255
print("opsi d %d opsi u %u" % (x, x))   # opsi d 255 opsi u 255

#=========================================

# opsi e dengan huruf kecil
# opsi E dengan huruf besar
# format float scientific/ilmiah
x = 255
print("opsi e %e opsi E %E" % (x, x))   # opsi e 2.550000e+02 opsi E 2.550000E+02

#=========================================

# opsi f dengan huruf kecil
# opsi F dengan huruf besar
# format float
x = 255
print("opsi f %f opsi F %F" % (x, x))   # opsi f 255.000000 opsi F 255.000000
# anda bisa mengatur jumlah angka dibelakang titik
y = 5.12345
print("jumlah 2: %.2f jumlah 4: %.4f" % (y, y)) # jumlah 2: 5.12 jumlah 4: 5.1235

#=========================================

# opsi g dengan huruf kecil
# opsi G dengan huruf besar
# format float dengan angka 5.0100 nilai float akan di bulatkan menjadi 5.01
print("opsi g %g opsi G %G" % (5.0100, -5.0100))
# jika opsi # digunakan untuk konversi.
# angka nol tidak dihapus dari hasil, dan angka 0 akan ditambahkan.
print("opsi #g %#g opsi #G %#G" % (5.0100, -5.0100)) # opsi #g 5.01000 opsi #G -5.01000

#=========================================

# opsi x dengan huruf kecil
# opsi X dengan huruf besar
# format hexa
x = 255
print("angka %d dari hexa adalah %x" % (x, x))  # angka 255 dari hexa adalah ff
print("angka %d dari hexa adalah %X" % (x, x))  # angka 255 dari hexa adalah FF

#=========================================

# opsi # digunakan untuk konversi. 
# Bentuk alternatif didefinisikan secara berbeda untuk jenis yang berbeda.
# opsi ini hanya berlaku untuk tipe integer, float, dan complex. 
# untuk bilangan bulat, ketika output oktal, atau heksadesimal digunakan,
# opsi ini menambahkan awalan masing-masing '0o', '0x', atau '0x' ke nilai output. 
# Untuk float dan complex, bentuk alternatif menyebabkan hasil konversi selalu 
# berisi karakter titik desimal, meskipun tidak ada angka yang mengikutinya. 
# biasanya, karakter titik desimal muncul di hasil konversi ini hanya jika digit mengikutinya.
# Selain itu, untuk konversi' g' dan 'G', angka nol tidak dihapus dari hasil.

angka = 255
print("nama: %#s usia: %#s" % ('alice', 23))
print("oktal: %o" % angka)  # oktal: 377
print("oktal: %#o" % angka) # oktal: 0o377
print("hexa: %x" % angka)   # hexa: 0xff
print("hexa: %#x" % angka)  # hexa: 0xff
print("float: %g" % angka)  # 255
print("float: %#g" % angka) # 255.000

#=========================================

# opsi 0 nol
# konversi akan menjadi nol untuk nilai numerik
# konversi akan menjadi spasi untuk nilai string 
print("%03d %05s" % (5, 45))    # 005    45

#=========================================

# opsi (spasi)
# format spasi
print("string % s " % "alice")
print("integer % d" % 255)
# anda bisa mengatur jumlah spasi
print("nama: %20s" % "carl") # nama:                 carl
print("usia: %10d" % 23)     # usia:         23

#=========================================

# opsi + dan -
# format dengan angka positif dan negatif
print("integer positif: %+d integer negatif: %-d" % (25, -25))
# opsi + atau - akan diabaikan jika tipe string
print("string positif: %+s" % ("25"))

#=========================================

# opsi s, r, dan a
# opsi s dari str(), opsi r dari repr() dan opsi a dari ascii()
x = "Hello ålice"
# string default/standar python
print("%s" % x) # Hello ålice
# untuk keperluan debuging
print("%r" % x) # 'Hello ålice'
# opsi a/fungsi ascii() menggantikan karakter non-ascii dengan karakter escape
print("%a" % x) # 'Hello \xe5lice'
# Pelajari lebih lanjut tentang fungsi str(), repr() dan ascii() di folder_name: "Fungsi-Bawaan".

# Catatan:
# tentang kecepatan formatting kunjungi file_name: "example.py"
