# Argument default pada fungsi di Python adalah sebuah fitur yang memungkinkan 
# Anda untuk memberikan nilai default untuk setiap parameter fungsi. 
# Ini berguna ketika Anda ingin mengijinkan pengguna fungsi untuk tidak 
# mengirimkan nilai untuk parameter tersebut, 
# sehingga fungsi akan menggunakan nilai default yang telah ditentukan.
# Untuk memberikan nilai default untuk parameter fungsi, Anda dapat menuliskannya
# setelah parameter diikuti dengan tanda sama dengan = dan nilai default yang diinginkan.

def fungsiku(nama='tidak ada', usia=0, alamat='-'):
    print(f"{nama}, {usia}, {alamat}")

fungsiku()
# tidak ada, 0, -

fungsiku('alice', 23)
# alice, 23, -

fungsiku('carl', 25, 'bandung')
# carl, 25, bandung

fungsiku(usia=23, alamat='jakarta')
# tidak ada, 23, jakarta

# fungsi ini akan, menjalankan loop jika kondisi True
def main(kondisi=None, angka=0):
    if kondisi == True:
        for i in range(angka):
            print(i)

    else:
        print("hello world")

main('alice', 5)
# hello world

main(True, 3)
# 0
# 1
# 2
