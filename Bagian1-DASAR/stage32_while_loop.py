# definisi looping/perulangan
# Secara umum, looping atau perulangan pada Python adalah instruksi kode program 
# yang dieksekusi berulang kali. 
# Fungsinya untuk memerintah komputer melakukan sesuatu secara berulang-ulang 
# dengan jumlah tertentu selama sebuah kondisi yang telah ditentukan masih terpenuhi.

# while loop adalah perulangan uncountable atau perulangan yang jumlah proses 
# pengulangannya tidak ditentukan. 
# Ia akan menjalankan baris kode di dalam blok kodenya secara terus menerus 
# selama masih memenuhi ekspresi yang sudah ditentukan sebelumnya, 
# yang berarti ia akan terus mengulang selama kondisi bernilai True.

# Syntax
# while <kondisi>:
#     <expresi>

# <kondisi> dapat berupa operator matematika, logika fungsi atau nilai boolean
# <expresi> sebuah pernyataan apapun yang akan dieksekusi berulang kali selama <kondisi> bernilai True.

# menggunakan operator comparison/perbandingan
x = 0
while x < 5:
    # print(x)  # 0 1 2 3 4 
    # x = x + 1
    # kode ini setara dengan yang diatas
    x += 1
    print(x)    # 1 2 3 4 5
#1. apakah 0 lebih kecil dari 5, True
#2. kode <expresi> <x = x + 1> 0 + 1 = 1  print(x)
#3. apakah 1 lebih kecil dari 5, True
#4. kode <expresi> <x = x + 1> 1 + 1 = 2  print(x)
#6. apakah 2 lebih kecil dari 5, True
#7. ... dst(dan seterusnya sampai, kondisi bernilai False)
#8. apakah 5 lebih kecil dari 5, False
# looping berhenti kode <expresi> tidak dijalankan

# menggunakan fungsi bawaan python len() 
listku = ['alice', 'carl', 'eliot']
while len(listku):
    x = listku.pop() # data dihapus
    print(f"nama {x} telah dihapus")
#1. apakah ada data di variabel listku, True
#2. kode <expresi> listku.pop() 'eliot' dihapus
#3. apakah ada data di variabel listku, True
#4. kode <expresi> listku.pop() 'carl' dihapus
#5. apakah ada data di variabel listku, True
#6. kode <expresi> listku.pop() 'alice', dihapus
#7. apakah ada data di variabel listku, False
# looping berhenti kode <expresi> tidak dijalankan

x = ['alice', 'carl' 'eliot']
y = []
print(bool(x))  # True
print(bool(y))  # False

# ------ jenis syntax kode while loop -------

# while loop bersarang
# sebuah while loop dapat dimuat di dalam while loop lain.
# while <kondisi_1>:
#     <expresi_1>
#     <expresi_2>...dst
#     
#     while <kondisi_2>:
#         <expresi_1>
#         <expresi_2>...dst

# while loop di dalam statement if/elif/else
# whileloop dapat disarangkan di dalam statement if/elif/else
# if <kondisi>:
#     <expresi_if>
#     while <kondisi>:
#         <expresi>
#         <expresi>
# else:
#     while <kondisi>:
#         <expresi>
#         <expresi>
#     <expresi_else>
# 

# atau while loop berisi statement if/elif/else
# while <kondisi>:
#     if <kondisi>:
#         <expresi>
# 
#     elif <kondisi>:
#         <expresi>
#     else:
#         <expresi>
# 
#     if <kondisi>:
#         <expresi>

# Faktanya, semua struktur kontrol Python dapat digabungkan satu sama lain sejauh yang Anda butuhkan.

# jika anda ingin mengetahui tentang while loop dengan berbagai statement kunjungi folder_name: "python-looping"
# jika anda ingin mengetahui tentang operator comparison kunjungi folder_name: "python-operator"
