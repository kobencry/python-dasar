# argumen arbitrary/sewenang-wenang/semaunya *args
# Argument arbitrary/semaunya *args di Python adalah sebuah fitur yang memungkinkan
# Anda untuk menerima sejumlah argumen tak terbatas dalam fungsi. 
# Ini berguna ketika Anda tidak tahu berapa banyak argumen yang akan diterima oleh fungsi tersebut.

# Untuk menggunakan *args, Anda dapat menuliskannya di parameter fungsi diikuti dengan nama yang Anda inginkan.

def fungsiku(*args):
    # cetak panjang args
    print('panjang argumen:', len(args))
    # cetak tipe args
    print('tipe argumen:', type(args))
    # cetak isi args
    print('args:', args)

    # loop setiap elemen dalam tuple args
    for i in args:
        print(i)

fungsiku('alice', 'carl', 'eliot', 20, 28, 25)
# panjang argumen: 6
# tipe argumen: <class 'tuple'>
# args: ('alice', 'carl', 'eliot', 20, 28, 25)
# alice
# carl
# eliot
# 20
# 28
# 25

# penjelasan diatas:
# Ketika fungsi tersebut dipanggil, semua argumen yang dikirimkan ke fungsi 
# tersebut akan dikumpulkan ke dalam sebuah tuple bernama args. 
# Anda dapat mengakses setiap elemen dalam tuple tersebut seperti biasa, 
# misalnya dengan menggunakan for loop atau indeks tuple.
