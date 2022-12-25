# Method close() adalah method yang digunakan untuk menutup file yang telah 
# dibuka dengan menggunakan method open() di Python.

# Syntax
# file.close()

# Nilai Parameter
# tidak ada nilai parameter

# Berikut ini adalah contoh penggunaan method close() pada penanganan file di Python:
# membuka file dengan mode default ('r', atau 't')
fileku = open('file.txt')
# mengolah file dengan method read()
print(fileku.read())

# menutup file setelah selesai mengolah
fileku.close()

# Setelah file ditutup dengan menggunakan method close(), kita tidak dapat lagi
# melakukan operasi pada file tersebut sebelum membuka kembali file tersebut dengan
# menggunakan method open().

# Menutup file dengan method close() sangat penting karena dengan menutup file 
# maka memori yang digunakan oleh file tersebut akan dikembalikan ke sistem. 
# Jika file tidak ditutup setelah selesai digunakan, maka memori yang digunakan oleh file 
# tersebut tidak akan dikembalikan ke sistem sehingga dapat menyebabkan masalah pada kinerja sistem.

# Selain itu, menutup file juga penting karena jika file tidak ditutup maka dapat terjadi kesalahan pada file itu sendiri.
# Misalnya, jika Anda membuka file untuk ditulisi (menggunakan mode "w" atau "a"), 
# maka data yang telah ditulis ke file tidak akan disimpan ke disk jika file tidak ditutup.
# Ini dapat menyebabkan kehilangan data atau kesalahan pada file.
# Oleh karena itu, selalu pastikan untuk menutup file setelah selesai menggunakannya dengan menggunakan method close(). 

# atau dengan menggunakan statement with. 
# Ini akan memastikan bahwa memori yang digunakan oleh file dikembalikan 
# ke sistem dan data pada file disimpan dengan benar.
# kita juga dapat menggunakan statement with untuk membuka file di Python.
# Dengan menggunakan statement with, kita tidak perlu memikirkan untuk menutup file secara manual,
# karena file akan ditutup secara otomatis setelah selesai mengolah file tersebut.
# Berikut ini adalah contoh penggunaan statement with membuka file:
with open('file.txt', 'r') as fileku:
    # Mengolah file
    print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# dalam tutorial ini akan selalu menggunakan statement with
