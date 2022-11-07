# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isascii#str.isascii

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isascii() mengembalikan nilai boolean True jika semua karakter adalah karakter ascii.
# jika tidak, maka akan mengembalikan nilai boolean False.

# Syntax
# string.isascii()

# Nilai Parameter
# tidak ada nilai parameter

x = "hello world!"
y = "~>!@#$%^&*()-=_+;<>?/,.0123{}'|\\"
print(x.isascii())  # True
print(y.isascii())  # True

# jalankan program di bawah ini:
# menampilkan semua kode dan karakter ascii
#for i in range(128):
#    if len(chr(i).encode("ascii")) == 1:
#        print(f"{i} --> {chr(i)}")

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan chr() kunjungi folder_name: "Fungsi-Bawaan/fungsi_chr.py"
# jika ingin mempelajari lebih lanjut tentang formating string kunjungi folder_name: "python-formatting"
