# Operator walrus atau ':=' adalah operator baru yang ditambahkan ke dalam Python pada versi 3.8.
# Ini merupakan cara yang lebih efisien untuk menugaskan nilai ke dalam 
# variabel saat sekaligus melakukan ekspresi di dalam blok if atau while.
# Sebelumnya, Anda perlu menugaskan nilai ke dalam variabel terlebih dahulu sebelum menggunakannya dalam ekspresi.
# Dengan operator walrus, Anda dapat menulis kode Anda dengan lebih singkat dan ekspresif.

# Peringatan:
# saya berasumsi kalian sudah paham materi statement if/elif/else, forloop, whileloop, list, dict dan fungsi bawaan input().

# menggunakan operator walrus :=
print(x := "hello world")   # hello world
print(type(x))              # <class 'str'>
print(x == 'hello world')   # True

# tanpa operator walrus kita harus membuat dua baris.
y = "hello world"
print(y)    # hello world

# contoh kode biasa yang sering digunakan pada umumnya
# misalnya panjang username harus memiliki 4 karakter
username = ['alice', 'z', 'root', 'usr', 'carl', 'bin', 'eliot', 'ab']
for x in username:
    # panjang = len(x) # panjang karakter dari setiap username x
    # if panjang <= 3:
    #     print(f"username {x} memiliki {panjang} karakter")
    
    # kode ini setara dengan diatas
    if len(x) <= 3:
        print(f"username {x} memiliki {len(x)} karakter")
        # username z memiliki 1 karakter
        # username usr memiliki 3 karakter
        # username bin memiliki 3 karakter
        # username ab memiliki 2 karakter

# contoh menggunakan operator walrus ':='
for y in username:
    if (panjang := len(y)) <= 3:
        print(f"username {y} memiliki {panjang} karakter")
        # username z memiliki 1 karakter
        # username usr memiliki 3 karakter
        # username bin memiliki 3 karakter
        # username ab memiliki 2 karakter

# contoh kode biasa yang sering digunakan pada umumnya
# menampilkan daftar mahasiswa
mahasiswa = [
        {'nama':'alice', 'usia':23},
        {'nama':'carl', 'usia':26},
        {'nama':'eliot', 'usia':20}
        ]

for mhs in mahasiswa:
    # if mhs['nama'] is not None:
    #     print(f"{mhs['nama']} berusia {mhs['usia']}")
    
    # kode ini setara dengan diatas
    if mhs.get('nama') is not None:
        print(f"{mhs.get('nama')} berusia {mhs.get('usia')}")
        # alice berusia 23
        # carl berusia 26
        # eliot berusia 20

# contoh menggunakan operator walrus ':='
for mhs in mahasiswa:
    if (nama := mhs.get('nama')) and (usia := mhs.get('usia')) is not None:
        print(f"{nama} berusia {usia}")
        # alice berusia 23
        # carl berusia 26
        # eliot berusia 20

# Pada contoh di atas, kita mencari angka genap dalam variabel listku. 
# Dengan menggunakan operator walrus, kita dapat menulis kode yang lebih singkat dan ekspresif daripada sebelumnya.
# Dengan operator walrus, kita dapat menugaskan hasil ekspresi ke dalam 
# variabel 'kondisi' dan sekaligus menggunakannya dalam blok 'if'.


# jika masih bingung saya akan membuat beberapa contoh operator walrus

# contoh kode biasa yang sering digunakan pada umumnya
# jika user menulis 'quit' maka program akan 'break'
while True:
    user = input('Masukan sesuatu: ')
    if user == 'quit':
        break
    # cetak hasil dari inputan user
    print(user)


# contoh menggunakan operator walrus :=
while (user := input("Masukan sesuatu: ")) != 'quit':
    # cetak hasil dari inputan user
    print(user)
