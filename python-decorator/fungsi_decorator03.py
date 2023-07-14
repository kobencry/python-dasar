# Dekorator dalam Python didefinisikan menggunakan simbol "@" yang 
# diikuti oleh nama fungsi dekorator di atas definisi fungsi yang akan didekorasi. 
# Ini memungkinkan kita untuk menerapkan dekorasi secara langsung pada fungsi 
# yang akan didekorasi tanpa perlu menetapkan kembali hasil dekorasi ke variabel terpisah.

# Berikut ini adalah contoh kode yang menunjukkan penggunaan dekorator 
# menggunakan simbol "@" diikuti oleh nama fungsi dekorator di atas definisi fungsi yang akan didekorasi:

# Contoh 1
def decorator(func):
    def wrapper():
        print("-- sebelum --")
        func()
        print("-- setelah --")
    return wrapper

@decorator
def hello():
    print("Hello World")

hello()
# Output:
# -- sebelum --
# Hello World
# -- setelah --

# Contoh 2
def func_luar(func_lain):
    def func_dalam():
        print("fungsi decorator")
        func_lain()
    return func_dalam

@func_luar
def hello():
    print("fungsi hello")
hello()
# Output:
# fungsi decorator
# fungsi hello

# Berikut beberapa contoh tambahan:
#----------------------------------
# Contoh fungsi dengan argumen *args atau **kwargs
def main(func):
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
    return wrapper

@main
def getNama(nama):
    print(f"hello {nama}")

getNama("Alice")
# Output:
# hello Alice

# menggunakan argumen list dan dictionary
getNama(['alice', 'carl', 'eliot'])
# Output:
# hello ['alice', 'carl', 'eliot']

@main
def data_mahasiswa(nama, usia, email):
    print(f"nama:{nama}, usia:{usia}, email:{email}")

data_mahasiswa(nama='alice', usia=20, email='alice@gmail.com')
# Output:
# nama:alice, usia:20, email:alice@gmail.com