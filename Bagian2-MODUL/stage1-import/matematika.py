# ini adalah modul matematika
def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    # periksa apakah y nilainya nol
    # dalam matematis nilai bilangan tidak bisa membagi dengan nol.
    try:
        # jika hasilnya ingin float/bilangan desimal gunakan tanda /
        # return x /y
        # jika hasilnya ingin bilangan bulat gunakan tanda //
        return x // y
    except Exception as e:    # menangkap jenis error apapun
        return f"(!) Error: {e}"
