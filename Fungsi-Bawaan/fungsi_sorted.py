# -- Fungsi bawaan python --

# https://docs.python.org/3/howto/sorting.html#operator-module-functions

# fungsi sorted() mengembalikan tipe list dalam daftar terurut dari objek iterable yang ditentukan.
# Anda dapat menentukan urutan naik/ascending atau turun/descending.
# String diurutkan berdasarkan abjad, dan angka diurutkan secara numerik.

# Catatan: Anda tidak dapat mengurutkan daftar yang berisi KEDUA nilai string DAN nilai numerik.

# Syntax
# sorted(iterable, key=key, reverse=reverse)

# Nilai Parameter
# Parameter                     Deskripsi
# iterable                      Dibutuhkan. Urutan untuk mengurutkan, list, dict, tuple dll.
# key                           Opsional. Fungsi untuk mengeksekusi untuk memutuskan pesanan. Standarnya adalah None
# reverse                       Opsional. Boolean. False akan mengurutkan menaik/ascending, True akan mengurutkan menurun/descending. Standarnya adalah False.

# contoh menggunakan string
alphabet = ('b', 'd', 'c', 'a', 'g', 'h', 'f', 'e')
x = sorted(alphabet)
print(x)    # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# contoh menggunakan int
numerik = [9, 2, 0, 1, 7, 3, 6, 5, 8, 4]
x = sorted(numerik)
print(x)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

alphanum = ('e', '3', 'a', '0', 'c', '4', 'd', '2', 'b', '1')
x = sorted(alphanum)
print(x)    # ['0', '1', '2', '3', '4', 'a', 'b', 'c', 'd', 'e']

# contoh menggunakan parameter reverse
x = ('hello', 'carl', 'Eliot', 'alice', 'World')
# mengurutkan secara ascending/menaik
print(sorted(x)) # ['Eliot', 'World', 'alice', 'carl', 'hello']
# mengurutkan secara descending/menurun
print(sorted(x, reverse=True))   # ['hello', 'carl', 'alice', 'World', 'Eliot']

# contoh menggunakan parameter key 
x = ('java', 'c++', 'javascript', 'ruby', 'python', 'golang', 'php')

def fungsi(e):
    return len(e)

print(sorted(x))                # ['c++', 'golang', 'java', 'javascript', 'php', 'python', 'ruby']
print(sorted(x, key=fungsi))    # ['c++', 'php', 'java', 'ruby', 'python', 'golang', 'javascript']
print(sorted(x, key=len))       # ['c++', 'php', 'java', 'ruby', 'python', 'golang', 'javascript']

# menggunakan parameter method string str.lower
s = "Hello World"
print(sorted(s))                    # [' ', 'H', 'W', 'd', 'e', 'l', 'l', 'l', 'o', 'o', 'r']
print(sorted(s, key=str.lower))     # [' ', 'd', 'e', 'H', 'l', 'l', 'l', 'o', 'o', 'r', 'W']

# menggunakan itemgetter attrgetter
data_tuple = [
        # nama, nilai, usia
        ('alice', 50, 18),
        ('tony', 75, 12),
        ('carl', 75, 20),
        ('eliot', 90, 22),
        ('early', 45, 23)
             ]
def sortir_nilai(item):  # urutkan berdasarkan nilai
    n = item[1]
    return n

x = sorted(data_tuple, key=sortir_nilai, reverse=True)
print(x)    # [('eliot', 90, 22), ('tony', 75, 12), ('carl', 75, 20), ('alice', 50, 18), ('early', 45, 23)]

data_tuple = [
        # nama, nilai, usia
        ('alice', 50, 18),
        ('tony', 75, 12),
        ('carl', 75, 20),
        ('eliot', 90, 22),
        ('early', 45, 23)
             ]

def sortir_usia(item):
    return item[2]

x = sorted(data_tuple, key=sortir_usia)
print(x)    # [('tony', 75, 12), ('alice', 50, 18), ('carl', 75, 20), ('eliot', 90, 22), ('early', 45, 23)]


class Data:
    def __init__(self, nama, nilai, usia):
        self.nama = nama
        self.nilai = nilai
        self.usia = usia
    
    def __repr__(self):
        return repr((self.nama, self.nilai, self.usia))

data_objek = [
        Data('eliot', 90, 22),
        Data('tony', 75, 12),
        Data('carl', 75, 20),
        Data('alice', 50, 18),
        Data('early', 45, 23)
        ]

# menggunakan fungsi anonim keyword 'lambda' ini setara dengan fungsi diatas
x = sorted(data_objek, key=lambda item: item.nilai, reverse=True)
print(x)    # [('eliot', 90, 22), ('tony', 75, 12), ('carl', 75, 20), ('alice', 50, 18), ('early', 45, 23)]

data_objek = [
        Data('eliot', 90, 22),
        Data('tony', 75, 12),
        Data('carl', 75, 20),
        Data('alice', 50, 18),
        Data('early', 45, 23)
        ]

x = sorted(data_objek, key=lambda item: item.usia)
print(x)    # [('tony', 75, 12), ('alice', 50, 18), ('carl', 75, 20), ('eliot', 90, 22), ('early', 45, 23)]

from operator import itemgetter, attrgetter
data_tuple = [
        ('eliot', 90, 22),
        ('tony', 75, 12),
        ('carl', 75, 20),
        ('alice', 50, 18),
        ('early', 45, 23)
        ]
x = sorted(data_tuple, key=itemgetter(1), reverse=True)
print(x)    # [('eliot', 90, 22), ('tony', 75, 12), ('carl', 75, 20), ('alice', 50, 18), ('early', 45, 23)]

data_objek = [
        # menggunakan class Data diatas
        Data('eliot', 90, 22),
        Data('tony', 75, 12),
        Data('carl', 75, 20),
        Data('alice', 50, 18),
        Data('early', 45, 23)
        ]
x = sorted(data_objek, key=attrgetter('usia'))
print(x)    # [('tony', 75, 12), ('alice', 50, 18), ('carl', 75, 20), ('eliot', 90, 22), ('early', 45, 23)]

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan repr() kunjungi folder_name: "Fungsi-Bawaan/fungsi_repr.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-string str.lower kunjungi folder_name: "Method-String/method_lower.py"
# jika ingin mempelajari lebih lanjut tentang itemgetter dan attrgetter kunjungi folder_name: "modul-operator"
