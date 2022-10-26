# python mengiris string/slicing string
# slice/mengiris
# anda dapat mengembalikan rentang karakter dengan menggunakan sintaks irisan.
# menentukan indeks awal dan indeks akhir, dipisahkan oleh titik dua (:),
# untuk mengembalikan bagian dari string.

# catatan: karakter pertama dimulai dari indeks 0
# parameter slice [awal:akhir:langkah]

# slicing/pengirisan dimulai dengan parameter indeks awal(termasuk) dan berakhir 
# pada parameter indeks akhir (dikecualikan/tidak termasuk). 
# Parameter langkah digunakan untuk menentukan langkah-langkah untuk mengambil 
# dari awal sampai akhir indeks. 
# mengiris string python selalu mengikuti aturan ini s[:i] + s[i:] == s untuk setiap Indeks 'i'. 
# semua parameter ini opsional-nilai default parameter awal adalah 0, 
# nilai default parameter akhir adalah panjang string dan nilai default 
# parameter langkah adalah 1. 
# Mari kita lihat beberapa contoh sederhana dari fungsi string slice untuk membuat substring.
s = "hello world"
print(s[:])     # hello world
print(s[::])    # hello world

# mendapatkan karakter dari posisi 2 ke posisi 5. 
# bagian karakter 5 (tidak termasuk)
s = "hello world"
# hello world
# 012345678910
print(s[1:5])     # ello
print(s[1:4])     # ell

# slice/iris dari awal
# mengabaikan indeks awal, akan dimulai pada rentang karakter pertama
# [:6] sama dengan [0:6]
s = "hello wrodl!"
print(s[0:5])     # hello
print(s[:5])      # hello

# slice/iris sampai akhir
# mengabaikan indeks akhir, akan dimulai pada rentang karakter akhir
x = "hello"
y = "hello world!"
print(x[0:5])       # hello
print(x[0:])        # hello
print(y[0:5])       # hello
print(y[0:])        # hello world!

# menggunakan parameter langkah s[awal:akhir:langkah]
s = "abcdefghijklmnopqrstuvwxyz"
print(s[2:25:2])     # cegikmoqsuwy
print(s[2:len(s):2]) # cegikmoqsuwy 
# jika anda ingin mengetahui fungsi len() kunjungi file_name: "Fungsi-Bawaan/fungsi_len.py"

# membalikkan string/karakter menggunakan slicing/mengiris
# kita dapat membalikkan string/karakter menggunakan slice dengan 
# memberikan nilai parameter langkah sebagai -1.
s = "hello world"
print(s[::-1])  # dlrow olleh

# pengindeksan negatif
# menggunakan indeks negatif untuk memulai irisan dari akhir string

# catatan: indeks negatif karakter akhir dimulai dari indeks -1

#-------------------------------------------------------
# alice carl
#-------------------------------------------------------
#   a |  l |  i |  c |  e  |space|   c |  a |  r |  l
#   0 |  1 |  2 |  3 |  4  |  5  |   6 |  7 |  8 |  9  # positif
# -10 | -9 | -8 | -7 | -6  | -5  |  -4 | -3 | -2 | -1  # negatif
#-------------------------------------------------------

s = "alice carl"
print(s[-4:-1])       # car
print(s[-4:])         # carl
print(s[-10:-6])      # alic
print(s[-10:-1])      # alice car
print(s[-10:])        # alice carl
print(s[-10:0], 'tidak ada')

text = "email: hello_world@gmail.com"
x = '****'
y = 11
print(text[:y] + x + text[y + len(x):])
# jika anda ingin mengetahui fungsi len() kunjungi file_name: "Fungsi-Bawaan/fungsi_len.py"

