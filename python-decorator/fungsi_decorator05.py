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