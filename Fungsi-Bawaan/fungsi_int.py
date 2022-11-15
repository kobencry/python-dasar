# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-int#int
# https://docs.python.org/3/library/stdtypes.html?highlight=int#int.bit_length

# fungsi int() mengubah nilai yang ditentukan menjadi bilangan bulat/int

# Syntax:
# int(value, base)

# Nilai Parameter:
# Parameter                     Deskripsi
# value                         Dibutuhkan. Angka atau string yang dapat diubah menjadi bilangan bulat
# base                          opsional. Angka yang mewakili format angka. Nilai default: 10

print(int("11")) # default
# 11
print(int("11", base=2)) # biner
# 3
print(int("11", base=8)) # octal
# 9
print(int("11", base=10)) # default
# 11
print(int("11", base=16)) # hexa 
# 17
print(int(11 - 9))
# 2
print(int.from_bytes(b"\x0f", "little"))
# 15
print(int.from_bytes(b"\xc0\xff\xee", "big"))
# 12648430

#===============================================================================

# Method/metode tambahan pada fungsi int()

# Tipe integer mengimplementasikan angka.
# class dasar abstrak Integral.
# Selain itu, ini menyediakan beberapa metode lagi:

#-------------------------------------------------------------------------------
# int.bit_length()
# megembalikan jumlah bit yang diperlukan untuk mewakili bilangan bulat dalam biner, 
# tidak termasuk tanda dan nol di depan.

x = 225
y = -225
# print(bin(x))   # 0b11100001
# print(bin(y))   # -0b11100001
# tanda '0b' dan '-0b' tidak dihitung 
print(x.bit_length())   # 8
print(y.bit_length())   # 8

# fungsi kode ini setara dengan diatas 
def panjang_bit(angka):
    # mengembalikan dalam tipe biner '0b'
    string_byte = bin(angka)
    # menghapus karakter tipe biner negatif '-0b'
    string_byte = string_byte.lstrip('-0b')
    # menghitung jumlah biner '1010101'
    return len(string_byte)
print(panjang_bit(x))   # 8
print(panjang_bit(y))   # 8

#-------------------------------------------------------------------------------
# int.bit_count()
# mengembalikan jumlah angka satu dalam representasi biner dari nilai absolut bilangan bulat.
x = 225
y = -225
print(bin(x))   # 0b11100001 
print(bin(y))   # -0b11100001
# tanda '0b', '-0b' dan '0' tidak dihitung
print(x.bit_count())    # 4
print(y.bit_count())    # 4

# fungsi kode ini setara dengan di atas
def jumlah_bit(angka):
    return bin(angka).count('1')
print(jumlah_bit(225))  # 4
print(jumlah_bit(-225)) # 4

#-------------------------------------------------------------------------------
# int.to_bytes(length=1, byteorder='big', *, signed=False)
# mengembalikan byte array yang mewakili bilangan bulat.
x = 225
y = -225

print(x.to_bytes(2, byteorder='little')) # b'\xe1\x00'
print(x.to_bytes(2, byteorder='big'))    # b'\x00\xe1'
print(x.to_bytes(5, byteorder='little')) # b'\xe1\x00\x00\x00\x00'
print(x.to_bytes(5, byteorder='big'))    # b'\x00\x00\x00\x00\xe1'
print(x.to_bytes(5, byteorder='little', signed=True)) # b'\xe1\x00\x00\x00\x00'
print(x.to_bytes(5, byteorder='big', signed=True))    # b'\x00\x00\x00\x00\xe1'

# gunakan parameter signed=True untuk menangani nilai byte negagif/minus
print(y.to_bytes(2, byteorder='little', signed=True))   # b'\x1f\xff'
print(y.to_bytes(2, byteorder='big', signed=True))      # b'\xff\x1f'
print(y.to_bytes(5, byteorder='little', signed=True))   # b'\x1f\xff\xff\xff\xff'
print(y.to_bytes(5, byteorder='big', signed=True))      # b'\xff\xff\xff\xff\x1f'

