# Method flush() memberisihkan buffer internal, yang berguna untuk mengalirkan(flush) 
# semua output yang terkumpul pada buffer ke output secara langsung.
# Biasanya, buffer ini akan terisi ketika kita menuliskan output ke dalam 
# suatu file atau perangkat lain yang membutuhkan waktu untuk menuliskannya.

# Buffer adalah sebuah area penyimpanan sementara yang digunakan untuk 
# menampung data yang akan diolah atau disimpan. 
# Pada Python, buffer biasanya digunakan untuk menyimpan output yang akan dituliskan
# ke dalam suatu file atau perangkat lain, seperti terminal atau printer.

# Buffer akan terisi ketika kita menuliskan output ke dalam file atau perangkat lain,
# dan akan dikosongkan ketika output tersebut selesai dituliskan.
# Hal ini dilakukan agar tidak terjadi pengaliran data secara terus-menerus ke
# file atau perangkat lain, yang dapat menyebabkan kinerja sistem menjadi lebih lambat.

# Method flush() pada Python berguna untuk mengalirkan(flush) semua output 
# yang terkumpul pada buffer ke output secara langsung,
# sehingga kita dapat yakin bahwa output tersebut telah tersimpan di file atau perangkat lain yang dituju.

# Syntax
# file.flush()

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode 'w' (write/tulis)
with open('file_demo_flush.txt', 'w') as fileku:
    # menuliskan output ke file
    fileku.write('ini adalah output pertama\n')
    # menggunakan method flush() untuk mengalirkan output ke file
    fileku.flush()
    # menuliskan output ke file lagi
    fileku.write('ini adalah output kedua\n')
# File akan ditutup secara otomatis setelah selesai mengolah

# membuka file dengan mode 'a' (append/tambahkan)
with open('file_demo_flush.txt', 'a') as fileku:
    fileku.write('hello world\n')
    fileku.flush()
    fileku.write('...ini adalah file demo flush')
# File akan ditutup secara otomatis setelah selesai mengolah

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file_demo_flush.txt') as fileku:
    isi_file = fileku.read()
    print(isi_file)
# Output:
# ini adalah output pertama
# ini adalah output kedua
# hello world
# ...ini adalah file demo flush

# Dengan menggunakan method flush(), kita dapat yakin bahwa output 
# yang terkumpul pada buffer akan dituliskan ke file secara langsung, 
# sehingga kita tidak perlu menunggu sampai buffer terisi terlebih dahulu.
