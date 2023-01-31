# mengubah karakter ascii ke octal(basis 8)
def convert_ascii(s):
    # Metod ini baru diperkenalkan pada Python 3.7 dan mengembalikan True jika semua karakter dalam string adalah ASCII.
    # menggunakan fungsi-string .isascii() untuk memastikan bahwa string input adalah ASCII.
    # buka folder python-string/metod_string file "metod_isascii.py"
    if not s.isascii():
        # Jika string bukan karakter ASCII, maka fungsi akan melemparkan error "ValueError" dengan pesan "bukan tabel ascii".
        raise ValueError("bukan karakter ascii")
    # Jika string hanya terdiri dari karakter ASCII, 
    # akan mengembalikan string hasil konversi karakter ASCII menjadi angka oktal, 
    # dengan masing-masing karakter dipisahkan oleh spasi.
    return " ".join(f"{ord(i):o}" for i in s)

print(convert_ascii("Hello world!"))
# Output:
# 110 145 154 154 157 40 167 157 162 154 144 41
# Ini menunjukkan bahwa karakter 'H' memiliki representasi numerik 110 (dalam octal),
# karakter 'e' memiliki representasi numerik 145 (dalam octal), dan seterusnya

# program ini akan menampilkan pesan error
#print(convert_ascii('hello world✨'))

# Output:
# Traceback (most recent call last):
#   File ".\ascii_to_oct.py", line 21, in <module>
#     print(convert_ascii('hello world✨'))
#   File ".\ascii_to_oct.py", line 8, in convert_ascii
#     raise ValueError("bukan karakter ascii")
# ValueError: bukan karakter ascii