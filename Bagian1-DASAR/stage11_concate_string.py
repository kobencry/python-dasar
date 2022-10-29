# Penggabunagan string python

# untuk menggabungkan 2 string anda dapat menggunakan operator tambah (+)

x = "hello"
y = "world"
print(x + y)    # helloworld

# untuk menambahkan spasi diantara mereka, tambahkan " " atau ' '
x = "hello"
y = "world"
print(x + " " + y)  # hello world
print(x + ' ' + y)  # hello world

print("nama" + ": " + "alice")  # nama: alice
print("usia" + ": " + "23")     # usia: 23
# menampilkan kesalahan runtime
# print("noid" + ": " + 12345)    # error

# gunakan casting data dengan memanggil fungsi/konstraktor str()
print("noid" + ": " + str(12345))   # noid: 12345
