class decor:
    def __init__(self, a=None, b=None) :
        self.ans = a
        self.st = b
    @classmethod
    def add(cls, args):
        if len(args) == 2:
            return cls(args[0]+args[1])
        return f"string so not have same arguments."


# p = decor.add([1, 2])
# print(p.ans)

obj = decor()
obj.add([1,2])
print(obj.ans)

p = decor.add([1,2])
print(p.ans)
print(p.__dict__)