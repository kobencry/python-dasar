# List Comprehension adalah jenis comprehension paling sering digunakan dalam Python. 
# List Comprehension membuat sebuah list baru dari suatu iterasi. 
# Misalnya, kita memiliki sebuah list angka dan ingin mencari angka yang lebih besar dari 10.
# Kita dapat menggunakan List Comprehension untuk mencapai hal tersebut dengan mudah seperti kode berikut ini:

# Syntax
# new_list = [expression for item in iterable]
listku = [i for i in range(1, 6)]
print(listku)
# Output:
# [1, 2, 3, 4, 5]

# kode ini setara dengan diatas
listku = []
for i in range(1, 6): # dimulai dari 1 sampai 5
    listku.append(i)
print(listku)
# Output:
# [1, 2, 3, 4, 5]


# menambahkan kondisional di akhir ekspresi
# Syntax
# new_list = [expression for item in iterable (if conditional)]

listku = [i for i in range(1, 11) if i > 5]
print(listku)
# Output:
# [6, 7, 8, 9, 10]

# kode ini setara dengan yang diatas
listku = []
for i in range(1, 11): # dimulai dari 1 sampai 10
    if i > 5:
        listku.append(i)
print(listku)
# Output:
# [6, 7, 8, 9, 10]

# menambahkan kondisional diawal ekspresi
# Syntax
# new_list = [(if conditional) for item in iterable]
listku = [f"{i} genap" if i %2==0 else f"{i} ganjil" for i in range(1, 6)]
print(listku)
# Output:
# ['1 ganjil', '2 genap', '3 ganjil', '4 genap', '5 ganjil']

# kode ini setara dengan diatas
listku = []
for i in range(1, 6): # dimulai dari 1 sampai 5
    if i %2==0:
        listku.append(f"{i} genap")
    else:
        listku.append(f"{i} ganjil")
print(listku)
# Output:
# ['1 ganjil', '2 genap', '3 ganjil', '4 genap', '5 ganjil']

# menambahkan kondisional diawal dan diakhir
# new_list = [(if conditional) for item in iterable (if conditional)]
alphabet = "A#Bcd@efG!"
listku = [f"{i} upper" if i.isupper() else f'{i} lower' for i in alphabet if i.isalpha()]
print(listku)
# Output:
# ['A upper', 'B upper', 'c lower', 'd lower', 'e lower', 'f lower', 'G upper']

# kode ini setara dengan diatas
listku = []
for i in alphabet:
    if i.isalpha():
        if i.isupper():
            listku.append(f"{i} upper")
        else:
            listku.append(f"{i} lower")
print(listku)
# ['A upper', 'B upper', 'c lower', 'd lower', 'e lower', 'f lower', 'G upper']