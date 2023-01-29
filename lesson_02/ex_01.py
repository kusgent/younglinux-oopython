# https://younglinux.info/oopython/objects

#1
class A:
    pass


a = A()
b = A()

# 2
class B:
    n = 5

    def adder(v):
        return v + B.n


print(B.n)
print(B.adder(4))

a = B()
b = B()
print(a.n)
print(a.n is B.n)

a.n = 10
print(a.n, b.n, B.n)
print(a.n is B.n)

B.n = 100
print(a.n, b.n, B.n)

# 3
