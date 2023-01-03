# Mode 'w' (write/tulis) untuk menulis isi file
# Saat menggunakan mode ini, kita tidak dapat membaca isi file,
# namun dapat menulis atau mengubah isi file tersebut. 
# Jika file yang dibuka dengan mode ini sudah ada, 
# maka isi file tersebut akan ditimpa (overwritten) dengan data yang baru ditulis. 
# Jika file belum ada, maka file tersebut akan tercipta dengan sendirinya.

# Contoh penggunaan mode 'w' pada objek file adalah sebagai berikut:
with open("filedemo.txt", mode="w") as fileku:
    # menulis string ke file
    fileku.write("hello world\n")
    fileku.write("alice\n")
# File akan ditutup secara otomatis setelah selesai mengolah

# membaca file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("filedemo.txt") as f:
    # membaca seluruh isi file
    print(f.read())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# hello world
# alice

# jika file tersebut sudah ada maka isi file akan ditimpa(overwrite)
dataku = ('='*25, 'carl', 'eliot')
with open("filedemo.txt", mode='w') as fileku:
    # menulis string ke file
    fileku.write("isi file telah ditimpah\n")
    for i in dataku:
        fileku.write(i + '\n')
    fileku.write("ini adalah file demo")
# File akan ditutup secara otomatis setelah selesai mengolah

# membaca file dengan mode default
with open("filedemo.txt") as f:
    print(f.read())
# Output:
# isi file telah ditimpah
# =========================
# carl
# eliot
# ini adalah file demo

# Mode 'w+'  
