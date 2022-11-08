# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=rsplit#str.rsplit

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi rsplit() membagi string menjadi tipe data list, membaginya mulai dari kanan.
# Jika tidak ada parameter "maxsplit" yang ditentukan, fungsi ini akan mengembalikan sama seperti fungsi split().

# Catatan: Ketika maxsplit ditentukan, tipe data list akan berisi jumlah elemen yang ditentukan, ditambahkan satu.

# Syntax
# string.rsplit(separator, maxsplit)

# Nilai Parameter
# Parameter             Deskripsi
# separator             Opsional. Menentukan pemisah yang akan digunakan saat memisahkan string. Secara default/standarnya spasi putih apa pun adalah pemisah
# maxsplit              Opsional. Menentukan berapa banyak split yang harus dilakukan. Nilai default adalah -1, yang merupakan "semua kejadian"

x = "nama alice usia 23"
y = "nama;alice;usia;23;"

print(x.rsplit())    # ['nama', 'alice', 'usia', '23'] 
print(y.rsplit(';')) # ['nama', 'alice', 'usia', '23', '']

x = "nama alice usia 23"
y = "nama; alice; usia; 23"
print(x.rsplit(maxsplit=2)) # ['nama alice', 'usia', '23']
print(y.rsplit('; ', 1))    # ['nama; alice; usia', '23']

# jika ingin mempelajari lebih lanjut tentang Method-List kunjungi folder_name: "Method-List"
