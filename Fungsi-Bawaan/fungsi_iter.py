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

# Ada sedikit terminologi yang membingungkan untuk diluruskan: iterable tidak sama dengan iterator.
# Objek iterator menyimpan keadaan iterasinya saat ini dan "yield" masing-masing anggotanya secara berurutan,
# sesuai permintaan melalui berikutnya, hingga habis. 
# Seperti yang telah kita lihat, generator adalah contoh dari iterator.
# Kita sekarang harus memahami bahwa setiap iterator adalah iterable, tetapi tidak setiap iterable adalah iterator.
# Iterable adalah objek yang dapat diulang tetapi tidak harus memiliki semua mesin iterator. 
# Misalnya, urutan (list, tupel, dan string) dan wadah lain (dictionaty dan set)
# tidak melacak status iterasinya sendiri. 
# Dengan demikian Anda tidak dapat memanggil salah satu dari ini secara langsung

# menggunakan argumen sentinel
# menghitung berapa jumlah fungsi yang dipanggil
def tambah() -> 0:
    tambah.__annotations__['return'] += 1
    return tambah.__annotations__['return']

iterator = iter(lambda: tambah() * 1, 4)
for i in iterator:
    print(f"fungsi {tambah.__name__}() telah dipanggil {i} kali")
# Output:
# fungsi tambah() telah dipanggil 1 kali
# fungsi tambah() telah dipanggil 2 kali
# fungsi tambah() telah dipanggil 3 kali

# membaca karakter string sampai ketemu 
s = "hello world alice \ncarl eliot"
mulai = 0
akhir = 1
def karakter(s):
    return s[mulai: mulai + akhir]

for i in iter(lambda: karakter(s), '\n'):
    print(i, end='')
    mulai += akhir
# Output:
# hello world alice

print()

# membaca inputan dari user, sampai user memasukan 'exit'
def user_input():
    iterator = iter(lambda: input('>>> '), 'exit')
    for i in iterator:
        print(i)
    else:
        print('[!] iterator berhenti')
user_input()