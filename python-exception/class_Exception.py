# -- python exception --

#-------------------------------------------------------------------
# (!) Peringatan:
# Jika teks editor anda ada pesan error "PROBLEMS" atau baris kode berwarna "MERAH atau KUNING" diabaikan saja
#-------------------------------------------------------------------

# Exception adalah sebuah class bawaan Python yang merepresentasikan sebuah kesalahan atau error
# yang terjadi pada saat program dijalankan. 
# Class ini dapat dijadikan sebagai superclass atau parent class untuk membuat subclass 
# yang merepresentasikan jenis-jenis kesalahan atau error yang lebih spesifik. 
# Semua subclass dari Exception dan Exception sendiri akan dianggap sebagai kesalahan atau error
# pada saat program dijalankan.
# Ketika kita ingin membuat exception kita sendiri, kita bisa menginherit Exception atau subclassnya.
# kunjungi file: "Exception_Hierarchy.txt"

# Berikut adalah contoh penggunaan class Exception dalam kode Python:
try:
    x = 10 / 0
except Exception as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'ZeroDivisionError'>
# Pesan Error: division by zero

# menangkap error menggunakan class Exception sehingga pesan error yang muncul akan 
# disesuaikan dengan jenis error yang terjadi.

try:
    x = fungsiku()
except Exception as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'NameError'>
# Pesan Error: name 'fungsiku' is not defined

def bagi(x, y):
    return x / y

try:
    print(bagi(10, 2))
    print(bagi(10, 5))
    print(bagi(10, 0))
except Exception as err:
    print("(!) error:", err)
# Output:
# 5.0
# 2.0
# (!) error: division by zero