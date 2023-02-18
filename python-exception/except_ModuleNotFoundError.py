# -- python exception --

#-------------------------------------------------------------------
# (!) Peringatan:
# Jika teks editor anda ada pesan error "PROBLEMS" atau baris kode berwarna "MERAH atau KUNING" diabaikan saja
#-------------------------------------------------------------------

# https://docs.python.org/3/library/exceptions.html#ModuleNotFoundError

# ModuleNotFoundError adalah subclass dari ImportError yang terjadi ketika module yang dicoba 
# diimport tidak ditemukan atau tidak dapat diakses. 
# Ini berbeda dengan ImportError umumnya yang dapat terjadi karena banyak alasan, 
# seperti kesalahan sintaks dalam module yang dicoba diimpor atau kesalahan dalam module
# yang dicoba diimpor itu sendiri.

try:
    import sys         # modul bawaan python
    import time        # modul bawaan python
    import hello_world # mencoba mengimpor modul yang tidak ada
except ModuleNotFoundError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'ModuleNotFoundError'>
# Pesan Error: No module named 'hello_world'

# menggunakan pesan error sendiri
try:
    import hello_world
# menangkap jenis Error
except ModuleNotFoundError as err:
    print(f"modul {err.name} tidak ada")
# Output:
# modul hello_world tidak ada