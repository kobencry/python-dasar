# menguji kecepatan formatting 
# f-string lebih cepat dari formatting % dan str.format(). 
# seperti yang sudah anda lihat, f-String adalah ekspresi yang dievaluasi 
# saat runtime daripada nilai konstan. Berikut Kutipan dari dokumen:

# "F-string menyediakan cara untuk menanamkan ekspresi di dalam string 
# literal, menggunakan sintaks minimal. 
# Perlu dicatat bahwa F-string benar-benar ekspresi yang dievaluasi saat 
# runtime, bukan nilai konstan. 
# Dalam kode sumber Python, f-string adalah string literal, 
# diawali dengan f, yang berisi ekspresi di dalam kurung kurawal.
# Ekspresi diganti dengan nilai-nilai mereka.
# sumber https://peps.python.org/pep-0498/#abstract

# Saat runtime, ekspresi di dalam kurung kurawal dievaluasi dalam cakupannya 
# sendiri dan kemudian disatukan dengan bagian literal string dari F-string. 
# String yang dihasilkan kemudian dikembalikan.
# Hanya itu yang diperlukan.

# Berikut adalah perbandingan kecepatan

import timeit
# jika ingin mempelajari lebih lanjut tentang modul timeit kunjungi folder_name: "modul-timeit"

# formatting persen % 
print(timeit.timeit("""x = "alice"; y = 23; 'nama: %s  usia: %s' % (x, y)""", number=100000))
# 0.09190259990282357

# formatting str.format()
print(timeit.timeit("""nama = "alice"; usia = 23; 'nama: {} usia: {}'.format(nama, usia)""", number=100000))
# 0.11462850007228553

# formatting f-string
print(timeit.timeit("""nama = "alice"; usia = 23; 'nama: {nama} usia: {usia}'""", number=100000))
# 0.009169099968858063

# lihat selisihnya formatting persen%, str.format() dan f-string.
# jadi gunakanlah f-string
