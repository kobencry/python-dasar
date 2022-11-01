# Jenis Pemformatan menggunakan fungsi format()
# Di dalam placeholder {} Anda dapat menambahkan tipe pemformatan untuk memformat hasil

# :<
# rata kiri (dalam spasi yang tersedia)
txt = "nama:{nama:<10} usia:{usia}".format(nama='axel', usia=23)
print(txt)  # nama:axel         usia:23

#=========================================

# :>
# rata kanan (dalam spasi yang tersedia)
txt = "nama:{nama:>20} usia:{usia:>3}".format(nama='axel', usia=23)
print(txt)  # nama:                axel usia: 23

#=========================================

# :^
# rata tengah (dalam spasi yang tersedia)
txt = "nama:{nama:^8} usia:{usia:^8}".format(nama='axel', usia=23)
print(txt)  # nama:  axel   usia:   23

#=========================================

# := (hanya untuk type numerik)
# tempatkan tanda di posisi paling kiri
# Gunakan "=" untuk menempatkan tanda plus/minus di posisi paling kiri:
txt = "nilai plus {x:=8} nilai minus {y:=10} nilai biasa {z:=10} nilai float {a:=10}".format(x=+23, y=-20, z=50, a=38.3)
print(txt)  # nilai plus       23 nilai minus -       20 nilai biasa         50 nilai float       38.3
 
#==========================================

# :+ (hanya untuk type numerik)
# Gunakan tanda plus untuk menunjukkan apakah hasilnya positif atau negatif
txt = "nilai x: {x:+} nilai y: {y:+}".format(x=-8, y=38.0)
print(txt)  # nilai x: -8 nilai y: +38.0

#===========================================

# :- (hanya untuk type numerik)
# Gunakan tanda minus hanya untuk nilai negatif
txt = "nilai x: {x:-} nilai y: {y:-}".format(x=-13.8, y=24.8)
print(txt)  # nilai x: -13.8 nilai y: 24.8

#===========================================

# :(spasi) (hanya untuk type numerik)
# Gunakan spasi untuk menyisipkan spasi tambahan sebelum 
# angka positif (dan tanda minus sebelum angka negatif)
txt = "nilai x:{x: } nilai y:{y: }".format(x=-5, y=10)
print(txt)  # nilai x:-5 nilai y: 10

#============================================

# :, (hanya untuk type numerik)
# Gunakan koma sebagai pemisah seribu
txt = "nilai x: {x:,}".format(x=280000000)
print(txt)  # nilai x: 280,000,000

#============================================

# :_ (hanya untuk type numerik)
# Gunakan garis bawah sebagai pemisah seribu
txt = "nilai x: {x:_}".format(x=59000)
print(txt)  # nilai x: 59_000

#============================================

# :b
# format biner
txt = "nilai {x} => biner {x:b}".format(x=50)
print(txt)  # nilai 50 => biner 110010

#============================================

# :c 
# mengonversi nilai menjadi karakter unicode yang sesuai
# print("{:c}".format(1)) # \x01
#for i in range(1,256):
#    txt = "unicode: {x} karakter: {x:c}".format(x=i)
#    print(txt) # unicode: 1  karakter:^1
                # unicode:... karakter:...
                # unicode: 48 karakter: 0
                # unicode: 49 karakter: 1
                # unicode: 50 karakter: 2
                # unicode: 51 karakter: 3
                # unicode: 52 karakter: 4
                # unicode: 53 karakter: 5
                # unicode: 54 karakter: 6
                # unicode: 55 karakter: 7
                # unicode: 56 karakter: 8
                # unicode: 57 karakter: 9
                # unicode:... karakter:...

#============================================

# :d
# format decimal
txt = "biner: {x:b} decimal: {x:d}".format(x=50)
print(txt)  # biner: 110010 decimal: 50

#============================================

# :e  Format ilmiah, dengan huruf kecil e
# :E  Format ilmiah, dengan huruf besar E
txt = "nilai e: {x:e} nilai E: {x:E}".format(x=50000)
print(txt)  # nilai e: 5.000000e+04 nilai E: 5.000000E+04

#============================================

# :f
# :F  
# Memperbaiki format angka titik, dalam format huruf besar (tampilkan inf dan nan sebagai INF dan NAN)
txt = "nilai f: {x:f} nilai F: {x:F}".format(x=4.1)
print(txt)  # nilai f: 4.100000 nilai F: 4.100000
txt = "nilai f: {x:} nilai F: {x:F}".format(x=float('inf'))
print(txt)  # nilai f: inf nilai F: INF
# format float
# anda bisa mengatur jumlah angka dibelakang titik
txt = "angka float x: {x:f} angka float y:{y:.2f}".format(x=5, y=5)
print(txt)  # angka float x: 5.000000 angka float y:5.00
txt = "angka float x: {x:.3f} angka float y: {y:.5f}".format(x=5.112233, y=5.112233)
print(txt)  # angka float x: 5.112 angka float y: 5.11223

