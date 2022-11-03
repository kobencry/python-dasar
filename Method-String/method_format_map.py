# -- Method String --

# Catatan: 
# Semua method/metode/fungsi string mengembalikan nilai baru. 
# Mereka tidak mengubah string asli.

# fungsi format_map() digunakan untuk mengembalikan key=val dict.
# Di sini, mapping/pemetaan dapat berupa pemetaan apa pun, seperti dictionary. 
# Pemetaan dapat dilihat dalam bentuk {key: value}.
# ini akan mengembalikan string baru.

# Syntax
# string.format_map(dict_map)

# Nilai Parameter
# Parameter         Deskripsi
# dict_map          Dibutuhkan. nilai mapping/pemetaan dapat berupa pemetaan apapun, seperti dict.

dict_map = {"nama":'alice', "usia":23}
data_str = "nama: {nama} usia: {usia}"
print(data_str.format_map(dict_map))    # nama: alice usia: 23

data_mahasiswa = {"nama":['alice', 'carl', 'eliot'],
        "usia":[23, 27, 22],
        "jurusan":['teknik komputer', 'teknik mesin', 'teknik jaringan']}
table = "nama: {nama} \nusia: {usia} \njurusan: {jurusan}"
print(table.format_map(data_mahasiswa))
# nama: ['alice', 'carl', 'eliot']
# usia: [23, 27, 22]
# jurusan: ['teknik komputer', 'teknik mesin', 'teknik jaringan']

print("nama: {nama[0]} \nusia: {usia[0]} \njurusan: {jurusan[2]}".format_map(data_mahasiswa))
# nama: alice
# usia: 23
# jurusan: teknik jaringan

print("nama: {nama[2]} \nusia: {usia[1]} \njurusan: {jurusan[1]}".format_map(data_mahasiswa))
# nama: eliot
# usia: 27
# jurusan: teknik mesin
