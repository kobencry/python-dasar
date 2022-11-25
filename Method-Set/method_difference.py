# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.difference

# fungsi difference() mengembalikan satu set yang berisi perbedaan antara dua set.

# Artinya: Set yang dikembalikan berisi item yang hanya ada di set pertama,
# dan tidak ada di kedua set

# Syntax
# set.difference(set)
# set.difference(set1, set2)

# Nilai Parameter
# Parameter                 Deskripsi
# set                       Dibutuhkan. Set untuk memeriksa perbedaan

# mengembalikan set yang berisi item yang hanya ada di set x, dan tidak ada di set y
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
z = x.difference(y)
print(z)
# jalankan kode diatas berulang-ulang maka akan menampilkan hasil 
# nilai yang keluarannya berubah-ubah.
# outputnya >>> {'eliot', 'carl'} atau {'carl', 'eliot'}

# balikan contoh yang diatas
# mengembalikan set yang berisi item yang hanya ada di set y, dan tidak ada di set x
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
z = y.difference(x)
print(z)
# jalankan kode diatas berulang-ulang maka akan menampilkan hasil 
# nilai yang keluarannya berubah-ubah.
# outputnya >>> {'world', 'hello'} atau {'world', 'hello'}

# menggunakan operator - 
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
z = x - y
print(z)
# jalankan kode diatas berulang-ulang maka akan menampilkan hasil 
# nilai yang keluarannya berubah-ubah.
# outputnya >>> {'eliot', 'carl'} atau {'carl', 'eliot'}

x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
z = y - x
print(z)
# jalankan kode diatas berulang-ulang maka akan menampilkan hasil 
# nilai yang keluarannya berubah-ubah.
# outputnya >>> {'world', 'hello'} atau {'world', 'hello'}

# menggunakan lebih dari dua set
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'eliot', 'world'}
z = {'bert', 'geral', 'carl'}
print(x.difference(y, z))   # {'alice'}
print(x - y - z)            # {'alice'}

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
