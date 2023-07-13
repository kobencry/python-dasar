# Fungsi dekorator adalah sebuah fungsi yang digunakan untuk memodifikasi atau melengkapi 
# perilaku dari suatu fungsi lain tanpa mengubah kode sumber asli dari fungsi tersebut.
# Fungsi dekorator memberikan kemampuan untuk mengubah fungsi menjadi fungsi yang 
# lebih kuat dengan menambahkan fungsionalitas tambahan.

# Fungsi dekorator menggunakan konsep Higher-Order Functions(fungsi yang menerima atau mengembalikan fungsi) 
# dan Nested Functions(fungsi yang didefinisikan di dalam fungsi lain). 
# Fungsi dekorator didefinisikan dengan menggunakan simbol @ diikuti dengan 
# nama fungsi dekorator di atas definisi fungsi yang akan didekorasi.

# Berikut adalah sintaks umum untuk mendefinisikan fungsi dekorator
# mengunakan konsep Higher-Order Functions:

def getNama(nama):
    return f"Hello, {nama}"

def decorate(func):
    def wrapper(nama):
        return f"----- {func(nama)} -----"
    return wrapper

hasil = decorate(getNama)
print(hasil("Alice"))
# Output:
# ----- Hello, Alice -----

# Berikut beberapa contoh tambahan:
#----------------------------------
# Contoh fungsi dengan satu argumen/parameter 
def tambah(x):
    return x + x

def kali(x):
    return x * x

def main(func, x):
    hasil = func(x)
    return hasil

print(main(tambah, 3))
# Output:
# 6

print(main(kali, 4))
# Output:
# 16

# Contoh fungsi dengan dua argumen/parameter
def tambah2(x, y):
    return x + y

def kali2(x, y):
    return x * y

def main2(func, x, y):
    hasil = func(x, y)
    return hasil

print(main2(tambah2, 4, 5))
# Output:
# 9

print(main2(kali2, 5, 6))
# Output:
# 30

# Mengambil fungsi lain sebagai argumen dalam bahasa pemrograman Python 
# termasuk dalam konsep Higher-Order Functions. 
# Higher-Order Functions adalah fungsi yang dapat menerima fungsi lain sebagai argumen, 
# atau mengembalikan fungsi sebagai nilai kembalian. 
# Dalam hal ini, fungsi yang menerima fungsi lain sebagai argumen adalah fungsi tingkat yang lebih tinggi. 