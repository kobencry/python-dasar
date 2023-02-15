# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html#set

# fungsi set() membuat himpunan/set
# Objek set adalah tidak terurut, sehingga item akan muncul dalam urutan acak.
# jika ada item yang sama atau ganda dalam set(), maka item tersebut akan diabaikan

# Syntax
# set(iterable)

# Nilai Parameter
# Parameter                 Deskripsi
# iterable                  Opsional. Urutan, koleksi, atau objek iterator

# membuat set dengan konstruktor set()
listku = ['alice', 'carl', 'eliot']
setku = set(listku)
print(setku)
# Output:
# {'carl', 'eliot', 'alice'}

# Catatan: Output saya dan Anda akan berbeda karena set() tidak diurutkan

tupleku = ('alice', 'carl', 'eliot')
setku = set(tupleku)
print(setku)
# Output:
# {'alice', 'carl', 'eliot'}

# membuat set dengan comprehension
bilangan_genap = set(i for i in range(1,11) if i %2==0)
print(bilangan_genap)
# Output:
# {2, 4, 6, 8, 10}

nama =['alice', 'carl', 'alice', 'eliot', 'carl']
data_unik = set(i for i in nama)
print(data_unik)
# Output:
# {'carl', 'alice', 'eliot'}

# jika anda ingin mengetahui tentang koleksi-set kunjungi folder_name: "Method-Set"