# operator keanggotaan/membership hanya bisa digunakan pada variable jenis
# sequence/iterable yang dapat menampung banyak nilai.
# fungsi dari operator ini adalah untuk memeriksa apakah suatu nilai merupakan
# salah satu anggota dari variabel berjenis sequence/iterable atau tidak.
# Kemudian akan menghasilkan nilai TRUE atau FALSE.

#-------------------------------------------
#  Simbol           Deskripsi
#-------------------------------------------
#   in         Menghasilkan nilai TRUE jika nilai yang ditentukan berada dalam objek tertentu
#  not in      Menghasilkan nilai TRUE jika nilai yang ditentukan tidak ada dalam objek tertentu

x = "alice carl eliot"

print("carl" in x)  # True
print("hello" in x) # False

print("carl" not in x)  # False
print("hello" not in x) # True
