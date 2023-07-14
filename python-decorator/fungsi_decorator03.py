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