# memodifikasi tuple python
# Ingat: Tuple tidak dapat diubah, artinya Anda tidak dapat mengubah,
# menambah, atau menghapus item setelah tupel dibuat.
# Tetapi ada beberapa solusi.

# mengubah item tuple menggunakan indeks
# mengkonversi tuple menjadi list. 
# mengubah list, dan mengubah list kembali menjadi tuple.
tupleku = ('hello', 'world')

# ubah tuple menjadi list
listku = list(tupleku)
listku[0] = 'war'
tupleku = tuple(listku)
print(tupleku)  # ('war', 'world')

# menambahkan item tuple mengunakan fungsi append() list
tupleku = ('alice', 'carl')
x = list(tupleku)
x.append('eliot')
tupleku = tuple(x)
print(tupleku)  # ('alice', 'carl', 'eliot')

# Catatan: Saat membuat tuple dengan hanya satu item, 
# ingatlah untuk menyertakan koma setelah item, 
# jika tidak maka tidak akan teridentifikasi sebagai tuple.

# menambahkan item tuple menggunakan operator assignment/penugasan (+=)
tupleku = ('alice', 'carl')
tupleku += ('eliot', )
print(tupleku)  # ('alice', 'carl', 'eliot')

# menggabunggkan item tuple menggunakan operator tambah +
tuple1 = ('hello', 'world')
tuple2 = (25, True, None)
tuple3 = tuple1 + tuple2
print(tuple3)   # ('hello', 'world', 25, True, None)

# melipatgandakan item tuple menggunakan operator kali *
tupleku = ('hello', 'world')
x = tupleku * 2
print(x)    # ('hello', 'world', 'hello', 'world')

# menghapus item tuple mengunakan fungsi remove() list
tupleku = ('alice', 'carl', 'eliot')
x = list(tupleku)
x.remove('eliot')
tupleku = tuple(x)
print(tupleku)  # ('alice', 'carl')

# menghapus item tuple menggunakan keyword python 'del'
# menghapus sepenuhnya item tuple dan variabel x 
# akan menampilkan error runtime "NameError:"
x = ('alice', 'carl', 'eliot')
print(x)
del x
print(x)

# jika anda ingin mengetahui tentang python-operator kunjungi folder_name: "python-operator"
# jika anda ingin mengetahui tentang Method-Tuple kunjungi folder_name: "Method-Tuple"
