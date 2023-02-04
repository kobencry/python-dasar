# -- Fungsi bawaan python --
# https://docs.python.org/3/library/functions.html#iter

# fungsi iter() mengembalikan objek iterator
# Iterator adalah suatu objek yang memiliki metode next() yang mengembalikan elemen-elemen dari iterable secara berurutan.
# Setiap iterator memiliki posisi yang berbeda, dan jika posisi sudah berada pada akhir iterable, 
# metode next() akan mengeluarkan exception StopIteration.

# Jadi, untuk membuat iterator dari suatu iterable, kita memanggil metode iter() pada objek iterable tersebut.
# Kemudian, kita dapat menggunakan metode next() pada objek iterator untuk mengakses elemen-elemen dari iterable.

# Syntax
# iter(object, sentinel)

# Nilai Parameter
# Parameter             Deskripsi
# object                Dibutuhkan. Sebuah objek iterable
# sentinel              Opsional. Jika objek adalah objek yang dapat dipanggil, 
#                       iterasi akan berhenti ketika nilai yang dikembalikan sama dengan sentinel


listku = ['alice', 'carl', 'eliot']
obj_iter = iter(listku)
print(obj_iter) # <list_iterator object at 0x00000237BDC28910>

# untuk menampilkan objek iterator dari iterable
print(next(obj_iter))   # alice
print(next(obj_iter))   # carl
print(next(obj_iter))   # eliot

# menggunakan parameter sentinel
