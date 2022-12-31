# Method writable() mengembalikan nilai boolean True jika file dapat ditulis.
# Jika tidak maka akan mengembalikan nilai boolean False.
# File dapat ditulis dengan mode "a", "a+", "ab", "w", "w+", "wb"...dst yang mengandung mode (write/tulis)

# Syntax
# file.writable()

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode "w" (write/tulis)
with open("file_demo_writable.txt", "w") as fileku:
    # periksa apakah file dapat ditulis
    print("apakah file dapat ditulis:", fileku.writable())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# apakah file dapat ditulis: True

# membuka file dengan mode "a" (append/tambahkan)
with open("file_demo_writable.txt", "a") as fileku:
    # periksa dengan statemen if/else
    if fileku.writable():
        print("file dapat ditulis")
    else:
        print("file tidak dapat ditulis")
# File akan ditutup secara otomatis setelah selesai mengolah
# file dapat ditulis

# membuka file dengan mode "wb+" (write/tulis, binary/biner, append/tambahkan) 
with open("file_demo_writable.txt", "wb+") as fileku:
    print("apakah file dapat ditulis:", fileku.writable())
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# apakah file dapat ditulis: True
