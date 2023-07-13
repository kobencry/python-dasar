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