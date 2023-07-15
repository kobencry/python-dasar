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