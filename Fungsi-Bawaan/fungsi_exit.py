# -- Fungsi Bawaan --

# fungsi exit() digunakan untuk menghentikan program secara langsung.
# Saat fungsi exit() dipanggil, program akan segera berhenti dan keluar dari program tersebut.

# Syntax
# exit(code)

# Nilai Parameter
# Parameter                 Deskripsi
# code                      Opsional. yang menentukan kode keluaran (exit code) program. 

# tidak menggunakan fungsi exit()
def fungsiku1():
    try:
        # baris kode yang mungkin memicu exception
        x = 10 / 0
    except ZeroDivisionError as err:
        print(err)
fungsiku1()

# kode program dibawah ini dieksekusi

# menggunakan fungsi exit()
def fungsiku2():
    try:
        # baris kode yang mungkin memicu exception
        x = 10 / 0
    # menangkap jenis Error
    except ZeroDivisionError as err:
        # memasukan pesan error ke fungsi exit()
        exit(err)
fungsiku2()
# Output:
# division by zero

# kode program dibawah ini tidak dieksekusi
x = 100
y = 200
print(x + y)
print("hello world")

# Catatan:
# menggunakan fungsi exit() tidak harus di dalam block try except atau di dalam fungsi

# Pelajari lebih lanjut tentang exception error di folder_name: "python-exception"