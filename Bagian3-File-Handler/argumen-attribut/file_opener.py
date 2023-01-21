# Argumen opener digunakan untuk memberikan fungsi yang digunakan untuk
# membuka file, sebagai gantinya untuk fungsi-bawaan open().
# Fungsi harus menerima path, mode dan buffering sebagai argumen dan mengembalikan file yang terbuka.

# fungsi-bawaan open() mengambil nama file dan mengembalikan objek file Python baru.
# Inilah yang Anda butuhkan di sebagian besar kasus.

# os.open() mengambil nama file dan mengembalikan file deskriptor baru. 
# Deskriptor file ini dapat diteruskan ke fungsi tingkat rendah lainnya, 
# seperti os.read() dan os.write(), atau untuk os.fdopen(), seperti yang dijelaskan di bawah ini. 
# Anda hanya memerlukan ini saat menulis kode yang bergantung pada API yang bergantung pada 
# sistem operasi, seperti menggunakan attribut O_EXCL ke open(2).

# os.fdopen() mengambil deskriptor file yang ada — biasanya dihasilkan oleh panggilan 
# sistem Unix seperti pipe() atau dup(), dan membuat objek file Python di sekitarnya.
# Secara efektif itu mengubah deskriptor file menjadi objek file penuh, 
# yang berguna saat berinteraksi dengan kode C atau dengan API yang hanya membuat deskriptor file tingkat rendah.

import os

# fungsi membuat file deskriptor tingkat OS
def opener(path: str, flags: int):
    '''mengambil nama file dan mengembalikan file deskriptor baru'''
    print(f"menggunakan fungsi {opener.__name__}...")
    return os.open(path, flags)

dataku = ('alice', 'carl', 'eliot')

# membuka file dengan mode 'w'(write/tulis)
with open('demo_opener.txt', mode='w', opener=opener) as f:
    print(f"menulis data ke file: {f.name}")
    # menulis data string ke file
    f.write("hello world\n")
    # menulis data string lain ke file
    for i in dataku:
        # menulis data dengan menggunakan argumen file pada fungsi-bawaan print()
        print(i, file=f)
    # menulis data string lain ke file
    f.write("ini adalah file demo opener")
# File akan ditutup secara otomatis setelah selesai mengolah.
print("kode program selesai.")

# Jika ingin mempelajari lebih lanjut tentang modul os kunjungi folder_name: "modul-os"
# Jika ingin mempelajari lebih lanjut tentang modul os kunjungi folder_name: "Fungsi-Bawaan/fungsi_print.py"