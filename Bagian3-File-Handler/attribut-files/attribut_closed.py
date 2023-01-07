# attribut 'closed' menyimpan informasi apakah file sedang terbuka atau sudah ditutup. 
# Nilainya bernilai True jika file sudah ditutup, dan False jika file masih terbuka.

# Syntax
# file.closed

# Nilai parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open("example.txt") as fileku:
    print("apakah file ditutup:", fileku.closed)
    # Output:
    # apakah file ditutup: False
print("apakah file ditutup:", fileku.closed)
# Output:
# apakah file ditutup: True
