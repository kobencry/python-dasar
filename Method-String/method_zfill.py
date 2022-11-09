# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=zfill#str.zfill

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi zfill() menambahkan angka nol (0) di awal string, hingga mencapai panjang yang ditentukan.
# Jika nilai parameter val kurang dari panjang string, tidak ada pengisian/penambahan yang dilakukan.

# Syntax
# string.zfill(val)

# Nilai Parameter
# Parameter             Deskripsi
# val                   Dibutuhkan. Angka yang menentukan panjang string yang diinginkan


x = "hello"
print(x.zfill(5))   # hello
print(x.zfill(6))   # 0hello
print(x.zfill(10))  # 00000hello
print(x.zfill(20))  # 000000000000000hello

x = "123"
print(x.zfill(3))   # 123
print(x.zfill(5))   # 00123
print(x.zfill(10))  # 0000000123


# menghasilkan karakter unicode
def kode_unicode(nomor_kode):
    return chr(int(nomor_kode.lstrip("U+").zfill(3), base=16))

for i in range(30, 81): # ubah nilai range(1, 1000)
    print(fr"\u" + str(i).zfill(3), kode_unicode("U+" + str(i)))

# jika ingin mempelajari lebih lanjut tentang formating string kunjungi folder_name: "python-formatting"
# jika ingin mempelajari lebih lanjut tentang encoding unicode kunjungi folder_name: "python-encoding"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan str(), chr(), dan int() kunjungi folder_name: "Fungsi-Bawaan"
