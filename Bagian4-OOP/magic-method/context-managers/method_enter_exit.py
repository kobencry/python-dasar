# Magic method __enter__ dan __exit__ adalah dua metode khusus dalam Python 
# yang digunakan dalam context managers exception/pengecuali(exception handling) 
# dengan menggunakan statement "with". 
# Kedua metode ini bekerja bersama untuk memberikan perilaku yang diinginkan 
# saat memasuki dan keluar dari blok konteks.

# __enter__ adalah metode yang dieksekusi saat memasuki blok konteks dengan statement "with".
# Metode ini menginisialisasi konteks dan mengembalikan objek yang akan digunakan dalam blok konteks.
# __exit__ adalah metode yang dieksekusi saat keluar dari blok konteks dengan statement "with". 
# Metode ini bertanggung jawab untuk menangani pengecualian(exception) 
# yang terjadi dalam blok konteks dan melakukan tindakan yang sesuai, 
# seperti membersihkan sumber daya atau menangani eksepsi tersebut.

# Definisi dan penggunaan deskripsi syntax dari __enter__ dan __exit__ adalah sebagai berikut:
# def __enter__(self):
    # Logika atau tindakan yang akan dilakukan saat memasuki blok konteks
    # Mengembalikan objek yang akan digunakan dalam blok konteks

# def __exit__(self, exc_type, exc_value, traceback):
    # Logika atau tindakan yang akan dilakukan saat keluar dari blok konteks
    # Biasanya berhubungan dengan penanganan eksepsi (exception handling)

# Parameter
# self: Merujuk pada instance objek yang sedang digunakan.
# exc_type: Merupakan tipe eksepsi yang diangkat, jika ada.
#           Jika tidak ada eksepsi, maka exc_type akan bernilai None.
# exc_value: Merupakan instance eksepsi yang diangkat, jika ada.
#            Jika tidak ada eksepsi, maka exc_value akan bernilai None.
# traceback: Merupakan traceback (jejak panggilan) exception/pengecualian yang diangkat, jika ada. 
#            Jika tidak ada eksepsi, maka traceback akan bernilai None.

# Contoh penggunaan __enter__ dan __exit__ dalam blok konteks "with" untuk menutup 
# file adalah sebagai berikut:
class FileOpener:
    def __init__(self, nama_file):
        self.nama_file = nama_file
        self.objek_file = None
    
    def __enter__(self):
        self.objek_file = open("demo.txt", 'r')
        return self.objek_file
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.objek_file.close()
