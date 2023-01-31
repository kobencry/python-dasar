# mengubah karakter ascii ke bit(binary digits)
def convert_ascii(s:str) -> str:
    # Metod ini baru diperkenalkan pada Python 3.7 dan mengembalikan True jika semua karakter dalam string adalah ASCII.
    # menggunakan fungsi-string .isascii() untuk memastikan bahwa string input adalah ASCII.
    # buka folder python-string/metod_string file "metod_isascii.py"
    if not s.isascii():
        # Jika string tidak ASCII, maka fungsi akan melemparkan error "ValueError" dengan pesan "bukan tabel ascii".
        raise ValueError("bukan tabel ascii")
    # Jika string input ASCII, maka fungsi akan menggunakan expression  generator bersama dengan metod join() 
    # untuk mengubah string menjadi representasi biner ASCII, 
    # dan masing-masing karakter akan dikonversi menggunakan fungsi-bawaan ord(). 
    # Setiap representasi biner akan dipisahkan oleh spasi.
    return " ".join(f"{ord(i):08b}" for i in s)

print(convert_ascii("Hello world!"))
# Output:
# 01001000 01100101 01101100 01101100 01101111 00100000 01110111 01101111 01110010 01101100 01100100 00100001