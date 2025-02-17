def addition(a,b):
    c = a + b
    print("Dodawanie", a, "i", b, "wynik to", c)
    return c

def demo(a,b):
    c = a+b
    d = a-b
    print("Dodawanie i odejmowanie", a, "i", b)
    return b,c

print(addition(3,5))
print(demo(3,2))
x, y = demo(4,7)
print(x, y)