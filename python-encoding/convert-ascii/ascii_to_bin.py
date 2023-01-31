# mengubah karakter ascii ke bit/binary digits(basis 2)
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
    return " ".join(f"{ord(i):08b}" for i in s)

print(convert_ascii("Hello world!"))
# Output:
# 01001000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100 00100001
# Ini menunjukkan bahwa karakter 'H' memiliki representasi 01001000 (dalam bit),
# karakter 'e' memiliki representasi 01100101 (dalam bit), dan seterusnya.

# program ini akan menampilkan pesan error
print(convert_ascii('hello world✨'))
# Output:
# Traceback (most recent call last):
#   File ".\ascii_to_bin.py", line 20, in <module>
#     print(convert_ascii('hello world✨'))
#   File ".\ascii_to_bin.py", line 8, in convert_ascii
#     raise ValueError("bukan tabel ascii")
# ValueError: bukan karakter ascii