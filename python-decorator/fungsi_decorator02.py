# Nested Functions(fungsi yang didefinisikan di dalam fungsi lain),
# di sisi lain, adalah fungsi yang didefinisikan di dalam fungsi lain. 
# Nested Functions digunakan untuk membatasi cakupan fungsi dalam konteks tertentu dan
# menyediakan cara untuk mengorganisir dan mengelompokkan kode yang terkait secara logis. 
# Nested Functions tidak secara khusus terkait dengan mengambil fungsi lain sebagai argumen.

# Berikut adalah sintaks umum untuk mendefinisikan fungsi dekorator
# mengunakan konsep Nested Functions:

# contoh 1
def func_luar():
    def func_dalam():
        return "hello world"
    return func_dalam

hasil = func_luar()
hasil = hasil()
print(hasil)
# Output:
# hello world

# contoh 2
def func_luar():
    def func_dalam():
        return "hello alice"
    return func_dalam()

hasil = func_luar()
print(hasil)
# Output:
# hello alice

# Berikut beberapa contoh tambahan:
#----------------------------------
# Contoh fungsi dengan argumen/parameter
def matematika(x):
    def tambah(y):
        return x + y
    return tambah

func_tambah = matematika(5)
hasil = func_tambah(3)
print(hasil)
# Output:
# 8