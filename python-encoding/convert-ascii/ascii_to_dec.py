# mengubah karakter ascii ke decimal(basis 10)
def convert_ascii(s:str) -> str:
    # Metod ini baru diperkenalkan pada Python 3.7 dan mengembalikan True jika semua karakter dalam string adalah ASCII.
    # menggunakan fungsi-string .isascii() untuk memastikan bahwa string input adalah ASCII.
    # buka folder python-string/metod_string file "metod_isascii.py"
    if not s.isascii():
        # Jika string bukan karakter ASCII, maka fungsi akan melemparkan error "ValueError" dengan pesan "bukan tabel ascii".
        raise ValueError("bukan karakter ascii")
    # Jika string hanya terdiri dari karakter ASCII, 
    # akan mengembalikan string hasil konversi karakter ASCII menjadi angka desimal, 
    # dengan masing-masing karakter dipisahkan oleh spasi.
    return " ".join(f"{ord(i):d}" for i in s)

print(convert_ascii("Hello world!"))
# Output:
# 72 101 108 108 111 32 119 111 114 108 100 33
# Ini menunjukkan bahwa karakter 'H' memiliki representasi numerik 72 (dalam desimal),
# karakter 'e' memiliki representasi numerik 101 (dalam desimal), dan seterusnya.

# program ini akan menampilkan pesan error
print(convert_ascii('hello world✨'))
# Output:
# Traceback (most recent call last):
#   File ".\convert_asciindec.py", line 20, in <module>                                                                                             00d\x00\x00\x00'
#     print(convert_ascii('hello world✨'))
#   File ".\convert_asciindec.py", line 8, in convert_ascii
#     raise ValueError("bukan tabel ascii")
# ValueError: bukan karakter ascii