# python slicing/mengiris tuple
# slice/mengiris
# anda dapat mengembalikan rentang karakter dengan menggunakan sintaks irisan.
# menentukan indeks awal dan indeks akhir, dipisahkan oleh titik dua (:),
# untuk mengembalikan bagian dari item tuple.

# catatan: item tuple pertama dimulai dari indeks 0
# parameter slice [awal:akhir:langkah]

# slicing/pengirisan dimulai dengan parameter indeks awal(termasuk) dan berakhir 
# pada parameter indeks akhir (dikecualikan/tidak termasuk). 
# Parameter langkah digunakan untuk menentukan langkah-langkah untuk mengambil 
# dari awal sampai akhir indeks. 
# mengiris item tuple python selalu mengikuti aturan ini t[:i] + t[i:] == t untuk setiap Indeks 'i'. 
# semua parameter ini opsional-nilai default parameter awal adalah 0, 
# nilai default parameter akhir adalah panjang item tuple dan nilai default parameter langkah adalah 1. 

t = ('alice', 'carl', 'eliot')
print(t[:])     # ('alice', 'carl', 'eliot')
print(t[::])    # ('alice', 'carl', 'eliot')
print(t[0])     # alice
print(t[1])     # carl
print(t[2])     # eliot

# mendapatkan item tuple dari posisi 1 sampai ke posisi 3 (item ke 3 tidak termasuk)
t = ('alice', 'carl', 'eliot', 'geral')
print(t[1:3])   # ('carl', 'eliot')
print(t[1:4])   # ('carl', 'eliot', 'geral')

# melebihi rentang dari item tuple
print(t[1:6])   # ('carl', 'eliot', 'geral')

# slice/iris dari awal
# mengabaikan nilai indeks awal, akan dimulai pada rentang item tuple pertama
# [:2] sama dengan [0:2]
# ingat posisi item tuple 2 (tidak termasuk)
t = ('alice', 'carl', 'eliot', 'geral')
print(t[:2])    # ('alice', 'carl')
print(t[0:2])   # ('alice', 'carl')

# slice/iris sampai akhir
# mengabaikan nilai indeks akhir, akan dimulai pada rentang item tuple akhir.
t = ('alice', 'carl', 'eliot', 'geral')
print(t[0:])    # ('alice', 'carl', 'eliot', 'geral')
print(t[0:4])   # ('alice', 'carl', 'eliot', 'geral')
print(t[0:len(t)])  # ('alice', 'carl', 'eliot', 'geral')

# slice/iris menggunakan parameter langkah t[awal:akhir:langkah]
t = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',' k', 'l')
print(t[2:12:2])        # ('c', 'e', 'g', 'i', ' k')
print(t[2:len(t):2])    # ('c', 'e', 'g', 'i', ' k')
# parameter awal nilainya 2 berarti mulai dari huruf c "ingat indeks tuple dimulai dari angka 0"
# parameter akhir nilainya 11 berarti di akhiri dari huruf l lalu, 
# parameter langkah nilainya 2 berarti langkah huruf 2 kali
# a b c d e f g h i j k  l
# 0 1 2 3 4 5 6 7 8 9 10 11
#     c   e   g   i   k 

# membalikkan item tuple menggunakan slicing/mengiris
# kita dapat membalikkan item tuple menggunakan slice dengan 
# memberikan nilai parameter langkah sebagai -1.
t = ('alice', 'carl', 'eliot', 'geral')
print(t[::-1])   # ('geral', 'eliot', 'carl', 'alice')

# pengindeksan negatif
# menggunakan indeks negatif untuk memulai irisan dari akhir item tuple

# catatan: indeks negatif item tuple akhir dimulai dari indeks -1

t = ('alice', 'carl', 'eliot', 'geral')
print(t[-1])        # geral
print(t[:-1])       # ('alice', 'carl', 'eliot')
print(t[-1:])       # ('geral',)
print(t[-3:-1])     # ('carl', 'eliot')
print(t[-3:])       # ('carl', 'eliot', 'geral')
print(t[-10:-1])    # ('alice', 'carl', 'eliot')
print(t[-10:])      # ('alice', 'carl', 'eliot', 'geral')

# menggunakan tuple dalam tuple atau disebut tuple bersarang.
t = ('alice', ('carl', 'eliot'), False, (2.5, (True, (None, 'geral'))))
# mendapatkan item tuple 'eliot'
print(t[1][1])
# mendapatkan item tuple 'geral'
print(t[3][1][1][1])

# looping beberapa item tuple
tupleku = ('alice', 'carl', 'eliot', 'geral')
for i in tupleku[1:len(tupleku)]:
    print(i)
# carl
# eliot
# geral

# periksa apakah item tuple tertentu ada di dalam tuple
tupleku = ('alice', 'carl', 'eliot', 'geral')
if 'eliot' in tupleku:
    print("passed")
else:
    print("failed")

# jika anda ingin mengetahui tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
