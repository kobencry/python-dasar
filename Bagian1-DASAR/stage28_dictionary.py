# python dictionary

# dictionary/kamus 
# dict digunakan untuk menyimpan nilai data dalam pasangan key/kunci:val/nilai.
# dict adalah kumpulan yang dipesan*, dapat diubah, dan tidak memungkinkan nilai duplikat/sama.

# dict ditulis dengan kurung kurawal, dan memiliki key/kunci dan val/nilai: {key:val}
dictku = {'nama':'alice', 'usia':23}
print(dictku)   # {'nama': 'alice', 'usia': 23}

# menggunakan konstruktor dict()
dictku = dict(nama='carl', usia=26)
print(dictku)   # {'nama': 'carl', 'usia': 26}

# dict tidak boleh memiliki item dengan key/kunci yang sama
dictku = {'nama':'alice', 'nama':'carl'}
# key/kunci yang duplikat/sama akan menimpa val/nilai yang ada.
print(dictku)   # {'nama': 'carl'}

# keys/kunci dan value/nilai dalam item dict dapat berupa tipe data apapun.
dictku = {'hello':'world', 10:'x', 2.5:'y', True:'t', False:'f', 0xff:'hexa', 0b10:'byte'}
print(dictku)   # {'hello': 'world', 10: 'x', 2.5: 'y', True: 't', False: 'f', 255: 'hexa', 2: 'byte'}

# Unordered berarti item tidak memiliki urutan yang ditentukan, 
# Anda tidak dapat merujuk ke item dengan menggunakan indeks.
# mengakses item dict dengan mengacu pada nama keys/kunci. 
dictku = {'nama':'alice', 'usia':23}
print(dictku['nama'])   # alice

# mengakses item dict dengan fungsi get()
dictku = {'nama':'carl', 'usia':23}
x = dictku.get('nama')
print(x)    # carl
print(dictku.get('usia'))   # 23

# menggunakan dict bersarang/nested
# dictionary dapat berisi dictionary, ini disebut dict bersarang.
# membuat dict yang berisi tiga dict
dictku = {
        'data1':{'nama':'alice', 'usia':23, 'alamat':'jakarta'},
        'data2':{'nama':'carl', 'usia':26, 'alamat':'bandung'},
        'data3':{'nama':'eliot', 'usia':22, 'alamat':'surabaya'}
        }
print(dictku)
# {'data1': {'nama': 'alice', 'usia': 23, 'alamat': 'jakarta'}, 'data2': {'nama': 'carl', 'usia': 26, 'alamat': 'bandung'}, 'data3': {'nama': 'eliot', 'usia': 22, 'alamat': 'surabaya'}}
print(dictku['data1']['nama'])          # alice
print(dictku.get('data2').get('nama'))  # carl

# mengubah nilai dict
dictku = {'nama':'alice', 'usia':23}
dictku['nama'] = 'hello'
print(dictku)   # {'nama': 'hello', 'usia': 23}

# menambahkan item dict
dictku = {'nama':'alice'}
dictku['usia'] = 23
print(dictku)   # {'nama': 'alice', 'usia': 23}

# menggunakan looping untuk mengakses semua key/kunci dict
dictku = {'nama':'alice', 'usia':23, 'alamat':'jakarta'}
for i in dictku:
    print(i)
# nama
# usia
# alamat

# memeriksa apakah keys/kunci 'usia' ada
dictku = {'nama':'alice', 'usia':23}
if 'usia' in dictku:
    print("passed")
else:
    print("failed")

# jika anda ingin mengetahui tentang operator python kunjungi folder_name: "python-operator"
