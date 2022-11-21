# karakter pelarian python
# ntuk menyisipkan karakter yang ilegal dalam string, gunakan karakter escape.
# karakter escape adalah garis miring terbalik \ diikuti oleh karakter yang ingin Anda sisipkan.
# Contoh karakter ilegal adalah tanda kutip ganda di dalam string yang dikelilingi oleh tanda kutip ganda:

# tanda kutip ganda "
print("hello \"world\"")    # hello "world"
print('hello "world"')      # hello "world"

# tanda kutip tunggal '
print('hello \'world\'')    # hello 'world'
print("hello 'world'")      # hello 'world'

# \\ backslash
print('hello \\ world') # hello \ world
print('c:\\system32\\user\\python') # c:\system32\user\python
print('\\new line')

# \n new line
print("hello \nworld")

# \r carriage return
print("hello \rworld")  # world

# \t tab
print("hello \tworld")  # hello   world

# \b backspace
print("hello \bworld")  # helloworld
print("hello\bworld")   # hellworld

# \f form feed
print("hello \fworld")  # hello world     # hello \x0cworld
print("hello\fworld")   # helloworld      # hello\x0cworld

# \ooo oktal
print("\110\145\154\154\157\40\167\157\162\154\144")    # Hello world

# \xhh hexa
print("\x48\x65\x6c\x6f\x20\x77\x6f\x72\x6c\x64")   # Hello world

# jika ingin mempelajari lebih lanjut tentang encoding kunjungi folder_name:"python-encoding"



