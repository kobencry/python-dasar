# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-ascii#ascii

# fungsi ascii() mengembalikan versi yang dapat dibaca dari objek apa pun (String, Tuple, List, dll).
# fungsi ascii() ini akan mengganti karakter non-ascii dengan karakter escape:
# å akan diganti dengan \xe5.

# Syntax
# ascii(objek)

# Nilai Parameter
# Parameter                 Deskripsi
# objek                     objek, seperti String, List, Tuple, Dict dll.

x = ascii("Hello ålice")
print(x)    # 'Hello \xe5lice'

emoji = ascii("🤨")
print(emoji)    # '\U0001f928'

alphabet = ascii("αβγδεζηθικλμνξοπρςστυφχψ")
print(alphabet)
# '\u03b1\u03b2\u03b3\u03b4\u03b5\u03b6\u03b7\u03b8\u03b9\u03ba\u03bb\u03bc\u03bd\u03be\u03bf\u03c0\u03c1\u03c2\u03c3\u03c4\u03c5\u03c6\u03c7\u03c8'

print(ascii("€"))   # '\u20ac'
