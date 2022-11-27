# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.symmetric_difference_update

# fungsi symmetric_difference_update() memperbarui set asli dengan menghapus 
# item yang ada atau sama di kedua set, dan memasukkan item lainnya.

# Syntax
# set.symmetric_difference_update(set)

# Nilai Parameter
# Parameter                     Deskripsi
# set                           Dibutuhkan. Set untuk memeriksa kecocokan

# menghapus item yang ada atau sama di kedua set,
# dan masukkan item yang tidak ada dikedua set x dan set y.
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'carl'}
x.symmetric_difference_update(y)
print(x)    # {'alice', 'eliot', 'hello', 'world'}

x = {10, 20, 'hello'}
y = {10, 20, 'world'}
x.symmetric_difference_update(y)
print(x)    # {'hello', 'world'}

# menggunakan operator ^=
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'carl'}
x ^= y
print(x)    # {'world', 'alice', 'hello', 'eliot'}

x = {10, 20, 'hello'}
y = {10, 20, 'world'}
x ^= y
print(x)    # {'hello', 'world'}

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