#=============================================

# :g
# :G
# angka nol yang tidak signifikan dihapus dari angka signifikan, dan 
# titik desimal juga dihapus jika tidak ada digit tersisa yang mengikutinya, 
# kecuali opsi '#' digunakan.
# format float dengan angka 5.0100 nilai float akan di bulatkan menjadi 5.01
print("{x:g}".format(x=5.0100))     # 5.01
print("{y:G}".format(y=-5.0100))    # -5.01
# tidak menggunakan flag :g/:G secara default python membulatkan floating
print(5.0100)   # 5.01
print(-5.0100)  # -5.01

#=============================================

# :o
# format oktal
txt = "nilai x: {x} nilai oktal: {x:o}".format(x=9)
print(txt)  # nilai x: 9 nilai oktal: 11

#==============================================

# :x
# :X
# format hexa
txt = "nilai x: {x} hexa x: {x:x} hexa X: {x:X}".format(x=255)
print(txt)  # nilai x: 255 hexa x: ff hexa X: FF

#==============================================

# :%
# format persen
txt = "nilai x: {x} persen %: {x:%}".format(x=0.35)
print(txt)  # nilai x: 0.35 persen %: 35.000000%

#for i in range(1, 10):
#    print("nilai: {i} persen %: {i:%}".format(i=i))

#for i in range(1, 10):
#    print("nilai: {i} persen %: {i:.0%}".format(i=i))

#================================================

# :#
# opsi ' # digunakan untuk konversi. 
# Bentuk alternatif didefinisikan secara berbeda untuk jenis yang berbeda.
# opsi ini hanya berlaku untuk tipe integer, float, dan complex. 
# untuk bilangan bulat, ketika output biner, oktal, atau heksadesimal digunakan,
# opsi ini menambahkan awalan masing-masing '0b', '0o', '0x', atau '0x' ke nilai output. 
# Untuk float dan complex, bentuk alternatif menyebabkan hasil konversi selalu 
# berisi karakter titik desimal, meskipun tidak ada angka yang mengikutinya. 
# biasanya, karakter titik desimal muncul di hasil konversi ini hanya jika digit mengikutinya.
# Selain itu, untuk konversi' g' dan 'G', angka nol tidak dihapus dari hasil.
angka = 255
print("biner: {:b}".format(angka))      # biner: 11111111
print("biner: {:#b}".format(angka))     # biner: 0b11111111
print("oktal: {:o}".format(angka))      # oktal: 377
print("oktal: {:#o}".format(angka))     # oktal: 0o377
print("hexa: {:x}".format(angka))       # hexa: ff
print("hexa: {:#x}".format(angka))      # hexa: 0xff
print("float: {:g}".format(5.000))      # float: 5
print("float: {:#g}".format(5.000))     # float: 5.00000

#================================================

# !s !r dan !a
# pola !s sama dengan fungsi str()
# pola !r sama dengan fungsi repr()
# pola !a sama dengan fungsi ascii()
# konversi !s !r dan !a tidak benar-benar diperlukan. 
# karena ekspresi sewenang-wenang diperbolehkan di dalam format string kode ini
x = "Hello ålice"
# hasil default string dari program python
print("{!s}".format(x))
# untuk keperluan debuging
print("{!r}".format(x))
# pola !a/fungsi ascii() menggantikan karakter non-ascii dengan karakter escape
print("{!a}".format(x))
# Pelajari lebih lanjut tentang fungsi str(), repr() dan ascii() di folder_name: "Fungsi-Bawaan".

# menggunakan konstraktor dict()
data_dict = {"nama":'alice', "usia":23, "email":'alice@gmail.com', "jurusan":'teknik komputer'}
print("{nama} {usia} {email} {jurusan}".format(**data_dict))


x = 0.3
y = 5.5
z = 10
print()
print(f"x {x}: {x:%} {x:.0%}") # x 0.3: 30.000000% 30%
print(f"y {y}: {y:%} {y:.0%}") # y 5.5: 550.000000% 550%
print(f"z {z}: {z:%} {z:.0%}") # z 10: 1000.000000% 1000%

# Catatan:
# tentang kecepatan formatting kunjungi file_name: "example.py"
