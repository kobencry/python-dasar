# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=replace#str.replace

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi replace() mengganti huruf string dengan huruf lain yang ditentukan.
# jika nilai tidak ada maka akan mengembalikan string asli.

# Syntax
# string.replace(nilai_lama, nilai_baru, jumlah)

# Nilai Parameter
# Parameter         Deskripsi
# nilai_lama        Dibutuhkan. String untuk mencari
# nilai_baru        Dibutuhkan. String untuk menggantikan nilai lama dengan nilai baru
# jumlah            Opsional. Jumlah menentukan berapa banyak kejadian dari nilai lama yang ingin Anda ganti. 
#                   Defaultnya adalah semua kejadian

s = "hello world!"
x = s.replace('hello', 'war')
print(x)    # war world

s = "hello world!"
x = s.replace('word', 'false')
print(x)    # hello world!

s = "hello world"
print(s.replace('world', 'alice'))  # hello alice

s = "tak tik tuk tek tok"
x = s.replace('t', 'b', 3)
print(x)    # bak bik buk tek tok

# Hati-hati jika karakter \n (LF) yang digunakan di os Unix, termasuk Mac, dan
# \r\n (CR + LF) yang digunakan di os Windows dicampur.
# Karena karakter \n(newline) termasuk dalam \r\n, hasil yang diinginkan tidak
# dapat diperoleh tergantung pada urutannya. 
# Contoh berikut juga menunjukkan hasil repr() yang menghasilkan \n dan \r sebagai string.

text = "alice\nbob\r\neliot"
print(text.replace('\r\n', '-').replace('\n', '-')) # alice-bob-eliot
print(text.replace('\n', '-').replace('\r\n', '-')) # -eliot-bob


# Ingat: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.
s = "hello world"
# string melakukan perubahan
print(s.replace('hello', 'war'))    # war world
# string tidak melakukan perubahan
print(s)    # hello world

# string tidak melakukan perubahan
s = "hello world"
s.replace('hello', 'war')
print(s)    # hello world
# jika ingin mempelajari lebih lanjut tentang escape/pelarian karakter kunjungi folder_name: "Bagian1-DASAR/stage13_escape_character.py"
