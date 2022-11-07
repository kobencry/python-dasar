# -- Method String --

# https://docs.python.org/3/library/stdtypes.html?highlight=count#str.count

# fungsi count() mengembalikan berapa kali nilai tertentu muncul dalam string.

# Syntax
# string.count(nilai, awal, akhir)

# Nilai Parameter
# Parameter         Deskripsi
# nilai             Dibutuhkan. Sebuah String. String ke nilai untuk mencari
# awal              Opsional. Sebuah Integer. Posisi untuk memulai pencarian. Defaultnya adalah 0
# akhir             Opsional. Sebuah Integer. Posisi untuk mengakhiri pencarian. Default adalah akhir dari string

# menggunakan parameter nilai
# ada berapakah jumlah nama alice?
x = "hei alice myalice hello alice worldalice".count('alice')
print(x)    # 4

# menggunakan parameter nilai, awal, dan akhir
# ada berapakah jumlah nama alice?
y = "hei alice myalice hello alice worldalice".count('alice', 10, 20)
print(y)    # 1
# parameter nilai 'alice'
# parameter awal 10, berarti dimulai dari huruf 'm' "ingat indeks string dimulai dari 0"
# parameter akhir 20, berarti diakhiri sampai huruf 'l'
# pencarian dimulai dari huruf 'm' lalu ketemu dengan kata myalice dan,
# pencarian berhenti di kata hello diakhiri huruf 'l'

# coba = "hei alice myalice hello alice worldalice"
# print(coba[10])
# print(coba[20])

print("hei alice myalice hello alice worldalice".count('alice', 10, 100))  # 3

# contoh nyata jika anda ingin mencari domain web tersebut dan menggantinya 
url = input("masukan host: ")
# https://www.python.org
# www.python.org

if url.count('https://') and url.count('www'):
    url = url.replace('www', 'docs')
else:
    url = 'https://' + url
    if url.count('www'):
        url = url.replace('www', 'docs', 1)
print(url)  # https://docs.python.org


# Ingat: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.
s = "hei alice myalice hello alice worldalice"
# string melakukan perubahan
print(s.count('alice', 10, 30))  # 2
# string tidak melakukan perubahan
print(s)    # "hei alice myalice hello alice worldalice"


# string tidak melakukan perubahan
s = "hei alice myalice hello alice worldalice"
s.count('alice', 10, 30)
print(s)    # "hei alice myalice hello alice worldalice"
