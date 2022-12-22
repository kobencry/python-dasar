# 'assert' adalah sebuah perintah yang digunakan dalam bahasa pemrograman Python
# untuk mengecek apakah sebuah ekspresi benar atau salah. 
# Jika ekspresi tersebut benar, maka perintah assert tidak akan melakukan apa-apa. 
# Namun, jika ekspresi tersebut salah, maka assert akan mengeluarkan pesan 
# kesalahan (error message) dan menghentikan eksekusi program.

# Contoh penggunaan assert dalam Python adalah sebagai berikut:
# Syntax
# assert(expression), <message>
x = 100
y = 2

# periksa apakah x lebih besar dari y
assert(x > y), "hello world"
# periksa apakah x sama dengan y
#assert(x == y)

# Pada contoh di atas, perintah assert pertama tidak akan mengeluarkan pesan kesalahan
# karena ekspresi x > y benar (nilai x adalah 100 dan nilai y adalah 2, sehingga 100 > 2).
# Namun, perintah assert kedua akan mengeluarkan pesan kesalahan karena 
# ekspresi x == y salah (nilai x adalah 100 dan nilai y adalah 2, sehingga 100 tidak sama dengan 2).

# periksa system operasi windows, linux, macos
import sys  # standar library python anda akan mempelajari di Bagian2-MODUL
def info_os():
    # jika anda memakai os windows pesan error tidak di tampilkan 
    assert('win32' in sys.platform), "program ini hanya berlaku untuk windows"

    # jika anda memakai os linux
    # assert('linux' in sys.platform), "program ini hanya berlaku untuk linux & macos"
info_os()

# Catatan: penggunaan assert harus digunakan dengan hati-hati dan hanya untuk mengecek kondisi 
# yang harusnya selalu terpenuhi pada saat program dijalankan. 
# Jika Anda perlu mengecek kondisi yang mungkin saja tidak terpenuhi, 
# sebaiknya menggunakan perintah if atau try dan except yang lebih tepat.

# kapan Tidak menggunakan statement assert
# Jangan gunakan kode yang sedang diproduksi, pernyataan assert hanya untuk develop/pengembang dalam debugging

#===================================================================================

# 'raise' adalah sebuah perintah yang digunakan dalam bahasa pemrograman Python untuk 
# menaikan (raise) sebuah exception (kesalahan). 
# Exception dapat digunakan untuk menandakan bahwa terjadi sebuah 
# kesalahan atau kondisi aneh pada saat program dijalankan. 
# Exception dapat ditangani dengan menggunakan perintah try dan except, 
# sehingga program tidak terhenti eksekusinya ketika terjadi exception.

# Contoh penggunaan raise dalam Python adalah sebagai berikut:
def bagi(x, y):
  # perika apakah y sama dengan 0
  if y == 0:
    # Menaikan exception jika y sama dengan 0
    raise ValueError("Tidak bisa membagi dengan 0")
  return x / y


if __name__=='__main__':
    # Mencoba memanggil fungsi bagi()
    try:
      hasil = bagi(10, 0)
      print(hasil)
    except ValueError as e:
      print("Terjadi kesalahan:", e)
    # output:
    # Terjadi kesalahan: Tidak bisa membagi dengan 0

# Pada contoh di atas, fungsi bagi() akan menaikan kesalahan exception ValueError 
# jika terjadi pembagian dengan nol (nilai y sama dengan 0). 
# Exception tersebut kemudian dapat ditangani dengan menggunakan perintah try dan except,
# sehingga program tidak berhenti eksekusinya ketika terjadi pembagian dengan nol.

# jika anda ingin mengetahui tentang menangani kesalahan kunjungi folder_name: "python-exception"
# jika anda ingin mengetahui tentang __name__=='__main__' kunjungi folder_name: "Bagian2-Modul"

# Selanjutnya anda akan belajar di folder_name:
# Bagian2-Modul
# Bagian3-File-Handler
# Bagian4-OOP(Object Oriented Programming)

# anda dapat mempelajari berbagai folder yang sudah disematkan untuk beberapa kebutuhan.
