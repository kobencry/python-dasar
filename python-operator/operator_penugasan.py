# operator penugasan/assignment adalah operator untuk memasukkan suatu nilai ke dalam variabel.
# Dalam Bahasa Pemrograman Python, Operator Assignment menggunakan tanda sama dengan (=). 
# Misal variabel x = 5, artinya variabel x telah diberi tugas untuk menyimpan angka 5.

#-------------------------------------------
# Simbol         Deskripsi
#-------------------------------------------
#  =             pengisian
#  +=            penjumlahan
#  -=            pengurangan
#  *=            perkalian
#  /=            pembagian
#  %=            sisa bagi
# **=            pemangkatan

x = 5
x += 1
print(x)    # 6
# kode dibawah ini setara dengan di atas
x = 5
x = x + 1
print(x)    # 6


x = 5
x -= 2
print(x)    # 3
# kode dibawah ini setara dengan di atas
x = 5
x = x - 2
print(x)    # 3


x = 5
x *= 3
print(x)    # 15
# kode dibawah ini setara dengan di atas
x = 5
x = x * 3
print(x)    # 15


x = 10
x /= 4
print(x)    # 2.5
# kode dibawah ini setara dengan di atas
x = 10
x = 10 / 4
print(x)    # 2.5

x = 10
x %= 3
print(x)    # 1
# kode dibawah ini setara dengan di atas
x = 10
x = x % 3
print(x)    # 1

x = 2
x **= 3
print(x)    # 8
# kode dibawah ini setara dengan di atas
x = 2
x = x ** 3
print(x)    # 8
