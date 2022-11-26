# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.intersection

# fungsi intersection() mengembalikan satu set yang berisi kesamaan antara dua atau lebih set.

# Artinya: Set yang dikembalikan hanya berisi item yang ada di kedua set, atau
# di semua set jika perbandingan dilakukan dengan lebih dari dua set.

# Syntax
# set.intersection(set, set1, set2..dll)

# Nilai Parameter
# Parameter                     Deskripsi
# set1                          Dibutuhkan. Set untuk mencari item yang sama
# set2                          Opsional. Set lainnya untuk mencari item yang sama.
#                               Anda dapat membandingkan banyak set yang Anda suka.
#                               Pisahkan set dengan koma

# mengembalikan set yang berisi item yang ada di kedua set x, dan set y
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'eliot', 'fox'}
hasil = x.intersection(y)
print(hasil)    # {'eliot'}

# mengembalikan set yang berisi item yang ada di ketiga set x, y dan set z
x = {'alice', 'bert', 'carl'}
y = {'carl', 'daily', 'eliot'}
z = {'fox', 'geral', 'carl'}
hasil = x.intersection(y, z)
print(hasil)    # {'carl'}

# mengembalikan set yang berisi item yang ada di keempat set a, b, c, dan set d
a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
hasil = a.intersection(b, c, d)
print(hasil)    # {4}

# jika tidak ada item di set z maka akan menampilkan set kosong set()
x = {'alice', 'bert', 'carl'}
y = {'carl', 'daily', 'eliot'}
z = {'fox', 'geral', 'hello'}
hasil = x.intersection(y, z)
print(hasil)    # set()

# menggunakan operator bitwise &
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'eliot', 'fox'}
hasil = x & y
print(hasil)    # {'eliot'}

x = {'alice', 'bert', 'carl'}
y = {'carl', 'daily', 'eliot'}
z = {'fox', 'geral', 'carl'}
hasil = x & y & z
print(hasil)    # {'carl'}

x = {'alice', 'bert', 'carl'}
y = {'carl', 'daily', 'eliot'}
z = {'fox', 'geral', 'hello'}
hasil = x & y & z
print(hasil)    # set()

a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}
hasil = a & b & c & d
print(hasil)    # {4}

# jika anda ingin mengetahui tentang operator bitwise python kunjungi folder_name: "python-operator"
