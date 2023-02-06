# Set Comprehension adalah jenis comprehension yang digunakan untuk membuat sebuah set.
# Set Comprehension membuat sebuah set baru dari suatu iterasi.
# Misalnya, kita memiliki sebuah list angka dan ingin membuat set dari angka-angka tersebut.
# Kita dapat menggunakan Set Comprehension untuk mencapai hal tersebut seperti kode berikut ini:

# Syntax
# new_set = {expression for item in iterable}
setku = {i for i in range(1, 6)}
print(setku)
# Output:
# {1, 2, 3, 4, 5}

# kode ini setara dengan diatas
setku = set()
for i in range(1, 6): # dimulai dari 1 sampai 5
    setku.add(i)
print(setku)

# menambahkan kondisional di akhir ekspresi
# Syntax
# new_set = {expression for item in iterable (if conditional)}
setku = {i for i in range(1, 11) if i > 5}
print(setku)
# Output:
# {6, 7, 8, 9, 10}

# kode ini setara dengan diatas
setku = set()
for i in range(1, 11): # dimulai dari 1 sampai 10
    if i > 5:
        setku.add(i)
print(setku)
# Output:
# {6, 7, 8, 9, 10}

# menambahkan kodisional diawal ekspresi
# Syntax
# new_set = {(if conditional) for item in iterable}
setku = {f"{i} genap" if i %2==0 else f"{i} ganjil" for i in range(1, 6)}
print(setku)
# Output:
# {'3 ganjil', '4 genap', '2 genap', '5 ganjil', '1 ganjil'}
# jika anda outputnya berbeda, karna set() menyimpan himpunan elemen unik yang tidak berurutan.

# kode ini setara dengan diatas
setku = set()
for i in range(1, 6): # dimulai dari 1 sampai 5
    if i %2==0:
        setku.add(f"{i} genap")
    else:
        setku.add(f"{i} ganjil")
print(setku)
# Output:
# {'3 ganjil', '4 genap', '2 genap', '5 ganjil', '1 ganjil'}

# menambahkan kodisional diawal dan diakhir
# Syntax
# new_set = {(if conditional) for item in iterable (if conditional)}
alphabet = "A#Bcd@efG!"
setku = {f"{i} upper" if i.isupper() else f"{i} lower" for i in alphabet if i.isalpha()}
print(setku)
# Output:
# {'e lower', 'G upper', 'f lower', 'B upper', 'A upper', 'c lower', 'd lower'}
# jika anda outputnya berbeda, karna set() menyimpan himpunan elemen unik yang tidak berurutan.

# kode ini setara dengan diatas
setku = set()
for i in alphabet:
    if i.isalpha():
        if i.isupper():
            setku.add(f"{i} upper")
        else:
            setku.add(f"{i} lower")
print(setku)
# Output:
# {'B upper', 'G upper', 'c lower', 'A upper', 'e lower', 'f lower', 'd lower'}