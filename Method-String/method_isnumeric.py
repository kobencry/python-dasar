# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isnumeric#str.isnumeric

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isnumeric() mengembalikan nilai boolean True jika semua karakter numerik (0-9),
# jika tidak, maka akan mengembalikan nilai boolean False.
# seperti eksponen/perpangkatan ⁰¹²³⁴⁵⁶⁷⁸⁹, pecahan ½ ¾, unicode jenis angka,
# juga dianggap sebagai nilai numerik.

# nilai minus "-1" dan nilai float "1.5" TIDAK dianggap sebagai nilai numerik

# Syntax
# string.isnumeric()

# Nilai Parameter
# tidak ada nilai parameter

pecahan = "½"
exponen = "5⁵"
print(pecahan.isnumeric()) # True
print(exponen.isnumeric()) # True
print("0".isnumeric())  # True

x = "1.5"
y = "-5"
print(x.isnumeric()) # False
print(y.isnumeric()) # False

# periksa apakah nilai unicode termasuk numerik?
if "\u00B3".isnumeric():
    print("passed")
else:
    print("failed")

x = "\u0030"    # unicode jenis angka
y = "\u0039"    # unicode jenis angka
print(x.isnumeric())
print(y.isnumeric())

print(int(x, base=16))  # 0
print(int(y, base=16))  # 9
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan int() kunjungi folder_name: "Fungsi-Bawaan/fungsi_int.py"

x = "\u0078"    # unicode jenis huruf
y = "\u0079"    # unicode jenis huruf
print(x.isnumeric()) # False
print(y.isnumeric()) # False

# jalankan kode dibawah ini:
# menghasilkan karakter unicode
#def kode_unicode(nomor_kode):
#    return chr(int(nomor_kode.lstrip("U+").zfill(3), base=16))
#
#for i in range(30, 81): # ubah nilai range(1, 1000)
#    print(fr"\u" + str(i).zfill(3), kode_unicode("U+" + str(i)))

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan chr() kunjungi folder_name: "Fungsi-Bawaan/fungsi_chr.py"
# jika ingin mempelajari lebih lanjut tentang formating string kunjungi folder_name: "python-formatting"
# jika ingin mempelajari lebih lanjut tentang encoding unicode kunjungi folder_name: "python-encoding"
