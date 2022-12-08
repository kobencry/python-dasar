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


# kita bisa membuat berbagai bentuk pola bintang dan angka
for baris in range(5): # mencetak mulai dari 0 - 4 atau for baris in range(1, 6): mencetak mulai dari 1 - 5
    for kolom in range(baris + 1):
        print('*', end='') # print menggunakan parameter end='string'
    print() # kode ini setara dengan karakter \n newline/baris baru
# *
# **
# ***
# ****
# *****

# + Dalam program diatas, perulangan luar adalah jumlah baris yang dicetak.
# + Jumlah baris adalah 5, sehingga perulangan luar akan dieksekusi 5 kali.
# + Selanjutnya, perulangan dalam adalah jumlah total kolom di setiap baris.
# + Untuk setiap iterasi perulangan luar, jumlah kolom bertambah 1.
# + Pada iterasi pertama dari perulangan luar, jumlah kolom adalah 1, berikutnya 2, dan seterusnya.
# + iterasi perulangan dalam sama dengan jumlah kolom.
# + Di setiap iterasi dari perulangan dalam, kami mencetak bintang.

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
