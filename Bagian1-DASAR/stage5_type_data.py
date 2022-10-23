# tipe data python
# dalam pemrograman, tipe data merupakan konsep penting.
# variabel dapat menyimpan data dari tipe yang berbeda,
# dan tipe yang berbeda dapat melakukan hal yang berbeda

# python memiliki tipe data bawaan secara default, berikut dalam kategori:
# Tipe Text:        str
# Tipe Numerik:     int, float, complex
# Tipe Urutan:      list, tuple, range
# Tipe Pemetaan:    dict
# Tipe Set:         set, frozenset
# Tipe Boolean:     bool
# Tipe Biner:       bytes, bytearray, memoryview
# Tipe Tidak ada:   NoneType

# Menadapatkan tipe data
# fungsi type() menampilkan tipe data objek apa pun
x = 5
print(type(x))


# Mengatur tipe data
# di python, tipe data diatur saat anda menetapkan nilai ke variabel

# tipe set
str_x = "hello world"
print(str_x, type(str_x))

# tipe int
int_x = 10
print(int_x, type(int_x))

# tipe float
float_x = 10.5
print(float_x, type(float_x))

# tipe complex
complex_x = 1j
print(complex_x, type(complex_x))

# tipe list
list_x = ['alice', 'carl', 'eliot']
print(list_x, type(list_x))

# tipe tuple
tuple_x = ('alice', 'carl', 'eliot')
print(tuple_x, type(tuple_x))

# tipe range
range_x = range(5)
print(range_x, type(range_x))

# tipe dict
dict_x = {'nama':'alice', 'usia':23}
print(dict_x, type(dict_x))

# tipe set
set_x = {'alice', 'carl', 'eliot'}
print(set_x, type(set_x))

# tipe frozenset
frozen_x = frozenset({'alice', 'carl', 'eliot'})
print(frozen_x, type(frozen_x))

# tipe boolean
true_x = True
false_x = False
print(true_x, type(true_x))
print(false_x, type(false_x))

# tipe biner
bytes_x = b"hello world"
bytes_y = bytes(10)
bytearray_x = bytearray(5)
bytmemory_x = memoryview(bytes(5))
print(bytes_x, type(bytes_x))
print(bytes_y, type(bytes_y))
print(bytearray_x, type(bytearray_x))
print(bytmemory_x, type(bytmemory_x))

# tipe tidak ada
none_x = None
print(none_x, type(none_x))

#===============================================================================
# mengatur tipe data tertentu
# jika anda ingin menentukan tipe data, anda dapat menggunakan fungsi konstraktor python:
# ada beberapa contoh ini berkaitan dengan casting tipe data. file_name "stage7_casting_type_data.py"

str_x = str("hello world")
str_y = str(100)
print(str_x)
print(str_y)

int_x = int("23")
int_y = int(15.500)
print(int_x)
print(int_y)

float_x = float('15')
float_y = float(15)
print(float_x)
print(float_y)

complex_x = complex(1.9999999999j)
print(complex_x)

list_x = list(('alice', 'carl', 'eliot'))
list_y = list(range(5))
print(list_x)
print(list_y)

tuple_x = tuple(['alice', 'carl', 'eliot'])
tuple_y = tuple('hello world')
print(tuple_x)
print(tuple_y, type(tuple_y))

dict_x = dict(nama='alice', usia=23)
print(dict_x)

set_str = set('hello world')
set_list = set(['alice', 'carl', 'eliot'])
set_tuple = set(('alice', 'carl', 'eliot'))
print(set_str)
print(set_list)
print(set_tuple)

true_x = bool(1)
false_y = bool(0)
print(true_x)
print(false_x)
