# -- python exception --

# https://docs.python.org/3/library/exceptions.html#OSError

# OSError adalah sebuah kelas exception di Python yang menunjukkan kesalahan yang terkait
# dengan sistem operasi atau lingkungan eksekusi seperti masalah file, jaringan, proses, dll. 
# Exception ini biasanya dihasilkan ketika ada kesalahan dalam operasi yang melibatkan sistem operasi.

# Contoh penggunaan OSError bisa terjadi saat mencoba membuka atau menulis ke sebuah file yang tidak ditemukan 
# atau tidak dapat diakses, atau ketika terjadi kesalahan koneksi jaringan saat mencoba mengakses server.

try:
    # membuka file yang tidak ada
    with open("fileku.txt") as f:
        print(f.read())
except OSError as e:
    # menangani error dan cetak pesan kesalahan
    print("OSError:", e)
# Output:
# OSError: [Errno 2] No such file or directory: 'fileku.txt'

# menggunakan Argument
# Argument errno, strerror, dan filename dapat diakses sebagai atribut dari object OSError,
# sehingga dapat digunakan untuk mengedit atau menampilkan informasi error yang lebih detail.
try:
    # membuka file yang tidak ada
    f = open('fileku.txt')
except OSError as e:
    # menangani error dan cetak pesan kesalahan
    print("OSError: ", e.errno, e.strerror, e.filename)
# Output:
# OSError:  2 No such file or directory fileku.txt