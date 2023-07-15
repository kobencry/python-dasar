# Untuk menggunakan dua decorator atau lebih secara bersamaan dengan menggunakan sintaks @,
# Anda dapat menerapkan decorator-decorator tersebut secara berurutan di atas definisi
# fungsi yang akan didekorasi.

# Berikut ini adalah contoh penggunaan dua decorator sekaligus:
# Contoh 1
def dekorator1(func):
    def wrapper(*args, **kwargs):
        print("Dekorator 1: Sebelum eksekusi fungsi")
        func(*args, **kwargs)
        print("Dekorator 1: Setelah eksekusi fungsi")
    return wrapper

def dekorator2(func):
    def wrapper(*args, **kwargs):
        print("Dekorator 2: Sebelum eksekusi fungsi")
        func(*args, **kwargs)
        print("Dekorator 2: Setelah eksekusi fungsi")
    return wrapper

# Ingat Anda bisa meletakan dekorator tersebut dengan terurut atau pun tidak terurut
@dekorator1
@dekorator2
def tambah(x, y):
    print(x + y)

tambah(5, 5)
# Output:
# Dekorator 1: Sebelum eksekusi fungsi
# Dekorator 2: Sebelum eksekusi fungsi
# 10
# Dekorator 2: Setelah eksekusi fungsi
# Dekorator 1: Setelah eksekusi fungsi

# Contoh 2
# fungsi teks bintang
def bintang(func):
    def wrapper(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return wrapper

# fungsi teks persen
def persen(func):
    def wrapper(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return wrapper

@bintang
@persen
def input_user(text):
    print(text)

input_user("Hello World!")
# Output:
# ******************************
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# Hello World!
# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# ******************************

# Berikut beberapa contoh tambahan:
import time

# fungsi untuk menghitung jumlah yang di panggil
def counter(func):
    def wrapper(*args, **kwargs):
        jumlah = callable(func)
        result = func(*args, **kwargs)
        wrapper.jumlah += jumlah
        print(f"Memanggil fungsi {func.__name__}, {wrapper.jumlah} kali")
        return result
    wrapper.jumlah = 0
    return wrapper

# fungsi untuk menghitung jumlah waktu
def ex_timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        wrapper.total_time += total_time
        return result
    wrapper.total_time = 0.0
    return wrapper

@ex_timer
@counter
def faktorial(n):
    """Menghitung bilangan faktorial dengan fungsi rekursif"""
    if n == 1:
        return n
    else:
        return (n * faktorial(n - 1))

print(f"Hasil: {faktorial(5)}")
print(f"Total time: {faktorial.total_time} seconds")
# Output:
# Memanggil fungsi faktorial, 1 kali
# Memanggil fungsi faktorial, 2 kali
# Memanggil fungsi faktorial, 3 kali
# Memanggil fungsi faktorial, 4 kali
# Memanggil fungsi faktorial, 5 kali
# Hasil: 120
# Total time: 0.12798595428466797 seconds