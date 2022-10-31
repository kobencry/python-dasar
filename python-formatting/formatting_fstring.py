# Jenis Pemformatan menggunakan f-string
# Di dalam placeholder {} Anda dapat menambahkan tipe pemformatan untuk memformat hasil

# contoh menggunakan f-string
print(f"{2*5} {'alice'} hello world")   # 10 alice hello world
x = 5
y = 'hello world'
print(f"nilai a:{x} nilai b: {y}")  # nilai x:5 nilai y: hello world

# :<
# rata kiri (dalam spasi yang tersedia)
nama = "alice"
usia = 23

txt = f"nama: {nama:<10} usia: {usia:<10}hello"
print(txt)      # nama: alice      usia: 23     hello


# :>
# rata kanan (dalam spasi yang tersedia)














# for i in range(1,10):
#     print(f"nilai: {i} persen %: {i:%}")

# for i in range(1, 10):
#     print(f"nilai: {i} persen %: {i:.0%}")
