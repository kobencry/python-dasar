# attribut 'mode'  menyimpan mode file yang sedang digunakan (misalnya 'r' untuk mode read, atau 'w' untuk mode write).

# Syntax
# file.mode

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("example.txt") as fileku:
    print("file mode:", fileku.mode)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# file mode: r

# membuka file dengan mode 'rb' (read/baca, binary/biner)
with open("example.txt", mode='rb') as fileku:
    print("file mode:", fileku.mode)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# file mode: rb