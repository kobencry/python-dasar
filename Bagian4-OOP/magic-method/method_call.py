# method __call__() adalah method khusus yang digunakan untuk memungkinkan objek dipanggil seperti fungsi.
# Method ini digunakan untuk memberikan sifat fungsi pada objek, 
# sehingga objek dapat diperlakukan seperti fungsi dan dipanggil dengan argumen.

# Ketika suatu objek dipanggil, Python akan mencari method __call__() pada kelas objek. 
# Jika method __call__() ditemukan, maka Python akan memanggil method tersebut dan menjalankan blok kode di dalamnya.
# Method __call__() biasanya digunakan untuk mengimplementasikan objek yang dapat dipanggil, 
# seperti decorator atau class-based views pada web framework.

# Syntax
# class MyClass:
#    def __call__(self, arg1, arg2, ...):
        # kode yang akan dijalankan saat objek dipanggil seperti fungsi

# Nilai Parameter
# Parameter             Deskripsi
# self                  merujuk pada objek itu sendiri.
# arg1, arg2, ...       argumen yang diberikan saat objek dipanggil seperti fungsi.

# Dalam method __call__(), kita dapat menentukan logika atau kode yang 
# ingin dijalankan ketika objek tersebut dipanggil seperti fungsi. 
# Kode yang dituliskan pada method __call__() akan dieksekusi saat objek dipanggil seperti fungsi.