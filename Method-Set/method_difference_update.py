# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.difference_update

# fungsi difference_update() menghapus item yang ada di kedua set.
# fungsi difference_update() ini berbeda dengan fungsi difference(),
# karena fungsi difference() mengembalikan set baru, tanpa item yang tidak 
# diinginkan, dan difference_update() menghapus item yang tidak diinginkan dari set asli.

# Syntax
# set.difference_update(set)
# set.difference_update(set1, set2)

# Nilai Parameter
# Parameter                 Deskripsi
# set                       Dibutuhkan. Set untuk memeriksa perbedaan

# menghapus item set yang ada di set x dan y.
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
x.difference_update(y)
print(x)
# jalankan kode diatas berulang-ulang maka akan menampilkan hasil 
# nilai yang keluarannya berubah-ubah.
# outputnya >>> {'eliot', 'carl'} atau {'carl', 'eliot'}

# balikan contoh yang diatas
# menghapus item set yang ada di set x dan y.
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
y.difference_update(x)
print(y)
# jalankan kode diatas berulang-ulang maka akan menampilkan hasil 
# nilai yang keluarannya berubah-ubah.
# outputnya >>> {'world', 'hello'} atau {'world', 'hello'}

# menggunakan operator assigment/penugasan -=
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
x -= y
print(x)
# jalankan kode diatas berulang-ulang maka akan menampilkan hasil 
# nilai yang keluarannya berubah-ubah.
# outputnya >>> {'eliot', 'carl'} atau {'carl', 'eliot'}

x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'alice'}
y -= x
print(y)
# jalankan kode diatas berulang-ulang maka akan menampilkan hasil 
# nilai yang keluarannya berubah-ubah.
# outputnya >>> {'world', 'hello'} atau {'world', 'hello'}

# menggunakan lebih dari dua set
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'eliot', 'world'}
z = {'bert', 'geral', 'carl'}
x.difference_update(y, z)
print(x)    # {'alice'}

x = {'alice', 'carl', 'eliot'}
y = {'hello', 'eliot', 'world'}
z = {'bert', 'geral', 'carl'}
x -= y
print(x)    # {'carl', 'alice'}
x -= z
print(x)    # {'alice'}

# jika anda ingin mengetahui tentang operator assigment python kunjungi folder_name: "python-operator"
