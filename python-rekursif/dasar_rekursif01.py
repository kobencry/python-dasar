# Fungsi rekursif adalah sebuah fungsi yang memanggil dirinya sendiri secara berulang 
# dalam proses pemrosesan.

# Berikut contoh fungsi rekursif yang terus memanggil dirinya sendiri tanpa kondisi berhenti:
def main():
    print("hello world")

    # memanggil dirinya sendiri
    main()

main()
# Output:
# hello world
# hello world
# hello world
# ....
# Traceback (most recent call last):
# ...
# RecursionError: maximum recursion depth exceeded while calling a Python object

# Program tersebut merupakan contoh dari fungsi "main" yang terus memanggil dirinya sendiri tanpa kondisi berhenti.
# Ketika fungsi main() dipanggil, ia akan mencetak "hello world" ke layar, dan kemudian memanggil dirinya sendiri lagi.
# Hal ini akan terus berulang sehingga akan mencetak "hello world" secara berulang kali tanpa berhenti.

# Namun, karena tidak ada kondisi berhenti yang ditentukan, 
# fungsi akan terus memanggil dirinya sendiri hingga mencapai batas maksimum rekursif
# yang telah ditentukan oleh Python. 
# Ketika batas tersebut tercapai, Python akan menganggapnya sebagai rekursif yang 
# berlebihan dan mengangkat exception/pengecualian RecursionError yang menunjukkan 
# bahwa batas maksimum rekursif telah terlampaui.

# Untuk menghindari RecursionError, penting untuk menentukan kondisi berhenti yang tepat dalam fungsi rekursif.
# Kondisi berhenti tersebut dapat berupa pengecekan pada parameter fungsi atau variabel yang mengubah perilaku rekursif
# agar akhirnya berhenti.