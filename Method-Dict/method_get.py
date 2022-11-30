# -- Method Dictionary --

# https://docs.python.org/3/library/stdtypes.html?#dict.get

# fungsi get() mengembalikan value/nilai item dengan nama keys/kunci yang ditentukan.

# Syntax
# dictionary.get(namakey, value)

# Nilai Parameter
# Parameter                 Deskripsi
# namakey                   Dibutuhkan. namakey item yang ingin Anda kembalikan nilainya.
# value                     Opsional. Nilai untuk dikembalikan jika keys/kunci yang ditentukan tidak ada.# value/nilai default None/Tidak ada.


dictku = {'nama':'alice', 'usia':23}
x = dictku.get('alamat')    # menggunakan pesan default
print(x)    # None 
y = dictku.get('alamat', 'tidak ada')
print(y)    # tidak ada     # menggunakan pesan tersendiri

print(dictku.get('nama'))   # alice
print(dictku.get('usia'))   # 23
print(dictku.get('alamat', 'xxxx')) # xxxx
