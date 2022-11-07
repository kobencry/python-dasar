# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=center#str.center

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi center() akan berpusat(ketengah) menyelaraskan string, menggunakan karakter tertentu 
# (defaultnya spasi) sebagai mengisi karakter.

# Syntax
# string.center(panjang, karakter_opsional)

# Nilai Parameter
# Parameter             Deskripsi
# panjang               panjang yang dibutuhkan. panjang string yang di kembalikan
# karakter              opsional. karakter untuk mengisi spasi yang hilang di setiap sisi. defaultnya adalah (spasi)

# menggunakan parameter panjang
x = "hello world".center(20)
print(x)    #     hello world    

# menggunakan parameter panjang dan karakter_opsional
y = "hello world".center(20, '#')
print(y)    # ####hello world#####

print(" HELLO WORLD ".center(20, '.'))  # ... HELLO WORLD ....


# Ingat: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.
s = "hello world"
# string melakukan perubahan
print(s.center(20, '%'))    # %%%%hello world%%%%%
# string tidak melakukan perubahan
print(s)    # hello world

# string tidak melakukan perubahan
s = "hello world"
s.center(20, '%')
print(s)    # hello world
