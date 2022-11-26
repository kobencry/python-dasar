# -- Method Set --

# https://docs.python.org/3/library/stdtypes.html?#frozenset.issuperset 

# fungsi issuperset() mengembalikan nilai boolean True jika semua item dalam set yang ditentukan ada di set asli, 
# jika tidak maka mengembalikan nilai boolean False.

# Syntax
# set.issuperset(set)

# Nilai Parameter
# Parameter                     Deskripsi
# set                           Dibutuhkan. Set untuk mencari item yang sama

# superset adalah kebalikan dari subset. 
# set x dianggap sebagai superset dari set y lain.
# jika x mengandung setiap elemen dari y

# mengembalikan True jika semua set item y ada di set x.
x = {'alice', 'carl', 'eliot', 'geral', 'hello'}
y = {'alice', 'carl', 'eliot'}
hasil = x.issuperset(y)
print(hasil)    # True

# mengembalikan False jika semua set item y tidak ada di set x. 
x = {'alice', 'carl', 'eliot'}
y = {'geral', 'hello', 'alice', 'carl', 'eliot'}
hasil = x.issuperset(y)
print(hasil)    # False

# sebuah set juga dianggap sebagai superset dari dirinya sendiri
x = {'alice', 'carl', 'eliot'}
hasil = x.issuperset(x)
print(hasil)    # True

# menggunakan operator comparison/perbandingan >=
# kode ini setara dengan yang diatas
x = {'alice', 'carl', 'eliot', 'geral', 'hello'}
y = {'alice', 'carl', 'eliot'}
hasil = x >= y
print(hasil)    # True

x = {'alice', 'carl', 'eliot'}
y = {'geral', 'hello', 'alice', 'carl', 'eliot'}
hasil = x >= y
print(hasil)    # False

# sebuah set juga dianggap sebagai superset dari dirinya sendiri
x = {'alice', 'carl', 'eliot'}
hasil = x >= x
print(hasil)    # True

# menggunakan operator comparison/perbandingan >
# Catatan: operator > adalah satu-satunya cara untuk menguji
# apakah satu set adalah superset yang tepat.
x = {'alice', 'carl', 'eliot', 'geral', 'hello'}
y = {'alice', 'carl', 'eliot'}
hasil = x > y
print(hasil)    # True

x = {'alice', 'carl', 'eliot'}
y = {'geral', 'hello', 'alice', 'carl', 'eliot'}
hasil = x > y
print(hasil)    # False

# Suatu set bukanlah superset yang tepat dari dirinya sendiri
x = {'alice', 'carl', 'eliot'}
hasil = x > x
print(hasil)    # False

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
