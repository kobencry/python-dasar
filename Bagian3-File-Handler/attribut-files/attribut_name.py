# attribut 'name' menyimpan nama file yang sedang dibuka.

# Syntax
# file.name

# Nilai parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r'(read/baca) atau 't'(text/teks)
with open("example.txt") as fileku:
    print("nama file:", fileku.name)
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# nama file: example.txt
