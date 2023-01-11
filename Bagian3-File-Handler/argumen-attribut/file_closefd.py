# Argument 'closefd' pada method open() di Python adalah sebuah parameter Boolean 
# yang mengontrol apakah file descriptor harus ditutup atau tidak saat objek file ditutup. 
# File descriptor adalah objek berkompleksitas rendah yang digunakan sistem operasi 
# untuk melacak file yang terbuka. Jika 'closefd' diatur ke True (nilai default), 
# maka file descriptor akan ditutup saat objek file ditutup, sehingga file tidak lagi dapat diakses. 
# Jika 'closefd' diatur ke False, maka file descriptor tidak akan ditutup, sehingga file akan tetap terbuka.

# Contoh penggunaan argumen closefd pada method open() adalah sebagai berikut:

# membuka file dengan mode 'r+' (read/baca, write/tulis)
with open("example2.txt", mode='r+') as fr:
    # mengembalikan nilai file deskriptor
    file_deskriptor = fr.fileno()

    # membuka file dengan mode 'a' (append/tambah)
    # untuk menggunakan file deskriptor argumen closefd harus bernilai boolean False
    with open(file_deskriptor, mode='a', closefd=False) as fw:
        # menulis data string ke file
        fw.write('\n' + "hello world")

        # untuk membaca isi file yang sudah dibaca atau ditulis
        # kita harus pindahkan posisi pointer(cursor) ke awal file
        # posisi pointer(cursor) saat ini berada diakhir file
        # mengatur posisi pointer(cursor) ke awal file
        fw.seek(0)
        # membaca isi file
        print(fr.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# hello world