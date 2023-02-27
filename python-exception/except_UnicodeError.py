# -- python exception --

# https://docs.python.org/3/library/exceptions.html#UnicodeError

# UnicodeError adalah sebuah exception yang terjadi ketika terjadi kesalahan dalam 
# encoding atau decoding karakter Unicode. 
# Exception ini merupakan subclass dari ValueError.
# Ketika UnicodeError terjadi, atribut-atribut yang dapat digunakan untuk mengakses informasi 
# tentang kesalahan encoding atau decoding meliputi 
# encoding (nama encoding yang menyebabkan error), 
# reason (deskripsi kesalahan spesifik), 
# object (objek yang sedang di encoding/decoding), 
# start (indeks awal data yang tidak valid pada objek), dan 
# end (indeks setelah data terakhir yang tidak valid pada objek). 
# Dengan menggunakan atribut-atribut tersebut, kita dapat mengakses dan memperbaiki 
# kesalahan pada encoding atau decoding karakter Unicode.
# # Hal ini dapat terjadi jika sebuah string yang tidak valid di-encode atau di-decode.

try:
    # mencoba melakukan encoding pada string yang mengandung karakter unicode 
    # yang tidak valid untuk karakter ascii
    string_unicode = "ålice".encode('ascii')
    print(string_unicode)
except UnicodeError as err:
    print("Pesan Error:", err)
    print("atribut encoding:", err.encoding)
    print("atribut reason:", err.reason)
    print("atribut object:", err.object[err.start:err.end])
    print("atribut start:", err.start)
    print("atribut end:", err.end)
# Output:
# Pesan Error: 'ascii' codec can't encode character '\xe5' in position 0: ordinal not in range(128)
# atribut encoding: ascii
# atribut reason: ordinal not in range(128)
# atribut object: å
# atribut start: 0
# atribut end: 1

# Beberapa exception terkait UnicodeError yang menjadi subclass dari ValueError, 
# seperti UnicodeDecodeError dan UnicodeEncodeError.

try:
    # karakter string "ålice" di-encode
    text = "ålice"
    print(text.encode(encoding="ascii",errors="strict"))
except UnicodeError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
    
# Output:
# Nama Class Error: <class 'UnicodeEncodeError'>
# Pesan Error: 'ascii' codec can't encode character '\xe5' in position 0: ordinal not in range(128)

try:
    # karakter string "ålice" di-decode
    text = "ålice"
    var = text.encode()
    print(var.decode(encoding="ascii", errors="strict"))
except UnicodeError as err:
    print("Nama Class Error:", err.__class__)
    print("Pesan Error:", err)
# Output:
# Nama Class Error: <class 'UnicodeDecodeError'>
# Pesan Error: 'ascii' codec can't decode byte 0xc3 in position 0: ordinal not in range(128)