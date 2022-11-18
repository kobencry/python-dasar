# -- Fungsi bawaan python --

# https://docs.python.org/3/library/stdtypes.html?#callable

# fungsi callable() mengembalikan nilai boolean True jika objek yang ditentukan
# dapat dipanggil, jika tidak maka akan mengembalikan nilai boolean False.

# Syntax
# callable(objek)

# Nilai Parameter
# Parameter             Deskripsi
# objek                 Objek yang ingin Anda uji apakah dapat dipanggil atau tidak.

# contoh menggunakan variabel
x = 5
print(callable(x))  # False

# contoh menggunakan fungsi
def fungsi():
    return "hello world"
print(callable(fungsi)) # True

# contoh menggunakan Fungsi-Bawaan python len()
jumlah = len('hello world')
print(callable(jumlah))  # False

# contoh menggunakan Fungsi-Bawaan python range()
x = range(10)
print(callable(x))  # False

# contoh menggunakan class dan magic method python __call__ 

class A:
    def __call__(self):
        return "hello world"

    def fungsi(self):
        return "hello world"

objek_a = A()
print(callable(objek_a))            # True
print(callable(objek_a.fungsi))     # True
print(callable(objek_a.fungsi()))   # False

# contoh menggunakan class tanpa magic method __call__
class  B:
    def fungsi(self):
        return "hello world"

objek_b = B()
print(callable(objek_b))    # False
