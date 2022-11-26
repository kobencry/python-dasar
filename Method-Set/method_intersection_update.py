# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.intersection_update

# fungsi intersection_update() menghapus item yang tidak ada di kedua set 
# (atau di semua set jika perbandingan dilakukan antara lebih dari dua set).
# fungsi intersection_update() ini berbeda dengan fungsi intersection(),
# karena intersection() mengembalikan set baru, tanpa item yang tidak diinginkan,
# dan intersection_update() menghapus item yang tidak diinginkan dari set asli.

# Syntax
# set.intersection(set, set1, set2..dll)

# Nilai Parameter
# Parameter                  Deskripsi
# set1                       Dibutuhkan. Set untuk mencari item yang sama
# set2                       Opsional. Set lainnya untuk mencari item yang sama.
#                            Anda dapat membandingkan banyak set yang Anda suka.
#                            Pisahkan set dengan koma

# menghapus item yang tidak ada di keduanya x dan y
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'eliot', 'fox'}
x.intersection_update(y)
print(x)    # {'eliot'}

# menghapus item yang tidak ada di ketiganya x, y dan z
x = {'alice', 'bert', 'carl'}
y = {'carl', 'daily', 'eliot'}
z = {'fox', 'geral', 'carl'}
x.intersection_update(y, z)
print(x)    # {'carl'}

# menghapus item yang tidak ada di keempatnya a, b, c dan d
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
a.intersection_update(b, c, d)
print(a)    # {4}

# jika tidak ada item di set z maka akan menampilkan set kosong set()
x = {'alice', 'bert', 'carl'}
y = {'carl', 'daily', 'eliot'}
z = {'fox', 'geral', 'hello'}
x.intersection_update(y, z)
print(x)    # set()

# menggunakan operator assigment/penugasan &=
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'eliot', 'fox'}
x &= y
print(x)    # {'eliot'}

x = {'alice', 'bert', 'carl'}
y = {'carl', 'daily', 'eliot'}
z = {'fox', 'geral', 'carl'}
x &= y
x &= z
print(x)    # {'carl'}

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
a &= b
a &= c
a &= d
print(a)    # {4}

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