# kesimpulan diatas adalah nilai integer diwakili menggunakan byte panjang, dan defaultnya adalah 1.
# jika nilai integer tidak dapat di representasikan dengan jumlah byte yang diberikan, maka kesalahan runtime OverflowError dimunculkan. 
# argumen byteorder menentukan urutan byte yang digunakan untuk mewakili bilangan bulat, dan defaultnya adalah "big"/"besar".
# Jika byteorder adalah "big", byte yang paling signifikan berada di awal array byte. 
# Jika byteorder adalah "little"/"kecil", byte yang paling signifikan berada di akhir array byte.
# b'\xe1\x00' -> little
# b'\x00\xe1' -> big

# Argumen signed menentukan apakah komplemen dua digunakan untuk mewakili bilangan bulat.
# Jika argumen signed adalah False dan diberikan bilangan bulat negatif, maka kesalahan runtime OverflowError dimunculkan.
# Nilai default/standarnya untuk signed adalah False.
# Nilai default/standarnya dapat digunakan untuk mengubah integer menjadi objek byte tunggal dengan mudah.
# Namun, saat menggunakan argumen default, jangan mencoba mengonversi nilai yang lebih besar dari 255 
# atau anda akan mendapatkan kesalahan runtime OverflowError:
print((64).to_bytes(1, byteorder='little')) # '@'
# jalankan program dibawah ini:
# menampilkan tabel ascii
#for i in range(128):
#    print(int(i).to_bytes(1, byteorder='little'))

# fungsi kode ini setara dengan diatas
def ke_bytes(angka, panjang, byteorder='besar', signed=False):
    if byteorder == 'kecil':
        order = range(panjang)
    elif byteorder == 'besar':
        order = reversed(range(panjang))
    else:
        raise ValueError("byteorder harus 'kecil' atau 'besar'")
    return bytes((angka >> i * 8) & 0xff for i in order)

print(ke_bytes(64, panjang=1, byteorder='kecil'))   # b'@'

#-------------------------------------------------------------------------------
# int.from_bytes(bytes, byteorder='big', *, signed=False)
# mengembalikan nilai integer/bilangan bulat oleh byte array yang diberikan.
x = b'\xe1\x00'
y = b'\x1f\xff'
print(int.from_bytes(x, byteorder='little'))    # 225
print(int.from_bytes(x, byteorder='big'))       # 57600
print(int.from_bytes(y, byteorder='little', signed=True))   # -225
print(int.from_bytes(y, byteorder='big', signed=True))      # 8191

print(int.from_bytes(b"@", byteorder='big'))    # 64

# fungsi kode ini setara dengan diatas
def dari_bytes(bit, byteorder='besar', signed=False):
    if byteorder == 'kecil':
        l_ordered = list(bit)
    elif byteorder == 'besar':
        l_ordered = list(reversed(bit))
    else:
        raise ValueError("byteorder harus 'kecil' atau 'besar'")
    x = sum(b << i * 8 for i, b in enumerate(l_ordered))
    if signed and l_ordered and (l_ordered[-1] & 0x80):
        x -= 1 << 8 * len(l_ordered)
    return x
print(dari_bytes(b'\xe1\x00', byteorder='kecil'))   # 225
print(dari_bytes(b'\xe1\x00', byteorder='besar'))   # 57600

#-------------------------------------------------------------------------------
# mengembalikan sepasang bilangan bulat yang rasionya sama persis dengan bilangan float asli dan dengan penyebut positif.
# bilangan bulat rasio, bilangan bulat (whole number) selalu bilangan bulat sebagai pembilang dan 1 sebagai penyebut.
x = 2.5
print(x.as_integer_ratio()) # (5, 2)
l = x.as_integer_ratio()
print(f"{l[0]} / {l[1]}")   # 5 / 2

# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan range() kunjungi folder_name: "Fungsi-Bawaan/fungsi_range.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan enumerate() kunjungi folder_name: "Fungsi-Bawaan/fungsi_enumerate.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan len() kunjungi folder_name: "Fungsi-Bawaan/fungsi_len.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan reversed() kunjungi folder_name: "Fungsi-Bawaan/fungsi_reversed.py"
# jika ingin mempelajari lebih lanjut tentang fungsi-bawaan sum() kunjungi folder_name: "Fungsi-Bawaan/fungsi_sum.py"
# jika ingin mempelajari lebih lanjut tentang python-encoding tabel ascii kunjungi folder_name: "python-encoding"
# jika ingin mempelajari lebih lanjut tentang python-operator kunjungi folder_name: "python-operator"
