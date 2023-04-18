# overriding ...
# coming soon

class A: #superclass
    # method instance
    def display(self):
        return "hello"

class B(A): #subclass
    # method instance
    def display(self):
        return f"{super().display()} world"

# membuat objek
b = B()
print(b.display())
# Output:
# hello world
