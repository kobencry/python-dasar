# Method readlines() adalah method yang terdapat pada objek file di Python, 
# yang digunakan untuk membaca seluruh baris dari file tersebut dan mengembalikannya dalam bentuk list dan karakter spesial \n(newline).
# Method ini berguna untuk membaca file yang terdiri dari beberapa baris teks, seperti file CSV atau file log.

# Syntax
# file.readlines(hint)

# Nilai Parameter
# Parameter                 Deskripsi
# hint                      Opsional.Jika jumlah byte yang dikembalikan melebihi jumlah petunjuk, tidak ada lagi baris yang akan dikembalikan. 
#                           Nilai default adalah -1, yang berarti semua baris akan dikembalikan.

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file_demo_readlines.txt') as fileku:
    isi_file_list = fileku.readlines()
    print(isi_file_list)
    # Output:
    # ['hello world\n', 'ini adalah file demo readlines\n']

    # karna tipe data list kita bisa indexing
    print(isi_file_list[0])
    # Output:
    # hello world

    for i in isi_file_list:
        # print(i)
        print(i, end='')
    # Output:
    # hello world
    # ini adalah file demo readlines
# File akan ditutup secara otomatis setelah selesai mengolah

# membuka file dengan mode 'r' (read/baca)
with open('file_demo_readlines.csv', 'r') as fileku:
    isi_file_list = fileku.readlines()
    print(isi_file_list)
    # Output:
    # ['nama,umur,jenis_kelamin\n', 'Alice,23,Perempuan\n', 'Bob,27,Laki-laki\n', 'Carl,25,Perempuan\n', 'Dom,28,Laki-laki\n', 'Eliot,22,Laki-laki\n']

    for i in isi_file_list:
        # print(i)
        print(i, end='')
    # Output:
    # nama,umur,jenis_kelamin
    # Alice,23,Perempuan
    # Bob,27,Laki-laki
    # Carl,25,Perempuan
    # Dom,28,Laki-laki
    # Eliot,22,Laki-laki
# File akan ditutup secara otomatis setelah selesai mengolah

# menggunakan parameter hint tidak menjamin bahwa jumlah baris yang dibaca
# akan sesuai dengan nilai yang diberikan, namun dapat memberikan performa yang 
# lebih baik jika diimplementasikan dengan benar.
with open('file_demo_readlines.csv') as fileku: # bebas anda ingin menggunakan file txt, csv, config, jpg, dll.
    # Memberikan petunjuk bahwa file tersebut terdiri dari 1 baris
    print(fileku.readlines(1))
    # Output:
    # ['nama,umur,jenis_kelamin\n']

    # Memberikan petunjuk bahwa file tersebut terdiri dari 2 sampai 4 baris
    for i in range(2,5): # mencetak mulai dari 2 - 4
        print(fileku.readlines(i))
    # Output:
    # ['Alice,23,Perempuan\n']
    # ['Bob,27,Laki-laki\n']
    # ['Carl,25,Perempuan\n']

# Catatan: Perlu diingat bahwa method readlines() akan membaca seluruh isi file ke dalam memory sekaligus, 
# sehingga tidak disarankan untuk digunakan pada file yang sangat besar karena dapat menyebabkan masalah pada kinerja sistem. 
