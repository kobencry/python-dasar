# Nested while loop adalah sebuah perulangan while di dalam perulangan while lainnya. 
# Dalam bahasa Python, kita dapat menggunakan perulangan while dalam perulangan while lainnya
# untuk mengeksekusi blok kode berulang kali sampai kondisi yang ditentukan terpenuhi.
# Ini berguna ketika kita ingin mengeksekusi suatu blok kode berulang kali sampai kondisi yang ditentukan terpenuhi,
# dan juga ingin mengeksekusi blok kode lainnya berulang kali sampai kondisi yang berbeda terpenuhi.

# Misalnya, kita dapat menggunakan nested while loop untuk mencetak angka dari 1 sampai 5 di setiap baris, seperti ini:

# Inisialisasi variabel yang akan digunakan dalam nested while loop
x = 1  # Variabel untuk perulangan pertama
y = 1  # Variabel untuk perulangan kedua

# Mulai nested while loop
while x <= 5:
    while y <= 5:
        # Cetak angka
        print(y, end=" ")

        # Increment variabel y 
        # y = y + 1
        # kode ini setara dengan diatas
        y += 1
    
    # Increment variabel x 
    # x = x + 1
    # kode ini setara dengan diatas
    x += 1
    
    # Reset variabel y 
    y = 1
    
    # Tambahkan baris baru setelah mencetak angka di setiap baris
    print() # kode ini setara dengan karakter '\n' newline

# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5
# 1 2 3 4 5

# menggunakan fungsi bawaan python input()
while True:
    user_input = input("tekan [y]es/[n]ext/[q]uit: ")
    # yes: menggunakan nested while loop
    # next: melanjutkan while loop luar
    # quit: berhenti looping
    if user_input in ('y', 'yes'):
        # inisialisasi variabel
        x = 1
        while x <= 5:
            # akan mencetak 'hello world' 5 kali
            print("hello world")
            # increment variabel x
            x += 1
        # jika kode diatas sudah terpenuhi lanjutkan while loop luar 
        continue

    # kondisi dimana user ingin keluar
    elif user_input in ('q', 'quit'):
        print('stop looping')
        break

    # kondisi dimana user ingin next atau apapun
    else:
        print(user_input)

# kita bisa membuat berbagai bentuk pola bintang dan angka
i = 1
while i <= 5:
    x = 1
    while x <= i:
        print('*', end='')
        # increment variabel y
        x += 1
    
    print()
    # increment variabel x
    i += 1
# *
# **
# ***
# ****
# *****

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan print() kunjungi folder_name: "Fungsi-Bawaan/fungsi_print.py"
