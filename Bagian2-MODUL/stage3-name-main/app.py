# __name__ adalah sebuah variabel bawaan dalam Python yang menyimpan nama 
# dari modul atau nama dari skrip yang sedang dijalankan. 
# Jika sebuah skrip dijalankan langsung, maka __name__ akan bernilai __main__. 
# Ini bisa digunakan sebagai cara untuk menentukan apakah sebuah skrip sedang
# dijalankan langsung atau diimport ke dalam skrip lain.

# Berikut ini adalah contoh sederhana tentang bagaimana __name__=='__main__' bisa digunakan:
def fungsiku():
    print("ini adalah fungsi utama")
    print(f"nilai __name__ pada file app.py -> {__name__}")

if __name__=='__main__':
    fungsiku()
    # output:
    # ini adalah fungsi utama
    # nilai __name__ pada file app.py -> __main__

# Jika skrip di atas dijalankan langsung, maka akan dicetak kelayar. 
# Namun, jika skrip di atas diimport ke dalam skrip lain, maka fungsiku()
# tidak akan dijalankan, karena kondisi if tidak akan terpenuhi.


# Jika anda masih bingung saya akan buatkan beberapa contoh:
# kita memiliki package "matematika" yang berisi modul penjumlahan.py, dan pengurangan.py
# dalam contoh ini kita akan melihat perbedaan dari modul tersebut

# buka modul penjumlahan.py anda melihat baris kode, if __name__=='__main__':
from matematika import penjumlahan

def fungsiku():
    hasil = penjumlahan.tambah(10, 20)
    print(hasil)

if __name__=="__main__":
    fungsiku()
    # output:
    # ini adalah fungsi tambah dari modul penjumlahan
    # nilai __name__ pada modul penjumlahan.py -> matematika.penjumlahan
    # 30
 
# buka modul pengurangan.py anda tidak melihat baris kode, yang berisi if __name__=='__main__':
from matematika import pengurangan as mtk

def fungsiku2():
    hasil = mtk.kurang(100, 50)
    print(hasil)
if __name__=="__main__":
    fungsiku2()
    # output:
    # ini adalah fungsi kurang dari modul pengurangan
    # nilai __name__ pada modul pengurangan.py -> matematika.pengurangan
    # 5
    # ini adalah fungsi kurang dari modul pengurangan
    # nilai __name__ pada modul pengurangan.py -> matematika.pengurangan
    # 50

# lihatlah perbedaan dari kedua output tersebut.
# jika anda menggunakan if __name__=='__main__', kemudian script tersebut diimport 
# ke dalam sebuah module atau file lain, maka fungsi tambah() tidak akan dijalankan.

# Penggunaan if __name__=='__main__' sangat berguna jika Anda ingin menuliskan sebuah 
# script yang dapat diimport ke dalam module lain, tetapi juga bisa dijalankan secara langsung jika diperlukan.
