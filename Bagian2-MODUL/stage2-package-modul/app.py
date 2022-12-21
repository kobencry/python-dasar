# Package adalah sekumpulan modul Python yang terorganisir dan terstruktur dengan baik.
# Modul adalah sebuah file yang berisi kode Python yang dapat digunakan kembali di dalam sebuah aplikasi. 
# Package menyediakan cara untuk mengelompokkan modul-modul terkait menjadi satu unit yang lebih besar dan lebih mudah dikelola.

# Contohnya, sebuah package bernama "matematika" dapat berisi beberapa modul seperti "penjumlahan", "pengurangan", dan "perkalian". 
# Masing-masing modul tersebut dapat berisi fungsi-fungsi yang berkaitan dengan penjumlahan, pengurangan, dan perkalian.
# Dengan menggunakan package ini, kita dapat dengan mudah mengakses semua fungsi yang terdapat di dalamnya tanpa perlu mengimport setiap modul secara terpisah.

# contoh untuk menggunakan package atau modul di Python, 
# kita perlu mengimportnya terlebih dahulu dengan menggunakan perintah import.

# package ini hanya berlaku untuk fungsi penjumlahan.
import matematika.penjumlahan

hasil = matematika.penjumlahan.tambah(10, 20)
print(hasil)    # 30

# menggunakan as 'alias' atau (singkatan)
# package ini hanya berlaku untuk fungsi perkalian. 
import matematika.perkalian as mtk

hasil = mtk.kali(2, 5)
print(hasil)

# menggunakan from nama_package import nama_modul
from matematika import penjumlahan, pengurangan, perkalian

hasil_tambah = penjumlahan.tambah(50, 50)
print(hasil_tambah) # 100

hasil_kurang = pengurangan.kurang(20, 10)
print(hasil_kurang) # 10

hasil_kali = perkalian.kali(5, 5)
print(hasil_kali)   # 25
