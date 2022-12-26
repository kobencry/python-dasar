# Method isatty() mengembalikan nilai True jika perangkat tersebut merupakan terminal, dan False jika bukan.

# Syntax
# file.isatty()

# Nilai Parameter
# tidak ada nilai parameter

# membuka file dengan mode default 'r' (read/baca) atau 't' (text/teks)
with open('file.txt') as fileku:
    # print(fileku.isatty())
    # periksa apakah file merupakan terminal
    if fileku.isatty():
        print(f"{fileku.name} merupakan terminal")
    else:
        print(f"{fileku.name} bukan merupakan terminal")
# File akan ditutup secara otomatis setelah selesai mengolah


# Contoh yang merupakan file terminal adalah tty
# tty (Teletype) adalah sebuah file spesial yang merujuk ke terminal yang sedang digunakan.
# File tty biasanya terletak di direktori /dev/tty pada sistem operasi seperti-Unix, Linux atau macOS.
# Namun, pada sistem operasi Windows, file tty tidak tersedia.

# Pada sistem operasi Unix-seperti, terminal biasanya merupakan perangkat yang
# bertanggung jawab untuk menampilkan output dan menerima input dari pengguna.
# File tty dapat digunakan untuk mengakses terminal yang sedang digunakan, 
# sehingga kita dapat menuliskan output ke terminal atau membaca input dari terminal.

# Pada sistem operasi Windows tidak memiliki konsep file tty yang sama dengan sistem operasi seperti-Unix.
# Pada Windows, terminal biasanya disimulasikan oleh aplikasi Command Prompt atau PowerShell,
# yang dapat diakses melalui menu Start atau dengan mengetik perintah di dalam jendela Run.

# Untuk menuliskan output ke terminal atau membaca input dari terminal pada Windows, 
# kita dapat menggunakan perangkat-perangkat yang tersedia pada Python, 
# seperti sys.stdout (perangkat yang bertanggung jawab untuk menampilkan output pada terminal) 
# dan sys.stdin (perangkat yang bertanggung jawab untuk menerima input dari terminal). 
# Kita juga dapat menggunakan aplikasi-aplikasi tambahan seperti PIPE atau Winpty untuk mengakses terminal pada Windows dengan lebih mudah.

# Contoh jika anda menggunakan os linux atau macos
# jalankan program dibawah ini:
'''
with open('/dev/tty') as fileku:
    # print(fileku.isatty())
    # periksa apakah file merupakan terminal
    if fileku.isatty():
        print(f"{fileku.name} merupakan terminal")
    else:
        print(f"{fileku.name} bukan merupakan terminal")
# File akan ditutup secara otomatis setelah selesai mengolah
'''

# Contoh jika anda menggunakan os windows
import sys
# Mengecek apakah stdout (perangkat yang bertanggung jawab untuk menampilkan output pada terminal) merupakan terminal
if sys.stdout.isatty():
    print('stdout merupakan terminal')
else:
    print('stdout bukan merupakan terminal')

# Mengecek apakah stdin (perangkat yang bertanggung jawab untuk menerima input dari terminal) merupakan terminal
if sys.stdin.isatty():
    print('stdin merupakan terminal')
else:
    print('stdin bukan merupakan terminal')
# Output:
# stdout merupakan terminal
# stdin merupakan terminal
