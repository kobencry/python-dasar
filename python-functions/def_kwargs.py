# Argumen arbitrary/sewenang-wenang/semaunya **kwargs
# Dalam bahasa Python, **kwargs adalah singkatan dari keyword arguments. 
# Ini adalah sebuah parameter tambahan yang dapat digunakan dalam fungsi Python 
# untuk menerima argumen berupa pasangan nilai-kunci (key-value). 
# Dengan menggunakan **kwargs, Anda dapat mengirim sejumlah argumen ke fungsi 
# dengan gaya yang sama seperti menggunakan dictionary, 
# dan Anda dapat mengakses argumen tersebut menggunakan kunci dari dictionary.

def fungsiku(**kwargs):
    # cetak panjang kwargs
    print('panjang argumen:', len(kwargs))
    # cetak tipe kwargs
    print('tipe argumen:', type(kwargs))
    # cetak isi kwargs
    print('kwargs:', kwargs)
    
    for i in kwargs:
        print(kwargs[i])

# mengirimkan argumen ke dalam fungsi menggunakan **kwargs
fungsiku(nama='alice', usia=23)
# panjang argumen: 2
# tipe argumen: <class 'dict'>
# kwargs: {'nama': 'alice', 'usia': 23}
# alice
# 23

# mengirimkan argumen ke dalam fungsi menggunakan **kwargs
fungsiku(nama='carl', usia=25, alamat='jakarta')
# panjang argumen: 3
# tipe argumen: <class 'dict'>
# kwargs: {'nama': 'carl', 'usia': 25, 'alamat': 'jakarta'}
# carl
# 25
# jakarta
