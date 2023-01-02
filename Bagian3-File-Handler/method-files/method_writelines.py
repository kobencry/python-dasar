# Method writelines() adalah method yang digunakan untuk menulis beberapa string sekaligus ke file yang terbuka.
# Method ini hanya dapat digunakan pada file yang dibuka dengan mode 
# 'w', 'a', 'w+', 'wb' atau yang mengandung mode (write/tulis).

# Syntax
# file.writelines(list)

# Nilai Parameter
# Parameter                 Deskripsi
# list                      Daftar teks atau objek byte yang akan disisipkan.

# membuka file dengan mode 'w' (write/tulis)
with open("file_demo_writelines.txt", 'w') as fileku:
    # menulis item list ke file
    # tambahkan baris baru ('\n'newline) untuk memisahkan string
    fileku.writelines(['hello world\n', 'alice\n', 'carl\n'])
# File akan ditutup secara otomatis setelah selesai mengolah

# untuk mengetahui isinya buka file tersebut atau buat kode program membaca file.
# membuka file dengan mode default 'r' (read/tulis) atau 't' (text/teks)
with open("file_demo_writelines.txt") as fileku:
    # membaca seluruh isi file
    print(fileku.read())
# File akan ditutup secara otomatis setelah selesai mengolah 
# Output:
# hello world
# alice
# carl

dataku = ('eliot\n', 'ini adalah file demo writelines')
# membuka file dengan mode 'a' (append/tambah)
with open("file_demo_writelines.txt", 'a') as fileku:
    # menulis item tuple ke file
    fileku.writelines(dataku)
    # menggunakan attribut "name" dari objek file
    print("selesai menambahkan data ke file:", fileku.name)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# selesai menambahkan data ke file: file_demo_writelines.txt

# membaca seluruh isi file
with open("file_demo_writelines.txt") as fileku:
    print(fileku.read())
# Output:
# hello world
# alice
# carl
# eliot
# ini adalah file demo writelines
