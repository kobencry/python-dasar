# Fungsi lambda adalah fungsi yang didefinisikan tanpa nama (anonim) dan hanya dapat berisi satu ekspresi. 
# Fungsi lambda ini sering digunakan sebagai callback function atau sebagai parameter dari fungsi lain.

# Syntax
# lambda argument: expression

# argument     nilai yang diteruskan ke fungsi. 
# expression   dieksekusi dan hasilnya dikembalikan.

# menggunakan fungsi biasa dengan satu statement
# def fungsiku(x):
#     return x
# print(fungsiku('hello world'))

# jika anda memiliki fungsi dengan satu statement/expression gunakanlah fungsi lambda (anonim)
# kode ini setara dengan diatas
fungsiku = lambda x: x
print(fungsiku('hello world'))

tambah = lambda x, y: x + y
print(tambah(2, 3))     # 5

# contoh fungsi lambda dengan fungsi print() dalam satu expression/statement
kurang = lambda x, y: print(x - y)
kurang(5, 2)    # 3

# membalikkan suatu kata
# menggunakan fungsi biasa
# def fungsiku(text):
#     return text[::-1]
# print(fungsiku('hello world')) # dlrow olleh

# kode ini setara dengan diatas
fungsiku = lambda text: text[::-1]
print(fungsiku('hello world'))  # dlrow olleh

# Anda, tidak perlu menetapkan variabel ke lambda ekspresi sebelum memanggilnya.
# Anda juga dapat memanggil fungsi yang ditentukan oleh lambda ekspresi secara langsung:
print((lambda text: text[::-1])('Hello World'))     # dlroW olleH

# menampilkan menggunakan formatting f-string dan fungsi lambda dalam satu baris.
print(f"--- {(lambda angka: [x for x in angka])(range(5))} ---")
# --- [0, 1, 2, 3, 4] ---

# Mengapa Menggunakan Fungsi Lambda?
# Kekuatan lambda ditampilkan dengan lebih baik saat Anda menggunakannya sebagai fungsi anonim di dalam fungsi lain.
# Katakanlah Anda memiliki definisi fungsi yang mengambil satu argumen, 
# dan argumen itu akan dikalikan dengan nomor yang tidak diketahui:
def kali(n):
    return lambda x: x * n

fungsi_kali2 = kali(5)
print(fungsi_kali2(2))  # 10

# memanggil dengan cara seperti ini:
print(kali(5)(2))   # 10

# contoh fungsi lambda untuk mengurutkan list
angka = [4, 2, 6, 1, 8]
print('sebelum:', angka)    # sebelum: [4, 2, 6, 1, 8]
angka.sort(key=lambda x: -x)
print('sesudah:', angka)    # sesudah: [8, 6, 4, 2, 1]
