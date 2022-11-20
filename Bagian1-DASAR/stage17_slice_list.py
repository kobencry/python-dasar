# python mengiris list/slicing list
# slice/mengiris
# anda dapat mengembalikan rentang karakter dengan menggunakan sintaks irisan.
# menentukan indeks awal dan indeks akhir, dipisahkan oleh titik dua (:),
# untuk mengembalikan bagian dari item list.

# catatan: item list pertama dimulai dari indeks 0
# parameter slice [awal:akhir:langkah]

# slicing/pengirisan dimulai dengan parameter indeks awal(termasuk) dan berakhir 
# pada parameter indeks akhir (dikecualikan/tidak termasuk). 
# Parameter langkah digunakan untuk menentukan langkah-langkah untuk mengambil 
# dari awal sampai akhir indeks. 
# mengiris item list python selalu mengikuti aturan ini l[:i] + l[i:] == l untuk setiap Indeks 'i'. 
# semua parameter ini opsional-nilai default parameter awal adalah 0, 
# nilai default parameter akhir adalah panjang item list dan nilai default parameter langkah adalah 1. 

l = ['alice', 'carl', 'eliot']
print(l[:])     # ['alice', 'carl', 'eliot']
print(l[::])    # ['alice', 'carl', 'eliot']
print(l[0])     # alice
print(l[1])     # carl
print(l[2])     # eliot

# mendapatkan item list dari posisi 1 sampai ke posisi 3 (item ke 3 tidak termasuk)
l = ['alice', 'carl', 'eliot', 'geral']
print(l[1:3])   # ['carl', 'eliot']
print(l[1:4])   # ['carl', 'eliot', 'geral']
# melebihi rentang dari item list
print(l[1:6])   # ['carl', 'eliot', 'geral']

# slice/iris dari awal
# mengabaikan nilai indeks awal, akan dimulai pada rentang item list pertama
# [:2] sama dengan [0:2]
# ingat posisi item list 2 (tidak termasuk)
l = ['alice', 'carl', 'eliot', 'geral']
print(l[:2])    # ['alice', 'carl']
print(l[0:2])   # ['alice', 'carl']

# slice/iris sampai akhir
# mengabaikan nilai indeks akhir, akan dimulai pada rentang item list akhir
l = ['alice', 'carl', 'eliot', 'geral']
print(l[0:])    # ['alice', 'carl', 'eliot', 'geral']
print(l[0:4])   # ['alice', 'carl', 'eliot', 'geral']
print(l[0:len(l)])  # ['alice', 'carl', 'eliot', 'geral']

# slice/iris menggunakan parameter langkah l[awal:akhir:langkah]
l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',' k', 'l']
print(l[2:12:2])        # ['c', 'e', 'g', 'i', ' k']
print(l[2:len(l):2])    # ['c', 'e', 'g', 'i', ' k']
# parameter awal nilainya 2 berarti mulai dari huruf c "ingat indeks list dimulai dari angka 0"
# parameter akhir nilainya 11 berarti di akhiri dari huruf l lalu, 
# parameter langkah nilainya 2 berarti langkah huruf 2 kali
# a b c d e f g h i j k  l
# 0 1 2 3 4 5 6 7 8 9 10 11
#     c   e   g   i   k 

# membalikkan item list menggunakan slicing/mengiris
# kita dapat membalikkan item list menggunakan slice dengan 
# memberikan nilai parameter langkah sebagai -1.
l = ['alice', 'carl', 'eliot', 'geral']
print(l[::-1])  # ['geral', 'eliot', 'carl', 'alice']

# pengindeksan negatif
# menggunakan indeks negatif untuk memulai irisan dari akhir item list

# catatan: indeks negatif item list akhir dimulai dari indeks -1

l = ['alice', 'carl', 'eliot', 'geral']
print(l[-1])        # geral
print(l[:-1])       # ['alice', 'carl', 'eliot']
print(l[-1:])       # ['geral']
print(l[-3:-1])     # ['carl', 'eliot']
print(l[-3:])       # ['carl', 'eliot', 'geral']
print(l[-10:-1])    # ['alice', 'carl', 'eliot']
print(l[-10:])      # ['alice', 'carl', 'eliot', 'geral']

# menggunakan list dalam list atau disebut list bersarang.
l = ['alice', ['carl', 'eliot'], False, [2.5, [True, [None, 'geral']]]]
# mendapatkan item list 'eliot'
print(l[1][1])
# mendapatkan item list 'geral'
print(l[3][1][1][1])

# looping beberapa item list
listku = ['alice', 'carl', 'eliot', 'geral']
for i in listku[1:len(listku)]:
    print(i)
# carl
# eliot
# geral

# periksa apakah item list tertentu ada di dalam list
listku = ['alice', 'carl', 'eliot', 'geral']
if 'eliot' in listku:
    print("passed")
else:
    print("failed")

# jika anda ingin mengetahui tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
