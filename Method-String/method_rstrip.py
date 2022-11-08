# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=rstrip#str.rstrip

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi rstrip() menghapus semua karakter tambahan (karakter diakhir/dikanan string), 
# spasi adalah karakter tambahan default yang akan dihapus.

# Syntax
# string.rstrip(karakter)

# Nilai Parameter
# Parmeter                  Deskripsi
# karakter                  Opsional. Satu set karakter untuk dihapus sebagai karakter tambahan

x = "Hello    "
y = "Hello World..,.,!.,!" 
print(x.rstrip(), 'world') # Hello world
print(y.rstrip('.,!'))     # Hello World

x = "....hello world...."
print(x.rstrip('.'))    # ....hello world
