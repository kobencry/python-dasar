# Mode 'rb' (read binary) untuk membaca file dalam format biner.
#  Saat menggunakan mode ini, kita tidak dapat menulis atau mengubah isi dari file tersebut.

# Contoh penggunaan mode 'rb' pada objek file adalah sebagai berikut:
with open("file_gambar.png", mode='rb') as fileku:
    # membaca seluruh isi file gambar
    # print(fileku.read())

    # membaca sebanyak 20 bytes atau karakter dari file gambar
    print(fileku.read(20))
# File akan ditutup secara otomatis setelah selesai mengolah
# Output:
# b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\xc8'

# Baca file executable
with open("test.exe", mode='rb') as fileku:
    # membaca sebanyak 20 bytes atau karakter dari file exe
    print(fileku.read(20))
# Output:
# b'MZ\x90\x00\x03\x00\x00\x00\x04\x00\x00\x00\xff\xff\x00\x00\xb8\x00\x00\x00'

# membuka dengan mode 'rb+'
with





# fungsi untuk membaca isi file byte
def baca_file_byte(nama_file, nilai_byte):
    # membaca dengan mode 'rb'
    with open(nama_file, mode='rb') as fileku:
        # looping dengan while jika kondisi bernilai True
        while True:
            # membaca sebanyak 1 bytes atau karakter dari file
            data_byte = fileku.read(1)
            # periksa jika kondisi True masukan data ke keyword "yield"
            if data_byte:
                yield data_byte
            # jika kondisi diatas tidak terpenuhi jalankan kode program dibawah ini:
            else:
                break
            # periksa nilai_byte lebih besar dari 0
            if nilai_byte > 0:
                # nilai_byte akan di dekremen/dikurangi
                nilai_byte -= 1
                # periksa jika nilai_byte sama dengan 0 kode program berhenti
                if nilai_byte == 0:
                    break
# jalankan fungsi baca_file_byte() dengan forloop
for b in baca_file_byte("file_gambar.png", 20):
    i = int.from_bytes(b, 'big')
    print(f"raw: {b} \t- int: {i} \t- binary: {bin(i)}")
