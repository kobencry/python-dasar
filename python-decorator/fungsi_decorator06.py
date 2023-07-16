# Dekorator identitas atau dekorator "kosong" adalah jenis dekorator 
# yang tidak melakukan perubahan atau penambahan apa pun pada fungsi yang didekorasi. 
# Dekorator semacam ini hanya mengembalikan fungsi aslinya tanpa melakukan manipulasi tambahan.

# Dekorator identitas sering digunakan untuk tujuan dokumentasi, 
# di mana dekorator digunakan untuk menandai atau memberikan label 
# pada fungsi tertentu agar dapat dikenali dan dipahami lebih baik oleh pengembang. 
# Misalnya, dekorator dapat digunakan untuk memberikan keterangan, metadata, atau penjelasan tambahan tentang fungsi tersebut.

# Selain itu, dekorator identitas juga dapat digunakan untuk mengelompokkan fungsi-fungsi dengan cara yang konsisten. 
# Misalnya, beberapa fungsi yang terkait atau memiliki karakteristik serupa dapat didekorasi 
# dengan dekorator identitas yang sama untuk memberikan keseragaman dalam kode.

# Namun, meskipun dekorator identitas atau "kosong" ini tidak melakukan perubahan yang signifikan 
# pada fungsi yang didekorasi, mereka masih mempertahankan kemampuan untuk memengaruhi perilaku 
# fungsi dengan memodifikasi argumen atau nilai kembalian fungsi.

# Berikut ini adalah contoh skrip kode untuk decorator identitas atau decorator "kosong" 
# yang hanya mengembalikan fungsi aslinya tanpa melakukan perubahan atau penambahan apa pun:
def root(func):
    return func

@root
def inputNama(nama):
    return f"Nama: {nama}"

@root
def inputUsia(usia):
    return f"Usia: {usia}"

@root
def inputEmail(email):
    return f"Email: {email}"

print(inputNama("alice"))
print(inputUsia(23))
print(inputEmail("alice@gmail.com"))

# Menampilkan isi dari dictionary row yang berisi nama-nama fungsi sebagai key dan 
# referensi ke fungsi-fungsinya sebagai value. 
# Setiap fungsi akan direpresentasikan dalam bentuk <function nama_fungsi at alamat_memori>, 
# di mana alamat memori merupakan alamat memori tempat fungsi tersebut disimpan.
row = {}

def main(func):
    row[func.__name__] = func
    return func

@main
def getNama(nama):
    return nama

@main
def getUsia(usia):
    return usia

print(row)
# Output:
# {'getNama': <function getNama at 0x000001B49E40A820>, 'getUsia': <function getUsia at 0x000001B49E40A8B0>}

# Dengan menggunakan dekorator dari fugsi "main" dan dictionary dari variabel "row", 
# kita dapat mengelompokkan dan mengakses fungsi-fungsi yang didefinisikan 
# dalam script dengan lebih terstruktur dan fleksibel.
print(row['getNama']('Alice'))
print(row['getUsia'](23))
# Output:
# Alice
# 23

# Dalam contoh di atas, kita dapat mengakses fungsi "getNama" dan "getUsia"
# melalui dictionary "row" dengan menggunakan nama fungsi sebagai key/kunci.
# Kita dapat memanggil fungsi-fungsi tersebut dengan memberikan argumen yang sesuai. 
# Pendekatan ini memungkinkan kita untuk mengelompokkan fungsi-fungsi terkait dan 
# mengaksesnya dengan cara yang lebih terstruktur dan fleksibel.