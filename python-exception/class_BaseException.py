# -- python exception --

#-------------------------------------------------------------------
# (!) Peringatan:
# Jika teks editor anda ada pesan error "PROBLEMS" atau baris kode berwarna "MERAH atau KUNING" diabaikan saja
#-------------------------------------------------------------------

# https://docs.python.org/3/library/exceptions.html

# BaseException adalah kelas dasar untuk semua Exception/pengecualian bawaan di Python.
# Semua kelas pengecualian lainnya berasal dari kelas ini,
# dan menyediakan antarmuka standar untuk Exception/pengecualian bawaan.
# Ini berarti BaseException adalah akar dari hierarki pengecualian di Python.
# kunjungi file: "exception_hierarchy.txt"

# Kelas BaseException mendefinisikan beberapa atribut dan metode umum yang diwarisi oleh semua subkelasnya.
# Ini termasuk atribut args, yang berisi argumen yang diteruskan ke pengecualian, dan metode __str__(),
# yang mengembalikan representasi string dari pengecualian.

# Catatan:
# Umumnya tidak disarankan untuk menangkap BaseException secara langsung dalam kode,
# karena menyertakan pengecualian keluar sistem dan interupsi keyboard yang biasanya tidak dimaksudkan
# untuk ditangkap di sebagian besar kode. 
# Sebaliknya, lebih baik menangkap Exception/pengecualian yang lebih spesifik yang mewakili 
# kesalahan yang Anda tangani.

# kode Buruk
try:
    1/0
except BaseException as err:
    print("BaseException:", err)
# Output:
# BaseException: division by zero

# kode Buruk
# try:
#     fungsiku()
# except BaseException as err:
#     print("BaseException:", err)
# Output:
# BaseException: name 'fungsiku' is not defined

# kode Bagus
# try:
#     1/0
# except ZeroDivisionError as err:
#     print("ZeroDivisionError:", err)
# Output:
# ZeroDivisionError: division by zero

# kode Bagus
# try:
#     fungsiku()
# except NameError as err:
#     print("NameError:", err)
# Output:
# NameError: name 'fungsiku' is not defined