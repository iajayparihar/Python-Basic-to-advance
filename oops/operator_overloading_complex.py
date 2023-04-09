class Complex:
    def __init__(self, x, y):
        self.real = x
        self.image = y

    def display(self):
        print("Real=", self.real)
        print("Image=", self.image)

    def __add__(self, m):
        t = Complex(0, 0)
        t.real = self.real+m.real
        t.image = self.image+m.image
        return t


# __main__
p = Complex(2.3, 3.2)
k = Complex(1.5, 3.1)
s = p+k
p.display()
k.display()
s.display()
