# -- python exception --

#-------------------------------------------------------------------
# (!) Peringatan:
# Jika teks editor anda ada pesan error "PROBLEMS" atau baris kode berwarna "MERAH atau KUNING" diabaikan saja
#-------------------------------------------------------------------

# https://docs.python.org/3/library/exceptions.html#NameError

# NameError merupakan sebuah exception yang terjadi ketika suatu variabel atau
# nama yang digunakan tidak ditemukan dalam lingkup yang sesuai. 
# Hal ini dapat terjadi ketika kita mencoba untuk menggunakan suatu variabel atau 
# fungsi yang belum didefinisikan. 
# Exception ini umumnya terjadi pada saat runtime.
# Sebagai contoh, jika kita mencoba untuk menggunakan sebuah variabel yang belum didefinisikan
# dalam sebuah program Python

try:
    x = "hello"
    y = "world"
    print(x + y + z)
except NameError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'NameError'>
# Pesan Error: name 'z' is not defined

# menggunakan pesan error sendiri
try:
    x = 10
    y = 50
    print(x + y + z)
# menangkap jenis Error
except NameError:
    print("variabel atau fungsi belum didefinisikan")
# Output:
# variabel atau fungsi belum didefinisikan