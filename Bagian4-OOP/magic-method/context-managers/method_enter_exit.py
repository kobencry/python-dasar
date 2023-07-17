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