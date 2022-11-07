# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isdigit#str.isdigit

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isdigit() mengembalikan nilai boolean True jika semua karakter adalah angka, 
# jika tidak, maka akan mengembalikan nilai boolean False.
# seperti eksponen/perpangkatan ⁰¹²³⁴⁵⁶⁷⁸⁹, unicode berjenis angka \u0030 juga dianggap digit
# jika unicode berjenis huruf maka akan False

# Syntax
# string.isdigit()

# Nilai Parameter
# tidak ada nilai parameter

exponen = "⁰¹²³⁴⁵⁶⁷⁸⁹"
print(exponen.isdigit())    # True

pecahan = "1½"
print(pecahan.isdigit())    # False

x = "2⁵"
print(x.isdigit())  # True

print("\u0030".isdigit())   # True
print("\u00B2".isdigit())   # True
print("\u0078".isdigit())   # False karena jenis unicode huruf 'x'
print("\u0079".isdigit())   # False karena jenis unicode huruf 'y'

# periksa apakah karakter unicode adalah jenis angka?
if "\u00B3".isdigit():
    print("passed")
else:
    print("failed")

x = "\u0030" # int 0 unicode
y = "\u0039" # int 9 unicode
print(x.isdigit())    # True
print(y.isdigit())    # True

print(int(x, base=16))  # 0
print(int(y, base=16))  # 9
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan int() kunjungi folder_name: "Fungsi-Bawaan/fungsi_int.py"

# jalankan kode dibawah ini:
# menghasilkan karakter unicode
#def kode_unicode(nomor_kode):
#    return chr(int(nomor_kode.lstrip("U+").zfill(3), base=16))
#
#for i in range(30, 81): # ubah nilai range(1, 1000)
#    print(fr"\u" + str(i).zfill(3), kode_unicode("U+" + str(i)))

# jika ingin mempelajari lebih lanjut tentang formating string kunjungi folder_name: "python-formatting"
# jika ingin mempelajari lebih lanjut tentang encoding unicode kunjungi folder_name: "python-encoding"
