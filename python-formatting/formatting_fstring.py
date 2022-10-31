# Jenis Pemformatan menggunakan f-string
# Di dalam placeholder {} Anda dapat menambahkan tipe pemformatan untuk memformat hasil

# contoh menggunakan f-string
print(f"{2*5} {'alice'} hello world")   # 10 alice hello world
x = 5
y = 'hello world'
print(f"nilai a:{x} nilai b: {y}")  # nilai x:5 nilai y: hello world

#=========================================

# :<
# rata kiri (dalam spasi yang tersedia)
x = "alice"
y = 23
print(f"nama: {x:<10} usia: {y:<10}hello")  # nama: alice      usia: 23        hello
txt = f"nama: {x:<10} usia: {y:<10}hello"
print(txt)      # nama: alice      usia: 23     hello

#=========================================

# :>
# rata kanan (dalam spasi yang tersedia)
x = "carl"
y = 24
print(f"nama: {x:>10} usia: {y:>10}hello")  # nama:       carl usia:         24hello
txt = f"nama: {x:>10} usia: {y:>10}hello"
print(txt)  # nama:       carl usia:         24hello

#=========================================

# :^
# rata tengah (dalam spasi yang tersedia)
x = "axel"
y = 25
print(f"nama: {x:^8} usia: {y:^8}")     # nama:   axel   usia:    25

#=========================================

# := (hanya untuk tipe numerik)
# tempatkan tanda di posisi paling kiri
# gunakan "=" untuk menempatkan tanda plus/minus di posisi paling kiri.
x = +10
y = -20
a = 30
b = 3.9
print(f"nilai plus {x:5} nilai minus: {y:=5} nilai biasa: {a:=5} nilai float: {b:=5}")
# nilai plus    10 nilai minus: -  20 nilai biasa:    30 nilai float:  58.3

#=========================================

# :+ (hanya untuk tipe numerik)
# gunakan tanda plus untuk menunjukan apakah hasilnya positif atau negatif
x = -8
y = 3.10
print(f"nilai x: {x:+} nilai y: {y:+}") # nilai x: -8 nilai y: +3.1

#=========================================

# :- (hanya untuk tipe numerik)
# gunakan tanda minus hanya untuk nilai negatif
x = -3.8
y = 3.8
print(f"nilai x: {x:-} nilai y: {y:-}") # nilai x: -3.8 nilai y: 3.8

#=========================================

# :(spasi) (hanya untuk tipe numerik)
# gunakan spasi untuk menyisipkan spasi tambahan sebelum
# angka positif dan tanda  minus sebelum angka negatif
x = -5
y = 10
print(f"nilai x: {x: } nilai y: {y: }") # nilai x: -5 nilai y:  10

#=========================================

# :, (hanya untuk tipe numerik)
# gunakan koma sebagai pemisah seribu
x = 20000
y = 2000000
print(f"nilai x: {x:,} nilai y: {y:,}") # nilai x: 20,000 nilai y: 2,000,000

#=========================================

# :_ (hanya untuk tipe numerik)
# gunakan garis bawah sebagai pemisah seribu
x = 3000
y = 30000
print(f"nilai x: {x:_} nilai y: {y:_}") # nilai x: 3_000 nilai y: 30_000

#=========================================

# :b
# format biner
x = 50
print(f"nilai x: {x} -> biner: {x:b}")  # nilai x: 50 -> biner: 110010

# :c
# mengonversi nilai menjadi karakter unicode yang sesuai
#for i in range(1,256):
#    print(f"unicode:{i}  karakter: {i:c}")
    # unicode:1   karakter: ^A
    # unicode:... karakter:...
    # unicode:48  karakter: 0
    # unicode:... karakter:...
    # unicode:255 karakter: ÿ

#=========================================

# :d
# format decimal
x = 50
print(f"nilai biner: {x:b} -> decimal: {x:d}")  # nilai biner: 110010 -> decimal: 50

#=========================================

# :e format scientific/ilmiah, dengan huruf kecil
# :E format scientific/ilmiah, dengan huruf besar
x = 50
print(f"nilai e: {x:e} nilai E: {x:E}") # nilai e: 5.000000e+01 nilai E: 5.000000E+01

#=========================================

# :f
# :F
# format float, inf nan, INF NAN
# Memperbaiki format angka titik, dalam format huruf besar (tampilkan inf dan nan sebagai INF dan NAN)
x = 5
y = float("inf")
print(f"nilai x: {x:f} nilai y: {y:f}") # nilai x: 5.000000 nilai y: inf
print(f"nilai x: {x:F} nilai y: {y:F}") # nilai x: 5.000000 nilai y: INF
# anda bisa mengatur jumlah angka dibelakang titik
x = 5.112233
print(f"jumlah 2: {x:.2f} jumlah 4: {x:.4f}")   # jumlah 2: 5.11 jumlah 4: 5.1122

#=========================================

# :o
# format oktal
x = 10
print(f"nilai x: {x} nilai octal: {x:o}") # nilai x: 10 nilai octal: 12

#=========================================

# :x
# :X
# format hexa
y = 255
print(f"nilai y: {y} hexa x: {y:x}  hexa X: {y:X}") # nilai y: 255 hexa x: ff  hexa X: FF

#=========================================

# :%
# format persen
x = 0.39
print(f"nilai x: {x} nilai persen: {x:%}") # nilai x: 0.39 nilai persen: 39.000000%

# for i in range(1,10):
#     print(f"nilai: {i} persen %: {i:%}")

# for i in range(1, 10):
#     print(f"nilai: {i} persen %: {i:.0%}")

#=========================================

# fr""
# Raw dan F-string dapat digabungkan. 
# Misalnya, mereka dapat digunakan untuk membangun ekspresi reguler
# jika anda tidak terbiasa dengan pola regex.
# tutorial ini akan menggunakan escape karakter
print(f"\n\t\rhello\n\t\rworld")
print(fr"\n\t\rhello\n\t\rworld")   # \n\t\rhello\n\t\rworld

