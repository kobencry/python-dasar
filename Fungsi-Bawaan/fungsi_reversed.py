# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?#reversed

# fungsi reversed() mengembalikan objek iterator terbalik.

# Syntax
# reversed(urutan)

# Nilai Parameter
# Parameter                 Deskripsi
# urutan                    Dibutuhkan. Objek apa pun yang dapat diubah

listku = ['alice', 'carl', 'eliot']
tupleku = ('alice', 'carl', 'eliot')
print(reversed(listku))     # <list_reverseiterator object at 0x0000020A87A07670>
print(reversed(tupleku))    # <reversed object at 0x0000020A87A07670>

# menggunakan konstruktor list() dan tuple()
print(list(reversed(listku)))   # ['eliot', 'carl', 'alice']
print(tuple(reversed(tupleku))) # ('eliot', 'carl', 'alice')

# menggunakan looping for
iter_list = reversed(listku)
iter_tupl = reversed(tupleku)

for l in iter_list:
    print(l)
# eliot
# carl
# alice

for t in iter_tupl:
    print(t)
# eliot
# carl
# alice

# jika ingin memasukan data dalam tipe list dan tuple
listku = ['alice', 'carl', 'eliot']
tupleku = ('alice', 'carl', 'eliot')
iter_list = reversed(listku)
iter_tupl = reversed(tupleku)

listku = list()
for i in iter_list:
    listku.append(i)

tupleku = tuple()
for i in iter_tupl:
    tupleku += (i,)
print(listku)   # ['eliot', 'carl', 'alice']
print(tupleku)  # ('eliot', 'carl', 'alice')

# menggunakan fungsi join() pada "Method-String"
listku = ['alice', 'carl', 'eliot']
tupleku = ('alice', 'carl', 'eliot')
iter_list = reversed(listku)
iter_tupl = reversed(tupleku)

print(" ".join(iter_list))  # eliot carl alice
print(" ".join(iter_tupl))  # eliot carl alice

# jika anda ingin mengetahui tentang fungsi-string join() kunjungi folder_name: "Method-String/method_join.py"
# jika anda ingin mengetahui tentang fungsi-bawaan konstruktor list() kunjungi folder_name: "Fungsi-Bawaan/fungsi_list.py"
# jika anda ingin mengetahui tentang fungsi-bawaan konstruktor tuple() kunjungi folder_name: "Fungsi-Bawaan/fungsi_tuple.py"
