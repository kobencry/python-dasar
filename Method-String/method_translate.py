# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=translate#str.translate

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi translate() mengembalikan string di mana beberapa karakter tertentu 
# diganti dengan karakter yang dijelaskan dalam tipe data dict,
# atau dalam tabel pemetaan.

# Gunakan fungsi maketrans() untuk membuat tabel pemetaan.
# Jika karakter tidak ditentukan dalam dict/tabel, karakter tidak akan diganti.
# Jika Anda menggunakan dict, Anda harus menggunakan kode ascii bukan karakter

# Syntax
# string.translate(tabel)

# Nilai Parameter
# Parameter                 Deskripsi
# tabel                     Dibutuhkan. Baik tipe data dict, atau tabel pemetaan yang menjelaskan cara melakukan penggantian.


text = "hello world"
# 101 -> 'e', 51 -> '3', 111 -> 'o', 48 -> '0'
kode_asci = {101: 51, 111: 48}
print(text.translate(kode_asci))    # h3ll0 w0rld

text = "hello alice carl eliot"
sumber = "aeio"
tujuan = "4310"
kode_asci = text.maketrans(sumber, tujuan)
print(text.translate(kode_asci))    # h3ll0 4l1c3 c4rl 3l10t

# jika ingin mempelajari lebih lanjut tentang kode ascii kunjungi folder_name: "python-encoding"
# jika ingin mempelajari lebih lanjut tentang Method-String maketrans() kunjungi folder_name: "Method-String/method_maketrans.py"
