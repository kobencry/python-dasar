# -- Fungsi bawaan python --

# fungsi input() memungkinkan input/masukan pengguna
# jika argumen prompt hadir, itu ditulis ke output standar tanpa tambahan baris baru/(\n).
# fungsi input() kemudian membaca baris dari input, mengubahnya menjadi string 
# (menghapus baris baru yang tertinggal), dan mengembalikannya. 

# Syntax
# input(prompt)

# Nilai Parameter
# Parameter         Deskripsi
# prompt            Sebuah String, mewakili pesan default sebelum input.

x = input('--> ')
print(x)

s = input("masukan nama: ")
print(type(s))
# pelajari lebih lanjut tentang fungsi-bawaan type() folder_name: "fungsi_type.py"

s = input("--> ").upper()
# pelajari lebih lanjut tentang fungsi-string upper() folder_name: "Method-String/fungsi_upper.py"
print(s)
