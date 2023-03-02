# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=isalpha#str.isalpha

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi isalpha() mengembalikan nilai boolean True jika semua karakter alfabet (a-z)
# contoh karakter yang bukan huruf abjad: angka (0-9) (spasi) !@#$%^()?[].;''"" dll

# Syntax
# string.isalpha()

# Nilai Parameter
# tidak ada nilai parameter

print("helloworld".isalpha())   
# Output:
# True

print("hello world".isalpha())  
# Output:
# False

x = "alice123"
print(x.isalpha())  
# Output:
# False

user = input("masukan alphabet (a-zA-Z): ")
# apakah variabel user memasukan huruf alphabet (a-zA-Z)?
if user.isalpha():  # jika kondisi True
    print("passed")
else: # jika kondisi False
    print("failed")