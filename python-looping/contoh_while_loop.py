# Berikut ini adalah beberapa contoh kode nested while loop dengan bahasa Python:

# 1. Mencetak tabel perkalian dengan nested while loop

# Mendefinisikan variabel i sebagai 1
i = 1
# Memulai perulangan while
while i <= 10:
    # Mendefinisikan variabel j sebagai 1
    j = 1
    # Memulai perulangan while
    while j <= 10:
        # Mencetak hasil perkalian i dan j
        print(f"{i} x {j} = {i * j}")
        # Menambah nilai j dengan 1
        j += 1
    # Mencetak baris baru setelah setiap baris tabel perkalian
    print()   # kode ini setara dengan karakter '\n'(newline) atau print('')
    
    # Menambah nilai i dengan 1
    i += 1

#=============================================================================

# 2. Mencetak pola segitiga dengan nested while loop

# Mendefinisikan variabel i sebagai 1
i = 1
# Memulai perulangan while
while i <= 5:
    # Mendefinisikan variabel j sebagai 1
    j = 1
    # Memulai perulangan while
    while j <= i:
        # Mencetak bintang
        print("*", end='')
        # Menambah nilai j dengan 1
        j += 1
    # Mencetak baris baru setelah setiap baris pola segitiga
    print()   # kode ini setara dengan '\n'(newline) 
    # Menambah nilai i dengan 1
    i += 1

#=============================================================================

# 3. Mencetak pola kotak dengan nested while loop

# Mendefinisikan variabel i sebagai 1
i = 1
# Memulai perulangan while
while i <= 4:
    # Mendefinisikan variabel j sebagai 1
    j = 1
    # Memulai perulangan while
    while j <= 4:
        # Mencetak bintang atau spasi sesuai dengan kondisi
        if i == 1 or i == 4 or j == 1 or j == 4:
            print("*", end='')
        else:
            print(" ", end='')
        # Menambah nilai j dengan 1
        j += 1
    # Mencetak baris baru setelah setiap baris pola kotak
    print()
    # Menambah nilai i dengan 1
    i += 1

#=============================================================================

# Mencetak pola angka checkerboard dengan nested while loop

# Mendefinisikan variabel i sebagai 1
i = 1

# Memulai perulangan while
while i <= 4:
    # Mendefinisikan variabel j sebagai 1
    j = 1
    # Memulai perulangan while
    while j <= 4:
        print(j + i, end='')
        
        # Menambah nilai j dengan 1
        # j = j + 1
        # kode ini setara dengan diatas
        j += 1
    # Mencetak baris baru setelah setiap baris pola kotak
    print() # kode ini setara dengan karakter '\n'(newline) atau print('')
    # Menambah nilai i dengan 1
    i += 1
