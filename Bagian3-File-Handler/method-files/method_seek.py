# Method seek() adalah method yang terdapat pada objek file di Python yang 
# digunakan untuk mengatur posisi file pointer pada file yang terbuka saat ini.
# Method ini memiliki dua argument yaitu "offset" dan "whence".

# Syntax
# file.seek(offset, whence)

# Argument "offset" menentukan jumlah byte yang akan ditambahkan atau dikurangi
# dari posisi file pointer saat ini. 
# Jika "offset" bernilai positif, maka file pointer akan berpindah ke depan sebanyak "offset" byte. 
# Sebaliknya, jika "offset" bernilai negatif, maka file pointer akan berpindah ke belakang sebanyak "offset" byte.

# Argument "whence" menentukan dari mana offset akan ditambahkan atau dikurangi.
# Nilai "whence" dapat bernilai:
# 0 (mengacu pada awal file)
# 1 (mengacu pada posisi file pointer saat ini) atau 
# 2 (mengacu pada akhir file).

# Berikut ini adalah contoh penggunaan method seek() di Python:
# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file_demo_seek.txt') as fileku:
    # membaca sebanyak 22 byte atau karakter dari file
    isi_file = fileku.read(22)
    print(isi_file)
    # Output:
    # hello world
    # alice
    # carl

    # >>> posisi pointer saat ini berada di carl 

    # membaca seluruh isi file
    print(fileku.read())
    # Output:
    # eliot
    # ini adalah file demo seek
    
    # >>> posisi pointer saat ini berada diakhir
    
    # mengatur posisi pointer keawal
    fileku.seek(0)
    
    # membaca sebanyak 11 byte atau karakter dari file
    print(fileku.read(11))
    # Output:
    # hello world

    # mengatur posisi pointer ke baris 19
    fileku.seek(19)
    print(fileku.read(5))
    # Output:
    # carl
# File akan ditutup secara otomatis setelah selesai mengolah

# menggunakan argument "whence"
with open('file_demo_seek.txt') as fileku:
    # membaca seluruh isi file
    print(fileku.read())
    
    # >>> posisi pointer saat ini berada diakhir
    # mengatur posisi pointer
    print(fileku.seek(0,0))

    print(fileku.read(5))
    


# Perlu diingat bahwa penggunaan method seek() hanya dapat dilakukan pada file yang terbuka dengan mode "read" atau "write+". Jika file tersebut dibuka dengan mode "write", maka method seek() akan menyebabkan error
