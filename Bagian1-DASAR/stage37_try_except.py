#-------------------------------------------------------------------
# (!) Peringatan:
# Jika teks editor anda ada pesan error "PROBLEMS" atau baris kode berwarna "MERAH atau KUNING" diabaikan saja
#-------------------------------------------------------------------

# Konstruksi try-except-else-finally adalah mekanisme yang disediakan oleh Python
# untuk menangani error (exception) yang mungkin terjadi saat menjalankan program.
# Konstruksi ini terdiri dari empat bagian, yaitu:

# try: Bagian ini merupakan blok kode yang akan diuji untuk mencari error (exception).
# Jika tidak ada error yang terjadi, maka kode akan berjalan normal.
# Namun, jika terdapat error, maka eksekusi akan dihentikan dan akan dilanjutkan ke bagian except.

# except: Bagian ini merupakan blok kode yang akan dijalankan jika terjadi error pada bagian try.
# Di sini kita dapat menuliskan tindakan yang akan dilakukan saat terjadi error,
# misalnya menampilkan pesan error ke layar atau menuliskan pesan error ke file log.

# else: Bagian ini merupakan blok kode yang akan dijalankan jika tidak terjadi error pada bagian try.
# Ini biasanya digunakan untuk melakukan tindakan tambahan setelah kode di dalam try dijalankan dengan sukses.

# finally: Bagian ini merupakan blok kode yang akan selalu dijalankan, 
# baik terjadi error atau tidak pada bagian try.
# Ini biasanya digunakan untuk melakukan tindakan pembersihan atau 
# penutupan yang diperlukan setelah kode di dalam try dijalankan, misalnya menutup file yang dibuka di dalam try.

# menggunakan blok 'try' dan 'except'
# menangani error pada variabel 'x' yang belum di definisikan
try:
    print(x)
except:
    # menulis pesan kesalahan
    print("variabel x tidak ada")
# output:
# variabel x tidak ada

# Karena blok try menimbulkan kesalahan, blok exception akan dieksekusi.
# Tanpa blok try, program akan macet dan menimbulkan kesalahan
# print(x) # akan menampilkan kesalahan NameError: name 'x' is not defined

#===============================================================================

# menggunakan blok else
# Anda dapat menggunakan keyword 'else' untuk menentukan blok kode yang akan 
# dieksekusi jika tidak ada kesalahan yang muncul:
try:
    print('hello world')
except:
    # jika ada error tampilkan pesan ini
    print('pesan error')
else:
    # jika tidak terjadi error tampilkan pesan ini
    print('kode program tidak ada error')
# output:
# hello world
# kode program tidak ada error

#===============================================================================

# menggunakan blok finally
# blok kode finally akan selalu dijalankan baik terjadi error atau tidak pada bagian try.
try:
    print("hello world")
except:
    print("pesan error")
else:
    print("tidak ada error")
    for i in range(1,3):
        print('hello world', i)
finally:
    print("akhir dari program... selesai")
# output:
# hello world
# tidak ada error
# hello world 1
# hello world 2
# akhir dari program... selesai

try:
    x = 'hello'
    print(x[10])
except IndexError:
    print("(!) indeks string di luar jangkauan")
else:
    print('tidak ada error')
finally:
    print('akhir dari program... selesai')
# output:
# indeks string di luar jangkauan
# akhir dari program... selesai

#===============================================================================

# menggunakan klausa "except as Exception"
# "except as Exception" adalah sebuah klausa yang digunakan dalam pemrosesan 
# penanganan kesalahan (error handling) di Python. 
# Ini menangkap semua jenis kesalahan yang mungkin terjadi saat mengeksekusi kode dan
# mengizinkan Anda untuk menangani kesalahan tersebut dengan cara yang sesuai.

# Untuk menggunakan klausa "except as Exception", Anda dapat menuliskannya seperti ini:
try:
    # kode yang mungkun menyebabkan kesalahan
    print(y)
except Exception as err:
    # kode yang akan dieksekusi jika terjadi kesalahan
    # 'err' merupakan variabel yang menyimpan informasi tentang kesalahan yang terjadi
    print("terjadi kesalahan:", err)
# output:
# terjadi kesalahan: name 'y' is not defined

# Anda tidak perlu mencari jenis tipe error, cukup gunakan klausa "except Exception as err"
try:
    print(100 / 0)      # type error: ZeroDivisionError
except Exception as err:
    print("(!) terjadi kesalahan:", err)
finally:
    print("selesai.")
# output:
# (!) terjadi kesalahan: division by zero
# selesai.

# Jika anda ingin menangani kesalahan dengan menggunakan jenis kesalahan 
# yang spesifik, seperti ZeroDivisionError, ValueError, IndexError, dll.

try:
    print(100 / 0)
except ZeroDivisionError as err:
    print("[!] Error:", err)
# output:
# [!] Error: division by zero

# Anda dapat menentukan blok except sebanyak yang Anda inginkan, dan
# membuat sebuah pesan kesalahan yang anda inginkan
try:
    print(100/0)  # type error: ZeroDivisionError
    print(x)      # type error: NameError
except NameError:   # menangani kesalahan NameError
    print("variabel x tidak ada")
except ZeroDivisionError:   # menangani kesalahan ZeroDivisionError
    print("bilangan tidak bisa dibagi dengan angka nol")
# output:
# bilangan tidak bisa dibagi dengan angka nol

# cara untuk mengetahui type error jalankan program dibawah ini:
#print(100/0)

# output:
# Traceback (most recent call last):
#   File "stage37_try_except.py", line 50, in <module>
#     print(100/0)
# ZeroDivisionError: division by zero

#print(z)

# output:
# Traceback (most recent call last):
#   File "stage37_try_except.py", line 57, in <module>
#     print(z)
# NameError: name 'z' is not defined

# Dengan menggunakan jenis kesalahan yang spesifik, Anda dapat memberikan 
# respons yang lebih spesifik terhadap kesalahan yang terjadi.

# jika anda ingin mengetahui tentang menangani kesalahan kunjungi folder_name: "python-exception"