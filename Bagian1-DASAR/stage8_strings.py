# python string
# string dalam python dikelilingi oleh tanda kutip tunggal, atau tanda kutip ganda.
# 'hello', sama dengan "hello"
# tanda kutip tunggal, maupun tanda kutip ganda tidak mempengaruhi kode/program python anda.
# benar-benar sama ('tidak ada magic dalam tanda tunggal/ganda')

print('hello world') # kutip tunggal
print("hello world") # kutip ganda


# menggunakan string multiline
# Anda dapat menetapkan string multiline ke variabel dengan menggunakan tiga tanda kutip ganda.
x = """
> Apa itu Python?
> Python adalah bahasa pemrograman yang populer. 
> Itu dibuat oleh Guido van Rossum, dan dirilis pada tahun 1991.
"""
print(x)

# menggunakan tiga tanda kutip tunggal
x = '''
    > Apa itu Python?
    > Python adalah bahasa pemrograman yang populer. 
    > Itu dibuat oleh Guido van Rossum, dan dirilis pada tahun 1991.
'''
print(x)

# Catatan: 
# pada hasilnya, jeda baris disisipkan pada posisi yang sama seperti contoh pada kode yang diatas.

#===============================================================================

# string adalah array
# Seperti banyak bahasa pemrograman populer lainnya, string dalam Python adalah 
# array byte yang mewakili karakter unicode.

# namun, Python tidak memiliki tipe data karakter, karakter tunggal hanyalah string dengan panjang 1.
# Tanda kurung siku dapat digunakan untuk mengakses elemen string.

# ingat karakter pertama memiliki posisi 0
# menampilkan karakter di posisi 2
x = "hello world!"
print(x[1])

print(x[0], x[1], x[2], x[3], x[4])

# karena string adalah array, kita dapat mengulang karakter dalam string dengan forloop.
# loop huruf-huruf dalam kata "hello world!"
for x in "hello world!":
    print(x)    # pelajari lebih lanjut tentang forloop di file_name: ""


# panjang string
# untuk mendapatkan panjang string, gunakan fungsi len()
# pelajari labih lanjut tentang fungsi len() di file_name: "Fungsi-Bawaan"
x = "hello world!"
print(len(x))

y = "python3.8|3.9|3.10"
panjang = len(y)
print(panjang)

# menggunakan keyword "in" yang sudah di jelaskan di file_name: "stage1_hello world.py"
# memeriksa string apakah ada suatu karakter tertentu dalam sebuah string.
txt = "hello world!"
print("world" in txt) # mengembalikan tipe data boolean True

# menggunakan keyword "not" dan "in"
# periksa apakah ada "war world" Tidak ada dalam txt.
txt = "hello world!"
print("war world!" not in txt) # megembalikan tipe data boolean True

# menggabungkan string dengan operator aritmatika tambah (+)
x = "hello"
y = "world"
print(x + y)
print(x + " " + y) # menggunakan spasi
