# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.symmetric_difference

# fungsi symmetric_difference() mengembalikan satu set yang berisi semua item dari kedua set,
# tapi bukan item yang ada di kedua set.
# Artinya: Set yang dikembalikan berisi campuran item yang tidak ada di kedua set.

# Syntax
# set.symmetric_difference(set)

# Nilai Parameter
# Parameter                 Deskripsi
# set                       Dibutuhkan. Set untuk memeriksa kecocokan

# mengembalikan set yang berisi semua item dari kedua set x dan set y.
# kecuali item yang ada atau sama di kedua set x dan set y
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
hasil = x.symmetric_difference(y)
print(hasil)    # {'world', 'carl', 'eliot', 'hello'}

x = {10, 20, 'hello'}
y = {10, 20, 'world'}
hasil = x.symmetric_difference(y)
print(hasil)    # {'hello', 'world'}

# menggunakan operator ^
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
hasil = x ^ y
print(hasil)    # {'hello', 'carl', 'eliot', 'world'}

# jika menggunakan operator ^ bisa membandingkan lebih dari 2 set
x = {10, 20, 'hello'}
y = {10, 20, 'world'}
z = {30, 40, 'abcde'}
hasil = x ^ y ^ z
print(hasil)    # {40, 'world', 'abcde', 'hello', 30}

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
