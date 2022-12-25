# Method fileno() adalah method yang terdapat pada objek file di Python.
# Method ini mengembalikan nomor file descriptor yang terkait dengan objek file tersebut.
# File descriptor adalah angka unik yang digunakan oleh sistem operasi untuk mengidentifikasi file yang terbuka.

# Syntax
# file.fileno()

# Nilai Parameter
# tidak ada nilai parameter

# Berikut ini adalah contoh penggunaan method fileno() di Python:
# membuka file dengan mode 'r' (read/baca) 
with open('file.txt', 'r') as fileku:
    # menggunakan method fileno() untuk mendapatkan nomor file descriptor
    fd = fileku.fileno()
    # menampilkan nomor file descriptor
    print(fd)   # Output: 3
# File akan ditutup secara otomatis setelah selesai mengolah

# Jika file 'file.txt' berhasil dibuka dan ditampilkan nomor file descriptor-nya, 
# maka output dari program tersebut adalah angka yang menunjukkan nomor file descriptor dari file tersebut.

# Perlu diingat bahwa method fileno() hanya dapat digunakan pada objek file yang sudah dibuka dengan mode yang sesuai.
# Jika objek file tidak dibuka atau dibuka dengan mode yang tidak sesuai, maka method ini akan mengembalikan error.

# membuka file dengan mode 'w' (write/tulis)
with open('file_demo_fileno.txt', 'w') as fileku:
    fd = fileku.fileno()
    print(fd)   # Output: 3
    # menulis data ke filedemo.txt
    fileku.write('hello world')
    fd2 = fileku.fileno()
    print(fd2)  # Output: 3
# File akan ditutup secara otomatis setelah selesai mengolah

# Jika Anda menjalankan program yang menggunakan method fileno() 
# di Python dan hasilnya selalu mengembalikan angka 3,
# maka hal tersebut mungkin disebabkan oleh beberapa hal berikut:

'''
1. Anda mungkin menggunakan Python di lingkungan command prompt atau terminal,
 dan file descriptor 3 telah dialokasikan untuk mengakses input dan output standar (stdin dan stdout).
 Hal ini mungkin terjadi jika Anda membuka file dengan menggunakan metode open() biasa, tanpa menyertakan parameter fd.

2. Anda mungkin menggunakan library tambahan di Python yang secara default 
 menggunakan file descriptor 3 untuk mengakses stdin dan stdout. 
 Hal ini mungkin terjadi jika Anda menggunakan library yang membuka file 
 dengan menggunakan metode yang berbeda dari open().

3. Anda mungkin menggunakan Python di lingkungan yang membatasi jumlah file descriptor yang tersedia. 
 Hal ini mungkin terjadi jika Anda menggunakan Python di lingkungan yang terbatas seperti container atau virtual machine,
 dan file descriptor 3 telah dialokasikan sebagai file descriptor yang tersedia pertama kali.

 Untuk mengatasi masalah ini, Anda dapat mencoba menggunakan metode open() 
 dengan menyertakan parameter fd untuk menentukan nomor file descriptor yang diinginkan.
 Anda juga dapat mencoba menggunakan library tambahan yang tidak menggunakan file descriptor 3 
 secara default atau menggunakan Python di lingkungan yang tidak membatasi jumlah file descriptor yang tersedia.
 '''
