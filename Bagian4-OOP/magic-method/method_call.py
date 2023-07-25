# Dalam Python, Magic method __call__ adalah Method khusus dalam Python 
# yang digunakan untuk membuat objek dapat dipanggil seperti sebuah fungsi. 
# Ketika sebuah objek memiliki Method __call__ yang diimplementasikan, 
# objek tersebut dapat dianggap sebagai fungsi dan dapat dipanggil menggunakan tanda kurung ().

# Deskripsi:
# Method __call__ memungkinkan kita untuk mendefinisikan perilaku ketika objek tersebut dipanggil.
# Dengan mengimplementasikan Method ini, kita dapat mengubah objek kita agar dapat berperilaku seperti fungsi, 
# sehingga dapat menerima argumen dan mengembalikan hasil seperti fungsi pada umumnya.

# Syntax:
# def __call__(self, *args, **kwargs):
    # implementasi perilaku ketika objek dipanggil

# Parameter
# self: Merujuk pada objek saat ini.
# *args: Berisi argumen posisi yang diteruskan saat objek dipanggil.
# **kwargs: Berisi argumen kata kunci yang diteruskan saat objek dipanggil.


# Berikut adalah contoh sederhana penggunaan metode __call__ dalam sebuah kelas:
class A:
    def __call__(self):
        return "hello world"

# membuat objek A
x = A()
y = A()
print(x())
print(y())
# Output:
# hello world
# hello world

# menjumlahkan dari setiap bilangan 
class Tambah:
    def __init__(self):
        self.total = 0
    
    def __call__(self, *args):
        for i in args:
            self.total += i
        return self.total

# membuat objek dan memanggilnya
tambah = Tambah()
print(tambah(1, 2)) # 1 + 2 = 3
# Output:
# 3

print(tambah(5, 5)) # 3 + 5 + 5 = 13
# Output:
# 13

print(tambah(10, 20, 30))   # 13 + 10 + 20 + 30 = 73
# Output:
# 73

# contoh menggunakan argumen *args dan **kwargs
class A:
    def __init__(self):
        print('Objek dibuat')
    
    def __call__(self, *args, **kwargs):
        print('Objek dipanggil dengan nilai argumen:', args, kwargs)

# Membuat objek dan memanggilnya
obj = A()
obj(1, 2, a=3, b=4)
# Output:
# Objek dibuat
# Objek dipanggil dengan nilai argumen: (1, 2) {'a': 3, 'b': 4}

# Berikut beberapa contoh tambahan menggunakan fungsi decorator:
import time

class root:
    def __init__(self, func):
        self.func = func
        self.jumlah = 0

    def __call__(self, *args, **kwargs):
        self.jumlah += 1
        print(f"\rMemanggil fungsi {self.func.__name__}: {self.jumlah}", end='', flush=True)
        rv = self.func(*args, **kwargs)
        return rv

@root
def fibonaci(n):
    if n < 2:
        return n
    else:
        #print(n)
        return fibonaci(n - 1) + fibonaci(n - 2)

start = time.perf_counter()
fibonaci(20)
end = time.perf_counter()

result = end - start
print(f"\ntimes: {result} second")
# Output:
# Memanggil fungsi fibonaci: 21891
# times: 8.8199903 second