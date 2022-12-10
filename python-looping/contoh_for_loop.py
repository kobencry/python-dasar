# Berikut ini beberapa contoh kode nested for loop di bahasa Python:

# 1. Mencetak pola angka segitiga

for x in range(1, 6):
  for y in range(1, x + 1):
    print(y, end='')
  print()
# 1
# 12
# 123
# 1234
# 12345

#=============================================================================

for i in range(1, 6):
  for x in range(1, 6 - i):
    print(" ", end="")
  for y in range(1, i + 1):
    print(y, end="")
  for z in range(1, i):
    print(z, end="")
  print()

#     1
#    121
#   12321
#  1234321
# 123454321

#=============================================================================

# 2. Mencetak pola angka checkerboard 
for x in range(1, 5):   # mencetak mulai dari 1 - 4
    for y in range(1, 5):
        print(y + x, end='')
    print() # kode ini setara dengan karakter '\n'(newline) atau print('')
# 2345
# 3456
# 4567
# 5678

# Penjelasan kode di atas:
# Baris pertama kita menggunakan for loop untuk mengiterasi variabel x dari 1 hingga 4 (tidak termasuk 5).
# Di dalam for loop pertama, kita juga menggunakan for loop kedua untuk mengiterasi variabel y dari 1 hingga 4 (tidak termasuk 5).
# Di dalam for loop kedua, kita mencetak nilai y + x dan menambahkan y dengan 1 untuk memulai iterasi selanjutnya.
# Setelah for loop kedua selesai, kita mencetak baris baru (enter) dengan menggunakan perintah print().
# Setelah for loop pertama selesai, kita akan mencetak pola angka checkerboard sesuai dengan keinginan kita.
# Dengan menggunakan for loop seperti di atas, kita dapat dengan mudah mencetak pola angka checkerboard di bahasa Python.
