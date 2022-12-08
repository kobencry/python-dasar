# loop/perulangan bersarang adalah perulangan di dalam perulangan.
# "perulangan di dalam" akan dieksekusi satu kali untuk setiap iterasi dari "perulangan di luar".

# menggunakan list di dalam list
listku = [['alice', 'carl', 'eliot'], [23, 22, 20]]
for nama_usia in listku:
    #print(nama_usia)
    for x in nama_usia:
        print(x)
# alice
# carl
# eliot
# 23
# 22
# 20

# perulangan yang ada di dalam akan dilakukan sekali untuk setiap iterasi dari perulangan luar.
# contoh 1
listku = ['hello', 'world']
for nama in listku:
    #print(nama)
    for i in nama:
        print(nama, i)
# hello h
# hello e
# hello l
# hello l
# hello o
# world w
# world o
# world r
# world l
# world d

# contoh 2
warna = ['merah', 'kuning', 'hijau']
nama = ['alice', 'carl', 'eliot']
for x in warna:
    for y in nama:
        print(x, y)
# merah alice
# merah carl
# merah eliot
# kuning alice
# kuning carl
# kuning eliot
# hijau alice
# hijau carl
# hijau eliot

# contoh 3
data1 = ['hello', ['alice', 2008]]
data2 = ['world', ['eliot', 2012]]
baris = [data1, data2]
for x in range(len(baris)):
    #print(x)   # 0 1
    for y in range(len(baris[x])):
        #print(y)    # 0 1 0 1
        for z in range(len(baris[x][y])):
            #print(z)    # 0 1 2 3 4 0 1 0 1 2 3 4 0 1
            print(f"x:{x} y:{y} z:{z} baris:{baris[x][y][z]}")

# x:0 y:0 z:0 baris:h
# x:0 y:0 z:1 baris:e
# x:0 y:0 z:2 baris:l
# x:0 y:0 z:3 baris:l
# x:0 y:0 z:4 baris:o
# x:0 y:1 z:0 baris:alice
# x:0 y:1 z:1 baris:2008
# x:1 y:0 z:0 baris:w
# x:1 y:0 z:1 baris:o
# x:1 y:0 z:2 baris:r
# x:1 y:0 z:3 baris:l
# x:1 y:0 z:4 baris:d
# x:1 y:1 z:0 baris:eliot
# x:1 y:1 z:1 baris:2012

# kita bisa membuat bentuk setengah segitiga
for baris in range(5): # mencetak mulai dari 0 - 4 atau for baris in range(1, 6)
    for kolom in range(baris + 1):
        print('*', end='') # print menggunakan parameter end='string'
    print() # kode ini setara dengan karakter \n newline/baris baru
# *
# **
# ***
# ****
# *****

for baris in range(5):
    for kolom in range(baris + 1):
        print(kolom + 1, end='')
    print()
# 1
# 12
# 123
# 1234
# 12345

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan print() kunjungi folder_name: "Fungsi-Bawaan/fungsi_print.py"
