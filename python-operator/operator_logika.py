# operator logika digunakan untuk membandingkan dua operand atau dua nilai yang
# bertipe Boolean dan akan menghasilkan nilai Boolean yaitu TRUE atau FALSE.

#-------------------------------------------
#  Simbol         Deskripsi
#-------------------------------------------
#   and           mengembalikan True jika kedua statemen sama-sama benar
#   or            mengembalikan True jika salah satu statemen bernilai benar
#   not           menegasikan hasil. True menjadi False dan sebaliknya

x = True
y = False

# logika and
print(x and y)  # False
print(x and x)  # True

# logika or
print(x or y)  # True
print(x or x)  # True

# logika not
print(not x)    # False
print(not y)    # True
