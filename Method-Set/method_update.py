# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.update

# fungsi update() memperbarui set saat ini, dengan menambahkan item dari set lain (atau iterable lainnya).
# Jika item ada di kedua set, hanya satu tampilan item ini yang akan ada di set yang diperbarui.

# Syntax
# set.update(set)

# Nilai Parameter
# Parameter                 Deskripsi
# set                       Dibutuhkan. Masukkan iterable ke dalam set saat ini

# menambahkan item dari set y ke set x
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'carl'}
x.update(y)
print(x)    # {'eliot', 'carl', 'world', 'alice', 'hello'}

x = {10, 20, 'hello'}
y = {10, 20, 'world'}
x.update(y)
print(x)    # {20, 'hello', 10, 'world'}

# menggunakan operator |=
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'world', 'carl'}
x |= y
print(x)    # {'world', 'carl', 'hello', 'alice', 'eliot'}

x = {10, 20, 'hello'}
y = {10, 20, 'world'}
x |= y
print(x)    # {10, 20, 'world', 'hello'}

# Ingat: kemungkinan hasil keluaran itemnya berbeda dengan anda, 
# karena tipe data set nilainya yang berubah-ubah

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
