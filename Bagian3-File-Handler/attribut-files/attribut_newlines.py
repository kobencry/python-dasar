# attribut 'newlines' menyimpan informasi tentang newline yang digunakan pada file.
# Nilainya hanya berlaku untuk file yang berisi teks (text file).

# Syntax
# file.newlines

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("example.txt") as fileku:
    print(fileku.newlines)
# File akan ditutup secara ototmatis setelah selesai mengolah
# Output:
# None
