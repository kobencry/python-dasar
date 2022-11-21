# -- Method Tuple --

# fungsi count() mengembalikan berapa kali nilai tertentu yang muncul di tuple.

# Syntax
# tuple.count(nilai)

# Nilai Parameter
# Parameter             Deskripsi
# nilai                 Dibutuhkan. Item yang akan dicari

tupleku = (1, 2.5, 3, 5, 2.5, 10, 2.5)
print(tupleku.count(2.5))   # 3

tupleku = ('alice', 'carl', 'eliot', 'alice')
print(f"nama {tupleku[0]} berjumlah: {tupleku.count('alice')}")
# nama alice berjumlah: 2

# jika ingin mempelajari lebih lanjut tentang format string kunjungi folder_name: "python-formatting"
