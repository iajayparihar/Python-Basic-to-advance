class Simple:
    def __init__(self, *args):
        self.ans = 0
        if len(args) == 1:
            self.ans = 3.14*args[0]*args[0]
        elif len(args) == 2:
            self.ans = args[0]*args[1]
        elif len(args) == 3:
            self.ans = args[0]*args[1]*args[2]
        else:
            self.a = 1
            a = tuple(map(int, args))
            print(a)
            for i in a:
                self.a = self.a+a[i]


# __main__
k = Simple(2.5)
print("Area of Circle=", k.ans)
m = Simple(1.3, 4.2)
print("Area of rectangle is =", m.ans)
s = Simple(0.5, 2.2, 3.5)
print("Area of triangle=", s.ans)
sq = Simple(1, 3.5, 2.2, 3.5, 5, 1, 2.2)
print("Add only integer values =", sq.a)
