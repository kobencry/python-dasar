# Penggabunagan string python

# untuk menggabungkan 2 string anda dapat menggunakan operator tambah (+)

x = "hello"
y = "world"
print(x + y)    # helloworld

x = "abc"
y = "123"
z = x + y
print(z)    # abc123

# untuk menambahkan spasi diantara mereka, tambahkan " " atau ' '
x = "hello"
y = "world"
print(x + " " + y)  # hello world
print(x + ' ' + y)  # hello world

print("nama" + ": " + "alice")  # nama: alice
print("usia" + ": " + "23")     # usia: 23
# menampilkan kesalahan runtime
# print("noid" + ": " + 12345)    # error

# menggunakan casting data dengan memanggil fungsi/konstraktor str()
print("noid" + ": " + str(12345))   # noid: 12345

# menggunakan fungsi-string format() 
# jika ingin mempelajari lebih lanjut tentang fungsi-string format() kunjungi folder_name: "python-formatting/formatting_format.py"
nama = "alice"
usia = 23
text = "nama: {} dan usia: {}"
print(text.format(nama, usia))      # nama: alice dan usia: 23
