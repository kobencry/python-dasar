# UTF-8 adalah sebuah encoding karakter yang memungkinkan kita menyimpan data teks dalam bentuk byte.
# prefix code(Kode awalan) dalam UTF-8 digunakan untuk menandakan berapa banyak byte 
# yang dibutuhkan untuk menyimpan sebuah karakter dalam memori.
# Ini membantu decoder menentukan apakah sejumlah byte tertentu merupakan bagian dari
# satu karakter atau beberapa karakter yang berbeda.
# Contohnya, karakter latin seperti "a" hanya membutuhkan satu byte untuk disimpan dalam UTF-8,
# sehingga byte pertama yang merepresentasikan karakter "a" memiliki nilai decimal 97 (0x61 dalam hexadecimal).
# Sementara itu, karakter emoji seperti "✨" membutuhkan tiga byte untuk disimpan dalam UTF-8,
# dan byte pertama memiliki nilai decimal 226 (0xe2 dalam hexadecimal), 
# yang menunjukkan bahwa ada dua byte lain yang berikutnya akan membentuk karakter tersebut.

# Contoh kode UTF-8:
# Jika kita memiliki karakter "A" yang memiliki kode Unicode 65, maka kode UTF-8 untuk karakter "A" adalah 0x41.
# Jika kita memiliki karakter "✨" yang memiliki kode Unicode U+2728, maka kode UTF-8 untuk karakter "✨" adalah 0xe2 0x9c 0xa8'.
# Dalam contoh kode UTF-8 di atas, kode prefix menunjukkan bahwa ada 4 byte yang digunakan untuk menyimpan karakter "✨" dalam bentuk byte.

berkilau = "✨"
print(berkilau.encode('utf-8'))
# Output:
# b'\xe2\x9c\xa8'

print(f"{0xe2:08b}") # 11100010

# Ketiga byte \xe2\x9c\xa8 adalah representasi numerik dari emoji "✨" dalam UTF-8.
# Kemudian, kode awalan dalam UTF-8 dapat dilihat dari byte pertama (dalam hal ini, \xe2).
# Byte pertama menunjukkan jumlah byte dalam urutan:
# 0xxxxxxx (7 bit) menunjukkan 1 byte
# 110xxxxx (5 bit) + 10xxxxxx (6 bit) menunjukkan 2 byte
# 1110xxxx (4 bit) + 10xxxxxx (6 bit) + 10xxxxxx (6 bit) menunjukkan 3 byte
# 11110xxx (3 bit) + 10xxxxxx (6 bit) + 10xxxxxx (6 bit) + 10xxxxxx (6 bit) menunjukkan 4 byte
# Dalam hal ini, \xe2 memiliki nilai biner 11100010, sehingga menunjukkan bahwa emoji "✨" memerlukan 3 byte dalam representasi UTF-8-nya.
# kunjungi tentang utf-8: https://en.wikipedia.org/wiki/UTF-8