# mengubah karakter ascii ke hexadecimal(basis 16)
def convert_ascii(s:str) -> str:
    # Metod ini baru diperkenalkan pada Python 3.7 dan mengembalikan True jika semua karakter dalam string adalah ASCII.
    # menggunakan fungsi-string .isascii() untuk memastikan bahwa string input adalah ASCII.
    # buka folder python-string/metod_string file "metod_isascii.py"
    if not s.isascii():
        # Jika string bukan karakter ASCII, maka fungsi akan melemparkan error "ValueError" dengan pesan "bukan tabel ascii".
        raise ValueError("bukan karakter ascii")
    # Jika string hanya terdiri dari karakter ASCII, 
    # akan mengembalikan string hasil konversi karakter ASCII menjadi angka hexadecimal, 
    # dengan masing-masing karakter dipisahkan oleh spasi.
    return " ".join(f"{ord(i):0x}" for i in s)

print(convert_ascii('Hello world!'))
# Output:
# 48 65 6c 6c 6f 20 77 6f 72 6c 64 21
# Ini menunjukkan bahwa karakter 'H' memiliki representasi numerik 48 (dalam hexadecimal),
# karakter 'e' memiliki representasi numerik 65 (dalam hexadecimal), dan seterusnya.

# program ini akan menampilkan pesan error
#print(convert_ascii('hello world✨'))

# Output:
# Traceback (most recent call last):
#   File ".\ascii_to_hex.py", line 22, in <module>
#     print(convert_ascii('hello world✨'))
#   File ".\ascii_to_hex.py", line 8, in convert_ascii
#     raise ValueError("bukan karakter ascii")
# ValueError: bukan karakter ascii