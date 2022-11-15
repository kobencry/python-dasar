# -- Fungsi bawaan python --

# https://docs.python.org/3/library/functions.html?highlight=built-function-type#type

# fungsi type() mengembalikan jenis objek yang ditentukan.

# Syntax
# type(object, bases, dict)

# Nilai Parameter
# Parameter         Deskripsi
# object            Dibutuhkan. Jika hanya satu parameter yang ditentukan, fungsi type() mengembalikan jenis objek ini
# bases             opsional. Menentukan kelas dasar/bases class
# dict              opsional. Menentukan namespace dengan definisi untuk class/kelas

s = "hello world"
i = 23
f = 5.20
b = 0b01001
h = 0xff
l = ["alice", "carl", "eliot"]
t = ("alice",)
d = {"nama":"alice", "usia":23}
st = {"alice", "carl", "eliot"}
bt = True
n = None


print(type(s))  # <class 'str'>
print(type(i))  # <class 'int'>
print(type(f))  # <class 'float'>
print(type(b))  # <class 'int'>
print(type(h))  # <class 'int'>
print(type(l))  # <class 'list'>
print(type(t))  # <class 'tuple'>
print(type(d))  # <class 'dict'>
print(type(st)) # <class 'set'>
print(type(bt)) # <class 'bool'>
print(type(n))  # <class 'NoneType'>

def main():
    return "hello world"

print(type(main))   # <class 'function'>
