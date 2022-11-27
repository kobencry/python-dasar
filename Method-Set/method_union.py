# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.union

# fungsi union() mengembalikan satu set yang berisi semua item dari set asli,
# dan semua item dari set yang ditentukan.
# anda dapat menentukan set sebanyak yang anda inginkan, dipisahkan dengan koma.
# itu tidak harus satu set, itu bisa berupa objek yang dapat diubah.
# Jika item ada di lebih dari satu set, hasilnya hanya akan berisi satu tampilan item.

# Syntax
# set.union(set1, set2..dst)

# Nilai Parameter
# Parameter                 Deskripsi
# set1                      Dibutuhkan. Iterable untuk disatukan
# set2                      Opsional. Iterable lainnya untuk disatukan.
#                           Anda dapat membandingkan iterables sebanyak yang Anda suka.
#                           Pisahkan setiap iterable dengan koma

# menggabungkan set yang berisi semua item set x dan set y, 
# item yang sama dari set x dan y hanya menampilkan satu item
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'carl', 'eliot'}
hasil = x.union(y)
print(hasil)    # {'hello', 'eliot', 'carl', 'alice'}

# menggabungkan lebih dari dua set item
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'carl', 'eliot'}
z = {'world', 'carl', 20}
hasil = x.union(y, z)
print(hasil)    # {'hello', 'eliot', 'alice', 20, 'carl', 'world'}

# menggunakan operator |
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot'}
y = {'hello', 'carl', 'eliot'}
hasil = x | y
print(hasil)    # {'carl', 'eliot', 'alice', 'hello'}

x = {'alice', 'carl', 'eliot'}
y = {'hello', 'carl', 'eliot'}
z = {'world', 'carl', 20}
hasil = x | y | z
print(hasil)    # {'carl', 'eliot', 20, 'world', 'alice', 'hello'}

# Ingat: kemungkinan hasil keluaran itemnya berbeda dengan anda, 
# karena tipe data set nilainya yang berubah-ubah

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
