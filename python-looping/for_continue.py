# statement continue
# menggunakan pernyataan continue kita dapat menghentikan iterasi loop saat ini, 
# dan melanjutkan dengan yang berikutnya

for i in range(1, 5):   # dimulai dari 1 - 4
    if i == 3:
        print("hello world")
        print("lanjutkan looping")
        continue
    print(i)
# 1
# 2
# hello world
# lanjutkan looping
# 4

# menggunakan tipe data string
for i in 'hello world':
    if i in ('w', 'r'):
        continue
    print(i)
# h
# e
# l
# l
# o
# 
# o
# l
# d

# menggunakan tipe data list
listku = ['alice', 'carl', 10, 20, 'eliot']
for i in listku:
    if i in (10, 20):
        print(i, 'bukan string')
        continue
    print(i)
# alice
# carl
# 10 bukan string
# 20 bukan string
# eliot

# perbedaan menggunakan statement continue dan tidak.

# nilai yang di cetak akan duplikat/sama
# tidak menggunakan statement continue
for i in range(1, 5): # mencetak dari 1 - 4
    if i == 3:
        print(i)
    print(i)
# 1
# 2
# 3  <-  
# 3  <-
# 4

# menggunakan statement contunie
for i in range(1, 5):
    if i == 3:
        print(i)
        continue
    print(i)
# 1
# 2
# 3  <-
# 4

# jika statement continue tidak melakukan apapun Contoh:
# tidak mencetak nilainya, maka nilai tersebut akan diabaikan "tidak di cetak"
for i in range(1, 5):
    if i == 3:
        continue
    print(i)
# 1
# 2
# 4
# angka tiga tidak di cetak ke layar

# apakah angka tersebut bilangan ganjil atau bilangan genap.
# tidak menggunakan statement continue, gunkanlah statement if/else
for i in range(1, 20):
    if i %2==0:
        print(i, "bilangan genap")
    else:
        print(i, "bilangan ganjil")

# beberapa contoh jalankan kode program di bawah ini
#for i in range(1, 20):
#    if i %2==0:
#        print(i, "bilangan genap")
#        continue
#    print(i, "bilangan ganjil")

#for i in range(1, 20):
#    if i %2==0:
#        print(i, "bilangan genap")
#    print(i, "bilangan ganjil")

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
