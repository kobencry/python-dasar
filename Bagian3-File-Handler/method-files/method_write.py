# Method write() adalah method yang digunakan untuk menulis string ke file yang terbuka.
# Method ini hanya dapat digunakan pada file yang dibuka dengan mode 
# 'w', 'a', 'w+', 'wb' atau yang mengandung mode (write/tulis).

# Syntax
# file.write(byte)

# Nilai Parameter
# Parameter                 Deskripsi
# byte                      Teks atau objek byte yang akan disisipkan.

# membuka file dengan mode 'w' (write/tulis)
with open("file_demo_write.txt", 'w') as fileku:
    # menulis data ke file
    fileku.write("hello world\n")
# File akan ditutup secara otomatis setelah selesai mengolah

# untuk mengetahui isinya buka file tersebut atau buat kode program membaca file.
# membuka file dengan mode default 'r' (read/tulis) atau 't' (text/teks)
with open("file_demo_write.txt") as fileku:
    # membaca seluruh isi file
    print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah 
# Output:
# hello world

dataku = ('alice', 'carl', 'eliot')
# membuka file dengan mode 'a' (append/tambah)
with open("file_demo_write.txt", 'a') as fileku:
    # menulis data ke file 
    for i in dataku:
        fileku.write(i + '\n')
    # menulis data lain ke file
    fileku.write("ini adalah file demo write")
    # menggunakan attribut "name" dari objek file 
    print("selesai menambahkan data ke file:", fileku.name)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# selesai menambahkan data ke file: file_demo_write.txt

with open("file_demo_write.txt") as fileku:
    print(fileku.read())
# Output:
# hello world
# alice
# carl
# eliot
# ini adalah file demo write
