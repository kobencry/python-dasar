# attribut 'mode'  menyimpan mode file yang sedang digunakan (misalnya 'r' untuk mode read, atau 'w' untuk mode write).

# Syntax
# file.mode

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("example.txt") as fileku:
    print("file mode:", fileku.mode)
# File akan ditutup secara ototmatis setelah selesai mengolah
# Output:
# file mode: r
