# menggunakan fungsi rekursif
# Python juga menerima fungsi rekursif, yang berarti fungsi yang dapat memanggil dirinya sendiri.

# Rekursif adalah konsep matematika dan pemrograman yang umum. 
# Ini berarti bahwa suatu fungsi memanggil dirinya sendiri. 
# Ini bermanfaat karena Anda dapat mengulang data untuk mencapai hasil tanpa menggunakan while/for/loop.

# Bagi programer pemula/baru, perlu waktu untuk mengetahui cara kerjanya, 
# cara terbaik untuk mengetahuinya adalah dengan menguji dan memodifikasinya.

def rekursif(n):
    print(n)
    if n == 1:
        return 1
    else:
        return n + rekursif(n - 1)

print(rekursif(5))
# 5
# 4
# 3
# 2
# 1
# 15

# Catatan: bahwa sebuah fungsi rekursif harus memiliki kondisi berhenti 
# (dalam contoh di atas, kondisi berhenti adalah saat nilai argumen mencapai 1) agar tidak terjadi infinite recursion.

# "Infinite recursion adalah suatu keadaan di mana sebuah fungsi memanggil dirinya sendiri tanpa adanya kondisi berhenti.
# Ini dapat menyebabkan program mengalami crash atau menghabiskan seluruh sumber daya
# yang tersedia sehingga tidak dapat digunakan untuk mengeksekusi tugas lain. 
# Infinite recursion biasanya terjadi ketika sebuah fungsi tidak memiliki kondisi berhenti yang tepat,
# sehingga fungsi terus memanggil dirinya sendiri secara terus-menerus.
# Untuk menghindari infinite recursion, sebaiknya pastikan bahwa setiap fungsi rekursif memiliki kondisi berhenti yang tepat."

# menyimpulkan kembali kode diatas
def rekursif(n:int) -> 0:
    rekursif.__annotations__['return'] += 1
    print(f"memanggil fungsi {rekursif.__name__}() yang ke: {rekursif.__annotations__['return']} kali")
    print(f"{n} + {rekursif.__name__}({n} - 1) = {n}")

    # fungsi tersebut memeriksa apakah 'n' sama dengan 1. 
    # Jika ya, maka fungsi akan mengembalikan nilai 1 ('fungsi rekursif() akan berhenti')
    # Jika tidak, maka fungsi akan terus memanggil dirinya sendiri dengan nilai 'n' yang terus berkurang hingga 'n' menjadi 1.
    if n == 1:
        return 1

    # Jika 'n' tidak sama dengan 1, maka fungsi akan mengembalikan nilai 'n' 
    # ditambahkan dengan hasil pemanggilan kembali fungsi rekursif() dengan nilai n-1.
    else:
        return n + rekursif(n - 1) 
print(rekursif(5))

# jumlah fungsi rekursif() yang memanggil dirinya sendiri
print(f"total: {rekursif.__annotations__['return']}")


# penjelasan singkatnya, dari hasil outputnya seperti dibawah ini:
rekursif = 1
for n in range(1, 6): # cetak angka dimulai dari 1 - 5
    rekursif += n
    print(f"{n} + {rekursif - n} = {rekursif}")
# 1 + 0 = 1
# 2 + 1 = 3
# 3 + 3 = 6
# 4 + 6 = 10
# 5 + 10 = 15
