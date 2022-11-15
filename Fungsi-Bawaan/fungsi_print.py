# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-print#print

# fungsi print() mencetak pesan yang ditentukan ke layar, atau perangkat output standar lainnya.
# pesan dapat berupa string, atau objek lain, objek tersebut akan diubah menjadi string sebelum ditulis ke layar.

# Syntax: 
# print(objek1, objek2, ..dst, sep=separator, end=end, file=file, flush=flush)

# Nilai Parameter:
# Parameter         Deskripsi
# objek1,2,..dst    Dibutuhkan. Objek apa saja, dan sebanyak yang Anda suka. Akan dikonversi ke string sebelum dicetak
# sep='separator'   Opsional. Tentukan cara memisahkan objek, jika ada lebih dari satu. Standarnya adalah '' atau (spasi)
# end='end'         Opsional. Tentukan apa yang akan dicetak di bagian akhir. Defaultnya adalah '\n' (umpan baris)
# file=file         Opsional. Sebuah objek dengan metode menulis. Standarnya adalah sys.stdout
# flush=flush       Opsional. Sebuah Boolean, menentukan apakah output mengalir (True) atau buffer (False). Defaultnya False

# menggunakan argumen objek
print("hello", 'world', 123, True, None, 0xff) # hello world 123 True None 255

# menggunakan argumen sep='separator'
print("hello", "world", sep="")      # helloworld
print("hello", "world", sep="#")     # hello#world
print("alice", "gmail.com", sep="@") # alice@gmail.com
# contoh yang lebih berguna dari parameter sep tersebut adalah mencetak sesuatu seperti jalur file
print("home", "usr", "bin", sep="/") # home/usr/bin
print("hello", "world", sep="\n")    # hello\nworld

# Satu contoh yang lebih menarik dapat mengekspor data ke format nilai yang dipisahkan koma (CSV)
print("alice", "23", "10/4/2022", "jakarta", sep=",") # alice,23,10/4/2022,jakarta

# parameter sep tidak dibatasi hanya untuk satu karakter. 
# Anda dapat menggabungkan elemen dengan string dengan panjang berapapun.
print("alice", "carl", "eliot", sep=" -> ") # alice -> carl -> eliot

#==========================================================

# menggunakan argumen end=end
# Seperti halnya sep, Anda dapat menggunakan end untuk menggabungkan bagian individu menjadi
# gumpalan teks besar dengan pemisah khusus. Alih-alih menggabungkan beberapa argumen,
# bagaimanapun, itu akan menambahkan teks dari setiap panggilan fungsi ke baris yang sama
print("hello", end="")
print("world")
# >>> helloworld
# ketiga kode ini akan menghasilkan satu baris teks
print("alice", end=" ")
print("carl", end=" ")
print("eliot")
# alice carl eliot

print("hello", end="\n")
print("world")
# hello
# world

# Anda dapat mencampur dua argumen keyword sep dan end
# Anda tidak hanya mendapatkan satu baris teks, 
print("alice", "bob", sep=" -> ", end=" >>> ")
print("eliot", "geral")
# alice -> bob >>> eliot geral

#==========================================================
import sys # pelajari lebih lanjut tentang modul sys di folder_name: "modul-sys"

# menggunakan argumen file=file
# Percaya atau tidak, fungsi-bawaan print() tidak tahu cara mengubah pesan menjadi teks di layar Anda,
# dan terus terang itu tidak perlu. itu adalah tugas untuk lapisan kode tingkat rendah, 
# yang memahami byte dan mengetahui cara mendorongnya.
# fungsi print() adalah abstraksi di atas lapisan ini, menyediakan antarmuka yang nyaman yang hanya 
# mendelegasikan pencetakan sebenarnya, ke aliran atau objek seperti file.
# aliran dapat berupa file apa pun di disk Anda, soket jaringan, atau mungkin buffer dalam memori.
# Selain itu, ada tiga aliran standar yang disediakan oleh sistem operasi:

# stdin : masukan standar
# stdout: keluaran standar
# stderr: kesalahan standar

print(sys.stdin)
print(sys.stdout)
print(sys.stderr)
#------------------------------------------
# Secara default, fungsi print() terikat sys.stdout melalui file argumennya, tetapi Anda bisa mengubahnya.
# Gunakan argumen kata kunci tersebut untuk menunjukkan file yang dibuka dalam mode tulis atau tambahkan,
# sehingga pesan langsung masuk ke sana.
with open('file.txt', mode='w') as tulis:
    print('hello world', file=tulis)

#-------------------------------------------
# Catatan: 
# Jangan coba gunakan fungsi print() untuk menulis data biner karena ini hanya cocok untuk teks.
# Panggil saja file biner .write() secara langsung.
with open('file.dat', mode='wb') as wb:
    wb.write(bytes(4))
    wb.write(b'\xff')

#-------------------------------------------
with open('file.dat', mode='rb') as rb:
    print(rb.read())

# Jika Anda ingin menulis byte mentah pada keluaran standar, 
# maka ini juga akan gagal karena sys.stdout merupakan aliran karakter:
# sys.stdout.write(bytes(4))
# Anda harus menggali lebih dalam untuk mendapatkan pegangan dari aliran byte yang mendasarinya:
sys.stdout.buffer.write(b'\x41\x0a')

#--------------------------------------------
with open('file.txt', mode='w', encoding='iso-8859-1') as wb:
    print('über naïve café', file=wb)
print()

#==========================================================
import time # pelajari lebih lanjut tentang modul time di folder_name: "modul-time"

# menggunakan argumen flush=flush
# argumen flush yang memungkinkan pengguna untuk memutuskan apakah dia ingin outputnya disangga atau tidak.
# Nilai default dari ini adalah False artinya output akan disangga. 
# Jika Anda mengubahnya menjadi True, output akan ditulis sebagai urutan karakter satu demi satu

print("menggunakan flush=False")
for i in range(10):
    print(end='#', flush=False)
    time.sleep(1)
print("\tselesai")

print("menggunakan flush=True")
for i in range(10):
    print(end="#", flush=True)
    time.sleep(1)
print("\tselesai")

# Benar-benar sebuah overhead! Masuk akal untuk menunggu hingga setidaknya beberapa karakter
# diketik dan kemudian mengirimkannya bersama-sama. Di situlah buffering masuk.
# Di sisi lain, buffering terkadang memiliki efek yang tidak diinginkan seperti yang baru saja Anda lihat
# pada contoh diatas. untuk memperbaikinya, Anda cukup memberi tahu print() untuk 
# mengosongkan aliran secara paksa tanpa menunggu karakter baris baru di buffer menggunakan flush=True

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
