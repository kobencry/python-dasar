# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=maketrans#str.maketrans

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi maketrans() mengembalikan tabel pemetaan yang dapat digunakan dengan 
# fungsi translate() untuk mengganti karakter yang ditentukan.

# Syntax
# string.maketrans(sumber, tujuan, hapus)

# Nilai Parameter
# Parameter             Deskripsi
# sumber                Dibutuhkan. Jika hanya satu parameter yang ditentukan, 
#                       ini harus berupa dict yang menjelaskan cara melakukan penggantian.
#                       jika dua atau lebih parameter ditentukan, parameter ini harus berupa string yang menentukan karakter yang ingin Anda ganti.
# tujuan                Opsional. Sebuah string dengan panjang yang sama dengan parameter x. 
#                       Setiap karakter dalam parameter pertama akan diganti dengan karakter yang sesuai dalam string ini.
# hapus                 Opsional. String yang menjelaskan karakter mana yang akan dihapus dari string asli.


text = "Hello world"
x = "eo"
y = "30"
# mengembalikan dict dalam kode ascii
print(text.maketrans(x, y)) # {101: 51, 111: 48}
tabel_ascii = text.maketrans(x,y)
print(text.translate(tabel_ascii)) # H3ll0 w0rld

sumber = "aAeEiItT"
tujuan = "44331177"
# mengembalikan dict dalam kode ascii
tabel_ascii = str.maketrans(sumber, tujuan)
print(tabel_ascii)  # {97: 52, 65: 52, 101: 51, 69: 51, 105: 49, 73: 49, 116: 55, 84: 55}

text = "Hello Alice, carl, eliot".translate(tabel_ascii)
print(text) # H3llo 4l1c3, c4rl, 3l1o7

# menghapus karakter yang ditentukan
sumber = "aAeit"
tujuan = "44317"
hapus = "aei"
tabel_ascii = str.maketrans(sumber, tujuan, hapus)
print(tabel_ascii)  # {97: None, 65: 52, 101: None, 105: None, 116: 55}

text = "Hello Alice, carl, eliot".translate(tabel_ascii)
print(text) # Hllo 4lc, crl, lo7

# jika ingin mempelajari lebih lanjut tentang Method-String translate() kunjungi folder_name: "Method-String/fungsi_translate.py"
# jika ingin mempelajari lebih lanjut tentang Method-Dict kunjungi folder_name: "Method-Dict"
# jika ingin mempelajari lebih lanjut tentang encoding ascii kunjungi folder_name: "python-encoding"
